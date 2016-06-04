
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

//#include "../../PMGTools/Root/PMGCorrsAndSysts.cxx"
//#include "../../PMGTools/PMGTools/PMGCorrsAndSysts.h"

#include "TLorentzVector.h"
#include <vector>

class WrapperExtras {
  public:
    TtresNeutrinoBuilder m_neutrinoBuilder;
    TtresChi2 m_chi2;
    WeakCorr::WeakCorrScaleFactorParam m_ewkTool;
    //PMGCorrsAndSysts m_pmg;

    WrapperExtras() : m_neutrinoBuilder("MeV"), m_chi2("MeV"), m_ewkTool("../share/EWcorr_param.root"), m_pmg() {
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
    double getEWK(TLorentzVector top, TLorentzVector topbar, int initial_type, int var = 0) {
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
      if (var == 1) {
        return sf.up;
      } else if (var == 2) {
        return sf.down;
      }
      return sf.nominal;
    }
    //double getWjets22Weight(int njets) {
    //  return m_pmg.Get_Sherpa22VJets_NJetCorrection(njets);
    //}
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

MV2C10_CUT = 0.6455
# systematic variations are specified according to this syntax:
# btag[A]SF_[eig][_pt[X]]__1[up/down]
# where:
# [A] = b,c,l,e for b-jet, c-jet, light-jet or extrapolation variations
# [eig] is the number of the eigen vector
# [X] is the number of the pt bin if we want to vary only jets within a pt bin
# if there is no 'btag' in the name of the variation, then the nominal SF is used
def applyBtagSF(sel, s):
    pref = 'tjet_bTagSF_70'
    varName = ''
    nomName = pref
    ptbinInS = 0
    eig = -1
    # if this is a b-tagging variation
    # then check which branch to take to apply the variation
    if 'btag' in s:
        # if we are also varying only jets in a specific pt bin, the pt bin is identified as "ptX", where X is an integer
	# get "X" as an integer from the systematic name
        if 'pt' in s:
	    ptbinInS = int(s.split('pt')[1][0])
	    # later, if this is != -1, we will use it to apply the variation only at the jets within this pt bin
	# get eigenvector index
	eig = int(s.split('_')[1])
	# get direction
	direction = 'up'
	if 'down' in s:
  	    direction = 'down'
	# check if it is a b,c,light or extrapolation variation and set name
        if 'btagbSF_' in s:
            varName = pref+'_eigen_B_'+direction
        if 'btagcSF_' in s:
            varName = pref+'_eigen_C_'+direction
        if 'btaglSF_' in s:
            varName = pref+'_eigen_Light_'+direction
        if 'btageSF_0' in s:
            varName = pref+'_extrapolation_'+direction
	    eig = -1
        if 'btageSF_1' in s:
            varName = pref+'_extrapolation_from_charm_'+direction
	    eig = -1
    else: # not a b-tagging variation, so take the nominal
        varName = pref

    btagsf = 1.0
    # loop over track jets
    for bidx in range(0, len(sel.tjet_mv2c20)):
        pb = ROOT.TLorentzVector(sel.tjet_pt[bidx], sel.tjet_eta[bidx], sel.tjet_phi[bidx], sel.tjet_e[bidx])
	# and apply object definition cuts (should already have been applied)
        if pb.Perp() > 10e3 and math.fabs(pb.Eta()) < 2.5 and sel.tjet_numConstituents[bidx] >= 2:
	    # if we requested to vary only jets in a specific pt bin, check if this jet is in the pt bin
	    if ptbinInS != 0:
  	        ptbin = 0
	        if pb.Perp() < 50e3:
	            ptbin = 1
                elif pb.Perp() < 100e3:
	            ptbin = 2
	        else:
	            ptbin = 3
		if ptbinInS == ptbin:
		    # if this jet is in the correct pt bin, apply the syst. variation
	            theWeight = getattr(sel, varName)
		else:
		    # otherwise, take the nominal SF for this jet
		    # even if we are supposed to vary it for any other criteria
	            theWeight = getattr(sel, nomName)
	    else: # we have not requested the pt binned variation
	        # so we always vary all jets, regardless of the pt bin
		# if no variation was requested, varName will be set to the nominal above
	        theWeight = getattr(sel, varName)
	    if eig > -1: # branches in b,c,light variation have a second index related to the eigenvector number
                btagsf *= theWeight[bidx][eig]
	    else: # extrapolation branches or the nominal, have no second index
                btagsf *= theWeight[bidx]
    return btagsf

# TODO
def readEvent(mt):
    return mt

listEWK = [410000, 301528, 301529, 301530, 301531, 301532]
def applyEWK(sel, s):
    top = ROOT.TLorentzVector()
    top.SetPtEtaPhiM(sel.MC_t_pt, sel.MC_t_eta, sel.MC_t_phi, sel.MC_t_m)
    topbar = ROOT.TLorentzVector()
    topbar.SetPtEtaPhiM(sel.MC_tbar_pt, sel.MC_tbar_eta, sel.MC_tbar_phi, sel.MC_tbar_m)
    if s == 'ttEWK__1up':
        w = wrapperC.getEWK(top, topbar, sel.initial_type, 1)
    elif s == 'ttEWK__1down':
        w = wrapperC.getEWK(top, topbar, sel.initial_type, 2)
    else:
        w = wrapperC.getEWK(top, topbar, sel.initial_type, 0)
    return w

listWjets22 = []
listWjets22.extend(range(363330, 363354+1))
listWjets22.extend(range(363436, 363483+1))
#def applyWjets22Weight(sel):
#    if not sel.mcChannelNumber in listWjets22:
#        return 1.0
#    njet = 0
#    for i in range(0, len(sel.akt4truthjet_pt)):
#        if sel.akt4truthjet_pt[i] > 20e3 and fabs(sel.akt4truthjet_eta[i]) < 4.5:
#	    njet += 1
#    return wrapperC.getWjets22Weight(njet)

# list of systematics related to changes in the weights only
weightSF = {'' : ['pileup', 'leptonSF', 'jvt'],
            'eTrigSF__1up': ['pileup', 'leptonSF_EL_SF_Trigger_UP', 'jvt'],
            'eTrigSF__1down': ['pileup', 'leptonSF_EL_SF_Trigger_DOWN', 'jvt'],
            'eIDSF__1up': ['pileup', 'leptonSF_EL_SF_ID_UP', 'jvt'],
            'eIDSF__1down': ['pileup', 'leptonSF_EL_SF_ID_DOWN', 'jvt'],
            'eRecoSF__1up': ['pileup', 'leptonSF_EL_SF_Reco_UP', 'jvt'],
            'eRecoSF__1down': ['pileup', 'leptonSF_EL_SF_Reco_DOWN', 'jvt'],
            'eIsolSF__1up': ['pileup', 'leptonSF_EL_SF_Isol_UP', 'jvt'],
            'eIsolSF__1down': ['pileup', 'leptonSF_EL_SF_Isol_DOWN', 'jvt'],
            'muTrigStatSF__1up': ['pileup', 'leptonSF_MU_SF_Trigger_STAT_UP', 'jvt'],
            'muTrigStatSF__1down': ['pileup', 'leptonSF_MU_SF_Trigger_STAT_DOWN', 'jvt'],
            'muTrigSystSF__1up': ['pileup', 'leptonSF_MU_SF_Trigger_SYST_UP', 'jvt'],
            'muTrigSystSF__1down': ['pileup', 'leptonSF_MU_SF_Trigger_SYST_DOWN', 'jvt'],
            'muIDStatSF__1up': ['pileup', 'leptonSF_MU_SF_ID_STAT_UP', 'jvt'],
            'muIDStatSF__1down': ['pileup', 'leptonSF_MU_SF_ID_STAT_DOWN', 'jvt'],
            'muIDSystSF__1up': ['pileup', 'leptonSF_MU_SF_ID_SYST_UP', 'jvt'],
            'muIDSystSF__1down': ['pileup', 'leptonSF_MU_SF_ID_SYST_DOWN', 'jvt'],
            'muIsolStatSF__1up': ['pileup', 'leptonSF_MU_SF_Isol_STAT_UP', 'jvt'],
            'muIsolStatSF__1down': ['pileup', 'leptonSF_MU_SF_Isol_STAT_DOWN', 'jvt'],
            'muIsolSystSF__1up': ['pileup', 'leptonSF_MU_SF_Isol_SYST_UP', 'jvt'],
            'muIsolSystSF__1down': ['pileup', 'leptonSF_MU_SF_Isol_SYST_DOWN', 'jvt'],
            'pileupSF__1up': ['pileup_UP', 'leptonSF', 'jvt'],
            'pileupSF__1down': ['pileup_DOWN', 'leptonSF', 'jvt'],
            'jvtSF__1up': ['pileup', 'leptonSF', 'jvt_UP'],
            'jvtSF__1down': ['pileup', 'leptonSF', 'jvt_DOWN'],
	   }

weightChangeSystematics = weightSF.keys()

