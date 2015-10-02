/**
 * @brief Analysis class for tt resonances.
 * @author Danilo Enoque Ferreira de Lima <dferreir@cern.ch>
 */
#ifndef ANATTRESQCD_H
#define ANATTRESQCD_H

#include <string>
#include "TH1F.h"
#include "TH2F.h"
#include "TFile.h"
#include "TopNtupleAnalysis/Event.h"
#include "TopNtupleAnalysis/Analysis.h"

#include "TopNtupleAnalysis/TtresNeutrinoBuilder.h"
#include "TopNtupleAnalysis/TtresChi2.h"

class AnaTtresQCD : public Analysis {
  public:
    AnaTtresQCD(const std::string &filename, bool electron, bool boosted, std::vector<std::string> &systList);
    virtual ~AnaTtresQCD();

    virtual void runEfficiency(const Event &e, double weight, const std::string &syst);
    virtual void runFakeRate(const Event &e, double weight, const std::string &syst);
    void terminate() {};
    void setIsData(bool isData) {};

  protected:
    bool m_electron;
    bool m_boosted;

    TtresNeutrinoBuilder m_neutrinoBuilder;
    TtresChi2 m_chi2;
};

#endif

