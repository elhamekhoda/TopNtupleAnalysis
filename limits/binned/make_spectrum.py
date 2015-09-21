
from ROOT import *
from array import array
import os

L=10e3
#bins = array('f', [0,80,160,240,320,400,480,560,640,720,800,920,1040,1160,1280,1400,1600,1800,2000,2500,3600])
#nbins = 20
bins = array('f', [400,480,560,640,720,800,920,1040,1160,1280,1400,1550,1700,1850,2000,2150,2300,2450,2600,2750,2900,3200,3600,4000,4500, 5000])
nbins = 25

ch = {}
ch["bmu"] = 1
ch["be"] = 0
ch["rmu"] = 2
ch["re"] = 3
chinv = {}
chinv[0] = "be"
chinv[1] = "bmu"
chinv[2] = "rmu"
chinv[3] = "re"

systlist  = [""]
systlist += ["JET_NPScenario1_JET_GroupedNP_1__1up", "JET_NPScenario1_JET_GroupedNP_1__1down"]
systlist += ["JET_NPScenario1_JET_GroupedNP_2__1up", "JET_NPScenario1_JET_GroupedNP_2__1down"]
systlist += ["JET_NPScenario1_JET_GroupedNP_3__1up", "JET_NPScenario1_JET_GroupedNP_3__1down"]
systlist += ["JET_JER_SINGLE_NP__1up"]
systlist += ["MET_SoftTrk_ResoPara"]
systlist += ["MET_SoftTrk_ResoPerp"]
systlist += ["MET_SoftTrk_ScaleUp", "MET_SoftTrk_ScaleDown"]
systlist += ["MUONS_ID__1up", "MUONS_ID__1down"]
systlist += ["MUONS_MS__1up", "MUONS_MS__1down"]
systlist += ["MUONS_SCALE__1up", "MUONS_SCALE__1down"]
systlist += ["EG_RESOLUTION_ALL__1up", "EG_RESOLUTION_ALL__1down"]
systlist += ["EG_SCALE_ALL__1up", "EG_SCALE_ALL__1down"]

def make_hist(pref, slist, clist):
  print "  - Making hists for "+pref
  f = TFile(pref+".root")
  t = f.Get("mini")
  fo = TFile("hist_"+pref+".root", "recreate")
  h = {}
  for syst in slist:
    sufsyst = syst
    for cat in clist:
      h["mtt"+cat+sufsyst] = TH1F("mtt"+cat+sufsyst, "", nbins, bins)
      h["mtt"+cat+sufsyst].Sumw2()

  for i in range(0, t.GetEntries()):
    t.GetEntry(i)
    sufsyst = str(t.syst)
    if not sufsyst in slist:
      continue
    sufcat = chinv[t.cat]
    h["mtt"+sufcat+sufsyst].Fill(t.mtt, L*t.weight)
  fo.cd()
  for histname in h:
    h[histname].Write()

os.system("rm -f hist_*.root")

clist = ["bmu", "be", "re", "rmu"]
for samp in ["ttbar", "zp1tev", "zp125tev", "zp15tev", "zp175tev", "zp2tev", "zp225tev", "zp25tev", "zp275tev", "zp4tev"]:
    make_hist(samp, systlist, clist)

os.system("cp hist_ttbar.root hist_data.root")

