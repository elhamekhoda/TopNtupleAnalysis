/**
 * @brief Analysis class for tt resonances.
 * @author Danilo Enoque Ferreira de Lima <dferreir@cern.ch>
 */

#include "TopNtupleAnalysis/Analysis.h"
#include "TopNtupleAnalysis/AnaTtresQCD.h"
#include "TopNtupleAnalysis/Event.h"
#include "TLorentzVector.h"
#include <vector>
#include <string>
#include "TopNtupleAnalysis/HistogramService.h"

AnaTtresQCD::AnaTtresQCD(const std::string &filename, bool electron, bool boosted, std::vector<std::string> &systList)
  : Analysis(filename, systList), m_electron(electron), m_boosted(boosted),
    m_neutrinoBuilder("MeV"), m_chi2("MeV") {

  m_chi2.Init(TtresChi2::DATA2015_MC15);

  Double_t pT_bins_r[8] = {25, 40, 60, 80, 100, 150, 250, 500};
  Double_t pT_bins_b[8] = {25, 40, 60, 80, 100, 150, 250, 500}; 
  Double_t DR_bins_r[8] = {0.,0.2, 0.4, 0.6, 0.8, 1.0, 1.7, 5.0};
  Double_t DR_bins_b[8] = {0.,0.2, 0.4, 0.6, 0.8, 1.0, 1.7, 5.0};
    
  //Histograms for MC variables
  //electrons
  m_hSvc.create1D("MC_e_pt", "; Pt of MC electron [GeV]; Events", 40, 0, 500);
  m_hSvc.create1D("MC_e_eta", "; Eta of MC electron ; Events", 24, -3.0, 3.0);
  m_hSvc.create1D("MC_e_phi", "; Phi of MC electron ; Events", 40, -4.0, 4.0);
  m_hSvc.create1D("MC_e_m", "; Mass of MC electron [GeV]; Events", 100, -0.2, 0.2);  
  m_hSvc.create2D("MCe_pt_vs_eta", "; pt of electron(truth) [GeV]; #eta of electron(truth)", 40, 0, 500, 24, -3., 3.);
  
  //muons
  m_hSvc.create1D("MC_mu_pt", "; Pt of MC muon [GeV]; Events", 40, 0, 500);
  m_hSvc.create1D("MC_mu_eta", "; Eta of MC muon ; Events", 24, -3.0, 3.0);
  m_hSvc.create1D("MC_mu_phi", "; Phi of MC muon ; Events", 40, -4.0, 4.0);
  m_hSvc.create1D("MC_mu_m", "; Mass of MC muon [GeV]; Events", 100, -0.2, 0.2);  
  m_hSvc.create2D("MCmu_pt_vs_eta", "; pt of muon(truth) [GeV]; #eta of muon(truth)", 40, 0, 500, 24, -3., 3.);
  
  //Matched reco leptons
  m_hSvc.create1D("lepMa_pt",    "; Pt of Matched lept [GeV]; Events", 40, 0, 500);
  m_hSvc.create1D("lepMa_eta",   "; #eta of Matched lept ; Events", 24, -3.0, 3.0);
  m_hSvc.create1D("lepMa_phi",   "; #phi of Matched lept ; Events", 40, -4.0, 4.0);
  m_hSvc.create1D("lepMa_m",     "; Mass of Matched lept [GeV]; Events", 100, -0.2, 0.2);
  m_hSvc.create1D("lepMa_pdgId", "; pdgId of Matched lept ; Events", 30, -15, 15);
  m_hSvc.create2D("Ma_pt_vs_eta", "; pt of Matched lepton [GeV]; #eta of Matched lepton", 40, 0, 500, 24, -3., 3.);

  //Delta R between the Ma reco leptons and the closest jet
  
  if (!boosted)	{
     m_hSvc.create2DVar("LepMa_pt_vs_DR", "; pt of Matched lepton [GeV]; min #Delta R(lep, jet)", 7, pT_bins_r, 7, DR_bins_r);
     m_hSvc.create1DVar("minDeltaR_jet_lept", "; min #Delta R(lep, jet); Events", 7, DR_bins_r);
     m_hSvc.create1DVar("lepMadR_pt",    "; Pt of Matched lept [GeV]; Events", 7, pT_bins_r);
     
  }else	{	
     m_hSvc.create2DVar("LepMa_pt_vs_DR", "; pt of Matched lepton [GeV]; min #Delta R(lep, jet)", 7, pT_bins_b, 7, DR_bins_b);
     m_hSvc.create1DVar("minDeltaR_jet_lept", "; min #Delta R(lep, jet); Events", 7, DR_bins_b);
     m_hSvc.create1DVar("lepMadR_pt",    "; Pt of Matched lept [GeV]; Events", 7, pT_bins_b);
     
  }

}

AnaTtresQCD::~AnaTtresQCD() {
}

void AnaTtresQCD::run(const Event &evt, double weight, const std::string &s) {
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
  
  //Pre-selection
  
  ///Objects from the truth (MC) with (pT < 25GeV && |eta|<2.5)
  
  ///Electrons
  
  if (evt.MC_w1l_pdgId()==11){
  
  	if (evt.MC_w1l().Perp()<25000 || fabs(evt.MC_w1l().Eta())>2.5)	return;   
  	h->h1D("MC_e_pt", "", s)      ->Fill(evt.MC_w1l().Perp()*1e-3);
  	h->h1D("MC_e_eta", "", s)     ->Fill(evt.MC_w1l().Eta());
  	h->h1D("MC_e_phi", "", s)     ->Fill(evt.MC_w1l().Phi());
  	h->h1D("MC_e_m", "", s)       ->Fill(evt.MC_w1l().M()*1e-3);
  	h->h2D("MCe_pt_vs_eta", "", s)->Fill(evt.MC_w1l().Perp()*1e-3, evt.MC_w1l().Eta()); 
  }else if(evt.MC_w2l_pdgId()==-11){  
  
  	if (evt.MC_w2l().Perp()<25000 || fabs(evt.MC_w2l().Eta())>2.5)	return; 	
	h->h1D("MC_e_pt", "", s)      ->Fill(evt.MC_w2l().Perp()*1e-3);
  	h->h1D("MC_e_eta", "", s)     ->Fill(evt.MC_w2l().Eta());
  	h->h1D("MC_e_phi", "", s)     ->Fill(evt.MC_w2l().Phi());
  	h->h1D("MC_e_m", "", s)       ->Fill(evt.MC_w2l().M()*1e-3);
  	h->h2D("MCe_pt_vs_eta", "", s)->Fill(evt.MC_w2l().Perp()*1e-3, evt.MC_w2l().Eta()); 
  }//if
    
  ///Muons
 
  if (evt.MC_w1l_pdgId()==13){
  
  	if (evt.MC_w1l().Perp()<25000 || fabs(evt.MC_w1l().Eta())>2.5)	return;         	
	h->h1D("MC_mu_pt", "", s) 	->Fill(evt.MC_w1l().Perp()*1e-3);
  	h->h1D("MC_mu_eta", "", s)	->Fill(evt.MC_w1l().Eta());
  	h->h1D("MC_mu_phi", "", s)	->Fill(evt.MC_w1l().Phi());
  	h->h1D("MC_mu_m", "", s)  	->Fill(evt.MC_w1l().M()*1e-3);
  	h->h2D("MCmu_pt_vs_eta", "", s) ->Fill(evt.MC_w1l().Perp()*1e-3, evt.MC_w1l().Eta()); 	
  }else if(evt.MC_w2l_pdgId()==-13){
  
  	if (evt.MC_w2l().Perp()<25000 || fabs(evt.MC_w2l().Eta())>2.5)	return;	        
	h->h1D("MC_mu_pt", "", s) 	->Fill(evt.MC_w2l().Perp()*1e-3);
  	h->h1D("MC_mu_eta", "", s)	->Fill(evt.MC_w2l().Eta());
  	h->h1D("MC_mu_phi", "", s)	->Fill(evt.MC_w2l().Phi());
  	h->h1D("MC_mu_m", "", s)  	->Fill(evt.MC_w2l().M()*1e-3);
  	h->h2D("MCmu_pt_vs_eta", "", s) ->Fill(evt.MC_w2l().Perp()*1e-3, evt.MC_w2l().Eta()); 
  }//if

  ///----------------------------------
  //Matching truth and reco lepton
  ///----------------------------------
  
  TLorentzVector lept;    
  int leptMa_pdgId = 0;

  float dr = 99;
  float drMax = 0.4;
  
  if (m_electron) {  
    lept = evt.electron()[0].mom();       
    
    if (evt.MC_w1l_pdgId()==11){
    	dr = lept.DeltaR(evt.MC_w1l());
	if (dr<drMax)	leptMa_pdgId = evt.MC_w1l_pdgId();
	
    }else if (evt.MC_w2l_pdgId()==-11){
    	dr = lept.DeltaR(evt.MC_w2l());
    	if (dr<drMax)	leptMa_pdgId = evt.MC_w2l_pdgId();
	
    }else if (abs(evt.MC_w1l_pdgId())==13 || abs(evt.MC_w2l_pdgId())==13)	std::cout << "reco electron and truth muon" << std::endl;
	   
  } else {
    lept = evt.muon()[0].mom();   
    
    if (evt.MC_w1l_pdgId()==13){
    	dr = lept.DeltaR(evt.MC_w1l());
	if (dr<drMax)	leptMa_pdgId = evt.MC_w1l_pdgId();
	
    }else if (evt.MC_w2l_pdgId()==-13){
    	dr = lept.DeltaR(evt.MC_w2l());
	if (dr<drMax)	leptMa_pdgId = evt.MC_w2l_pdgId();
	
    }else if (abs(evt.MC_w1l_pdgId())==11 || abs(evt.MC_w2l_pdgId())==11)    	std::cout << "reco muon and truth electron" << std::endl;    
  
  }//m_electron
 
  if (leptMa_pdgId!=0){
  	//std::cout << "Matched lepton" << std::endl;
	//std::cout << "m_electron: " << m_electron << " -> Matched to MC: " << leptMa_pdgId << std::endl;
	//std::cout << "Ma lepton pT:" << lept.Pt() << std::endl;	
	  
  	//Filling histograms
  	h->h1D("lepMa_pt", "", s)   ->Fill(lept.Perp()*1e-3);
  	h->h1D("lepMa_eta", "", s)  ->Fill(lept.Eta()    );
  	h->h1D("lepMa_phi", "", s)  ->Fill(lept.Phi()    );
  	h->h1D("lepMa_m", "", s)    ->Fill(lept.M()*1e-3 ); 
  	h->h1D("lepMa_pdgId", "", s)->Fill(leptMa_pdgId  ); 
  	h->h2D("Ma_pt_vs_eta", "", s)->Fill(lept.Perp()*1e-3, lept.Eta());  
	
	//deltaR between lepton and the closest narrow jet
  	float closejl_deltaR  = 99;
  	float deltaR_tmp      = 99;
  	int closejl_idx       = -1;
	double deltaRapidity2  = 99;
        double deltaPhi2       = 99;

  	size_t jet_idx = 0;
  	for (; jet_idx < evt.jet().size(); ++jet_idx){  
	
	  deltaRapidity2 = evt.jet()[jet_idx].mom().Rapidity() - lept.Eta();
          deltaRapidity2 = pow(deltaRapidity2, 2);
          
          deltaPhi2 = evt.jet()[jet_idx].mom().Phi() - lept.Phi();
          deltaPhi2 = pow(deltaPhi2, 2);
           
          //deltaR_tmp = lept.DeltaR(evt.jet()[jet_idx].mom());
          deltaR_tmp = sqrt(deltaPhi2 + deltaRapidity2);
	  
    	  if (deltaR_tmp < closejl_deltaR){
              closejl_deltaR = deltaR_tmp;
              closejl_idx = jet_idx;
    	  }   
  	}//for     
  	
	if (closejl_deltaR<99){
  	   h->h1D("minDeltaR_jet_lept", "", s)->Fill(closejl_deltaR); 
	   h->h2D("LepMa_pt_vs_DR", "", s)    ->Fill(lept.Perp()*1e-3, closejl_deltaR);
	   h->h1D("lepMadR_pt", "", s)        ->Fill(lept.Perp()*1e-3);

	}//(closejl_deltaR<99)
  }//(leptMa_pdgId!=0)
  
  
  //std::cout << " -- " << std::endl;

  
  /*
  std::cout << " ** reco lepton ** " << std::endl;
  std::cout << "m_electron: " << m_electron << std::endl;
  std::cout << "lept.Pt(): " << lept.Perp() << " lept.M(): " << lept.M() << " lept.Eta(): " << lept.Eta() << " lept.Phi(): " << lept.Phi() << std::endl;
  std::cout << " ** truth lepton ** " << std::endl;
  std::cout << "evt.MC_w1l().Pt(): " << evt.MC_w1l().Perp() << " evt.MC_w1l().M(): " << evt.MC_w1l().M() << " evt.MC_w1l().Eta(): " << evt.MC_w1l().Eta() << " evt.MC_w1l().Phi(): " << evt.MC_w1l().Phi() << std::endl;
  std::cout << "evt.MC_w2l().Pt(): " << evt.MC_w2l().Perp() << " evt.MC_w2l().M(): " << evt.MC_w2l().M() << " evt.MC_w2l().Eta(): " << evt.MC_w2l().Eta() << " evt.MC_w2l().Phi(): " << evt.MC_w2l().Phi() << std::endl;
  std::cout << "pdgId1: " << evt.MC_w1l_pdgId() << " - pdgId2: " << evt.MC_w2l_pdgId() << std::endl;
  std::cout << "dr: " << dr << std::endl;
  std::cout << "leptMa_pdgId: " << leptMa_pdgId << std::endl;
  std::cout << "--" << std::endl;
  */

}//AnaTtresQCD::run

