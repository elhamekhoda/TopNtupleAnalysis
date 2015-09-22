#include "ParseUtils.h"
#include "SignalModel.h"
#include "BkgModel.h"

#include "RooBinning.h"

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

using namespace std;
using namespace RooFit;
using namespace RooStats;

int main(int argc, char **argv) {
  int help = 0;
  string _outdir = "results";
  string _workspace = "results/workspace_zp2tev.root";
  string _bkg = "ttres_new/bkg.root";
  string _signal = "ttres_new/zp2tev.root";
  float _sigweight = 0.0;
  float _mu = -1;
  float _L = 20e3;
  string _suffix = "zp2tev";

  static struct extendedOption extOpt[] = {
      {"help",            no_argument,       &help,   1, "Display help", &help, extendedOption::eOTInt},
      {"outdir",          required_argument,     0, 'd', "Output plot directory", &_outdir, extendedOption::eOTString},
      {"workspace",       required_argument,     0, 'w', "Workspace file", &_workspace, extendedOption::eOTString},
      {"bkg",             required_argument,     0, 'b', "Background input file", &_bkg, extendedOption::eOTString},
      {"signal",          required_argument,     0, 's', "Signal input file", &_signal, extendedOption::eOTString},
      {"sigweight",       required_argument,     0, 'S', "Signal weight", &_sigweight, extendedOption::eOTFloat},
      {"mu",              required_argument,     0, 'm', "If >= 0, fix mu at this value.", &_mu, extendedOption::eOTFloat},
      {"L",               required_argument,     0, 'L', "Luminotisty to multiply data.", &_L, extendedOption::eOTFloat},
      {"suffix",          required_argument,     0, 'n', "Suffix to append in output files.", &_suffix, extendedOption::eOTString},
      {0, 0, 0, 0, 0, 0, extendedOption::eOTInt}
  };

  if (!parseArguments(argc, argv, extOpt) || help) {
    dumpHelp("FitCombined", extOpt, "FitCombined\nFit combined model in workspace to bkg + signal*signalweight from input.\n");
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

  TFile f(_workspace.c_str());
  RooWorkspace *work = (RooWorkspace *) f.Get("work");

  RooRealVar *mu = work->var("mu");
  RooCategory *idx = work->cat("channel");
  RooRealVar *x = work->var("x");

  if (_mu >= 0) {
    mu->setVal(_mu);
    mu->setConstant(true);
  } else {
    mu->setConstant(false);
  }

  ModelConfig *mc = (ModelConfig*)work->obj("ModelConfig");
  RooAbsPdf *jointModel = work->pdf("combined");

  RooDataSet *data = new RooDataSet("data", "", RooArgSet(*work->var("x"), *work->cat("channel"), *work->var("w")), WeightVar(*work->var("w")));
  readData(data, _bkg, -1, "", work, _L, true);
  if (_sigweight > 0)
    readData(data, _signal, -1, "", work, _L*_sigweight, true);

  // set syst. params. to zero
  RooRealVar *p = 0;
  RooFIter pi = work->set("nuisParams")->fwdIterator();
  while ( (p = (RooRealVar *) pi.next()) ) {
    if (std::string(p->GetName()).find("a_") != std::string::npos) {
      std::cout << "Setting " << p->GetName() << " to zero." << std::endl;
      p->setVal(0);
    }
  }
  work->var("mu")->setVal(0);

  //RooFitResult *pre_fr = jointModel->fitTo(*data, SumW2Error(true), Minimizer("Minuit2", "Migrad"), Save(true), Strategy(2));
  //pre_fr->Print();

  // now let them free after first fit
  /*
  p = 0;
  pi = work->set("nuisParams")->fwdIterator();
  while ( (p = (RooRealVar *) pi.next()) ) {
    if (std::string(p->GetName()).find("a_") != std::string::npos) {
      std::cout << "Setting " << p->GetName() << " to zero." << std::endl;
      p->setVal(0);
      p->setConstant(false);
    }
  }
  */
  //RooFitResult *fr = jointModel->fitTo(*data, SumW2Error(true), Minimizer("Minuit2", "Migrad"), Save(true), Strategy(2));
  ROOT::Math::MinimizerOptions::SetDefaultMinimizer("Minuit2");
  ROOT::Math::MinimizerOptions::SetDefaultStrategy(1);

  RooFitResult *fr = 0;
  RooArgSet *params = 0;
  params = jointModel->getParameters(*data);
  RooStats::RemoveConstantParameters(params);
  RooNLLVar* nll = (RooNLLVar*) jointModel->createNLL(*data, RooFit::Constrain(*params), RooFit::Offset(true), RooFit::Optimize(2), RooFit::Extended(true));
  int status = minimizeFancy(nll, &fr);
  
  if (work->var("mu")->getVal() < 0)
    work->var("mu")->setVal(0);

  /*
  RooFitResult *fr = jointModel->fitTo(*data, SumW2Error(true), Minimizer("Minuit2", "Migrad"), Save(true), Strategy(2));
  if (fr->status() != 0 && fr->status() != 1) {
    fr = jointModel->fitTo(*data, SumW2Error(true), Minimizer("Minuit2", "Migrad"), Save(true), Strategy(1));
    if (fr->status() != 0 && fr->status() != 1) {
      fr = jointModel->fitTo(*data, SumW2Error(true), Minimizer("Minuit2", "Migrad"), Save(true), Strategy(0));
      if (fr->status() != 0 && fr->status() != 1) {
        fr = jointModel->fitTo(*data, SumW2Error(true), Minimizer("Minuit", "Migrad"), Save(true), Strategy(2));
        if (fr->status() != 0 && fr->status() != 1) {
          fr = jointModel->fitTo(*data, SumW2Error(true), Minimizer("Minuit", "Migrad"), Save(true), Strategy(1));
          if (fr->status() != 0 && fr->status() != 1) {
            fr = jointModel->fitTo(*data, SumW2Error(true), Minimizer("Minuit", "Migrad"), Save(true), Strategy(0));
          }
        }
      }
    }
  }
  */
  fr->Print();

  RooBinning b(x->getMin(), x->getMax());
  b.addUniform((int) ((2e3-x->getMin())/100.0), x->getMin(), 2e3);
  b.addUniform((int) ((2.5e3-2e3)/250.0), 2e3, 2.5e3);
  b.addUniform((int) ((x->getMax()-2.5e3)/500.0), 2.5e3, x->getMax());

  for (int ch = 0; ch <= 1; ++ch) {
    std::string &channel = chmap[ch];
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


    RooPlot *frame = x->frame(Title(" "));
    frame->GetXaxis()->SetTitle("m_{tt} [GeV]");
    frame->GetYaxis()->SetTitle("Entries");
    data->plotOn(frame, Name("dataplot"), Cut(Form("channel==channel::%s", channel.c_str())), Binning(b));
    jointModel->plotOn(frame, Name("pdfplotb"), Components(Form("bkg_shape_bkg_%s", channel.c_str())), LineStyle(kDashed), LineColor(kBlue), Slice(*idx,channel.c_str()), ProjWData(*x, *data), Binning(b));
    jointModel->plotOn(frame, Name("pdfplots"), Components(Form("fsig_shape_%s", channel.c_str())), LineStyle(kDashed), LineColor(kRed), Slice(*idx,channel.c_str()), ProjWData(*x, *data), Binning(b));
    jointModel->plotOn(frame, Name("pdfplot"), LineColor(kBlack), Slice(*idx,channel.c_str()), ProjWData(*x, *data), Binning(b));
    l.AddEntry(frame->findObject("dataplot"), "Input data", "L");
    l.AddEntry(frame->findObject("pdfplotb"), "Background fit", "L");
    l.AddEntry(frame->findObject("pdfplots"), "Signal fit", "L");
    l.AddEntry(frame->findObject("pdfplot"), "Signal + background fit", "L");
    frame->SetMinimum(5e-1);
    frame->GetYaxis()->SetTitleFont(42);
    frame->GetYaxis()->SetLabelFont(42);
    frame->GetYaxis()->SetTitleOffset(0.75);
    frame->GetYaxis()->SetTitleSize(0.06);
    frame->GetYaxis()->SetLabelSize(0.05);
    frame->Draw();
    l.Draw();
    TLatex t;
    t.SetNDC();
    t.SetTextSize(0.02);
    if (_mu >= 0) {
      t.DrawLatex(0.7, 0.66, Form("Fixed #mu=%f", mu->getVal()));
    } else {
      size_t idx = -1;
      for (size_t z = 0; z < fr->floatParsFinal().getSize(); ++z) {
        if (std::string(fr->floatParsFinal().at(z)->GetName()) == "mu") {
          idx = z;
          break;
        }
      }
      t.DrawLatex(0.7, 0.66, Form("#mu_{fit}=%f#pm%f", ((RooRealVar *) fr->floatParsFinal().at(idx))->getVal(), ((RooRealVar *) fr->floatParsFinal().at(idx))->getError()));
    }
    t.DrawLatex(0.7, 0.62, Form("Injected signal weight=%f", _sigweight));
    float xs = 0.7;
    float ys = 0.62;
    ys -= 0.04;
    for (size_t z = 0; z < fr->floatParsFinal().getSize(); ++z) {
      if (std::string(fr->floatParsFinal().at(z)->GetName()) != "mu" && std::string(fr->floatParsFinal().at(z)->GetName()).find("a_") == std::string::npos) {
        t.DrawLatex(xs, ys, Form("%s=%3.2e#pm%3.2e", fr->floatParsFinal().at(z)->GetName(), ((RooRealVar *) fr->floatParsFinal().at(z))->getVal(), ((RooRealVar *) fr->floatParsFinal().at(z))->getError()));
        ys -= 0.04;
      }
    }
    t.DrawLatex(xs, ys, Form("#chi^2/ndof=%3.3e", frame->chiSquare()));
    ys -= 0.04;
    t.DrawLatex(xs, ys, Form("Channel %s", channel.c_str()));
    ys -= 0.04;
    c2->cd(1)->SetLogy(1);
    c2->cd(2);

    RooPlot *frame_rat = x->frame(Title(" "));
    RooCurve* curveb = (RooCurve*) frame->findObject("pdfplotb");
    RooCurve* curve = (RooCurve*) frame->findObject("pdfplot");
    RooHist* histnum = (RooHist*) frame->findObject("dataplot");
    RooHist* hist = new RooHist(frame->getFitRangeBinW()) ;
    double maxSB = 1;
    for (Int_t i = 0; i < histnum->GetN(); i++) {
      Double_t xx,point;
      histnum->GetPoint(i,xx,point);

      Double_t ybkg = curveb->interpolate(xx);
      Double_t ysb = curve->interpolate(xx);
      if (ysb/ybkg > maxSB) maxSB = ysb/ybkg;

      Double_t yy = 1;
      if (point != 0) yy = curve->interpolate(xx)/point;
      Double_t dyl = 0;
      if (point) dyl = curve->interpolate(xx)*histnum->GetErrorYlow(i)/std::pow(point,2);
      Double_t dyh = 0;
      if (point) dyh = curve->interpolate(xx)*histnum->GetErrorYhigh(i)/std::pow(point,2);
      hist->addBinWithError(xx,yy,dyl,dyh);
    }
    std::cout << "Maximum of (S+B)/B = " << maxSB << " in channel " << channel << std::endl;
    //frame_rat->addPlotable(frame->residHist(), "P");
    frame_rat->addPlotable(hist, "P");
    frame_rat->Draw();
    frame_rat->GetYaxis()->SetRangeUser(0.8, 1.2);
    frame_rat->GetYaxis()->SetNdivisions(3, 0, 2);
    frame_rat->SetTitle("");
    frame_rat->GetXaxis()->SetTitle("m_{tt} [GeV]");
    frame_rat->GetXaxis()->SetTitleFont(42);
    frame_rat->GetXaxis()->SetLabelFont(42);
    frame_rat->GetXaxis()->SetTitleOffset(0.7);
    frame_rat->GetXaxis()->SetTitleSize(0.18);
    frame_rat->GetXaxis()->SetLabelSize(0.13);
    frame_rat->GetYaxis()->SetTitle("Fit/Data");
    frame_rat->GetYaxis()->SetTitleFont(42);
    frame_rat->GetYaxis()->SetLabelFont(42);
    frame_rat->GetYaxis()->SetTitleOffset(0.3);
    frame_rat->GetYaxis()->SetTitleSize(0.16);
    frame_rat->GetYaxis()->SetLabelSize(0.13);
    TLine li(work->var("x")->getMin(),1,work->var("x")->getMax(),1);
    li.SetLineWidth(2);
    li.SetLineStyle(kDashed);
    li.Draw();
    c2->SaveAs(Form("%s/combinedfit_%s_%s.eps", _outdir.c_str(), channel.c_str(), _suffix.c_str()));
    delete c2;
  }

  std::vector<std::string> np_name;
  std::vector<double> np_val;
  std::vector<double> np_err;
  for (size_t z = 0; z < fr->floatParsFinal().getSize(); ++z) {
    std::string fancyName;
    if (std::string(fr->floatParsFinal().at(z)->GetName()).find("a_") != std::string::npos) {
      fancyName = std::string("#alpha(")+std::string(fr->floatParsFinal().at(z)->GetName()).substr(2)+std::string(")");
    } else if (std::string(fr->floatParsFinal().at(z)->GetName()) == std::string("mu")) {
      fancyName = "#mu";
    } else fancyName = fr->floatParsFinal().at(z)->GetName();

    if (std::string(fr->floatParsFinal().at(z)->GetName()).find("a_") != std::string::npos || 
        std::string(fr->floatParsFinal().at(z)->GetName()) == std::string("mu")) {
      np_name.push_back(fancyName);
      np_val.push_back(((RooRealVar *) fr->floatParsFinal().at(z))->getVal());
      np_err.push_back(((RooRealVar *) fr->floatParsFinal().at(z))->getError());
    }
  }

  // make nuisParam plot
  gStyle->SetOptStat(0);
  TCanvas *cn = new TCanvas("cn", "", 500, 600);
  TH2F *hn = new TH2F("hn", " ; #hat{#alpha} ; ", 10, -3, 3, np_name.size(), 0.0, 1.0*np_name.size());
  cn->SetLeftMargin(0.2);
  cn->SetBottomMargin(0.20);
  for (size_t z = 0 ; z < np_name.size(); ++z) {
    hn->GetYaxis()->SetBinLabel(z+1, np_name[z].c_str());
  }
  hn->GetYaxis()->SetTitleSize(0.05);
  hn->GetXaxis()->SetTitleSize(0.05);
  hn->GetYaxis()->SetTitleFont(42);
  hn->GetXaxis()->SetTitleFont(42);
  hn->GetYaxis()->SetTitleOffset(1.8);
  hn->Draw("hist");
  TGraphErrors *nps = new TGraphErrors(np_name.size());
  for (size_t z = 0 ; z < np_name.size(); ++z) {
    nps->SetPoint(z, np_val[z], 1.0*z+0.5);
    nps->SetPointError(z, np_err[z], 0);
  }
  TBox s2(-2, 1.0*np_name.size(), 2, 0);
  s2.SetFillStyle(1001);
  s2.SetFillColor(5);
  TBox s1(-1, 1.0*np_name.size(), 1, 0);
  s1.SetFillStyle(1001);
  s1.SetFillColor(3);
  s2.Draw();
  s1.Draw();

  TLine lin(0, 0, 0, 1.0*np_name.size());
  lin.SetLineStyle(kDashed);
  lin.SetLineWidth(2);
  lin.Draw();
  nps->SetLineWidth(3);
  nps->SetMarkerStyle(21);
  nps->SetMarkerColor(4);
  nps->SetMarkerSize(1.5);
  nps->Draw("P");

  cn->SaveAs(Form("%s/combinedfit_nuisParam_%s.eps", _outdir.c_str(), _suffix.c_str()));
  delete cn;

  //delete data;

  return 0;
}

