/**
 * @brief Code to implement the Matrix method for the QCD estimation
 * @author Danilo Enoque Ferreira de Lima <dferreir@cern.ch>
 */
#ifndef MMUTILS_H
#define MMUTILS_H

#include "TopNtupleAnalysis/Event.h"
#include "TopNtupleAnalysis/HistogramService.h"

#include <string>
#include <getopt.h>

#include "TFile.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TH1D.h"
#include "TH2D.h"

class MMUtils{

  public:
    MMUtils(const std::string &eff_filename="eff.root", const std::string &fake_filename="fake.root"); 
    ~MMUtils();

    float getMMweights(const Event &evt, const int runMM_StatErr, const bool isElectron, const bool isBoosted);
    
    void get2Drates(float &rate, float &rate_err, TH2F* rate_map, float x, float y);
    void get1Drates(float &rate, float &rate_err, TH1F* rate_map, float x);
    
    void getRatesBoostedMu(float &realRate, float &realRate_err, float &fakeRate, float &fakeRate_err, float lepPt, float closejl_DR);
    void getRatesBoostedEl(float &realRate, float &realRate_err, float &fakeRate, float &fakeRate_err, float lepPt, float closejl_DR);
    void getRatesResolvedMu(float &realRate, float &realRate_err, float &fakeRate, float &fakeRate_err, float lepPt, float closejl_DR, float absEta, float cosDPhi, float met, float mwt);
    void getRatesResolvedEl(float &realRate, float &realRate_err, float &fakeRate, float &fakeRate_err, float lepPt, float closejl_DR, float closejl_pT, float cosDPhi);
    
    
  private:

    TH2F * eff_map_resolved_e;
    TH2F * eff_map_resolved_mu;
    TH2F * eff_map_boosted_e;
    TH2F * eff_map_boosted_mu;
    	
    TH2F * fake_map_resolved_e;
    TH2F * fake_map_resolved_e_lEta;
    TH2F * fake_map_resolved_e_hEta;
    TH2F * fake_map_resolved_mu;
    TH2F * fake_map_resolved_mu_lDR;
    TH2F * fake_map_resolved_mu_hDR;
    TH2F * fake_map_resolved_mu_lCos;
    TH2F * fake_map_resolved_mu_hCos;
    TH2F * fake_map_resolved_mu_lLepPt;
    TH2F * fake_map_resolved_mu_hLepPt;
    
    TH1F * fake_dr_resolved_mu;
    TH1F * fake_pt_resolved_mu;
    TH1F * fake_cos_resolved_mu;
    TH1F * fake_met_resolved_mu;
    TH1F * fake_mwt_resolved_mu;
    TH1F * fake_mwtmet_resolved_mu;
    
    TH1F * fake_pt_boosted_e;
    TH1F * fake_dr_boosted_mu;
    
    HistogramService m_hSvc;
        
};

#endif

