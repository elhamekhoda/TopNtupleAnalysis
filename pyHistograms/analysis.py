import helpers
import ROOT
import math
from array import array

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
		self.keep = '' # can be 'bb', 'cc', 'c' or 'l' and only applies to W+jets

	def add(self, hName, nBins, xLow, xHigh):
		self.h[hName] = {}
		#self.fi.cd()
		for s in self.histSuffixes:
			#print "adding histogram with name ", hName+self.ch+s
			self.h[hName][s] = ROOT.TH1D(hName+self.ch+s, "", nBins, xLow, xHigh)
			self.h[hName][s].SetDirectory(0)

	def addVar(self, hName, nBinsList):
		ar = array("d", nBinsList)
		#self.fi.cd()
		self.h[hName] = {}
		for s in self.histSuffixes:
			self.h[hName][s] = ROOT.TH1D(hName+self.ch+s, "", len(nBinsList) - 1, ar)
			self.h[hName][s].SetDirectory(0)

	def write(self):
		self.fi.cd()
		for hName in self.h:
			for s in self.histSuffixes:
				print "writing histogram with name ", hName+s, " in file ",self.fi.GetName()
				self.h[hName][s].Write(hName+s)
		self.fi.Close()

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
			wItem = getattr(sel, 'weight_'+item)
			weight *= wItem

		# this applies the EWK weight
		channel = sel.mcChannelNumber
		if channel in helpers.listEWK:
			weight *= helpers.applyEWK(sel, s)

		# this applies the W+jets Sherpa 2.2 nJets reweighting correction
		#weight *= helpers.applyWjets22Weight(sel)
		weight *= sel.weight_Sherpa22_corr

		return weight


class AnaTtresSL(Analysis):
	def __init__(self, channel, suf, outputFile):
		Analysis.__init__(self, channel, suf, outputFile)
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

	# only apply the reco weights
	def getWeight(self, sel, s):
		if sel.mcChannelNumber == 0:
  			return 1.0
		weight = Analysis.getWeight(self, sel, s)

		# just add the btagging SFs on top of those, as this Analysis implementation applies b-tagging
		# warning: disabled for now in mc15c
		btagsf = 1.0 #applyBtagSF(sel, s)
		weight *= btagsf
		return weight

	def run(self, sel, syst, w):
		if sel.mcChannelNumber in helpers.listWjets22:
			flag = sel.Wfilter_Sherpa_nT
			if self.keep == 'bb':
				if flag != 3 and flag != 4:
					return
			if self.keep == 'cc':
				if flag != 1:
					return
			if self.keep == 'c':
				if flag != 2:
					return
			if self.keep == 'l':
				if flag != 5:
					return

		# OR all channels in the comma-separated list
		mapSel = {'be': 'bejets', 'bmu': 'bmujets,bmujetsmet80', 're': 'rejets', 'rmu': 'rmujets,rmujetsmet80'}
		listSel = mapSel[self.ch].split(',')

		passAllChannels = False
		for item in listSel:
			passChannel = getattr(sel, item)
			if not passChannel:
				passAllChannels = True
		if not passAllChannels:
			return

		# veto resolved event if it passes the boosted channel
		if self.ch == 're' or self.ch == 'rmu':
			if sel.bejets or sel.bmujets or sel.bmujetsmet80:
				return

		if ((sel.bmujets or sel.rmujets) and not (sel.HLT_mu50 or sel.HLT_mu20_iloose_L1MU15)) or ((sel.bmujetsmet80 or sel.rmujetsmet80) and not (sel.HLT_xe80_tc_lcw_L1XE50)):
			return
		if (sel.bejets or sel.rejets) and (sel.mcChannelNumber != 0) and not (sel.HLT_e24_lhmedium_L1EM18VH or sel.HLT_e60_lhmedium or HLT_e120_lhloos):
			return
		if (sel.bejets or sel.rejets) and (sel.mcChannelNumber == 0) and not (sel.HLT_e24_lhmedium_L1EM20VH or sel.HLT_e60_lhmedium or HLT_e120_lhloos):
			return

		# apply b-tagging cut
		nBtag = 0
		for bidx in range(0, len(sel.tjet_mv2c10)):
			pb = ROOT.TLorentzVector(sel.tjet_pt[bidx], sel.tjet_eta[bidx], sel.tjet_phi[bidx], sel.tjet_e[bidx])
			if pb.Perp() > 10e3 and math.fabs(pb.Eta()) < 2.5 and sel.tjet_numConstituents[bidx] >= 2:
				if sel.tjet_mv2c10[bidx] > helpers.MV2C10_CUT:
					nBtag += 1
		if nBtag < 1:
			return

		# veto events in nominal ttbar overlapping with the mtt sliced samples
		# commented now as it is not available in mc15c
		#if sel.mcChannelNumber == '410000':
		#	if sel.MC_ttbar_beforeFSR_m > 1.1e6:
		#		return

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
		for bidx in range(0, len(sel.tjet_mv2c10)):
			pb = ROOT.TLorentzVector(sel.tjet_pt[bidx], sel.tjet_eta[bidx], sel.tjet_phi[bidx], sel.tjet_e[bidx])
			if pb.Perp() > 10e3 and math.fabs(pb.Eta()) < 2.5 and sel.tjet_numConstituents[bidx] >= 2:
				tjets.append(pb)
				b = False
				if sel.tjet_mv2c10 > helpers.MV2C10_CUT:
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


class AnaWjetsCR(Analysis):
	def __init__(self, channel, suf, outputFile):
		Analysis.__init__(self, channel, suf, outputFile)
		# make histograms
		self.add("yields", 1, 0.5, 1.5)
		self.add("lepPt", 100, 25, 525)
		self.add("lepEta", 20, -2.5, 2.5)
		self.add("lepPhi", 32, -3.2, 3.3)
		self.add("nJets", 4, 0.5, 4.5)
		self.add("nJetsPos", 4, 0.5, 4.5)
		self.add("nJetsNeg", 4, 0.5, 4.5)
		self.addVar("MET", [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 220, 240, 260, 280, 300, 340, 380, 450, 500])
		self.add("mwt", 20, 0, 200)

	# only apply the reco weights
	def getWeight(self, sel, s):
		if sel.mcChannelNumber == 0:
			return 1.0
		weight = Analysis.getWeight(self, sel, s)

		# just add the btagging SFs on top of those, as this Analysis implementation applies b-tagging
		# warning: disabled for now in mc15c
		btagsf = 1.0 #applyBtagSF(sel, s)
		weight *= btagsf
		return weight

	def run(self, sel, syst, w):
		if sel.mcChannelNumber in helpers.listWjets22:
			flag = sel.Wfilter_Sherpa_nT
			if self.keep == 'bb':
				if flag != 3 and flag != 4:
					return
			if self.keep == 'cc':
				if flag != 1:
					return
			if self.keep == 'c':
				if flag != 2:
					return
			if self.keep == 'l':
				if flag != 5:
					return

		passChannel = getattr(sel, self.ch)
		if not passChannel:
			return

		# veto events in nominal ttbar overlapping with the mtt sliced samples
		# commented now as it is not available in mc15c
		#if sel.mcChannelNumber == '410000':
		#    if sel.MC_ttbar_beforeFSR_m > 1.1e6:
		#        return

		self.h["yields"][syst].Fill(1, w)
		l = ROOT.TLorentzVector()
		if len(sel.el_pt) == 1:
			l.SetPtEtaPhiE(sel.el_pt[0], sel.el_eta[0], sel.el_phi[0], sel.el_e[0])
		elif len(sel.mu_pt) == 1:
			l.SetPtEtaPhiE(sel.mu_pt[0], sel.mu_eta[0], sel.mu_phi[0], sel.mu_e[0])
		self.h["lepPt"][syst].Fill(l.Perp()*1e-3, w)
		self.h["lepEta"][syst].Fill(l.Eta(), w)
		self.h["lepPhi"][syst].Fill(l.Phi(), w)
		self.h["MET"][syst].Fill(sel.met_met*1e-3, w)
		njets = len(sel.jet_pt)
		if njets >= 4:
			njets = 4
		q = 0
		if len(sel.el_pt) == 1:
			q = sel.el_charge[0]
		elif len(sel.mu_pt) == 1:
			q = sel.mu_charge[0]
		self.h["nJets"][syst].Fill(njets, w)
		if q > 0:
			self.h["nJetsPos"][syst].Fill(njets, w)
		elif q < 0:
			self.h["nJetsNeg"][syst].Fill(njets, w)
		self.h["mwt"][syst].Fill(math.sqrt(2*l.Perp()*sel.met_met*(1 - math.cos(l.Phi() - sel.met_phi)))*1e-3, w)
	def end(self):
		print "Yield for channel ", self.ch, self.h["yields"][""].GetBinContent(1)
		self.write()

