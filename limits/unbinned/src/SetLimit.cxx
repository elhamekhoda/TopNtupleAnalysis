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

#include "TCanvas.h"
#include "TAxis.h"
#include "RooStats/ModelConfig.h"
#include "RooCategory.h"
#include "TGraph.h"
#include "TGraphErrors.h"
#include "TGraphAsymmErrors.h"
#include "TLine.h"
#include "TMath.h"
#include "FitUtils.h"
#include "RooStats/AsymptoticCalculator.h"
#include "RooStats/HypoTestInverter.h"
#include "RooStats/HypoTestInverterResult.h"
#include "RooStats/HypoTestInverterPlot.h"
#include "TLegend.h"

#include "runAsymptoticsCLs.C"

using namespace std;
using namespace RooFit;
using namespace RooStats;

int main(int argc, char **argv) {
  int help = 0;
  string _outdir = "results";
  string _workspace = "results/workspace_zp2tev.root";
  string _data = "data.root";
  string _signal = "ttres_new/zp2tev.root";
  float _sigweight = 0.0;
  string _poiscan = "0:40:2.0";
  float _L = 20e3;
  string _suffix = "zp2tev";
  int _external = 0;

  static struct extendedOption extOpt[] = {
      {"help",            no_argument,       &help,   1, "Display help", &help, extendedOption::eOTInt},
      {"outdir",          required_argument,     0, 'd', "Output plot directory", &_outdir, extendedOption::eOTString},
      {"workspace",       required_argument,     0, 'w', "Workspace file", &_workspace, extendedOption::eOTString},
      {"data",            required_argument,     0, 'f', "Data input file", &_data, extendedOption::eOTString},
      {"signal",          required_argument,     0, 's', "Signal input file", &_signal, extendedOption::eOTString},
      {"sigweight",       required_argument,     0, 'S', "Signal weight", &_sigweight, extendedOption::eOTFloat},
      {"poiscan",         required_argument,     0, 'p', "PoI scan range in format MIN:NBINS:MAX", &_poiscan, extendedOption::eOTString},
      {"L",               required_argument,     0, 'L', "Luminotisty to multiply data.", &_L, extendedOption::eOTFloat},
      {"suffix",          required_argument,     0, 'n', "Suffix for output files", &_suffix, extendedOption::eOTString},
      {"external",        required_argument,     0, 'e', "Run external macro.", &_external, extendedOption::eOTInt},
      {0, 0, 0, 0, 0, 0, extendedOption::eOTInt}
  };

  if (!parseArguments(argc, argv, extOpt) || help) {
    dumpHelp("SetLimits", extOpt, "SetLimits\nDo limit setting.\n");
    return 0;
  } else {
    std::cout << "Dumping options:" << std::endl;
    dumpOptions(extOpt);
  }

  std::vector<double> poiList;
  for (size_t i = 0,n; i <= _poiscan.length(); i=n+1) {
    n = _poiscan.find_first_of(':',i);
    if (n == std::string::npos)
      n = _poiscan.length();
    std::string tmp = _poiscan.substr(i,n-i);
    poiList.push_back(atof(tmp.c_str()));
  }

  if (_external) {
    runAsymptoticsCLs(_workspace.c_str(),               // file
                      "work",                           // workspace name
                      "ModelConfig",                    // ModelConfig object name
                      "data",                           // dataset name
                      "",                               // asimov data name
                      _outdir.c_str(),                  // directory name
                      std::string("extlimit_")+_suffix, // file name to save results on
                      0.95);                            // set 95% CL limits
    return 0;
  }

  TFile f(_workspace.c_str());
  RooWorkspace *work = (RooWorkspace *) f.Get("work");

  RooRealVar *mu = work->var("mu");
  RooCategory *idx = work->cat("channel");
  RooRealVar *x = work->var("x");

  ModelConfig *mc = (ModelConfig*)work->obj("ModelConfig");

  // get the modelConfig (S+B) out of the file
  // and create the B model from the S+B model
  ModelConfig*  sbModel = (ModelConfig *) mc->Clone();
  sbModel->SetName("S+B Model");      
  RooRealVar* poi = (RooRealVar*) sbModel->GetParametersOfInterest()->first();
  poi->setVal(1);  // set POI snapshot in S+B model for expected significance
  sbModel->SetSnapshot(*poi);
  ModelConfig * bModel = (ModelConfig*) sbModel->Clone();
  bModel->SetName("B Model");      
  poi->setVal(0);
  bModel->SetSnapshot( *poi  );

  //mu->setVal(0);
  //RooArgSet allParams(*(bModel->GetSnapshot()));
  //allParams.add(*work->set("nuisParams"));
  //RooArgSet globalObs("gO");
  //globalObs.add(*work->set("globalObs"));
  //RooAbsData *data = AsymptoticCalculator::MakeAsimovData(*bModel, allParams, globalObs); 

  RooDataSet *data = new RooDataSet("data", "", RooArgSet(*work->var("x"), *work->cat("channel"), *work->var("w")), WeightVar(*work->var("w")));
  readData(data, _data, -1, "", work, _L, true);
  if (_sigweight > 0)
    readData(data, _signal, -1, "", work, _L*_sigweight, true);

  // set syst. params. to zero
  RooRealVar *par = 0;
  RooFIter pi = work->set("nuisParams")->fwdIterator();
  while ( (par = (RooRealVar *) pi.next()) ) {
    if (std::string(par->GetName()).find("a_") != std::string::npos) {
      std::cout << "Setting " << par->GetName() << " to zero." << std::endl;
      par->setVal(0);
      //par->setConstant(true);
    }
  }
  work->var("mu")->setVal(0);

  double p = 1;
  double expP = p;

  int npointsa = (int) std::floor(poiList[1]);  // number of points to scan
  // min and max (better to choose smaller intervals)
  double poimina = poiList[0];
  double poimaxa = poiList[2];


  /*
  AsymptoticCalculator::SetPrintLevel(-1);
  ROOT::Math::MinimizerOptions::SetDefaultMinimizer("Minuit");
  ROOT::Math::MinimizerOptions::SetDefaultStrategy(0);
  
  AsymptoticCalculator  *acl = new AsymptoticCalculator(*data, *bModel, *sbModel);
  acl->SetOneSided(true);  // for one-side tests (limits)
  HypoTestInverter calc(*acl);    // for asymptotic
  calc.SetConfidenceLevel(0.95);
  // for CLS
  bool useCLs = true;
  calc.UseCLs(useCLs);

  calc.SetFixedScan(npointsa,poimina,poimaxa);
  //calc.SetAutoScan();
  
  HypoTestInverterResult * r = calc.GetInterval();
  double upperLimit = r->UpperLimit();
  
  std::cout << "mu = " << mu->getVal() << std::endl;

  std::cout << "The computed upper limit is: " << upperLimit << std::endl;
  // compute expected limit
  std::cout << "Expected upper limits in mu, using the B (alternate) model : " << std::endl;
  std::cout << " expected limit (median) " << r->GetExpectedUpperLimit(0) << std::endl;
  std::cout << " expected limit (-1 sig) " << r->GetExpectedUpperLimit(-1) << std::endl;
  std::cout << " expected limit (+1 sig) " << r->GetExpectedUpperLimit(1) << std::endl;

  // plot now the result of the scan 
  TCanvas *cscan = new TCanvas("cscan", "", 800, 600);
  HypoTestInverterPlot *plot = new HypoTestInverterPlot("HTI_Result_Plot","HypoTest Scan Result",r);
  cscan->SetLogy(false);
  plot->Draw("EXP CLs CLb OBS");  // plot also CLb and CLs+b
  cscan->SaveAs(Form("%s/limitscan_%s.eps", _outdir.c_str(), _suffix.c_str()));
  delete cscan;

  double mu_up = r->GetExpectedUpperLimit(0);
  double mu_up_1p = r->GetExpectedUpperLimit(1);
  double mu_up_1m = r->GetExpectedUpperLimit(-1);
  double mu_up_2p = r->GetExpectedUpperLimit(2);
  double mu_up_2m = r->GetExpectedUpperLimit(-2);
  double mu_up_obs = upperLimit;
  */

  TCanvas *cscan = new TCanvas("cscan", "", 800, 600);
  TGraph *gscans = new TGraph(npointsa);
  TGraph *gscan = new TGraph(npointsa);
  TGraph *gscanb = new TGraph(npointsa);
  TGraph *gscana = new TGraph(npointsa);
  TGraphAsymmErrors *gscana1 = new TGraphAsymmErrors(npointsa);
  TGraphAsymmErrors *gscana2 = new TGraphAsymmErrors(npointsa);
  double scan_pnull = 1;
  double scan_palt = 1;
  double scan_pnullA = 1;
  int count = 0;
  getSignificance(data, mc, work, scan_pnull, scan_palt, scan_pnullA, true, 0);
  if (scan_pnull != scan_pnull || scan_pnull < 0) scan_pnull = 0.49;
  if (scan_palt != scan_palt || scan_palt < 0) scan_palt = 0.49;
  double CLsplusbD = scan_pnull;
  double CLbD = scan_palt;
  std::cout << "p_0 = " << scan_pnull << ", p_alt = " << scan_palt << ", significance = " << ROOT::Math::normal_quantile_c(scan_pnull,1.) << std::endl;
  double expected_pnull = AsymptoticCalculator::GetExpectedPValues(scan_pnull, scan_palt, 0, false);
  if (expected_pnull != expected_pnull || expected_pnull < 0) expected_pnull = 0.49;

  double mu_up = 0;
  double mu_up_1p = 0;
  double mu_up_1m = 0;
  double mu_up_2p = 0;
  double mu_up_2m = 0;
  double mu_up_obs = 0;
  
  TLegend l(0.6,0.6,0.89,0.89);
  l.SetBorderSize(0);

  std::vector<double> vscans;
  std::vector<double> vscana;
  std::vector<double> vscana1p;
  std::vector<double> vscana1m;
  std::vector<double> vscana2p;
  std::vector<double> vscana2m;
  std::vector<double> mulist;
  double old_pnull = 1;
  double old_palt = 1;
  double my_mu = 0;
  while (count < npointsa) {
    getSignificance(data, mc, work, scan_pnull, scan_palt, scan_pnullA, false, my_mu);
    if (scan_pnull < 0 || scan_palt < 0) {
      my_mu += poimaxa/((double)npointsa);
      continue;
    }
    double CLsplusb = scan_pnull;
    double CLb = scan_palt;
    double CLs = CLsplusb/CLb;

    gscans->SetPoint(count, my_mu, CLs);
    vscans.push_back(CLs);
    gscan->SetPoint(count, my_mu, CLsplusb);
    gscanb->SetPoint(count, my_mu, CLb);

    double scan_pnullA_sig = ROOT::Math::normal_quantile(scan_pnullA, 1.);
    double expected_CLs = ROOT::Math::normal_cdf_c(scan_pnullA_sig, 1.)/ROOT::Math::normal_cdf(0, 1.);
    double expected_CLs1p = ROOT::Math::normal_cdf_c(scan_pnullA_sig - 1.0, 1.)/ROOT::Math::normal_cdf(1, 1.);
    double expected_CLs1m = ROOT::Math::normal_cdf_c(scan_pnullA_sig + 1.0, 1.)/ROOT::Math::normal_cdf(-1, 1.);
    double expected_CLs2p = ROOT::Math::normal_cdf_c(scan_pnullA_sig - 2.0, 1.)/ROOT::Math::normal_cdf(2, 1.);
    double expected_CLs2m = ROOT::Math::normal_cdf_c(scan_pnullA_sig + 2.0, 1.)/ROOT::Math::normal_cdf(-2, 1.);

    if (expected_CLs > 1 || expected_CLs < 0 || expected_CLs != expected_CLs) expected_CLs = 1;
    if (expected_CLs1p > 1 || expected_CLs1p < 0 || expected_CLs1p != expected_CLs1p) expected_CLs1p = 1;
    if (expected_CLs1m > 1 || expected_CLs1m < 0 || expected_CLs1m != expected_CLs1m) expected_CLs1m = 1;
    if (expected_CLs2p > 1 || expected_CLs2p < 0 || expected_CLs2p != expected_CLs2p) expected_CLs2p = 1;
    if (expected_CLs2m > 1 || expected_CLs2m < 0 || expected_CLs2m != expected_CLs2m) expected_CLs2m = 1;
    std::cout << "expected_CLs = " << expected_CLs << " +/- " << expected_CLs1p << " " << expected_CLs1m << " " << expected_CLs2p << " " << expected_CLs2m << std::endl;

    gscana->SetPoint(count, my_mu, expected_CLs);
    vscana.push_back(expected_CLs);

    gscana1->SetPoint(count, my_mu, expected_CLs);
    gscana1->SetPointError(count, 0, 0, std::fabs(expected_CLs1m-expected_CLs), std::fabs(expected_CLs1p-expected_CLs));
    vscana1m.push_back(expected_CLs1m);
    vscana1p.push_back(expected_CLs1p);

    gscana2->SetPoint(count, my_mu, expected_CLs);
    gscana2->SetPointError(count, 0, 0, std::fabs(expected_CLs2m-expected_CLs), std::fabs(expected_CLs2p-expected_CLs));
    vscana2m.push_back(expected_CLs2m);
    vscana2p.push_back(expected_CLs2p);
    mulist.push_back(my_mu);

    old_pnull = scan_pnull;
    old_palt = scan_palt;
    count++;

    mu_up_obs = getTransition(0.05, vscans, mulist);
    mu_up = getTransition(0.05, vscana, mulist);
    mu_up_1p = getTransition(0.05, vscana1p, mulist);
    mu_up_1m = getTransition(0.05, vscana1m, mulist);
    mu_up_2p = getTransition(0.05, vscana2p, mulist);
    mu_up_2m = getTransition(0.05, vscana2m, mulist);

    double delta_mu = poimaxa/((double)npointsa);
    int lidx = vscana.size()-1;
    if (count > 2 && vscana[lidx]>0.05) {
      double diff = -1;
      if (vscana[lidx-1] - vscana[lidx] != 0)
        diff = (vscana[lidx] - vscana[lidx-1])/(mulist[lidx] - mulist[lidx-1]);
      if (diff < 1.0 && diff > 0.3) {
        double new_delta = 0.5*(vscana[lidx] - 0.05)/std::fabs(diff);
        if (new_delta < 0.01) new_delta = delta_mu;
        delta_mu = new_delta;
      }
    }
    my_mu += delta_mu;
    if (count > 2 && vscana[lidx] < 0.2e-3) break;
  }
  while (count < npointsa) {
    gscans->SetPoint(count, my_mu, 0);
    gscan->SetPoint(count, my_mu, 0);
    gscanb->SetPoint(count, my_mu, 0);
    gscana->SetPoint(count, my_mu, 0);
    gscana1->SetPoint(count, my_mu, 0);
    gscana1->SetPointError(count, 0, 0, 0, 0);
    gscana2->SetPoint(count, my_mu, 0);
    gscana2->SetPointError(count, 0, 0, 0);
    count++;
    my_mu += 0.01;
  }
  double maxpoint = mulist[mulist.size()-1];
  

  gscans->SetLineWidth(2);
  gscan->SetLineWidth(2);
  gscana->SetLineWidth(2);
  gscanb->SetLineWidth(2);
  gscans->SetLineColor(kBlue);
  gscan->SetLineColor(kRed);
  gscanb->SetLineColor(kBlack);

  gscana2->SetFillStyle(1001);
  gscana2->SetFillColor(5);
  gscana2->SetLineColor(5);
  gscana2->SetMarkerColor(5);
  gscana1->SetFillStyle(1001);
  gscana1->SetFillColor(3);
  gscana1->SetLineColor(kBlack);

  gscana->SetLineStyle(kDashed);
  gscana->SetLineWidth(2);

  gscana2->GetYaxis()->SetRangeUser(0,1.1);
  gscana2->GetXaxis()->SetRangeUser(0,maxpoint);

  gscana->SetMarkerStyle(20);
  gscana->SetMarkerSize(1.0);
  gscans->SetMarkerStyle(20);
  gscans->SetMarkerSize(1.0);
  gscanb->SetMarkerStyle(20);
  gscanb->SetMarkerSize(1.0);
  gscan->SetMarkerStyle(20);
  gscan->SetMarkerSize(1.0);

  l.AddEntry(gscana, "Expected CLs", "L");
  l.AddEntry(gscans, "CLs", "LP");
  l.AddEntry(gscanb, "CLb", "LP");
  l.AddEntry(gscan, "CLs+b", "LP");
  l.AddEntry(gscana1, "Expected CLs #pm 1 #sigma", "F");
  l.AddEntry(gscana2, "Expected CLs #pm 2 #sigma", "F");

  gscana2->SetTitle(" ");
  gscana2->GetXaxis()->SetTitle("#mu");
  gscana2->GetYaxis()->SetTitle("probability");

  TLine lin(0, 0.05, maxpoint, 0.05);
  lin.SetLineWidth(2);
  lin.SetLineColor(kRed);
  gscana2->Draw("A E3");
  gscana1->Draw("E3");
  gscana->Draw("LP");
  gscans->Draw("LP");
  gscanb->Draw("LP");
  gscan->Draw("LP");
  lin.Draw();
  l.Draw();

  cscan->SaveAs(Form("%s/limitscan_%s.eps", _outdir.c_str(), _suffix.c_str()));

  delete cscan;
  delete gscans;
  delete gscan;
  delete gscanb;
  delete gscana;
  delete gscana1;
  delete gscana2;

  ofstream result(Form("%s/limit_%s.txt", _outdir.c_str(), _suffix.c_str()));
  result << "mumaxobs       " << mu_up_obs << std::endl;
  result << "mumax          " << mu_up << std::endl;
  result << "mumax1p        " << mu_up_1p << std::endl;
  result << "mumax1m        " << mu_up_1m << std::endl;
  result << "mumax2p        " << mu_up_2p << std::endl;
  result << "mumax2m        " << mu_up_2m << std::endl;
  result << "p0             " << expected_pnull << std::endl;
  result << "p0obs          " << CLsplusbD << std::endl;
  result << "sigobs         " << ROOT::Math::normal_quantile_c(CLsplusbD,1.) << std::endl;
  result.close();

  delete data;
  delete sbModel;
  delete bModel;

  return 0;
}

