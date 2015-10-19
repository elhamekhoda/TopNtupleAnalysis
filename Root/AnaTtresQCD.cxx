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
  Double_t closeLJpT_bins_r[8] = {25, 40, 60, 80, 100, 150, 250, 500};
  Double_t closeLJpT_bins_b[8] = {25, 40, 60, 80, 100, 150, 250, 500}; 
  
  //****Efficiency studies  
  //MC variables: electrons
  m_hSvc.create1D("MC_e_pt", "; Pt of MC electron [GeV]; Events", 40, 0, 500);
  m_hSvc.create1D("MC_e_eta", "; Eta of MC electron ; Events", 24, -3.0, 3.0);
  m_hSvc.create1D("MC_e_phi", "; Phi of MC electron ; Events", 40, -4.0, 4.0);
  m_hSvc.create1D("MC_e_m", "; Mass of MC electron [GeV]; Events", 100, -0.2, 0.2);  
  m_hSvc.create2D("MCe_pt_vs_eta", "; pt of electron(truth) [GeV]; #eta of electron(truth)", 40, 0, 500, 24, -3., 3.);
  
  //MC variables: muons
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

  //****Fake studies  
  m_hSvc.create1D("MET", "; Missing E_{T} [GeV]; Events", 25, 0, 25);
  m_hSvc.create1D("MET_phi", "; Missing E_{T} #phi; Events", 40, -4.0, 4.0);    
  m_hSvc.create1D("mwt", "; W transverse mass [GeV]; Events", 30, 0, 150);  
  
  if (!boosted)	{
     //Eff
     m_hSvc.create2DVar("LepMa_pt_vs_DR", 	"; Pt of Matched lepton [GeV]; min #Delta R(lep, jet)", 7, pT_bins_r, 7, DR_bins_r);
     m_hSvc.create1DVar("minDeltaR_jet_lept", 	"; min #Delta R(lep, jet); Events", 7, DR_bins_r);
     m_hSvc.create1DVar("lepMadR_pt",    	"; Pt of Matched lept [GeV]; Events", 7, pT_bins_r);
     //Fake 
     m_hSvc.create2DVar("lepPt_vs_closeJL_pt", 	"; Pt of lepton [GeV]; Pt of closest jet to the lept [GeV]", 7, pT_bins_r, 7, closeLJpT_bins_r);
     m_hSvc.create1DVar("closeLepJet_pt",    	"; Pt of closest jet to the lept [GeV]; Events", 7, closeLJpT_bins_r);
     m_hSvc.create1DVar("lep_pt",    		"; Pt of Matched lept [GeV]; Events", 7, pT_bins_r);
     
  }else	{
     //Eff	
     m_hSvc.create2DVar("LepMa_pt_vs_DR", 	"; Pt of Matched lepton [GeV]; min #Delta R(lep, jet)", 7, pT_bins_b, 7, DR_bins_b);
     m_hSvc.create1DVar("minDeltaR_jet_lept", 	"; min #Delta R(lep, jet); Events", 7, DR_bins_b);
     m_hSvc.create1DVar("lepMadR_pt",    	"; Pt of Matched lept [GeV]; Events", 7, pT_bins_b);
     //Fake 
     m_hSvc.create2DVar("lepPt_vs_closeJL_pt", 	"; Pt of lepton [GeV]; Pt of closest jet to the lept [GeV]", 7, pT_bins_b, 7, closeLJpT_bins_b);
     m_hSvc.create1DVar("closeLepJet_pt",    	"; Pt of closest jet to the lept [GeV]; Events", 7, closeLJpT_bins_b);     
     m_hSvc.create1DVar("lep_pt",    		"; Pt of Matched lept [GeV]; Events", 7, pT_bins_b);
     
  }

}

AnaTtresQCD::~AnaTtresQCD() {
}

void AnaTtresQCD::run(const Event &evt, double weight, const std::string &s){
}

void AnaTtresQCD::runEfficiency(const Event &evt, double weight, const std::string &s){
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
  
  //Pre-selection: 
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
	float deltaRapidity2  = 99;
        float deltaPhi2       = 99;

  	size_t jet_idx = 0;
  	for (; jet_idx < evt.jet().size(); ++jet_idx){  
	
          deltaRapidity2 = pow(evt.jet()[jet_idx].mom().Rapidity() - lept.Eta(), 2);
          
          deltaPhi2 = pow(evt.jet()[jet_idx].mom().DeltaPhi(lept), 2);
           
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
  
}//AnaTtresQCD::runEffRate 

void AnaTtresQCD::runFakeRate(const Event &evt, double weight, const std::string &s){
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
  
  TLorentzVector lept;  
  float mWt(0);  
  float mWt_threshold(100000);
  
  //lepton
  if (m_electron) 	lept = evt.electron()[0].mom(); 
  else			lept = evt.muon()[0].mom();   
 
  //transverse W mass 
  mWt = sqrt(2. * lept.Perp() * evt.met().Perp() * (1. - cos(lept.Phi() - evt.met().Phi()) )); 
  
  if (mWt < mWt_threshold){
  
     h->h1D("MET", "", s)	   ->Fill(evt.met().Perp()*1e-3, weight);
     h->h1D("MET_phi", "", s)->Fill(evt.met().Phi(), weight);  
     h->h1D("mwt", "", s)->Fill(mWt*1e-3, weight); 
  
     //deltaR between lepton and the closest narrow jet
  
     float deltaRapidity2  = 99;
     float deltaPhi2       = 99;
     float closejl_deltaR   = 99;
     float deltaR_tmp       = 99;
     int closejl_idx        = -1;
     float closejl_pT       = -1;
  
     size_t jet_idx = 0;
     for (; jet_idx < evt.jet().size(); ++jet_idx){  	

       deltaRapidity2 = pow(evt.jet()[jet_idx].mom().Rapidity() - lept.Eta(), 2); 
           
       deltaPhi2 = pow(evt.jet()[jet_idx].mom().DeltaPhi(lept), 2);
      
       deltaR_tmp = sqrt(deltaPhi2 + deltaRapidity2);

        if (deltaR_tmp < closejl_deltaR){
     	   closejl_deltaR = deltaR_tmp;
     	   closejl_idx = jet_idx;
	   closejl_pT  = evt.jet().at(jet_idx).mom().Pt();
	      
        }   
     }//for
     
     if (closejl_deltaR<99){
        h->h1D("closeLepJet_pt", "", s)	    ->Fill(closejl_pT*1e-3, weight);
	h->h1D("lep_pt", "", s)		    ->Fill(lept.Pt()*1e-3, weight);
	h->h2D("lepPt_vs_closeJL_pt", "", s)->Fill(lept.Perp()*1e-3, closejl_pT*1e-3, weight);      
     }//if(closejl_deltaR<99)
     
  }//if   
  
}//AnaTtresQCD::runFakeRate





