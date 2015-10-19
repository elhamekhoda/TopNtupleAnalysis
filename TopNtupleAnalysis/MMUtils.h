/**
 * @brief Code to implement the Matrix method for the QCD estimation
 * @author Danilo Enoque Ferreira de Lima <dferreir@cern.ch>
 */
#ifndef MMUTILS_H
#define MMUTILS_H

#include <string>
#include <getopt.h>
#include "TopNtupleAnalysis/Event.h"
#include "TFile.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TH1D.h"
#include "TH2D.h"

class MMUtils{

  public:
    MMUtils(const std::string &eff_filename="eff.root", const std::string &fake_filename="fake.root"); 
    ~MMUtils();

    float getMMweights(const Event &evt);

  private:

    TH2F * eff_map_resolved_e;
    TH2F * eff_map_resolved_mu;
    TH2F * eff_map_boosted_e;
    TH2F * eff_map_boosted_mu;
    
    TH2F * fake_map_resolved_e;
    TH2F * fake_map_resolved_mu;
    TH2F * fake_map_boosted_e;
    TH2F * fake_map_boosted_mu;

    TH2F * eff_map;
    TH2F * fake_map;
};

#endif

