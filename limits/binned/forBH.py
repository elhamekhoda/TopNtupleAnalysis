

import ROOT

def main():
  chs = ['bmu3', 'bmu2', 'bmu1', 'be3', 'be2', 'be1', 'rmu3', 'rmu2', 'rmu1', 're3', 're2', 're1']
  f = ROOT.TFile("forBH.root", "recreate")
  for c in chs:
    fi = ROOT.TFile("%s_postFit.root" % c, "read")
    htot = fi.Get("h_tot_postFit").Clone("bkg_%s" % c)
    gtot_syst = fi.Get("g_totErr_postFit")
    htot_syst = htot.Clone("bkg_syst_%s" % c)
    for j in range(1, htot.GetNbinsX()+1):
      htot_syst.SetBinContent(j, htot_syst.GetBinContent(j) + gtot_syst.GetErrorYhigh(j-1))
    hdata = fi.Get("h_Data").Clone("data_%s" % c)
    f.cd()
    htot.Write("bkg_%s" % c, ROOT.TObject.kOverwrite)
    htot_syst.Write("bkg_syst_%s" % c, ROOT.TObject.kOverwrite)
    hdata.Write("data_%s" % c, ROOT.TObject.kOverwrite)
main()
