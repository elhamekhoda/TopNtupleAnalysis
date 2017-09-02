
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
ch += ["bmuX", "beX", "reX", "rmuX"]

samples = ["qcde", "qcdmu"]

histList = ["mtt", "closestJetDr", "lepPt", "lepEta", "nJets", "nTrkBtagJets", "mwt", "MET", "MET_phi", "closestJetPt", "largeJetPt", "largeJetM", "yields", "largeJetPtMtt", "largeJetEta", "largeJetPhi", "mtlep_boo", "mtlep_res", "mthad_res", "mwhad_res", "chi2", "largeJet_tau32_wta", "largeJet_tau21_wta"]

scale = 15.0/36.09

systs = ["", "qcdcenup", "qcdcendw", "qcdfwdup", "qcdfwddw"]

for i in samples:
  for j in ch:
    os.system("cp %s/%s_%s.root %s/%s_%s.root" % (".", j, i, ".", j, i+"_15ifb"))
    ftar = ROOT.TFile.Open("%s/%s_%s.root" % (".", j, i+"_15ifb"), "update")
    for hist in histList:
      for k in systs:
        hsyst = ftar.Get("%s%s" % (hist, k))
	if not isinstance(hsyst, ROOT.TH1D):
	  print "Could not get %s in %s" % ("%s%s" % (hist, k), ftar.GetName())
	  continue
	hsyst.Scale(scale)
        ftar.cd()
        hsyst.Write("%s%s" % (hist, k), ROOT.TObject.kOverwrite)
