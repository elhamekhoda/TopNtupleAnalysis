#include "FitUtils.h"

#include "TFile.h"
#include "TTree.h"
#include "TChain.h"
#include "TCanvas.h"
#include "TAxis.h"
#include "TString.h"
#include "TStyle.h"
#include "TMath.h"
#include "TH2.h"
#include "TLatex.h"
#include "TLine.h"

#include <fstream>
#include <sstream>
#include <iomanip>
#include <string>
#include <map>
#include <vector>

#include "RooMinimizer.h"
#include "RooLognormal.h"
#include "RooCategory.h"
#include "RooWorkspace.h"
#include "RooRealVar.h"
#include "RooSimultaneous.h"
#include "RooPlot.h"
#include "RooHist.h"
#include "RooDataSet.h"
#include "RooAbsPdf.h"
#include "RooAddPdf.h"
#include "RooExtendPdf.h"
#include "RooProduct.h"
#include "RooConstVar.h"
#include "RooFitResult.h"
#include "RooExponential.h"
#include "RooLandau.h"

#include "RooStats/ModelConfig.h"
#include "RooStats/ProfileLikelihoodCalculator.h"
#include "RooStats/LikelihoodInterval.h"
#include "RooStats/LikelihoodIntervalPlot.h"

#include "RooStats/ToyMCSampler.h"
#include "RooStats/ProfileLikelihoodTestStat.h"
#include "RooStats/HypoTestInverterResult.h"

#include "RooStats/HypoTestInverterPlot.h"
#include "RooStats/FrequentistCalculator.h"
#include "RooStats/AsymptoticCalculator.h"
#include "RooStats/HypoTestInverter.h"

#include "Models.h"

using namespace RooFit;
using namespace RooStats;
using namespace std;

const double mttlow = 1.1;
const double mttlim = 4.1;

string outputDir = "";

Results::Results() {
}

Results::Results(double a, double b, double c, double d, double e, double f, double g, double h)
   : mumax(a), mumax_dw(b), mumax_up(c), mumax2_dw(d), mumax2_up(e),
     p(f), expP(g), mumax_obs(h) {
}

RooDataSet *readData(const std::string &file, int channels_hist, const std::string &syst, RooWorkspace *work, double extraWeight, bool useCat) {
  RooDataSet *data = new RooDataSet(Form("signaldata_%s_%d_%s", file.c_str(), channels_hist, syst.c_str()), "", RooArgSet(*work->var("x"), *work->var("w")), WeightVar(*work->var("w")));
  readData(data, file, channels_hist, syst, work, extraWeight, useCat);
  return data;
}

void readData(RooDataSet *data, const std::string &file, int channels_hist, const std::string &syst, RooWorkspace *work, double extraWeight, bool useCat) {
  TFile *f = new TFile(file.c_str());
  TTree *mini = (TTree *) f->Get("mini");
  std::string *s = 0;
  int cat;
  double mtt, weight;
  mini->SetBranchAddress("cat", &cat);
  mini->SetBranchAddress("syst", &s);
  mini->SetBranchAddress("mtt", &mtt);
  mini->SetBranchAddress("weight", &weight);
  for (Long_t entry = 0; entry < mini->GetEntries(); ++entry) {
    mini->GetEntry(entry);
    if (channels_hist >= 0 && cat != channels_hist) continue;
    if (cat >= 2) continue; // TODO (temporary)
    if (useCat) {
      work->cat("channel")->setIndex(cat);
    }
    if (*s != syst) continue;
    if (mtt < work->var("x")->getMin() || mtt > work->var("x")->getMax()) continue;
    weight *= extraWeight;
    *work->var("x") = mtt;
    *work->var("w") = weight;
    if (!useCat) {
      data->add(RooArgSet(*work->var("x"), *work->var("w")), weight);
    } else {
      data->add(RooArgSet(*work->var("x"), *work->var("w"), *work->cat("channel")), weight);
    }
  }
  delete f;
}

int minimizeFancy(RooNLLVar* nll, RooFitResult **fr)
{
  RooAbsReal* fcn = (RooAbsReal*)nll;
  return minimizeFancy(fcn, fr);
}

int minimizeFancy(RooAbsReal* fcn, RooFitResult **fr)
{
  int printLevel = ROOT::Math::MinimizerOptions::DefaultPrintLevel();
  RooFit::MsgLevel msglevel = RooMsgService::instance().globalKillBelow();
  if (printLevel < 0) RooMsgService::instance().setGlobalKillBelow(RooFit::FATAL);

  int strat = ROOT::Math::MinimizerOptions::DefaultStrategy();
  int save_strat = strat;
  RooMinimizer minim(*fcn);
  minim.setStrategy(strat);
  minim.setPrintLevel(printLevel);


  int status = minim.minimize(ROOT::Math::MinimizerOptions::DefaultMinimizerType().c_str(), ROOT::Math::MinimizerOptions::DefaultMinimizerAlgo().c_str());

  if (status != 0 && status != 1 && strat < 2) {
    strat++;
    cout << "Fit failed with status " << status << ". Retrying with strategy " << strat << endl;
    minim.setStrategy(strat);
    status = minim.minimize(ROOT::Math::MinimizerOptions::DefaultMinimizerType().c_str(), ROOT::Math::MinimizerOptions::DefaultMinimizerAlgo().c_str());
  }

  if (status != 0 && status != 1 && strat < 2) {
    strat++;
    cout << "Fit failed with status " << status << ". Retrying with strategy " << strat << endl;
    minim.setStrategy(strat);
    status = minim.minimize(ROOT::Math::MinimizerOptions::DefaultMinimizerType().c_str(), ROOT::Math::MinimizerOptions::DefaultMinimizerAlgo().c_str());
  }

  if (status != 0 && status != 1) {
    string minType = ROOT::Math::MinimizerOptions::DefaultMinimizerType();
    string newMinType;
    if (minType == "Minuit2") newMinType = "Minuit";
    else newMinType = "Minuit2";
  
    cout << "Switching minuit type from " << minType << " to " << newMinType << endl;
  
    ROOT::Math::MinimizerOptions::SetDefaultMinimizer(newMinType.c_str());
    strat = ROOT::Math::MinimizerOptions::DefaultStrategy();
    minim.setStrategy(strat);

    status = minim.minimize(ROOT::Math::MinimizerOptions::DefaultMinimizerType().c_str(), ROOT::Math::MinimizerOptions::DefaultMinimizerAlgo().c_str());

    if (status != 0 && status != 1 && strat < 2) {
      strat++;
      cout << "Fit failed with status " << status << ". Retrying with strategy " << strat << endl;
      minim.setStrategy(strat);
      status = minim.minimize(ROOT::Math::MinimizerOptions::DefaultMinimizerType().c_str(), ROOT::Math::MinimizerOptions::DefaultMinimizerAlgo().c_str());
    }

    if (status != 0 && status != 1 && strat < 2) {
      strat++;
      cout << "Fit failed with status " << status << ". Retrying with strategy " << strat << endl;
      minim.setStrategy(strat);
      status = minim.minimize(ROOT::Math::MinimizerOptions::DefaultMinimizerType().c_str(), ROOT::Math::MinimizerOptions::DefaultMinimizerAlgo().c_str());
    }

    ROOT::Math::MinimizerOptions::SetDefaultMinimizer(minType.c_str());
  }

  *fr = minim.save();

  if (printLevel < 0) RooMsgService::instance().setGlobalKillBelow(msglevel);
  ROOT::Math::MinimizerOptions::SetDefaultStrategy(save_strat);


  return status;
}


double load(const char *filename, RooDataSet *data, \
            RooRealVar &x, RooRealVar &w, \
            double extraWeight, RooCategory *idx) {
  double yield = 0;
  if (string(filename).find(".root") != string::npos) {
    TChain c("mini");
    c.Add(filename);
    double recoMtt;
    double weight;
    c.SetBranchAddress("recoMtt", &recoMtt);
    c.SetBranchAddress("weight", &weight);
    for (Long_t entry = 0; entry < c.GetEntries(); ++entry) {
      c.GetEntry(entry);

      if (recoMtt*1e-3 < mttlow) continue;
      if (recoMtt*1e-3 > mttlim) continue;

      x = recoMtt*1e-3;
      weight *= extraWeight;
      w = weight;

      if (idx) {
        data->add(RooArgSet(x, w, *idx), weight);
      } else {
        data->add(RooArgSet(x, w), weight);
      }
      yield += weight;
    }
  } else { // assume it is text
    ifstream file(filename);
    file.seekg(0);
    do {
      std::stringstream sl;
      file.get(*sl.rdbuf(), '\n');
      if (file.get() == EOF) break;
      if (sl.str() == "") continue;
      if (sl.str() == "\n") continue;
      double mtt, weight;
      sl >> mtt >> weight;
      weight *= extraWeight;
      if (mtt*1e-6 < mttlow) continue;
      if (mtt*1e-6 > mttlim) continue;
      x = mtt*1e-6;
      w = weight;
      if (idx) {
        data->add(RooArgSet(x, w, *idx), weight);
      } else {
        data->add(RooArgSet(x, w), weight);
      }
      yield += weight;
    } while (file.good());
  }
  return yield;
}


void MakeBkgModel(const char *bkgfile, const char *channel, double extraWeight) {
  RooWorkspace work("work"); 

  RooRealVar x("x", "x", mttlow, mttlim);                                                 // mtt
  RooRealVar w("w", "w", 1, 0, 100e3);                                                    // event weight

  RooRealVar nbkg(Form("%s_%s", "nbkg", channel), "nbkg", 3000, 0, 1e6);                  // number of background events
  RooRealVar p1(Form("%s_%s", "p1", channel), "", 0., -100., 10.);
  RooRealVar p2(Form("%s_%s", "p2", channel), "", 0., -100., 10.);
  //RooRealVar p3(Form("%s_%s", "p3", channel), "", 0., -100., 10.);
  //RooRealVar p4(Form("%s_%s", "p4", channel), "", 0., -100., 10.);

  RooAbsPdf *bkgshape = new BkgFallPdf(Form("%s_%s", "bkgshape", channel), "bkg_shape", x, p1, p2);//, p3);
  RooExtendPdf *bkg = new RooExtendPdf(Form("%s_%s", "bkg", channel), "bkg", *bkgshape, nbkg);

  RooDataSet *databkg = new RooDataSet("mtt", "mtt", RooArgSet(x, w), WeightVar(w));
  load(bkgfile, databkg, x, w, extraWeight);

  RooFitResult *fr1 = bkg->fitTo(*databkg, SumW2Error(true), Minimizer("Minuit2", "Migrad"), Save(true), Extended());
  RooFitResult *fr = bkg->fitTo(*databkg, SumW2Error(true), Minimizer("Minuit2", "Migrad"), Save(true), Extended());
  cout << "(MakeBkgModel)  Fit result:" << endl;
  fr->Print();
  TCanvas *c1 = new TCanvas("ch1", "", 800, 600);
  fr->correlationHist(Form("bkgfit_corrmat_%s", channel))->Draw("zcol");
  c1->SaveAs(Form("%s/bkgfit_corrmat_%s.eps", outputDir.c_str(), channel));
  delete c1;

  for (int i = 0; i < fr->floatParsFinal().getSize();++i) {
    for (int j = i+1; j < fr->floatParsFinal().getSize();++j) {
      c1 = new TCanvas("ch1", "", 800, 600);
      RooPlot *cp = x.frame(Title(Form("Correlation between %s and %s in signal fit", fr->floatParsFinal().at(i)->GetName(), fr->floatParsFinal().at(j)->GetName())));
      fr->plotOn(cp, *fr->floatParsFinal().at(i), *fr->floatParsFinal().at(j), "ME12B");
      cp->Draw();
      c1->SaveAs(Form("%s/bkgfit_corr_%s_%s_%s.eps", outputDir.c_str(), fr->floatParsFinal().at(i)->GetName(), fr->floatParsFinal().at(j)->GetName(), channel));
      delete c1;
    }
  }

  std::map<std::string, std::string> channel_str;
  channel_str.insert(std::make_pair<std::string, std::string>("be", "Boosted Electron"));
  channel_str.insert(std::make_pair<std::string, std::string>("bmu", "Boosted Muon"));
  channel_str.insert(std::make_pair<std::string, std::string>("re", "Resolved Electron"));
  channel_str.insert(std::make_pair<std::string, std::string>("rmu", "Resolved Muon"));
  std::string full_channel_name = "";
  if (channel_str.find(channel) != channel_str.end()) full_channel_name = channel_str[channel];

  TCanvas *cbs = new TCanvas("cbs", "", 800, 600);
  RooPlot *frame = x.frame(Title(Form("Background, %s", full_channel_name.c_str())), Bins((unsigned int) ((mttlim-mttlow)*10)), Range(mttlow, mttlim));
  databkg->plotOn(frame);
  bkg->plotOn(frame);
  bkg->paramOn(frame,Layout(0.45,0.9,0.9), Format("NEU", AutoPrecision(1)));
  cbs->SetLogy(1);
  cbs->Update();
  double chi2 = frame->chiSquare();
  TLatex latex;
  latex.SetTextSize(0.05);
  latex.SetNDC(1);
  frame->Draw();
  latex.DrawLatex(0.5, 0.3, Form("#chi^{2}/ndof = %f", chi2));
  cbs->Update();
  cbs->SaveAs(Form("%s/bkgmtt_%s.eps", outputDir.c_str(), channel));

  work.import(*bkg);
  work.import(*databkg);
  work.writeToFile(Form("%s/workspace_bkg_%s.root", outputDir.c_str(), channel)); 
}

void MakeSignalModel(const char *sigfile, const char *channel, const char *sigpoint, double extraW) {
  RooWorkspace work("work"); 
  RooRealVar x("x", "x", mttlow, mttlim);                                                 // mtt
  RooRealVar w("w", "w", 1, 0, 100e3);                                                    // event weight

  RooRealVar sig_norm(Form("sig_norm_%s", channel), "sig_norm", 20, 0, 1000);             // signal expected number of events
  RooRealVar mu("mu", "mu", 1, 0, 100);                                                   //mu

  // as in W'->tb
  RooRealVar sig_m(Form("sig_m_%s", channel), "sig_m", 2, 0, mttlim);                     // gaussian mean in signal
  RooRealVar sig_s(Form("sig_s_%s", channel), "sig_s", 0.5, 0.1, 1000);                   // guassian sigma in signal
  RooRealVar sig_xi(Form("sig_xi_%s", channel), "sig_xi", 2, mttlow, mttlim);             // skew-normal mean in signal
  RooRealVar sig_omega(Form("sig_omega_%s", channel), "sig_omega", 0.5, 0.1, 2);          // skew-normal scale in signal
  RooRealVar sig_alpha(Form("sig_alpha_%s", channel), "sig_alpha", 0, -20.0, 0.0);        // skew-normal shape in signal
  RooRealVar sig_skewnorm(Form("sig_skewnorm_%s", channel), "sig_skewnorm", 1, 0, 1);     // skew-normal normalisation

  RooRealVar sig_m2(Form("sig_m2_%s", channel), "sig2_m", 2.5, 0, mttlim);                // gaussian mean in signal
  RooRealVar sig_s2(Form("sig_s2_%s", channel), "sig2_s", 0.5, 0.1, 1000);                // guassian sigma in signal
  RooRealVar sig_norm2(Form("sig_norm2_%s", channel), "sig_norm2", 0.3, 0, 1);            // skew-normal normalisation

  RooRealVar sig_m3(Form("sig_m3_%s", channel), "sig3_m", 2.5, 0, mttlim);                // gaussian mean in signal
  RooRealVar sig_s3(Form("sig_s3_%s", channel), "sig3_s", 0.5, 0.1, 1000);                // guassian sigma in signal
  RooRealVar sig_norm3(Form("sig_norm3_%s", channel), "sig_norm3", 0.3, 0, 1);            // skew-normal normalisation

  RooAbsPdf *sig_shape = new SignalPdf(Form("sig_shape_%s", channel), "sig_shape", x, sig_m, sig_s, sig_xi, sig_omega, sig_alpha, sig_skewnorm, sig_m2, sig_s2, sig_norm2, sig_m3, sig_s3, sig_norm3);

  RooFormulaVar *nsig_mu = new RooFormulaVar(Form("nsig_mu_%s", channel), "@0*@1", RooArgList(sig_norm, mu));
  RooExtendPdf *sig = new RooExtendPdf(Form("sig_%s", channel), "sig", *sig_shape, *nsig_mu);

  sig_m.setConstant(false);
  sig_s.setConstant(false);
  sig_xi.setConstant(false);
  sig_omega.setConstant(false);
  sig_alpha.setConstant(false);
  sig_skewnorm.setConstant(false);
  sig_norm.setConstant(false);

  sig_m2.setConstant(false);
  sig_s2.setConstant(false);
  sig_norm2.setConstant(false);
  sig_m3.setConstant(false);
  sig_s3.setConstant(false);
  sig_norm3.setConstant(false);

  mu.setVal(1);
  mu.setConstant(true);

  double y = 0;
  //RooDataSet *datasig_prep = fitSignal(sig, sigfile, x, w, y, extraW, sigpoint, channel);
  RooDataSet *datasig = fitSignal(sig, sigfile, x, w, y, extraW, sigpoint, channel);

  std::map<std::string, std::string> channel_str;
  channel_str.insert(std::make_pair<std::string, std::string>("be", "Boosted Electron"));
  channel_str.insert(std::make_pair<std::string, std::string>("bmu", "Boosted Muon"));
  channel_str.insert(std::make_pair<std::string, std::string>("re", "Resolved Electron"));
  channel_str.insert(std::make_pair<std::string, std::string>("rmu", "Resolved Muon"));
  std::string full_channel_name = "";
  if (channel_str.find(channel) != channel_str.end()) full_channel_name = channel_str[channel];

  std::map<std::string, std::string> mode_str;
  mode_str.insert(std::make_pair<std::string, std::string>("zp500", "Z' m = 500 GeV"));
  mode_str.insert(std::make_pair<std::string, std::string>("zp750", "Z' m = 750 GeV"));
  mode_str.insert(std::make_pair<std::string, std::string>("zp1tev", "Z' m = 1 TeV"));
  mode_str.insert(std::make_pair<std::string, std::string>("zp125tev", "Z' m = 1.25 TeV"));
  mode_str.insert(std::make_pair<std::string, std::string>("zp15tev", "Z' m = 1.5 TeV"));
  mode_str.insert(std::make_pair<std::string, std::string>("zp175tev", "Z' m = 1.75 TeV"));
  mode_str.insert(std::make_pair<std::string, std::string>("zp2tev", "Z' m = 2 TeV"));
  mode_str.insert(std::make_pair<std::string, std::string>("zp25tev", "Z' m = 2.5 TeV"));
  mode_str.insert(std::make_pair<std::string, std::string>("zp3tev", "Z' m = 3 TeV"));
  std::string full_mode_name = "";
  if (mode_str.find(sigpoint) != mode_str.end()) full_mode_name = mode_str[sigpoint];

  TCanvas *cs = new TCanvas("cs", "", 800, 600);
  RooPlot *framesig = x.frame(Title(Form("Signal (%s, %s)", full_mode_name.c_str(), full_channel_name.c_str())), Bins((unsigned int) ((mttlim-mttlow)*10)), Range(mttlow, mttlim));
  datasig->plotOn(framesig);
  sig->plotOn(framesig, LineStyle(kDashed));
  //double lxmin = 0.55;
  //double lxmax = 0.99;
  //if (sig_m.getVal() > 1.75) { lxmin = 0.1; lxmax = 0.5; }
  //sig->paramOn(framesig, Layout(lxmin,lxmax,0.9), ShowConstants(false), Format("NEU",AutoPrecision(1)));
  framesig->Draw();
  cs->SaveAs(Form("%s/sigmtt_%s_%s.eps", outputDir.c_str(), channel, sigpoint));
  //delete cs;

  sig_m.setConstant(true);
  sig_s.setConstant(true);
  sig_xi.setConstant(true);
  sig_omega.setConstant(true);
  sig_alpha.setConstant(true);
  sig_skewnorm.setConstant(true);
  sig_norm.setConstant(true);
  mu.setConstant(false);

  sig_m2.setConstant(true);
  sig_s2.setConstant(true);
  sig_norm2.setConstant(true);
  sig_m3.setConstant(true);
  sig_s3.setConstant(true);
  sig_norm3.setConstant(true);

  work.import(*sig);
  work.import(*datasig);

  work.writeToFile(Form("%s/workspace_sig_%s_%s.root", outputDir.c_str(), channel, sigpoint)); 

}


RooDataSet * fitSignal(RooAbsPdf *sig, const std::string &sigfile, RooRealVar &x, RooRealVar &w, double &yield, double extraW, const std::string &mode, const std::string &channel) {
  RooDataSet *data = new RooDataSet("sigmtt", "mtt", RooArgSet(x, w), WeightVar(w));
  yield = load(sigfile.c_str(), data, x, w, extraW);
  RooFitResult *fr = sig->fitTo(*data, SumW2Error(true), Minimizer("Minuit2", "Migrad"), Save(true), Strategy(2));
  cout << "(fitSignal)  Fit result:" << endl;
  fr->Print();
  TCanvas *c1 = new TCanvas("ch1", "", 800, 600);
  fr->correlationHist()->Draw("zcol");
  c1->SaveAs(Form("%s/sigfit_corrmat_%s_%s.eps", outputDir.c_str(), channel.c_str(), mode.c_str()));
  delete c1;

  for (int i = 0; i < fr->floatParsFinal().getSize();++i) {
    for (int j = i+1; j < fr->floatParsFinal().getSize();++j) {
      c1 = new TCanvas("ch1", "", 800, 600);
      RooPlot *cp = x.frame(Title(Form("Correlation between %s and %s in signal fit", fr->floatParsFinal().at(i)->GetName(), fr->floatParsFinal().at(j)->GetName())));
      fr->plotOn(cp, *fr->floatParsFinal().at(i), *fr->floatParsFinal().at(j), "ME12B");
      cp->Draw();
      c1->SaveAs(Form("%s/sigfit_corr_%s_%s_%s_%s.eps", outputDir.c_str(), fr->floatParsFinal().at(i)->GetName(), fr->floatParsFinal().at(j)->GetName(), channel.c_str(), mode.c_str()));
      delete c1;
    }
  }

  return data;
}

double lnmuLogNormal(double mean, double sigma) {
  return mean*mean/TMath::Sqrt(sigma*sigma + +mean*mean);
}

double lnkLogNormal(double mean, double sigma) {
  return TMath::Exp(TMath::Sqrt(TMath::Log(sigma*sigma/(mean*mean)+1)));
}

void MakeSBModel(vector<string> &vws, vector<string> &vwb, vector<string> &vchannel, const string &mode,
                 vector<string> &vfs, vector<string> &vfb, double bkgW, double sigW, double sigSyst, double sigShapeSyst) {
  RooWorkspace work("work"); 
  RooRealVar x("x", "x", mttlow, mttlim);                            // mtt
  RooRealVar w("w", "w", 1, 0, 100e3);                               // event weight

  RooRealVar mu("mu", "mu", 1, 0, 100);                              // mu

  RooCategory *idx = new RooCategory("channel", "channel");
  for (size_t z = 0; z < vws.size(); ++z) {
    idx->defineType(vchannel[z].c_str(), z);
  }

  map<string, RooAbsPdf *> jointMap;
  RooArgSet nuisParam("nuisParam");
  for (size_t z = 0; z < vws.size(); ++z) {
    RooArgSet ctr;
    std::string ws = vws[z];
    std::string wb = vwb[z];
    std::string mchannel = vchannel[z];
    const char *channel = mchannel.c_str();

    TFile *fs = new TFile(ws.c_str());
    RooWorkspace *wws = (RooWorkspace *) fs->Get("work");

    RooRealVar *sig_m = wws->var(Form("sig_m_%s", channel));
    RooRealVar *sig_s = wws->var(Form("sig_s_%s", channel));
    RooRealVar *sig_xi = wws->var(Form("sig_xi_%s", channel));
    RooRealVar *sig_omega = wws->var(Form("sig_omega_%s", channel));
    RooRealVar *sig_alpha = wws->var(Form("sig_alpha_%s", channel));
    RooRealVar *sig_skewnorm = wws->var(Form("sig_skewnorm_%s", channel));
    RooAbsReal *sig_norm = 0;
    if (sigSyst <= 0) {
      sig_norm = wws->var(Form("sig_norm_%s", channel));
    }

    RooRealVar *sig_m2 = wws->var(Form("sig_m2_%s", channel));
    RooRealVar *sig_s2 = wws->var(Form("sig_s2_%s", channel));
    RooRealVar *sig_norm2 = wws->var(Form("sig_norm2_%s", channel));

    RooRealVar *sig_m3 = wws->var(Form("sig_m3_%s", channel));
    RooRealVar *sig_s3 = wws->var(Form("sig_s3_%s", channel));
    RooRealVar *sig_norm3 = wws->var(Form("sig_norm3_%s", channel));

    RooRealVar *a_sig_m = new RooRealVar(Form("a_sig_m_%s", channel), "", 1e-1, 2);
    RooRealVar *a_sig_s = new RooRealVar(Form("a_sig_s_%s", channel), "", 1e-1, 2);
    RooRealVar *a_sig_xi = new RooRealVar(Form("a_sig_xi_%s", channel), "", 1e-1, 2);
    RooRealVar *a_sig_omega = new RooRealVar(Form("a_sig_omega_%s", channel), "", 1e-1, 2);
    RooRealVar *a_sig_alpha = new RooRealVar(Form("a_sig_alpha_%s", channel), "", 1e-1, 2);
    RooRealVar *a_sig_skewnorm = new RooRealVar(Form("a_sig_skewnorm_%s", channel), "", 1e-1, 2);
    RooRealVar *a_sig_m2 = new RooRealVar(Form("a_sig_m2_%s", channel), "", 1e-1, 2);
    RooRealVar *a_sig_s2 = new RooRealVar(Form("a_sig_s2_%s", channel), "", 1e-1, 2);
    RooRealVar *a_sig_norm2 = new RooRealVar(Form("a_sig_norm2_%s", channel), "", 1e-1, 2);
    RooRealVar *a_sig_m3 = new RooRealVar(Form("a_sig_m3_%s", channel), "", 1e-1, 2);
    RooRealVar *a_sig_s3 = new RooRealVar(Form("a_sig_s3_%s", channel), "", 1e-1, 2);
    RooRealVar *a_sig_norm3 = new RooRealVar(Form("a_sig_norm3_%s", channel), "", 1e-1, 2);

    RooFormulaVar *s_sig_m = new RooFormulaVar(Form("s_sig_m_%s", channel), "@0*@1", RooArgList(*a_sig_m, RooConst(sig_m->getVal())));
    RooFormulaVar *s_sig_s = new RooFormulaVar(Form("s_sig_s_%s", channel), "@0*@1", RooArgList(*a_sig_s, RooConst(sig_s->getVal())));
    RooFormulaVar *s_sig_xi = new RooFormulaVar(Form("s_sig_xi_%s", channel), "@0*@1", RooArgList(*a_sig_xi, RooConst(sig_xi->getVal())));
    RooFormulaVar *s_sig_omega = new RooFormulaVar(Form("s_sig_omega_%s", channel), "@0*@1", RooArgList(*a_sig_omega, RooConst(sig_omega->getVal())));
    RooFormulaVar *s_sig_alpha = new RooFormulaVar(Form("s_sig_alpha_%s", channel), "@0*@1", RooArgList(*a_sig_alpha, RooConst(sig_alpha->getVal())));
    RooFormulaVar *s_sig_skewnorm = new RooFormulaVar(Form("s_sig_skewnorm_%s", channel), "@0*@1", RooArgList(*a_sig_skewnorm, RooConst(sig_skewnorm->getVal())));
    RooFormulaVar *s_sig_m2 = new RooFormulaVar(Form("s_sig_m2_%s", channel), "@0*@1", RooArgList(*a_sig_m2, RooConst(sig_m2->getVal())));
    RooFormulaVar *s_sig_s2 = new RooFormulaVar(Form("s_sig_s2_%s", channel), "@0*@1", RooArgList(*a_sig_s2, RooConst(sig_s2->getVal())));
    RooFormulaVar *s_sig_norm2 = new RooFormulaVar(Form("s_sig_norm2_%s", channel), "@0*@1", RooArgList(*a_sig_norm2, RooConst(sig_norm2->getVal())));
    RooFormulaVar *s_sig_m3 = new RooFormulaVar(Form("s_sig_m3_%s", channel), "@0*@1", RooArgList(*a_sig_m3, RooConst(sig_m3->getVal())));
    RooFormulaVar *s_sig_s3 = new RooFormulaVar(Form("s_sig_s3_%s", channel), "@0*@1", RooArgList(*a_sig_s3, RooConst(sig_s3->getVal())));
    RooFormulaVar *s_sig_norm3 = new RooFormulaVar(Form("s_sig_norm3_%s", channel), "@0*@1", RooArgList(*a_sig_norm3, RooConst(sig_norm3->getVal())));

    RooAbsPdf *sig_shape = 0;
    if (sigShapeSyst > 0) {
      RooLognormal *sig_m_const = new RooLognormal(Form("sig_m_const_%s", channel), "sig_m_const", *a_sig_m, RooConst(lnmuLogNormal(1.0, sigShapeSyst)), RooConst(lnkLogNormal(1.0, sigShapeSyst)));
      RooLognormal *sig_s_const = new RooLognormal(Form("sig_s_const_%s", channel), "sig_s_const", *a_sig_s, RooConst(lnmuLogNormal(1.0, sigShapeSyst)), RooConst(lnkLogNormal(1.0, sigShapeSyst)));
      RooLognormal *sig_xi_const = new RooLognormal(Form("sig_xi_const_%s", channel), "sig_xi_const", *a_sig_xi, RooConst(lnmuLogNormal(1.0, sigShapeSyst)), RooConst(lnkLogNormal(1.0, sigShapeSyst)));
      RooLognormal *sig_omega_const = new RooLognormal(Form("sig_omega_const_%s", channel), "sig_omega_const", *a_sig_omega, RooConst(lnmuLogNormal(1.0, sigShapeSyst)), RooConst(lnkLogNormal(1.0, sigShapeSyst)));
      RooLognormal *sig_alpha_const = new RooLognormal(Form("sig_alpha_const_%s", channel), "sig_alpha_const", *a_sig_alpha, RooConst(lnmuLogNormal(1.0, sigShapeSyst)), RooConst(lnkLogNormal(1.0, sigShapeSyst)));
      RooLognormal *sig_skewnorm_const = new RooLognormal(Form("sig_skewnorm_const_%s", channel), "sig_skewnorm_const", *a_sig_skewnorm, RooConst(lnmuLogNormal(1.0, sigShapeSyst)), RooConst(lnkLogNormal(1.0, sigShapeSyst)));
      RooLognormal *sig_m2_const = new RooLognormal(Form("sig_m2_const_%s", channel), "sig_m2_const", *a_sig_m2, RooConst(lnmuLogNormal(1.0, sigShapeSyst)), RooConst(lnkLogNormal(1.0, sigShapeSyst)));
      RooLognormal *sig_s2_const = new RooLognormal(Form("sig_s2_const_%s", channel), "sig_s2_const", *a_sig_s2, RooConst(lnmuLogNormal(1.0, sigShapeSyst)), RooConst(lnkLogNormal(1.0, sigShapeSyst)));
      RooLognormal *sig_norm2_const = new RooLognormal(Form("sig_norm2_const_%s", channel), "sig_norm2_const", *a_sig_norm2, RooConst(lnmuLogNormal(1.0, sigShapeSyst)), RooConst(lnkLogNormal(1.0, sigShapeSyst)));
      RooLognormal *sig_m3_const = new RooLognormal(Form("sig_m3_const_%s", channel), "sig_m3_const", *a_sig_m3, RooConst(lnmuLogNormal(1.0, sigShapeSyst)), RooConst(lnkLogNormal(1.0, sigShapeSyst)));
      RooLognormal *sig_s3_const = new RooLognormal(Form("sig_s3_const_%s", channel), "sig_s3_const", *a_sig_s3, RooConst(lnmuLogNormal(1.0, sigShapeSyst)), RooConst(lnkLogNormal(1.0, sigShapeSyst)));
      RooLognormal *sig_norm3_const = new RooLognormal(Form("sig_norm3_const_%s", channel), "sig_norm3_const", *a_sig_norm3, RooConst(lnmuLogNormal(1.0, sigShapeSyst)), RooConst(lnkLogNormal(1.0, sigShapeSyst)));

      ctr.add(*sig_m_const);
      nuisParam.add(*a_sig_m);
      ctr.add(*sig_s_const);
      nuisParam.add(*a_sig_s);
      ctr.add(*sig_xi_const);
      nuisParam.add(*a_sig_xi);
      ctr.add(*sig_omega_const);
      nuisParam.add(*a_sig_omega);
      //ctr.add(*sig_alpha_const);
      //nuisParam.add(*a_sig_alpha);
      //ctr.add(*sig_skewnorm_const);
      //nuisParam.add(*a_sig_skewnorm);
      //ctr.add(*sig_m2_const);
      //nuisParam.add(*a_sig_m2);
      //ctr.add(*sig_s2_const);
      //nuisParam.add(*a_sig_s2);
      //ctr.add(*sig_norm2_const);
      //nuisParam.add(*a_sig_norm2);
      //ctr.add(*sig_m3_const);
      //nuisParam.add(*a_sig_m3);
      //ctr.add(*sig_s3_const);
      //nuisParam.add(*a_sig_s3);
      //ctr.add(*sig_norm3_const);
      //nuisParam.add(*a_sig_norm3);

      //sig_shape = new SignalPdf(Form("sig_shape_%s", channel), "sig_shape", x, *s_sig_m, *s_sig_s, *s_sig_xi, *s_sig_omega, *s_sig_alpha, *s_sig_skewnorm, *s_sig_m2, *s_sig_s2, *s_sig_norm2, *s_sig_m3, *s_sig_s3, *s_sig_norm3);
      sig_shape = new SignalPdf(Form("sig_shape_%s", channel), "sig_shape", x, *s_sig_m, *s_sig_s, *s_sig_xi, *s_sig_omega, *sig_alpha, *sig_skewnorm, *sig_m2, *sig_s2, *sig_norm2, *sig_m3, *sig_s3, *sig_norm3);

    } else {
      sig_shape = new SignalPdf(Form("sig_shape_%s", channel), "sig_shape", x, *sig_m, *sig_s, *sig_xi, *sig_omega, *sig_alpha, *sig_skewnorm, *sig_m2, *sig_s2, *sig_norm2, *sig_m3, *sig_s3, *sig_norm3);
    }

    TFile *fb = new TFile(wb.c_str());
    RooWorkspace *wwb = (RooWorkspace *) fb->Get("work");

    RooRealVar *nbkg = wwb->var(Form("nbkg_%s", channel));
    nbkg->setConstant(false);
    nuisParam.add(*nbkg);

    RooRealVar *p1 = wwb->var(Form("p1_%s", channel));
    RooRealVar *p2 = wwb->var(Form("p2_%s", channel));
    RooRealVar *p3 = wwb->var(Form("p3_%s", channel));
    RooRealVar *p4 = wwb->var(Form("p4_%s", channel));
    p1->setConstant(false);
    p2->setConstant(false);
    //p3->setConstant(false);
    //p4->setConstant(false);
    nuisParam.add(*p1);
    nuisParam.add(*p2);
    //nuisParam.add(*p3);
    //nuisParam.add(*p4);

    double valsn = wws->var(Form("sig_norm_%s", channel))->getVal();
    if (sigSyst > 0) {
      RooRealVar *a_sig_norm = new RooRealVar(Form("a_sig_norm_%s", channel), "", 1e-3, 5);
      sig_norm = new RooFormulaVar(Form("sig_norm_%s", channel), "@0*@1", RooArgList(*a_sig_norm, RooConst(valsn)));
      RooLognormal *sig_norm_const = new RooLognormal(Form("sig_norm_const_%s", channel), "sig_norm_const", *a_sig_norm, RooConst(lnmuLogNormal(1.0, sigSyst)), RooConst(lnkLogNormal(1.0, sigSyst))); // mean 1, variance = 1.0^2
      ctr.add(*sig_norm_const);
      nuisParam.add(*a_sig_norm);
    }

    RooFormulaVar *nsig_mu = new RooFormulaVar(Form("nsig_mu_%s", channel), "@0*@1", RooArgList(*sig_norm, mu));

    RooAbsPdf *bkgshape = new BkgFallPdf(Form("%s_%s", "bkgshape", channel), "bkg_shape", x, *p1, *p2);//, *p3);
    //RooAbsPdf *bkgshape = new RooBukinPdf(Form("%s_%s", "bkgshape", channel), "bkg_shape", x, *pbxp, *pbsigp, *pbxi, *pbrho1, *pbrho2);

    RooAddPdf *model = new RooAddPdf(Form("model_%s", channel), "model", RooArgList(*bkgshape, *sig_shape), RooArgList(*nbkg, *nsig_mu));
    ctr.add(*model);
    RooProdPdf *model_syst = new RooProdPdf(Form("model_syst_%s", channel), "", ctr);

    jointMap.insert(make_pair<string, RooAbsPdf*>(channel, model_syst));
  }
  RooSimultaneous *jointModel = new RooSimultaneous("combined", "combined", jointMap, *idx);

  work.import(*jointModel);

  work.defineSet("nuisParams",nuisParam);
  work.defineSet("globalObs","");

  ModelConfig *mc = new ModelConfig("ModelConfig", &work);
  mc->SetPdf(*jointModel);
  mc->SetParametersOfInterest(*work.var("mu"));
  mc->SetObservables(RooArgSet(*work.var("x"), *work.cat("channel")));
  mc->SetSnapshot(*work.var("mu"));

  // define set of nuisance parameters
  mc->SetNuisanceParameters(*work.set("nuisParams"));
  mc->SetGlobalObservables(*work.set("globalObs"));

  work.import(*mc);

  cout << "************************************************" << endl;
  cout << "Doing fitting on S+B joint model" << endl;

  //RooDataSet *data = jointModel_syst->generate(RooArgSet(x,*idx));
  RooDataSet *data = new RooDataSet("mtt_plot", "mtt", RooArgSet(x, *idx, w), WeightVar(w));
  for (size_t z = 0; z < vfs.size(); ++z) {
    idx->setLabel(vchannel[z].c_str());

    double sigYield = load(vfs[z].c_str(), data, x, w, sigW, idx);
    load(vfb[z].c_str(), data, x, w, bkgW, idx);
  }
  RooFitResult *frj = jointModel->fitTo(*data, SumW2Error(true), Minimizer("Minuit2", "Migrad"), Save(true), Extended());

  cout << "Print out of the joint model fit on bkg." << endl;
  frj->Print();

  for (size_t z = 0; z < vws.size(); ++z) {
    std::string ws = vws[z];
    std::string wb = vwb[z];
    std::string mchannel = vchannel[z];
    const char *channel = mchannel.c_str();

    TCanvas *cplot = new TCanvas("cplot", "", 800, 600);
    TPad *pad_ratio = 0;
    cplot->Divide(1, 2, 0.015, 0.01);
    pad_ratio = (TPad *) cplot->cd(2);
    pad_ratio->SetPad(0,0,1,0.30);
    pad_ratio->SetTopMargin(0.01);
    pad_ratio->SetBottomMargin(0.45);
    cplot->cd(1)->SetPad(0,0.2,1,1);
    cplot->cd(1)->SetBottomMargin(0.13);

    std::map<std::string, std::string> channel_str;
    channel_str.insert(std::make_pair<std::string, std::string>("be", "Boosted Electron"));
    channel_str.insert(std::make_pair<std::string, std::string>("bmu", "Boosted Muon"));
    channel_str.insert(std::make_pair<std::string, std::string>("be", "Resolved Electron"));
    channel_str.insert(std::make_pair<std::string, std::string>("bmu", "Resolved Muon"));
    std::string full_channel_name = "";
    if (channel_str.find(channel) != channel_str.end()) full_channel_name = channel_str[channel];

    RooPlot *plot = x.frame(Title(Form("%s channel", full_channel_name.c_str())), Bins((unsigned int) ((mttlim-mttlow)*10)), Range(mttlow, mttlim));
    data->plotOn(plot, Cut(Form("channel==channel::%s", channel)));
    jointModel->plotOn(plot, Components(Form("bkgshape_%s", channel)), LineStyle(kDashed), LineColor(kBlue), Slice(*idx,channel), ProjWData(x, *data));
    jointModel->plotOn(plot, Components(Form("sig_shape_%s", channel)), LineStyle(kDashed), LineColor(kRed), Slice(*idx,channel), ProjWData(x, *data));
    jointModel->plotOn(plot, LineColor(kBlack), Slice(*idx,channel), ProjWData(x, *data));
    RooArgSet *myParams = jointModel->getParameters(plot->getNormVars());
    RooArgSet myParams2;
    RooFIter y = myParams->fwdIterator();
    RooAbsArg *yn = 0;
    while ((yn = y.next())) {
      if (string(yn->GetName()).find(Form("_%s", channel)) != string::npos) {
        myParams2.add(*yn);
      }
    }
    myParams2.add(mu);
    jointModel->paramOn(plot, ShowConstants(false), Layout(0.66, 0.99, 0.99), Format("NEU",AutoPrecision(1)), Parameters(myParams2));
    plot->SetMinimum(5e-1);
    plot->GetYaxis()->SetTitleFont(42);
    plot->GetYaxis()->SetLabelFont(42);
    plot->GetYaxis()->SetTitleOffset(0.75);
    plot->GetYaxis()->SetTitleSize(0.06);
    plot->GetYaxis()->SetLabelSize(0.05);
    plot->Draw();
    double chi2 = plot->chiSquare();
    TLatex latex;
    latex.SetTextSize(0.05);
    latex.SetNDC(1);
    latex.DrawLatex(0.66, 0.55, Form("#chi^{2}/ndof = %f", chi2));
    cplot->Update();
    cplot->cd(1)->SetLogy(1);
    cplot->cd(2);
    RooPlot *plot2 = x.frame(Title(" "), Bins((unsigned int) ((mttlim-mttlow)*10)), Range(mttlow,mttlim));
    RooCurve* curve = (RooCurve*) plot->findObject(0,RooCurve::Class());
    RooHist* histnum = (RooHist*) plot->findObject(0,RooHist::Class());
    RooHist* hist = new RooHist(plot->getFitRangeBinW()) ;
    for (Int_t i = 0; i < histnum->GetN(); i++) {
      Double_t xx,point;
      histnum->GetPoint(i,xx,point);
      Double_t yy = 1;
      if (point != 0) yy = curve->interpolate(xx)/point;
      Double_t dyl = 0;
      if (point) dyl = curve->interpolate(xx)*histnum->GetErrorYlow(i)/std::pow(point,2);
      Double_t dyh = 0;
      if (point) dyh = curve->interpolate(xx)*histnum->GetErrorYhigh(i)/std::pow(point,2);
      hist->addBinWithError(xx,yy,dyl,dyh);
    }
    //plot2->addPlotable(plot->residHist(), "P");
    plot2->addPlotable(hist, "P");
    plot2->Draw();
    plot2->GetYaxis()->SetRangeUser(0.5, 1.6);
    plot2->GetYaxis()->SetNdivisions(3, 0, 2);
    plot2->SetTitle("");
    plot2->GetXaxis()->SetTitle("m_{tt} [TeV]");
    plot2->GetXaxis()->SetTitleFont(42);
    plot2->GetXaxis()->SetLabelFont(42);
    plot2->GetXaxis()->SetTitleOffset(0.7);
    plot2->GetXaxis()->SetTitleSize(0.18);
    plot2->GetXaxis()->SetLabelSize(0.13);
    plot2->GetYaxis()->SetTitle("Fit/Data");
    plot2->GetYaxis()->SetTitleFont(42);
    plot2->GetYaxis()->SetLabelFont(42);
    plot2->GetYaxis()->SetTitleOffset(0.3);
    plot2->GetYaxis()->SetTitleSize(0.16);
    plot2->GetYaxis()->SetLabelSize(0.13);
    TLine l(mttlow,1,mttlim,1);
    l.SetLineWidth(2);
    l.SetLineStyle(kDashed);
    l.Draw();
    cplot->SaveAs(Form("%s/jointmtt_%s_%s.eps", outputDir.c_str(), channel, mode.c_str()));
    delete cplot;
  }

  // write workspace in the file 
  work.writeToFile(Form("%s/jointModel_%s.root", outputDir.c_str(), mode.c_str()), true); 
}

int minimize(RooNLLVar* nll, RooFitResult *&res) {
  int printLevel = -1;//ROOT::Math::MinimizerOptions::DefaultPrintLevel();
  RooFit::MsgLevel msglevel = RooMsgService::instance().globalKillBelow();
  if (printLevel < 0) RooMsgService::instance().setGlobalKillBelow(RooFit::FATAL);

  int strat = ROOT::Math::MinimizerOptions::DefaultStrategy();
  RooMinimizer minim(*nll);
  minim.setStrategy(strat);
  minim.setPrintLevel(printLevel);

  int status = minim.minimize(ROOT::Math::MinimizerOptions::DefaultMinimizerType().c_str(), ROOT::Math::MinimizerOptions::DefaultMinimizerAlgo().c_str());

  if (status != 0 && status != 1 && strat < 2)
  {
    strat++;
    //std::cout << "Fit failed with status " << status << ". Retrying with strategy " << strat << std::endl;
    minim.setStrategy(strat);
    status = minim.minimize(ROOT::Math::MinimizerOptions::DefaultMinimizerType().c_str(), ROOT::Math::MinimizerOptions::DefaultMinimizerAlgo().c_str());
  }

  if (status != 0 && status != 1 && strat < 2)
  {
    strat++;
    //std::cout << "Fit failed with status " << status << ". Retrying with strategy " << strat << std::endl;
    minim.setStrategy(strat);
    status = minim.minimize(ROOT::Math::MinimizerOptions::DefaultMinimizerType().c_str(), ROOT::Math::MinimizerOptions::DefaultMinimizerAlgo().c_str());
  }
  if (status != 0 && status != 1)
  {
    //std::cout << "Fit failed with status " << status << std::endl;
  }
  //res = minim.save();

  if (printLevel < 0) RooMsgService::instance().setGlobalKillBelow(msglevel);

  return status;
}

void getSignificance(RooDataSet *data, ModelConfig *sbModel, RooWorkspace *w, double &pnull, double &palt, double &pnullA, bool discovery, double mu) {
  int status;
  double significance = 0;
  double significanceA = 0;
  double p = 0;

  RooFitResult *res = 0;

  RooRealVar *poi = (RooRealVar *)sbModel->GetParametersOfInterest()->first();
  if (!discovery)
    poi->setVal(0);
  else
    poi->setVal(1);

  RooArgSet fAsimovGlobObs;
  poi->setConstant(true);

  // this makes a fit to data!
  //RooAbsData * fAsimovData = AsymptoticCalculator::MakeAsimovData(*data, *sbModel, *poi, fAsimovGlobObs, tmp);

  RooArgSet *asimovParams = 0;
  asimovParams = sbModel->GetPdf()->getParameters(*data);
  RooStats::RemoveConstantParameters(asimovParams);

  // fit data with background only
  RooNLLVar* nll_asimov = (RooNLLVar*)sbModel->GetPdf()->createNLL(*data, RooFit::Constrain(*asimovParams), RooFit::Offset(true), RooFit::Optimize(2), RooFit::Extended(true));
  status = minimizeFancy(nll_asimov, &res);
  if (status < 0) {
    status = minimizeFancy(nll_asimov, &res);
  }

  delete nll_asimov;

  RooAbsData * fAsimovData = AsymptoticCalculator::MakeAsimovData(*sbModel, *asimovParams, fAsimovGlobObs);
  delete asimovParams;
  poi->setConstant(false);

  RooArgSet *allParams = 0;

  poi->setVal(mu);
  poi->setConstant(true);

  allParams = sbModel->GetPdf()->getParameters(*data);
  RooStats::RemoveConstantParameters(allParams);
  RooNLLVar* nll = (RooNLLVar*)sbModel->GetPdf()->createNLL(*data, RooFit::Constrain(*allParams), RooFit::Offset(true), RooFit::Optimize(2), RooFit::Extended(true));

  if (allParams->getSize() > 0) {
    status = minimize(nll, res);
    if (status < 0) {
      status = minimize(nll, res);
    }
    if (status < 0) {
      pnull = -1;
      palt = -1;
      delete allParams;
      delete nll;
      delete fAsimovData;
      return;
    }
  }
  RooAbsReal::setHideOffset(kTRUE);
  double nll_cond = nll->getVal();
  RooAbsReal::setHideOffset(kFALSE);

  delete allParams;
  delete nll;

  poi->setVal(0);
  poi->setConstant(false);

  allParams = sbModel->GetPdf()->getParameters(*data);
  RooStats::RemoveConstantParameters(allParams);

  RooNLLVar* nll2 = (RooNLLVar*)sbModel->GetPdf()->createNLL(*data, RooFit::Constrain(*allParams), RooFit::Offset(true), RooFit::Optimize(2), RooFit::Extended(true));
  status = minimize(nll2, res);
  if (status < 0) {
    status = minimize(nll2, res);
  }
  if (status < 0) {
    pnull = -1;
    palt = -1;
    delete nll2;
    delete allParams;
    delete fAsimovData;
    return;
  }
  if (poi->getVal() < 0) poi->setVal(0);

  RooAbsReal::setHideOffset(kTRUE);
  double nllHat = nll2->getVal();
  RooAbsReal::setHideOffset(kFALSE);
  double muHat = poi->getVal();

  delete nll2;

  double nll_min = nllHat;
  double q0 = 2*(nll_cond - nll_min);
  if (q0 < 0) {
    nll2 = (RooNLLVar*)sbModel->GetPdf()->createNLL(*data, RooFit::Constrain(*allParams), RooFit::Offset(true), RooFit::Optimize(2), RooFit::Extended(true));
    status = minimize(nll2, res);
    if (status < 0) {
      status = minimize(nll2, res);
    }
    if (status < 0) {
      pnull = -1;
      palt = -1;
      delete allParams;
      delete nll2;
      delete fAsimovData;
      return;
    }

  RooAbsReal::setHideOffset(kTRUE);
    nll_min = nll2->getVal();
  RooAbsReal::setHideOffset(kFALSE);
    q0 = 2*(nll_cond - nll_min);
    if (q0 < 0) {
      pnull = -1;
      palt = -1;
      delete allParams;
      delete nll2;
      delete fAsimovData;
      return;
    }
    delete nll2;
  }
  if (discovery) {
    if (muHat < mu) q0 = 0;
  } else {
    if (muHat > mu) q0 = 0;
  }

  delete allParams;

  //sign = int(q0 != 0 ? q0/fabs(q0) : 0);
  significance = std::sqrt(std::fabs(q0));
  pnull = ROOT::Math::normal_cdf_c(significance, 1.);

  std::cout << "getSignificance with mu = " << mu << ", muHat = " << muHat << ", nll_min = " << nll_min << ", nll_cond = " << nll_cond << ", q0 = " << q0 << ", pnull = " << pnull << std::endl;

  poi->setVal(mu);
  poi->setConstant(true);
  allParams = sbModel->GetPdf()->getParameters(*fAsimovData);
  RooStats::RemoveConstantParameters(allParams);

  // asimov
  RooNLLVar* nlla = (RooNLLVar*)sbModel->GetPdf()->createNLL(*fAsimovData, RooFit::Constrain(*allParams), RooFit::Offset(true), RooFit::Optimize(2), RooFit::Extended(true));

  //sbModel->GetGlobalObservables()->Print("v");
  if (allParams->getSize() > 0) {
    status = minimize(nlla, res);
    if (status < 0) {
      status = minimize(nlla, res);
    }
    if (status < 0) {
      palt = -1;
      delete nlla;
      delete allParams;
      delete fAsimovData;
      return;
    }
  }
  RooAbsReal::setHideOffset(kTRUE);
  double nlla_cond = nlla->getVal();
  RooAbsReal::setHideOffset(kFALSE);

  delete allParams;
  delete nlla;

  poi->setVal(0);
  poi->setConstant(false);
  allParams = sbModel->GetPdf()->getParameters(*fAsimovData);
  RooStats::RemoveConstantParameters(allParams);

  RooNLLVar* nlla2 = (RooNLLVar*)sbModel->GetPdf()->createNLL(*fAsimovData, RooFit::Constrain(*allParams), RooFit::Offset(true), RooFit::Optimize(2), RooFit::Extended(true));
  status = minimize(nlla2, res);
  if (status < 0) {
    status = minimize(nlla2, res);
  }
  if (status < 0) {
    palt = -1;
    delete nlla2;
    delete allParams;
    delete fAsimovData;
    return;
  }

  if (poi->getVal() < 0) poi->setVal(0);
  RooAbsReal::setHideOffset(kTRUE);
  double nllHatA = nlla2->getVal();
  RooAbsReal::setHideOffset(kFALSE);
  double muHatA = poi->getVal();

  delete nlla2;

  double nlla_min = nllHatA;
  double q0A = 2*(nlla_cond - nlla_min);
  if (q0A < 0) {
    nlla2 = (RooNLLVar*)sbModel->GetPdf()->createNLL(*fAsimovData, RooFit::Constrain(*allParams), RooFit::Offset(true), RooFit::Optimize(2), RooFit::Extended(true));
    status = minimize(nlla2, res);
    if (status < 0) {
      status = minimize(nlla2, res);
    }
    if (status < 0) {
      palt = -1;
      delete nlla2;
      delete allParams;
      delete fAsimovData;
      return;
    }
  RooAbsReal::setHideOffset(kTRUE);
    nlla_min = nlla2->getVal();
  RooAbsReal::setHideOffset(kFALSE);
    q0A = 2*(nlla_cond - nlla_min);
    if (q0A < 0) {
      palt = -1;
      delete nlla2;
      delete allParams;
      delete fAsimovData;
      return;
    }
    delete nlla2;
  }

  delete allParams;
  delete fAsimovData;

  significanceA = std::sqrt(std::fabs(q0A));
  palt = ROOT::Math::normal_cdf( significanceA - significance, 1.);
  pnullA = ROOT::Math::normal_cdf( significanceA, 1.);

  std::cout << "getSignificance(asimov) with mu = " << mu << ", muHat = " << muHat << ", nll_min = " << nlla_min << ", nll_cond = " << nlla_cond << ", q0A = " << q0A << ", palt = " << palt << ", pnullA = " << pnullA << std::endl;
}

double getTransition(double y, std::vector<double> &ylist, std::vector<double> &xlist) {
  for (size_t i = 1; i < ylist.size(); ++i) {
    if (ylist[i] < y && ylist[i-1] > y) {
      double dx = xlist[i] - xlist[i-1];
      double dy = ylist[i] - ylist[i-1];
      double tantheta = dy/dx; // y = tantheta*(x-x0) + y0 => 
      double xf = (y - ylist[i-1])/tantheta + xlist[i-1];
      return xf;
    }
  }
  return xlist[xlist.size()-1];
}

Results Limits(const char *mfile, const string &mode,
               vector<string> &vfb, vector<string> &vfs, vector<string> &vchannel, double injMu) {
  TFile f(mfile);

  RooWorkspace *work = (RooWorkspace *) f.Get("work");
  //RooAbsPdf *jointModel = work->pdf("combined");

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

  RooRealVar w("w", "w", 1, 0, 10000);                              // event weight

  RooDataSet *data = new RooDataSet("obsData", "mtt", RooArgSet(*x, *idx, w), WeightVar(w));
  for (size_t z = 0; z < vfs.size(); ++z) {
    idx->setLabel(vchannel[z].c_str());

    // inject signal
    load(vfs[z].c_str(), data, *x, w, injMu, idx);
    load(vfb[z].c_str(), data, *x, w, 20e3, idx);
  }

  double p = 1;
  double expP = p;

  AsymptoticCalculator::SetPrintLevel(-1);
  
  int npointsa = 10;  // number of points to scan
  // min and max (better to choose smaller intervals)
  double poimina = 0;
  double poimaxa = 1;
  if (mode == "zp500") poimaxa = 4;
  if (mode == "zp750") { poimaxa = 2; npointsa = 40; }
  if (mode == "zp1tev") { poimaxa = 3; npointsa = 10; }
  if (mode == "zp125tev") { poimaxa = 1.2; npointsa = 10; }
  if (mode == "zp15tev") { poimaxa = 0.2; npointsa = 20; }
  if (mode == "zp175tev") { poimaxa = 0.4; npointsa = 10; }
  if (mode == "zp2tev") { poimaxa = 1; npointsa = 10;}
  if (mode == "zp25tev") { poimaxa = 2; npointsa = 10; }
  if (mode == "zp3tev") { poimaxa = 5; npointsa = 10; }


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
  //double expected_pnull = expP;
  //double CLsplusbD = p;

  double mu_up = 0;
  double mu_up_1p = 0;
  double mu_up_1m = 0;
  double mu_up_2p = 0;
  double mu_up_2m = 0;
  double mu_up_obs = 0;
  
  std::vector<double> vscans;
  std::vector<double> vscana;
  std::vector<double> vscana1p;
  std::vector<double> vscana1m;
  std::vector<double> vscana2p;
  std::vector<double> vscana2m;
  std::vector<double> mulist;
  double old_pnull = 1;
  double old_palt = 1;
  for (double my_mu = 0; my_mu < poimaxa; my_mu += poimaxa/((double)npointsa)) {
    getSignificance(data, mc, work, scan_pnull, scan_palt, scan_pnullA, false, my_mu);
    if (scan_pnull < 0 || scan_palt < 0) {
      scan_pnull = 1;//old_pnull;
      scan_palt = 1;//old_palt;
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
  }
  mu_up_obs = getTransition(0.05, vscans, mulist);
  mu_up = getTransition(0.05, vscana, mulist);
  mu_up_1p = std::fabs(getTransition(0.05, vscana1p, mulist) - mu_up);
  mu_up_1m = std::fabs(getTransition(0.05, vscana1m, mulist) - mu_up);
  mu_up_2p = std::fabs(getTransition(0.05, vscana2p, mulist) - mu_up);
  mu_up_2m = std::fabs(getTransition(0.05, vscana2m, mulist) - mu_up);

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
  gscana2->GetXaxis()->SetRangeUser(0,poimaxa);

  gscana->SetMarkerStyle(20);
  gscana->SetMarkerSize(1.0);
  gscans->SetMarkerStyle(20);
  gscans->SetMarkerSize(1.0);
  gscanb->SetMarkerStyle(20);
  gscanb->SetMarkerSize(1.0);
  gscan->SetMarkerStyle(20);
  gscan->SetMarkerSize(1.0);

  TLine lin(0, 0.05, poimaxa, 0.05);
  lin.SetLineWidth(2);
  lin.SetLineColor(kRed);
  gscana2->Draw("A E3");
  gscana1->Draw("E3");
  gscana->Draw("LP");
  gscans->Draw("LP");
  gscanb->Draw("LP");
  gscan->Draw("LP");
  lin.Draw();

  cscan->SaveAs(Form("%s/cscan_%s.eps", outputDir.c_str(), mode.c_str()));

  delete cscan;
  delete gscans;
  delete gscan;
  delete gscanb;
  delete gscana;
  delete gscana1;
  delete gscana2;
  delete data;
  delete sbModel;
  delete bModel;

  return Results(mu_up, mu_up_1m, mu_up_1p, mu_up_2m, mu_up_2p, CLsplusbD, expected_pnull, mu_up_obs);

  //return Results(r->GetExpectedUpperLimit(0), std::fabs(r->GetExpectedUpperLimit(0) - r->GetExpectedUpperLimit(-1)),
  //                                            std::fabs(r->GetExpectedUpperLimit(0) - r->GetExpectedUpperLimit(1)),
  //                                            std::fabs(r->GetExpectedUpperLimit(0) - r->GetExpectedUpperLimit(-2)),
  //                                            std::fabs(r->GetExpectedUpperLimit(0) - r->GetExpectedUpperLimit(2)),
  //                                            p, expP, r->UpperLimit());
}

