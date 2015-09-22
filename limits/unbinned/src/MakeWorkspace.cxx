#include "ParseUtils.h"
#include "SignalModel.h"
#include "BkgModel.h"

#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <sstream>
#include <cmath>

#include "RooWorkspace.h"
#include "RooDataSet.h"
#include "RooRealVar.h"
#include "TTree.h"
#include "TFile.h"
#include "RooAbsPdf.h"
#include "RooGlobalFunc.h"

#include "RooSimultaneous.h"
#include "RooCategory.h"
#include "RooStats/ModelConfig.h"
#include "RooProdPdf.h"
#include "RooAddPdf.h"
#include "RooGaussian.h"
#include "RooConstVar.h"
#include "FitUtils.h"

#include "TStyle.h"
#include "TCanvas.h"
#include "TH2F.h"
#include "TGraphAsymmErrors.h"

#include "TLine.h"

using namespace std;
using namespace RooFit;
using namespace RooStats;

std::string cleanQuotes(const std::string &q) {
  size_t pos = 0;
  std::string out = "";
  int start = 0;
  while (pos < q.size()) {
    if (start == 0 && q[pos] == '"') {
      start = 1;
    } else if (start == 1 && q[pos] == '"') {
      start = 2;
    } else if (start == 1) {
      out += q[pos];
    }
    if (start == 2) break;
    pos++;
  }
  return out;
}

void parseConfig(const std::string &_config, \
                 std::vector<std::string> &channels, std::vector<int> &channels_hist, \
                 std::vector<std::string> &systs, std::vector<std::string> &systs_suf1, std::vector<std::string> &systs_suf2, \
                 std::vector<std::string> &name, std::vector<std::string> &file, \
                 std::vector<double> &xsec, std::vector<double> &param, \
                 double &systs_bkg) {
  ifstream fconfig(_config.c_str());
  std::string line;

  enum Section {SecNone = 0, SecFit, SecRegion, SecSample, SecSysts};
  Section sec = SecNone;

  while (std::getline(fconfig, line)) {
    std::stringstream ss (line);
    std::string first, second;
    ss >> first;
    ss >> second;
    std::string secondStr = cleanQuotes(second);
    if (first == "Fit:") {
      sec = SecFit;
    } else if (first == "Region:") {
      sec = SecRegion;
      channels.push_back(second);
    } else if (first == "Sample:") {
      sec = SecSample;
      name.push_back(second);
    } else if (first == "Systematic:") {
      sec = SecSysts;
      systs.push_back(second);
    }
    if (sec == SecRegion && first == "HistoName:") channels_hist.push_back(atoi(second.c_str()));
    if (sec == SecSample && first == "HistoFile:") file.push_back(secondStr);
    if (sec == SecSample && first == "Xsec:") xsec.push_back(atof(second.c_str()));
    if (sec == SecSample && first == "Param:") param.push_back(atof(second.c_str()));
    if (sec == SecSysts && first == "HistoNameSufUp:") systs_suf1.push_back(secondStr);
    if (sec == SecSysts && first == "HistoNameSufDown:") systs_suf2.push_back(secondStr);
    if (sec == SecFit && first == "BkgSyst:") systs_bkg = atof(second.c_str());
  }
}


int main(int argc, char **argv) {
  int help = 0;
  string _outdir = "results";
  string _config = "config_signal.txt";
  string name = "zp2tev";
  int _nosyst = 0;
  float _L = 1.0;
  string _data = "";

  static struct extendedOption extOpt[] = {
      {"help",            no_argument,       &help,   1, "Display help", &help, extendedOption::eOTInt},
      {"name",            required_argument,     0, 'n', "Name of signal to use in model.", &name, extendedOption::eOTString},
      {"outdir",          required_argument,     0, 'd', "Output plot directory", &_outdir, extendedOption::eOTString},
      {"config",          required_argument,     0, 'c', "Config. file.", &_config, extendedOption::eOTString},
      {"nosyst",          required_argument,     0, 'N', "Disable all systs.", &_nosyst, extendedOption::eOTInt},
      {"L",               required_argument,     0, 'L', "Luminosity to apply on loaded data.", &_L, extendedOption::eOTFloat},
      {"data",            required_argument,     0, 'D', "Data.", &_data, extendedOption::eOTString},
      {0, 0, 0, 0, 0, 0, extendedOption::eOTInt}
  };

  if (!parseArguments(argc, argv, extOpt) || help) {
    dumpHelp("MakeWorkspace", extOpt, "MakeWorkspace\nUse result of FitSignal in outdir to prepare a RooFit workspace for the limit setting with all systematics.\n");
    return 0;
  } else {
    std::cout << "Dumping options:" << std::endl;
    dumpOptions(extOpt);
  }

  vector<std::string> channels;
  vector<int> channels_hist;

  vector<std::string> systs;
  vector<std::string> systs_suf1;
  vector<std::string> systs_suf2;

  vector<std::string> nameList;
  vector<std::string> file;
  vector<double> xsec;
  vector<double> param;
  double systs_bkg = -1;

  systs.push_back("");
  systs_suf1.push_back("");
  systs_suf2.push_back("");

  // read config file to determine channels, systs and names
  parseConfig(_config, channels, channels_hist, systs, systs_suf1, systs_suf2, nameList, file, xsec, param, systs_bkg);

  if (_nosyst == 1) {
    systs.clear();
    systs_suf1.clear();
    systs_suf2.clear();

    systs.push_back("");
    systs_suf1.push_back("");
    systs_suf2.push_back("");
    systs_bkg = -1;
  }

  RooWorkspace *work = new RooWorkspace("work");
  RooRealVar *x = new RooRealVar("x", "x", 1.0e3, 4.1e3);
  RooRealVar *w = new RooRealVar("w", "w", 1, 0, 100e3);
  RooRealVar *mu = new RooRealVar("mu", "mu", 0, 0, 100);
  work->import(*x);
  work->import(*w);
  work->import(*mu);

  RooCategory *idx = new RooCategory("channel", "channel");
  for (size_t z = 0; z < channels.size(); ++z) {
    idx->defineType(channels[z].c_str(), channels_hist[z]);
  }

  std::map<std::string, BaseSignalModel *> models;
  std::map<std::string, BkgModel *> bkg;

  for (size_t zs = 0; zs < systs.size(); ++zs) {
    for (size_t zc = 0; zc < channels.size(); ++zc) {
      std::vector<std::string> systsud;
      systsud.push_back(systs[zs]);
      if (systs_suf2[zs] != "") systsud.push_back(Form("%sdw", systs[zs].c_str()));

      for (size_t zsd = 0; zsd < systsud.size(); ++zsd) {
        models.insert(std::make_pair<std::string, SignalModel *>(\
              std::string(Form("%s_%s_%s", name.c_str(), channels[zc].c_str(), systsud[zsd].c_str())), \
              new SignalModel(name, xsec[zc], param[zc], channels[zc], systsud[zsd], work)));
        models[Form("%s_%s_%s", name.c_str(), channels[zc].c_str(), systsud[zsd].c_str())]->readParameters(Form("%s/%s_%s_%s.txt", _outdir.c_str(), name.c_str(), channels[zc].c_str(), systsud[zsd].c_str()));
      }
    }
  }

  for (size_t zc = 0; zc < channels.size(); ++zc) {
    bkg.insert(std::make_pair<std::string, BkgModel *>(\
            std::string(Form("%s", channels[zc].c_str())), \
            new BkgModel("bkg", 1.0, -1.0, channels[zc], "", work)));
  }

  RooArgSet nuisParam("nuisParam");
  RooArgSet globalObs("globalObs");

  std::vector<RooRealVar *> alpha;
  std::vector<RooRealVar *> cons;
  std::map<std::string, std::map<std::string, std::map<std::string, double> > > delta_p;

  for (size_t z = 1; z < systs.size(); ++z) {
    alpha.push_back(new RooRealVar(Form("a_%s", systs[z].c_str()), "", -1, 1));
    nuisParam.add(*alpha[z-1]);

    //RooRealVar *mean = new RooRealVar(Form("nom_a_%s", systs[z].c_str()), "", 0);
    //mean->setConstant(true);
    //cons.push_back(mean);
    //globalObs.add(*mean);
  }
  if (systs_bkg > 0) {
    alpha.push_back(new RooRealVar(Form("a_%s", "bkg"), "", -2, 2));
    nuisParam.add(*alpha[alpha.size()-1]);

    //RooRealVar *mean = new RooRealVar(Form("nom_a_%s", "bkg"), "", 0);
    //mean->setConstant(true);
    //cons.push_back(mean);
    //globalObs.add(*mean);
  }

  // for each signal sample, make a workspace
  map<string, RooAbsPdf *> jointMap;
  for (size_t zc = 0; zc < channels.size(); ++zc) {
    delta_p[channels[zc]] = std::map<std::string, std::map<std::string, double> >();

    RooArgSet ctr_local;

    SignalModel *s_n = (SignalModel *) models[Form("%s_%s_%s", name.c_str(), channels[zc].c_str(), "")];
    BkgModel *b_n = bkg[Form("%s", channels[zc].c_str())];

    // make new models to add systs.
    s_n->getParamWithSystematics(alpha, systs, models, delta_p[channels[zc]]);
    RooAbsPdf *s = s_n->getPdfWithSystematics();
    RooAbsPdf *b = b_n->getPdf();

    // load bkg parameters
    RooRealVar *nbkg = new RooRealVar(Form("nbkg_%s", channels[zc].c_str()), "nbkg", 0, 1e6);
    nbkg->setConstant(false);
    nuisParam.add(*nbkg);
    
    RooRealVar *p1 = b_n->param("p1");
    RooRealVar *p2 = b_n->param("p2");
    //RooRealVar *p3 = b_n->param("p3");
    //RooRealVar *p4 = b_n->param("p4");
    p1->setConstant(false);
    p2->setConstant(false);
    //p3->setConstant(false);
    //p4->setConstant(false);
    nuisParam.add(*p1);
    nuisParam.add(*p2);
    //nuisParam.add(*p3);
    //nuisParam.add(*p4);

    RooFormulaVar *nsig_mu = 0;
    if (systs_bkg > 0) {
      nsig_mu = new RooFormulaVar(Form("fnsig_mu_%s", channels[zc].c_str()), "(@0*@1 + @2*@3)", \
                         RooArgList(*s_n->systParam("norm"), *work->var("mu"), *alpha[alpha.size()-1], RooConst(systs_bkg)));
    } else {
      nsig_mu = new RooFormulaVar(Form("fnsig_mu_%s", channels[zc].c_str()), "@0*@1", \
                         RooArgList(*s_n->systParam("norm"), *work->var("mu")));
    }

    RooAddPdf *model = new RooAddPdf(Form("model_%s", channels[zc].c_str()), "model", RooArgList(*b, *s), RooArgList(*nbkg, *nsig_mu));
    //jointMap[channels[zc]] =  model;

    for (size_t z = 1; z < systs.size(); ++z) {
      //RooAbsPdf *gaussian = new RooGaussian(Form("const_%s_%s", systs[z].c_str(), channels[zc].c_str()), "constraint", *alpha[z-1], *cons[z-1], RooConst(1));
      RooAbsPdf *gaussian = new RooGaussian(Form("const_%s_%s", systs[z].c_str(), channels[zc].c_str()), "constraint", *alpha[z-1], RooConst(0), RooConst(1));
      ctr_local.add(*gaussian);
    }
    RooAbsPdf *gaussian_bkg = 0;
    if (systs_bkg > 0) {
      //gaussian_bkg = new RooGaussian(Form("const_%s_%s", "bkg", channels[zc].c_str()), "constraint", *alpha[alpha.size()-1], *cons[alpha.size()-1], RooConst(1));
      gaussian_bkg = new RooGaussian(Form("const_%s_%s", "bkg", channels[zc].c_str()), "constraint", *alpha[alpha.size()-1], RooConst(0), RooConst(1));
      ctr_local.add(*gaussian_bkg);
    }
    ctr_local.add(*model);

    RooProdPdf *model_const = new RooProdPdf(Form("model_%s_const", channels[zc].c_str()), "model constrained", ctr_local);
    jointMap[channels[zc]] =  model_const;
  }
  RooSimultaneous *jointModel = new RooSimultaneous("combined", "combined model", jointMap, *idx);

  //RooArgSet ctr;
  //for (size_t z = 1; z < systs.size(); ++z) {
  //  RooRealVar *mean = new RooRealVar(Form("nom_a_%s", systs[z].c_str()), "", 0);
  //  mean->setConstant(true);
  //  RooAbsPdf *gaussian = new RooGaussian(Form("const_%s", systs[z].c_str()), "constraint", *alpha[z-1], *mean, RooConst(1));
  //  ctr.add(*gaussian);
  //  globalObs.add(*mean);
  //}
  //if (systs_bkg > 0) {
  //  RooRealVar *mean = new RooRealVar(Form("nom_a_%s", "bkg"), "", 0);
  //  mean->setConstant(true);
  //  RooAbsPdf *gaussian = new RooGaussian(Form("const_%s", "bkg"), "constraint", *alpha[alpha.size()-1], *mean, RooConst(1));
  //  ctr.add(*gaussian);
  //  globalObs.add(*mean);
  //}
  //RooSimultaneous *jointModel_no_const = new RooSimultaneous("combined_no_const", "combined no constrains", jointMap, *idx);
  //ctr.add(*jointModel_no_const);
  //RooProdPdf *jointModel = new RooProdPdf("combined", "combined", ctr);

  work->import(*jointModel);
  work->defineSet("nuisParams",nuisParam);
  work->defineSet("globalObs",globalObs);

  ModelConfig *mc = new ModelConfig("ModelConfig", work);
  mc->SetPdf(*jointModel);
  mc->SetParametersOfInterest(*work->var("mu"));
  mc->SetObservables(RooArgSet(*work->var("x"), *work->cat("channel")));
  mc->SetSnapshot(*work->var("mu"));
  mc->SetNuisanceParameters(*work->set("nuisParams"));
  mc->SetGlobalObservables(*work->set("globalObs"));
  work->import(*mc);

  if (_data != "") {
    RooDataSet *data = new RooDataSet("data", "", RooArgSet(*work->var("x"), *work->cat("channel"), *work->var("w")), WeightVar(*work->var("w")));
    readData(data, _data, -1, "", work, _L, true);
    work->import(*data);
  }

  work->writeToFile(Form("%s/workspace_%s.root", _outdir.c_str(), name.c_str()), true); 

  gStyle->SetOptStat(0);
  for (size_t zc = 0; zc < channels.size(); ++zc) {
    for (std::map<std::string, std::map<std::string, double> >::iterator itp = delta_p[channels[zc]].begin(); itp != delta_p[channels[zc]].end(); ++itp) {
      TCanvas *cn = new TCanvas("cn", "", 500, 600);
      cn->SetLeftMargin(0.2);
      cn->SetBottomMargin(0.20);
      TH2F *hn = new TH2F("hn", Form(" ; #Delta p(%s,channel=%s) ; ", itp->first.c_str(), channels[zc].c_str()), 10, -1, 1, systs.size(), 0.0, 1.0*systs.size());
    
      for (size_t z = 0 ; z < systs.size(); ++z) {
        hn->GetYaxis()->SetBinLabel(z+1, systs[z].c_str());
      }
      hn->GetYaxis()->SetTitleSize(0.05);
      hn->GetXaxis()->SetTitleSize(0.05);
      hn->GetYaxis()->SetTitleFont(42);
      hn->GetXaxis()->SetTitleFont(42);
      hn->GetYaxis()->SetTitleOffset(1.8);
      hn->Draw("hist");
      TGraphAsymmErrors *nps = new TGraphAsymmErrors(systs.size());
      for (std::map<std::string, double>::iterator its = itp->second.begin(); its != itp->second.end(); ++its) {
        std::cout << "  |--> delta p(" << itp->first << ", " << channels[zc] << ", " << its->first << ") = " << its->second << std::endl;
        int idx = std::find(systs.begin(), systs.end(), its->first) - systs.begin();
        if (its->first == "") idx = 0;
        if (std::fabs(its->second) < 1e-3) {
          nps->SetPoint(idx, 0, 1.0*idx+0.5);
          nps->SetPointError(idx, 0, 0, 0, 0);
        } else if (its->second > 0) {
          nps->SetPoint(idx, its->second, 1.0*idx+0.5);
          nps->SetPointError(idx, its->second, 0, 0, 0);
        } else {
          nps->SetPoint(idx, its->second, 1.0*idx+0.5);
          nps->SetPointError(idx, 0, std::fabs(its->second), 0, 0);
        }
      }

      nps->SetLineWidth(3);
      nps->SetMarkerStyle(21);
      nps->SetMarkerColor(4);
      nps->SetMarkerSize(0.8);
      TLine lin(0, 0, 0, 1.0*systs.size());
      lin.SetLineWidth(2);
      lin.SetLineStyle(kDashed);
      lin.SetLineColor(kRed);
      lin.Draw();
      nps->Draw("P");

      cn->SaveAs(Form("%s/syst_deltap_%s_%s_%s.eps", _outdir.c_str(), name.c_str(), itp->first.c_str(), channels[zc].c_str()));
      delete cn;
      delete hn;
      delete nps;
    }
  }

  return 0;
}

