
import ROOT
from array import array

def initBinds():
    bind_neutrino = '''
#include "TopNtupleAnalysis/TtresNeutrinoBuilder.h"
#include "TopNtupleAnalysis/TtresChi2.h"

#include "Root/TtresNeutrinoBuilder.cxx"
#include "Root/TtresChi2.cxx"

#include "TopNtupleAnalysis/WeakCorrScaleFactorParam.h"
#include "Root/WeakCorrScaleFactorParam.cxx"

#include "TLorentzVector.h"
#include <vector>

class WrapperExtras {
  public:
    TtresNeutrinoBuilder m_neutrinoBuilder;
    TtresChi2 m_chi2;
    WeakCorr::WeakCorrScaleFactorParam m_ewkTool;
    WrapperExtras() : m_neutrinoBuilder("MeV"), m_chi2("MeV"), m_ewkTool("../share/EWcorr_param.root") {
      m_chi2.Init(TtresChi2::DATA2015_MC15);
    }
    TLorentzVector getNu(TLorentzVector l, double met, double met_phi) {
      std::vector<TLorentzVector *> vec_nu = m_neutrinoBuilder.candidatesFromWMass_Rotation(&l, met, met_phi, true);
      TLorentzVector nu;
      if (vec_nu.size() > 0) {
        nu = *(vec_nu[0]);
	for (size_t z = 0; z < vec_nu.size(); ++z) delete vec_nu[z];
	vec_nu.clear();
      }
      return nu;
    }

    std::map<std::string, double> getMtt(TLorentzVector lep, std::vector<TLorentzVector> jets, std::vector<bool> btag, TLorentzVector met) {
      // inputs 
      // LEPTON --> TLorentzVector for your lepton
      // vjets -->  std::vector<TLorentzVector*> for the jets
      // vjets_btagged --> std::vector<bool> to say if the jets are btagged or not
      // met --> TLorentzVector for your MET

      // outputs, they will be filled by the TTBarLeptonJetsBuilder_chi2
      int  igj3, igj4; // index for the Whad
      int igb3, igb4; // index for the b's
      int  ign1;  // index for the neutrino (because chi2 can test both pz solution)
      double chi2ming1, chi2ming1H, chi2ming1L;

      std::vector<TLorentzVector *> vjets;
      std::vector<bool> vjets_btagged;
      for (size_t z = 0; z < jets.size(); ++z) {
        vjets.push_back(new TLorentzVector(0,0,0,0));
        vjets[z]->SetPtEtaPhiE(jets[z].Perp(), jets[z].Eta(), jets[z].Phi(), jets[z].E());
        // https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/BTagingxAODEDM
        // https://twiki.cern.ch/twiki/bin/view/AtlasProtected/BTaggingBenchmarks
        vjets_btagged.push_back(btag[z]);
      }
      bool status = m_chi2.findMinChiSquare(&lep, &vjets, &vjets_btagged, &met, igj3, igj4, igb3, igb4, ign1, chi2ming1, chi2ming1H, chi2ming1L); 
    
      float chi2Value = 1000000; // log10(1000000) = 6
      float mwh = -1;
      float mtl = -1;
      float mth = -1;
      float mtt = -1;

      if (status) {
        chi2Value = chi2ming1;
	mwh = m_chi2.getResult_Mwh();
	mtl = m_chi2.getResult_Mtl();
	mth = m_chi2.getResult_Mth();
	mtt = m_chi2.getResult_Mtt();
      }
    
      for (size_t z = 0; z < vjets.size(); ++z) {
        delete vjets[z];
      }
      vjets.clear();
      vjets_btagged.clear();
      std::map<std::string, double> ret;
      ret["mtt"] = mtt;
      ret["mtl"] = mtl;
      ret["mth"] = mth;
      ret["mwh"] = mwh;
      return ret;
    }
    double getEWK(TLorentzVector top, TLorentzVector topbar, int initial_type) {
      WeakCorr::ScaleFactor sf; 
      float t_pt = top.Perp();
      float t_eta = top.Eta();
      float t_phi = top.Phi();
      float t_m = top.M();

      float tbar_pt = topbar.Perp();
      float tbar_eta = topbar.Eta();
      float tbar_phi = topbar.Phi();
      float tbar_m = topbar.M();
      sf = m_ewkTool.getScaleFactor(t_pt, t_eta, t_phi, t_m, tbar_pt, tbar_eta, tbar_phi, tbar_m, initial_type);
      return sf.nominal;
    }
};
'''
    # hack to get the proper paths
    import os.path
    import os
    if not (os.path.isfile('TopNtupleAnalysis') or os.path.islink('TopNtupleAnalysis')):
        os.system('ln -s ../TopNtupleAnalysis .')
    if not (os.path.isfile('Root') or os.path.islink('Root')):
        os.system('ln -s ../Root .')
    ROOT.gInterpreter.ProcessLine(bind_neutrino)
    return ROOT.WrapperExtras()

wrapperC = initBinds()


def loadXsec(m, fName):
    f = open(fName)
    for l in f.readlines():
        if l[0] == '#':
	    continue
        lsplit = l.split()
	if len(lsplit) == 0:
	    continue
	if len(lsplit) < 3:
	    print "I cannot understand this line:", lsplit
	    continue
	m[int(lsplit[0])] = float(lsplit[1])*float(lsplit[2])

def addFilesInChain(c, txtFileOption):
    for f in txtFileOption.split(','):
        txtf = open(f)
        for l in txtf.readlines():
	    if l[-1] == '\n':
	        l = l[0:-1]
            c.Add(l)

class Event:
    def __init__(self):
        pass

MV2C20_CUT = -0.3098
# TODO
def readEvent(mt):
    return mt
    #sel = Event()
    #sel.weight_mc = mt.weight_mc
    #sel.weight_pileup = mt.weight_pileup

# TODO
listEWK = [410000, 301528, 301529, 301530, 301531, 301532]
def applyEWK(sel):
    top = ROOT.TLorentzVector()
    top.SetPtEtaPhiM(sel.MC_t_pt, sel.MC_t_eta, sel.MC_t_phi, sel.MC_t_m)
    topbar = ROOT.TLorentzVector()
    topbar.SetPtEtaPhiM(sel.MC_tbar_pt, sel.MC_tbar_eta, sel.MC_tbar_phi, sel.MC_tbar_m)
    w = wrapperC.getEWK(top, topbar, sel.initial_type)
    return w

