
from ROOT import *

from os import system
system("cp -f hist_bkg.root hist_data_inj.root")

stepSize = -0.25 # 25% discrepancy
firstBin = 2e3
lastBin = 3e3

f = TFile("hist_data_inj.root", "update")
for i in ["xmttboostede", "xmttboostedmu", "xlargeJetMboostede", "xlargeJetMboostedmu", "xlargeJetPtboostede", "xlargeJetPtboostedmu"]:
    h = f.Get(i)
    for b in range(1, h.GetNbinsX()):
        if h.GetXaxis().GetBinCenter(b) > firstBin and h.GetXaxis().GetBinCenter(b) < lastBin:
            h.SetBinContent(b, h.GetBinContent(b)*(1 + stepSize))
    f.cd()
    h.Write(i, TObject.kOverwrite)
