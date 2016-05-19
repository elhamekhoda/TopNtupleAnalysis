import helpers
import ROOT
import math

class Analysis:
    ch = ''
    fi = None
    histSuffixes = [] # systematic copies of histograms
    h = {} # map of histogram names to map of systematics to histograms
    def __init__(self, channel, suf, outputFile):
	self.fi = ROOT.TFile(outputFile, "recreate")
	self.ch = channel
	self.histSuffixes = suf
	self.h = {}

    def add(self, hName, nBins, xLow, xHigh):
        self.h[hName] = {}
        self.fi.cd()
	for s in self.histSuffixes:
	    self.h[hName][s] = ROOT.TH1D(hName+self.ch+s, "", nBins, xLow, xHigh)
	    self.h[hName][s].SetDirectory(0)

    def addVar(self, hName, nBinsList):
        ar = array("d", nBinsList)
        self.fi.cd()
        self.h[hName] = {}
	for s in self.histSuffixes:
	    self.h[hName][s] = ROOT.TH1D(hName+self.ch+s, "", len(nBinsList) - 1, ar)
	    self.h[hName][s].SetDirectory(0)

    def write(self):
        self.fi.cd()
	for hName in self.h:
	    for s in self.histSuffixes:
	        self.h[hName][s].Write(hName+s)

class AnaTtresSL(Analysis):
    def __init__(self, channel, suf, outputFile):
        super(AnaTtresSL, self).__init__(channel, suf, outputFile)
        # make histograms
        self.add("yields", 1, 0.5, 1.5)
        self.add("lepPt", 100, 25, 525)
        self.add("lepEta", 20, -2.5, 2.5)
        self.add("lepPhi", 32, -3.2, 3.3)
        self.add("nJets", 10, -0.5, 9.5)
        self.add("nTrkBtagJets", 10, -0.5, 9.5)
        self.addVar("MET", [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 220, 240, 260, 280, 300, 340, 380, 450, 500])
        self.add("MET_phi", 32, -3.2, 3.2)
        self.add("mwt", 20, 0, 200)
        self.add("mu", 100, 0, 100)
        self.add("vtxz", 40, -400, 400)
        self.add("npv", 50, 0, 50)

        self.addVar("closeJetPt", [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 220, 240, 260, 280, 300, 340, 380, 450, 500])
        self.addVar("largeJetPt", [300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 540, 580, 620, 660, 700, 800, 1e3, 1.2e3, 1.5e3])
        self.add("largeJetM", 30, 0, 300)
        self.add("largeJetEta", 20, -2., 2.)
        self.add("largeJetPhi", 32, -3.2, 3.2)
        self.addVar("mtlep_boo", [80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 340, 380, 420, 460, 500])
        self.addVar("mtlep_res", [80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 340, 380, 420, 460, 500])
        self.addVar("mthad_res", [80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 340, 380, 420, 460, 500])
        self.add("mwhad_res", 40, 0, 400)
        self.add("chi2", 50, -3, 7)
        self.addVar("mtt", [0, 80, 160, 240, 320, 400, 480, 560,640,720,800,920,1040,1160,1280,1400,1550,1700,2000,2300,2600,2900,3200,3600,4100,4600,5100,6000])
        self.addVar("trueMtt", [0, 80, 160, 240, 320, 400, 480, 560,640,720,800,920,1040,1160,1280,1400,1550,1700,2000,2300,2600,2900,3200,3600,4100,4600,5100,6000])

        self.add("largeJet_tau32_wta", 20, 0, 1)
        self.add("largeJet_tau21_wta", 20, 0, 1)

    def run(self, sel, syst, w):
        if self.ch == 're' or self.ch == 'be':
            if len(sel.el_pt) != 1 or len(sel.mu_pt) != 0:
    	        return
        if self.ch == 'rmu' or self.ch == 'bmu':
            if len(sel.el_pt) != 0 or len(sel.mu_pt) != 0:
    	        return
        if self.ch == 'bmu' or self.ch == 'be':
            if not(sel.bejets or sel.bmujets):
    	        return
        if self.ch == 'rmu' or self.ch == 're':
            if not(sel.rejets or sel.rmujets):
    	        return
        self.h["yields"][syst].Fill(1, w)
        l = ROOT.TLorentzVector()
        if len(sel.el_pt) == 1:
            l.SetPtEtaPhiE(sel.el_pt[0], sel.el_eta[0], sel.el_phi[0], sel.el_e[0])
        elif len(sel.mu_pt) == 1:
            l.SetPtEtaPhiE(sel.mu_pt[0], sel.mu_eta[0], sel.mu_phi[0], sel.mu_e[0])
        self.h["lepPt"][syst].Fill(l.Perp()*1e-3, w)
        self.h["lepEta"][syst].Fill(l.Eta(), w)
        self.h["lepPhi"][syst].Fill(l.Phi(), w)
        self.h["MET_phi"][syst].Fill(sel.met_phi, w)
        self.h["MET"][syst].Fill(sel.met_met*1e-3, w)
        self.h["nJets"][syst].Fill(len(sel.jet_pt), w)
	nBtags = 0
        tjets = []
        tb = []
  	for bidx in range(0, len(sel.tjet_mv2c20)):
	    pb = ROOT.TLorentzVector(sel.tjet_pt[bidx], sel.tjet_eta[bidx], sel.tjet_phi[bidx], sel.tjet_e[bidx])
	    if pb.Perp() > 10e3 and math.fabs(pb.Eta()) < 2.5 and sel.tjet_numConstituents[bidx] >= 2:
    	       tjets.append(pb)
    	       b = False
               if sel.tjet_mv2c20 > helpers.MV2C20_CUT:
	           nBtags += 1
    	           b = True
               tb.append(b)
        self.h["nTrkBtagJets"][syst].Fill(nBtags, w)
        self.h["mwt"][syst].Fill(math.sqrt(2*l.Perp()*sel.met_met*(1 - math.cos(l.Phi() - sel.met_phi)))*1e-3, w)
        self.h["mu"][syst].Fill(sel.mu, w)
        self.h["npv"][syst].Fill(sel.npv, w)
        self.h["vtxz"][syst].Fill(sel.vtxz, w)
        ##TLorentzVector getNu(TLorentzVector l, double met, double met_phi) {
        ##double getMtt(TLorentzVector lep, std::vector<TLorentzVector> jets, std::vector<bool> btag, TLorentzVector met) {
        nu = helpers.wrapperC.getNu(l, sel.met_met, sel.met_phi)
        if sel.bmujets or sel.bejets:
            goodJetIdx = -1
    	    closeJetIdx = -1
    	    for i in range(0, len(sel.jet_pt)):
    	        if sel.jet_closeToLepton:
    	            closeJetIdx = i
    		    break
            for i in range(0, len(sel.ljet_pt)):
    	        if sel.ljet_good:
    	            goodJetIdx = i
    		    break
            lj = ROOT.TLorentzVector()
    	    lj.SetPtEtaPhiM(sel.ljet_pt[goodJetIdx], sel.ljet_eta[goodJetIdx], sel.ljet_phi[goodJetIdx], sel.ljet_m[goodJetIdx])
            closeJet = ROOT.TLorentzVector()
            closeJet.SetPtEtaPhiE(sel.jet_pt[closeJetIdx], sel.jet_eta[closeJetIdx], sel.jet_phi[closeJetIdx], sel.jet_e[closeJetIdx])
    	    self.h["largeJetPt"][syst].Fill(lj.Perp()*1e-3, w)
    	    self.h["largeJetM"][syst].Fill(lj.M()*1e-3, w)
    	    self.h["largeJetEta"][syst].Fill(lj.Eta(), w)
    	    self.h["largeJetPhi"][syst].Fill(lj.Phi(), w)
      	    self.h["largeJet_tau32_wta"][syst].Fill(sel.ljet_tau32_wta[goodJetIdx], w)
    	    self.h["largeJet_tau21_wta"][syst].Fill(sel.ljet_tau21_wta[goodJetIdx], w)
    	    self.h["mtlep_boo"][syst].Fill((closeJet+nu+l).M()*1e-3, w)
    	    self.h["mtt"][syst].Fill((closeJet+nu+l+lj).M()*1e-3, w)
        elif sel.rejets or sel.rmujets:
            jets = ROOT.vector('TLorentzVector')()
            #jets = []
            btag = ROOT.vector('bool')()
            #btag = []
            for k in range(0, len(sel.jet_pt)):
                jets.push_back(ROOT.TLorentzVector(sel.jet_pt[k], sel.jet_eta[k], sel.jet_phi[k], sel.jet_e[k]))
    	    tagged = False
    	    for t in range(0, len(tjets)):
    	        dr = jets[k].DeltaR(tjets[t])
    	        if dr < 0.4 and tb[t]:
    	            tagged = True
                btag.push_back(tagged)
            met = ROOT.TLorentzVector(sel.met_met, 0, sel.met_phi, sel.met_met)
            res_info = helpers.wrapperC.getMtt(l, jets, btag, met)
            mtt = res_info["mtt"]
            mtl = res_info["mtl"]
            mth = res_info["mth"]
            mwh = res_info["mwh"]
            self.h["mtt"][syst].Fill(mtt*1e-3, w)
            self.h["mtlep_res"][syst].Fill(mtl*1e-3, w)
            self.h["mthad_res"][syst].Fill(mth*1e-3, w)
            self.h["mwhad_res"][syst].Fill(mwh*1e-3, w)
    def end(self):
        print "Yield for channel ", self.ch, self.h["yields"][""].GetBinContent(1)
        self.write()

class AnaTest(Analysis):
    def __init__(self, channel, suf, outputFile):
        Analysis.__init__(self, channel, suf, outputFile)
        # make histograms
        self.add("yields", 1, 0.5, 1.5)
        self.y = 0

    def run(self, sel, syst, w):
        ech = getattr(sel, self.ch)
        if not ech:
            return
        self.h["yields"][syst].Fill(1, w)
	self.y += w

    def end(self):
        print "Yield for channel ", self.ch, self.h["yields"][""].GetBinContent(1)
        self.write()

