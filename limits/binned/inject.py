
from ROOT import *

from os import system
#system("cp -f hist_bkg.root hist_data_inj.root")

mu = -1.0

fb = TFile("hist_bkg.root")
f = TFile("hist_data_inj.root", "recreate")
fs = TFile("hist_Zprime3000.root")
for i in ["xmttboostede", "xmttboostedmu", "xlargeJetMboostede", "xlargeJetMboostedmu", "xlargeJetPtboostede", "xlargeJetPtboostedmu"]:
    hb = fb.Get(i)
    hs = fs.Get(i)
    f.cd()
    h = hb.Clone(i+"clone")
    h.Add(hs, mu)
    for b in range(0,h.GetNbinsX()+1):
        if h.GetBinContent(b) < 0:
            h.SetBinContent(b, 0)
    f.cd()
    h.Write(i, TObject.kOverwrite)
