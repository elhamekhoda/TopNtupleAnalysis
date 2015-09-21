#include <string>
#include "BkgModel.h"
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
#include "RooGenericPdf.h"

using namespace std;
using namespace RooFit;

BkgModel::BkgModel(const std::string &name, double xsec, double param, const std::string &channel, const std::string &syst,
                         RooWorkspace *work)
  : BaseSignalModel(name, xsec, param, channel, syst, work) {

  //m_p["p1"] = new RooRealVar(Form("p1_%s_%s", name.c_str(), channel.c_str()), "p1", 0.0, -1.0e-2, 1.0e-2);
  //m_p["p2"] = new RooRealVar(Form("p2_%s_%s", name.c_str(), channel.c_str()), "p2", 0.0, -1.0e-2, 1.0e-2);
  //RooAbsPdf *bkg_shape = new BkgWtbPdf(Form("bkg_shape_%s_%s", name.c_str(), channel.c_str()), "bkg_shape", *work->var("x"), *m_p["p1"], *m_p["p2"]);

  // dijets pdf
  //m_p["p1"] = new RooRealVar(Form("p1_%s_%s", name.c_str(), channel.c_str()), "p1", -1.0, -10.0, 0.0);
  //m_p["p2"] = new RooRealVar(Form("p2_%s_%s", name.c_str(), channel.c_str()), "p2", 2.0, 0.0, 40.0);
  //m_p["p3"] = new RooRealVar(Form("p3_%s_%s", name.c_str(), channel.c_str()), "p3", 0.0, -4.0, 4.0);
  //RooAbsPdf *bkg_shape = new BkgDijetsPdf(Form("bkg_shape_%s_%s", name.c_str(), channel.c_str()), "bkg_shape", *work->var("x"), *m_p["p1"], *m_p["p2"], *m_p["p3"]);

  m_p["p1"] = new RooRealVar(Form("p1_%s_%s", name.c_str(), channel.c_str()), "p1", -10.0, -40.0, 20.0);
  m_p["p2"] = new RooRealVar(Form("p2_%s_%s", name.c_str(), channel.c_str()), "p2", -1.0, -40.0, 0.0);
  //m_p["p3"] = new RooRealVar(Form("p3_%s_%s", name.c_str(), channel.c_str()), "p3",  0.1, -2.0, 2.0);

  //RooAbsPdf *bkg_shape = new BkgFallPdf(Form("bkg_shape_%s_%s", name.c_str(), channel.c_str()), "bkg_shape", *work->var("x"), *m_p["p1"], *m_p["p2"]);//, *m_p["p3"]);
  RooAbsPdf *bkg_shape = new RooGenericPdf(Form("bkg_shape_%s_%s", name.c_str(), channel.c_str()), "TMath::Power(@0/13.0e3, @1 + @2*TMath::Log(@0/13.0e3))", RooArgList(*work->var("x"), *m_p["p1"], *m_p["p2"]));

  m_pdf = bkg_shape;//new RooExtendPdf(Form("bkg_%s_%s", name.c_str(), channel.c_str()), "bkg", *bkg_shape, *m_nsig_mu);
  m_fr = 0;
}

BkgModel::~BkgModel() {
}

void BkgModel::fit(RooDataSet *data, const std::string &outdir) {
  m_fr = m_pdf->fitTo(*data, SumW2Error(true), Minimizer("Minuit2", "Migrad"), Save(true), Strategy(2));
  cout << "[fitBkg, name = " << m_name << ", syst = " << m_syst << ", channel = " << m_channel << "]  Fit result:" << endl;
  m_fr->Print();
  TCanvas *c1 = new TCanvas("ch1", "", 800, 600);
  m_fr->correlationHist(Form("corrbkg_%s_%s_%s", m_name.c_str(), m_syst.c_str(), m_channel.c_str()))->Draw("zcol");
  c1->SaveAs(Form("%s/bkg_%s_%s_%s_corrmat.eps", outdir.c_str(), m_name.c_str(), m_syst.c_str(), m_channel.c_str()));
  delete c1;
}

RooAbsPdf *BkgModel::getPdfWithSystematics() {
  //RooAbsPdf *bkg_shape = new BkgFallPdf(Form("fbkg_shape_%s_%s", m_name.c_str(), m_channel.c_str()), "bkg_shape", \
  //                       *m_work->var("x"), *m_syst_param["p1"], *m_syst_param["p2"]);//, *m_syst_param["p3"]);

  //RooAbsPdf *bkg_shape = new BkgDijetsPdf(Form("fbkg_shape_%s_%s", m_name.c_str(), m_channel.c_str()), "bkg_shape", \
  //                       *m_work->var("x"), *m_syst_param["p1"], *m_syst_param["p2"], *m_syst_param["p3"]);

  //RooAbsPdf *bkg_shape = new BkgWtbPdf(Form("fbkg_shape_%s_%s", m_name.c_str(), m_channel.c_str()), "bkg_shape", \
  //                       *m_work->var("x"), *m_syst_param["p1"], *m_syst_param["p2"]);//, *m_syst_param["p3"], *m_syst_param["p4"]);

  RooAbsPdf *bkg_shape = new RooGenericPdf(Form("bkg_shape_%s_%s", m_name.c_str(), m_channel.c_str()), "TMath::Power(@0/13.0e3, @1 + @2*TMath::Log(@0/13.0e3))", RooArgList(*m_work->var("x"), *m_syst_param["p1"], *m_syst_param["p2"]));

  RooFormulaVar *nsig_mu = new RooFormulaVar(Form("fnsig_mu_%s_%s", m_name.c_str(), m_channel.c_str()), "@0*@1", \
                         RooArgList(*m_syst_param["norm"], *m_work->var("mu")));

  return new RooExtendPdf(Form("fbkg_%s_%s", m_name.c_str(), m_channel.c_str()), "bkg", *bkg_shape, *nsig_mu);
}

