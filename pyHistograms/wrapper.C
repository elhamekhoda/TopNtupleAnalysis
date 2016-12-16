
#include "TopNtupleAnalysis/TtresChi2.h"
#include "TLorentzVector.h"
#include <vector>
#include "TopNtupleAnalysis/WeakCorrScaleFactorParam.h"
#include "TLorentzVector.h"

#include "TopNtupleAnalysis/MMUtils.h"
#include "TopNtupleAnalysis/Event.h"
#include "TopNtupleAnalysis/Electron.h"
#include "TopNtupleAnalysis/Muon.h"
#include "TopNtupleAnalysis/Jet.h"
#include "TopNtupleAnalysis/LargeJet.h"
#include "TopNtupleAnalysis/MObject.h"

#include "TLorentzVector.h"
#include <vector>

#include "TopNtupleAnalysis/TtresNeutrinoBuilder.h"

#include "TLorentzVector.h"
#include <vector>
#include <cstdlib>
#include <sstream>

#include "TopNtupleAnalysis/EFTLib.h"


#include "TLorentzVector.h"
#include <vector>
#include <cstdlib>
#include <sstream>

#include "TopNtupleAnalysis/EFTLib.h"

TtresChi2 m_chi2("MeV");
bool m_status;
WeakCorrScaleFactorParam m_ewkTool("../share/EWcorr_param.root");
TtresNeutrinoBuilder m_neutrinoBuilder("MeV");

MMUtils *m_mm_b0_res_e = 0;
MMUtils *m_mm_b1_res_e = 0;
MMUtils *m_mm_b0_res_mu = 0;
MMUtils *m_mm_b1_res_mu = 0;

/*
MMUtils m_mm_b0_res_e(0, "../scripts/QCDestimation/RATES_2015/resolved_e_eff_ttbar.root", // real2015
		     "../scripts/QCDestimation/RATES_2015/resolved_e_btag0_fake.root",       // fake2015
		     "../scripts/QCDestimation/RATES_2016/resolved_e_eff_ttbar.root",        // real2016
		     "../scripts/QCDestimation/RATES_2016/resolved_e_btag0_fake.root");      // fake2016
MMUtils m_mm_b1_res_e(1, "../scripts/QCDestimation/RATES_2015/resolved_e_eff_ttbar.root", // real2015
		     "../scripts/QCDestimation/RATES_2015/resolved_e_btag1_fake.root",       // fake2015
		     "../scripts/QCDestimation/RATES_2016/resolved_e_eff_ttbar.root",   // real2016
		     "../scripts/QCDestimation/RATES_2016/resolved_e_btag1_fake.root"); // fake2016
MMUtils m_mm_b0_res_mu(0, "../scripts/QCDestimation/RATES_2015/resolved_mu_eff_ttbar.root",// real2015
		      "../scripts/QCDestimation/RATES_2015/resolved_mu_btag0_fake.root",      // fake2015
		      "../scripts/QCDestimation/RATES_2016/resolved_mu_eff_ttbar.root",        // real2016
		      "../scripts/QCDestimation/RATES_2016/resolved_mu_btag0_fake.root"); // fake2016
MMUtils m_mm_b1_res_mu(1, "../scripts/QCDestimation/RATES_2015/resolved_mu_eff_ttbar.root",// real2015
		      "../scripts/QCDestimation/RATES_2015/resolved_mu_btag1_fake.root",// fake2015
		      "../scripts/QCDestimation/RATES_2016/resolved_mu_eff_ttbar.root",       // real2016
		      "../scripts/QCDestimation/RATES_2016/resolved_mu_btag1_fake.root"); // fake2016
*/

void initWrapper() {
  m_chi2.Init(TtresChi2::DATA2015_MC15C);
  m_status = false;
  m_mm_b0_res_e = new MMUtils(0, "../scripts/QCDestimation/RATES_2015/resolved_e_eff_ttbar.root", // real2015
		     "../scripts/QCDestimation/RATES_2015/resolved_e_btag0_fake.root",       // fake2015
		     "../scripts/QCDestimation/RATES_2016/resolved_e_eff_ttbar.root",        // real2016
		     "../scripts/QCDestimation/RATES_2016/resolved_e_btag0_fake.root");      // fake2016
  m_mm_b1_res_e = new MMUtils(1, "../scripts/QCDestimation/RATES_2015/resolved_e_eff_ttbar.root", // real2015
		     "../scripts/QCDestimation/RATES_2015/resolved_e_btag1_fake.root",       // fake2015
		     "../scripts/QCDestimation/RATES_2016/resolved_e_eff_ttbar.root",   // real2016
		     "../scripts/QCDestimation/RATES_2016/resolved_e_btag1_fake.root"); // fake2016
  m_mm_b0_res_mu = new MMUtils(0, "../scripts/QCDestimation/RATES_2015/resolved_mu_eff_ttbar.root",// real2015
		      "../scripts/QCDestimation/RATES_2015/resolved_mu_btag0_fake.root",      // fake2015
		      "../scripts/QCDestimation/RATES_2016/resolved_mu_eff_ttbar.root",        // real2016
		      "../scripts/QCDestimation/RATES_2016/resolved_mu_btag0_fake.root"); // fake2016
  m_mm_b1_res_mu = new MMUtils(1, "../scripts/QCDestimation/RATES_2015/resolved_mu_eff_ttbar.root",// real2015
		      "../scripts/QCDestimation/RATES_2015/resolved_mu_btag1_fake.root",// fake2015
		      "../scripts/QCDestimation/RATES_2016/resolved_mu_eff_ttbar.root",       // real2016
		      "../scripts/QCDestimation/RATES_2016/resolved_mu_btag1_fake.root"); // fake2016
}

void getMtt(TLorentzVector lep, std::vector<TLorentzVector> jets, std::vector<bool> btag, TLorentzVector met) {
  m_status = m_chi2.findMinChiSquareSimple(lep, jets, btag, met);
}

double res_mtt() {
  if (!m_status) return -1;
  return m_chi2.getResult_Mtt();
}
double res_mtl() {
  if (!m_status) return -1;
  return m_chi2.getResult_Mtl();
}
double res_mth() {
  if (!m_status) return -1;
  return m_chi2.getResult_Mth();
}
double res_mwh() {
  if (!m_status) return -1;
  return m_chi2.getResult_Mwh();
}
double res_chi2() {
  if (!m_status) return -1;
  return m_chi2.getResult_Chi2All();
}
double getEWK(TLorentzVector top, TLorentzVector topbar, int initial_type, int var = 0) {
  float sf; 
  float t_pt = top.Perp();
  float t_eta = top.Eta();
  float t_phi = top.Phi();
  float t_m = top.M();

  float tbar_pt = topbar.Perp();
  float tbar_eta = topbar.Eta();
  float tbar_phi = topbar.Phi();
  float tbar_m = topbar.M();
  sf = m_ewkTool.getScaleFactor(t_pt, t_eta, t_phi, t_m, tbar_pt, tbar_eta, tbar_phi, tbar_m, initial_type, var);
  return sf;
}

TLorentzVector getNu(TLorentzVector l, double met, double met_phi) {
  std::vector<TLorentzVector *> vec_nu = m_neutrinoBuilder.candidatesFromWMass_Rotation(&l, met, met_phi, true);
  TLorentzVector nu;
  if (vec_nu.size() > 0) {
    nu = *(vec_nu[0]);
    for (size_t z = 0; z < vec_nu.size(); ++z) delete vec_nu[z];
    vec_nu.clear();
  }
  return nu;
}


double getQCDWeight(int btags, int boosted, TLorentzVector met, TLorentzVector lep, int isTight, std::vector<TLorentzVector> jet, float sd0, int isElectron, int muonTrigger, float topoetcone20, int runNumber) {
  Event e;
  e.met(met.Px(), met.Py());
  if (isElectron) {
    e.electron().push_back(Electron(lep));
    e.electron()[0].setTightPP(isTight);
    e.electron()[0].topoetcone20() = topoetcone20;
    e.electron()[0].sd0() = sd0;
  } else {
    e.muon().push_back(Muon(lep));
    e.muon()[0].sd0() = sd0;
	e.muon()[0].setTight(isTight);
	e.muon()[0].HLT_mu20_iloose_L1MU15() = muonTrigger;
	e.muon()[0].HLT_mu50() = muonTrigger;
	e.muon()[0].topoetcone20() = topoetcone20;
  }
  for (int k = 0; k < jet.size(); ++k) {
    e.jet().push_back(Jet(jet[k]));
  }
  double w = 0;
  if (!btags && boosted && isElectron) {
    w = m_mm_b0_res_e->getMMweights(e, 0, isElectron, boosted, runNumber);
  } else if (btags && boosted && isElectron) {
    w = m_mm_b1_res_e->getMMweights(e, 0, isElectron, boosted, runNumber);
  } else if (!btags && !boosted && isElectron) {
    w = m_mm_b0_res_e->getMMweights(e, 0, isElectron, boosted, runNumber);
  } else if (btags && !boosted && isElectron) {
    w = m_mm_b1_res_e->getMMweights(e, 0, isElectron, boosted, runNumber);
  } else if (!btags && boosted && !isElectron) {
    w = m_mm_b0_res_mu->getMMweights(e, 0, isElectron, boosted, runNumber);
  } else if (btags && boosted && !isElectron) {
    w = m_mm_b1_res_mu->getMMweights(e, 0, isElectron, boosted, runNumber);
  } else if (!btags && !boosted && !isElectron) {
    w = m_mm_b0_res_mu->getMMweights(e, 0, isElectron, boosted, runNumber);
  } else if (btags && !boosted && !isElectron) {
    w = m_mm_b1_res_mu->getMMweights(e, 0, isElectron, boosted, runNumber);
  }
  return w;
}

void initPDF(const std::string &s = "NNPDF21_lo_as_0130_100") {
  initPDFForReweighting(s.c_str(), 0);
}
double alphaS(double Q2) {
  return pdfAlphaS(Q2);
}
void setEFT(float eftLambda, float eftCvv) {
  initEFTModels(eftLambda, eftCvv);
}
double getEFTSMWeight(int i1_pid, int i2_pid, std::vector<int> f_pid, TLorentzVector i1, TLorentzVector i2, TLorentzVector t, TLorentzVector tbar, std::vector<TLorentzVector> f, double Q2) {
  double eftw = getEFTWeight(i1_pid, i2_pid, f_pid, i1, i2, t, tbar, f, Q2, 1.0);
  double smw  = getSMWeight(i1_pid, i2_pid, f_pid, i1, i2, t, tbar, f, Q2);
  return eftw/smw - 1.0;
}

