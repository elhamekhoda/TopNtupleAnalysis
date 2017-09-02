
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

samples = ["ttall"]

histList = ["mtt"]

systs = {'highMtt': 1.0, 'lowMtt': -1.0}

ref_low = "ttradlo"
ref_high = "ttradhi"


for i in samples:
  for j in ch:
    x0 = 1.7e3
    if 'b' in ch:
      x0 = 1.7e3
    elif 'r' in ch:
      x0 = 1e3
    fref_low = ROOT.TFile.Open("%s/%s_%s.root" % (target, j, ref_low), "read")
    fref_high = ROOT.TFile.Open("%s/%s_%s.root" % (target, j, ref_high), "read")
    ftar = ROOT.TFile.Open("%s/%s_%s.root" % (target, j, i), "update")
    for hist in histList:
      href_in_target = ftar.Get(hist)
      href_low = fref_low.Get(hist)
      href_high = fref_high.Get(hist)
      normDiff = math.fabs(href_low.Integral() - href_high.Integral())*0.5
      for k in systs:
        hsyst = href_in_target.Clone("%s%s" % (hist, k))
	for b in range(1, hsyst.GetNbinsX()+1):
	  y = hsyst.GetBinContent(b)
	  x = hsyst.GetXaxis().GetBinCenter(b)
	  var = (x**2 - x0**2)/(x**2 + x0**2)
	  hsyst.SetBinContent(b, y*(1 + normDiff*systs[k]*var))
        ftar.cd()
        hsyst.Write("%s%s" % (hist, k), ROOT.TObject.kOverwrite)
