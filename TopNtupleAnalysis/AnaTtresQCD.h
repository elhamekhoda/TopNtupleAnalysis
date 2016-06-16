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

    void run(const Event &e, double weight, const std::string &syst);
    
    virtual void runRealRateQCDCR(const Event &e, double weight, const std::string &suffix);
    virtual void runRealRateWQCDCR(const Event &e, double weight, const std::string &suffix);
    virtual void GetRealHistograms(const Event &evt, const double weight, const std::string &suffix);
    
    virtual void runFakeRateQCDCR(const Event &e, double weight, const std::string &suffix);
    virtual void runFakeRateWQCDCR(const Event &e, double weight, const std::string &suffix);
    virtual void GetFakeHistograms(const Event &e, double weight, const std::string &suffix_corr, const std::string &suffix);
    virtual void get1Drates(float &rate, float &rate_err, TH1F* rate_map, float x);
    virtual void get2Drates(float &rate, float &rate_err, TH2F* rate_map, float x, float y);
    virtual void IniHistograms(std::string &suffix);
    
    void terminate() {};
    void setIsData(bool isData) {};

  protected:
    bool m_electron;
    bool m_boosted;

    TtresNeutrinoBuilder m_neutrinoBuilder;
    TtresChi2 m_chi2;
};

#endif

