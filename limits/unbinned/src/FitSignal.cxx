#include "ParseUtils.h"
#include "SignalModel.h"

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
#include "RooPlot.h"
#include <map>

#include "TCanvas.h"
#include "FitUtils.h"
#include "TH1F.h"
#include "RooHistPdf.h"
#include "TLegend.h"
#include "TLatex.h"

using namespace std;
using namespace RooFit;

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
                 std::vector<double> &xsec, std::vector<double> &param) {
  ifstream fconfig(_config.c_str());
  std::string line;

  enum Section {SecNone = 0, SecFit, SecRegion, SecSample, SecSysts};
  Section sec = SecNone;

  while (std::getline(fconfig, line)) {
    std::stringstream ss (line);
    std::string first, second;
    ss >> first;
    ss >> second;
    std::string secondStr = second;//cleanQuotes(second);
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
  }
}

void draw(const std::string &outdir, \
          RooDataSet *adata, SignalModel *a, \
          RooDataSet *bdata, SignalModel *b, \
          const std::string &name, const std::string &channel, const std::string &syst,
          RooRealVar *x) {
  TCanvas *cs = new TCanvas("cs", "", 800, 600);
  TLegend l(0.7,0.7,0.89,0.89);
  l.SetBorderSize(0);
  RooPlot *framesig = x->frame(Title(Form("Signal (%s, %s, %s)", name.c_str(), channel.c_str(), syst.c_str())));
  adata->plotOn(framesig, LineColor(kRed), FillStyle(0), LineWidth(2), DrawOption("Z"), Name(Form("adata_%s%s%s", name.c_str(), channel.c_str(), syst.c_str())));
  a->getPdf()->plotOn(framesig, LineStyle(kDashed), LineColor(kRed), Name(Form("apdf_%s%s%s", name.c_str(), channel.c_str(), syst.c_str())));
  bdata->plotOn(framesig, LineColor(kBlue), FillStyle(0), LineWidth(2), DrawOption("Z"), Name(Form("bdata_%s%s%s", name.c_str(), channel.c_str(), syst.c_str())));
  b->getPdf()->plotOn(framesig, LineStyle(kDashed), LineColor(kBlue), Name(Form("bpdf_%s%s%s", name.c_str(), channel.c_str(), syst.c_str())));
  //sig->paramOn(framesig, Layout(lxmin,lxmax,0.9), ShowConstants(false), Format("NEU",AutoPrecision(1)));
  framesig->Draw();
  l.AddEntry(framesig->findObject(Form("adata_%s%s%s", name.c_str(), channel.c_str(), syst.c_str())), Form("Simulation for nominal"), "L");
  l.AddEntry(framesig->findObject(Form("apdf_%s%s%s", name.c_str(), channel.c_str(), syst.c_str())), Form("Fit for nominal"), "L");
  l.AddEntry(framesig->findObject(Form("bdata_%s%s%s", name.c_str(), channel.c_str(), syst.c_str())), Form("Simulation for syst. %s", syst.c_str()), "L");
  l.AddEntry(framesig->findObject(Form("bpdf_%s%s%s", name.c_str(), channel.c_str(), syst.c_str())), Form("Fit for syst. %s", syst.c_str()), "L");
  l.Draw();
  TLatex t;
  t.SetNDC();
  t.SetTextSize(0.02);
  float xs = 0.55;
  float ys = 0.55;
  float xs2 = 0.55;
  float ys2 = 0.55;
  if (a->m_param >= 2.5) {
    xs = 0.12;
    ys = 0.85;
  }
  for (size_t z = 0; z < a->m_fr->floatParsFinal().getSize(); ++z) {
    //t.DrawLatex(0.5, 0.55-0.05*z, Form("p%s_{nom} = %4.3e #pm %4.3e", ((RooAbsArg *) a->m_fr->floatParsFinal().at(z))->GetName(), ((RooRealVar *) a->m_fr->floatParsFinal().at(z))->getVal(), ((RooRealVar *) a->m_fr->floatParsFinal().at(z))->getError()));
    t.DrawLatex(xs, ys-0.04*z, Form("p%d_{nom}=%3.2e#pm%3.2e", (int) z, ((RooRealVar *) a->m_fr->floatParsFinal().at(z))->getVal(), ((RooRealVar *) a->m_fr->floatParsFinal().at(z))->getError()));
  }
  for (size_t z = 0; z < b->m_fr->floatParsFinal().getSize(); ++z) {
    //t.DrawLatex(0.6, 0.55-0.05*z, Form("%s_{%s} = %4.3e #pm %4.3e", ((RooAbsArg *) b->m_fr->floatParsFinal().at(z))->GetName(), syst.c_str(), ((RooRealVar *) b->m_fr->floatParsFinal().at(z))->getVal(), ((RooRealVar *) b->m_fr->floatParsFinal().at(z))->getError()));
    t.DrawLatex(xs2+0.18, ys2-0.04*z, Form("p%d_{%s}=%3.2e#pm%3.2e", (int) z, syst.c_str(), ((RooRealVar *) b->m_fr->floatParsFinal().at(z))->getVal(), ((RooRealVar *) b->m_fr->floatParsFinal().at(z))->getError()));
  }
  cs->SaveAs(Form("%s/signaldiff_%s_%s_%s.eps", outdir.c_str(), name.c_str(), channel.c_str(), syst.c_str()));
  delete cs;
}

int main(int argc, char **argv) {
  int help = 0;
  string _outdir = "results";
  string _config = "config_signal.txt";
  float _L = 20e3;

  static struct extendedOption extOpt[] = {
      {"help",            no_argument,       &help,   1, "Display help", &help, extendedOption::eOTInt},
      {"outdir",          required_argument,     0, 'd', "Output plot directory", &_outdir, extendedOption::eOTString},
      {"config",          required_argument,     0, 'c', "Config. file.", &_config, extendedOption::eOTString},
      {"L",               required_argument,     0, 'L', "Luminosity.", &_L, extendedOption::eOTFloat},
      {0, 0, 0, 0, 0, 0, extendedOption::eOTInt}
  };

  if (!parseArguments(argc, argv, extOpt) || help) {
    dumpHelp("FitSignal", extOpt, "FitSignal\nFit signal with all syst. uncertainties.\n");
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

  vector<std::string> name;
  vector<std::string> file;
  vector<double> xsec;
  vector<double> param;

  systs.push_back("");
  systs_suf1.push_back("");
  systs_suf2.push_back("");

  // read config file to determine channels, systs and names
  parseConfig(_config, channels, channels_hist, systs, systs_suf1, systs_suf2, name, file, xsec, param);

  RooWorkspace *work = new RooWorkspace("work");
  RooRealVar *x = new RooRealVar("x", "x", 0.0e3, 5e3);
  RooRealVar *w = new RooRealVar("w", "w", 1, 0, 100e3);
  RooRealVar *mu = new RooRealVar("mu", "mu", 1, 0, 10);
  work->import(*x);
  work->import(*w);
  work->import(*mu);

  std::map<std::string, SignalModel *> models;
  std::map<std::string, RooDataSet *> data;
  for (size_t z = 0; z < name.size(); ++z) {
    for (size_t zs = 0; zs < systs.size(); ++zs) {
      for (size_t zc = 0; zc < channels.size(); ++zc) {
        std::vector<std::string> systsud;
        systsud.push_back(systs[zs]);
        if (systs_suf2[zs] != "") systsud.push_back(Form("%sdw", systs[zs].c_str()));

        for (size_t zsd = 0; zsd < systsud.size(); ++zsd) {
          models.insert(std::make_pair<std::string, SignalModel *>(\
                  std::string(Form("%s_%s_%s", name[z].c_str(), channels[zc].c_str(), systsud[zsd].c_str())), \
                  new SignalModel(name[z], xsec[z], param[z], channels[zc], systsud[zsd], work)));
          RooDataSet *_data = 0;
	  if (zsd == 0) _data = readData(file[z].c_str(), channels_hist[zc], systs_suf1[zs], work, _L);
          else _data = readData(file[z].c_str(), channels_hist[zc], systs_suf2[zs], work, _L);

          data[Form("%s_%s_%s", name[z].c_str(), channels[zc].c_str(), systsud[zsd].c_str())] = _data;

          if (systsud[zsd] != "")
            models[Form("%s_%s_%s", name[z].c_str(), channels[zc].c_str(), systsud[zsd].c_str())]->readParameters(Form("%s/%s_%s_%s.txt", _outdir.c_str(), name[z].c_str(), channels[zc].c_str(), ""));

          models[Form("%s_%s_%s", name[z].c_str(), channels[zc].c_str(), systsud[zsd].c_str())]->fit(_data, _outdir);
          models[Form("%s_%s_%s", name[z].c_str(), channels[zc].c_str(), systsud[zsd].c_str())]->saveParameters(Form("%s/%s_%s_%s.txt", _outdir.c_str(), name[z].c_str(), channels[zc].c_str(), systsud[zsd].c_str()));
          draw(_outdir, \
             data[Form("%s_%s_%s", name[z].c_str(), channels[zc].c_str(), "")], \
             models[Form("%s_%s_%s", name[z].c_str(), channels[zc].c_str(), "")],
             data[Form("%s_%s_%s", name[z].c_str(), channels[zc].c_str(), systsud[zsd].c_str())], \
             models[Form("%s_%s_%s", name[z].c_str(), channels[zc].c_str(), systsud[zsd].c_str())], \
             name[z], channels[zc], systsud[zsd],\
             work->var("x"));
        }
      }
    }
  }


  return 0;
}

