/**
 * @brief Analysis class for tt resonances.
 * @author Danilo Enoque Ferreira de Lima <dferreir@cern.ch>
 */
#ifndef ANAMULTIJETALLIN1_H
#define ANAMULTIJETALLIN1_H

#include <string>
#include "TH1F.h"
#include "TH2F.h"
#include "TFile.h"
#include "TopNtupleAnalysis/Event.h"
#include "TopNtupleAnalysis/Analysis.h"

#include "TopNtupleAnalysis/TtresNeutrinoBuilder.h"
#include "TopNtupleAnalysis/TtresChi2.h"

class AnaMultijetAllIn1 : public Analysis {
  public:
    AnaMultijetAllIn1(const std::string &filename, bool electron, bool boosted, std::vector<std::string> &systList);
    virtual ~AnaMultijetAllIn1();

    void run(const Event &e, double weight, const std::string &syst);
    void terminate() {};
    void setIsData(bool isData) {};

    inline bool isElectron(){return m_electron;};
    inline bool isBoosted(){return m_boosted;};

  protected:
    bool m_electron;
    bool m_boosted;

    TtresNeutrinoBuilder m_neutrinoBuilder;
    TtresChi2 m_chi2;

    double _tree_truemtt;
    double _tree_mtt;
    double _tree_weight;
    int     _tree_cat;
    std::string _tree_syst;

 
};

#endif

