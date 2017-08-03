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


MMUtils::MMUtils(const int isBtagged,const int etaCorr, const int DRCorr, const std::string &eff_filename, const std::string &fake_filename) {
    m_isBtagged = isBtagged;
    m_etaCorr = etaCorr;
    m_DRCorr  = DRCorr;
    std::cout << "MMUtils:: Going to use  " << std::endl;
    std::cout << "  for 2015+2016:" << eff_filename << " and " << fake_filename << std::endl;


    // --------------------- 2016 files ------------------------------------------- //
    TFile m_eff_rootfile2016(eff_filename.c_str(), "r");
    
    //eff_map_resolved_e_2016 = 	(TH2F*) m_eff_rootfile2016.Get("eff_pTdr_resolved_e");
    //if(eff_map_resolved_e_2016)	eff_map_resolved_e_2016->SetDirectory(0);

    eff_map_resolved_e_2016 = 	(TH2F*) m_eff_rootfile2016.Get("eff_lepPt_topoetcone_resolved_e");
    if(eff_map_resolved_e_2016)	eff_map_resolved_e_2016->SetDirectory(0);
    
    eff_map_resolved_mu_2016 = 	(TH2F*) m_eff_rootfile2016.Get("eff_LepPt_DR_sbin_resolved_mu");
    if(eff_map_resolved_mu_2016)	eff_map_resolved_mu_2016->SetDirectory(0);

    eff_map_resolved_mu_2016_lDR =  (TH2F*) m_eff_rootfile2016.Get("eff_lepPt_topoetcone_lowDR_resolved_mu");
    if(eff_map_resolved_mu_2016_lDR)        eff_map_resolved_mu_2016_lDR->SetDirectory(0);

    eff_map_resolved_mu_2016_mDR =  (TH2F*) m_eff_rootfile2016.Get("eff_lepPt_topoetcone_medDR_resolved_mu");
    if(eff_map_resolved_mu_2016_mDR)        eff_map_resolved_mu_2016_mDR->SetDirectory(0);
          
    eff_map_resolved_mu_2016_hDR =  (TH2F*) m_eff_rootfile2016.Get("eff_lepPt_topoetcone_highDR_resolved_mu");
    if(eff_map_resolved_mu_2016_hDR)        eff_map_resolved_mu_2016_hDR->SetDirectory(0);

    eff_map_boosted_e_2016 = 	(TH2F*) m_eff_rootfile2016.Get("eff_pTdr_boosted_e");
    if(eff_map_boosted_e_2016)	eff_map_boosted_e_2016->SetDirectory(0);
    
    eff_map_boosted_mu_2016 = 	(TH2F*) m_eff_rootfile2016.Get("eff_pTdr_boosted_mu");    
    if(eff_map_boosted_mu_2016)	eff_map_boosted_mu_2016->SetDirectory(0);
      
    TFile m_fake_rootfile2016(fake_filename.c_str(), "r");

    fake_map_resolved_e_2016 =        (TH2F*)m_fake_rootfile2016.Get("2Dfake_lepPt_topoetcone_resolved_e");
    if(fake_map_resolved_e_2016)      fake_map_resolved_e_2016->SetDirectory(0);

    fake_map_resolved_mu_2016_lDR =    (TH2F*)m_fake_rootfile2016.Get("2Dfake_lepPt_topoetcone_lowDR_resolved_mu");
    if(fake_map_resolved_mu_2016_lDR)  fake_map_resolved_mu_2016_lDR->SetDirectory(0);
    fake_map_resolved_mu_2016_mDR =    (TH2F*)m_fake_rootfile2016.Get("2Dfake_lepPt_topoetcone_resolved_mu");
    if(fake_map_resolved_mu_2016_mDR)  fake_map_resolved_mu_2016_mDR->SetDirectory(0);
    fake_map_resolved_mu_2016_hDR =    (TH2F*)m_fake_rootfile2016.Get("2Dfake_lepPt_topoetcone_highDR_resolved_mu");
    if(fake_map_resolved_mu_2016_hDR)  fake_map_resolved_mu_2016_hDR->SetDirectory(0);
    
    fake_pt_boosted_e_2016 = 	(TH1F*)m_fake_rootfile2016.Get("fakeRate_pt_boosted_e");
    if(fake_pt_boosted_e_2016)	fake_pt_boosted_e_2016->SetDirectory(0);
    
    fake_dr_boosted_mu_2016  = 	(TH1F*)m_fake_rootfile2016.Get("fakeRate_dr_boosted_mu");
    if(fake_dr_boosted_mu_2016)	fake_dr_boosted_mu_2016->SetDirectory(0); 
    
    
    
    
    // Taking lepEta histograms with different binning. These histograms will be used to compute a ratio that will be applied on the weights
    //************************ 2016 files ****************************************************************************************************************
    fake_lepEta_1bin_e_2016     = (TH1F*) m_fake_rootfile2016.Get("fakeRate_lepEta_1bin_resolved_e");
    if(fake_lepEta_1bin_e_2016)  fake_lepEta_1bin_e_2016->SetDirectory(0);
    fake_lepEta_20bins_e_2016    = (TH1F*) m_fake_rootfile2016.Get("fakeRate_lepEta_20bins_resolved_e");
    if(fake_lepEta_20bins_e_2016) fake_lepEta_20bins_e_2016->SetDirectory(0);
    fake_lepEta_e_2016    = (TH1F*) m_fake_rootfile2016.Get("fakeRate_lepEta_resolved_e");
    if(fake_lepEta_e_2016) fake_lepEta_e_2016->SetDirectory(0);
    
    eff_lepEta_1bin_e_2016     = (TH1F*) m_eff_rootfile2016.Get("realRate_lepEta_1bin_resolved_e");
    if(eff_lepEta_1bin_e_2016)  eff_lepEta_1bin_e_2016->SetDirectory(0);
    eff_lepEta_20bins_e_2016     = (TH1F*) m_eff_rootfile2016.Get("realRate_lepEta_20bins_resolved_e");
    if(eff_lepEta_20bins_e_2016)  eff_lepEta_20bins_e_2016->SetDirectory(0);
    
    
    fake_lepEta_1bin_mu_2016     = (TH1F*) m_fake_rootfile2016.Get("fakeRate_lepEta_1bin_resolved_mu");
    if(fake_lepEta_1bin_mu_2016)  fake_lepEta_1bin_mu_2016->SetDirectory(0);
    fake_lepEta_20bins_mu_2016    = (TH1F*) m_fake_rootfile2016.Get("fakeRate_lepEta_20bins_resolved_mu");
    if(fake_lepEta_20bins_mu_2016) fake_lepEta_20bins_mu_2016->SetDirectory(0);
    fake_lepEta_mu_2016    = (TH1F*) m_fake_rootfile2016.Get("fakeRate_lepEta_resolved_mu");
    if(fake_lepEta_mu_2016) fake_lepEta_mu_2016->SetDirectory(0);
    
    eff_lepEta_1bin_mu_2016     = (TH1F*) m_eff_rootfile2016.Get("realRate_lepEta_1bin_resolved_mu");
    if(eff_lepEta_1bin_mu_2016)  eff_lepEta_1bin_mu_2016->SetDirectory(0);
    eff_lepEta_20bins_mu_2016     = (TH1F*) m_eff_rootfile2016.Get("realRate_lepEta_20bins_resolved_mu");
    if(eff_lepEta_20bins_mu_2016)  eff_lepEta_20bins_mu_2016->SetDirectory(0);
    
    
    // Taking lepPt highDR and lowDR histograms. These histograms will be used to compute a ratio that will be applied on the weights
    //************************ 2016 files ****************************************************************************************************************
    //TH1F
    fake_lepPt_highDR_e_2016 = (TH1F*)m_fake_rootfile2016.Get("fakeRate_lepPt_highDR_resolved_e");
    if(fake_lepPt_highDR_e_2016) fake_lepPt_highDR_e_2016->SetDirectory(0);
    fake_lepPt_lowDR_e_2016 = (TH1F*)m_fake_rootfile2016.Get("fakeRate_lepPt_lowDR_resolved_e");
    if(fake_lepPt_lowDR_e_2016) fake_lepPt_lowDR_e_2016->SetDirectory(0);
    
    fake_lepPt_highDR_mu_2016 = (TH1F*)m_fake_rootfile2016.Get("fakeRate_lepPt_highDR_resolved_mu");
    if(fake_lepPt_highDR_mu_2016) fake_lepPt_highDR_mu_2016->SetDirectory(0);
    fake_lepPt_lowDR_mu_2016 = (TH1F*)m_fake_rootfile2016.Get("fakeRate_lepPt_lowDR_resolved_mu");
    if(fake_lepPt_lowDR_mu_2016) fake_lepPt_lowDR_mu_2016->SetDirectory(0);
    
    
    eff_lepPt_highDR_e_2016 = (TH1F*)m_eff_rootfile2016.Get("realRate_lepPt_highDR_resolved_e");
    if(eff_lepPt_highDR_e_2016) eff_lepPt_highDR_e_2016->SetDirectory(0);
    eff_lepPt_lowDR_e_2016 = (TH1F*)m_eff_rootfile2016.Get("realRate_lepPt_lowDR_resolved_e");
    if(eff_lepPt_lowDR_e_2016) eff_lepPt_lowDR_e_2016->SetDirectory(0);
    
    eff_lepPt_highDR_mu_2016 = (TH1F*)m_eff_rootfile2016.Get("realRate_lepPt_highDR_resolved_mu");
    if(eff_lepPt_highDR_mu_2016) eff_lepPt_highDR_mu_2016->SetDirectory(0);
    eff_lepPt_lowDR_mu_2016 = (TH1F*)m_eff_rootfile2016.Get("realRate_lepPt_lowDR_resolved_mu");
    if(eff_lepPt_lowDR_mu_2016) eff_lepPt_lowDR_mu_2016->SetDirectory(0);
    
    // TH2F
    fake_map_lepPt_minDeltaR_e_2016 = (TH2F*)m_fake_rootfile2016.Get("2Dfake_lepPt_minDeltaR_resolved_e");
    if(fake_map_lepPt_minDeltaR_e_2016) fake_map_lepPt_minDeltaR_e_2016->SetDirectory(0);
    fake_map_lepPt_minDeltaR_mu_2016 = (TH2F*)m_fake_rootfile2016.Get("2Dfake_lepPt_minDeltaR_resolved_mu");
    if(fake_map_lepPt_minDeltaR_mu_2016) fake_map_lepPt_minDeltaR_mu_2016->SetDirectory(0);
    
    eff_map_lepPt_DR_resolved_e_2016    =   (TH2F*) m_eff_rootfile2016.Get("eff_LepPt_DR_resolved_e");
    if(eff_map_lepPt_DR_resolved_e_2016)    eff_map_lepPt_DR_resolved_e_2016->SetDirectory(0);
    
    eff_map_lepPt_DR_resolved_mu_2016    =   (TH2F*) m_eff_rootfile2016.Get("eff_LepPt_DR_resolved_mu");
    if(eff_map_lepPt_DR_resolved_mu_2016)    eff_map_lepPt_DR_resolved_mu_2016->SetDirectory(0);
    
    
    
}
  
MMUtils::~MMUtils(){ 

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


float MMUtils::getEtaCorrectionFactor(TH1F* rate_1bin, TH1F* rate_xbins, float absEta)
{
   // Get rate_1bin bin content
   int bin(0);
   
   if(absEta > rate_1bin->GetXaxis()->GetXmax()) bin = rate_1bin->GetXaxis()->FindBin(0.99*rate_1bin->GetXaxis()->GetXmax());
   else bin = rate_1bin->GetXaxis()->FindBin(absEta);
   float eta_1bin = rate_1bin->GetBinContent(bin);
   
   // Get rate_xbins bins contents
   int binx(0);
   
   if(absEta > rate_xbins->GetXaxis()->GetXmax()) binx = rate_xbins->GetXaxis()->FindBin(0.99*rate_xbins->GetXaxis()->GetXmax());
   else binx = rate_xbins->GetXaxis()->FindBin(absEta);
   float eta_xbins = rate_xbins->GetBinContent(binx);
   
   // Take the ratio
   float eta_corr = eta_xbins / eta_1bin;
   return eta_corr;
}

float MMUtils::getFakeDRCorrectionFactor(bool isElectron, float lepPt, float closejl_DR, const unsigned int runNumber)
{

 	  if(isElectron) return getDRCorrectionFactorTools(fake_lepPt_lowDR_e_2016,  fake_lepPt_highDR_e_2016,  fake_map_lepPt_minDeltaR_e_2016,  lepPt, closejl_DR);
 	  else           return getDRCorrectionFactorTools(fake_lepPt_lowDR_mu_2016,  fake_lepPt_highDR_mu_2016,  fake_map_lepPt_minDeltaR_mu_2016,  lepPt, closejl_DR);

}



float MMUtils::getEffDRCorrectionFactor(bool isElectron, float lepPt, float closejl_DR, const unsigned int runNumber)
{

 	  if(isElectron) return getDRCorrectionFactorTools(eff_lepPt_lowDR_e_2016,  eff_lepPt_highDR_e_2016,  eff_map_lepPt_DR_resolved_e_2016,  lepPt, closejl_DR);
 	  else           return getDRCorrectionFactorTools(eff_lepPt_lowDR_mu_2016,  eff_lepPt_highDR_mu_2016,  eff_map_lepPt_DR_resolved_mu_2016,  lepPt, closejl_DR);
}





float MMUtils::getDRCorrectionFactorTools(TH1F* lepPt_lowDR, TH1F* lepPt_highDR, TH2F* lepPt_minDeltaR, float lepPt, float closejl_DR)
{
   int bin_1D(0);
   float rate_1D(0.);
   if(closejl_DR < 0.4)
   {
      if(lepPt > lepPt_lowDR->GetXaxis()->GetXmax()) bin_1D = lepPt_lowDR->GetXaxis()->FindBin(0.99*lepPt_lowDR->GetXaxis()->GetXmax());
      else bin_1D = lepPt_lowDR->GetXaxis()->FindBin(lepPt);
      rate_1D = lepPt_lowDR->GetBinContent(bin_1D);
   }
   else
   {
     if(lepPt > lepPt_highDR->GetXaxis()->GetXmax()) bin_1D = lepPt_highDR->GetXaxis()->FindBin(0.99*lepPt_highDR->GetXaxis()->GetXmax());
     else bin_1D = lepPt_highDR->GetXaxis()->FindBin(lepPt);
     rate_1D = lepPt_highDR->GetBinContent(bin_1D);
   }
   
   int binx_2D(0);
   int biny_2D(0);
   
   if(lepPt > lepPt_minDeltaR->GetXaxis()->GetXmax()) binx_2D = lepPt_minDeltaR->GetXaxis()->FindBin(0.99*lepPt_minDeltaR->GetXaxis()->GetXmax());	  
   else binx_2D = lepPt_minDeltaR->GetXaxis()->FindBin(lepPt);   
     
   if(closejl_DR >= lepPt_minDeltaR->GetYaxis()->GetXmax()) biny_2D = lepPt_minDeltaR->GetYaxis()->FindBin(0.99*lepPt_minDeltaR->GetYaxis()->GetXmax());
   else biny_2D = lepPt_minDeltaR->GetYaxis()->FindBin(closejl_DR);
   
   int bin       = lepPt_minDeltaR->GetBin(binx_2D , biny_2D , 0);   
   float rate_2D = lepPt_minDeltaR->GetBinContent(bin);
   
   if(rate_1D == 0) std::cout << "Error, In getDRCorrectionFactorTools : rate_1D = 0 -> dividing by 0 !!!" << std::endl;
   float corr = rate_2D / rate_1D;
   return corr;
}


void MMUtils::getRatesResolvedMu(float &realRate, float &realRate_err, float &fakeRate, float &fakeRate_err, float lepPt, float closejl_DR, float closejl_pT, float cosDPhi, float met, float mwt, float DPhi, float topoetcone, const unsigned int runNumber){


    float met_min(0);
    float met_limit(95);
    
    float mwt_min(0);
    float mwt_limit(95);

    float lepPt_min(0.);
    float lepPt_limit(300);

    float topoet_min(-5.);
    float topoet_limit(30);

    lepPt_min = std::min(lepPt, lepPt_limit);
    topoet_min = std::min(topoetcone, topoet_limit);

    if(closejl_DR < 0.4)
    get2Drates(realRate, realRate_err, eff_map_resolved_mu_2016_lDR, lepPt_min, topoet_min);
    else
    get2Drates(realRate, realRate_err, eff_map_resolved_mu_2016_hDR, lepPt_min, topoet_min);
    
  
    if(m_isBtagged==0) {
  
      	if(closejl_DR >= 0.4) {
	      // for  pT>100, let take the average
    	   if(lepPt_min >= 100) get1Drates(fakeRate, fakeRate_err, fake_lepPt_highDR_mu_2016, lepPt_min);
	   else get2Drates(fakeRate, fakeRate_err, fake_map_resolved_mu_2016_hDR, lepPt_min, topoet_min);
      	}
	else{
		get2Drates(fakeRate, fakeRate_err, fake_map_resolved_mu_2016_hDR, lepPt_min, topoet_min);
	}
    }
    else if(m_isBtagged==1) {
      
      if(closejl_DR >= 0.4) {  
	      	if(lepPt_min >= 70 && lepPt_min < 100 && topoet_min >= 10)   topoet_min = 7;
	      	if(lepPt_min >= 100 && topoet_min >= 6)   topoet_min = 5;
		
	  	get2Drates(fakeRate, fakeRate_err, fake_map_resolved_mu_2016_hDR, lepPt_min, topoet_min);
      } 
      else{  
	      // for  pT>100, let take the average
    	   if(lepPt_min >= 100) get1Drates(fakeRate, fakeRate_err, fake_lepPt_lowDR_mu_2016, lepPt_min);
	   else get2Drates(fakeRate, fakeRate_err, fake_map_resolved_mu_2016_lDR, lepPt_min, topoet_min);
      } 
    }
   else if(m_isBtagged==2) {
        // -- checking for inclusive dR only -- //  
        if(topoet_min > 6 && topoet_min < 10 && lepPt_min >=100)
        topoet_min = 5;
    	
	get2Drates(fakeRate, fakeRate_err, fake_map_resolved_mu_2016_mDR, lepPt_min, topoet_min);

    } // if(m_isBtagged==2)


    if (fakeRate<0) fakeRate=0; 

    if(fakeRate>realRate) {
    //std::cout<<"REACHED HERE = "<<std::endl;
    if(m_isBtagged==2) {
    
    int lepPtBin = fake_map_resolved_mu_2016_mDR->GetXaxis()->FindBin(lepPt_min);
    int topoetBin = fake_map_resolved_mu_2016_mDR->GetYaxis()->FindBin(topoet_min);
    std::cout<<"FakeRate = "<<fakeRate<<", RealRate = "<<realRate<<", xbin = "<<lepPtBin<<", ybin = "<<topoetBin<<std::endl;
    } // if(m_isBtagged==2)
    else {    
    if(closejl_DR < 0.4) {
    int lepPtBin = fake_map_resolved_mu_2016_lDR->GetXaxis()->FindBin(lepPt_min);
    int topoetBin = fake_map_resolved_mu_2016_lDR->GetYaxis()->FindBin(topoet_min);
    std::cout<<"DR < 0.4"<<std::endl;
    std::cout<<"FakeRate = "<<fakeRate<<", RealRate = "<<realRate<<", xbin = "<<lepPtBin<<", ybin = "<<topoetBin<<std::endl;
    } // if(closejl_DR < 0.4)


    if(closejl_DR > 0.4) {
    int lepPtBin = fake_map_resolved_mu_2016_hDR->GetXaxis()->FindBin(lepPt_min);
    int topoetBin = fake_map_resolved_mu_2016_hDR->GetYaxis()->FindBin(topoet_min);
    std::cout<<"DR > 0.4"<<std::endl; 
    std::cout<<"FakeRate = "<<fakeRate<<", RealRate = "<<realRate<<", xbin = "<<lepPtBin<<", ybin = "<<topoetBin<<std::endl;
    } // if(closejl_DR > 0.4)
    } // else

    } // if(fakeRate>realRate)

  
  return;
        
}

void MMUtils::getRatesResolvedEl(float &realRate, float &realRate_err, float &fakeRate, float &fakeRate_err, float lepPt, float closejl_DR, float absEta, float cosDPhi, float mwt, float topoetcone, const unsigned int runNumber){


    get2Drates(realRate, realRate_err, eff_map_resolved_e_2016, lepPt, topoetcone);  

    float lepPt_min(0.);
    //float lepPt_limit(700);
    float lepPt_limit(695);

    float topoet_min(-5.);
    float topoet_limit(30);

    lepPt_min = std::min(lepPt, lepPt_limit);
    topoet_min = std::min(topoetcone, topoet_limit);
 
    get2Drates(fakeRate, fakeRate_err, fake_map_resolved_e_2016, lepPt_min, topoet_min);

    return;
}

float MMUtils::getMMweights(const Event &evt, const int runMM_StatErr, const bool isElectron, const bool isBoosted, const unsigned int runNumber) {
   
   bool isTight;
   float d0sig;
   float topoetcone;

   if ( isElectron && evt.electron().size()<1 ) return 0;
   if (!isElectron && evt.muon().size()<1 )     return 0;
   
   TLorentzVector lepP4; 
    
   if (isElectron)    {
       lepP4 = evt.electron()[0].mom();
       isTight = evt.electron()[0].isTightPP();
       d0sig = evt.electron()[0].sd0();
       topoetcone = evt.electron()[0].topoetcone20()*1e-3;
       
   }else {
       lepP4 = evt.muon()[0].mom();
       isTight = evt.muon()[0].isTight();
       d0sig = evt.muon()[0].sd0();
       topoetcone = evt.muon()[0].topoetcone20()*1e-3;
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
   

   	if (isElectron)	getRatesResolvedEl(realRate, realRate_err, fakeRate, fakeRate_err, lepPt, closejl_DR, absEta, cosDPhi, mWt, topoetcone, runNumber);
   	else		getRatesResolvedMu(realRate, realRate_err, fakeRate, fakeRate_err, lepPt, closejl_DR, closejl_pT, cosDPhi, MET, mWt, deltaPhi, topoetcone, runNumber);
	

   float fake_eta_ratio(1.);
   float eff_eta_ratio(1.);
   if(m_etaCorr > 0){

      if(isElectron)
	  {
	     fake_eta_ratio = getEtaCorrectionFactor(fake_lepEta_1bin_e_2016, fake_lepEta_20bins_e_2016, absEta);
	     eff_eta_ratio  = getEtaCorrectionFactor(eff_lepEta_1bin_e_2016,  eff_lepEta_20bins_e_2016, absEta);
	  }
   	else
	  {
	     fake_eta_ratio = getEtaCorrectionFactor(fake_lepEta_1bin_mu_2016, fake_lepEta_20bins_mu_2016, absEta);
	     eff_eta_ratio  = getEtaCorrectionFactor(eff_lepEta_1bin_mu_2016,  eff_lepEta_20bins_mu_2016, absEta);
	  }
      
     }
   
   float fake_DR_ratio(1.);
   float eff_DR_ratio(1.);
   if(m_DRCorr > 0)
     {
   	fake_DR_ratio = getFakeDRCorrectionFactor(isElectron, lepPt, closejl_DR, runNumber);
	eff_DR_ratio = getEffDRCorrectionFactor(isElectron, lepPt, closejl_DR, runNumber);
     }
   
   
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
   
   
   float fake_corr = 1;
   float real_corr = 1;
   if(m_etaCorr > 0 ){
   	fake_corr *= fake_eta_ratio;
   	real_corr *= eff_eta_ratio;
   }
   if(m_DRCorr > 0 ){
   	fake_corr *= fake_DR_ratio;
   	real_corr *= eff_DR_ratio;
   }
   
   if(fakeRate * fake_corr < realRate * real_corr && realRate * real_corr<=1.)
     {
	fakeRate  *= fake_corr;
     	realRate  *= real_corr;
     }
   else
     {
	std::cerr << "Error: fakeRate= "   << fakeRate   << "\t fake_corr= "   << fake_corr        << " -> new fake rate: "                    << fakeRate * fake_corr << std::endl;
	std::cerr << "Error: realRate= "   << realRate   << "\t real_corr= "   << real_corr        << " -> new real rate: "                    << realRate * real_corr << std::endl;
	std::cerr << "Error: iselectron= " << isElectron << "\t pT= " << lepPt << "\t  Delta R= " << closejl_DR << "\t  btag=" << m_isBtagged << std::endl; // pt, dr, bjet, iselec
     }
   
   
   if (isTight){
     if(realRate>0 && fakeRate>0)     Weight = fakeRate*(realRate - 1)/(realRate - fakeRate);     
     else{
     	   //  if(realRate==0)std::cerr << "Error: realRate equal to " << realRate << " (tight) " << mWt << std::endl;	   
     	   //  if(fakeRate==0)std::cerr << "Error: fakeRate equal to " << fakeRate << " (tight) " << lepPt << " " << topoetcone << std::endl;	    
	     Weight = 0;
     }
   }
   else {	
     if(realRate>0 && fakeRate>0)  Weight = fakeRate*realRate/(realRate - fakeRate);
     else{
	  //   if(realRate==0)std::cerr << "Error: realRate equal to " << realRate << "  (anti-tight) " << mWt << std::endl;	   
     	     //if(fakeRate==0)std::cerr << "Error: fakeRate equal to " << fakeRate << "  (anti-tight) " << mWt << " " << cosDPhi << std::endl;
     	     Weight = 0;
     }       
   
   }//isTight
   
   //if(!isTight)	std::cout << "is tight? " << isTight << " - QCD weight" << Weight << std::endl;
   
   return Weight;  

}//getMMweights

