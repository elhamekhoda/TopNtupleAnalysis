
from ROOT import *

from os import system
#system("cp -f hist_bkg.root hist_data_inj.root")

stepSize = -0.25 # 25% discrepancy
firstBin = 2e3
lastBin = 3e3

fb = TFile("hist_bkg.root")
f = TFile("hist_data_inj.root", "recreate")
for i in ["xmttboostede", "xmttboostedmu", "xlargeJetMboostede", "xlargeJetMboostedmu", "xlargeJetPtboostede", "xlargeJetPtboostedmu"]:
    hb = fb.Get(i)
    f.cd()
    h = hb.Clone(i+"clone")
    for b in range(1, h.GetNbinsX()):
        if h.GetXaxis().GetBinCenter(b) > firstBin and h.GetXaxis().GetBinCenter(b) < lastBin:
            if h.GetBinContent(b)*(1 + stepSize) > 0:
                h.SetBinContent(b, floor(h.GetBinContent(b)*(1 + stepSize)))
            else:
                h.SetBinContent(b, 0)
        else:
            h.SetBinContent(b, floor(h.GetBinContent(b)))
    f.cd()
    h.Write(i, TObject.kOverwrite)
