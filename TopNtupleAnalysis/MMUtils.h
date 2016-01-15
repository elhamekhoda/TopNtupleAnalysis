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

    float getMMweights(const Event &evt, int runMM_StatErr);

  private:

    TH2F * eff_map_resolved_e;
    TH2F * eff_map_resolved_mu;
    TH2F * eff_map_boosted_e;
    TH2F * eff_map_boosted_mu;
    
    TH2F * eff_map;
	
    TH1F * fake_pt_resolved_e;
    TH1F * fake_pt_resolved_mu;
    TH1F * fake_pt_boosted_e;
    TH1F * fake_pt_boosted_mu;
    
    TH1F * fake_dr_resolved_e;
    TH1F * fake_dr_resolved_mu;
    TH1F * fake_dr_boosted_e;
    TH1F * fake_dr_boosted_mu;
    
    TH1F * fake_dr;;
    TH1F * fake_pt;
    
    HistogramService m_hSvc;
    
    bool fake_1Dparam_dr;
    
};

#endif

