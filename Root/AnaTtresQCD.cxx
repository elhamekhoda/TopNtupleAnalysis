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
   
  Double_t eff_pT_bins_re[]     = {30, 35, 40, 60, 85, 120, 250, 400, 700};
  Double_t eff_pT_bins_rmu[]    = {25, 30, 35, 40, 50, 70, 100, 250, 700};
  Double_t eff_pT_bins_be[]     = {30, 40, 60, 120, 700};
  Double_t eff_pT_bins_bmu[]    = {25, 35, 50, 100, 700};

  Double_t DR_bins_re[]  	= {0., 0.4, 0.6, 1.0, 1.5, 5.0};
  //Double_t DR_bins_rmu[] 	= {0., 0.4, 0.6, 1.0, 1.5, 2.5, 5.0};
  //Double_t DR_bins_rmu[]        = {0., 0.2, 0.35, 0.4, 0.5, 0.55, 0.6, 1.0, 1.5, 2.5, 5.0};
  Double_t DR_bins_rmu[]        = {0., 0.4, 0.5, 0.6, 1.0, 1.5, 2.5, 5.0};
  Double_t DR_bins_be[]  	= {0., 0.4, 0.6, 0.8, 1.0, 1.5};
  Double_t DR_bins_bmu[] 	= {0., 0.2, 0.3, 0.4, 0.5, 1.5};
    
  //MC variables:  
  m_hSvc.create2D("eff_MCe_pt_eta", "; pt of electron(truth) [GeV]; #eta of electron(truth)", 40, 0, 500, 24, -3.5, 3.5);
  m_hSvc.create2D("eff_MCmu_pt_eta", "; pt of muon(truth) [GeV]; #eta of muon(truth)", 40, 0, 500, 24, -3.5, 3.5);
  
  m_hSvc.create1D("eff_d0sig", 		"; d0sig; Events", 30, -15, 15);
  m_hSvc.create1D("eff_nJets",          "; number of jets ; Events", 10, -0.5, 9.5);
  m_hSvc.create1D("eff_nTrkBtagJets",   "; number of b-tagged track jets ; Events", 10, 0, 10);
    
  //Matched reco leptons  
  m_hSvc.create2D("eff_MaLep_pt_eta", "; pt of Matched lepton [GeV]; #eta of Matched lepton", 40, 0, 500, 24, -3., 3.);

  //****Fake studies  
   
  m_hSvc.create1D("eventN",           "; N event; Events", 10000, 0, 1e10);
  m_hSvc.create1D("runN",   	      "; N run; Events", 1000, 0, 1e10); 
  m_hSvc.create1D("fake_z0sin",       "; z0*sin(#theta); Events", 50, -1, 1);
  m_hSvc.create1D("fake_d0sig",       "; d0sig; Events", 200, -100, 100);
  m_hSvc.create1D("fake_MET", 	      "; Missing E_{T} [GeV]; Events", 100, 0, 500);
  m_hSvc.create1D("fake_MET_phi",     "; Missing E_{T} #phi; Events", 20, -4.0, 4.0);	
  m_hSvc.create1D("fake_mwt", 	      "; W transverse mass [GeV]; Events", 50, 0, 500);
  m_hSvc.create1D("fake_mwt_met",     "; MET + MWT [GeV]; Events", 50, 0, 500);
  m_hSvc.create1D("fake_closJetPt",   "; Pt of closest jet to lepton [GeV]; Events", 100, 25, 525);
  m_hSvc.create1D("fake_nJets",       "; number of jets ; Events", 10, -0.5, 9.5);
  m_hSvc.create1D("fake_nTrkBtagJets","; number of b-tagged track jets ; Events", 10, 0, 10); 
   
  double varBin1[] = {0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 220, 240, 260, 280, 300, 340, 380, 450, 700};
  int varBinN1 = sizeof(varBin1)/sizeof(double) - 1;
  
  //double CdPhiBin[] = {-1.0, -0.6, -0.2, 0.2, 0.6, 1.0};
  double CdPhiBin[] = {-1.0, -0.98, -0.8, -0.20, 0.20, 0.40, 0.60, 0.70, 0.80, 0.85, 0.90, 0.92, 0.94, 0.96, 0.98, 1.0};
  int CdPhiBinN = sizeof(CdPhiBin)/sizeof(double) - 1; 
    
  m_hSvc.create1DVar("fake_lepPt",  	        	"; lepton p_{T} [GeV]; Events", varBinN1, varBin1);
  m_hSvc.create1DVar("fake_cos_metPhi_lepPhi_effBins",  "; Cos( met #phi - lept #phi ); Events", CdPhiBinN, CdPhiBin);
  m_hSvc.create1D("fake_cos_metPhi_lepPhi",  		"; Cos( met #phi - lept #phi ); Events", 50, -1, 1);
  
  m_hSvc.create1D("fake_closJetJVT", 		"; JVT of closest Jet to lepton ; Events", 20, -1, 1); 
  m_hSvc.create1D("fake_minDeltaR",      	"; min #Delta R(lep, jet); Events", 50, 0, 5); 
  m_hSvc.create1D("fake_lepPhi",         	"; lepton #phi; Events", 20, -4.0, 4.0);  
  m_hSvc.create1D("fake_lepEta",         	"; lepton #eta; Events", 20, -4.0, 4.0);  
   
  m_hSvc.create1DVar("fake_lowCos_lepPt",  	        "; lepton p_{T} [GeV]; Events", varBinN1, varBin1);
  m_hSvc.create1D("fake_lowCos_cos_metPhi_lepPhi",   	"; Cos( met #phi - lept #phi ); Events", 100, -1, 1);
  m_hSvc.create1D("fake_lowCos_MET", 	      		"; Missing E_{T} [GeV]; Events", 50, 0, 300);
  m_hSvc.create1D("fake_lowCos_d0sig",       		"; d0sig; Events", 200, -100, 100);
  m_hSvc.create1D("fake_lowCos_mwt", 	      		"; W transverse mass [GeV]; Events", 30, 0, 300); 
  m_hSvc.create1D("fake_lowCos_minDeltaR",      	"; min #Delta R(lep, jet); Events", 50, 0, 5); 
  m_hSvc.create2D("fake_lowCos_lepEtaVSPhi",         "; lepton #eta; lepton #phi", 20, -4, 4, 20, -4, 4);

  m_hSvc.create1DVar("fake_highCos_lepPt",  	        "; lepton p_{T} [GeV]; Events", varBinN1, varBin1);
  m_hSvc.create1D("fake_highCos_cos_metPhi_lepPhi",   	"; Cos( met #phi - lept #phi ); Events", 100, -1, 1);
  m_hSvc.create1D("fake_highCos_MET", 	      		"; Missing E_{T} [GeV]; Events", 50, 0, 300);
  m_hSvc.create1D("fake_highCos_d0sig",       		"; d0sig; Events", 200, -100, 100);
  m_hSvc.create1D("fake_highCos_mwt", 	      		"; W transverse mass [GeV]; Events", 30, 0, 300); 
  m_hSvc.create1D("fake_highCos_minDeltaR",      	"; min #Delta R(lep, jet); Events", 50, 0, 5); 
  m_hSvc.create2D("fake_highCos_lepEtaVSPhi", 		"; lepton #eta; lepton #phi", 20, -4, 4, 20, -4, 4);

  m_hSvc.create1D("fake_trig1",  "; trig1; Events", 2, 0, 2);
  m_hSvc.create1D("fake_trig2",  "; trig1; Events", 2, 0, 2);
  m_hSvc.create1D("fake_trig3",  "; trig1; Events", 2, 0, 2);
  m_hSvc.create1D("fake_trig4",  "; trig1; Events", 2, 0, 2);
  m_hSvc.create1D("fake_trig5",  "; trig1; Events", 2, 0, 2);
  
  double metBin[] = {20, 30, 40, 50, 60, 70, 80, 150, 400};
  int metBinN = sizeof(metBin)/sizeof(double) - 1; 
  m_hSvc.create1DVar("fake_MET_effBins", 	      "; Missing E_{T} [GeV]; Events", metBinN, metBin);
  
  double mwtBin[] = {0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 300, 400};
  int mwtBinN = sizeof(mwtBin)/sizeof(double) - 1; 
  m_hSvc.create1DVar("fake_mwt_effBins", 	      "; W transverse mass [GeV]; Events", mwtBinN, mwtBin);
  
  double mwtmetBin[] = {60, 65, 70, 75, 80, 85, 90, 100, 120, 150, 400};
  int mwtmetBinN = sizeof(mwtmetBin)/sizeof(double) - 1; 
  m_hSvc.create1DVar("fake_mwt_met_effBins", 	      "; MET + MWT [GeV]; Events", mwtmetBinN, mwtmetBin);
  
  Double_t fake_pT_bins_re[]  	 	= {30, 35, 40, 60, 85, 120, 700};
  Double_t fake_leptEta_bins_re[]    	= {0.0, 1.6, 2.5};
  Double_t fake_closeLJpT_bins_re[]  	= {20, 40, 60, 80, 100, 700};
   
  Double_t fake_pT_bins_rmu[] 	 	= {25, 30, 40, 50, 700};  
  Double_t fake_leptEta_bins_rmu[]    	= {0.0, 1.6, 2.5};
  Double_t fake_closeLJpT_bins_rmu[] 	= {20, 40, 60, 80, 100, 700};
  
  Double_t fake_pT_bins_be[]  	 	= {30, 60, 120, 700};
  Double_t fake_leptEta_bins_be[]    	= {0.0, 1.6, 2.5};
  Double_t fake_closeLJpT_bins_be[]  	= {20, 40, 60, 80, 100, 700};
  
  Double_t fake_pT_bins_bmu[] 	 	= {25, 50, 100, 700};
  Double_t fake_leptEta_bins_bmu[]    	= {0.0, 1.6 ,2.5};
  Double_t fake_closeLJpT_bins_bmu[] 	= {20, 40, 60, 80, 100, 700}; 
    
  int eff_N_pT_bins(0);
  int N_DR_bins(0);
  int fake_N_pT_bins(0);
  int fake_N_leptEta_bins(0);
  int fake_N_closeLJpT_bins(0);
  
  if (m_boosted){
    
     if (m_electron)  	{
     
        eff_N_pT_bins 		= sizeof(eff_pT_bins_be)/sizeof(double) -1;
	N_DR_bins 		= sizeof(DR_bins_be)/sizeof(double) -1;	
	fake_N_pT_bins 		= sizeof(fake_pT_bins_be)/sizeof(double) -1;
	fake_N_leptEta_bins 	= sizeof(fake_leptEta_bins_be)/sizeof(double) -1;
        fake_N_closeLJpT_bins 	= sizeof(fake_closeLJpT_bins_be)/sizeof(double) -1;

     	//Eff
  	m_hSvc.create2DVar("eff_LepPt_DR", "; Pt of Matched lepton [GeV]; min #Delta R(lep, jet)", eff_N_pT_bins, eff_pT_bins_be, N_DR_bins, DR_bins_be);
  
  	//Fake 1D     
  	m_hSvc.create1DVar("fake_lepPt_effBins", 	  "; Pt of lepton [GeV]; Eff", fake_N_pT_bins, fake_pT_bins_be);
	
	//Fake 1D
	m_hSvc.create1DVar("fake_minDeltaR_effBins",   	  "; min #Delta R(lep, jet); Eff", N_DR_bins, DR_bins_be);
	
	//Fake 1D
	m_hSvc.create1DVar("fake_closJetPt_effBins",      "; Pt of closest jet to lepton [GeV]; Eff", fake_N_closeLJpT_bins, fake_closeLJpT_bins_be);
	
	//Fake 2D
	m_hSvc.create2DVar("fake_lepPt_lepEta",   	  "; Pt of lepton [GeV]; |#eta| of lepton", fake_N_pT_bins, fake_pT_bins_be, fake_N_leptEta_bins, fake_leptEta_bins_be);
	m_hSvc.create2DVar("fake_lepPt_closJetPt",   	  "; Pt of lepton [GeV]; Pt of closest jet to lepton [GeV]", fake_N_pT_bins, fake_pT_bins_be, fake_N_closeLJpT_bins, fake_closeLJpT_bins_be);
	m_hSvc.create2DVar("fake_closJetPt_cosDPhi",       "; Pt of closest jet to lepton [GeV]; Cos( met #phi - lept #phi )",   fake_N_closeLJpT_bins, fake_closeLJpT_bins_be, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_minDeltaR_cosDPhi", 	   "; min #Delta R(lep, jet); Cos( met #phi - lept #phi )", N_DR_bins, DR_bins_be, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_minDeltaR_cosDPhi_highLepPt", "; min #Delta R(lep, jet); Cos( met #phi - lept #phi )", N_DR_bins, DR_bins_be, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_minDeltaR_cosDPhi_lowLepPt",  "; min #Delta R(lep, jet); Cos( met #phi - lept #phi )", N_DR_bins, DR_bins_be, CdPhiBinN, CdPhiBin);
	
	m_hSvc.create2DVar("fake_lepPt_cosDPhi",   	  "; Pt of lepton [GeV]; Cos( met #phi - lept #phi )", fake_N_pT_bins, fake_pT_bins_be, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_lepPt_cosDPhi_lowEta",   "; Pt of lepton [GeV]; Cos( met #phi - lept #phi )", fake_N_pT_bins, fake_pT_bins_be, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_lepPt_cosDPhi_highEta",  "; Pt of lepton [GeV]; Cos( met #phi - lept #phi )", fake_N_pT_bins, fake_pT_bins_be, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_lepPt_cosDPhi_lowDR",    "; Pt of lepton [GeV]; Cos( met #phi - lept #phi )", fake_N_pT_bins, fake_pT_bins_be, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_lepPt_cosDPhi_highDR",   "; Pt of lepton [GeV]; Cos( met #phi - lept #phi )", fake_N_pT_bins, fake_pT_bins_be, CdPhiBinN, CdPhiBin);
	
	m_hSvc.create2DVar("fake_lepPt_minDeltaR",   	  "; Pt of lepton [GeV]; min #Delta R(lep, jet)", fake_N_pT_bins, fake_pT_bins_be, N_DR_bins, DR_bins_be);
	m_hSvc.create2DVar("fake_lepPt_minDeltaR_lowCos", "; Pt of lepton [GeV]; min #Delta R(lep, jet)", fake_N_pT_bins, fake_pT_bins_be, N_DR_bins, DR_bins_be);
	m_hSvc.create2DVar("fake_lepPt_minDeltaR_highCos","; Pt of lepton [GeV]; min #Delta R(lep, jet)", fake_N_pT_bins, fake_pT_bins_be, N_DR_bins, DR_bins_be);
	
	m_hSvc.create2DVar("fake_lepPt_met",		   "; Pt of lepton [GeV]; MET [GeV] ", fake_N_pT_bins, fake_pT_bins_be, metBinN, metBin);
	m_hSvc.create2DVar("fake_lepPt_met",	   	   "; Pt of lepton [GeV]; MET [GeV] ", fake_N_pT_bins, fake_pT_bins_be, metBinN, metBin);
	m_hSvc.create2DVar("fake_lepPt_met_lowDR", 	   "; Pt of lepton [GeV]; MET [GeV] ", fake_N_pT_bins, fake_pT_bins_be, metBinN, metBin);
	m_hSvc.create2DVar("fake_lepPt_met_highDR",	   "; Pt of lepton [GeV]; MET [GeV] ", fake_N_pT_bins, fake_pT_bins_be, metBinN, metBin);
	m_hSvc.create2DVar("fake_minDeltaR_met_highLepPt", "; min #Delta R(lep, jet); MET [GeV]", N_DR_bins, DR_bins_be, metBinN, metBin);
	m_hSvc.create2DVar("fake_minDeltaR_met_lowLepPt",  "; min #Delta R(lep, jet); MET [GeV]", N_DR_bins, DR_bins_be, metBinN, metBin);
	
	//ljet
	m_hSvc.create1D("fake_ljet_pt",    	"; Pt of largeR jet [GeV]; Events", 100, 0, 1000);
	m_hSvc.create1D("fake_ljet_m",    	"; mass of largeR jet [GeV]; Events", 50, 0, 200);
	m_hSvc.create1D("fake_ljet_tau32", 	"; #tau_{32}; Events", 20, 0, 1);
	m_hSvc.create1D("fake_ljet_tau32_wta", 	"; #tau_{32} wta; Events", 20, 0, 1);

     }else{
     
        eff_N_pT_bins 		= sizeof(eff_pT_bins_bmu)/sizeof(double) -1;
	N_DR_bins 		= sizeof(DR_bins_bmu)/sizeof(double) -1;	
	fake_N_pT_bins 		= sizeof(fake_pT_bins_bmu)/sizeof(double) -1;
        fake_N_leptEta_bins 	= sizeof(fake_leptEta_bins_bmu)/sizeof(double) -1;
	fake_N_closeLJpT_bins 	= sizeof(fake_closeLJpT_bins_bmu)/sizeof(double) -1;
	
     	//Eff
  	m_hSvc.create2DVar("eff_LepPt_DR", "; Pt of Matched lepton [GeV]; min #Delta R(lep, jet)", eff_N_pT_bins, eff_pT_bins_bmu, N_DR_bins, DR_bins_bmu);
  
  	//Fake 1D    
  	m_hSvc.create1DVar("fake_lepPt_effBins", 	  "; Pt of lepton [GeV]; Eff", fake_N_pT_bins, fake_pT_bins_bmu);
	m_hSvc.create1DVar("fake_minDeltaR_effBins",   "; min #Delta R(lep, jet); Eff", N_DR_bins, DR_bins_bmu);
	m_hSvc.create1DVar("fake_closJetPt_effBins",   "; Pt of closest jet to lepton [GeV]; Eff", fake_N_closeLJpT_bins, fake_closeLJpT_bins_bmu);
	
	//Fake 2D
	m_hSvc.create2DVar("fake_lepPt_lepEta",      "; Pt of lepton [GeV]; |#eta| of lepton",		   fake_N_pT_bins, fake_pT_bins_bmu, fake_N_leptEta_bins, fake_leptEta_bins_bmu);
	m_hSvc.create2DVar("fake_lepPt_closJetPt",   "; Pt of lepton [GeV]; Pt of closest jet to lepton [GeV]",  fake_N_pT_bins, fake_pT_bins_bmu, fake_N_closeLJpT_bins, fake_closeLJpT_bins_bmu);		
	m_hSvc.create2DVar("fake_closJetPt_cosDPhi", "; Pt of closest jet to lepton [GeV]; Cos( met #phi - lept #phi )",   fake_N_closeLJpT_bins, fake_closeLJpT_bins_bmu, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_minDeltaR_cosDPhi", "; min #Delta R(lep, jet); Cos( met #phi - lept #phi )", N_DR_bins, DR_bins_bmu, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_minDeltaR_cosDPhi_highLepPt", "; min #Delta R(lep, jet); Cos( met #phi - lept #phi )", N_DR_bins, DR_bins_bmu, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_minDeltaR_cosDPhi_lowLepPt",  "; min #Delta R(lep, jet); Cos( met #phi - lept #phi )", N_DR_bins, DR_bins_bmu, CdPhiBinN, CdPhiBin);
	
	m_hSvc.create2DVar("fake_lepPt_cosDPhi",   	  "; Pt of lepton [GeV]; Cos( met #phi - lept #phi )", fake_N_pT_bins, fake_pT_bins_bmu, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_lepPt_cosDPhi_lowEta",   "; Pt of lepton [GeV]; Cos( met #phi - lept #phi )", fake_N_pT_bins, fake_pT_bins_bmu, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_lepPt_cosDPhi_highEta",  "; Pt of lepton [GeV]; Cos( met #phi - lept #phi )", fake_N_pT_bins, fake_pT_bins_bmu, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_lepPt_cosDPhi_lowDR",    "; Pt of lepton [GeV]; Cos( met #phi - lept #phi )", fake_N_pT_bins, fake_pT_bins_bmu, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_lepPt_cosDPhi_highDR",   "; Pt of lepton [GeV]; Cos( met #phi - lept #phi )", fake_N_pT_bins, fake_pT_bins_bmu, CdPhiBinN, CdPhiBin);
	
	m_hSvc.create2DVar("fake_lepPt_minDeltaR",   	   "; Pt of lepton [GeV]; min #Delta R(lep, jet)", fake_N_pT_bins, fake_pT_bins_bmu, N_DR_bins, DR_bins_bmu);
	m_hSvc.create2DVar("fake_lepPt_minDeltaR_lowCos",  "; Pt of lepton [GeV]; min #Delta R(lep, jet)", fake_N_pT_bins, fake_pT_bins_bmu, N_DR_bins, DR_bins_bmu);
	m_hSvc.create2DVar("fake_lepPt_minDeltaR_highCos", "; Pt of lepton [GeV]; min #Delta R(lep, jet)", fake_N_pT_bins, fake_pT_bins_bmu, N_DR_bins, DR_bins_bmu);
	
	m_hSvc.create2DVar("fake_lepPt_met",		   "; Pt of lepton [GeV]; MET [GeV] ", fake_N_pT_bins, fake_pT_bins_bmu, metBinN, metBin);
	m_hSvc.create2DVar("fake_lepPt_met",	   	   "; Pt of lepton [GeV]; MET [GeV] ", fake_N_pT_bins, fake_pT_bins_bmu, metBinN, metBin);
	m_hSvc.create2DVar("fake_lepPt_met_lowDR", 	   "; Pt of lepton [GeV]; MET [GeV] ", fake_N_pT_bins, fake_pT_bins_bmu, metBinN, metBin);
	m_hSvc.create2DVar("fake_lepPt_met_highDR",	   "; Pt of lepton [GeV]; MET [GeV] ", fake_N_pT_bins, fake_pT_bins_bmu, metBinN, metBin);
	m_hSvc.create2DVar("fake_minDeltaR_met_highLepPt", "; min #Delta R(lep, jet); MET [GeV]", N_DR_bins, DR_bins_bmu, metBinN, metBin);
	m_hSvc.create2DVar("fake_minDeltaR_met_lowLepPt",  "; min #Delta R(lep, jet); MET [GeV]", N_DR_bins, DR_bins_bmu, metBinN, metBin);
	
	//ljet
	m_hSvc.create1D("fake_ljet_pt",    	"; Pt of largeR jet [GeV]; Events", 100, 0, 1000);
	m_hSvc.create1D("fake_ljet_m",    	"; mass of largeR jet [GeV]; Events", 50, 0, 200);
	m_hSvc.create1D("fake_ljet_tau32", 	"; #tau_{32}; Events", 20, 0, 1);
	m_hSvc.create1D("fake_ljet_tau32_wta", 	"; #tau_{32} wta; Events", 20, 0, 1);
	
     }
  }else{
  
    if (m_electron){
        eff_N_pT_bins 		= sizeof(eff_pT_bins_re)/sizeof(double) -1;
	N_DR_bins 		= sizeof(DR_bins_re)/sizeof(double) -1;	
        fake_N_pT_bins 		= sizeof(fake_pT_bins_re)/sizeof(double) -1;
	fake_N_leptEta_bins 	= sizeof(fake_leptEta_bins_re)/sizeof(double) -1;
	fake_N_closeLJpT_bins 	= sizeof(fake_closeLJpT_bins_re)/sizeof(double) -1;
     
       	//Eff
 	m_hSvc.create2DVar("eff_LepPt_DR", "; Pt of Matched lepton [GeV]; min #Delta R(lep, jet)", eff_N_pT_bins, eff_pT_bins_re, N_DR_bins, DR_bins_re);
  
  	//Fake 1D     
  	m_hSvc.create1DVar("fake_lepPt_effBins",   "; Pt of lepton [GeV]; Eff", fake_N_pT_bins, fake_pT_bins_re);
	m_hSvc.create1DVar("fake_lepEta_effBins",  "; |#eta| of lepton; Eff", fake_N_leptEta_bins, fake_leptEta_bins_re);
	m_hSvc.create1DVar("fake_minDeltaR_effBins", "; min #Delta R(lep, jet); Eff", N_DR_bins, DR_bins_re);
	m_hSvc.create1DVar("fake_closJetPt_effBins", "; Pt of closest jet to lepton [GeV]; Eff", fake_N_closeLJpT_bins, fake_closeLJpT_bins_re);
	
	//Fake 2D
	m_hSvc.create2DVar("fake_lepPt_lepEta",   	   "; Pt of lepton [GeV]; |#eta| of lepton", fake_N_pT_bins, fake_pT_bins_re, fake_N_leptEta_bins, fake_leptEta_bins_re);
	m_hSvc.create2DVar("fake_lepPt_closJetPt",   	   "; Pt of lepton [GeV]; Pt of closest jet to lepton [GeV]", fake_N_pT_bins, fake_pT_bins_re, fake_N_closeLJpT_bins, fake_closeLJpT_bins_re);
	m_hSvc.create2DVar("fake_closJetPt_cosDPhi", 	   "; Pt of closest jet to lepton [GeV]; Cos( met #phi - lept #phi )",   fake_N_closeLJpT_bins, fake_closeLJpT_bins_re, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_minDeltaR_cosDPhi",       "; min #Delta R(lep, jet); Cos( met #phi - lept #phi )", N_DR_bins, DR_bins_re, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_minDeltaR_cosDPhi_highLepPt", "; min #Delta R(lep, jet); Cos( met #phi - lept #phi )", N_DR_bins, DR_bins_re, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_minDeltaR_cosDPhi_lowLepPt",  "; min #Delta R(lep, jet); Cos( met #phi - lept #phi )", N_DR_bins, DR_bins_re, CdPhiBinN, CdPhiBin);
	
	m_hSvc.create2DVar("fake_lepPt_cosDPhi",   	  "; Pt of lepton [GeV]; Cos( met #phi - lept #phi )", fake_N_pT_bins, fake_pT_bins_re, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_lepPt_cosDPhi_lowEta",   "; Pt of lepton [GeV]; Cos( met #phi - lept #phi )", fake_N_pT_bins, fake_pT_bins_re, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_lepPt_cosDPhi_highEta",  "; Pt of lepton [GeV]; Cos( met #phi - lept #phi )", fake_N_pT_bins, fake_pT_bins_re, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_lepPt_cosDPhi_lowDR",    "; Pt of lepton [GeV]; Cos( met #phi - lept #phi )", fake_N_pT_bins, fake_pT_bins_re, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_lepPt_cosDPhi_highDR",   "; Pt of lepton [GeV]; Cos( met #phi - lept #phi )", fake_N_pT_bins, fake_pT_bins_re, CdPhiBinN, CdPhiBin);
		
	m_hSvc.create2DVar("fake_lepPt_minDeltaR",   	  "; Pt of lepton [GeV]; min #Delta R(lep, jet)", fake_N_pT_bins, fake_pT_bins_re, N_DR_bins, DR_bins_re);
	m_hSvc.create2DVar("fake_lepPt_minDeltaR_lowCos", "; Pt of lepton [GeV]; min #Delta R(lep, jet)", fake_N_pT_bins, fake_pT_bins_re, N_DR_bins, DR_bins_re);
	m_hSvc.create2DVar("fake_lepPt_minDeltaR_highCos","; Pt of lepton [GeV]; min #Delta R(lep, jet)", fake_N_pT_bins, fake_pT_bins_re, N_DR_bins, DR_bins_re);
	
	m_hSvc.create2DVar("fake_lepPt_met",		   "; Pt of lepton [GeV]; MET [GeV] ", fake_N_pT_bins, fake_pT_bins_re, metBinN, metBin);
	m_hSvc.create2DVar("fake_lepPt_met",	   	   "; Pt of lepton [GeV]; MET [GeV] ", fake_N_pT_bins, fake_pT_bins_re, metBinN, metBin);
	m_hSvc.create2DVar("fake_lepPt_met_lowDR", 	   "; Pt of lepton [GeV]; MET [GeV] ", fake_N_pT_bins, fake_pT_bins_re, metBinN, metBin);
	m_hSvc.create2DVar("fake_lepPt_met_highDR",	   "; Pt of lepton [GeV]; MET [GeV] ", fake_N_pT_bins, fake_pT_bins_re, metBinN, metBin);
	m_hSvc.create2DVar("fake_minDeltaR_met_highLepPt", "; min #Delta R(lep, jet); MET [GeV]", N_DR_bins, DR_bins_re, metBinN, metBin);
	m_hSvc.create2DVar("fake_minDeltaR_met_lowLepPt",  "; min #Delta R(lep, jet); MET [GeV]", N_DR_bins, DR_bins_re, metBinN, metBin);
		
	//chi2
	m_hSvc.create1D("fake_chi2", "; log(#chi^{2}) ; Events", 50, -3, 7);

     }else{
     
        eff_N_pT_bins 		= sizeof(eff_pT_bins_rmu)/sizeof(double) -1;
	N_DR_bins 		= sizeof(DR_bins_rmu)/sizeof(double) -1;	
	fake_N_pT_bins 		= sizeof(fake_pT_bins_rmu)/sizeof(double) -1;	
	fake_N_leptEta_bins 	= sizeof(fake_leptEta_bins_rmu)/sizeof(double) -1;
	fake_N_closeLJpT_bins 	= sizeof(fake_closeLJpT_bins_rmu)/sizeof(double) -1;
     
     	//Eff
  	m_hSvc.create2DVar("eff_LepPt_DR", "; Pt of Matched lepton [GeV]; min #Delta R(lep, jet)", eff_N_pT_bins, eff_pT_bins_rmu, N_DR_bins, DR_bins_rmu);
  
  	//Fake 1D     
  	m_hSvc.create1DVar("fake_lepPt_effBins",  "; Pt of lepton [GeV]; Eff", fake_N_pT_bins, fake_pT_bins_rmu);
	m_hSvc.create1DVar("fake_minDeltaR_effBins",    "; min #Delta R(lep, jet); Eff", N_DR_bins, DR_bins_rmu);
	m_hSvc.create1DVar("fake_lepEta_effBins",  	"; |#eta| of lepton; Eff", fake_N_leptEta_bins, fake_leptEta_bins_rmu);
	m_hSvc.create1DVar("fake_closJetPt_effBins",    "; Pt of closest jet to lepton [GeV]; Eff", fake_N_closeLJpT_bins, fake_closeLJpT_bins_rmu);
	
	//Fake 2D
	m_hSvc.create2DVar("fake_lepPt_lepEta",   	  "; Pt of lepton [GeV]; |#eta| of lepton", fake_N_pT_bins, fake_pT_bins_rmu, fake_N_leptEta_bins, fake_leptEta_bins_rmu);
	m_hSvc.create2DVar("fake_lepPt_closJetPt",   	  "; Pt of lepton [GeV]; Pt of closest jet to lepton [GeV]", fake_N_pT_bins, fake_pT_bins_rmu, fake_N_closeLJpT_bins, fake_closeLJpT_bins_rmu);
	m_hSvc.create2DVar("fake_closJetPt_cosDPhi", 	  "; Pt of closest jet to lepton [GeV]; Cos( met #phi - lept #phi )",   fake_N_closeLJpT_bins, fake_closeLJpT_bins_rmu, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_minDeltaR_cosDPhi",      "; min #Delta R(lep, jet); Cos( met #phi - lept #phi )", N_DR_bins, DR_bins_rmu, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_minDeltaR_cosDPhi_highLepPt", "; min #Delta R(lep, jet); Cos( met #phi - lept #phi )", N_DR_bins, DR_bins_rmu, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_minDeltaR_cosDPhi_lowLepPt",  "; min #Delta R(lep, jet); Cos( met #phi - lept #phi )", N_DR_bins, DR_bins_rmu, CdPhiBinN, CdPhiBin);
	
	m_hSvc.create2DVar("fake_lepPt_cosDPhi",   	  "; Pt of lepton [GeV]; Cos( met #phi - lept #phi )", fake_N_pT_bins, fake_pT_bins_rmu, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_lepPt_cosDPhi_lowEta",   "; Pt of lepton [GeV]; Cos( met #phi - lept #phi )", fake_N_pT_bins, fake_pT_bins_rmu, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_lepPt_cosDPhi_highEta",  "; Pt of lepton [GeV]; Cos( met #phi - lept #phi )", fake_N_pT_bins, fake_pT_bins_rmu, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_lepPt_cosDPhi_lowDR",    "; Pt of lepton [GeV]; Cos( met #phi - lept #phi )", fake_N_pT_bins, fake_pT_bins_rmu, CdPhiBinN, CdPhiBin);
	m_hSvc.create2DVar("fake_lepPt_cosDPhi_highDR",   "; Pt of lepton [GeV]; Cos( met #phi - lept #phi )", fake_N_pT_bins, fake_pT_bins_rmu, CdPhiBinN, CdPhiBin);
	
	m_hSvc.create2DVar("fake_lepPt_minDeltaR",   	  "; Pt of lepton [GeV]; min #Delta R(lep, jet)", fake_N_pT_bins, fake_pT_bins_rmu, N_DR_bins, DR_bins_rmu);
	m_hSvc.create2DVar("fake_lepPt_minDeltaR_lowCos", "; Pt of lepton [GeV]; min #Delta R(lep, jet)", fake_N_pT_bins, fake_pT_bins_rmu, N_DR_bins, DR_bins_rmu);
	m_hSvc.create2DVar("fake_lepPt_minDeltaR_highCos","; Pt of lepton [GeV]; min #Delta R(lep, jet)", fake_N_pT_bins, fake_pT_bins_rmu, N_DR_bins, DR_bins_rmu);
	
	m_hSvc.create2DVar("fake_lepPt_met",	   	   "; Pt of lepton [GeV]; MET [GeV] ", fake_N_pT_bins, fake_pT_bins_rmu, metBinN, metBin);
	m_hSvc.create2DVar("fake_lepPt_met_lowDR", 	   "; Pt of lepton [GeV]; MET [GeV] ", fake_N_pT_bins, fake_pT_bins_rmu, metBinN, metBin);
	m_hSvc.create2DVar("fake_lepPt_met_highDR",	   "; Pt of lepton [GeV]; MET [GeV] ", fake_N_pT_bins, fake_pT_bins_rmu, metBinN, metBin);
	m_hSvc.create2DVar("fake_minDeltaR_met_highLepPt", "; min #Delta R(lep, jet); MET [GeV]", N_DR_bins, DR_bins_rmu, metBinN, metBin);
	m_hSvc.create2DVar("fake_minDeltaR_met_lowLepPt",  "; min #Delta R(lep, jet); MET [GeV]", N_DR_bins, DR_bins_rmu, metBinN, metBin);
	
	//chi2
	m_hSvc.create1D("fake_chi2", "; log(#chi^{2}) ; Events", 50, -3, 7);
     }	
  }//if (m_boosted) 


}//AnaTtresQCD::AnaTtresQCD

AnaTtresQCD::~AnaTtresQCD() {
}

void AnaTtresQCD::run(const Event &evt, double weight, const std::string &suffix){
}


//**************************
//******* Real Rates *******
//**************************


void AnaTtresQCD::runRealRateQCDCR(const Event &evt, double weight, const std::string &suffix){
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
  bool isTight;
   
  ///Electrons  
  if (evt.MC_w1l_pdgId()==11){

  	if (evt.MC_w1l().Perp()<15000 || fabs(evt.MC_w1l().Eta())>3.0)  return; 	
  	h->h2D("eff_MCe_pt_eta", "", suffix)->Fill(evt.MC_w1l().Perp()*1e-3, evt.MC_w1l().Eta()); 

  }else if(evt.MC_w2l_pdgId()==-11){  

  	if (evt.MC_w2l().Perp()<15000 || fabs(evt.MC_w2l().Eta())>3.0)  return; 	
  	h->h2D("eff_MCe_pt_eta", "", suffix)->Fill(evt.MC_w2l().Perp()*1e-3, evt.MC_w2l().Eta()); 

  }//if
    
  ///Muons 
  if (evt.MC_w1l_pdgId()==13){

  	if (evt.MC_w1l().Perp()<15000 || fabs(evt.MC_w1l().Eta())>3.0)  return; 	
  	h->h2D("eff_MCmu_pt_eta", "", suffix) ->Fill(evt.MC_w1l().Perp()*1e-3, evt.MC_w1l().Eta()); 
  		
  }else if(evt.MC_w2l_pdgId()==-13){

  	if (evt.MC_w2l().Perp()<15000 || fabs(evt.MC_w2l().Eta())>3.0)  return; 	
  	h->h2D("eff_MCmu_pt_eta", "", suffix) ->Fill(evt.MC_w2l().Perp()*1e-3, evt.MC_w2l().Eta()); 

  }//if

  ///----------------------------------
  //Matching truth and reco lepton
  ///----------------------------------

  TLorentzVector lept;    
  int leptMa_pdgId = 0;

  float dr = 99;
  float drMax = 0.4;

  float d0sig(0); 
  bool trig1(0); 
  bool trig2(0); 
  bool trig3(0);
  bool trig4(0);
  bool trig5(0);

  if (m_electron) {  
    lept = evt.electron()[0].mom();	  
    d0sig = evt.electron()[0].sd0();
    
    //Electron trigers
    trig1 = evt.electron()[0].HLT_e24_lhmedium_L1EM18VH();		// MC / data prescaled
    trig2 = evt.electron()[0].HLT_e24_lhmedium_L1EM20VH();		// data only
    trig3 = evt.electron()[0].HLT_e60_lhmedium();
    trig4 = evt.electron()[0].HLT_e120_lhloose();

    isTight = evt.electron()[0].isTightPP();
  		
    bool trig_MC = trig1 || trig3 || trig4;	
    bool trig_DT = trig2 || trig3 || trig4;

    if (evt.channelNumber()!=0){
  	  if (!trig_MC)return;
    }else{
  	  if (!trig_DT)return;
    }			
    
    if (evt.MC_w1l_pdgId()==11 || evt.MC_w1l_pdgId()==15){
  	dr = lept.DeltaR(evt.MC_w1l());
  	if (dr<drMax)	leptMa_pdgId = evt.MC_w1l_pdgId();

    }else if (evt.MC_w2l_pdgId()==-11 || evt.MC_w2l_pdgId()==-15){
  	dr = lept.DeltaR(evt.MC_w2l());
  	if (dr<drMax)	leptMa_pdgId = evt.MC_w2l_pdgId();

    }else if (abs(evt.MC_w1l_pdgId())==13 || abs(evt.MC_w2l_pdgId())==13)	std::cout << "reco electron and truth muon" << std::endl;
  	   
  } else {
    lept = evt.muon()[0].mom();   
    d0sig = evt.muon()[0].sd0();
    
    //Muon triggers
    trig1 = evt.muon()[0].HLT_mu20_L1MU15(); //prescaled
    trig2 = evt.muon()[0].HLT_mu50();
    trig3 = evt.muon()[0].HLT_mu20_iloose_L1MU15();

    isTight = evt.muon()[0].isTight();

    bool trig_prescaled   = trig1;
    bool trig_unprescaled = trig2 || trig3;

    if (!isTight) {
  	 if (evt.channelNumber()!=0) if (trig_prescaled && !trig_unprescaled)		weight *= 1/10.;
    }
    else{
  	 if (trig_prescaled && !trig_unprescaled)		return;  
    }	
    
    if (evt.MC_w1l_pdgId()==13 || evt.MC_w1l_pdgId()==15){
  	dr = lept.DeltaR(evt.MC_w1l());
  	if (dr<drMax)	leptMa_pdgId = evt.MC_w1l_pdgId();

    }else if (evt.MC_w2l_pdgId()==-13 || evt.MC_w2l_pdgId()==-15){
  	dr = lept.DeltaR(evt.MC_w2l());
  	if (dr<drMax)	leptMa_pdgId = evt.MC_w2l_pdgId();

    }else if (abs(evt.MC_w1l_pdgId())==11 || abs(evt.MC_w2l_pdgId())==11)	std::cout << "reco muon and truth electron" << std::endl;    

  }//m_electron

  h->h1D("eff_d0sig", "", suffix)  ->Fill(d0sig, weight);

  h->h1D("trig1", "", suffix)  ->Fill(trig1);
  h->h1D("trig2", "", suffix)  ->Fill(trig2);
  h->h1D("trig3", "", suffix)  ->Fill(trig3);
  h->h1D("trig4", "", suffix)  ->Fill(trig4);
  h->h1D("trig5", "", suffix)  ->Fill(trig5);
  
  if (leptMa_pdgId!=0)	GetRealHistograms(evt, weight, suffix);

}//AnaTtresQCD::runRealRateQCDCR


void AnaTtresQCD::runRealRateWQCDCR(const Event &evt, double weight, const std::string &suffix){
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

  if (!m_boosted)	if(evt.jet().size()<2)	return; 
  
  HistogramService *h = &m_hSvc;
	  
  //Pre-selection: 
  ///Objects from the truth (MC) with (pT < 25GeV && |eta|<2.5)  
     
  ///Electrons  
  if (evt.MC_w1l_pdgId()==11){

  	if (evt.MC_w1l().Perp()<15000 || fabs(evt.MC_w1l().Eta())>3.0)  return; 	
  	h->h2D("eff_MCe_pt_eta", "", suffix)->Fill(evt.MC_w1l().Perp()*1e-3, evt.MC_w1l().Eta()); 

  }else if(evt.MC_w2l_pdgId()==-11){  

  	if (evt.MC_w2l().Perp()<15000 || fabs(evt.MC_w2l().Eta())>3.0)  return; 	
  	h->h2D("eff_MCe_pt_eta", "", suffix)->Fill(evt.MC_w2l().Perp()*1e-3, evt.MC_w2l().Eta()); 

  }//if
    
  ///Muons 
  if (evt.MC_w1l_pdgId()==13){

  	if (evt.MC_w1l().Perp()<15000 || fabs(evt.MC_w1l().Eta())>3.0)  return; 	
  	h->h2D("eff_MCmu_pt_eta", "", suffix) ->Fill(evt.MC_w1l().Perp()*1e-3, evt.MC_w1l().Eta()); 
  		
  }else if(evt.MC_w2l_pdgId()==-13){

  	if (evt.MC_w2l().Perp()<15000 || fabs(evt.MC_w2l().Eta())>3.0)  return; 	
  	h->h2D("eff_MCmu_pt_eta", "", suffix) ->Fill(evt.MC_w2l().Perp()*1e-3, evt.MC_w2l().Eta()); 

  }//if

  ///----------------------------------
  //Matching truth and reco lepton
  ///----------------------------------

  TLorentzVector lept;    
  int leptMa_pdgId = 0;

  float dr = 99;
  float drMax = 0.4;

  float d0sig(0); 
  bool trig1(0); 
  bool trig2(0); 
  bool trig3(0);
  bool trig4(0);
  bool trig5(0);
  
  bool isTight(0);

  if (m_electron) {  
    lept = evt.electron()[0].mom();	  
    d0sig = evt.electron()[0].sd0();
    
    //Electron trigers
    trig1 = evt.electron()[0].HLT_e24_lhmedium_L1EM18VH();		// MC / data prescaled
    trig2 = evt.electron()[0].HLT_e24_lhmedium_L1EM20VH();		// data only
    trig3 = evt.electron()[0].HLT_e60_lhmedium();
    trig4 = evt.electron()[0].HLT_e120_lhloose();

    isTight = evt.electron()[0].isTightPP();
  		
    bool trig_MC = trig1 || trig3 || trig4;	
    bool trig_DT = trig2 || trig3 || trig4;

    if (evt.channelNumber()!=0){
  	  if (!trig_MC)return;
    }else{
  	  if (!trig_DT)return;
    }			
    
    if (evt.MC_w1l_pdgId()==11 || evt.MC_w1l_pdgId()==15){
  	dr = lept.DeltaR(evt.MC_w1l());
  	if (dr<drMax)	leptMa_pdgId = evt.MC_w1l_pdgId();

    }else if (evt.MC_w2l_pdgId()==-11 || evt.MC_w2l_pdgId()==-15){
  	dr = lept.DeltaR(evt.MC_w2l());
  	if (dr<drMax)	leptMa_pdgId = evt.MC_w2l_pdgId();

    }else if (abs(evt.MC_w1l_pdgId())==13 || abs(evt.MC_w2l_pdgId())==13)	std::cout << "reco electron and truth muon" << std::endl;
  	   
  } else {
    lept = evt.muon()[0].mom();   
    d0sig = evt.muon()[0].sd0();
    
    //Muon triggers
    trig1 = evt.muon()[0].HLT_mu20_L1MU15(); //prescaled
    trig2 = evt.muon()[0].HLT_mu50();
    trig3 = evt.muon()[0].HLT_mu20_iloose_L1MU15();

    isTight = evt.muon()[0].isTight();

    bool trig_prescaled   = trig1;
    bool trig_unprescaled = trig2 || trig3;

    if (!isTight) {
  	 if (evt.channelNumber()!=0) if (trig_prescaled && !trig_unprescaled)		weight *= 1/10.;
    }
    else{
  	 if (trig_prescaled && !trig_unprescaled)		return;  
    }	
    
    if (evt.MC_w1l_pdgId()==13 || evt.MC_w1l_pdgId()==15){
  	dr = lept.DeltaR(evt.MC_w1l());
  	if (dr<drMax)	leptMa_pdgId = evt.MC_w1l_pdgId();

    }else if (evt.MC_w2l_pdgId()==-13 || evt.MC_w2l_pdgId()==-15){
  	dr = lept.DeltaR(evt.MC_w2l());
  	if (dr<drMax)	leptMa_pdgId = evt.MC_w2l_pdgId();

    }else if (abs(evt.MC_w1l_pdgId())==11 || abs(evt.MC_w2l_pdgId())==11)	std::cout << "reco muon and truth electron" << std::endl;    

  }//m_electron

  h->h1D("eff_d0sig", "", suffix)  ->Fill(d0sig, weight);

  h->h1D("trig1", "", suffix)  ->Fill(trig1);
  h->h1D("trig2", "", suffix)  ->Fill(trig2);
  h->h1D("trig3", "", suffix)  ->Fill(trig3);
  h->h1D("trig4", "", suffix)  ->Fill(trig4);
  h->h1D("trig5", "", suffix)  ->Fill(trig5);
  
  if (leptMa_pdgId!=0)	GetRealHistograms(evt, weight, suffix);

}//AnaTtresQCD::runRealRateWQCDCR


void AnaTtresQCD::GetRealHistograms(const Event &evt, double weight, const std::string &suffix){

  HistogramService *h = &m_hSvc;
  
  //lepton
  TLorentzVector lept;   
  if (m_electron) {
     lept  = evt.electron()[0].mom();
  } else{			
     lept  = evt.muon()[0].mom();
  }//m_electron 
  
  h->h2D("eff_MaLep_pt_eta", "", suffix)->Fill(lept.Perp()*1e-3, lept.Eta());  

  //deltaR between lepton and the closest narrow jet
  float closejl_deltaR  = 99;
  float deltaR_tmp	= 99;
  int closejl_idx	= -1;
  float deltaRapidity2  = 99;
  float deltaPhi2	= 99;

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
   
  if (closejl_deltaR<99)  h->h2D("eff_LepPt_DR", "", suffix)	->Fill(lept.Perp()*1e-3, closejl_deltaR, weight);

}//AnaTtresQCD::GetRealHistograms 


//**************************
//******* Fake Rates *******
//**************************


void AnaTtresQCD::runFakeRateQCDCR(const Event &evt, double weight, const std::string &suffix){
    
  if (m_electron && (evt.electron().size() != 1 || evt.muon().size() != 0))
    return;

  if (!m_electron && (evt.electron().size() != 0 || evt.muon().size() != 1))
    return;

  if (m_boosted)
    if (!(evt.passes("be4jets") || evt.passes("bmu2jets")))
      return;

  if (!m_boosted)
    if (!(evt.passes("rejets") || evt.passes("rmu2jets")))
      return;
  
  if (!m_boosted)	if(evt.jet().size()<4)	return;
  
  bool trig1(0); 
  bool trig2(0); 
  bool trig3(0);
  bool trig4(0);
  bool trig5(0);
    
  bool isTight;

  if (m_electron) {	
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
	isTight = evt.muon()[0].isTight();
	
	//Muon triggers
	trig1 = evt.muon()[0].HLT_mu20_L1MU15(); //prescaled
	trig2 = evt.muon()[0].HLT_mu50();
	trig3 = evt.muon()[0].HLT_mu20_iloose_L1MU15();
	
	bool trig_prescaled   = trig1;
	bool trig_unprescaled = trig2 || trig3;
	
	if (!isTight) {
	 if (evt.channelNumber()!=0) if (trig_prescaled && !trig_unprescaled)		weight *= 1.0/10.;
	}
	else{
	 if (trig_prescaled && !trig_unprescaled)		return;	 
	}	
	
  }//m_electron
  HistogramService *h = &m_hSvc;
   
  h->h1D("fake_trig1", "", suffix)  ->Fill(trig1);
  h->h1D("fake_trig2", "", suffix)  ->Fill(trig2);
  h->h1D("fake_trig3", "", suffix)  ->Fill(trig3);
  h->h1D("fake_trig4", "", suffix)  ->Fill(trig4);
  h->h1D("fake_trig5", "", suffix)  ->Fill(trig5);
  
  GetFakeHistograms(evt, weight, suffix);
  
}

void AnaTtresQCD::runFakeRateWQCDCR(const Event &evt, double weight, const std::string &suffix){
    
  if (m_electron && (evt.electron().size() != 1 || evt.muon().size() != 0))
    return;

  if (!m_electron && (evt.electron().size() != 0 || evt.muon().size() != 1))
    return;

  if (m_boosted)
    if (!(evt.passes("be4jets") || evt.passes("bmujets")))
      return;

  if (!m_boosted)
    if (!(evt.passes("rejets") || evt.passes("rmujets")))
      return;
  
  if (!m_boosted)	if(evt.jet().size()<2)	return;
      
  bool trig1(0); 
  bool trig2(0); 
  bool trig3(0);
  bool trig4(0);
  bool trig5(0);
    
  bool isTight;
  TLorentzVector lept; 
  float sd0(99);

  if (m_electron) {	
	isTight = evt.electron()[0].isTightPP();
	lept  = evt.electron()[0].mom();
	sd0    = evt.electron()[0].sd0();

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
	isTight = evt.muon()[0].isTight();
	lept  = evt.muon()[0].mom();
        sd0    = evt.muon()[0].sd0();
	
	//Muon triggers
	trig1 = evt.muon()[0].HLT_mu20_L1MU15(); //prescaled
	trig2 = evt.muon()[0].HLT_mu50();
	trig3 = evt.muon()[0].HLT_mu20_iloose_L1MU15();
	
	bool trig_prescaled   = trig1;
	bool trig_unprescaled = trig2 || trig3;
	
	if (!isTight) {
	 if (evt.channelNumber()!=0) if (trig_prescaled && !trig_unprescaled)		weight *= 1.0/10.;
	}
	else{
	 if (trig_prescaled && !trig_unprescaled)		return;	 
	}	
		
  }//m_electron
  HistogramService *h = &m_hSvc;

  float triangularCut = 60; //(GeV)
  float metCut = 20; //(GeV)
  
  float mWt = sqrt(2. * lept.Perp() * evt.met().Perp() * (1. - cos(evt.met().DeltaPhi(lept)) ))*1e-3; 
  float MET = evt.met().Perp()*1e-3;
  
  if(mWt+MET<triangularCut)	return;
  if(MET<metCut)		return;
  
  int nTrkBtagged = 0; 
  for (size_t bidx = 0; bidx < evt.tjet().size(); ++bidx){
       if (evt.tjet()[bidx].btag_mv2c20_70_trk() && evt.tjet()[bidx].pass_trk())	     
          nTrkBtagged += 1;
  
  }//for 
  
  //if (nTrkBtagged<1)	return;

  //if(!m_electron)	if(fabs(sd0)<5)		return;
    
  h->h1D("fake_trig1", "", suffix)  ->Fill(trig1);
  h->h1D("fake_trig2", "", suffix)  ->Fill(trig2);
  h->h1D("fake_trig3", "", suffix)  ->Fill(trig3);
  h->h1D("fake_trig4", "", suffix)  ->Fill(trig4);
  h->h1D("fake_trig5", "", suffix)  ->Fill(trig5);
  
  GetFakeHistograms(evt, weight, suffix);
} 



void AnaTtresQCD::GetFakeHistograms(const Event &evt, double weight, const std::string &suffix){
  // check channel

  HistogramService *h = &m_hSvc;
  
  h->h1D("eventN", "", suffix)->Fill(evt.eventNumber());
  h->h1D("runN", "", suffix)->Fill(evt.runNumber());

  TLorentzVector lept; 
  float z0(0); 
  float d0sig(0);
  
   //lepton
  if (m_electron) {
     lept  = evt.electron()[0].mom();
     z0    = evt.electron()[0].z0();
     d0sig = evt.electron()[0].sd0();	  
  } else{			
     lept  = evt.muon()[0].mom();
     z0    = evt.muon()[0].z0();
     d0sig = evt.muon()[0].sd0();
  }//m_electron 
    
  float theta = 2*atan(exp(-lept.Eta()));
  h->h1D("fake_z0sin", "",   suffix)->Fill(z0*sin(theta), weight);
  h->h1D("fake_d0sig", "",   suffix)->Fill(d0sig  	, weight);
  
  // MET
  h->h1D("fake_MET", 	    "", suffix)->Fill(evt.met().Perp()*1e-3, weight);
  h->h1D("fake_MET_effBins","", suffix)->Fill(evt.met().Perp()*1e-3, weight);
  h->h1D("fake_MET_phi",    "", suffix)->Fill(evt.met().Phi()	, weight);
  
  // Transverse W mass 
  float mWt = sqrt(2. * lept.Perp() * evt.met().Perp() * (1. - cos(evt.met().DeltaPhi(lept)) )); 
  h->h1D("fake_mwt", 	    "",     suffix)->Fill(mWt*1e-3, weight);
  h->h1D("fake_mwt_effBins","",     suffix)->Fill(mWt*1e-3, weight);
  
  h->h1D("fake_mwt_met", 	 "",     suffix)->Fill( (mWt+evt.met().Perp())*1e-3, weight);
  h->h1D("fake_mwt_met_effBins", "",     suffix)->Fill( (mWt+evt.met().Perp())*1e-3, weight);
  
  // Cos(metPhi, lepPhi)
  h->h1D("fake_cos_metPhi_lepPhi", 	    "", suffix)->Fill(cos(evt.met().DeltaPhi(lept)), weight);
  h->h1D("fake_cos_metPhi_lepPhi_effBins",  "", suffix)->Fill(cos(evt.met().DeltaPhi(lept)), weight);
  
  // n Jets
  h->h1D("fake_nJets", "", suffix)->Fill(evt.jet().size(), weight);
  
  //nB-tagged jets 
  int nTrkBtagged = 0; 
  for (size_t bidx = 0; bidx < evt.tjet().size(); ++bidx){
       if (evt.tjet()[bidx].btag_mv2c20_70_trk() && evt.tjet()[bidx].pass_trk())	     
          nTrkBtagged += 1;
  
  }//for     
  h->h1D("fake_nTrkBtagJets", "", suffix)->Fill(nTrkBtagged, weight); 
       
  //min DR(lept, jet) 
  float deltaRapidity2   = 99;
  float deltaPhi2	 = 99;
  float closejl_deltaR   = 99;
  float deltaR_tmp	 = 99;
  int   closejl_idx	 = -1;
  float closejl_pT	 = -1;
  
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
     
       
     if (cos(lept.Phi() - evt.met().Phi()) < -0.98){
	h->h1D("fake_lowCos_cos_metPhi_lepPhi", "", suffix)->Fill(cos(lept.Phi() - evt.met().Phi()), weight);
	h->h1D("fake_lowCos_lepPt",	  	"", suffix)->Fill(lept.Pt()*1e-3 , weight); 
	h->h1D("fake_lowCos_MET", 		"", suffix)->Fill(evt.met().Perp()*1e-3, weight);
	h->h1D("fake_lowCos_d0sig", 		"", suffix)->Fill(d0sig, weight);
	h->h1D("fake_lowCos_mwt", 		"", suffix)->Fill(mWt*1e-3, weight);
	h->h1D("fake_lowCos_minDeltaR",	  	"", suffix)->Fill(closejl_deltaR , weight);
	h->h2D("fake_lowCos_lepEtaVSPhi",       "", suffix)->Fill(lept.Eta(), lept.Phi(), weight);	
     }else{
	h->h1D("fake_highCos_cos_metPhi_lepPhi", "", suffix)->Fill(cos(lept.Phi() - evt.met().Phi()), weight);
	h->h1D("fake_highCos_lepPt",	  	"", suffix)->Fill(lept.Pt()*1e-3 , weight); 
	h->h1D("fake_highCos_MET", 		"", suffix)->Fill(evt.met().Perp()*1e-3, weight);
	h->h1D("fake_highCos_d0sig", 		"", suffix)->Fill(d0sig, weight);
	h->h1D("fake_highCos_mwt", 		"", suffix)->Fill(mWt*1e-3, weight);
	h->h1D("fake_highCos_minDeltaR",	"", suffix)->Fill(closejl_deltaR , weight);
        h->h2D("fake_highCos_lepEtaVSPhi",       "", suffix)->Fill(lept.Eta(), lept.Phi(), weight);
     }
     
     h->h1D("fake_lepPt_effBins", "",suffix)->Fill(lept.Pt()*1e-3 , weight);
     h->h1D("fake_lepPt",	  "", suffix)->Fill(lept.Pt()*1e-3 , weight); 
     h->h1D("fake_lepEta",  	  "", suffix)->Fill(lept.Eta()     , weight);
     h->h1D("fake_lepPhi",  	  "", suffix)->Fill(lept.Phi()     , weight);

     h->h1D("fake_minDeltaR_effBins", 	"", suffix)->Fill(closejl_deltaR , weight); 
     h->h1D("fake_minDeltaR",	  	"", suffix)->Fill(closejl_deltaR , weight);
     h->h1D("fake_closJetPt_effBins", 	"", suffix)->Fill(closejl_pT*1e-3, weight);
     h->h1D("fake_closJetPt",	  	"", suffix)->Fill(closejl_pT*1e-3, weight);
     
     h->h1D("fake_closJetJVT", 		"", suffix)->Fill(evt.jet()[closejl_idx].jvt(), weight);
     
     h->h2D("fake_lepPt_lepEta",     "", suffix)->Fill(lept.Pt()*1e-3 ,fabs(lept.Eta()), weight);
     h->h2D("fake_lepPt_closJetPt",  "", suffix)->Fill(lept.Pt()*1e-3 ,closejl_pT*1e-3  , weight);
     h->h2D("fake_lepPt_minDeltaR",  "", suffix)->Fill(lept.Pt()*1e-3 ,closejl_deltaR, weight);
     h->h2D("fake_closJetPt_cosDPhi","", suffix)->Fill(closejl_pT*1e-3 ,cos(lept.Phi() - evt.met().Phi())  , weight);
     h->h2D("fake_minDeltaR_cosDPhi","", suffix)->Fill(closejl_deltaR  ,cos(lept.Phi() - evt.met().Phi())  , weight);
     h->h2D("fake_lepPt_met",        "", suffix)->Fill(lept.Pt()*1e-3 , evt.met().Perp()*1e-3, weight);
     
     h->h2D("fake_lepPt_cosDPhi",    "", suffix)->Fill(lept.Pt()*1e-3 ,cos(lept.Phi() - evt.met().Phi())  , weight);    	

     // For electron channel
     if(fabs(lept.Eta())<1.6)
  	h->h2D("fake_lepPt_cosDPhi_lowEta",   "", suffix)->Fill(lept.Pt()*1e-3 ,cos(lept.Phi() - evt.met().Phi()) , weight);
     else
  	h->h2D("fake_lepPt_cosDPhi_highEta",  "", suffix)->Fill(lept.Pt()*1e-3 ,cos(lept.Phi() - evt.met().Phi()) , weight);
  
  	
     // For muon channel
     if(closejl_deltaR<0.4)
        h->h2D("fake_lepPt_met_lowDR",        "", suffix)->Fill(lept.Pt()*1e-3 , evt.met().Perp()*1e-3, weight);
     else
        h->h2D("fake_lepPt_met_highDR",        "", suffix)->Fill(lept.Pt()*1e-3 , evt.met().Perp()*1e-3, weight);

     if(cos(lept.Phi() - evt.met().Phi())<0.6)
        h->h2D("fake_lepPt_minDeltaR_lowCos",  "", suffix)->Fill(lept.Pt()*1e-3 ,closejl_deltaR, weight);
     else
        h->h2D("fake_lepPt_minDeltaR_highCos", "", suffix)->Fill(lept.Pt()*1e-3 ,closejl_deltaR, weight);
	
     if(lept.Pt()*1e-3 > 50)	
        h->h2D("fake_minDeltaR_met_highLepPt", "", suffix)->Fill(closejl_deltaR, evt.met().Perp()*1e-3, weight);
     else
     	h->h2D("fake_minDeltaR_met_lowLepPt",  "", suffix)->Fill(closejl_deltaR, evt.met().Perp()*1e-3, weight);

	
  }//if(closejl_deltaR<99)	
		 
}//AnaTtresQCD::GetFakeHistograms






