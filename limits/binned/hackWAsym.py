
import ROOT
import math
import os

ref_syst = "../hists2429_corr_local_wjets_asym/"
target = "./"

ch = []
ch += ["bmu%d" % x for x in [3,2,1,0]]
ch += ["rmu%d" % x for x in [3,2,1,0]]
ch += ["be%d" % x for x in [3,2,1,0]]
ch += ["re%d" % x for x in [3,2,1,0]]
ch += ["bmu", "be", "re", "rmu"]

samples = ["wbbccjets", "wcjets", "wljets"]

tmp = "CAallMCAsym,wbb__1up,wbb__1down,wl__1up,wl__1down"
systs = tmp.split(",")

histList = ["mtt", "closestJetDr", "lepPt", "lepEta", "nJets", "nTrkBtagJets", "mwt", "MET", "MET_phi", "closestJetPt", "largeJetPt", "largeJetM", "yields", "largeJetPtMtt", "largeJetEta", "largeJetPhi", "mtlep_boo", "mtlep_res", "mthad_res", "mwhad_res", "chi2", "largeJet_tau32_wta", "largeJet_tau21_wta"]
for i in samples:
  for j in ch:
    fref = ROOT.TFile.Open("%s/%s_%s.root" % (ref_syst, j, i), "read")
    ftar = ROOT.TFile.Open("%s/%s_%s.root" % (target, j, i), "update")
    for hist in histList:
      hnom = fref.Get(hist)
      href_in_target = ftar.Get(hist)
      for k in systs:
        hsyst = fref.Get("%s%s" % (hist, k))
	hsyst.Add(hnom, -1)
        hsyst.Divide(hnom)
        ftar.cd()
        hnew = hsyst.Clone("%s%s" % (hist, k))
        hnew.Multiply(href_in_target)
        hnew.Add(href_in_target)
	if hnew.Integral() != 0:
          print hist, k, "var/nominal = ", hnew.Integral()/href_in_target.Integral()
        ftar.cd()
        hnew.Write("%s%s" % (hist, k), ROOT.TObject.kOverwrite)
