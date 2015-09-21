#include "ParseUtils.h"
#include "SignalModel.h"
#include "BkgModel.h"

#include "Math/MinimizerOptions.h"

#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <sstream>
#include <cmath>

#include "TStyle.h"
#include "TBox.h"

#include "RooWorkspace.h"
#include "RooDataSet.h"
#include "RooRealVar.h"
#include "TTree.h"
#include "TFile.h"
#include "RooAbsPdf.h"
#include "RooGlobalFunc.h"

#include "TH2F.h"
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
#include "RooPlot.h"
#include "TLatex.h"
#include "TLegend.h"
#include "RooHist.h"
#include "TLine.h"
#include "TPad.h"

#include <map>

#include "RooSimultaneous.h"
#include "RooExtendPdf.h"
#include "RooAddPdf.h"

using namespace std;
using namespace RooFit;
using namespace RooStats;

int main(int argc, char **argv) {
  int help = 0;
  string _outdir = "results";
  string _bkg = "ttres_new/bkg.root";
  float _L = 20e3;
  string _suffix = "bkg";

  static struct extendedOption extOpt[] = {
      {"help",            no_argument,       &help,   1, "Display help", &help, extendedOption::eOTInt},
      {"outdir",          required_argument,     0, 'd', "Output plot directory", &_outdir, extendedOption::eOTString},
      {"bkg",             required_argument,     0, 'b', "Background input file", &_bkg, extendedOption::eOTString},
      {"L",               required_argument,     0, 'L', "Luminotisty to multiply data.", &_L, extendedOption::eOTFloat},
      {"suffix",          required_argument,     0, 'n', "Suffix to append in output files.", &_suffix, extendedOption::eOTString},
      {0, 0, 0, 0, 0, 0, extendedOption::eOTInt}
  };

  if (!parseArguments(argc, argv, extOpt) || help) {
    dumpHelp("FitBkg", extOpt, "FitBkg\nFit background model from input.\n");
    return 0;
  } else {
    std::cout << "Dumping options:" << std::endl;
    dumpOptions(extOpt);
  }

  vector<std::string> channels;
  channels.push_back("bmu");
  channels.push_back("be");

  std::map<int, std::string> chmap;
  for (size_t i = 0; i < channels.size(); ++i) {
    chmap[(int) i] = channels[i];
  }

  RooWorkspace *work = new RooWorkspace("work");
  RooRealVar *x = new RooRealVar("x", "x", 1.0e3, 5.0e3);
  RooRealVar *w = new RooRealVar("w", "w", 1, 0, 100e3);
  RooRealVar *mu = new RooRealVar("mu", "mu", 0, 0, 100);
  work->import(*x);
  work->import(*w);
  work->import(*mu);

  RooCategory *idx = new RooCategory("channel", "channel");
  for (size_t z = 0; z < channels.size(); ++z) {
    idx->defineType(channels[z].c_str(), (int) z);
  }
  work->import(*idx);

  std::map<std::string, BkgModel *> bkg;

  for (size_t zc = 0; zc < channels.size(); ++zc) {
    bkg.insert(std::make_pair<std::string, BkgModel *>(\
            std::string(Form("%s", channels[zc].c_str())), \
            new BkgModel("bkg", 1.0, -1.0, channels[zc], "", work)));
  }

  RooArgSet nuisParam("nuisParam");
  RooArgSet globalObs("globalObs");

  map<string, RooAbsPdf *> jointMap;
  for (size_t zc = 0; zc < channels.size(); ++zc) {
    RooArgSet ctr_local;
    BkgModel *b_n = bkg[Form("%s", channels[zc].c_str())];
    RooAbsPdf *b = b_n->getPdf();

    // load bkg parameters
    RooRealVar *nbkg = new RooRealVar(Form("nbkg_%s", channels[zc].c_str()), "nbkg", 0, 1e6);
    nbkg->setConstant(false);
    nuisParam.add(*nbkg);
    
    RooRealVar *p1 = b_n->param("p1");
    RooRealVar *p2 = b_n->param("p2");
    RooRealVar *p3 = b_n->param("p3");
    p1->setConstant(false);
    p2->setConstant(false);
    //p3->setConstant(false);
    nuisParam.add(*p1);
    nuisParam.add(*p2);
    //nuisParam.add(*p3);

    RooAbsPdf *model = new RooExtendPdf(Form("model_%s", channels[zc].c_str()), "model", *b, *nbkg);
    jointMap[channels[zc]] =  model;

  }
  RooSimultaneous *jointModel = new RooSimultaneous("combined", "combined model", jointMap, *idx);
  work->import(*jointModel);

  RooDataSet *data = new RooDataSet("data", "", RooArgSet(*work->var("x"), *work->cat("channel"), *work->var("w")), WeightVar(*work->var("w")));
  readData(data, _bkg, -1, "", work, _L, true);

  ROOT::Math::MinimizerOptions::SetDefaultMinimizer("Minuit2");
  ROOT::Math::MinimizerOptions::SetDefaultStrategy(1);

  RooFitResult *fr = jointModel->fitTo(*data, SumW2Error(true), Minimizer("Minuit2", "Migrad"), Save(true), Strategy(2));
  fr->Print();

  double bins[] = {1000,1200,1400,1600,1800,2000,2200,2400,2600,2900,3200,3600};
  unsigned int nbins = sizeof(bins)/sizeof(double) - 1;
  std::vector<TH1F *> mtt;
  std::vector<TH1F *> mtt_data;
  std::vector<TH1F *> mtt_syst;

  gStyle->SetOptStat(0);

  TFile *fout = new TFile(Form("%s/fitbkg_%s.root", _outdir.c_str(), _suffix.c_str()), "recreate");

  for (int ch = 0; ch <= 1; ++ch) {
    std::string &channel = chmap[ch];
    mtt.push_back(new TH1F(Form("mtt%s", channel.c_str()), "", nbins, bins));
    mtt_data.push_back(new TH1F(Form("mtt_data_%s", channel.c_str()), "", nbins, bins));
    mtt_syst.push_back(new TH1F(Form("mtt%s_systbkg", channel.c_str()), "", nbins, bins));

    data->fillHistogram(mtt_data[ch], RooArgList(*x), Form("channel==channel::%s", channel.c_str()));

    RooArgSet condObs;
    condObs.add(*idx);
    idx->setLabel(channel.c_str());
    idx->setConstant(true);
    //jointMap[channel]->fillHistogram(mtt[ch], RooArgList(*x), 1.0, 0, false, &condObs, true);
    //RooAbsReal *integ = jointMap[channel]->createIntegral(*x, NormSet(*x), Range(Form("mtt_%s_bin%d", channel.c_str(), i)));
    RooAbsReal *integ = jointModel->createCdf(*x, RooArgSet(*idx));
    for (int i = 1; i <= mtt[ch]->GetNbinsX(); ++i) {
      double xc = mtt[ch]->GetBinCenter(i);
      double xl = mtt[ch]->GetXaxis()->GetBinLowEdge(i);
      double xh = mtt[ch]->GetXaxis()->GetBinUpEdge(i);
      //x->setVal(xc);
      //double y = jointMap[channel]->getVal();
      x->setVal(xh);
      double yh = integ->getVal();
      x->setVal(xl);
      double yl = integ->getVal();
      double y = (yh - yl)*jointMap[channel]->expectedEvents(*x);
      mtt[ch]->SetBinContent(i, y);
      mtt[ch]->SetBinError(i, sqrt(y));
      mtt_syst[ch]->SetBinContent(i, mtt_data[ch]->GetBinContent(i));
    }
    idx->setConstant(false);
    x->setConstant(false);


    TCanvas *c2 = new TCanvas("ch2", "", 800, 600);
    TLegend l(0.7,0.7,0.89,0.89);
    l.SetBorderSize(0);

    TPad *pad_ratio = 0;
    c2->Divide(1, 2, 0.015, 0.01);
    pad_ratio = (TPad *) c2->cd(2);
    pad_ratio->SetPad(0,0,1,0.30);
    pad_ratio->SetTopMargin(0.01);
    pad_ratio->SetBottomMargin(0.45);
    c2->cd(1)->SetPad(0,0.2,1,1);
    c2->cd(1)->SetBottomMargin(0.13);

    mtt[ch]->GetXaxis()->SetTitle("m_{tt} [GeV]");
    mtt[ch]->GetYaxis()->SetTitle("Entries");
    l.AddEntry(mtt[ch], "Histogram from fit", "F");
    l.AddEntry(mtt_data[ch], "Input data", "L");

    mtt[ch]->SetMinimum(5e-1);
    mtt[ch]->GetYaxis()->SetTitleFont(42);
    mtt[ch]->GetYaxis()->SetLabelFont(42);
    mtt[ch]->GetYaxis()->SetTitleOffset(0.75);
    mtt[ch]->GetYaxis()->SetTitleSize(0.06);
    mtt[ch]->GetYaxis()->SetLabelSize(0.05);
    mtt[ch]->SetLineWidth(2);

    mtt[ch]->Draw("hist");
    mtt_data[ch]->Draw("e1 same");

    l.Draw();
    TLatex t;
    t.SetNDC();
    t.SetTextSize(0.02);
    float xs = 0.7;
    float ys = 0.62;
    for (size_t z = 0; z < fr->floatParsFinal().getSize(); ++z) {
      t.DrawLatex(xs, ys, Form("%s=%3.2e#pm%3.2e", fr->floatParsFinal().at(z)->GetName(), ((RooRealVar *) fr->floatParsFinal().at(z))->getVal(), ((RooRealVar *) fr->floatParsFinal().at(z))->getError()));
      ys -= 0.04;
    }
    t.DrawLatex(xs, ys, Form("Channel %s", channel.c_str()));
    ys -= 0.04;
    c2->cd(1)->SetLogy(1);
    c2->cd(2);

    TH1F *rat_mtt = (TH1F *) mtt[ch]->Clone(Form("rat_%s", mtt[ch]->GetName()));
    rat_mtt->Divide(mtt[ch], mtt_data[ch], 1, 1, "B");
    rat_mtt->GetYaxis()->SetRangeUser(0.8, 1.2);
    rat_mtt->GetYaxis()->SetNdivisions(3, 0, 2);
    rat_mtt->SetTitle("");
    rat_mtt->GetXaxis()->SetTitle("m_{tt} [GeV]");
    rat_mtt->GetXaxis()->SetTitleFont(42);
    rat_mtt->GetXaxis()->SetLabelFont(42);
    rat_mtt->GetXaxis()->SetTitleOffset(0.7);
    rat_mtt->GetXaxis()->SetTitleSize(0.18);
    rat_mtt->GetXaxis()->SetLabelSize(0.13);
    rat_mtt->GetYaxis()->SetTitle("Fit/Data");
    rat_mtt->GetYaxis()->SetTitleFont(42);
    rat_mtt->GetYaxis()->SetLabelFont(42);
    rat_mtt->GetYaxis()->SetTitleOffset(0.3);
    rat_mtt->GetYaxis()->SetTitleSize(0.16);
    rat_mtt->GetYaxis()->SetLabelSize(0.13);
    rat_mtt->Draw();

    TLine li(work->var("x")->getMin(),1,work->var("x")->getMax(),1);
    li.SetLineWidth(2);
    li.SetLineStyle(kDashed);
    li.Draw();

    c2->SaveAs(Form("%s/fitbkghist_%s_%s.eps", _outdir.c_str(), channel.c_str(), _suffix.c_str()));
    delete c2;
  }


  delete data;

  fout->cd();
  for (int ch = 0; ch <= 1; ++ch) {
    mtt[ch]->Write();
    mtt_data[ch]->Write();
    mtt_syst[ch]->Write();
  }
  fout->Close();

  return 0;
}

