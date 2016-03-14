
from ROOT import *

from os import system
system("cp -f hist_data.root hist_data_inj.root")

mu = -2.0

f = TFile("hist_data_inj.root", "update")
fs = TFile("hist_Zprime3000.root")
for i in ["xmttboostede", "xmttboostedmu", "xlargeJetMboostede", "xlargeJetMboostedmu", "xlargeJetPtboostede", "xlargeJetPtboostedmu"]:
    h = f.Get(i)
    hs = fs.Get(i)
    h.Add(hs, mu)
    h.Write(i, TObject.kOverwrite)
