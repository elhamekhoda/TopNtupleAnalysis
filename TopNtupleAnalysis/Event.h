/**
 * @brief Event class, with information read off the input file read using MiniTree.
 * @author Danilo Enoque Ferreira de Lima <dferreir@cern.ch>
 */
#ifndef EVENT_H
#define EVENT_H

#include <vector>
#include "TopNtupleAnalysis/Electron.h"
#include "TopNtupleAnalysis/Muon.h"
#include "TopNtupleAnalysis/Jet.h"
#include "TopNtupleAnalysis/LargeJet.h"

class Event {
  public:
    Event();
    virtual ~Event();

    void clear();

    std::vector<Electron> &electron();
    std::vector<Muon> &muon();
    std::vector<Jet> &jet();
    std::vector<LargeJet> &largeJet();

    const std::vector<Electron> &electron() const;
    const std::vector<Muon> &muon() const;
    const std::vector<Jet> &jet() const;
    const std::vector<LargeJet> &largeJet() const;

    void met(float met_x, float met_y);
    TLorentzVector met() const;

    int &runNumber();
    const int runNumber() const;

    int &eventNumber();
    const int eventNumber() const;

    bool &isData();
    const bool isData() const;

    int &channelNumber();
    const int channelNumber() const;

    float &weight_pileup();
    const float weight_pileup() const;

    float &mu();
    const float mu() const;

    float &weight_mc();
    const float weight_mc() const;
    
    float &weight_bTagSF();
    const float weight_bTagSF() const;
    
    float &weight_leptonSF();
    const float weight_leptonSF() const;

    std::vector<std::string> &passes();
    const bool passes(const std::string &selection) const;

    // not implemented yet:
    unsigned int &lbn();
    const unsigned int lbn() const;
    const int hfor() const;
    int &hfor();
    int &npv();
    const int npv() const;


    TLorentzVector &MC_ttbar_beforeFSR();
    const TLorentzVector &MC_ttbar_beforeFSR() const;

  protected:

    std::vector<std::string> m_passes;

    int m_hfor;

    std::vector<Electron> m_electron;
    std::vector<Muon> m_muon;
    std::vector<Jet> m_jet;
    std::vector<LargeJet> m_largeJet;

    TLorentzVector m_met;
    TLorentzVector m_MC_ttbar_beforeFSR;

    int m_runNumber;
    int m_eventNumber;
    int m_channelNumber;
    bool m_isData;
    float m_mu;

    int m_npv;
    float m_rho;

    float m_weight_mc;
    float m_weight_pileup;
    float m_weight_bTagSF;
    float m_weight_leptonSF;
    
    unsigned int m_lbn;
};

#endif

