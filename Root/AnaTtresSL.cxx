/**
 * @brief Analysis class for tt resonances.
 * @author Danilo Enoque Ferreira de Lima <dferreir@cern.ch>
 */

#include "TopNtupleAnalysis/Analysis.h"
#include "TopNtupleAnalysis/AnaTtresSL.h"
#include "TopNtupleAnalysis/Event.h"
#include "TLorentzVector.h"
#include <vector>
#include <string>
#include "TopNtupleAnalysis/HistogramService.h"

AnaTtresSL::AnaTtresSL(const std::string &filename, bool electron, bool boosted, std::vector<std::string> &systList)
  : Analysis(filename, systList), m_electron(electron), m_boosted(boosted),
    m_neutrinoBuilder("MeV"), m_chi2("MeV") {

  m_chi2.Init(TtresChi2::DATA2015_MC15);

  m_hSvc.create1D("lepPt", "; Lepton p_{T} [GeV]; Events", 40, 0, 500);
  m_hSvc.create1D("lepEta", "; Lepton #eta ; Events", 24, -3.0, 3.0);
  m_hSvc.create1D("lepPhi", "; Lepton #phi ; Events", 40, -4.0, 4.0);

  m_hSvc.create1D("leadJetPt", "; Leading Jet p_{T} [GeV]; Events", 30, 0, 900);  
  m_hSvc.create1D("nJets", "; number of jets ; Events", 10, 0, 10);
  
  m_hSvc.create1D("leadbJetPt", "; Leading b-jet p_{T} [GeV]; Events", 40, 0, 500);
  m_hSvc.create1D("nBtagJets", "; number of b-tagged jets ; Events", 10, 0, 10);  

  m_hSvc.create1D("MET", "; Missing E_{T} [GeV]; Events", 50, 0, 500);
  m_hSvc.create1D("MET_phi", "; Missing E_{T} #phi; Events", 40, -4.0, 4.0);
    
  m_hSvc.create1D("mwt", "; W transverse mass [GeV]; Events", 50, 0, 500);
  m_hSvc.create1D("mu", "; <mu>; Events", 100, 0, 100);
  m_hSvc.create1D("mu_original", "; <mu_origianl>; Events", 100, 0, 100);
  m_hSvc.create1D("vtxz", ";Z position of truth primary vertex; Events", 40, -400, 400);
  m_hSvc.create1D("npv", "; npv; Events", 50, 0, 50);

  m_hSvc.create1D("closejl_minDeltaR", "; min #Delta R(lep, jet); Events", 40, 0, 4);
  m_hSvc.create1D("closejl_pt", "; Pt of closest jet to lep [GeV]; Events", 40, 0, 500);
 
  m_hSvc.create1D("jet0_m", "; mass of the jet[0] [GeV]; Events", 50, 0, 500); 
  m_hSvc.create1D("jet1_m", "; mass of the jet[1] [GeV]; Events", 50, 0, 500); 
  m_hSvc.create1D("jet2_m", "; mass of the jet[2] [GeV]; Events", 50, 0, 500); 
  m_hSvc.create1D("jet3_m", "; mass of the jet[3] [GeV]; Events", 50, 0, 500); 
  m_hSvc.create1D("jet4_m", "; mass of the jet[4] [GeV]; Events", 50, 0, 500); 
  m_hSvc.create1D("jet5_m", "; mass of the jet[5] [GeV]; Events", 50, 0, 500); 
  
  m_hSvc.create1D("jet0_pt", "; pt of the jet[0] [GeV]; Events", 40, 0, 500); 
  m_hSvc.create1D("jet1_pt", "; pt of the jet[1] [GeV]; Events", 40, 0, 500); 
  m_hSvc.create1D("jet2_pt", "; pt of the jet[2] [GeV]; Events", 40, 0, 500); 
  m_hSvc.create1D("jet3_pt", "; pt of the jet[3] [GeV]; Events", 40, 0, 500); 
  m_hSvc.create1D("jet4_pt", "; pt of the jet[4] [GeV]; Events", 40, 0, 500); 
  m_hSvc.create1D("jet5_pt", "; pt of the jet[5] [GeV]; Events", 40, 0, 500); 
  
  m_hSvc.create1D("jet0_eta", "; #eta of the jet[0]; Events", 20, -10, 10); 
  m_hSvc.create1D("jet1_eta", "; #eta of the jet[1]; Events", 20, -10, 10); 
  m_hSvc.create1D("jet2_eta", "; #eta of the jet[2]; Events", 20, -10, 10); 
  m_hSvc.create1D("jet3_eta", "; #eta of the jet[3]; Events", 20, -10, 10); 
  m_hSvc.create1D("jet4_eta", "; #eta of the jet[4]; Events", 20, -10, 10); 
  m_hSvc.create1D("jet5_eta", "; #eta of the jet[5]; Events", 20, -10, 10); 
  
  m_hSvc.create1D("jet0_phi", "; #phi of the jet[0]; Events", 20, -10, 10); 
  m_hSvc.create1D("jet1_phi", "; #phi of the jet[1]; Events", 20, -10, 10); 
  m_hSvc.create1D("jet2_phi", "; #phi of the jet[2]; Events", 20, -10, 10); 
  m_hSvc.create1D("jet3_phi", "; #phi of the jet[3]; Events", 20, -10, 10); 
  m_hSvc.create1D("jet4_phi", "; #phi of the jet[4]; Events", 20, -10, 10); 
  m_hSvc.create1D("jet5_phi", "; #phi of the jet[5]; Events", 20, -10, 10); 
  
  if (m_boosted) {
    m_hSvc.create1D("closeJetPt", "; Selected Jet p_{T} ; Events", 40, 0, 500);
    m_hSvc.create1D("largeJetPt", "; Large jet p_{T} ; Events", 40, 0, 800);
    m_hSvc.create1D("largeJetM", "; Large jet M ; Events", 30, 0, 300);
    m_hSvc.create1D("largeJetEta", "; Large jet eta ; Events", 24, -3., 3.);
    m_hSvc.create1D("largeJetPhi", "; Large jet phi ; Events", 40, -4., 4.);
    m_hSvc.create1D("largeJetSd12", "; Large jet #sqrt{d_{12}} ; Events", 30, 0, 300);
    m_hSvc.create1D("mtlep_boo", "; m_{t,lep} ; Events", 70, 0, 700);
  } else {
    m_hSvc.create1D("mtlep_res", "; m_{t,lep} [GeV]; Events", 40, 0, 400);
    m_hSvc.create1D("mthad_res", "; m_{t,had} [GeV]; Events", 40, 0, 400);
    m_hSvc.create1D("mwhad_res", "; m_{W,had} [GeV]; Events", 40, 0, 400);
    m_hSvc.create1D("chi2", "; log(#chi^{2}) ; Events", 50, -3, 7);
  }

  m_hSvc.create1D("mtt", "; m_{t#bar{t}} [GeV]; Events", 60, 0, 6000);
  
}

AnaTtresSL::~AnaTtresSL() {
}

void AnaTtresSL::run(const Event &evt, double weight, const std::string &s) {
  // check channel
  
  if (m_electron && (evt.electron().size() != 1 || evt.muon().size() != 0))
    return;

  if (!m_electron && (evt.electron().size() != 0 || evt.muon().size() != 1))
    return;

  if (m_boosted)
    if (!(evt.passes("bejets") || evt.passes("bmujets")))
      return;

  if (!m_boosted)
    if (!(evt.passes("rejets") || evt.passes("rmujets")))
      return;
  
  if (s=="_Loose" && isDuplicateEvent(evt.runNumber(), evt.eventNumber()) ){
      m_Nduplicate++;
      return;
  }
  
  HistogramService *h = &m_hSvc;
  TLorentzVector l;
  if (m_electron) {
    l = evt.electron()[0].mom();
  } else {
    l = evt.muon()[0].mom();
  }
  h->h1D("lepPt", "", s)->Fill(l.Perp()*1e-3, weight);
  h->h1D("lepEta", "", s)->Fill(l.Eta(), weight);
  h->h1D("lepPhi", "", s)->Fill(l.Phi(), weight);

  h->h1D("MET_phi", "", s)->Fill(evt.met().Phi(), weight);

  const TLorentzVector &j = evt.jet()[0].mom();
  h->h1D("leadJetPt", "", s)->Fill(j.Perp()*1e-3, weight);
  
  // for now
  int nJets = evt.jet().size(); //njets 
  h->h1D("nJets", "", s)->Fill(nJets, weight);
  
  int nBtagged = 0; //nB-tagged jets 
  for (size_t bidx = 0; bidx < evt.jet().size(); ++bidx)
    if (evt.jet()[bidx].btag_mv2c20_70()){
      if(nBtagged==0)h->h1D("leadbJetPt", "", s)->Fill(evt.jet()[bidx].mom().Perp()*1e-3, weight);
      nBtagged += 1;
    }
  h->h1D("nBtagJets", "", s)->Fill(nBtagged, weight);

  // Jet kinematics  
  
  std::vector<float> jetMass_vector;
  std::vector<float> jetPt_vector;
  std::vector<float> jetEta_vector;
  std::vector<float> jetPhi_vector;
  
  jetMass_vector.resize(evt.jet().size());
  jetPt_vector.resize(evt.jet().size());
  jetEta_vector.resize(evt.jet().size());
  jetPhi_vector.resize(evt.jet().size());  
  
  size_t iJet = 0;
  for (; iJet < evt.jet().size(); ++iJet){
    const TLorentzVector &jet_p4 = evt.jet()[iJet].mom();
    jetMass_vector[iJet] =  evt.jet()[iJet].mom().M();
    jetPt_vector[iJet]   =  evt.jet()[iJet].mom().Pt();
    jetEta_vector[iJet]  =  evt.jet()[iJet].mom().Eta();
    jetPhi_vector[iJet]  =  evt.jet()[iJet].mom().Phi();    
  }//for
  
  int maxNjet = (evt.jet().size()<6) ? evt.jet().size() : 6;
  for (int i = 0; i < maxNjet; ++i){  
     
     std::string nameJet_m = "jet" + std::to_string(i)+"_m";
     h->h1D(nameJet_m, "", s)->Fill(jetMass_vector[i]*1e-3, weight);
     
     std::string nameJet_pt = "jet" + std::to_string(i)+"_pt";
     h->h1D(nameJet_pt, "", s)->Fill(jetPt_vector[i]*1e-3, weight);
     
     std::string nameJet_eta = "jet" + std::to_string(i)+"_eta";
     h->h1D(nameJet_eta, "", s)->Fill(jetEta_vector[i], weight);
     
     std::string nameJet_phi = "jet" + std::to_string(i)+"_phi";
     h->h1D(nameJet_phi, "", s)->Fill(jetPhi_vector[i], weight);    
  
  }//for
  
  float mtt = -1;
  
  //missing et
  h->h1D("MET", "", s)->Fill(evt.met().Perp()*1e-3, weight);

  //transverse W mass  
  h->h1D("mwt", "", s)->Fill(sqrt(2. * l.Perp() * evt.met().Perp() * (1. - cos(l.Phi() - evt.met().Phi())))*1e-3, weight); 
  
  //mu
  h->h1D("mu", "", s)->Fill(evt.mu(), weight); 
  h->h1D("mu_original", "", s)->Fill(evt.mu_original(), weight); 
    
  //npv
  h->h1D("npv", "", s)->Fill(evt.npv(), weight);
  
  //z prosition of primary vertex
  h->h1D("vtxz", "", s)->Fill(evt.vtxz(), weight);

  //deltaR between lepton and the closest narrow jet
  float closejl_deltaR  = 99;
  float deltaR_tmp      = 99;
  int closejl_idx       = -1;
  
  size_t jet_idx = 0;
  for (; jet_idx < evt.jet().size(); ++jet_idx){    
    deltaR_tmp = l.DeltaR(evt.jet()[jet_idx].mom());
    if (deltaR_tmp < closejl_deltaR){
        closejl_deltaR = deltaR_tmp;
        closejl_idx = jet_idx;
    }   
  }//for     
  
  float closejl_pt = -1;
  if (closejl_idx>0)    closejl_pt = evt.jet()[closejl_idx].mom().Perp();  
  h->h1D("closejl_minDeltaR", "", s)->Fill(closejl_deltaR, weight); 
  h->h1D("closejl_pt", "", s)->Fill(closejl_pt*1e-3, weight);

  if (m_boosted && (evt.passes("bejets") || evt.passes("bmujets"))) {
    
    size_t close_idx = 0;
    for (; close_idx < evt.jet().size(); ++close_idx)
      if (evt.jet()[close_idx].closeToLepton())
        break;
    const TLorentzVector &sj = evt.jet()[close_idx].mom();
    h->h1D("closeJetPt", "", s)->Fill(sj.Perp()*1e-3, weight);
    
    size_t goodljet_idx = 0;
    for (; goodljet_idx < evt.largeJet().size(); ++goodljet_idx)
      if (evt.largeJet()[goodljet_idx].good())
        break;
    
    const TLorentzVector &lj = evt.largeJet()[goodljet_idx].mom();
    h->h1D("largeJetPt", "", s)->Fill(lj.Perp()*1e-3, weight);
    h->h1D("largeJetM", "", s)->Fill(lj.M()*1e-3, weight);
    h->h1D("largeJetEta", "", s)->Fill(lj.Eta(), weight);
    h->h1D("largeJetPhi", "", s)->Fill(lj.Phi(), weight);
    h->h1D("largeJetSd12", "", s)->Fill(evt.largeJet()[goodljet_idx].split12()*1e-3, weight);
    
    // recalc. mtt
    // lepton = l
    // large-R jet = hadronic top = lj
    // selected jet = leptonic top's b-jet = sj
    // neutrino px, py = met
    std::vector<TLorentzVector*> vec_nu = m_neutrinoBuilder.candidatesFromWMass_Rotation(&l, evt.met().Perp(), evt.met().Phi(), true);   
    TLorentzVector nu(0,0,0,0);
    if (vec_nu.size() > 0) {
      nu = *(vec_nu[0]);
      for (size_t z = 0; z < vec_nu.size(); ++z) delete vec_nu[z];
      vec_nu.clear();
    }
    
    if (evt.largeJet().size()!=0)    mtt = (lj+sj+nu+l).M();
    h->h1D("mtt", "", s)->Fill(mtt*1e-3, weight);
    h->h1D("mtlep_boo", "", s)->Fill((sj+nu+l).M()*1e-3, weight);
    
  }else if (!m_boosted && (evt.passes("rejets") || evt.passes("rmujets"))) {
    
    // inputs 
    // LEPTON --> TLorentzVector for your lepton
    // vjets -->  std::vector<TLorentzVector*> for the jets
    // vjets_btagged --> std::vector<bool> to say if the jets are btagged or not
    // met --> TLorentzVector for your MET

    // outputs, they will be filled by the TTBarLeptonJetsBuilder_chi2
    int  igj3, igj4; // index for the Whad
    int igb3, igb4; // index for the b's
    int  ign1;  // index for the neutrino (because chi2 can test both pz solution)
    double chi2ming1, chi2ming1H, chi2ming1L;

    std::vector<TLorentzVector *> vjets;
    std::vector<bool> vjets_btagged;
    for (size_t z = 0; z < evt.jet().size(); ++z) {
      vjets.push_back(new TLorentzVector(0,0,0,0));
      vjets[z]->SetPtEtaPhiE(evt.jet()[z].mom().Perp(), evt.jet()[z].mom().Eta(), evt.jet()[z].mom().Phi(), evt.jet()[z].mom().E());
      // https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/BTagingxAODEDM
      // https://twiki.cern.ch/twiki/bin/view/AtlasProtected/BTaggingBenchmarks
      vjets_btagged.push_back(evt.jet()[z].btag_mv2c20_60());
    }
    TLorentzVector met = evt.met();
    bool status = m_chi2.findMinChiSquare(&l, &vjets, &vjets_btagged, &met, igj3, igj4, igb3, igb4, ign1, chi2ming1, chi2ming1H, chi2ming1L); 
    
    float chi2Value = 1000000; // log10(1000000) = 6
    float mwh = -1;
    float mtl = -1;
    float mth = -1;

    if (status){
        chi2Value = chi2ming1;
	mwh = m_chi2.getResult_Mwh();
	mtl = m_chi2.getResult_Mtl();
	mth = m_chi2.getResult_Mth();
	mtt = m_chi2.getResult_Mtt();
    }
    
    for (size_t z = 0; z < vjets.size(); ++z) {
      delete vjets[z];
    }
    vjets.clear();
    vjets_btagged.clear();

    //Fill histograms
    h->h1D("mtt", "", s)->Fill(mtt*1e-3, weight);
    h->h1D("mtlep_res", "", s)->Fill(mtl*1e-3, weight);
    h->h1D("mthad_res", "", s)->Fill(mth*1e-3, weight);
    h->h1D("mwhad_res", "", s)->Fill(mwh*1e-3, weight);
    h->h1D("chi2", "", s)->Fill(log10(chi2Value), weight);
  }

}

