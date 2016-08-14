
import ROOT
from array import array
import math



def initBinds():
    bind_neutrino = '''

#include "TopNtupleAnalysis/TtresNeutrinoBuilder.h"
#include "TopNtupleAnalysis/TtresChi2.h"

#include "Root/TtresNeutrinoBuilder.cxx"
#include "Root/TtresChi2.cxx"

#include "TopNtupleAnalysis/WeakCorrScaleFactorParam.h"
#include "Root/WeakCorrScaleFactorParam.cxx"

#include "TopNtupleAnalysis/MMUtils.h"
#include "Root/MMUtils.cxx"

#include "TopNtupleAnalysis/Event.h"
#include "Root/Event.cxx"
#include "TopNtupleAnalysis/Electron.h"
#include "Root/Electron.cxx"
#include "TopNtupleAnalysis/Muon.h"
#include "Root/Muon.cxx"
#include "TopNtupleAnalysis/Jet.h"
#include "Root/Jet.cxx"
#include "TopNtupleAnalysis/LargeJet.h"
#include "Root/LargeJet.cxx"
#include "TopNtupleAnalysis/MObject.h"
#include "Root/MObject.cxx"

/*
#include "xAODBTaggingEfficiency/BTaggingEfficiencyTool.h"
#include "CalibrationDataInterface/CalibrationDataVariables.h"
#include "CalibrationDataInterface/CalibrationDataInterfaceROOT.h"
#include "PATInterfaces/SystematicRegistry.h"
*/

#include "TLorentzVector.h"
#include <vector>
#include <cstdlib>

class WrapperExtras {
  public:
    TtresNeutrinoBuilder m_neutrinoBuilder;
    TtresChi2 m_chi2;
    WeakCorr::WeakCorrScaleFactorParam m_ewkTool;
    //PMGCorrsAndSysts m_pmg;
	MMUtils m_mm_b0_boosted_e;
	MMUtils m_mm_b1_boosted_e;
	MMUtils m_mm_b0_res_e;
	MMUtils m_mm_b1_res_e;
	MMUtils m_mm_b0_boosted_mu;
	MMUtils m_mm_b1_boosted_mu;
	MMUtils m_mm_b0_res_mu;
	MMUtils m_mm_b1_res_mu;

	//BTaggingEfficiencyTool m_btageff;

    WrapperExtras() : m_neutrinoBuilder("MeV"), m_chi2("MeV"), m_ewkTool("../share/EWcorr_param.root"),
	                  m_mm_b0_boosted_e("../scripts/QCDestimation/110816_realRates_re_inc/eff_ttbar.root", "../scripts/QCDestimation/110816_fakeRates_re_0b/fake.root",
					                    "../scripts/QCDestimation/RATES_2016/resolved_e_eff_ttbar.root", "../scripts/QCDestimation/RATES_2016/resolved_e_btag0_fake.root"), 
	                  m_mm_b1_boosted_e("../scripts/QCDestimation/110816_realRates_re_inc/eff_ttbar.root", "../scripts/QCDestimation/110816_fakeRates_re_in1b/fake.root",
					                    "../scripts/QCDestimation/RATES_2016/resolved_e_eff_ttbar.root", "../scripts/QCDestimation/RATES_2016/resolved_e_btag1_fake.root"), 
	                  m_mm_b0_res_e("../scripts/QCDestimation/110816_realRates_re_inc/eff_ttbar.root", "../scripts/QCDestimation/110816_fakeRates_re_0b/fake.root",
					                    "../scripts/QCDestimation/RATES_2016/resolved_e_eff_ttbar.root", "../scripts/QCDestimation/RATES_2016/resolved_e_btag0_fake.root"), 
	                  m_mm_b1_res_e("../scripts/QCDestimation/110816_realRates_re_inc/eff_ttbar.root", "../scripts/QCDestimation/110816_fakeRates_re_in1b/fake.root",
					                    "../scripts/QCDestimation/RATES_2016/resolved_e_eff_ttbar.root", "../scripts/QCDestimation/RATES_2016/resolved_e_btag1_fake.root"), 

	                  m_mm_b0_boosted_mu("../scripts/QCDestimation/110816_realRates_rmu_inc/eff_ttbar.root", "../scripts/QCDestimation/110816_fakeRates_rmu_0b/fake.root",
					                     "../scripts/QCDestimation/RATES_2016/resolved_mu_eff_ttbar.root", "../scripts/QCDestimation/RATES_2016/resolved_mu_btag0_fake.root"), 
	                  m_mm_b1_boosted_mu("../scripts/QCDestimation/110816_realRates_rmu_inc/eff_ttbar.root", "../scripts/QCDestimation/110816_fakeRates_rmu_in1b/fake.root",
					                     "../scripts/QCDestimation/RATES_2016/resolved_mu_eff_ttbar.root", "../scripts/QCDestimation/RATES_2016/resolved_mu_btag1_fake.root"), 

	                  m_mm_b0_res_mu("../scripts/QCDestimation/110816_realRates_rmu_inc/eff_ttbar.root", "../scripts/QCDestimation/110816_fakeRates_rmu_0b/fake.root",
					                     "../scripts/QCDestimation/RATES_2016/resolved_mu_eff_ttbar.root", "../scripts/QCDestimation/RATES_2016/resolved_mu_btag0_fake.root"), 
	                  m_mm_b1_res_mu("../scripts/QCDestimation/110816_realRates_rmu_inc/eff_ttbar.root", "../scripts/QCDestimation/110816_fakeRates_rmu_in1b/fake.root",
					                     "../scripts/QCDestimation/RATES_2016/resolved_mu_eff_ttbar.root", "../scripts/QCDestimation/RATES_2016/resolved_mu_btag1_fake.root")//, 
					  //m_btageff("BTaggingEfficiencyTool")
					  {
      m_chi2.Init(TtresChi2::DATA2015_MC15C);
	  /*
	  if (!m_btageff.setProperty("TaggerName", "MV2c10")) std::cout << "Failed to set b-tagging property." << std::endl;
	  if (!m_btageff.setProperty("OperatingPoint", "FixedCutBEff_70")) std::cout << "Failed to set b-tagging property." << std::endl;
	  if (!m_btageff.setProperty("JetAuthor", "AntiKt2PV0TrackJets")) std::cout << "Failed to set b-tagging property." << std::endl;
	  if (!m_btageff.setProperty("EfficiencyFileName", "../share/2016-20_7-13TeV-MC15-CDI-June27_v1.root")) std::cout << "Failed to set b-tagging property." << std::endl;
	  if (!m_btageff.setProperty("ScaleFactorFileName", "../share/2016-20_7-13TeV-MC15-CDI-June27_v1.root")) std::cout << "Failed to set b-tagging property." << std::endl;
	  if (!m_btageff.setProperty("ScaleFactorBCalibration", "default")) std::cout << "Failed to set b-tagging property." << std::endl;
	  if (!m_btageff.setProperty("ScaleFactorCCalibration", "default")) std::cout << "Failed to set b-tagging property." << std::endl;
	  if (!m_btageff.setProperty("ScaleFactorTCalibration", "default")) std::cout << "Failed to set b-tagging property." << std::endl;
	  if (!m_btageff.setProperty("ScaleFactorLightCalibration", "default")) std::cout << "Failed to set b-tagging property." << std::endl;
	  if (!m_btageff.setProperty("ExcludeFromEigenVectorTreatment", "")) std::cout << "Failed to set b-tagging property." << std::endl;
	  if (!m_btageff.setProperty("EfficiencyBCalibrations", "410000;410004;410006;410187")) std::cout << "Failed to set b-tagging property." << std::endl;
	  if (!m_btageff.setProperty("EfficiencyCCalibrations", "410000;410004;410006;410187")) std::cout << "Failed to set b-tagging property." << std::endl;
	  if (!m_btageff.setProperty("EfficiencyTCalibrations", "410000;410004;410006;410187")) std::cout << "Failed to set b-tagging property." << std::endl;
	  if (!m_btageff.setProperty("EfficiencyLightCalibrations", "410000;410004;410006;410187")) std::cout << "Failed to set b-tagging property." << std::endl;
	  if (!m_btageff.initialize()) std::cout << "Failed to initialize b-tagging eff." << std::endl;
      CP::SystematicSet s = m_btageff.affectingSystematics();
	  //for (CP::SystematicSet::const_iterator it = s.begin(); it != s.end(); it++) {
	  //  std::cout << "Syst. " << it->name() << std::endl;
	  //}
	  */
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
      ret["chi2"] = chi2Value;
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
	/*
    float getBtaggingSF(std::vector<TLorentzVector> jet, std::vector<int> flavour, std::vector<float> mv2c10, std::vector<bool> vetoSyst, std::string syst = "") {
      m_btageff.setMapIndex("B", 0);
      m_btageff.setMapIndex("C", 0);
      m_btageff.setMapIndex("T", 0);
      m_btageff.setMapIndex("Light", 0);

      float btagsf = 1.0;
      for (int k = 0; k < jet.size(); ++k) {
	    float sf = 1;
		Analysis::CalibrationDataVariables v;
        v.jetPt = jet[k].Perp();
		v.jetEta = jet[k].Eta();
		v.jetTagWeight = mv2c10[k];
		v.jetAuthor = "AntiKt2PV0TrackJets";
		if (vetoSyst[k]) {
	      if (!m_btageff.applySystematicVariation(CP::SystematicSet())) {
	        std::cout << "Could not apply the sys variation " << "" << std::endl;
	  	    exit(-1);
	      }
		} else {
	      if (!m_btageff.applySystematicVariation(CP::SystematicSet(syst))) {
	        std::cout << "Could not apply the sys variation " << syst << std::endl;
	  	    exit(-1);
	      }
		}
		
        if (mv2c10[k] > 0.6455) {
		  if (!m_btageff.getScaleFactor(flavour[k], v, sf)) {
	        std::cout << "Could not get btag SF for " << syst << ", jet pt, eta, weight = " << v.jetPt << ", " << v.jetEta << ", " << v.jetTagWeight << std::endl;
		    exit(-1);
		  }
		} else {
		  if (!m_btageff.getInefficiencyScaleFactor(flavour[k], v, sf)) {
	        std::cout << "Could not get btag ineff. SF for " << syst << ", jet pt, eta, weight = " << v.jetPt << ", " << v.jetEta << ", " << v.jetTagWeight << std::endl;
		    exit(-1);
		  }
		}
		btagsf *= sf;
	  }
	  return btagsf;
    }*/
    double getQCDWeight(int btags, int boosted, TLorentzVector met, TLorentzVector lep, int isTight, std::vector<TLorentzVector> jet, float sd0, int isElectron, int muonTrigger, float topoetcone20, int runNumber) {
	  Event e;
	  e.met(met.Px(), met.Py());
	  if (isElectron) {
	    e.electron().push_back(Electron(lep));
		e.electron()[0].setTightPP(isTight);
		e.electron()[0].topoetcone20() = topoetcone20;
		e.electron()[0].sd0() = sd0;
	  } else {
	    e.muon().push_back(Muon(lep));
		e.muon()[0].sd0() = sd0;
		e.muon()[0].setTight(isTight);
		e.muon()[0].HLT_mu20_iloose_L1MU15() = muonTrigger;
		e.muon()[0].HLT_mu50() = muonTrigger;
	  }
	  for (int k = 0; k < jet.size(); ++k) {
	    e.jet().push_back(Jet(jet[k]));
	  }
	  double w = 0;
	  if (!btags && boosted && isElectron) {
	    w = m_mm_b0_boosted_e.getMMweights(e, 0, isElectron, boosted, runNumber);
	  } else if (btags && boosted && isElectron) {
	    w = m_mm_b1_boosted_e.getMMweights(e, 0, isElectron, boosted, runNumber);
	  } else if (!btags && !boosted && isElectron) {
	    w = m_mm_b0_res_e.getMMweights(e, 0, isElectron, boosted, runNumber);
	  } else if (btags && !boosted && isElectron) {
	    w = m_mm_b1_res_e.getMMweights(e, 0, isElectron, boosted, runNumber);
	  } else if (!btags && boosted && !isElectron) {
	    w = m_mm_b0_boosted_mu.getMMweights(e, 0, isElectron, boosted, runNumber);
	  } else if (btags && boosted && !isElectron) {
	    w = m_mm_b1_boosted_mu.getMMweights(e, 0, isElectron, boosted, runNumber);
	  } else if (!btags && !boosted && !isElectron) {
	    w = m_mm_b0_res_mu.getMMweights(e, 0, isElectron, boosted, runNumber);
	  } else if (btags && !boosted && !isElectron) {
	    w = m_mm_b1_res_mu.getMMweights(e, 0, isElectron, boosted, runNumber);
	  }
	  return w;
	}
};
'''
    ROOT.gInterpreter.ProcessLine("gSystem->AddIncludePath(\" -I../../RootCoreBin/include \") ")
    ROOT.gInterpreter.ProcessLine("gSystem->AddIncludePath(\" -I../ \") ")
    ROOT.gInterpreter.ProcessLine(".include ../../RootCoreBin/include ")
    ROOT.gInterpreter.ProcessLine(".include .. ")
    ROOT.gInterpreter.ProcessLine("gROOT->LoadMacro(\"/cvmfs/atlas.cern.ch/repo/sw/ASG/AnalysisTop/2.4.12/RootCore/scripts/load_packages.C\")")
    ROOT.gInterpreter.ProcessLine("load_packages()");
    ROOT.gInterpreter.ProcessLine("std::cout << 123 << std::endl;");
    ROOT.gInterpreter.ProcessLine(bind_neutrino)
    ROOT.gInterpreter.ProcessLine("std::cout << 456 << std::endl;");
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
    if sel.mcChannelNumber == 0:
        return 1
    ptbinInS = -1
    if 'btag' in s and 'pt' in s:
       ptbinInS = int(s.split('pt')[1][0])

    jetList = ROOT.vector('TLorentzVector')()
    jetFlavour = ROOT.vector('int')()
    jetWeight = ROOT.vector('float')()
    vetoSyst = ROOT.vector('bool')()
    for k in range(0, len(sel.tjet_pt)):
        jetList.push_back(ROOT.TLorentzVector(sel.tjet_pt[k], sel.tjet_eta[k], sel.tjet_phi[k], sel.tjet_e[k]))
        jetFlavour.push_back(int(sel.tjet_label[k]))
        jetWeight.push_back(float(sel.tjet_mv2c10[k]))
        ptbin = -1
        if ptbinInS >= 0:
            if jetList[k].Perp() < 50e3:
                ptbin = 1
            elif jetList[k].Perp() < 100e3:
                ptbin = 2
            else:
                ptbin = 3
        if ptbinInS == ptbin:
            # if this jet is in the correct pt bin, apply the syst. variation
            vetoSyst.push_back(False)
        else:
            # otherwise, take the nominal SF for this jet
            # even if we are supposed to vary it for any other criteria
            vetoSyst.push_back(True)
    syst = ""
    if 'down' in s:
       direction = 'down'
    else:
       direction = 'up'
    eig = -1
    if 'btagbSF_' in s:
        eig = int(s.split('_')[1])
        syst = "FT_EFF_Eigen_B_%d__1%s" % (eig, direction)
    elif 'btagcSF_' in s:
        eig = int(s.split('_')[1])
        syst = "FT_EFF_Eigen_C_%d__1%s" % (eig, direction)
    elif 'btaglSF_' in s:
        eig = int(s.split('_')[1])
        syst = "FT_EFF_Eigen_Light_%d__1%s" % (eig, direction)
    elif 'btageSF_0' in s:
        syst = "FT_EFF_Eigen_extrapolation__1%s" % (direction)
    elif 'btageSF_1' in s:
        syst = "FT_EFF_Eigen_extrapolation from charm__1%s" % (direction)
    return wrapperC.getBtaggingSF(jetList, jetFlavour, jetWeight, vetoSyst, syst)

# same as above, but it reads the SFs from the file
def applyBtagSFFromFile(sel, s):
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
        # get direction
        direction = 'up'
        if 'down' in s:
            direction = 'down'
        # check if it is a b,c,light or extrapolation variation and set name
        if 'btagbSF_' in s:
            varName = pref+'_eigen_B_'+direction
            # get eigenvector index
            eig = int(s.split('_')[1])
        if 'btagcSF_' in s:
            varName = pref+'_eigen_C_'+direction
            # get eigenvector index
            eig = int(s.split('_')[1])
        if 'btaglSF_' in s:
            varName = pref+'_eigen_Light_'+direction
            # get eigenvector index
            eig = int(s.split('_')[1])
        if 'btageSF_0' in s:
            varName = pref+'_syst_extrapolation_'+direction
            eig = -1
        if 'btageSF_1' in s:
            varName = pref+'_syst_extrapolation_from_charm_'+direction
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
            vetoed = False
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
                    vetoed = True
            else: # we have not requested the pt binned variation
                # so we always vary all jets, regardless of the pt bin
                # if no variation was requested, varName will be set to the nominal above
                theWeight = getattr(sel, varName)
            if eig > -1 and not vetoed: # branches in b,c,light variation have a second index related to the eigenvector number
                btagsf *= theWeight[bidx][eig]
            else: # extrapolation branches or the nominal, have no second index
                btagsf *= theWeight[bidx]
    return btagsf

# TODO
def readEvent(mt):
    return mt

listEWK = [410000, 301528, 301529, 301530, 301531, 301532]
def applyEWK(sel, s):
    if sel.mcChannelNumber == 0:
        return 1
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

