/**
 * @brief Code to parse input parameters without BOOST to avoid the unnecessary overload of libraries needed.
 * @author Danilo Enoque Ferreira de Lima <dferreir@cern.ch> 
 */
#include "TopNtupleAnalysis/MMUtils.h"

#include <getopt.h>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>

#include <vector>
#include <algorithm>
#include "TFile.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TH1D.h"
#include "TH2D.h"
#include "TLorentzVector.h"


MMUtils::MMUtils(const std::string &eff_filename, const std::string &fake_filename) {

  if (eff_filename!="" && fake_filename!=""){
    
    std::cout << "MMUtils:: Going to use " << eff_filename << " and " << fake_filename << std::endl;
    
    TFile m_eff_rootfile(eff_filename.c_str(), "r");
    
    eff_map_resolved_e = 	(TH2F*) m_eff_rootfile.Get("eff_pTdr_resolved_e");
    if(eff_map_resolved_e)	eff_map_resolved_e->SetDirectory(0);
    
    eff_map_resolved_mu = 	(TH2F*) m_eff_rootfile.Get("eff_pTdr_resolved_mu");
    if(eff_map_resolved_mu)	eff_map_resolved_mu->SetDirectory(0);
          
    eff_map_boosted_e = 	(TH2F*) m_eff_rootfile.Get("eff_pTdr_boosted_e");
    if(eff_map_boosted_e)	eff_map_boosted_e->SetDirectory(0);
    
    eff_map_boosted_mu = 	(TH2F*) m_eff_rootfile.Get("eff_pTdr_boosted_mu");    
    if(eff_map_boosted_mu)	eff_map_boosted_mu->SetDirectory(0);
      
    TFile m_fake_rootfile(fake_filename.c_str(), "r");

    fake_map_resolved_e_lEta =    (TH2F*)m_fake_rootfile.Get("2Dfake_lepPt_cosDPhi_lowEta_resolved_e");
    if(fake_map_resolved_e_lEta)  fake_map_resolved_e_lEta->SetDirectory(0);
    
    fake_map_resolved_e_hEta =    (TH2F*)m_fake_rootfile.Get("2Dfake_lepPt_cosDPhi_highEta_resolved_e");
    if(fake_map_resolved_e_hEta)  fake_map_resolved_e_hEta->SetDirectory(0);
    
    fake_map_resolved_mu_lDR =    (TH2F*)m_fake_rootfile.Get("2Dfake_mwt_met_map_lowDR_resolved_mu");
    if(fake_map_resolved_mu_lDR)  fake_map_resolved_mu_lDR->SetDirectory(0);
    fake_map_resolved_mu_mDR =    (TH2F*)m_fake_rootfile.Get("2Dfake_mwt_met_map_medDR_resolved_mu");
    if(fake_map_resolved_mu_mDR)  fake_map_resolved_mu_mDR->SetDirectory(0);
    fake_map_resolved_mu_hDR =    (TH2F*)m_fake_rootfile.Get("2Dfake_mwt_met_map_highDR_resolved_mu");
    if(fake_map_resolved_mu_hDR)  fake_map_resolved_mu_hDR->SetDirectory(0);

    fake_pt_boosted_e = 	(TH1F*)m_fake_rootfile.Get("fakeRate_pt_boosted_e");
    if(fake_pt_boosted_e)	fake_pt_boosted_e->SetDirectory(0);
    
    fake_dr_boosted_mu  = 	(TH1F*)m_fake_rootfile.Get("fakeRate_dr_boosted_mu");
    if(fake_dr_boosted_mu)	fake_dr_boosted_mu->SetDirectory(0); 

  }
  
}
  
MMUtils::~MMUtils(){
  
  delete eff_map_resolved_e  ;
  delete eff_map_resolved_mu  ;
  delete eff_map_boosted_e ;
  delete eff_map_boosted_mu ;
  
  delete fake_map_resolved_e_lEta;
  delete fake_map_resolved_e_hEta;
  delete fake_map_resolved_mu_lDR;
  delete fake_map_resolved_mu_mDR;
  delete fake_map_resolved_mu_hDR;
  delete fake_pt_boosted_e;  
  delete fake_dr_boosted_mu;

} 

void MMUtils::get2Drates(float &rate, float &rate_err, TH2F* rate_map, float x, float y){
   
   int binx(0);
   int biny(0);
      
   if(x > rate_map->GetXaxis()->GetXmax()){
          binx = rate_map->GetXaxis()->FindBin(0.99*rate_map->GetXaxis()->GetXmax());	  
   }else{
          binx = rate_map->GetXaxis()->FindBin(x);
   }
   
   if(y >= rate_map->GetYaxis()->GetXmax()){	
	  biny = rate_map->GetYaxis()->FindBin(0.99*rate_map->GetYaxis()->GetXmax());
   }else{
	  biny = rate_map->GetYaxis()->FindBin(y);
   }
            
   int bin      = rate_map->GetBin(binx, biny, 0);   
   rate    	= rate_map->GetBinContent(bin);
   rate_err 	= rate_map->GetBinError(bin); 
   
   return;
}

void MMUtils::get1Drates(float &rate, float &rate_err, TH1F* rate_map, float x){
   
   int binx(0);
   
   if(x >= rate_map->GetXaxis()->GetXmax()){
          binx = rate_map->GetXaxis()->FindBin(0.99*rate_map->GetXaxis()->GetXmax());	  
   }else{
          binx = rate_map->GetXaxis()->FindBin(x);
   }
      
   rate    	= rate_map->GetBinContent(binx);
   rate_err 	= rate_map->GetBinError(binx); 
   return;
}

void MMUtils::getRatesBoostedMu(float &realRate, float &realRate_err, float &fakeRate, float &fakeRate_err, float lepPt, float closejl_DR){

    get2Drates(realRate, realRate_err, eff_map_boosted_mu, lepPt, closejl_DR);
    get1Drates(fakeRate, fakeRate_err, fake_dr_boosted_mu, closejl_DR);
    return;
}

void MMUtils::getRatesBoostedEl(float &realRate, float &realRate_err, float &fakeRate, float &fakeRate_err, float lepPt, float closejl_DR){

    get2Drates(realRate, realRate_err, eff_map_boosted_e, lepPt, closejl_DR);

    if(lepPt > 120)	get1Drates(fakeRate, fakeRate_err, fake_pt_boosted_e, 119);
    else		get1Drates(fakeRate, fakeRate_err, fake_pt_boosted_e, lepPt);

    return;
}

void MMUtils::getRatesResolvedMu(float &realRate, float &realRate_err, float &fakeRate, float &fakeRate_err, float lepPt, float closejl_DR, float closejl_pT, float cosDPhi, float met, float mwt, float DPhi){
   
    float met_min(0);
    float met_limit(95);
    
    float mwt_min(0);
    float mwt_limit(95);
    
    get2Drates(realRate, realRate_err, eff_map_resolved_mu, lepPt, closejl_DR); 

    if(closejl_DR > 0.6){

      if(met<50)	mwt_limit = 95;
      else 		mwt_limit = 195;
      
      mwt_min = std::min(mwt, mwt_limit);
      met_min = std::min(met, met_limit);
      
      get2Drates(fakeRate, fakeRate_err, fake_map_resolved_mu_hDR, met_min, mwt_min);
      
      if (fakeRate<0) fakeRate=0;
      
    }else if(closejl_DR > 0.4){

      mwt_limit = 95;
      
      mwt_min = std::min(mwt, mwt_limit);
      met_min = std::min(met, met_limit);
      
      get2Drates(fakeRate, fakeRate_err, fake_map_resolved_mu_mDR, met_min, mwt_min);
      
      if (fakeRate<0) fakeRate=0;
            
    }else{
    
      if(met<40)	mwt_limit = 95;
      else 		mwt_limit = 195;
    
      mwt_min = std::min(mwt, mwt_limit);
      met_min = std::min(met, met_limit);
      
      get2Drates(fakeRate, fakeRate_err, fake_map_resolved_mu_lDR, met_min, mwt_min);
 
      if (fakeRate<0) fakeRate=0;
            
    }//if

    return;
        
}

void MMUtils::getRatesResolvedEl(float &realRate, float &realRate_err, float &fakeRate, float &fakeRate_err, float lepPt, float closejl_DR, float absEta, float cosDPhi){

    get2Drates(realRate, realRate_err, eff_map_resolved_e, lepPt, closejl_DR);
    
    if(absEta > 1.8)	get2Drates(fakeRate, fakeRate_err, fake_map_resolved_e_hEta, lepPt, cosDPhi);
    else		get2Drates(fakeRate, fakeRate_err, fake_map_resolved_e_lEta, lepPt, cosDPhi);

    return;
}

float MMUtils::getMMweights(const Event &evt, const int runMM_StatErr, const bool isElectron, const bool isBoosted) {
   
   bool isTight;
   float d0sig;

   if ( isElectron && evt.electron().size()<1 ) return 0;
   if (!isElectron && evt.muon().size()<1 )     return 0;
   
   TLorentzVector lepP4; 
    
   if (isElectron)    {
       lepP4 = evt.electron()[0].mom();
       isTight = evt.electron()[0].isTightPP();
       
   }else {
       lepP4 = evt.muon()[0].mom();
       isTight = evt.muon()[0].isTight();
       d0sig = evt.muon()[0].sd0();
       
       bool trig_unprescaled = evt.muon()[0].HLT_mu20_iloose_L1MU15() || evt.muon()[0].HLT_mu50();       
       if( !trig_unprescaled && isTight)	return 0;
   }
   
   float lepPt  = lepP4.Perp()*1e-3; 
   float absEta = fabs(lepP4.Eta());
   
   //min DR(lept, jet)
   float closejl_pT(0); 
   float closejl_DR(99);
   
   float deltaRapidity2 = 99;
   float deltaPhi2	= 99;
   float deltaR_tmp     = 99;

   size_t jet_idx = 0;
   for (; jet_idx < evt.jet().size(); ++jet_idx){  

       deltaRapidity2 = pow(evt.jet()[jet_idx].mom().Rapidity() - lepP4.Rapidity(), 2);    
       deltaPhi2 = pow(evt.jet()[jet_idx].mom().DeltaPhi(lepP4), 2);	     
       deltaR_tmp = sqrt(deltaPhi2 + deltaRapidity2);

       if (deltaR_tmp < closejl_DR){
   	  closejl_DR = deltaR_tmp;
          closejl_pT = evt.jet()[jet_idx].mom().Perp()*1e-3;
       }  
   }//for 
   
   //Cos(deltaPhi(met,lep)) 
   float deltaPhi = evt.met().DeltaPhi(lepP4);   
   float cosDPhi = std::cos(deltaPhi);   
   float MET = evt.met().Pt()*1e-3;
   float mWt = sqrt(2. * lepP4.Perp() * evt.met().Perp() * (1. - cos(evt.met().DeltaPhi(lepP4)) ))*1e-3; 
        
   //Getting rates
   float fakeRate(0);
   float fakeRate_err(0);
   float realRate(0);
   float realRate_err(0);  
   
   if (isBoosted){
   	if (isElectron)	getRatesBoostedEl(realRate, realRate_err, fakeRate, fakeRate_err, lepPt, closejl_DR);
   	else		getRatesBoostedMu(realRate, realRate_err, fakeRate, fakeRate_err, lepPt, closejl_DR);
   }
   else{
   	if (isElectron)	getRatesResolvedEl(realRate, realRate_err, fakeRate, fakeRate_err, lepPt, closejl_DR, absEta, cosDPhi);
   	else		getRatesResolvedMu(realRate, realRate_err, fakeRate, fakeRate_err, lepPt, closejl_DR, closejl_pT, cosDPhi, MET, mWt, deltaPhi);
		
   }//isBoosted	
     
   //Implementing weights
   float Weight = 1;

   //Maximazing the stat error for runMM_StatErr==1 || runMM_StatErr==2
   if (runMM_StatErr==1){
     realRate += realRate_err;
     fakeRate -= fakeRate_err;
   } else if (runMM_StatErr==2){
     realRate -= realRate_err;
     fakeRate += fakeRate_err;
   }
   	
   if (isTight){
     if(realRate>0 && fakeRate>0)     Weight = fakeRate*(realRate - 1)/(realRate - fakeRate);      
     else{
     	     //if(realRate==0)std::cerr << "Error: realRate equal to " << realRate << " (tight) " << mWt << std::endl;	   
     	     //if(fakeRate==0)std::cerr << "Error: fakeRate equal to " << fakeRate << " (tight) " << mWt << " " << cosDPhi << std::endl;	    
	     Weight = 0;
     }
   }
   else {	
     if(realRate>0 && fakeRate>0)  Weight = fakeRate*realRate/(realRate - fakeRate);
     else{
	     //if(realRate==0)std::cerr << "Error: realRate equal to " << realRate << "  (anti-tight) " << mWt << std::endl;	   
     	     //if(fakeRate==0)std::cerr << "Error: fakeRate equal to " << fakeRate << "  (anti-tight) " << mWt << " " << cosDPhi << std::endl;
     	     Weight = 0;
     }       
   
   }//isTight
   
   //if(!isTight)	std::cout << "is tight? " << isTight << " - QCD weight" << Weight << std::endl;
   
   return Weight;  

}//getMMweights

