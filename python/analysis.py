import helpers
import ROOT
import math
import copy
import os
import ctypes
from array import array
from ROOT import std
import observables
import selections
import wjets
logger = helpers.getLogger('TopNtupleAnalysis.analysis')

class Analysis(object):
    ch = ''
    fi = None
    histSuffixes = [] # systematic copies of histograms
    h = {} # map of histogram names to map of systematics to histograms
    trees = {} # dictionary for debug trees
    branches = {} # dictionary for debug trees branches
    noMttSlices = False
    applyMET = 0
    eftLambda = -1
    eftCvv = 0
    KKgluonWidth = -1
    w2HDM = 1
    me2SM = -1
    me2XX = -1
    alphaS = -1
    tName  = "debug"

    def __init__(self, channel, suf, outputFile, do_tree = False):
        self._outputFile = outputFile
        self.fi = ROOT.TFile.Open(outputFile + '.part', "recreate")
        self.ch = channel
        self.histSuffixes = suf
        self.noMttSlices = False
        self.applyMET = 0
        self.eftLambda = -1
        self.eftCvv = -1
        self.KKgluonWidth = -1
        self.w2HDM = 1
        self.me2SM = -1
        self.me2XX = -1
        self.alphaS = -1
        self._doTree = do_tree
        self.tName  = "mini"
        self.h = {}
        self.trees = {}
        self.branches = {}
        self.branches_noclear = {}
        self.keep = '' # can be 'bb', 'cc', 'bbcc', 'c' or 'l' and only applies to W+jets
        self.observables = [observable.registered(self) for observable in observables.ObservableList]

    @property
    def doTree(self):
        return self._doTree

    @doTree.setter
    def doTree(self, boolean):
        self._doTree = boolean
        if boolean:
            self.addTree()
        else:
            self.trees = {}
            self.branches = {}

    def add(self, hName, nBins, xLow, xHigh):
        self.h[hName] = {}
        #self.fi.cd()
        for s in self.histSuffixes:
            #print "adding histogram with name ", hName+self.ch+s
            self.h[hName][s] = ROOT.TH1D(hName+self.ch+s, "", nBins, xLow, xHigh)
            self.h[hName][s].Sumw2()
            self.h[hName][s].SetDirectory(0)

    def clearBranches(self):
        if not self._doTree: return
        tname = self.tName
        for s in self.histSuffixes:
            for bname in self.branches[tname][s]:
                self.branches[tname][s][bname].clear()

    def addTree(self):
        if not self._doTree:
            return
        tname = self.tName
        self.trees[tname] = {}
        self.branches[tname] = {}
        self.branches_noclear[tname] = {}
        #self.fi.cd()
        for s in self.histSuffixes:
            logger.info("Adding <Tree(\"{}\")>".format(tname+s))
            self.trees[tname][s] = ROOT.TTree(tname+s,tname+s)
            self.trees[tname][s].SetDirectory(0)
            self.branches[tname][s] = {}
            self.branches_noclear[tname][s] = {}

            self.branches[tname][s]["eventNumber"] = std.vector(float)()
            self.trees[tname][s].Branch("eventNumber",self.branches[tname][s]["eventNumber"])
            self.branches[tname][s]["runNumber"] = std.vector(float)()
            self.trees[tname][s].Branch("runNumber",self.branches[tname][s]["runNumber"])
            self.branches[tname][s]["mcChannelNumber"] = std.vector(float)()
            self.trees[tname][s].Branch("mcChannelNumber",self.branches[tname][s]["mcChannelNumber"])
            self.branches[tname][s]["aS"] = std.vector(float)()
            self.trees[tname][s].Branch("aS",self.branches[tname][s]["aS"])
            self.branches[tname][s]["w"] = std.vector(float)()
            self.trees[tname][s].Branch("w",self.branches[tname][s]["w"])
            self.branches[tname][s]["w0"] = std.vector(float)()
            self.trees[tname][s].Branch("w0",self.branches[tname][s]["w0"])
            self.branches[tname][s]["w2HDM"] = std.vector(float)()
            self.trees[tname][s].Branch("w2HDM",self.branches[tname][s]["w2HDM"])
            self.branches[tname][s]["me2SM"] = std.vector(float)()
            self.trees[tname][s].Branch("me2SM",self.branches[tname][s]["me2SM"])
            self.branches[tname][s]["me2XX"] = std.vector(float)()
            self.trees[tname][s].Branch("me2XX",self.branches[tname][s]["me2XX"])
            self.branches[tname][s]["id"] = std.vector(float)()
            self.trees[tname][s].Branch("id",self.branches[tname][s]["id"])
            self.branches[tname][s]["px"] = std.vector(float)()
            self.trees[tname][s].Branch("px",self.branches[tname][s]["px"])
            self.branches[tname][s]["py"] = std.vector(float)()
            self.trees[tname][s].Branch("py",self.branches[tname][s]["py"])
            self.branches[tname][s]["pz"] = std.vector(float)()
            self.trees[tname][s].Branch("pz",self.branches[tname][s]["pz"])
            self.branches[tname][s]["e"] = std.vector(float)()
            self.trees[tname][s].Branch("e",self.branches[tname][s]["e"])
            self.branches[tname][s]["mttReco"] = std.vector(float)()
            self.trees[tname][s].Branch("mttReco",self.branches[tname][s]["mttReco"])
            self.branches[tname][s]["mttTrue"] = std.vector(float)()
            self.trees[tname][s].Branch("mttTrue",self.branches[tname][s]["mttTrue"])

            self.branches_noclear[tname][s]["Btagcat"] = ctypes.c_int()
            self.trees[tname][s].Branch("Btagcat",ctypes.addressof(self.branches_noclear[tname][s]["Btagcat"]), 'Btagcat/I')

    def addVar(self, hName, nBinsList):
        ar = array("d", nBinsList)
        #self.fi.cd()
        self.h[hName] = {}
        for s in self.histSuffixes:
            self.h[hName][s] = ROOT.TH1D(hName+self.ch+s, "", len(nBinsList) - 1, ar)
            self.h[hName][s].Sumw2()
            self.h[hName][s].SetDirectory(0)

    def add2D(self, hName, nBins, xLow, xHigh, nBinsY, yLow, yHigh):
        self.h[hName] = {}
        #self.fi.cd()
        for s in self.histSuffixes:
            #print "adding histogram with name ", hName+self.ch+s
            self.h[hName][s] = ROOT.TH2D(hName+self.ch+s, "", nBins, xLow, xHigh, nBinsY, yLow, yHigh)
            self.h[hName][s].Sumw2()
            self.h[hName][s].SetDirectory(0)

    def write(self):
        self.fi.cd()
        for hName in self.h:
            for s in self.histSuffixes:
                self.h[hName][s].Write(hName+s)
        if self._doTree:
            tname = self.tName+self.ch
            for tname in self.trees:
                for s in self.histSuffixes:
                    self.trees[tname][s].Write(tname+s)
        if(helpers.nameX!=""):
            out_nameX = ROOT.TNamed("nameX",helpers.nameX)
            out_nameX.Write()
            out_mX = ROOT.TVectorF(1)
            out_mX[0] = helpers.mX
            out_mX.Write("mX")
            out_sba = ROOT.TVectorF(1)
            out_sba[0] = helpers.sba
            out_sba.Write("sba")
            out_tanb = ROOT.TVectorF(1)
            out_tanb[0] = helpers.tanb
            out_tanb.Write("tanb")
        self.fi.Close()

    def end(self):
        self.write()
        head, sep, tail = self._outputFile.partition('file://')
        f = tail if head == '' else self._outputFile
        try:
            os.rename(f + '.part', f)
        except OSError as e:
            logger.error(e, exc_info=True)

    def getWeight(self, sel, s):
        # this applies all the weights that come out of the box
        if sel.mcChannelNumber == 0:
            return 1.0
        k = s
        if not s in helpers.weightSF:
            k = ''
        listWeights = helpers.weightSF[k]
        weight = 1.0
        for item in listWeights:
            if 'pileup' in item and not helpers.doPRW:
                continue
            wItem = getattr(sel, 'weight_'+item)
            weight *= wItem

        # this applies the EWK weight
        channel = sel.mcChannelNumber
        if channel in helpers.listEWK and not self.noMttSlices:
            weight *= helpers.applyEWK(sel, s)

        # this applies the W+jets Sherpa 2.2.0 nJets reweighting correction
        # WARNING: disable this if using 2.2.1
        #weight *= sel.weight_Sherpa22_corr

        return weight
    def set_top_tagger(self, expr):
        self.top_tagger = selections.BoostedTopTagger(expr)

    def set_bot_tagger(self, algorithm_WP_systs = 'AntiKt2PV0TrackJets.MV2c10_70'):
        attr = algorithm_WP_systs.split('.',2)
        algorithm_WP_systs = attr[-1].split('_', 2)
        if len(attr)==2:
            algorithm_WP_systs.append(attr[0])
        self.bot_tagger = selections.TrackJetBotTagger(*algorithm_WP_systs)

    def set_TtresChi2(self):
        self.TtresChi2 = selections.TtresChi2(bot_tagger = self.bot_tagger)

class AnaTtresSL(Analysis):
    mapSel = {  # OR all channels in the comma-separated list
                'be': ['bejets_2015','bejets_2016'],
                'bmu': ['bmujets_2015','bmujets_2016'],
                're': ['rejets_2015','rejets_2016'],
                'rmu': ['rmujets_2015','rmujets_2016'],
                'be0': ['bejets_2015','bejets_2016'],
                'bmu0': ['bmujets_2015','bmujets_2016'],
                're0': ['rejets_2015','rejets_2016'],
                'rmu0': ['rmujets_2015','rmujets_2016'],
                'be1': ['bejets_2015','bejets_2016'],
                'bmu1': ['bmujets_2015','bmujets_2016'],
                're1': ['rejets_2015','rejets_2016'],
                'rmu1': ['rmujets_2015','rmujets_2016'],
                'be2': ['bejets_2015','bejets_2016'],
                'bmu2': ['bmujets_2015','bmujets_2016'],
                're2': ['rejets_2015','rejets_2016'],
                'rmu2': ['rmujets_2015','rmujets_2016'],
                'be3': ['bejets_2015','bejets_2016'],
                'bmu3': ['bmujets_2015','bmujets_2016'],
                're3': ['rejets_2015','rejets_2016'],
                'rmu3': ['rmujets_2015','rmujets_2016'],
                'be2015': ['bejets_2015'],
                'bmu2015': ['bmujets_2015'],
                're2015': ['rejets_2015'],
                'rmu2015': ['rmujets_2015'],
                'be2016': ['bejets_2016'],
                'bmu2016': ['bmujets_2016'],
                're2016': ['rejets_2016'],
                'rmu2016': ['rmujets_2016'],
                'ovre': ['rejets_2015','rejets_2016'],
                'ovrmu': ['rmujets_2015','rmujets_2016']}
    def __init__(self, channel, suf, outputFile, do_tree = False):
        Analysis.__init__(self, channel, suf, outputFile, do_tree)
        self.applyQCD = False
        self.noMttSlices = False
        self.applyMET = 0
        self.eftLambda = -1
        self.eftCvv = 0
        self.KKgluonWidth = -1
        self.DMMass = False
        self.w2HDM = 1
        self.me2SM = -1
        self.me2XX = -1
        self.alphaS = -1
        ########################
        ### make debug tree ####
        self.addTree() #########
        ########################
        # make histograms
        self.add("yields", 1, 0.5, 1.5)
        self.add("yieldsPos", 1, 0.5, 1.5)
        self.add("yieldsNeg", 1, 0.5, 1.5)
        self.add("runNumber", 24647, 276261.5, 300908.5)
        self.add("lepPt", 100, 25, 525)
        self.add("lepEta", 20, -2.5, 2.5)
        self.add("lepPhi", 32, -3.2, 3.2)
        self.add("nJets", 10, -0.5, 9.5)
        self.add("nTrkBtagJets", 10, -0.5, 9.5)
        self.addVar("MET", [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 220, 240, 260, 280, 300, 340, 380, 450, 500])
        self.add("MET_phi", 32, -3.2, 3.2)
        self.add("mwt", 20, 0, 200)
        self.add("closestJetDr", 20, 0, 2.0)
        self.add("closestJetPt", 20, 0, 200)
        self.add("mu", 100, 0, 100)
        self.add("vtxz", 40, -400, 400)
        self.add("npv", 50, 0, 50)
        self.addVar("closeJetPt", [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 220, 240, 260, 280, 300, 340, 380, 450, 500])
        self.addVar("largeJetPt", [300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 540, 580, 620, 660, 700, 800, 1e3, 1.2e3, 1.5e3])
        self.add("largeJetM", 30, 0, 300)
        self.add("largeJetPtMtt", 50, 0, 1)
        self.add("largeJetEta", 20, -2., 2.)
        self.add("largeJetPhi", 32, -3.2, 3.2)
        self.addVar("mtlep_boo", [80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 340, 380, 420, 460, 500])
        self.addVar("mtlep_res", [80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 340, 380, 420, 460, 500])
        self.addVar("mthad_res", [80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 340, 380, 420, 460, 500])
        self.add("mwhad_res", 40, 0, 400)
        self.add("chi2", 65, -3, 10)
        #self.addVar("mtt", [0, 80, 160, 240, 320, 400, 480, 560,640,720,800,920,1040,1160,1280,1400,1550,1700,2000,2300,2600,2900,3200,3600,4100,4600,5100,6000])
        self.add("mtt", 600 , 0, 6000)
        self.add("mttr", 600, 0, 6000)
        self.add("mttPos", 600, 0, 6000)
        self.add("mttNeg", 600, 0, 6000)
        self.add("trueMtt", 600, 0, 6000)
        self.add("trueMttr", 600, 0, 6000)
        self.addVar("mtt8TeV", [0,80,160,240,320,360,400,440,500,560,600,640,680,720,760,800,860,920,1040,1160,1280])
        self.addVar("mtt8TeVr",[0,80,160,240,320,360,400,440,500,560,600,640,680,720,760,800,860,920,1040,1160,1280])
        self.addVar("trueMtt8TeV",  [0,80,160,240,320,360,400,440,500,560,600,640,680,720,760,800,860,920,1040,1160,1280])
        self.addVar("trueMtt8TeVr", [0,80,160,240,320,360,400,440,500,560,600,640,680,720,760,800,860,920,1040,1160,1280])
        self.add("largeJet_tau32_wta", 20, 0, 1)
        self.add("largeJet_tau21_wta", 20, 0, 1)
        self.add("btagged_tjet_closest_to_ljet", 50, 0, (math.pi**2+2.5**2)**0.5)
        self.add("btagged_tjet_closest_to_lep", 50, 0, (math.pi**2+2.5**2)**0.5)
        for observable in self.observables:
            if type(observable.binning) == tuple:
                self.add(observable.name, *observable.binning)
            else:
                self.addVar(observable.name, observable.binning)

    # only apply the reco weights
    def getWeight(self, sel, s):
        if sel.mcChannelNumber == 0:
            return 1.0
        weight = Analysis.getWeight(self, sel, s)

        # just add the btagging SFs on top of those, as this Analysis implementation applies b-tagging
        #### warning: disabled for now in mc15c
        btagsf = self.bot_tagger.scale_factor(sel)
        weight *= btagsf

        if s == "singletopup" and sel.mcChannelNumber in [410011, 410012, 410013, 410014, 410015, 410016, 410025, 410026]:
            weight *= 1+0.053
        if s == "singletopdw" and sel.mcChannelNumber in [410011, 410012, 410013, 410014, 410015, 410016, 410025, 410026]:
            weight *= 1-0.053
        if s == "ttxsecup" and sel.mcChannelNumber in [410000, 301528, 301529, 301530, 301531, 301532]:
            weight *= 1+0.056
        if s == "ttxsecdw" and sel.mcChannelNumber in [410000, 301528, 301529, 301530, 301531, 301532]:
            weight *= 1-0.061

        # for EFT
        if self.eftLambda > 0:
            weight *= helpers.getEFTSMWeight(sel, s)

        # for KK gluon width reweighting
        if self.KKgluonWidth > 0:
            weight *= helpers.getKKgluonWidthWeight(self.KKgluonWidth, sel, s)
        # for DM reweighting
        if self.DMMass:
            weight *= helpers.getDMWeight(sel)

        # for 2HDM
        self.w2HDM = 1
        self.me2SM = -1
        self.me2XX = -1
        self.alphaS = -1
        if(helpers.nameX != ""):
            self.w2HDM,self.me2SM,self.me2XX,self.alphaS = helpers.get2HDMWeight(sel)
            weight *= self.w2HDM

        # W+jets C/A and HF syst. variations
        # assuming b-tagging
        hfweight = 1.0
        f_ca = 1.0

        nj = 4
        if len(sel.jet_pt) > 4:
            nj = 5
        if len(sel.jet_pt) < 2:
            nj = 2

        # flavour fractions at pretag level
        frac2 = {}
        frac2[2] = {'el': {}, 'mu': {}}
        frac2[3] = {'el': {}, 'mu': {}}
        frac2[4] = {'el': {}, 'mu': {}}
        frac2[5] = {'el': {}, 'mu': {}}

        chan = 'not-exactly-one-charged-lepton'
        if len(sel.el_pt) == 1:
            chan = 'el'
        elif len(sel.mu_pt) == 1:
            chan = 'mu'
        syst = ""
        if s in wjets.flav_map[nj][chan]: # You should always have exactly one electron or muon in a good event. It usually means the event selections are problematic (i.e. not exactly one electron or muon) if you get an error from here.
            syst = s

        frac2[nj][chan][syst] = copy.deepcopy(wjets.frac[nj][chan][syst])
        for f in frac2[nj][chan][syst]:
            frac2[nj][chan][syst][f] *= wjets.flav_map[nj][chan][syst][f]

        flav = ''
        if sel.mcChannelNumber in helpers.listWjets22:
            flag = sel.Wfilter_Sherpa_nT
            if flag == 3 or flag == 4:
                flav = 'bb'
            elif flag == 1:
                flav = 'cc'
            elif flag == 2:
                flav = 'c'
            elif flag == 5:
                flav = 'l'
            f_ca = wjets.f_ca_map[nj][chan][syst]
            norm = 1.0
            hfweight = wjets.flav_map[nj][chan][syst][flav]
            norm = 0
            for f in ['bb', 'cc', 'c', 'l']:
                norm += frac2[nj][chan][syst][f]
            hfweight /= norm
            weight *= f_ca*hfweight
        return weight

    def qcdWeight(self, sel, syst):
        if sel.mcChannelNumber != 0:
            return 1

        nBtag = sum(helpers.char2int(jet_isbtagged) for jet_isbtagged in self.bot_tagger.jet_isbtagged)
        isBoosted = 0
        #if 'be' in self.ch or 'bmu' in self.ch:
        #       isBoosted = 1

        met = ROOT.TLorentzVector()
        met.SetPtEtaPhiE(sel.met_met, 0, sel.met_phi, sel.met_met)
        l = ROOT.TLorentzVector()
        lisTight = 0
        lsd0 = 0
        isElectron = 0
        muonTrigger = 0
        topoetcone20 = 0
        runNumber = sel.runNumber
        if len(sel.el_pt) == 1:
            l.SetPtEtaPhiE(sel.el_pt[0], sel.el_eta[0], sel.el_phi[0], sel.el_e[0])
            lisTight = sel.el_isTight[0]
            lisTight = bool(int(lisTight.encode('hex'), 16))
            lsd0 = sel.el_d0sig[0]
            topoetcone20 = sel.el_topoetcone20[0]
            isElectron = 1
        elif len(sel.mu_pt) == 1:
            l.SetPtEtaPhiE(sel.mu_pt[0], sel.mu_eta[0], sel.mu_phi[0], sel.mu_e[0])
            lisTight = sel.mu_isTight[0]
            lisTight = bool(int(lisTight.encode('hex'), 16))
            lsd0 = sel.mu_d0sig[0]
            muonTrigger = bool(int(sel.mu_trigMatch_HLT_mu20_iloose_L1MU15[0].encode('hex'), 16)) or bool(int(sel.mu_trigMatch_HLT_mu50[0].encode('hex'), 16))
            topoetcone20 = sel.mu_topoetcone20[0]
        jets = ROOT.vector('TLorentzVector')()
        for k in range(0, len(sel.jet_pt)):
            j = ROOT.TLorentzVector()
            j.SetPtEtaPhiE(sel.jet_pt[k], sel.jet_eta[k], sel.jet_phi[k], sel.jet_e[k])
            jets.push_back(j)
        w = ROOT.TopNtupleAnalysis.getQCDWeight(nBtag, isBoosted, met, l, lisTight, jets, lsd0, isElectron, muonTrigger, topoetcone20, runNumber)
        if   math.fabs(l.Eta()) <= 1.5 and 'qcdcenup' in syst: w *= 1.5
        elif math.fabs(l.Eta()) <= 1.5 and 'qcdcendw' in syst: w *= 0.5
        elif math.fabs(l.Eta()) > 1.5 and 'qcdfwdup' in syst: w *= 2.0
        elif math.fabs(l.Eta()) > 1.5 and 'qcdfwddw' in syst: w *= 0
        return w

    def selectChannel(self, sel, syst):
        if self.ch not in self.mapSel:
            logger.warn('The selected channel "{}" is not registered. The events will be processed anyway without any further constraint.'.format(self.ch))
            self.mapSel[self.ch] = [self.ch]
        passSel = {}
        for i, listSel in self.mapSel.iteritems():
            passSel[i] = True
            passORChannels = False
            for item in listSel:
                if self.applyQCD == "e" and "mujets" in item:
                    continue
                elif self.applyQCD == "mu" and "ejets" in item:
                    continue
                hardPass = True
                #if 'be' in i or 'bmu' in i:
                #       hardPass = False
                #       for k in range(0, len(sel.ljet_pt)):
                #               if sel.ljet_good[k] and sel.ljet_pt[k] > 300e3:
                #                       hardPass = True
                #                       break
                passChannel = getattr(sel, item, False)
                if passChannel and hardPass:
                    passORChannels = True
                    break
            passSel[i] = passORChannels

        if not passSel[self.ch]:
            return False

        if not self.bot_tagger.passes(sel):
            return False
        # veto resolved event if it passes the boosted channel
        top_tagged = self.top_tagger.passes(sel)

        if ('re' in self.ch or 'rmu' in self.ch):
            self.TtresChi2.passes(sel)
            Btagcat = self.TtresChi2.bcategory
        else:
            Btagcat = sel.Btagcat

        if ('re' in self.ch or 'rmu' in self.ch) and not "ov" in self.ch:
            if (passSel['be'] or passSel['bmu']) and top_tagged:
                return False

        if self.ch in ['be0', 'bmu0', 're0', 'rmu0']:
            if Btagcat != 0:
                return False
        if self.ch in ['be1', 'bmu1', 're1', 'rmu1']:
            if Btagcat != 1:
                return False
        if self.ch in ['be2', 'bmu2', 're2', 'rmu2']:
            if Btagcat != 2:
                return False
        if self.ch in ['be3', 'bmu3', 're3', 'rmu3']:
            if Btagcat != 3:
                return False

        # veto events in nominal ttbar overlapping with the mtt sliced samples
        # commented now as it is not available in mc15c
        if sel.mcChannelNumber == 410000 and hasattr(sel, "MC_ttbar_beforeFSR_m") and not self.noMttSlices:
            if sel.MC_ttbar_beforeFSR_m > 1.1e6:
                return False
        return True


    def run(self, sel, syst, wo, wTruth):

        ########################
        self.clearBranches() ###
        ########################

        if sel.mcChannelNumber in helpers.listWjets22:
            flag = sel.Wfilter_Sherpa_nT
            if self.keep == 'bb':
                if flag != 3 and flag != 4:
                    return
            if self.keep == 'cc':
                if flag != 1:
                    return
            if self.keep == 'bbcc':
                if flag != 3 and flag != 4 and flag != 1:
                    return
            if self.keep == 'c':
                if flag != 2:
                    return
            if self.keep == 'l':
                if flag != 5:
                    return

        w = wo

        if self.applyQCD:
            w *= self.qcdWeight(sel, syst)
        if self.applyMET > 0 and not ('be' in self.ch or 'bmu' in self.ch):
            if sel.met_met*1e-3 < self.applyMET:
                return

        if(sel.mcChannelNumber != 0 and hasattr(sel, "MC_ttbar_beforeFSR_m") and sel.mcChannelNumber not in [407200, 407201, 407202, 407203, 407204]):
            w0 = w/self.w2HDM
            self.h["trueMtt"][syst].Fill(sel.MC_ttbar_beforeFSR_m*1e-3, w)
            self.h["trueMttr"][syst].Fill(sel.MC_ttbar_beforeFSR_m*1e-3, w0*(self.w2HDM-1.))
            self.h["trueMtt8TeV"][syst].Fill(sel.MC_ttbar_beforeFSR_m*1e-3, w)
            self.h["trueMtt8TeVr"][syst].Fill(sel.MC_ttbar_beforeFSR_m*1e-3, w0*(self.w2HDM-1.))
        if(sel.mcChannelNumber in [407200, 407201, 407202, 407203, 407204]):
            pME = helpers.getTruth4momenta(sel)
            truPttbar = pME[2]+pME[3]
            w0 = w/self.w2HDM
            self.h["trueMtt"][syst].Fill(truPttbar.M(), w)
            self.h["trueMttr"][syst].Fill(truPttbar.M(), w0*(self.w2HDM-1.))
            self.h["trueMtt8TeV"][syst].Fill(truPttbar.M(), w)
            self.h["trueMtt8TeVr"][syst].Fill(truPttbar.M(), w0*(self.w2HDM-1.))
        self.h["yields"][syst].Fill(1, w)
        self.h["runNumber"][syst].Fill(sel.runNumber, w)
        l = ROOT.TLorentzVector()
        lj = ROOT.TLorentzVector()
        tlep = ROOT.TLorentzVector()
        lQ = 0
        if len(sel.el_pt) == 1:
            l.SetPtEtaPhiE(sel.el_pt[0], sel.el_eta[0], sel.el_phi[0], sel.el_e[0])
            lQ = sel.el_charge[0]
        elif len(sel.mu_pt) == 1:
            l.SetPtEtaPhiE(sel.mu_pt[0], sel.mu_eta[0], sel.mu_phi[0], sel.mu_e[0])
            lQ = sel.mu_charge[0]
        if lQ > 0:
            self.h["yieldsPos"][syst].Fill(1, w)
        elif lQ < 0:
            self.h["yieldsNeg"][syst].Fill(1, w)
        self.h["lepPt"][syst].Fill(l.Perp()*1e-3, w)
        self.h["lepEta"][syst].Fill(l.Eta(), w)
        self.h["lepPhi"][syst].Fill(l.Phi(), w)
        self.h["MET_phi"][syst].Fill(sel.met_phi, w)
        self.h["MET"][syst].Fill(sel.met_met*1e-3, w)
        self.h["nJets"][syst].Fill(len(sel.jet_pt), w)
        closestJetIdx = -1
        closestJetPt = 0
        closestJetDr = 99
        for i in range(0, len(sel.jet_pt)):
            cj = ROOT.TLorentzVector()
            cj.SetPtEtaPhiE(sel.jet_pt[i], sel.jet_eta[i], sel.jet_phi[i], sel.jet_e[i])
            dy = (cj.Rapidity() - l.Rapidity())
            dp = cj.DeltaPhi(l)
            dr = (dy**2 + dp**2)**0.5
            if dr < closestJetDr:
                closestJetIdx = i
                closestJetDr = dr
                closestJetPt = cj.Perp()

        btagged_tjet_closest_to_lep = min((tjet for i, tjet in enumerate(self.bot_tagger._tjet_p4) if helpers.char2int(self.bot_tagger.tjet_isbtagged[i])), key = lambda btagged_tjet: btagged_tjet.DeltaR(l))
        self.h["btagged_tjet_closest_to_lep"][syst].Fill(btagged_tjet_closest_to_lep.DeltaR(l), w)
        self.h["closestJetDr"][syst].Fill(closestJetDr, w)
        self.h["closestJetPt"][syst].Fill(closestJetPt*1e-3, w)
        self.h["nTrkBtagJets"][syst].Fill(sum(helpers.char2int(tjet_isbtagged) for tjet_isbtagged in self.bot_tagger.tjet_isbtagged), w)
        self.h["mwt"][syst].Fill(math.sqrt(2*l.Perp()*sel.met_met*(1 - math.cos(l.Phi() - sel.met_phi)))*1e-3, w)
        self.h["mu"][syst].Fill(sel.mu, w)
        self.h["npv"][syst].Fill(sel.npv, w)
        self.h["vtxz"][syst].Fill(sel.vtxz, w)
        ##TLorentzVector getNu(TLorentzVector l, double met, double met_phi) {
        ##double getMtt(TLorentzVector lep, std::vector<TLorentzVector> jets, std::vector<bool> btag, TLorentzVector met) {
        nu = ROOT.TopNtupleAnalysis.getNu(l, sel.met_met, sel.met_phi)
        if ('be' in self.ch or 'bmu' in self.ch) and self.top_tagger.passed:
            for i in range(len(sel.jet_pt)):
                if sel.jet_closeToLepton[i]:
                    closeJetIdx = i
                    break
            
            goodJetIdx = self.top_tagger.thad_index
            lj.SetPtEtaPhiM(sel.ljet_pt[goodJetIdx], sel.ljet_eta[goodJetIdx], sel.ljet_phi[goodJetIdx], sel.ljet_m[goodJetIdx])
            closeJet = ROOT.TLorentzVector()
            closeJet.SetPtEtaPhiE(sel.jet_pt[closeJetIdx], sel.jet_eta[closeJetIdx], sel.jet_phi[closeJetIdx], sel.jet_e[closeJetIdx])
            btagged_tjet_closest_to_ljet = min((tjet for i, tjet in enumerate(self.bot_tagger._tjet_p4) if helpers.char2int(self.bot_tagger.tjet_isbtagged[i])), key = lambda btagged_tjet: btagged_tjet.DeltaR(lj))
            w0 = w/self.w2HDM
            tlep = closeJet+nu+l
            mtt = (tlep+lj).M()*1e-3 # unit is GeV
            self.h["largeJetPt"][syst].Fill(lj.Perp()*1e-3, w)
            self.h["largeJetM"][syst].Fill(lj.M()*1e-3, w)
            self.h["largeJetEta"][syst].Fill(lj.Eta(), w)
            self.h["largeJetPhi"][syst].Fill(lj.Phi(), w)
            self.h["largeJet_tau32_wta"][syst].Fill(sel.ljet_tau32_wta[goodJetIdx], w)
            self.h["largeJet_tau21_wta"][syst].Fill(sel.ljet_tau21_wta[goodJetIdx], w)
            self.h["mtlep_boo"][syst].Fill(tlep.M()*1e-3, w)
            self.h["mtt"][syst].Fill(mtt, w)
            self.h["btagged_tjet_closest_to_ljet"][syst].Fill(btagged_tjet_closest_to_ljet.DeltaR(lj), w)
            self.h["mttr"][syst].Fill(mtt, w0*(self.w2HDM-1.))
            self.h["mtt8TeV"][syst].Fill(mtt, w)
            self.h["mtt8TeVr"][syst].Fill(mtt, w0*(self.w2HDM-1.))
            if lQ > 0:
                self.h["mttPos"][syst].Fill(mtt, w)
            elif lQ < 0:
                self.h["mttNeg"][syst].Fill(mtt, w)
            self.h["largeJetPtMtt"][syst].Fill(lj.Perp()/(mtt*1e3), w)
            
            ################################
            ### fill the tree ##############
            if self._doTree:
                tname = self.tName
                self.branches[tname][syst]["eventNumber"].push_back(sel.eventNumber)
                self.branches[tname][syst]["runNumber"].push_back(sel.runNumber)
                self.branches[tname][syst]["mcChannelNumber"].push_back(sel.mcChannelNumber)
                self.branches[tname][syst]["aS"].push_back(self.alphaS)
                self.branches[tname][syst]["w"].push_back(w)
                self.branches[tname][syst]["w0"].push_back(w0)
                self.branches[tname][syst]["w2HDM"].push_back(self.w2HDM)
                self.branches[tname][syst]["me2SM"].push_back(self.me2SM)
                self.branches[tname][syst]["me2XX"].push_back(self.me2XX)
                self.branches[tname][syst]["mttReco"].push_back(mtt)
                self.branches_noclear[tname][syst]["Btagcat"].value = sel.Btagcat
                # pME = helpers.getTruth4momenta(sel)
                # truPttbar = pME[2]+pME[3]
                if sel.mcChannelNumber != 0:
                    self.branches[tname][syst]["mttTrue"].push_back(sel.MC_ttbar_beforeFSR_m*1e-3)
                # for i in xrange(sel.MC_id_me.size()):
                #     self.branches[tname][syst]["id"].push_back(sel.MC_id_me[i])
                #     self.branches[tname][syst]["px"].push_back(sel.MC_px_me[i])
                #     self.branches[tname][syst]["py"].push_back(sel.MC_py_me[i])
                #     self.branches[tname][syst]["pz"].push_back(sel.MC_pz_me[i])
                #     self.branches[tname][syst]["e"].push_back(sel.MC_e_me[i])
                ##################################
                ### fill the tree ################
                self.trees[tname][syst].Fill() ###
                ##################################
        elif 're' in self.ch or 'rmu' in self.ch:
            if len(sel.ljet_pt) >= 1:
                lj.SetPtEtaPhiM(sel.ljet_pt[0], sel.ljet_eta[0], sel.ljet_phi[0], sel.ljet_m[0])
                btagged_tjet_closest_to_ljet = min((tjet for i, tjet in enumerate(self.bot_tagger._tjet_p4) if helpers.char2int(self.bot_tagger.tjet_isbtagged[i])), key = lambda btagged_tjet: btagged_tjet.DeltaR(lj))
                self.h["largeJetPt"][syst].Fill(lj.Perp()*1e-3, w)
                self.h["largeJetM"][syst].Fill(lj.M()*1e-3, w)
                self.h["largeJetEta"][syst].Fill(lj.Eta(), w)
                self.h["largeJetPhi"][syst].Fill(lj.Phi(), w)
                self.h["largeJet_tau32_wta"][syst].Fill(sel.ljet_tau32_wta[0], w)
                self.h["largeJet_tau21_wta"][syst].Fill(sel.ljet_tau21_wta[0], w)
                self.h["btagged_tjet_closest_to_ljet"][syst].Fill(btagged_tjet_closest_to_ljet.DeltaR(lj), w)
            self.h["btagged_tjet_closest_to_lep"][syst].Fill(btagged_tjet_closest_to_lep.DeltaR(l), w)
            w0 = w/self.w2HDM
            mtt = self.TtresChi2.mtt
            self.h["mtt"][syst].Fill(mtt, w)
            self.h["mttr"][syst].Fill(mtt, w0*(self.w2HDM-1.))
            self.h["mtt8TeV"][syst].Fill(mtt, w)
            self.h["mtt8TeVr"][syst].Fill(mtt, w0*(self.w2HDM-1.))
            if lQ > 0:
                self.h["mttPos"][syst].Fill(mtt, w)
            elif lQ < 0:
                self.h["mttNeg"][syst].Fill(mtt, w)
            self.h["mtlep_res"][syst].Fill(self.TtresChi2.mtl, w)
            self.h["mthad_res"][syst].Fill(self.TtresChi2.mth, w)
            self.h["mwhad_res"][syst].Fill(self.TtresChi2.mwh, w)
            self.h["chi2"][syst].Fill(self.TtresChi2.chi2, w)
            ################################
            ### fill the tree ##############
            if self._doTree:
                tname = self.tName
                self.branches[tname][syst]["eventNumber"].push_back(sel.eventNumber)
                self.branches[tname][syst]["runNumber"].push_back(sel.runNumber)
                self.branches[tname][syst]["mcChannelNumber"].push_back(sel.mcChannelNumber)
                self.branches[tname][syst]["aS"].push_back(self.alphaS)
                self.branches[tname][syst]["w"].push_back(w)
                self.branches[tname][syst]["w0"].push_back(w0)
                self.branches[tname][syst]["w2HDM"].push_back(self.w2HDM)
                self.branches[tname][syst]["me2SM"].push_back(self.me2SM)
                self.branches[tname][syst]["me2XX"].push_back(self.me2XX)
                self.branches[tname][syst]["mttReco"].push_back(mtt)
                self.branches_noclear[tname][syst]["Btagcat"].value = self.TtresChi2.bcategory
                if sel.mcChannelNumber != 0:
                    if not (helpers.nameX!="" and sel.mcChannelNumber in [407200, 407201, 407202, 407203, 407204]):
                        self.branches[tname][syst]["mttTrue"].push_back(sel.MC_ttbar_beforeFSR_m*1e-3)
                    else:
                        pME = helpers.getTruth4momenta(sel)
                        truPttbar = pME[2]+pME[3]
                        self.branches[tname][syst]["mttTrue"].push_back(truPttbar.M())
                        for i in xrange(sel.MC_id_me.size()):
                            self.branches[tname][syst]["id"].push_back(sel.MC_id_me[i])
                            self.branches[tname][syst]["px"].push_back(sel.MC_px_me[i])
                            self.branches[tname][syst]["py"].push_back(sel.MC_py_me[i])
                            self.branches[tname][syst]["pz"].push_back(sel.MC_pz_me[i])
                            self.branches[tname][syst]["e"].push_back(sel.MC_e_me[i])
                ##################################
                ### fill the tree ################
                self.trees[tname][syst].Fill() ###
                ##################################
        for observable in self.observables:
            if observable.only != None:
                if not any (only in self.ch for only in observable.only):
                    break
            values = observable( _locals = locals())
            if observable.style == 'foreach':
                for v in values:
                    self.h[observable.name][syst].Fill(v, w)
            else:
                self.h[observable.name][syst].Fill(values, w)

