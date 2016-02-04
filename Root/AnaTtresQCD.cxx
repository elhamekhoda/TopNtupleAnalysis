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
    
  //****Efficiency studies   

  Double_t eff_pT_bins_re[7]     = {30, 35, 40, 50, 60, 120, 700};
  Double_t eff_pT_bins_rmu[8]    = {25, 30, 35, 40, 50, 70, 100, 700};
  Double_t eff_pT_bins_be[5]     = {30, 40, 60, 120, 700};
  Double_t eff_pT_bins_bmu[5]    = {25, 30, 40, 50, 700};

  Double_t DR_bins_re[6]  = {0., 0.4, 0.6, 1.0, 1.5, 5.0};
  Double_t DR_bins_rmu[7] = {0., 0.4, 0.6, 1.0, 1.5, 2.5, 5.0};
  Double_t DR_bins_be[5]  = {0., 0.4, 0.6, 1.0, 1.5};
  Double_t DR_bins_bmu[5] = {0., 0.4, 0.6, 1.0, 1.5};
    
  //MC variables:  
  m_hSvc.create2D("eff_MCe_pt_eta", "; pt of electron(truth) [GeV]; #eta of electron(truth)", 40, 0, 500, 24, -3., 3.);
  m_hSvc.create2D("eff_MCmu_pt_eta", "; pt of muon(truth) [GeV]; #eta of muon(truth)", 40, 0, 500, 24, -3., 3.);
  
  //Matched reco leptons  
  m_hSvc.create2D("eff_MaLep_pt_eta", "; pt of Matched lepton [GeV]; #eta of Matched lepton", 40, 0, 500, 24, -3., 3.);

  //****Fake studies  
   
  Double_t fake_pT_bins_re[7]  	 = {30, 35, 40, 50, 60, 120, 700};
  Double_t fake_closeLJpT_bins_re[2]  = {25, 500};
   
  Double_t fake_pT_bins_rmu[8] 	 = {25, 30, 35, 40, 50, 70, 100, 700};  
  Double_t fake_closeLJpT_bins_rmu[2] = {25, 500};
  
  Double_t fake_pT_bins_be[5]  	 = {30, 40, 60, 120, 700};
  Double_t fake_closeLJpT_bins_be[2]  = {25, 500};
  
  Double_t fake_pT_bins_bmu[5] 	 = {25, 30, 40, 50, 700};
  Double_t fake_closeLJpT_bins_bmu[2] = {25, 500}; 
  
  m_hSvc.create1D("fake_z0sin", 	"; z0*sin(#theta); Events", 50, -1, 1);
  m_hSvc.create1D("fake_z0", 		"; z0; Events", 25, -2, 2);
  m_hSvc.create1D("fake_d0", 		"; d0; Events", 25, -0.5, 0.5);
  m_hSvc.create1D("fake_d0sig", 	"; d0sig; Events", 30, -15, 15);
  m_hSvc.create1D("fake_MET", 		"; Missing E_{T} [GeV]; Events", 25, 0, 50);
  m_hSvc.create1D("fake_MET_phi", 	"; Missing E_{T} #phi; Events", 20, -4.0, 4.0);    
  m_hSvc.create1D("fake_mwt", 		"; W transverse mass [GeV]; Events", 15, 0, 150); 
  m_hSvc.create1D("fake_closJetPt",    	"; Pt of closest jet to lepton [GeV]; Events", 100, 25, 525);
  
  m_hSvc.create1D("fake_jvt_lowLepPt",  "; JVT (low lept Pt); Events",  25, -1.5, 1);
  m_hSvc.create1D("fake_jvt_highLepPt", "; JVT (high lept Pt); Events", 25, -1.5, 1);
    
  m_hSvc.create1D("fake_trig1",   "; trig1; Events", 2, 0, 2);
  m_hSvc.create1D("fake_trig2",   "; trig1; Events", 2, 0, 2);
  m_hSvc.create1D("fake_trig3",   "; trig1; Events", 2, 0, 2);
  m_hSvc.create1D("fake_trig4",   "; trig1; Events", 2, 0, 2);
  m_hSvc.create1D("fake_trig5",   "; trig1; Events", 2, 0, 2);
  
  m_hSvc.create1D("eventN", "; N event; Events", 10000, 0, 1e10);
  m_hSvc.create1D("runN",   "; N run; Events", 1000, 0, 1e10);

  int eff_N_pT_bins(0);
  int N_DR_bins(0);
  int fake_N_pT_bins(0);
  int fake_N_closeLJpT_bins(0);
  
  if (m_boosted){
    
     if (m_electron)  	{
     
        eff_N_pT_bins = sizeof(eff_pT_bins_be)/sizeof(eff_pT_bins_be[0]) -1;
	N_DR_bins = sizeof(DR_bins_be)/sizeof(DR_bins_be[0]) -1;
	
	fake_N_pT_bins = sizeof(fake_pT_bins_be)/sizeof(fake_pT_bins_be[0]) -1;
        fake_N_closeLJpT_bins = sizeof(fake_closeLJpT_bins_be)/sizeof(fake_closeLJpT_bins_be[0]) -1;

     	//Eff
  	m_hSvc.create2DVar("eff_LepPt_DR",       "; Pt of Matched lepton [GeV]; min #Delta R(lep, jet)", eff_N_pT_bins, eff_pT_bins_be, N_DR_bins, DR_bins_be);
  
  	//Fake 1D     
  	m_hSvc.create1DVar("fake_lepPt",  "; Pt of lepton [GeV]; Eff", fake_N_pT_bins, fake_pT_bins_be);
	
	//Fake 1D
	m_hSvc.create1DVar("fake_minDeltaR",   "; min #Delta R(lep, jet); Eff", N_DR_bins, DR_bins_be);


     }else{
     
        eff_N_pT_bins = sizeof(eff_pT_bins_bmu)/sizeof(eff_pT_bins_bmu[0]) -1;
	N_DR_bins = sizeof(DR_bins_bmu)/sizeof(DR_bins_bmu[0]) -1;
	
	fake_N_pT_bins = sizeof(fake_pT_bins_bmu)/sizeof(fake_pT_bins_bmu[0]) -1;
	fake_N_closeLJpT_bins = sizeof(fake_closeLJpT_bins_bmu)/sizeof(fake_closeLJpT_bins_bmu[0]) -1;
	
     	//Eff
  	m_hSvc.create2DVar("eff_LepPt_DR",       "; Pt of Matched lepton [GeV]; min #Delta R(lep, jet)", eff_N_pT_bins, eff_pT_bins_bmu, N_DR_bins, DR_bins_bmu);
  
  	//Fake 1D    
  	m_hSvc.create1DVar("fake_lepPt",  "; Pt of lepton [GeV]; Eff", fake_N_pT_bins, fake_pT_bins_bmu);

	//Fake 1D
	m_hSvc.create1DVar("fake_minDeltaR",   "; min #Delta R(lep, jet); Eff", N_DR_bins, DR_bins_bmu);

     }
  }else{
  
    if (m_electron){
        eff_N_pT_bins = sizeof(eff_pT_bins_re)/sizeof(eff_pT_bins_re[0]) -1;
	N_DR_bins = sizeof(DR_bins_re)/sizeof(DR_bins_re[0]) -1;
	
        fake_N_pT_bins = sizeof(fake_pT_bins_re)/sizeof(fake_pT_bins_re[0]) -1;
	fake_N_closeLJpT_bins = sizeof(fake_closeLJpT_bins_re)/sizeof(fake_closeLJpT_bins_re[0]) -1;
     
       	//Eff
 	m_hSvc.create2DVar("eff_LepPt_DR",       "; Pt of Matched lepton [GeV]; min #Delta R(lep, jet)", eff_N_pT_bins, eff_pT_bins_re, N_DR_bins, DR_bins_re);
  
  	//Fake 1D     
  	m_hSvc.create1DVar("fake_lepPt",  "; Pt of lepton [GeV]; Eff", fake_N_pT_bins, fake_pT_bins_re);
	
	//Fake 1D
	m_hSvc.create1DVar("fake_minDeltaR",   "; min #Delta R(lep, jet); Eff", N_DR_bins, DR_bins_re);
	
     }else{
     
        eff_N_pT_bins = sizeof(eff_pT_bins_rmu)/sizeof(eff_pT_bins_rmu[0]) -1;
	N_DR_bins = sizeof(DR_bins_rmu)/sizeof(DR_bins_rmu[0]) -1;
	
	fake_N_pT_bins = sizeof(fake_pT_bins_rmu)/sizeof(fake_pT_bins_rmu[0]) -1;	
	fake_N_closeLJpT_bins = sizeof(fake_closeLJpT_bins_rmu)/sizeof(fake_closeLJpT_bins_rmu[0]) -1;
     
     	//Eff
  	m_hSvc.create2DVar("eff_LepPt_DR",       "; Pt of Matched lepton [GeV]; min #Delta R(lep, jet)", eff_N_pT_bins, eff_pT_bins_rmu, N_DR_bins, DR_bins_rmu);
  
  	//Fake 1D     
  	m_hSvc.create1DVar("fake_lepPt",  "; Pt of lepton [GeV]; Eff", fake_N_pT_bins, fake_pT_bins_rmu);

	//Fake 1D
	m_hSvc.create1DVar("fake_minDeltaR",   "; min #Delta R(lep, jet); Eff", N_DR_bins, DR_bins_rmu);

     }	
  }//if (m_boosted) 


}//AnaTtresQCD::AnaTtresQCD

AnaTtresQCD::~AnaTtresQCD() {
}

void AnaTtresQCD::run(const Event &evt, double weight, const std::string &suffix){
}

void AnaTtresQCD::runEfficiency(const Event &evt, double weight, const std::string &suffix){
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
  
  if (!m_boosted)	if(evt.jet().size()<4)	return; 
  
  HistogramService *h = &m_hSvc;
  
  //Pre-selection: 
  ///Objects from the truth (MC) with (pT < 25GeV && |eta|<2.5)  
  
  ///Electrons  
  if (evt.MC_w1l_pdgId()==11){
  
  	if (evt.MC_w1l().Perp()<25000 || fabs(evt.MC_w1l().Eta())>2.5)	return;    	
  	h->h2D("eff_MCe_pt_eta", "", suffix)->Fill(evt.MC_w1l().Perp()*1e-3, evt.MC_w1l().Eta()); 
	
  }else if(evt.MC_w2l_pdgId()==-11){  
  
  	if (evt.MC_w2l().Perp()<25000 || fabs(evt.MC_w2l().Eta())>2.5)	return; 	
  	h->h2D("eff_MCe_pt_eta", "", suffix)->Fill(evt.MC_w2l().Perp()*1e-3, evt.MC_w2l().Eta()); 
	
  }//if
    
  ///Muons 
  if (evt.MC_w1l_pdgId()==13){
  
  	if (evt.MC_w1l().Perp()<25000 || fabs(evt.MC_w1l().Eta())>2.5)	return; 	
  	h->h2D("eff_MCmu_pt_eta", "", suffix) ->Fill(evt.MC_w1l().Perp()*1e-3, evt.MC_w1l().Eta()); 
		
  }else if(evt.MC_w2l_pdgId()==-13){
  
  	if (evt.MC_w2l().Perp()<25000 || fabs(evt.MC_w2l().Eta())>2.5)	return;		
  	h->h2D("eff_MCmu_pt_eta", "", suffix) ->Fill(evt.MC_w2l().Perp()*1e-3, evt.MC_w2l().Eta()); 
	
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

  // Duplicated event removal after the selection  
  if (suffix=="_Loose" && isDuplicateEvent(evt.runNumber(), evt.eventNumber(), lept.Perp()) ){
      m_Nduplicate++;
      return;
  }
   
  if (leptMa_pdgId!=0){
  		  
  	h->h2D("eff_MaLep_pt_eta", "", suffix)->Fill(lept.Perp()*1e-3, lept.Eta());  
	
	//deltaR between lepton and the closest narrow jet
  	float closejl_deltaR  = 99;
  	float deltaR_tmp      = 99;
  	int closejl_idx       = -1;
	float deltaRapidity2  = 99;
        float deltaPhi2       = 99;

  	size_t jet_idx = 0;
  	for (; jet_idx < evt.jet().size(); ++jet_idx){  
	
          deltaRapidity2 = pow(evt.jet()[jet_idx].mom().Rapidity() - lept.Rapidity(), 2);          
          deltaPhi2 = pow(evt.jet()[jet_idx].mom().DeltaPhi(lept), 2);           
          deltaR_tmp = sqrt(deltaPhi2 + deltaRapidity2);
	  
    	  if (deltaR_tmp < closejl_deltaR){
              closejl_deltaR = deltaR_tmp;
              closejl_idx = jet_idx;
    	  }   
  	}//for    
	 
	if (closejl_deltaR<99)	h->h2D("eff_LepPt_DR", "", suffix)    ->Fill(lept.Perp()*1e-3, closejl_deltaR, weight);

  }//(leptMa_pdgId!=0)
  
}//AnaTtresQCD::runEffRate 

void AnaTtresQCD::runFakeRate(const Event &evt, double weight, const std::string &suffix){
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
  
  if (!m_boosted)	if(evt.jet().size()<4)	return;
  
  HistogramService *h = &m_hSvc;
  
  h->h1D("eventN", "", suffix)->Fill(evt.eventNumber());
  h->h1D("runN", "", suffix)->Fill(evt.runNumber());
  
  TLorentzVector lept; 
  float theta(0);
  float z0(0);  
  float d0(0);  
  float d0sig(0); 
    
  bool trig1(0); 
  bool trig2(0); 
  bool trig3(0);
  bool trig4(0);
  bool trig5(0);
    
  float mWt(0);  
  float mWt_threshold(100*1e3);
  
  bool isTight;
  
  //lepton
  if (m_electron) {	
  	lept  = evt.electron()[0].mom();
	z0    = evt.electron()[0].z0();
	d0    = evt.electron()[0].d0();
	d0sig = evt.electron()[0].sd0();
	theta = 2*atan(exp(-lept.Eta()));
	isTight = evt.electron()[0].isTightPP();
	
	//Electron trigers
	trig1 = evt.electron()[0].HLT_e24_lhmedium_L1EM18VH(); 		// MC / data prescaled
	trig2 = evt.electron()[0].HLT_e24_lhmedium_L1EM20VH(); 		// data	only
	trig3 = evt.electron()[0].HLT_e60_lhmedium();
	trig4 = evt.electron()[0].HLT_e120_lhloose();
		
	bool trig_MC = trig1 || trig3 || trig4;	
	bool trig_DT = trig2 || trig3 || trig4;
	
	if (evt.channelNumber()!=0){
	  if (!trig_MC)return;
	}else{
	  if (!trig_DT)return;
	}			
  
  } else{			
  	lept  = evt.muon()[0].mom();
	z0    = evt.muon()[0].z0();	   
	d0    = evt.muon()[0].d0();	   
	d0sig = evt.muon()[0].sd0();
	theta = 2*atan(exp(-lept.Eta()));
	isTight = evt.muon()[0].isTight();
	
	//Muon triggers
	trig1 = evt.muon()[0].HLT_mu20_L1MU15(); //prescaled
	trig2 = evt.muon()[0].HLT_mu50();
	trig3 = evt.muon()[0].HLT_mu20_iloose_L1MU15();
	
	bool trig_prescaled   = trig1;
	bool trig_unprescaled = trig2 || trig3;
	
	if (suffix=="_Loose"){
	 if (evt.channelNumber()!=0) if (trig_prescaled && !trig_unprescaled)		weight *= 1/10.;
	}
	else{
	 if (trig_prescaled && !trig_unprescaled)		return;	 
	}	
	
  }//m_electron
    
  // Duplicated event removal after the selection  
  if (suffix=="_Loose" && isDuplicateEvent(evt.runNumber(), evt.eventNumber(), lept.Perp()) ){
      m_Nduplicate++;
      return;
  }
  
  h->h1D("fake_trig1", "", suffix)  ->Fill(trig1);
  h->h1D("fake_trig2", "", suffix)  ->Fill(trig2);
  h->h1D("fake_trig3", "", suffix)  ->Fill(trig3);
  h->h1D("fake_trig4", "", suffix)  ->Fill(trig4);
  h->h1D("fake_trig5", "", suffix)  ->Fill(trig5);
      
  // Transverse W mass 
  mWt = sqrt(2. * lept.Perp() * evt.met().Perp() * (1. - cos(lept.Phi() - evt.met().Phi()) )); 
    
  if (mWt < mWt_threshold){
     h->h1D("fake_z0sin", "", suffix)  ->Fill(z0*sin(theta), weight);
     h->h1D("fake_z0", "", suffix)     ->Fill(z0, weight);
     h->h1D("fake_d0", "", suffix)     ->Fill(d0, weight);
     h->h1D("fake_d0sig", "", suffix)  ->Fill(d0sig, weight);
     h->h1D("fake_MET", "", suffix)    ->Fill(evt.met().Perp()*1e-3, weight);
     h->h1D("fake_MET_phi", "", suffix)->Fill(evt.met().Phi(), weight);  
     h->h1D("fake_mwt", "", suffix)    ->Fill(mWt*1e-3, weight); 
           
     //deltaR between lepton and the closest narrow jet
  
     float deltaRapidity2   = 99;
     float deltaPhi2        = 99;
     float closejl_deltaR   = 99;
     float deltaR_tmp       = 99;
     int closejl_idx        = -1;
     float closejl_pT       = -1;
  
     size_t jet_idx = 0;
     for (; jet_idx < evt.jet().size(); ++jet_idx){  	

       deltaRapidity2 = pow(evt.jet()[jet_idx].mom().Rapidity() - lept.Rapidity(), 2);            
       deltaPhi2 = pow(evt.jet()[jet_idx].mom().DeltaPhi(lept), 2);      
       deltaR_tmp = sqrt(deltaPhi2 + deltaRapidity2);

        if (deltaR_tmp < closejl_deltaR){
     	   closejl_deltaR = deltaR_tmp;
     	   closejl_idx = jet_idx;	   	      
        }   
     }//for
     
     if (closejl_deltaR<99){
     
        closejl_pT  = evt.jet().at(closejl_idx).mom().Pt();
	h->h1D("fake_minDeltaR", "", suffix)	    ->Fill(closejl_deltaR, weight);         
	h->h1D("fake_lepPt", "", suffix)	    ->Fill(lept.Pt()*1e-3, weight);
	h->h1D("fake_closJetPt", "", suffix)	    ->Fill(closejl_pT*1e-3, weight);
		
	if (closejl_deltaR < 0.4){	
		if (lept.Pt()<50000) h->h1D("fake_jvt_lowLepPt", "", suffix)->Fill(evt.jet().at(closejl_idx).jvt(), weight);
		else		     h->h1D("fake_jvt_highLepPt", "", suffix)->Fill(evt.jet().at(closejl_idx).jvt(), weight);
	}
     }//if(closejl_deltaR<99)
     
  }//if   
  
}//AnaTtresQCD::runFakeRate






