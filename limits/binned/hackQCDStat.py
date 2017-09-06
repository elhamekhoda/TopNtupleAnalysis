
import ROOT
import math
import os

target = "./"

ch = []
ch += ["bmu%d" % x for x in [3,2,1,0]]
ch += ["rmu%d" % x for x in [3,2,1,0]]
ch += ["be%d" % x for x in [3,2,1,0]]
ch += ["re%d" % x for x in [3,2,1,0]]
ch += ["bmu", "be", "re", "rmu"]

samples = ["qcde", "qcdmu"]

histList = ["mtt", "closestJetDr", "lepPt", "lepEta", "nJets", "nTrkBtagJets", "mwt", "MET", "MET_phi", "closestJetPt", "largeJetPt", "largeJetM", "yields", "largeJetPtMtt", "largeJetEta", "largeJetPhi", "mtlep_boo", "mtlep_res", "mthad_res", "mwhad_res", "chi2", "largeJet_tau32_wta", "largeJet_tau21_wta"]

systs = {'qcdstatup': 1.0, 'qcdstatdw': -1.0}

for i in samples:
    for j in ch:
        ftar = ROOT.TFile.Open("%s/%s_%s.root" % (target, j, i), "update")
        for hist in histList:
            href_in_target = ftar.Get(hist)
            for k in systs:
                hsyst = href_in_target.Clone("%s%s" % (hist, k))
                for b in range(1, hsyst.GetNbinsX()+1):
                    y = hsyst.GetBinContent(b)
                    ye = systs[k]*hsyst.GetBinError(b)
                    res = y + ye
                    if res < 0: res = 0
                    hsyst.SetBinContent(b, res)
                ftar.cd()
                hsyst.Write("%s%s" % (hist, k), ROOT.TObject.kOverwrite)
