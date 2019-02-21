import re
import helpers
import ROOT
import math
import os
import ctypes
from array import array
from ROOT import std
import observables
import selections
import reweighting
logger = helpers.getLogger('TopNtupleAnalysis.analysis')

GeV = 1e-3
DeltaR = ROOT.Math.VectorUtil.DeltaR
DeltaPhi = ROOT.Math.VectorUtil.DeltaPhi

UNLOCKED = 0
SELECTION_LOCKED = 1
FILL_LOCKED = 2

class Analysis(object):
    ch = ''
    fi = None
    histSuffixes = [] # systematic copies of histograms
    treeSuffixes = {}
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
    blinded = False
    mapSel = {}
    prog_bcatN = re.compile(r"^(?P<region>[a-zA-Z]+?)(?P<bcat_or_period>([+-]?(\d+(\.\d+)?|\.\d+)([eE][+-]?\d+)?|))$")

    def __init__(self, channel, systgroups, outputFile, do_tree = False):
        self._outputFile = outputFile
        self.fi = ROOT.TFile.Open(outputFile + '.part', "recreate")
        self.ch = channel
        channel_match = self.prog_bcatN.match(channel)
        if channel_match:
            channel_match = channel_match.groupdict()
            self.region = channel_match['region']
            if len(channel_match['bcat_or_period']) == 4 and channel_match['bcat_or_period'].isalnum():
                self.period = int(channel_match['bcat_or_period'])
                self.bcategory = None
            else:
                self.bcategory = int(channel_match['bcat_or_period']) if channel_match['bcat_or_period'] else None
                self.period = None
        self.systgroups = systgroups
        self.histSuffixes =[]
        self.treeSuffixes ={}
        for systgroup in systgroups:
            self.histSuffixes.extend(s.hist_suffix for s in systgroup.systematics)
            self.treeSuffixes[systgroup.tree] = [s.hist_suffix for s in systgroup.systematics]
        self.noMttSlices = False
        self.doEWKCorrection = True
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
        # make histograms
        self.add('NEvents', 1, 0.5, 1.5)
        self.add("yields", 1, 0.5, 1.5)
        self.add('finalNEvents', 1, 0.5, 1.5)
        self.add('finalYields', 1, 0.5, 1.5)
        self.add("runNumber", 24647, 276261.5, 300908.5)
        self.add("nJets", 10, -0.5, 9.5)
        self.add("nTrkBtagJets", 10, -0.5, 9.5)
        self.addVar("MET", [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 220, 240, 260, 280, 300, 340, 380, 450, 500])
        self.add("MET_phi", 32, -3.2, 3.2)
        self.add("mu", 100, 0, 100)
        self.add("vtxz", 40, -400, 400)
        self.add("npv", 50, 0, 50)
        self.add("runNumber", 24647, 276261.5, 300908.5)
        ### boosted channel ###
        self.add("nlargeJets", 10, -0.5, 9.5)
        ### mass spectrum ###
        self.add("mtt", 600 , 0, 6000)
        self.add("mttr", 600, 0, 6000)
        self.add("trueMtt", 600, 0, 6000)
        self.add("trueMttr", 600, 0, 6000)
        self.addVar("mtt8TeV", [0,80,160,240,320,360,400,440,500,560,600,640,680,720,760,800,860,920,1040,1160,1280])
        self.addVar("mtt8TeVr",[0,80,160,240,320,360,400,440,500,560,600,640,680,720,760,800,860,920,1040,1160,1280])
        self.addVar("trueMtt8TeV",  [0,80,160,240,320,360,400,440,500,560,600,640,680,720,760,800,860,920,1040,1160,1280])
        self.addVar("trueMtt8TeVr", [0,80,160,240,320,360,400,440,500,560,600,640,680,720,760,800,860,920,1040,1160,1280])
        self._locked = UNLOCKED # this locks the selectors to avoid rerun all the selections for the same events with different systematics # 0: unlocked 1: selection locked 2: tree locked
        self._passed = False
        self.observables = [observable.registered(self) for observable in observables.ObservableList if ((observable.only is None) or any(only in self.ch for only in observable.only))]
        for observable in self.observables:
            if 'hist' in observable.do:
                if type(observable.binning) == tuple:
                    self.add(observable.name, *observable.binning)
                else:
                    self.addVar(observable.name, observable.binning)

    def unlock(self):
        self._locked = UNLOCKED

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
        for k, branches in self.branches.iteritems():
            if k.startswith('common'):
                if self._locked < FILL_LOCKED:
                    for branch in branches.itervalues():
                        branch.clear()
            else:
                branches['w'].clear()
                branches['w0'].clear()

    def addTree(self):
        if not self._doTree:
            return
        self.trees = {}
        self.branches = {}
        self.branches_noclear = {}
        #self.fi.cd()
        for t, systs in self.treeSuffixes.iteritems():
            trunk = 'common_'+t
            self.branches[trunk] = {}
            branches_noclear = {}
            for s in systs:
                out_tname = self.tName+s
                logger.info("Adding <Tree(\"{}\")>".format(out_tname))
                self.trees[s] = ROOT.TTree(out_tname, out_tname)
                self.trees[s].SetDirectory(0)
                self.branches[s] = {}
                self.branches_noclear[s] = {}

                self.branches[s]["w"] = std.vector(float)()
                self.trees[s].Branch("w", self.branches[s]["w"])
                self.branches[s]["w0"] = std.vector(float)()
                self.trees[s].Branch("w0", self.branches[s]["w0"])

                self.branches[s]["eventNumber"] = self.branches[trunk].setdefault("eventNumber", std.vector(long)())
                self.trees[s].Branch("eventNumber",self.branches[s]["eventNumber"])
                self.branches[s]["runNumber"] = self.branches[trunk].setdefault("runNumber", std.vector(long)())
                self.trees[s].Branch("runNumber",self.branches[s]["runNumber"])
                self.branches[s]["mcChannelNumber"] = self.branches[trunk].setdefault("mcChannelNumber", std.vector(float)())
                self.trees[s].Branch("mcChannelNumber",self.branches[s]["mcChannelNumber"])
                self.branches[s]["aS"] = self.branches[trunk].setdefault("aS", std.vector(float)())
                self.trees[s].Branch("aS",self.branches[s]["aS"])

                self.branches[s]["w2HDM"] = self.branches[trunk].setdefault("w2HDM", std.vector(float)())
                self.trees[s].Branch("w2HDM",self.branches[s]["w2HDM"])
                self.branches[s]["me2SM"] = self.branches[trunk].setdefault("me2SM", std.vector(float)())
                self.trees[s].Branch("me2SM",self.branches[s]["me2SM"])
                self.branches[s]["me2XX"] = self.branches[trunk].setdefault("me2XX", std.vector(float)())
                self.trees[s].Branch("me2XX",self.branches[s]["me2XX"])
                self.branches[s]["id"] = self.branches[trunk].setdefault("id", std.vector(float)())
                self.trees[s].Branch("id",self.branches[s]["id"])
                self.branches[s]["px"] = self.branches[trunk].setdefault("px", std.vector(float)())
                self.trees[s].Branch("px",self.branches[s]["px"])
                self.branches[s]["py"] = self.branches[trunk].setdefault("py", std.vector(float)())
                self.trees[s].Branch("py",self.branches[s]["py"])
                self.branches[s]["pz"] = self.branches[trunk].setdefault("pz", std.vector(float)())
                self.trees[s].Branch("pz",self.branches[s]["pz"])
                self.branches[s]["e"] = self.branches[trunk].setdefault("e", std.vector(float)())
                self.trees[s].Branch("e",self.branches[s]["e"])
                self.branches[s]["mttReco"] = self.branches[trunk].setdefault("mttReco", std.vector(float)())
                self.trees[s].Branch("mttReco",self.branches[s]["mttReco"])
                self.branches[s]["mttTrue"] = self.branches[trunk].setdefault("mttTrue", std.vector(float)())
                self.trees[s].Branch("mttTrue",self.branches[s]["mttTrue"])

                self.branches_noclear[s]["Btagcat"] = branches_noclear.setdefault("Btagcat", ctypes.c_int())
                self.trees[s].Branch("Btagcat",ctypes.addressof(self.branches_noclear[s]["Btagcat"]), 'Btagcat/I')

                for observable in self.observables:
                    if 'tree' in observable.do:
                        if observable.style == 'foreach':
                            self.branches[s][observable.name] = self.branches[trunk].setdefault(observable.name, std.vector(observable.dtype)())
                            self.trees[s].Branch(observable.name, self.branches[s][observable.name])
                        else:
                            self.branches_noclear[s][observable.name] = branches_noclear.setdefault(observable.name, getattr(ctypes, 'c_' + str(observable.dtype.__name__))())
                            self.trees[s].Branch(observable.name, ctypes.addressof(self.branches_noclear[s][observable.name]), observable.name + ('/I' if observable.dtype == int else '/F'))





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
            for tname in sorted(self.trees.iterkeys()):
                if tname != 'common':
                    self.trees[tname].Write(self.tName+tname)
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
        logger.info('Channel("{}")'.format(self.ch))
        meta = []
        if self.region:
            meta.append('Region: {}'.format(self.region))
        if self.period:
            meta.append('Period: {}'.format(self.period))
        if self.bcategory != None:
            meta.append('B-tagging Categroy: {}'.format(self.bcategory))
        logger.info('\t' + ' | '.join(meta))
        for histName in self.h:
            for s in self.histSuffixes:
                if self.h[histName][s].GetEntries() == 0:
                    logger.debug('\tUnfilled HIST({}<{}>)!'.format(histName, s))

        y_err = ROOT.Double()
        for s in self.histSuffixes:
            h = self.h['finalNEvents'][s]
            logger.info("\tFinal NEvents <{syst}>: {y}".format(syst = s, y = h.Integral()))
            h = self.h['finalYields'][s]
            logger.info("\tFinal Yields <{syst}>: {y:.4g}+/-{y_err:.2g}".format(syst = s, y = h.IntegralAndError(0, h.GetNbinsX()+1, y_err), y_err = y_err))
        self.write()
        head, sep, tail = self._outputFile.partition('file://')
        f = tail if head == '' else self._outputFile
        try:
            os.rename(f + '.part', f)
        except OSError as e:
            logger.error(e, exc_info=True)

    def _selectChannel(self, sel, syst):
        raise NotImplementedError

    def selectChannel(self, sel, syst):
        if self._locked != UNLOCKED: # this locks the selectors to avoid rerun all the selections for the same events with different systematics
            # logger.info('<{}, {}> cached'.format(sel, syst))
            return self._passed
        # logger.info('<{}, {}> new one'.format(sel, syst))
        self._passed = self._selectChannel(sel, syst)
        self._locked = SELECTION_LOCKED
        return self._passed

    def _run(self, sel, syst, wo, wTruth):
        raise NotImplementedError

    def run(self, sel, syst, wo, wTruth):
        assert self._locked != UNLOCKED, '`run` can be only executed after `selectChannel`'
        self._run(sel, syst, wo, wTruth)
        self._locked = FILL_LOCKED

    def getWeight(self, sel, s):
        # this applies all the weights that come out of the box
        if sel.mcChannelNumber == 0:
            return 1.0
        weight = 1.0
        syst_name = s.name
        for item in s.weight_map:
            weight *= getattr(sel, item)
        # this applies the EWK weight to _only_ ttbar samples
        if self.doEWKCorrection:
            weight *= reweighting.EWKCorrection.get_weight(sel, syst_name)
        # this compute the NNLO systematics to _only_ ttbar samples
        weight *= reweighting.NNLOReweighting.get_weight(sel, syst_name)
        # just add the btagging SFs on top of those, as this Analysis implementation applies b-tagging
        weight *= self.bot_tagger.scale_factor(sel, syst_name)
        # this applies the W+jets Sherpa 2.2.0 nJets reweighting correction
        # WARNING: disable this if using 2.2.1
        #weight *= sel.weight_Sherpa22_corr
        return weight

    def set_top_tagger(self, expr, num_thad = 1, **kwds):
        self.top_tagger = selections.BoostedTopTagger(expr, num_top = num_thad, **kwds)

    def set_bot_tagger(self, algorithm_WP_systs = 'AntiKt2PV0TrackJets.MV2c10_FixedCutBEff70', **kwds):
        attr = algorithm_WP_systs.split('.',2)
        algorithm_WP_systs = attr[-1].split('_', 2)
        if len(attr)==2:
            algorithm_WP_systs.append(attr[0])
        # print algorithm_WP_systs
        self.bot_tagger = selections.TrackJetBotTagger(*algorithm_WP_systs, **kwds)
    def set_aux_selector(self, expr = None):
        self.aux_selector = selections.AuxSelector(expr)
    def set_TtresChi2(self):
        self.TtresChi2 = selections.TtresChi2(bot_tagger = self.bot_tagger)

class AnaTtresSL(Analysis):
    mapSel = {  # OR all channels in the comma-separated list
                'be': ['bejets_2015','bejets_2016','bejets_2017'],
                'bmu': ['bmujets_2015','bmujets_2016','bmujets_2017'],
                're': ['rejets_2015','rejets_2016','rejets_2017'],
                'rmu': ['rmujets_2015','rmujets_2016','rmujets_2017'],
                'be0': ['bejets_2015','bejets_2016','bejets_2017'],
                'bmu0': ['bmujets_2015','bmujets_2016','bmujets_2017'],
                're0': ['rejets_2015','rejets_2016','rejets_2017'],
                'rmu0': ['rmujets_2015','rmujets_2016','rmujets_2017'],
                'be1': ['bejets_2015','bejets_2016','bejets_2017'],
                'bmu1': ['bmujets_2015','bmujets_2016','bmujets_2017'],
                're1': ['rejets_2015','rejets_2016','rejets_2017'],
                'rmu1': ['rmujets_2015','rmujets_2016','rmujets_2017'],
                'be2': ['bejets_2015','bejets_2016','bejets_2017'],
                'bmu2': ['bmujets_2015','bmujets_2016','bmujets_2017'],
                're2': ['rejets_2015','rejets_2016','rejets_2017'],
                'rmu2': ['rmujets_2015','rmujets_2016','rmujets_2017'],
                'be3': ['bejets_2015','bejets_2016','bejets_2017'],
                'bmu3': ['bmujets_2015','bmujets_2016','bmujets_2017'],
                're3': ['rejets_2015','rejets_2016','rejets_2017'],
                'rmu3': ['rmujets_2015','rmujets_2016','rmujets_2017'],
                'be2015': ['bejets_2015'],
                'bmu2015': ['bmujets_2015'],
                're2015': ['rejets_2015'],
                'rmu2015': ['rmujets_2015'],
                'be2016': ['bejets_2016'],
                'bmu2016': ['bmujets_2016'],
                're2016': ['rejets_2016'],
                'rmu2016': ['rmujets_2016'],
                'be2017': ['bejets_2017'],
                'bmu2017': ['bmujets_2017'],
                're2017': ['rejets_2017'],
                'rmu2017': ['rmujets_2017'],
                'ovre': ['rejets_2015','rejets_2016','rejets_2017'],
                'ovrmu': ['rmujets_2015','rmujets_2016','rmujets_2017']}
    def __init__(self, channel, systgroups, outputFile, do_tree = False):
        Analysis.__init__(self, channel, systgroups, outputFile, do_tree)
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
        self.add("yieldsPos", 1, 0.5, 1.5)
        self.add("yieldsNeg", 1, 0.5, 1.5)

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
        self.add("mttPos", 600, 0, 6000)
        self.add("mttNeg", 600, 0, 6000)
        self.add("largeJet_tau32_wta", 20, 0, 1)
        self.add("largeJet_tau21_wta", 20, 0, 1)
        self.add("btagged_tjet_closest_to_ljet", 50, 0, (math.pi**2+2.5**2)**0.5)
        self.add("btagged_tjet_closest_to_lep", 50, 0, (math.pi**2+2.5**2)**0.5)


    # only apply the reco weights
    def getWeight(self, sel, s):
        if sel.mcChannelNumber == 0:
            return 1.0

        syst_name = s.name
        weight = Analysis.getWeight(self, sel, s)

        if syst_name == "singletopup" and sel.mcChannelNumber in [410011, 410012, 410013, 410014, 410015, 410016, 410025, 410026]:
            weight *= 1+0.053
        if syst_name == "singletopdw" and sel.mcChannelNumber in [410011, 410012, 410013, 410014, 410015, 410016, 410025, 410026]:
            weight *= 1-0.053
        if syst_name == "ttxsecup" and sel.mcChannelNumber in [410000, 301528, 301529, 301530, 301531, 301532]:
            weight *= 1+0.056
        if syst_name == "ttxsecdw" and sel.mcChannelNumber in [410000, 301528, 301529, 301530, 301531, 301532]:
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
        weight *= reweighting.WjetSystWeight.get_weight(sel, syst_name)
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
        for k in xrange(sel.jet_pt.size()):
            j = ROOT.TLorentzVector()
            j.SetPtEtaPhiE(sel.jet_pt[k], sel.jet_eta[k], sel.jet_phi[k], sel.jet_e[k])
            jets.push_back(j)
        w = ROOT.TopNtupleAnalysis.getQCDWeight(nBtag, isBoosted, met, l, lisTight, jets, lsd0, isElectron, muonTrigger, topoetcone20, runNumber)
        if   math.fabs(l.Eta()) <= 1.5 and 'qcdcenup' in syst: w *= 1.5
        elif math.fabs(l.Eta()) <= 1.5 and 'qcdcendw' in syst: w *= 0.5
        elif math.fabs(l.Eta()) > 1.5 and 'qcdfwdup' in syst: w *= 2.0
        elif math.fabs(l.Eta()) > 1.5 and 'qcdfwddw' in syst: w *= 0
        return w

    def _selectChannel(self, sel, syst):
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
                passChannel = getattr(sel, item, False)
                if passChannel and hardPass:
                    passORChannels = True
                    break
            passSel[i] = passORChannels
        if not passSel[self.ch]:
            return False
        if not self.aux_selector.passes(sel):
            return False
        if not self.bot_tagger.passes(sel):
            return False
        # veto resolved event if it passes the boosted channel
        top_tagged = self.top_tagger.passes(sel)
        if ('be' in self.ch or 'bmu' in self.ch):
            if not top_tagged:
                return False
            Btagcat = self.top_tagger.bcategory

        if ('re' in self.ch or 'rmu' in self.ch):
            if not self.TtresChi2.passes(sel):
                return False
            Btagcat = self.TtresChi2.bcategory

        if ('re' in self.ch or 'rmu' in self.ch) and not "ov" in self.ch:
            if (passSel['be'] or passSel['bmu']) and top_tagged:
                return False
	
        if self.bcategory != None and Btagcat != self.bcategory:
            return False

        # veto events in nominal ttbar overlapping with the mtt sliced samples
        if sel.mcChannelNumber in [410000, 410470, 410471] and hasattr(sel, "MC_ttbar_beforeFSR_m") and not self.noMttSlices:
            if sel.MC_ttbar_beforeFSR_m > 1.1e6:
                return False

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

        if self.applyMET > 0 and not ('be' in self.ch or 'bmu' in self.ch):
            if sel.met_met*1e-3 < self.applyMET:
                return

        return True


    def _run(self, sel, syst, wo, wTruth):

        ########################
        self.clearBranches() ###
        ########################
        w = wo

        if self.applyQCD:
            w *= self.qcdWeight(sel, syst)

        isdata = (sel.mcChannelNumber == 0)
        if(not isdata and hasattr(sel, "MC_ttbar_beforeFSR_m") and sel.mcChannelNumber not in [407200, 407201, 407202, 407203, 407204]):
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
        self.h['NEvents'][syst].Fill(1, 1)
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
        self.h["lepPt"][syst].Fill(l.Pt()*1e-3, w)
        self.h["lepEta"][syst].Fill(l.Eta(), w)
        self.h["lepPhi"][syst].Fill(l.Phi(), w)
        self.h["MET_phi"][syst].Fill(sel.met_phi, w)
        self.h["MET"][syst].Fill(sel.met_met*1e-3, w)
        self.h["nJets"][syst].Fill(sel.jet_pt.size(), w)
        self.h["nlargeJets"][syst].Fill(sel.ljet_pt.size(), w)
        closestJetIdx = -1
        closestJetPt = 0
        closestJetDr = 99
        for i in xrange(sel.jet_pt.size()):
            cj = ROOT.TLorentzVector()
            cj.SetPtEtaPhiE(sel.jet_pt[i], sel.jet_eta[i], sel.jet_phi[i], sel.jet_e[i])
            dy = (cj.Rapidity() - l.Rapidity())
            dp = DeltaPhi(cj, l)
            dr = (dy**2 + dp**2)**0.5
            if dr < closestJetDr:
                closestJetIdx = i
                closestJetDr = dr
                closestJetPt = cj.Pt()
        try:
            btagged_tjet_closest_to_lep = min((tjet for i, tjet in enumerate(self.bot_tagger._tjet_p4) if helpers.char2int(self.bot_tagger.tjet_isbtagged[i])), key = lambda btagged_tjet: DeltaR(btagged_tjet, l))
            self.h["btagged_tjet_closest_to_lep"][syst].Fill(DeltaR(btagged_tjet_closest_to_lep, l), w)
        except ValueError:
            btagged_tjet_closest_to_lep = None
        self.h["closestJetDr"][syst].Fill(closestJetDr, w)
        self.h["closestJetPt"][syst].Fill(closestJetPt*1e-3, w)
        self.h["nTrkBtagJets"][syst].Fill(sum(helpers.char2int(tjet_isbtagged) for tjet_isbtagged in self.bot_tagger.tjet_isbtagged), w)
        self.h["mwt"][syst].Fill(math.sqrt(2*l.Pt()*sel.met_met*(1 - math.cos(l.Phi() - sel.met_phi)))*1e-3, w)
        self.h["mu"][syst].Fill(sel.mu, w)
        self.h["npv"][syst].Fill(sel.npv, w)
        self.h["vtxz"][syst].Fill(sel.vtxz, w)
        ##TLorentzVector getNu(TLorentzVector l, double met, double met_phi) {
        ##double getMtt(TLorentzVector lep, std::vector<TLorentzVector> jets, std::vector<bool> btag, TLorentzVector met) {
        nu = ROOT.TopNtupleAnalysis.getNu(l, sel.met_met, sel.met_phi)
        if ('be' in self.ch or 'bmu' in self.ch):
            for i in xrange(sel.jet_pt.size()):
                if sel.jet_closeToLepton[i]:
                    closeJetIdx = i
                    break
            
            goodJetIdx = self.top_tagger.ljet_selected.index(1)
            lj.SetPtEtaPhiM(sel.ljet_pt[goodJetIdx], sel.ljet_eta[goodJetIdx], sel.ljet_phi[goodJetIdx], sel.ljet_m[goodJetIdx])
            closeJet = ROOT.TLorentzVector()
            closeJet.SetPtEtaPhiE(sel.jet_pt[closeJetIdx], sel.jet_eta[closeJetIdx], sel.jet_phi[closeJetIdx], sel.jet_e[closeJetIdx])
            try:
                btagged_tjet_closest_to_ljet = min((tjet for i, tjet in enumerate(self.bot_tagger._tjet_p4) if helpers.char2int(self.bot_tagger.tjet_isbtagged[i])), key = lambda btagged_tjet: DeltaR(btagged_tjet, lj))
                self.h["btagged_tjet_closest_to_ljet"][syst].Fill(DeltaR(btagged_tjet_closest_to_ljet, lj), w)
            except ValueError:
                pass
            w0 = w/self.w2HDM
            tlep = closeJet+nu+l
            mtt = (tlep+lj).M()*1e-3 # unit is GeV
            self.h["largeJetPt"][syst].Fill(lj.Pt()*1e-3, w)
            self.h["largeJetM"][syst].Fill(lj.M()*1e-3, w)
            self.h["largeJetEta"][syst].Fill(lj.Eta(), w)
            self.h["largeJetPhi"][syst].Fill(lj.Phi(), w)
            self.h["largeJet_tau32_wta"][syst].Fill(sel.ljet_tau32_wta[goodJetIdx], w)
            self.h["largeJet_tau21_wta"][syst].Fill(sel.ljet_tau21_wta[goodJetIdx], w)
            self.h["mtlep_boo"][syst].Fill(tlep.M()*1e-3, w)
            self.h["mtt"][syst].Fill(mtt, w)
            self.h["mttr"][syst].Fill(mtt, w0*(self.w2HDM-1.))
            self.h["mtt8TeV"][syst].Fill(mtt, w)
            self.h["mtt8TeVr"][syst].Fill(mtt, w0*(self.w2HDM-1.))
            if lQ > 0:
                self.h["mttPos"][syst].Fill(mtt, w)
            elif lQ < 0:
                self.h["mttNeg"][syst].Fill(mtt, w)
            self.h["largeJetPtMtt"][syst].Fill(lj.Pt()/(mtt*1e3), w)
            self.h['finalYields'][syst].Fill(1, w)
            self.h['finalNEvents'][syst].Fill(1)
            
            ################################
            ### fill the tree ##############
            if self._doTree:
                self.branches[syst]["w"].push_back(w)
                self.branches[syst]["w0"].push_back(w0)
                if self._locked == SELECTION_LOCKED:
                    self.branches[syst]["eventNumber"].push_back(sel.eventNumber)
                    self.branches[syst]["runNumber"].push_back(sel.runNumber)
                    self.branches[syst]["mcChannelNumber"].push_back(sel.mcChannelNumber)
                    self.branches[syst]["aS"].push_back(self.alphaS)
                    self.branches[syst]["w2HDM"].push_back(self.w2HDM)
                    self.branches[syst]["me2SM"].push_back(self.me2SM)
                    self.branches[syst]["me2XX"].push_back(self.me2XX)
                    self.branches[syst]["mttReco"].push_back(mtt)
                    self.branches_noclear[syst]["Btagcat"].value = sel.Btagcat
                    # pME = helpers.getTruth4momenta(sel)
                    # truPttbar = pME[2]+pME[3]
                    if sel.mcChannelNumber != 0:
                        self.branches[syst]["mttTrue"].push_back(sel.MC_ttbar_beforeFSR_m*1e-3)
                    # for i in xrange(sel.MC_id_me.size()):
                    #     self.branches[syst]["id"].push_back(sel.MC_id_me[i])
                    #     self.branches[syst]["px"].push_back(sel.MC_px_me[i])
                    #     self.branches[syst]["py"].push_back(sel.MC_py_me[i])
                    #     self.branches[syst]["pz"].push_back(sel.MC_pz_me[i])
                    #     self.branches[syst]["e"].push_back(sel.MC_e_me[i])
                    ##################################
                    for observable in self.observables:
                        if isdata and observable.need_truth:
                            continue
                        if 'tree' in observable.do:
                            values = observable(_locals = locals())
                            if observable.style == 'foreach':
                                for v in values:
                                    self.branches[syst][observable.name].push_back(v)
                            else:
                                self.branches_noclear[syst][observable.name].value = values
                ### fill the tree ################

                self.trees[syst].Fill() ###
                ##################################
        elif 're' in self.ch or 'rmu' in self.ch:
            if sel.ljet_pt.size() >= 1:
                lj.SetPtEtaPhiM(sel.ljet_pt[0], sel.ljet_eta[0], sel.ljet_phi[0], sel.ljet_m[0])
                try:
                    btagged_tjet_closest_to_ljet = min((tjet for i, tjet in enumerate(self.bot_tagger._tjet_p4) if helpers.char2int(self.bot_tagger.tjet_isbtagged[i])), key = lambda btagged_tjet: DeltaR(btagged_tjet, lj))
                    self.h["btagged_tjet_closest_to_ljet"][syst].Fill(DeltaR(btagged_tjet_closest_to_ljet, lj), w)
                except ValueError:
                    pass
                self.h["largeJetPt"][syst].Fill(lj.Pt()*1e-3, w)
                self.h["largeJetM"][syst].Fill(lj.M()*1e-3, w)
                self.h["largeJetEta"][syst].Fill(lj.Eta(), w)
                self.h["largeJetPhi"][syst].Fill(lj.Phi(), w)
                self.h["largeJet_tau32_wta"][syst].Fill(sel.ljet_tau32_wta[0], w)
                self.h["largeJet_tau21_wta"][syst].Fill(sel.ljet_tau21_wta[0], w)
            if btagged_tjet_closest_to_lep is not None:
                self.h["btagged_tjet_closest_to_lep"][syst].Fill(DeltaR(btagged_tjet_closest_to_lep, l), w)
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
            self.h['finalYields'][syst].Fill(1, w)
            self.h['finalNEvents'][syst].Fill(1)
            ################################
            ### fill the tree ##############
            if self._doTree:
                self.branches[syst]["w"].push_back(w)
                self.branches[syst]["w0"].push_back(w0)
                if self._locked == SELECTION_LOCKED:
                    self.branches[syst]["eventNumber"].push_back(sel.eventNumber)
                    self.branches[syst]["runNumber"].push_back(sel.runNumber)
                    self.branches[syst]["mcChannelNumber"].push_back(sel.mcChannelNumber)
                    self.branches[syst]["aS"].push_back(self.alphaS)

                    self.branches[syst]["w2HDM"].push_back(self.w2HDM)
                    self.branches[syst]["me2SM"].push_back(self.me2SM)
                    self.branches[syst]["me2XX"].push_back(self.me2XX)
                    self.branches[syst]["mttReco"].push_back(mtt)
                    self.branches_noclear[syst]["Btagcat"].value = self.TtresChi2.bcategory
                    if sel.mcChannelNumber != 0:
                        if not (helpers.nameX!="" and sel.mcChannelNumber in [407200, 407201, 407202, 407203, 407204]):
                            self.branches[syst]["mttTrue"].push_back(sel.MC_ttbar_beforeFSR_m*1e-3)
                        else:
                            pME = helpers.getTruth4momenta(sel)
                            truPttbar = pME[2]+pME[3]
                            self.branches[syst]["mttTrue"].push_back(truPttbar.M())
                            for i in xrange(sel.MC_id_me.size()):
                                self.branches[syst]["id"].push_back(sel.MC_id_me[i])
                                self.branches[syst]["px"].push_back(sel.MC_px_me[i])
                                self.branches[syst]["py"].push_back(sel.MC_py_me[i])
                                self.branches[syst]["pz"].push_back(sel.MC_pz_me[i])
                                self.branches[syst]["e"].push_back(sel.MC_e_me[i])

                    for observable in self.observables:
                        if isdata and observable.need_truth:
                            continue
                        if 'tree' in observable.do:
                            values = observable( _locals = locals())
                            if observable.style == 'foreach':
                                for v in values:
                                    self.branches[syst][observable.name].push_back(v)
                            else:
                                self.branches_noclear[syst][observable.name].value = values
                ##################################
                ### fill the tree ################
                self.trees[syst].Fill() ###
                ##################################
        else:
            raise NameError( 'Undefined Channel <{}>'.format(self.ch) )
        for observable in self.observables:
            if isdata and observable.need_truth:
                continue
            if 'hist' in observable.do:
                values = observable(_locals = locals())
                if observable.style == 'foreach':
                    for v in values:
                        self.h[observable.name][syst].Fill(v, w)
                else:
                    self.h[observable.name][syst].Fill(values, w)

    def set_top_tagger(self, expr, num_thad = 1, strategy = 'obey', **kwds):
        kwds.setdefault('do_truth_matching', True)
        super(AnaTtresSL, self).set_top_tagger(expr, num_thad = num_thad, strategy = strategy, **kwds)

    def set_bot_tagger(self, algorithm_WP_systs = 'AntiKt2PV0TrackJets.MV2c10_FixedCutBEff70', **kwds):
        # kwds.setdefault('strategy', 'rebel')
        Analysis.set_bot_tagger(self, algorithm_WP_systs, **kwds)

class AnaTtresFH(Analysis):
    mapSel = {  # OR all channels in the comma-separated list
                'bFH': ['bFH_2015', 'bFH_2016', 'bFH_2017', 'bFH_2018'],
                'bFH-1': ['bFH_2015', 'bFH_2016', 'bFH_2017', 'bFH_2018'],
                'bFH0': ['bFH_2015', 'bFH_2016', 'bFH_2017', 'bFH_2018'],
                'bFH1': ['bFH_2015', 'bFH_2016', 'bFH_2017', 'bFH_2018'],
                'bFH2': ['bFH_2015', 'bFH_2016', 'bFH_2017', 'bFH_2018'],
                'bFH3': ['bFH_2015', 'bFH_2016', 'bFH_2017', 'bFH_2018'],
                'rFH': ['rFH_2015', 'rFH_2016'],
                'rFH0': ['rFH_2015', 'rFH_2016'],
                'rFH1': ['rFH_2015', 'rFH_2016'],
                'rFH2': ['rFH_2015', 'rFH_2016'],
                'rFH3': ['rFH_2015', 'rFH_2016'],
                'ovrFH': ['rFH_2015', 'rFH_2016'],
                'ovrFH': ['rFH_2015', 'rFH_2016']
                }
    def __init__(self, channel, systgroups, outputFile, do_tree = False):
        if 'rFH' in channel:
            raise NotImplementedError("resolved (bucket) analysis is not yet implemented!")
        Analysis.__init__(self, channel, systgroups, outputFile, do_tree)
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
        self.blinded = False
        ########################
        ### make debug tree ####
        self.addTree() #########
        ########################

        # Leading hadronic top candidate
        self.addVar("leadinglargeJetPt", [300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 540, 580, 620, 660, 700, 800, 1e3, 1.2e3, 1.5e3, 2e3, 2.5e3, 3e3, 4e3, 5e3])
        self.add("leadinglargeJetM", 30, 0, 300)
        self.add("leadinglargeJetY", 22, -2.2, 2.2)
        self.add("leadinglargeJetPtMtt", 50, 0, 1)
        self.add("leadinglargeJetEta", 22, -2.2, 2.2)
        self.add("leadinglargeJetPhi", 32, -3.2, 3.2)
        self.add("leadinglargeJet_tau32_wta", 20, 0, 1)
        self.add("leadinglargeJet_tau21_wta", 20, 0, 1)
        self.add("leadinglargeJet_DNNScore", 50, 0, 1)
        self.add2D("leadinglargeJetEtaPhi", 44, -2.2, 2.2, 64, -3.2, 3.2)
        self.add("btagged_tjet_closest_to_ljet1", 50, 0, (math.pi**2+2.5**2)**0.5)
        # Sub-leading hadronic top candidate
        self.addVar("subleadinglargeJetPt", [300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 540, 580, 620, 660, 700, 800, 1e3, 1.2e3, 1.5e3, 2e3, 2.5e3, 3e3, 4e3, 5e3])
        self.add("subleadinglargeJetM", 30, 0, 300)
        self.add("subleadinglargeJetY", 22, -2.2, 2.2)
        self.add("subleadinglargeJetPtMtt", 50, 0, 1)
        self.add("subleadinglargeJetEta", 22, -2.2, 2.2)
        self.add("subleadinglargeJetPhi", 32, -3.2, 3.2)
        self.add("subleadinglargeJet_tau32_wta", 20, 0, 1)
        self.add("subleadinglargeJet_tau21_wta", 20, 0, 1)
        self.add("subleadinglargeJet_DNNScore", 50, 0, 1)
        self.add2D("subleadinglargeJetEtaPhi", 44, -2.2, 2.2, 64, -3.2, 3.2)
        self.add("btagged_tjet_closest_to_ljet2", 50, 0, (math.pi**2+2.5**2)**0.5)
        self.add("dPhiJJ", 60, -math.pi*1.2, math.pi*1.2)
        self.add("Ystar", 22, -2.2, 2.2)
        self.add("Yboost", 22, -2.2, 2.2)
        ### resolved channel ###
        # Leading hadronic top candidate
        self.addVar("mthad1_res", [80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 340, 380, 420, 460, 500])
        self.add("mwhad1_res", 40, 0, 400)
        # Sub-leading hadronic top candidate
        self.addVar("mthad2_res", [80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 340, 380, 420, 460, 500])
        self.add("mwhad2_res", 40, 0, 400)

        #self.addVar("mtt", [0, 80, 160, 240, 320, 400, 480, 560,640,720,800,920,1040,1160,1280,1400,1550,1700,2000,2300,2600,2900,3200,3600,4100,4600,5100,6000])

        self.add("btagCat", 5, -1.5, 3.5)
        
        for observable in self.observables:
            if 'hist' in observable.do:
                if type(observable.binning) == tuple:
                    self.add(observable.name, *observable.binning)
                else:
                    self.addVar(observable.name, observable.binning)

    def _selectChannel(self, sel, syst):
        if self.ch not in self.mapSel:
            logger.warn('The selected channel "{}" is not registered. The events will be processed anyway without any further constraint.'.format(self.ch))
            self.mapSel[self.ch] = [self.ch]
        passSel = {}
        for i, listSel in self.mapSel.iteritems():
            passSel[i] = True
            passORChannels = False
            for item in listSel:
                hardPass = True
                passChannel = getattr(sel, item, False)
                if passChannel and hardPass:
                    passORChannels = True
                    break
            passSel[i] = passORChannels

        if not passSel[self.ch]:
            return False
        if not self.aux_selector.passes(sel):
            return False
        # if not sel.ljet_pt[0] > 500000: # Tigger threshold
        #     return False
        if not self.bot_tagger.passes(sel):
            return False
        # veto resolved event if it passes the boosted channel
        top_tagged = self.top_tagger.passes(sel)
        if 'bFH' in self.ch and not top_tagged:
                return False
        if 'rFH' in self.ch:
            self.TtresBucket.passes(sel)
            Btagcat = self.TtresBucket.bcategory
        else:
            Btagcat = self.top_tagger.bcategory

        if 'rFH' in self.ch and not "ov" in self.ch:
            if passSel['bFH'] and top_tagged:
                return False
        if self.bcategory != None and Btagcat != self.bcategory:
            return False

        # veto events in nominal ttbar overlapping with the mtt sliced samples
        if sel.mcChannelNumber in [410000, 410470, 410471] and hasattr(sel, "MC_ttbar_beforeFSR_m") and not self.noMttSlices:
            if sel.MC_ttbar_beforeFSR_m > 1.1e6:
                return False

        if self.applyMET > 0 and not 'bFH' in self.ch:
            if sel.met_met*1e-3 < self.applyMET:
                return

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

        return True
    def _run(self, sel, syst, wo, wTruth):
        ########################
        self.clearBranches() ###
        ########################
        w = wo
        isdata = sel.mcChannelNumber == 0
        if (not isdata and hasattr(sel, "MC_ttbar_beforeFSR_m")):
            w0 = w/self.w2HDM
            self.h["trueMtt"][syst].Fill(sel.MC_ttbar_beforeFSR_m*1e-3, w)

        self.h["runNumber"][syst].Fill(sel.runNumber, w)

        self.h["MET_phi"][syst].Fill(sel.met_phi, w)
        self.h["MET"][syst].Fill(sel.met_met*1e-3, w)
        self.h["nJets"][syst].Fill(sel.jet_pt.size(), w)

        self.h["nTrkBtagJets"][syst].Fill(sum(helpers.char2int(tjet_isbtagged) for tjet_isbtagged in self.bot_tagger.tjet_isbtagged), w)
        self.h["mu"][syst].Fill(sel.mu, w)
        self.h["npv"][syst].Fill(sel.npv, w)
        self.h["vtxz"][syst].Fill(sel.vtxz, w)
        self.h['NEvents'][syst].Fill(1, 1)
        self.h['yields'][syst].Fill(1, w)
        if 'bFH' in self.ch:
            goodJetIdx1 = self.top_tagger.ljet_selected.index(1)
            lj1 = self.top_tagger.ljet_p4[goodJetIdx1]*GeV
            goodJetIdx2 = self.top_tagger.ljet_selected.index(1, goodJetIdx1+1)
            lj2 = self.top_tagger.ljet_p4[goodJetIdx2]*GeV
            w0 = w/self.w2HDM
            mtt = (lj1+lj2).M() # unit is GeV
            bjets = list(tjet for i, tjet in enumerate(self.bot_tagger._tjet_p4) if helpers.char2int(self.bot_tagger.tjet_isbtagged[i]))
            self.h["mtt"][syst].Fill(mtt, w)
            self.h["mttr"][syst].Fill(mtt, w0*(self.w2HDM-1.))
            
            ### boosted channel ###
            self.h["nlargeJets"][syst].Fill(sel.ljet_pt.size(), w)
            # Leading hadronic top candidate
            self.h["leadinglargeJetPt"][syst].Fill(lj1.Pt(), w)
            self.h["leadinglargeJetM"][syst].Fill(lj1.M(), w)
            self.h["leadinglargeJetY"][syst].Fill(lj1.Rapidity(), w)
            self.h["leadinglargeJetPtMtt"][syst].Fill(lj1.Pt()/mtt, w)
            self.h["leadinglargeJetEta"][syst].Fill(lj1.Eta(), w)
            self.h["leadinglargeJetPhi"][syst].Fill(lj1.Phi(), w)
            self.h["leadinglargeJet_tau32_wta"][syst].Fill(sel.ljet_tau32_wta[goodJetIdx1], w)
            self.h["leadinglargeJet_tau21_wta"][syst].Fill(sel.ljet_tau21_wta[goodJetIdx1], w)
            self.h["leadinglargeJetEtaPhi"][syst].Fill(lj1.Eta(), lj1.Phi(), w)
            self.h["leadinglargeJet_DNNScore"][syst].Fill(sel.ljet_DNNTopTag_score[goodJetIdx1], w)
            deltaR_closest_btjet_to_ljet1 = 1e6
            for bjet in bjets:
                deltaR_closest_btjet_to_ljet1 = min(DeltaR(bjet, lj1), deltaR_closest_btjet_to_ljet1)
            self.h["btagged_tjet_closest_to_ljet1"][syst].Fill(deltaR_closest_btjet_to_ljet1, w)
            # Sub-leading hadronic top candidate
            self.h["subleadinglargeJetPt"][syst].Fill(lj2.Pt(), w)
            self.h["subleadinglargeJetM"][syst].Fill(lj2.M(), w)
            self.h["subleadinglargeJetY"][syst].Fill(lj2.Rapidity(), w)
            self.h["subleadinglargeJetPtMtt"][syst].Fill(lj2.Pt()/mtt, w)
            self.h["subleadinglargeJetEta"][syst].Fill(lj2.Eta(), w)
            self.h["subleadinglargeJetPhi"][syst].Fill(lj2.Phi(), w)
            self.h["subleadinglargeJet_tau32_wta"][syst].Fill(sel.ljet_tau32_wta[goodJetIdx2], w)
            self.h["subleadinglargeJet_tau21_wta"][syst].Fill(sel.ljet_tau21_wta[goodJetIdx2], w)
            self.h["subleadinglargeJetEtaPhi"][syst].Fill(lj2.Eta(), lj2.Phi(), w)
            self.h["subleadinglargeJet_DNNScore"][syst].Fill(sel.ljet_DNNTopTag_score[goodJetIdx2], w)

            self.h["dPhiJJ"][syst].Fill(DeltaPhi(lj1, lj2), w)
            self.h["Ystar"][syst].Fill((lj1.Rapidity()-lj2.Rapidity())/2, w)
            self.h["Yboost"][syst].Fill((lj1.Rapidity()+lj2.Rapidity())/2, w)
            deltaR_closest_btjet_to_ljet2 = 1e6
            for bjet in bjets:
                deltaR_closest_btjet_to_ljet2 = min(DeltaR(bjet, lj2), deltaR_closest_btjet_to_ljet2)
            self.h["btagged_tjet_closest_to_ljet2"][syst].Fill(deltaR_closest_btjet_to_ljet2, w)

            self.h["btagCat"][syst].Fill(self.top_tagger.bcategory, w)
            self.h['finalYields'][syst].Fill(1, w)
            self.h['finalNEvents'][syst].Fill(1)

            ################################
            ### fill the tree ##############
            if self._doTree:
                self.branches[syst]["w"].push_back(w)
                self.branches[syst]["w0"].push_back(w0)
                if self._locked == SELECTION_LOCKED:
                    self.branches[syst]["eventNumber"].push_back(sel.eventNumber)
                    self.branches[syst]["runNumber"].push_back(sel.runNumber)
                    self.branches[syst]["mcChannelNumber"].push_back(sel.mcChannelNumber)
                    self.branches[syst]["aS"].push_back(self.alphaS)
                    self.branches[syst]["w2HDM"].push_back(self.w2HDM)
                    self.branches[syst]["me2SM"].push_back(self.me2SM)
                    self.branches[syst]["me2XX"].push_back(self.me2XX)
                    self.branches[syst]["mttReco"].push_back(mtt)
                    self.branches_noclear[syst]["Btagcat"].value = self.top_tagger.bcategory
                    # pME = helpers.getTruth4momenta(sel)
                    # truPttbar = pME[2]+pME[3]
                    if sel.mcChannelNumber != 0:
                        self.branches[syst]["mttTrue"].push_back(sel.MC_ttbar_beforeFSR_m*1e-3)
                    # for i in xrange(sel.MC_id_me.size()):
                    #     self.branches[syst]["id"].push_back(sel.MC_id_me[i])
                    #     self.branches[syst]["px"].push_back(sel.MC_px_me[i])
                    #     self.branches[syst]["py"].push_back(sel.MC_py_me[i])
                    #     self.branches[syst]["pz"].push_back(sel.MC_pz_me[i])
                    #     self.branches[syst]["e"].push_back(sel.MC_e_me[i])
                    ##################################
                    for observable in self.observables:
                        if isdata and observable.need_truth:
                            continue
                        if 'tree' in observable.do:
                            values = observable( _locals = locals())
                            if observable.style == 'foreach':
                                for v in values:
                                    self.branches[syst][observable.name].push_back(v)
                            else:
                                self.branches_noclear[syst][observable.name].value = values

                ##################################
                ### fill the tree ################
                self.trees[syst].Fill() ###
                ##################################
        else:
            raise NameError( 'Undefined Channel <{}>'.format(self.ch) )
        for observable in self.observables:
            if isdata and observable.need_truth:
                continue
            if 'hist' in observable.do:
                values = observable(_locals = locals())
                if observable.style == 'foreach':
                    for v in values:
                        self.h[observable.name][syst].Fill(v, w)
                else:
                    self.h[observable.name][syst].Fill(values, w)

    def set_top_tagger(self, expr, num_thad = 2, strategy = 'rebel', **kwds):
        kwds.setdefault('min_pt', 350000)
        kwds.setdefault('leading_only', True)
        kwds.setdefault('do_truth_matching', True)
        super(AnaTtresFH, self).set_top_tagger(expr, num_thad = num_thad, strategy = strategy, **kwds)
        if self.blinded:
            logger.warning('The deltaY cut is inverted to 1.8 <= deltaY(J,J)')
            self.top_tagger.absdYJJRange = (1.8, float('inf'))
        if hasattr(self, 'bot_tagger'):
            self.top_tagger._bot_tagger = self.bot_tagger

    def set_bot_tagger(self, algorithm_WP_systs = 'AntiKt2PV0TrackJets.MV2c10_FixedCutBEff77', **kwds):
        kwds.setdefault('do_ljet_association', True)
        kwds.setdefault('strategy', 'obey')
        kwds.setdefault('min_nbjets', 0)
        kwds.setdefault('SF_type', 'eventlevel')
        kwds.setdefault('do_association', False)
        # kwds.setdefault('do_truth_matching', False)
        super(AnaTtresFH, self).set_bot_tagger(algorithm_WP_systs, **kwds)
        if hasattr(self, 'top_tagger'):
            self.top_tagger._bot_tagger = self.bot_tagger