
import ROOT
import math
import os

ref = "../../hists2429_local/"
ref_syst = "bkp/"

ch = ["bmu2"]
samples = ["tt"]

tmp = "LARGERJET_Medium_JET_Comb_Baseline_Kin__1up,LARGERJET_Medium_JET_Comb_Baseline_Kin__1down,LARGERJET_Medium_JET_Comb_Modelling_Kin__1up,LARGERJET_Medium_JET_Comb_Modelling_Kin__1down,LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up,LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down,LARGERJET_Medium_JET_Comb_Tracking_Kin__1up,LARGERJET_Medium_JET_Comb_Tracking_Kin__1down,LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up,LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down,LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up,LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down,LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up,LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down,LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up,LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down,CORR_LargeRSmallR_A__1up,CORR_LargeRSmallR_A__1down,CORR_LargeRSmallR_B__1up,CORR_LargeRSmallR_B__1down,CORR_LargeRSmallR_C__1up,CORR_LargeRSmallR_C__1down,LARGERJET_JER_LARGERJET_JER_PT__1up,LARGERJET_JER_LARGERJET_JER_TAU32__1up,LARGERJET_JER_LARGERJET_JER_MASS__1up"
systs = tmp.split(",")

histList = ["mtt", "closestJetDr", "lepPt", "lepEta", "nJets", "nTrkBtagJets", "mwt", "MET", "MET_phi", "closestJetPt", "largeJetPt", "largeJetM", "yields", "largeJetPtMtt", "largeJetEta", "largeJetPhi", "mtlep_boo", "mtlep_res", "mthad_res", "mwhad_res", "chi2", "largeJet_tau32_wta", "largeJet_tau21_wta"]
for i in samples:
  for j in ch:
    fs = ROOT.TFile.Open("%s/%s_%s.root" % (ref_syst, j, i), "read")
    fr = ROOT.TFile.Open("%s/%s_%s.root" % (ref, j, i), "read")
    os.system("cp %s/%s_%s.root %s/%s_%s.root" % (ref, j, i, ".", j, i))
    fnew = ROOT.TFile.Open("%s/%s_%s.root" % (".", j, i), "update")
    for hist in histList:
      hsn = fs.Get(hist)
      hr = fr.Get(hist)
      for k in systs:
        hsv = fs.Get("%s%s" % (hist, k))
	hsv.Add(hsn, -1)
        hsv.Divide(hsn)
        fnew.cd()
        hnew = hr.Clone("%s%s" % (hist, k))
        hnew.Multiply(hsv)
        hnew.Add(hr)
	if hr.Integral() != 0:
          print hist, k, "var/nominal = ", hnew.Integral()/hr.Integral()
        fnew.cd()
        hnew.Write("%s%s" % (hist, k), ROOT.TObject.kOverwrite)
