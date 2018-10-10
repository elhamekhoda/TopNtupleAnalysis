#include <cstdlib>
#include <sstream>
#include <vector>
#include <string>
#include "TLorentzVector.h"
#include "TopNtupleAnalysis/TtresChi2.h"
#include "TopNtupleAnalysis/WeakCorrScaleFactorParam.h"
#include "TopNtupleAnalysis/MMUtils.h"
#include "TopNtupleAnalysis/Event.h"
#include "TopNtupleAnalysis/Electron.h"
#include "TopNtupleAnalysis/Muon.h"
#include "TopNtupleAnalysis/Jet.h"
#include "TopNtupleAnalysis/LargeJet.h"
#include "TopNtupleAnalysis/MObject.h"
#include "TopNtupleAnalysis/TtresNeutrinoBuilder.h"
#include "TopNtupleAnalysis/EFTLib.h"
#include "TopNtupleAnalysis/wrapper.h"
#ifndef DATA_DIR
#include <PathResolver/PathResolver.h>
std::string data_dir = (std::string) PathResolverFindCalibDirectory("TopNtupleAnalysis/");
#else
std::string data_dir = (std::string) DATA_DIR;
#endif 
#ifdef NNLOReweighter_NNLOReweighter
#include "NNLOReweighter/NNLOReweighterTool.h"
#endif

TtresChi2 m_chi2("MeV");
bool m_status;

WeakCorrScaleFactorParam m_ewkTool(data_dir+"EWcorr_param.root");
TtresNeutrinoBuilder m_neutrinoBuilder("MeV");

std::vector<MMUtils *> mm_mu(20);
std::vector<MMUtils *> mm_e(20);

#ifdef NNLOReweighter_NNLOReweighter
NNLOReweighterTool *m_NNLO = 0;
#endif

#include "DMweight.cxx"

TopNtupleAnalysisUtils::TopNtupleAnalysisUtils(){

}

TopNtupleAnalysisUtils::~TopNtupleAnalysisUtils(){}

void TopNtupleAnalysisUtils::initWrapper(bool dt) {
  m_chi2.Init(TtresChi2::DATA2015_MC15C);
  m_status = false;
  if (dt) {
    int runMM_etaCorr_e = 0;
    int runMM_DRCorr_e = 0;
    int runMM_etaCorr_mu = 0;
    int runMM_DRCorr_mu = 1;
    std::cout << data_dir;
    // 2jets
    mm_e[0*10+2] = new MMUtils(0, runMM_etaCorr_e, runMM_DRCorr_e, 
             data_dir+"QCDestimation/RATES_2015_2016/resolved_e_eff_ttbar.root",  // real2015+2016
             data_dir+"QCDestimation/RATES_2015_2016/resolved_e_2jets_btag0_fake.root");  // fake2015+2016
        
    mm_e[1*10+2]  = new MMUtils(1, runMM_etaCorr_e, runMM_DRCorr_e, 
             data_dir+"QCDestimation/RATES_2015_2016/resolved_e_eff_ttbar.root",     // real2015+2016 
             data_dir+"QCDestimation/RATES_2015_2016/resolved_e_2jets_btag1_fake.root");   // fake2015+2016


    mm_mu[0*10+2] = new MMUtils(0, runMM_etaCorr_mu, runMM_DRCorr_mu,
             data_dir+"QCDestimation/RATES_2015_2016/resolved_mu_eff_ttbar.root",   // real2015+2016  
             data_dir+"QCDestimation/RATES_2015_2016/resolved_mu_2jets_btag0_fake.root"); // fake2015+2016
        
    mm_mu[1*10+2] = new MMUtils(1, runMM_etaCorr_mu, runMM_DRCorr_mu, 
             data_dir+"QCDestimation/RATES_2015_2016/resolved_mu_eff_ttbar.root",   // real2015+2016
             data_dir+"QCDestimation/RATES_2015_2016/resolved_mu_2jets_btag1_fake.root"); // fake2015+2016
    
    // 3jets
    mm_e[0*10+3] = new MMUtils(0, runMM_etaCorr_e, runMM_DRCorr_e,
             data_dir+"QCDestimation/RATES_2015_2016/resolved_e_eff_ttbar.root",  // real2015+2016
             data_dir+"QCDestimation/RATES_2015_2016/resolved_e_3jets_btag0_fake.root");  // fake2015+2016
        
    mm_e[1*10+3]  = new MMUtils(1, runMM_etaCorr_e, runMM_DRCorr_e, 
             data_dir+"QCDestimation/RATES_2015_2016/resolved_e_eff_ttbar.root",     // real2015+2016 
             data_dir+"QCDestimation/RATES_2015_2016/resolved_e_3jets_btag1_fake.root");   // fake2015+2016


    mm_mu[0*10+3] = new MMUtils(0, runMM_etaCorr_mu, runMM_DRCorr_mu,
             data_dir+"QCDestimation/RATES_2015_2016/resolved_mu_eff_ttbar.root",   // real2015+2016  
             data_dir+"QCDestimation/RATES_2015_2016/resolved_mu_3jets_btag0_fake.root"); // fake2015+2016
        
    mm_mu[1*10+3] = new MMUtils(1, runMM_etaCorr_mu, runMM_DRCorr_mu, 
             data_dir+"QCDestimation/RATES_2015_2016/resolved_mu_eff_ttbar.root",   // real2015+2016
             data_dir+"QCDestimation/RATES_2015_2016/resolved_mu_3jets_btag1_fake.root"); // fake2015+2016
    
    // 4jets    
    mm_e[0*10+4] = new MMUtils(0, runMM_etaCorr_e, runMM_DRCorr_e, 
             data_dir+"QCDestimation/RATES_2015_2016/resolved_e_eff_ttbar.root",  // real2015+2016
             data_dir+"QCDestimation/RATES_2015_2016/resolved_e_4jets_btag0_fake.root");  // fake2015+2016
        
    mm_e[1*10+4]  = new MMUtils(1, runMM_etaCorr_e, runMM_DRCorr_e, 
             data_dir+"QCDestimation/RATES_2015_2016/resolved_e_eff_ttbar.root",     // real2015+2016 
             data_dir+"QCDestimation/RATES_2015_2016/resolved_e_4jets_btag1_fake.root");   // fake2015+2016


    mm_mu[0*10+4] = new MMUtils(0, runMM_etaCorr_mu, runMM_DRCorr_mu,
             data_dir+"QCDestimation/RATES_2015_2016/resolved_mu_eff_ttbar.root",   // real2015+2016  
             data_dir+"QCDestimation/RATES_2015_2016/resolved_mu_4jets_btag0_fake.root"); // fake2015+2016
        
    mm_mu[1*10+4] = new MMUtils(1, runMM_etaCorr_mu, runMM_DRCorr_mu, 
             data_dir+"QCDestimation/RATES_2015_2016/resolved_mu_eff_ttbar.root",   // real2015+2016
             data_dir+"QCDestimation/RATES_2015_2016/resolved_mu_4jets_btag1_fake.root"); // fake2015+2016
  }
  #ifdef NNLOReweighter_NNLOReweighter
  m_NNLO = new NNLOReweighterTool("NNLO");
  #endif
}
#ifdef NNLOReweighter_NNLOReweighter
void TopNtupleAnalysisUtils::InitNNLO(int mcChannelNumber) {
  m_NNLO->setProperty("ChannelNumber", mcChannelNumber).isSuccess();
  m_NNLO->initialize().isSuccess();
}

double TopNtupleAnalysisUtils::getNNLOWeight(double ttbarPt, double topPt, int mode) {
  if (mode == 1) { // sequential
    return m_NNLO->get_ttbar_and_top_pt_weight(ttbarPt, topPt);
  } else if (mode == 0) { // top pt extended
    return m_NNLO->get_top_pt_weight(topPt, true);
  } else if (mode == 2) { // ratio of extended and non-extended top pT
    return m_NNLO->get_top_pt_weight(topPt, true)/m_NNLO->get_top_pt_weight(topPt);
  }
  return 1;
}
#endif

void TopNtupleAnalysisUtils::getMtt(TLorentzVector lep, std::vector<TLorentzVector> jets, std::vector<bool> btag, TLorentzVector met) {
  m_status = m_chi2.findMinChiSquareSimple(lep, jets, btag, met);
}

double TopNtupleAnalysisUtils::res_mtt() {
  if (!m_status) return -1;
  return m_chi2.getResult_Mtt();
}
double TopNtupleAnalysisUtils::res_mtl() {
  if (!m_status) return -1;
  return m_chi2.getResult_Mtl();
}
double TopNtupleAnalysisUtils::res_mth() {
  if (!m_status) return -1;
  return m_chi2.getResult_Mth();
}
double TopNtupleAnalysisUtils::res_mwh() {
  if (!m_status) return -1;
  return m_chi2.getResult_Mwh();
}
double TopNtupleAnalysisUtils::res_chi2() {
  if (!m_status) return -1;
  return m_chi2.getResult_Chi2All();
}
int TopNtupleAnalysisUtils::res_bcat() {
  if (!m_status) return -1;
  return m_chi2.getCategory();
}

double TopNtupleAnalysisUtils::getEWK(TLorentzVector top, TLorentzVector topbar, int initial_type, int var) {
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

TLorentzVector TopNtupleAnalysisUtils::getNu(TLorentzVector l, double met, double met_phi) {
  std::vector<TLorentzVector *> vec_nu = m_neutrinoBuilder.candidatesFromWMass_Rotation(&l, met, met_phi, true);
  TLorentzVector nu;
  if (vec_nu.size() > 0) {
    nu = *(vec_nu[0]);
    for (size_t z = 0; z < vec_nu.size(); ++z) delete vec_nu[z];
    vec_nu.clear();
  }
  return nu;
}
Double_t TopNtupleAnalysisUtils::wfunction(Int_t E, Double_t x) {
  return get_wfunction(E, x);
}

#ifndef NOEFT
double TopNtupleAnalysisUtils::getQCDWeight(int btags, int boosted, TLorentzVector met, TLorentzVector lep, int isTight, std::vector<TLorentzVector> jet, float sd0, int isElectron, int muonTrigger, float topoetcone20, int runNumber) {
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
  for (unsigned int k = 0; k < jet.size(); ++k) {
    e.jet().push_back(Jet(jet[k]));
  }
  double w = 0;
  int idx = ((int) (btags >= 1))*10 + min(4, int(jet.size()));
  if (isElectron) {
    w = mm_e[idx]->getMMweights(e, 0, isElectron, 0, runNumber);
  } else {
    w = mm_mu[idx]->getMMweights(e, 0, isElectron, 0, runNumber);
  }
  return w;
}

void TopNtupleAnalysisUtils::initPDF(const std::string &s) {
  initPDFForReweighting(s.c_str(), 0);
}
double TopNtupleAnalysisUtils::alphaS(double Q2) {
  return pdfAlphaS(Q2);
}
void TopNtupleAnalysisUtils::setEFT(float eftLambda, float eftCvv) {
  initEFTModels(eftLambda, eftCvv);
}
double TopNtupleAnalysisUtils::getEFTSMWeight(int i1_pid, int i2_pid, std::vector<int> f_pid, TLorentzVector i1, TLorentzVector i2, TLorentzVector t, TLorentzVector tbar, std::vector<TLorentzVector> f, double Q2) {
  double eftw = getEFTWeight(i1_pid, i2_pid, f_pid, i1, i2, t, tbar, f, Q2, 1.0);
  double smw  = getSMWeight(i1_pid, i2_pid, f_pid, i1, i2, t, tbar, f, Q2);
  return eftw/smw - 1.0;
}
#endif 
