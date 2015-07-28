/**
 * @brief Class that reads information from the input file and puts it in a object-oriented format in Event.
 * @author Danilo Enoque Ferreira de Lima <dferreir@cern.ch>
 */
#ifndef MINITREE_H
#define MINITREE_H

#include <string>
#include "TChain.h"
#include "TTree.h"
#include <vector>
#include "TopNtupleAnalysis/Event.h"

#include "TFile.h"

using namespace std;

class MiniTree {
  public:

    MiniTree(bool toWrite = true, const std::string &file = "tree.root", const std::string &name="nominal");
    virtual ~MiniTree();

    void addFileToRead(const std::string &fname);
    int GetEntries();
    double getSumWeights();
    void read(int event, Event &e);
    void write(const Event &e);

    double &sumWeights();
    TTree *m_chain;
    double m_sumWeights;

    TFile  *m_fileToWrite;
    TTree *m_num;
    bool m_toWrite;
    std::string m_name;
    
    Float_t         binning01;
    Float_t         binning02;
    Float_t         binning03;
    Float_t         binning04;
    Float_t         binning05;

  private:

    void prepareBranches();

    Float_t         weight_mc;
    Float_t         weight_pileup;
    Float_t         weight_bTagSF;
    Float_t         weight_leptonSF;
    UInt_t          eventNumber;
    UInt_t          runNumber;
    UInt_t          mcChannelNumber;
    Float_t         mu;
    vector<float>   *el_pt;
    vector<float>   *el_eta;
    vector<float>   *el_phi;
    vector<float>   *el_e;
    vector<float>   *el_charge;
    vector<float>   *el_miniiso;
    vector<float>   *mu_pt;
    vector<float>   *mu_eta;
    vector<float>   *mu_phi;
    vector<float>   *mu_e;
    vector<float>   *mu_charge;
    vector<float>   *mu_miniiso;
    vector<float>   *jet_pt;
    vector<float>   *jet_eta;
    vector<float>   *jet_phi;
    vector<float>   *jet_e;
    vector<int>     *jet_closeToLepton;
    vector<float>   *jet_mv1;
    vector<float>   *jet_mv2c20;
    vector<float>   *jet_ip3dsv1;
    vector<float>   *jet_jvt;
    vector<float>   *ljet_pt;
    vector<float>   *ljet_eta;
    vector<float>   *ljet_phi;
    vector<float>   *ljet_e;
    vector<float>   *ljet_m;
    vector<float>   *ljet_sd12;
    vector<int>     *ljet_good;

    float           MC_ttbar_beforeFSR_pt;
    float           MC_ttbar_beforeFSR_eta;
    float           MC_ttbar_beforeFSR_phi;
    float           MC_ttbar_beforeFSR_m;
    
    Float_t         met_met;
    Float_t         met_phi;

    vector<float>   *mc_pt;
    vector<float>   *mc_eta;
    vector<float>   *mc_phi;
    vector<float>   *mc_e;
    vector<int>     *mc_pdgId;

    // selections (some will not exist)
    Int_t           bejets;
    Int_t           bmujets;
    Int_t           rejets;
    Int_t           rmujets;

    Int_t           ejets;
    Int_t           mujets;

    Int_t           ee;
    Int_t           mumu;
    Int_t           emu;

};

#endif

