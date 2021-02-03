/**
 * @brief Code to implement the Matrix method for the QCD estimation
 * @author Danilo Enoque Ferreira de Lima <dferreir@cern.ch>
 */
#ifndef MMUTILS_H
#define MMUTILS_H

#include "TopNtupleAnalysis/Event.h"

#include <string>
#include <getopt.h>

#include "TFile.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TH1D.h"
#include "TH2D.h"

class MMUtils{

  public:
    MMUtils(const int isBtagged,const int etaCorr, const int DRCorr, const std::string &eff_filename2016, const std::string &fake_filename2016); 
    virtual ~MMUtils();

    float getMMweights(const Event &evt, const int runMM_StatErr, const bool isElectron, const bool isBoosted, const unsigned int runNumber);
    


     float getEtaCorrectionFactor(TH1D* rate_1bin, TH1D* rate_xbins, float absEta);
     float getFakeDRCorrectionFactor(bool isElectron, float lepPt, float closejl_DR, const unsigned int runNumber);
     float getEffDRCorrectionFactor(bool isElectron, float lepPt, float closejl_DR, const unsigned int runNumber);
     float getDRCorrectionFactorTools(TH2D* lepPt_lowDR, TH2D* lepPt_highDR, TH2D* lepPt_minDeltaR, float lepPt, float closejl_DR);
     void get2Drates(float &rate, float &rate_err, TH2D* rate_map, float x, float y);
     void get1Drates(float &rate, float &rate_err, TH1D* rate_map, float x);


    void getRatesResolvedMu(float &realRate, float &realRate_err, float &fakeRate, float &fakeRate_err, float lepPt, float closejl_DR, float absEta, float cosDPhi, float met, float mwt, float DPhi, float topoetcone, const unsigned int runNumber);
    void getRatesResolvedEl(float &realRate, float &realRate_err, float &fakeRate, float &fakeRate_err, float lepPt, float closejl_DR, float closejl_pT, float cosDPhi, float mwt, float topoetcone, const unsigned int runNumber);
    
       

  private:
TH1D *  eff_lepPt_highDR_mu_20161;
TH1D *  eff_lepPt_lowDR_mu_20161;
TH2D * fake_map_lepPt_minDeltaR_mu_20161;
TH2D * eff_map_lepPt_DR_resolved_mu_20161;   

TH2D * eff_map1_resolved_mu_2016_lDR;
TH2D * eff_map1_resolved_mu_2016_hDR;
TH2D * fake_map1_resolved_mu_2016_lDR;
TH2D * fake_map1_resolved_mu_2016_hDR;


TH2D * eff_map1_resolved_e_2016_lDR;
TH2D * eff_map1_resolved_e_2016_hDR;
TH2D * fake_map1_resolved_e_2016_lDR;
TH2D * fake_map1_resolved_e_2016_hDR;

TH2D * eff_map_resolved_e_2016_lDR;
TH2D * eff_map_resolved_e_2016_hDR;
 
   TH2D * eff_map_resolved_e_2015;
    TH2D * eff_map_resolved_mu_2015;
    TH2D * eff_map_boosted_e_2015;
    TH2D * eff_map_boosted_mu_2015;

    TH2D * eff_map_resolved_mu_2015_lDR;
    TH2D * eff_map_resolved_mu_2015_mDR;
    TH2D * eff_map_resolved_mu_2015_hDR;
	
    TH1D * fake_map_resolved_mu_2015_tmp;
    TH2D * fake_map_resolved_mu_2015_lDR;
    TH2D * fake_map_resolved_mu_2015_mDR;
    TH2D * fake_map_resolved_mu_2015_hDR;
    
    TH2D * fake_map_resolved_e_2015;
    TH2D * fake_map2_resolved_e_2015;
    TH2D * fake_map_resolved_e_2015_lEta;
    TH2D * fake_map_resolved_e_2015_hEta;
    
//     TH1F * fake_minDeltaR_resolved_e_hEta;
//     TH1F * fake_pt_resolved_e;
//     
//     TH1F * fake_pt_hmWt_resolved_e;
//     TH1F * fake_pt_mmWt_resolved_e;
//     TH1F * fake_pt_lmWt_resolved_e;
//     
     TH1D * fake_pt_boosted_e_2015;
     TH1D * fake_dr_boosted_mu_2015;
TH2D * eff_map_resolved_e_2016;
    TH2D * eff_map_resolved_e_20161;
    TH2D * eff_map_resolved_mu_2016;
    TH2D * eff_map_resolved_mu_2016_lDR1;
TH2D * eff_map_resolved_mu_2016_lDR;  
  TH2D * eff_map_resolved_mu_2016_mDR;
    TH2D * eff_map_resolved_mu_2016_hDR;
TH2D * eff_map_resolved_mu_2016_hDR1;  
  TH2D * eff_map_boosted_e_2016;
    TH2D * eff_map_boosted_mu_2016;
	
    TH2D * fake_map_resolved_e_2016_lDR;
    TH2D * fake_map_resolved_e_2016_mDR;
    TH2D * fake_map_resolved_e_2016_hDR;
    
  TH2D * fake_map_resolved_mu_2016_lDR1;
    TH2D * fake_map_resolved_mu_2016_mDR1;
    TH2D * fake_map_resolved_mu_2016_hDR1;


  TH1D * fake_map_resolved_mu_2016_tmp;
//    TH2D * fake_map_resolved_mu_2016_lDR1;
TH2D * fake_map_resolved_mu_2016_lDR;    
TH2D * fake_map_resolved_mu_2016_mDR;
    TH2D * fake_map_resolved_mu_2016_hDR;
    TH2D * fake_map_resolved_e_2016;
    TH2D * fake_map_resolved_e_20161;
    TH2D * fake_map2_resolved_e_2016;
    TH2D * fake_map_resolved_e_2016_lEta;
    TH2D * fake_map_resolved_e_2016_hEta;
    
//     TH1F * fake_minDeltaR_resolved_e_hEta;
//     TH1F * fake_pt_resolved_e;
//     
//     TH1F * fake_pt_hmWt_resolved_e;
//     TH1F * fake_pt_mmWt_resolved_e;
//     TH1F * fake_pt_lmWt_resolved_e;
//     
     TH1D * fake_pt_boosted_e_2016;
     TH1D * fake_dr_boosted_mu_2016;
    
    // lepton Eta 2016
    TH1D * fake_lepEta_1bin_e_2016;
    TH1D * fake_lepEta_20bins_e_2016;
    TH1D * fake_lepEta_e_2016;
    
 TH1D * fake_lepEta_1bin_e_20161;
    TH1D * fake_lepEta_20bins_e_20161;



    TH1D * fake_lepEta_1bin_mu_2016;
    TH1D * fake_lepEta_20bins_mu_2016;
    TH1D * fake_lepEta_mu_2016;
   

TH1D * fake_lepEta_1bin_mu_20161;
    TH1D * fake_lepEta_20bins_mu_20161; 
    
    TH1D * eff_lepEta_1bin_e_2016;
    TH1D * eff_lepEta_20bins_e_2016;
    

TH1D * eff_lepEta_1bin_e_20161;
    TH1D * eff_lepEta_20bins_e_20161;

    TH1D * eff_lepEta_1bin_mu_2016;
    TH1D * eff_lepEta_20bins_mu_2016;
    
     TH1D * eff_lepEta_1bin_mu_20161;
    TH1D * eff_lepEta_20bins_mu_20161;
    
    // lepton Eta 2015
    TH1D * fake_lepEta_1bin_e_2015;
    TH1D * fake_lepEta_20bins_e_2015;
    TH1D * fake_lepEta_e_2015;
    
    TH1D * fake_lepEta_1bin_mu_2015;
    TH1D * fake_lepEta_20bins_mu_2015;
    TH1D * fake_lepEta_mu_2015;
    
    
    TH1D * eff_lepEta_1bin_e_2015;
    TH1D * eff_lepEta_20bins_e_2015;
    
    TH1D * eff_lepEta_1bin_mu_2015;
    TH1D * eff_lepEta_20bins_mu_2015;
    
    
    // DeltaR 2016
    TH1D * fake_lepPt_highDR_e_2016;
    TH1D * fake_lepPt_lowDR_e_2016;
    
    TH1D * fake_lepPt_highDR_mu_2016;
    TH1D * fake_lepPt_lowDR_mu_2016;
    

TH1D * fake_lepPt_highDR_mu_20161;
    TH1D * fake_lepPt_lowDR_mu_20161;

    TH1D * eff_lepPt_highDR_e_2016;
    TH1D * eff_lepPt_lowDR_e_2016;
    
    TH1D * eff_lepPt_highDR_mu_2016;
    TH1D * eff_lepPt_lowDR_mu_2016;
    
    TH2D * fake_map_lepPt_minDeltaR_e_2016;
    TH2D * fake_map_lepPt_minDeltaR_mu_2016;
    TH2D * eff_map_lepPt_DR_resolved_e_2016;
    TH2D * eff_map_lepPt_DR_resolved_mu_2016;
    
    // DeltaR 2015
    TH1D * fake_lepPt_highDR_e_2015;
    TH1D * fake_lepPt_lowDR_e_2015;
    
    TH1D * fake_lepPt_highDR_mu_2015;
    TH1D * fake_lepPt_lowDR_mu_2015;
    
    TH1D * eff_lepPt_highDR_e_2015;
    TH1D * eff_lepPt_lowDR_e_2015;
    
    TH1D * eff_lepPt_highDR_mu_2015;
    TH1D * eff_lepPt_lowDR_mu_2015;
    
    TH2D * fake_map_lepPt_minDeltaR_e_2015;
    TH2D * fake_map_lepPt_minDeltaR_mu_2015;
    TH2D * eff_map_lepPt_DR_resolved_e_2015;
    TH2D * eff_map_lepPt_DR_resolved_mu_2015;
    
    
    int m_isBtagged; 
    int m_etaCorr;
    int m_DRCorr;
        
};

#endif

