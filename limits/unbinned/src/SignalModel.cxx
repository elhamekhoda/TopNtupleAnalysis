#include <string>
#include "SignalModel.h"
#include <fstream>
#include <iostream>
#include "Models.h"
#include "RooExtendPdf.h"
#include "RooWorkspace.h"
#include "RooRealVar.h"
#include <vector>
#include "TCanvas.h"
#include "RooFitResult.h"
#include "RooAbsPdf.h"
#include "RooRealVar.h"
#include "TH2.h"
#include "RooFormulaVar.h"
#include "RooPlot.h"
#include "TLatex.h"
#include "RooAddPdf.h"
#include "RooGaussian.h"
#include "TLegend.h"
#include "RooNLLVar.h"
#include "FitUtils.h"
#include "RooBreitWigner.h"
#include "RooLandau.h"
#include "RooFFTConvPdf.h"
#include "RooNumConvPdf.h"
#include "RooGenericPdf.h"
#include "RooConstVar.h"

using namespace std;
using namespace RooFit;

double mttlim = 5e3;
double mttlow = 0.0e3;

SignalModel::SignalModel(const std::string &name, double xsec, double param, const std::string &channel, const std::string &syst,
                         RooWorkspace *work)
  : BaseSignalModel(name, xsec, param, channel, syst, work) {

  /*
  m_p["xi"] = new RooRealVar(Form("xi_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "sig_xi", 1e3, mttlow, mttlim);             // skew-normal mean in signal
  m_p["omega"] = new RooRealVar(Form("omega_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "sig_omega", 0.1e3, 0.01e3, 2e3);          // skew-normal scale in signal
  m_p["alpha"] = new RooRealVar(Form("alpha_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "sig_alpha", -1.0, -22.0, 1);        // skew-normal shape in signal

  RooAbsPdf *skewnormal = new SkewNormalPdf(Form("skewnormal_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "skewnormal", *work->var("x"), *m_p["xi"], *m_p["omega"], *m_p["alpha"]);

  m_p["n0"] = new RooRealVar(Form("n0_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "n0", 0, 0, 1);

  // as in W'->tb
  m_p["m1"] = new RooRealVar(Form("m1_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "m1", 2e3, mttlow, mttlim);                     // gaussian mean in signal
  m_p["s1"] = new RooRealVar(Form("s1_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "s1", 0.5e3, 0.5e3, 2e3);                   // guassian sigma in signal

  //m_p["n1"] = new RooRealVar(Form("n1_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "n1", 0, 0, 1);
  //m_p["m2"] = new RooRealVar(Form("m2_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "m2", 2e3, mttlow, mttlim);                     // gaussian mean in signal
  //m_p["s2"] = new RooRealVar(Form("s2_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "s2", 0.5e3, 0.05e3, 2e3);                   // guassian sigma in signal

  RooAbsPdf *g1 = new RooGaussian(Form("g1_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "g1", *work->var("x"), *m_p["m1"], *m_p["s1"]);
  //RooAbsPdf *g2 = new RooGaussian(Form("g2_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "g2", *work->var("x"), *m_p["m2"], *m_p["s2"]);

  //RooAbsPdf *sig_shape = new RooAddPdf(Form("sig_shape_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "sig_shape", RooArgList(*skewnormal, *g1, *g2), RooArgList(*m_p["n0"], *m_p["n1"]), true);
  RooAbsPdf *sig_shape = new RooAddPdf(Form("sig_shape_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "sig_shape", RooArgList(*skewnormal, *g1), RooArgList(*m_p["n0"]), true);
  */

  /*
  m_p["ml"] = new RooRealVar(Form("ml_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "ml", 1e3, mttlow, mttlim);             // skew-normal mean in signal
  m_p["sl"] = new RooRealVar(Form("sl_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "sl", 0.1e3, 0.05e3, 2e3);          // skew-normal scale in signal
  RooAbsPdf *landau = new RooBreitWigner(Form("bw_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "", *work->var("x"), *m_p["ml"], *m_p["sl"]);

  m_p["mg"] = new RooRealVar(Form("mg_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "mg", 1e3, mttlow, mttlim);             // skew-normal mean in signal
  m_p["sg"] = new RooRealVar(Form("sg_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "sg", 0.1e3, 0.1e3, 2e3);          // skew-normal scale in signal
  RooAbsPdf *gauss = new RooGaussian(Form("gauss_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "", *work->var("x"), *m_p["mg"], *m_p["sg"]);

  work->var("x")->setBins(10000, "cache");
  RooFFTConvPdf *sig_shape = new RooFFTConvPdf(Form("sig_shape_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()),"landau (X) gauss", *work->var("x"), *landau, *gauss) ;
  */

  m_p["mg"] = new RooRealVar(Form("mg_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "mg", 6e3, mttlow, mttlim);             // skew-normal mean in signal
  m_p["sg"] = new RooRealVar(Form("sg_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "sg", 0.5e3, 0.1e3, 4e3);          // skew-normal scale in signal
  m_p["alpha"] = new RooRealVar(Form("alpha_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "alpha", -20.0, -100.0, 0.0);          // skew-normal scale in signal
  RooGenericPdf *skewnormal = new RooGenericPdf(Form("skewnormal_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "(2.0/@1)*exp(-0.5*((@3-@0)/@1)**2)*0.5*(1+TMath::Erf(@2*(@3-@0)/(@1*@4)))", RooArgList(*m_p["mg"], *m_p["sg"], *m_p["alpha"], *work->var("x"), RooConst(std::sqrt(2))));

  m_p["n0"] = new RooRealVar(Form("n0_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "n0", 0, 0, 1);
  m_p["m1"] = new RooRealVar(Form("m1_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "m1", 0.5e3, mttlow, mttlim);                     // gaussian mean in signal
  m_p["s1"] = new RooRealVar(Form("s1_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "s1", 0.5e3, 0.1e3, 4e3);                   // guassian sigma in signal

  RooAbsPdf *g1 = new RooBreitWigner(Form("g1_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "g1", *work->var("x"), *m_p["m1"], *m_p["s1"]);

  //m_p["n1"] = new RooRealVar(Form("n1_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "n1", 0, 0, 1);
  //m_p["m2"] = new RooRealVar(Form("m2_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "m2", 2e3, mttlow, mttlim);                     // gaussian mean in signal
  //m_p["s2"] = new RooRealVar(Form("s2_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "s2", 0.5e3, 0.1e3, 2e3);                   // guassian sigma in signal

  //RooAbsPdf *g2 = new RooBreitWigner(Form("g2_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "g2", *work->var("x"), *m_p["m2"], *m_p["s2"]);

  //work->var("x")->setBins(10000, "cache");
  //RooFFTConvPdf *sig_shape = new RooFFTConvPdf(Form("sig_shape_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()),"landau (X) gauss", *work->var("x"), *skewnormal, *g1) ;

  RooAbsPdf *sig_shape = new RooAddPdf(Form("sig_shape_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "sig_shape", RooArgList(*skewnormal, *g1), RooArgList(*m_p["n0"]), true);
  //RooAbsPdf *sig_shape = skewnormal;

  m_pdf = new RooExtendPdf(Form("sig_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "sig", *sig_shape, *m_nsig_mu);
  m_fr = 0;
  //work->import(*m_pdf);
}

SignalModel::~SignalModel() {
}

void SignalModel::fit(RooDataSet *data, const std::string &outdir) {
  m_work->var("mu")->setVal(1);
  m_work->var("mu")->setConstant(true);

  RooNLLVar* nll = (RooNLLVar*) m_pdf->createNLL(*data);
  int status = minimizeFancy(nll, &m_fr);

  /*
  m_fr = m_pdf->fitTo(*data, SumW2Error(true), Minimizer("Minuit2", "Migrad"), Save(true), Strategy(1));
  if (m_fr->status() != 0 && m_fr->status() != 1) {
    std::cout << "Fit failed. Trying with Minuit." << std::endl;
    m_fr = m_pdf->fitTo(*data, SumW2Error(true), Minimizer("Minuit", "Migrad"), Save(true), Strategy(1));
    if (m_fr->status() != 0 && m_fr->status() != 1) {
      std::cout << "Fit failed. Trying with Minuit2 and strategy 2." << std::endl;
      m_fr = m_pdf->fitTo(*data, SumW2Error(true), Minimizer("Minuit2", "Migrad"), Save(true), Strategy(2));
      if (m_fr->status() != 0 && m_fr->status() != 1) {
        std::cout << "Fit failed. Trying with Minuit and strategy 2." << std::endl;
        m_fr = m_pdf->fitTo(*data, SumW2Error(true), Minimizer("Minuit", "Migrad"), Save(true), Strategy(2));
        if (m_fr->status() != 0 && m_fr->status() != 1) {
          std::cout << "Fit failed. Trying with Minuit and strategy 0." << std::endl;
          m_fr = m_pdf->fitTo(*data, SumW2Error(true), Minimizer("Minuit", "Migrad"), Save(true), Strategy(0));
        }
      }
    }
  }
  int status = m_fr->status();
  */

  cout << "[fitSignal, name = " << m_name << ", syst = " << m_syst << ", channel = " << m_channel << "]  Fit result:" << endl;
  m_fr->Print();
  TCanvas *c1 = new TCanvas("ch1", "", 800, 600);
  m_fr->correlationHist(Form("corr_%s_%s_%s", m_name.c_str(), m_syst.c_str(), m_channel.c_str()))->Draw("zcol");
  c1->SaveAs(Form("%s/signal_%s_%s_%s_corrmat.eps", outdir.c_str(), m_name.c_str(), m_syst.c_str(), m_channel.c_str()));
  delete c1;
  TCanvas *c2 = new TCanvas("ch2", "", 800, 600);
  TLegend l(0.7,0.7,0.89,0.89);
  l.SetBorderSize(0);
  RooPlot *frame = m_work->var("x")->frame(Bins(50));
  frame->GetXaxis()->SetTitle("m_{tt} [GeV]");
  frame->GetYaxis()->SetTitle(Form("Entries / %f GeV", (m_work->var("x")->getMax() -  m_work->var("x")->getMin())/50.0));
  data->plotOn(frame, Name(Form("data_%s%s%s", m_name.c_str(), m_channel.c_str(), m_syst.c_str())));
  m_pdf->plotOn(frame, Name(Form("pdf_%s%s%s", m_name.c_str(), m_channel.c_str(), m_syst.c_str())));
  l.AddEntry(frame->findObject(Form("data_%s%s%s", m_name.c_str(), m_channel.c_str(), m_syst.c_str())), Form("Simulation"), "L");
  l.AddEntry(frame->findObject(Form("pdf_%s%s%s", m_name.c_str(), m_channel.c_str(), m_syst.c_str())), Form("Fit"), "L");
  frame->Draw();
  l.Draw();
  TLatex t;
  t.SetNDC();
  t.SetTextSize(0.02);
  float xs = 0.55;
  float ys = 0.55;
  if (m_param >= 2.5) {
    xs = 0.12;
    ys = 0.85;
  }
  for (size_t z = 0; z < m_fr->floatParsFinal().getSize(); ++z) {
    t.DrawLatex(xs, ys-0.04*z, Form("p%d=%3.2e#pm%3.2e", (int) z, ((RooRealVar *) m_fr->floatParsFinal().at(z))->getVal(), ((RooRealVar *) m_fr->floatParsFinal().at(z))->getError()));
  }
  t.DrawLatex(xs, ys-0.04*m_fr->floatParsFinal().getSize(), Form("#chi^2/ndof=%3.3e", frame->chiSquare()));
  c2->SaveAs(Form("%s/signal_%s_%s_%s.eps", outdir.c_str(), m_name.c_str(), m_channel.c_str(), m_syst.c_str()));
  delete c2;
  if (status != 0 && status != 1) {
    std::cout << "Status != 0 && != 1. CHAOS!" << std::endl;
    std::exit(-1);
  }
}

RooAbsPdf *SignalModel::getPdfWithSystematics() {
  RooGenericPdf *skewnormal = new RooGenericPdf(Form("skewnormal_%s_%s_%s", m_name.c_str(), m_channel.c_str(), m_syst.c_str()), "(2.0/@1)*exp(-0.5*((@3-@0)/@1)**2)*0.5*(1+TMath::Erf(@2*(@3-@0)/(@1*@4)))", RooArgList(*m_syst_param["mg"], *m_syst_param["sg"], *m_syst_param["alpha"], *m_work->var("x"), RooConst(std::sqrt(2))));
  RooAbsPdf *g1 = new RooBreitWigner(Form("g1_%s_%s_%s", m_name.c_str(), m_channel.c_str(), m_syst.c_str()), "g1", *m_work->var("x"), *m_syst_param["m1"], *m_syst_param["s1"]);

  //RooAbsPdf *g1 = new RooGaussian(Form("g1_%s_%s_%s", m_name.c_str(), m_channel.c_str(), m_syst.c_str()), "g1", *m_work->var("x"), *m_syst_param["m1"], *m_syst_param["s1"]);
  //RooAbsPdf *g2 = new RooBreitWigner(Form("g2_%s_%s_%s", m_name.c_str(), m_channel.c_str(), m_syst.c_str()), "g2", *m_work->var("x"), *m_syst_param["m2"], *m_syst_param["s2"]);

  RooAbsPdf *sig_shape = new RooAddPdf(Form("fsig_shape_%s", m_channel.c_str()), "sig_shape", RooArgList(*skewnormal, *g1), RooArgList(*m_syst_param["n0"]), true);

  return sig_shape;
}

