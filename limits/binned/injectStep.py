
from ROOT import *

from os import system
#system("cp -f hist_bkg.root hist_data_inj.root")

stepSizeE = -0.10 # 15% discrepancy
stepSizeMu = -0.20 # 25% discrepancy
firstBinE = 2.0e3
lastBinE = 3.0e3
firstBinMu = 2.3e3
lastBinMu = 3.2e3

fb = TFile("hist_bkg.root")
f = TFile("hist_data_inj.root", "recreate")
for i in ["xmttboostede", "xmttboostedmu", "xlargeJetMboostede", "xlargeJetMboostedmu", "xlargeJetPtboostede", "xlargeJetPtboostedmu"]:
    if 'boostede' in i:
        stepSize = stepSizeE
        firstBin = firstBinE
        lastBin = lastBinE
    elif 'boostedmu' in i:
        stepSize = stepSizeMu
        firstBin = firstBinMu
        lastBin = lastBinMu

    hb = fb.Get(i)
    f.cd()
    h = hb.Clone(i+"clone")
    for b in range(1, h.GetNbinsX()):
        if h.GetXaxis().GetBinCenter(b) > firstBin and h.GetXaxis().GetBinCenter(b) < lastBin:
            if h.GetBinContent(b)*(1 + stepSize) > 0:
                h.SetBinContent(b, round(h.GetBinContent(b)*(1 + stepSize), -1))
            else:
                h.SetBinContent(b, 0)
        else:
            h.SetBinContent(b, floor(h.GetBinContent(b)))
    f.cd()
    h.Write(i, TObject.kOverwrite)
