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

AnaTtresSL::AnaTtresSL(const std::string &filename, bool electron, bool boosted)
  : Analysis(filename), m_electron(electron), m_boosted(boosted),
    m_neutrinoBuilder("MeV"), m_chi2("MeV") {

  m_chi2.Init(TtresChi2::DATA2015_MC15);

  m_hSvc.create1D("lepPt", "; Lepton p_{T} [GeV]; Events", 30, 0, 300);
  m_hSvc.create1D("lepEta", "; Lepton #eta ; Events", 50, -2.5, 2.5);
  m_hSvc.create1D("lepPhi", "; Lepton #phi ; Events", 64, -3.2, 3.2);

  m_hSvc.create1D("leadJetPt", "; Leading Jet p_{T} [GeV]; Events", 50, 0, 500);  
  m_hSvc.create1D("nJets", "; number of jets ; Events", 10, 0, 10);
  
  m_hSvc.create1D("leadbJetPt", "; Leading b-jet p_{T} [GeV]; Events", 50, 0, 500);
  m_hSvc.create1D("nBtagJets", "; number of b-tagged jets ; Events", 10, 0, 10);  

  m_hSvc.create1D("met", "; Missing E_{T} [GeV]; Events", 50, 0, 500);
  m_hSvc.create1D("met_phi", "; Missing E_{T} #phi; Events", 64, -3.2, 3.2);
    
  m_hSvc.create1D("mwt", "; Transverse W mass [GeV]; Events", 40, 0, 400);
  m_hSvc.create1D("mu", "; mu; Events", 100, 0, 100);
  
  m_hSvc.create1D("jet0_m", "; mass of the jet[0] [GeV]; Events", 50, 0, 500); 
  m_hSvc.create1D("jet1_m", "; mass of the jet[1] [GeV]; Events", 50, 0, 500); 
  m_hSvc.create1D("jet2_m", "; mass of the jet[2] [GeV]; Events", 50, 0, 500); 
  m_hSvc.create1D("jet3_m", "; mass of the jet[3] [GeV]; Events", 50, 0, 500); 
  m_hSvc.create1D("jet4_m", "; mass of the jet[4] [GeV]; Events", 50, 0, 500); 
  m_hSvc.create1D("jet5_m", "; mass of the jet[5] [GeV]; Events", 50, 0, 500); 
  
  m_hSvc.create1D("jet0_pt", "; pt of the jet[0] [GeV]; Events", 50, 0, 500); 
  m_hSvc.create1D("jet1_pt", "; pt of the jet[1] [GeV]; Events", 50, 0, 500); 
  m_hSvc.create1D("jet2_pt", "; pt of the jet[2] [GeV]; Events", 50, 0, 500); 
  m_hSvc.create1D("jet3_pt", "; pt of the jet[3] [GeV]; Events", 50, 0, 500); 
  m_hSvc.create1D("jet4_pt", "; pt of the jet[4] [GeV]; Events", 50, 0, 500); 
  m_hSvc.create1D("jet5_pt", "; pt of the jet[5] [GeV]; Events", 50, 0, 500); 
  
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
    m_hSvc.create1D("closeJetPt", "; Selected Jet p_{T} ; Events", 25, 0, 500);

    m_hSvc.create1D("largeJetPt", "; Large jet p_{T} ; Events", 20, 300, 700);
    m_hSvc.create1D("largeJetM", "; Large jet M ; Events", 15, 0, 300);
    m_hSvc.create1D("largeJetSd12", "; Large jet #sqrt{d_{12}} ; Events", 30, 0, 300);

    m_hSvc.create1D("mtlep_boo", "; m_{t,lep} ; Events", 40, 0, 400);
  } else {
    m_hSvc.create1D("mtlep_res", "; m_{t,lep} [GeV]; Events", 40, 0, 400);
    m_hSvc.create1D("mthad_res", "; m_{t,had} [GeV]; Events", 40, 0, 400);
    m_hSvc.create1D("mwhad_res", "; m_{W,had} [GeV]; Events", 40, 0, 400);
    m_hSvc.create1D("chi2", "; #chi^{2} ; Events", 50, 0, 10);
  }

  m_hSvc.create1D("mtt", "; m_{t#bar{t}} [GeV]; Events", 60, 0, 6000);
}

AnaTtresSL::~AnaTtresSL() {
}

void AnaTtresSL::run(const Event &e, double weight) {
  std::string s = ""; // this would be the systematics ... could be sent as an argument in the future

  // check channel
  if (m_electron && (e.electron().size() != 1 || e.muon().size() != 0))
    return;

  if (!m_electron && (e.electron().size() != 0 || e.muon().size() != 1))
    return;

  if (m_boosted)
    if (!(e.passes("bejets") || e.passes("bmujets")))
      return;

  if (!m_boosted)
    if (!(e.passes("rejets") || e.passes("rmujets")))
      return;
    
  HistogramService *h = &m_hSvc;
  TLorentzVector l;
  if (m_electron) {
    l = e.electron()[0].mom();
  } else {
    l = e.muon()[0].mom();
  }
  h->h1D("lepPt", "", s)->Fill(l.Perp()*1e-3, weight);
  h->h1D("lepEta", "", s)->Fill(l.Eta(), weight);
  h->h1D("lepPhi", "", s)->Fill(l.Phi(), weight);

  h->h1D("met_phi", "", s)->Fill(e.met().Phi(), weight);

  const TLorentzVector &j = e.jet()[0].mom();
  h->h1D("leadJetPt", "", s)->Fill(j.Perp()*1e-3, weight);
  
  // for now
  int nJets = e.jet().size(); //njets 
  h->h1D("nJets", "", s)->Fill(nJets, weight);
  
  int nBtagged = 0; //nB-tagged jets 
  for (size_t bidx = 0; bidx < e.jet().size(); ++bidx)
    if (e.jet()[bidx].btag_mv2c20_60()){
      if(nBtagged==0)h->h1D("leadbJetPt", "", s)->Fill(e.jet()[bidx].mom().Perp()*1e-3, weight);
      nBtagged += 1;
    }
   h->h1D("nBtagJets", "", s)->Fill(nBtagged, weight);

  // Jet kinematics  
  
  std::vector<float> jetMass_vector;
  std::vector<float> jetPt_vector;
  std::vector<float> jetEta_vector;
  std::vector<float> jetPhi_vector;
  
  jetMass_vector.resize(e.jet().size());
  jetPt_vector.resize(e.jet().size());
  jetEta_vector.resize(e.jet().size());
  jetPhi_vector.resize(e.jet().size());  
  
  size_t iJet = 0;
  for (; iJet < e.jet().size(); ++iJet){
    const TLorentzVector &jet_p4 = e.jet()[iJet].mom();
    jetMass_vector[iJet] =  e.jet()[iJet].mom().M();
    jetPt_vector[iJet]   =  e.jet()[iJet].mom().Pt();
    //std::cout << jetPt_vector[iJet] << std::endl;
    jetEta_vector[iJet]  =  e.jet()[iJet].mom().Eta();
    jetPhi_vector[iJet]  =  e.jet()[iJet].mom().Phi();    
  }//for
  
  int maxNjet = (e.jet().size()<6) ? e.jet().size() : 6;
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
  
  float mtt = 0;

  h->h1D("met", "", s)->Fill(e.met().Perp()*1e-3, weight);
    
  //transverse W mass  
  h->h1D("mwt", "", s)->Fill(sqrt(2. * l.Perp() * e.met().Perp() * (1. - cos(l.Phi() - e.met().Phi())))*1e-3, weight); 
  
  //mu
  h->h1D("mu", "", s)->Fill(e.mu(), weight); 

  if (m_boosted && (e.passes("bejets") || e.passes("bmujets"))) {

    size_t close_idx = 0;
    for (; close_idx < e.jet().size(); ++close_idx)
      if (e.jet()[close_idx].closeToLepton())
        break;
    const TLorentzVector &sj = e.jet()[close_idx].mom();
    h->h1D("closeJetPt", "", s)->Fill(sj.Perp()*1e-3, weight);

    size_t goodljet_idx = 0;
    for (; goodljet_idx < e.largeJet().size(); ++goodljet_idx)
      if (e.largeJet()[goodljet_idx].good())
        break;
    const TLorentzVector &lj = e.largeJet()[goodljet_idx].mom();
    h->h1D("largeJetPt", "", s)->Fill(lj.Perp()*1e-3, weight);
    h->h1D("largeJetM", "", s)->Fill(lj.M()*1e-3, weight);
    h->h1D("largeJetSd12", "", s)->Fill(e.largeJet()[goodljet_idx].split12()*1e-3, weight);

    // recalc. mtt
    // lepton = l
    // large-R jet = hadronic top = lj
    // selected jet = leptonic top's b-jet = sj
    // neutrino px, py = met
    std::vector<TLorentzVector*> vec_nu = m_neutrinoBuilder.candidatesFromWMass_Rotation(&l, e.met().Perp(), e.met().Phi(), true);   
    TLorentzVector nu(0,0,0,0);
    if (vec_nu.size() > 0) {
      nu = *(vec_nu[0]);
      for (size_t z = 0; z < vec_nu.size(); ++z) delete vec_nu[z];
      vec_nu.clear();
    }
    mtt = (lj+sj+nu+l).M();
    h->h1D("mtt", "", s)->Fill(mtt*1e-3, weight);
    h->h1D("mtlep_boo", "", s)->Fill((sj+nu+l).M()*1e-3, weight);
  }

  if (!m_boosted && (e.passes("rejets") || e.passes("rmujets"))) {

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
    for (size_t z = 0; z < e.jet().size(); ++z) {
      vjets.push_back(new TLorentzVector(0,0,0,0));
      vjets[z]->SetPtEtaPhiE(e.jet()[z].mom().Perp(), e.jet()[z].mom().Eta(), e.jet()[z].mom().Phi(), e.jet()[z].mom().E());
      // https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/BTagingxAODEDM
      // https://twiki.cern.ch/twiki/bin/view/AtlasProtected/BTaggingBenchmarks
      vjets_btagged.push_back(e.jet()[z].btag_mv2c20_60());
    }
    TLorentzVector met = e.met();
    bool status = m_chi2.findMinChiSquare(&l, &vjets, &vjets_btagged, &met, igj3, igj4, igb3, igb4, ign1, chi2ming1, chi2ming1H, chi2ming1L); 
    // status has to be true

    if (status) mtt = m_chi2.getResult_Mtt();
    
    for (size_t z = 0; z < vjets.size(); ++z) {
      delete vjets[z];
    }
    vjets.clear();
    vjets_btagged.clear();
    h->h1D("mtt", "", s)->Fill(mtt*1e-3, weight);
    h->h1D("mtlep_res", "", s)->Fill(m_chi2.getResult_Mtl()*1e-3, weight);
    h->h1D("mthad_res", "", s)->Fill(m_chi2.getResult_Mth()*1e-3, weight);
    h->h1D("mwhad_res", "", s)->Fill(m_chi2.getResult_Mwh()*1e-3, weight);
    h->h1D("chi2", "", s)->Fill(chi2ming1, weight);
  }


}

