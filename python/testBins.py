#!/usr/bin/env python

import math
import ROOT
from optparse import OptionParser
from array import array

def getBinning(h, hs, threshold):
  pos = 1
  binning = [1]
  binEdges = [h.GetXaxis().GetBinLowEdge(1)]
  while pos < h.GetNbinsX()+1:
    currentBin = h.GetXaxis().GetBinLowEdge(pos)

    contentFromLastBin = 0
    errorFromLastBin = 0
    contentFromLastBinS = [0]*len(hs)
    errorFromLastBinS = [0]*len(hs)

    binAfterLast = 1
    if len(binning) > 1:
      binAfterLast = binning[-1]+1

    # for background
    for k in range(binAfterLast, pos):
      contentFromLastBin += h.GetBinContent(k)
      errorFromLastBin += h.GetBinError(k)**2
    errorFromLastBin = errorFromLastBin**0.5

    # for signal
    for i in range(len(hs)):
      for k in range(binAfterLast, pos):
        contentFromLastBinS[i] += hs[i].GetBinContent(k)
        errorFromLastBinS[i] += hs[i].GetBinError(k)**2
      errorFromLastBinS[i] = errorFromLastBinS[i]**0.5

    if contentFromLastBin == 0:
      contentFromLastBin = 1e-10
    for i in range(len(hs)):
      if contentFromLastBinS[i] == 0:
        contentFromLastBinS[i] = 1e-10

    ratio = errorFromLastBin/contentFromLastBin
    ratioS = [0]*len(hs)
    for i in range(len(hs)): ratioS[i] = errorFromLastBinS[i]/contentFromLastBinS[i]
    ratioSor = min(ratioS)

    if max([ratio, ratioSor]) < threshold:
      binning.append(pos)
      binEdges.append(currentBin)
    # else, we need to add more bins
    pos += 1
  if binning[-1] != pos:
    binning.append(pos)
    binEdges.append(h.GetXaxis().GetBinLowEdge(pos))


  return [binning, binEdges]

def fillStat(s, rs, h):
  for i in range(1, h.GetNbinsX()):
    s.SetPoint(i-1, h.GetBinCenter(i), h.GetBinError(i))
    if h.GetBinContent(i) > 0:
      rs.SetPoint(i-1, h.GetXaxis().GetBinLowEdge(i), h.GetBinError(i)/h.GetBinContent(i))
    else:
      rs.SetPoint(i-1, h.GetXaxis().GetBinLowEdge(i), 0)


def main():

  parser = OptionParser()
  parser.add_option("-f", "--file",
                    dest="file", default="re_ttPlusWjets.root",
                    help="Input background file.", metavar="FILE")
  parser.add_option("-s", "--signal",
                    dest="signal", default="re_Zprime400.root,re_Zprime500.root,re_Zprime750.root,re_Zprime1000.root,re_Zprime1250.root,re_Zprime1500.root,re_Zprime1750.root,re_Zprime2000.root,re_Zprime2250.root,re_Zprime2500.root,re_Zprime2750.root,re_Zprime3000.root,re_Zprime4000.root,re_Zprime5000.root",
                    help="Input signal files.", metavar="FILES")
  parser.add_option("-t", "--threshold",
                    dest="threshold", default="0.05",
                    help="Maximum allowed statistical error.", metavar="STATERROR")
  parser.add_option("-H", "--histogram",
                    dest="histogram", default="mtt",
                    help="Histogram to choose binning", metavar="HISTOGRAM")
  (options, args) = parser.parse_args()

  threshold = float(options.threshold)

  fb = ROOT.TFile(options.file)
  hb = fb.Get(options.histogram)

  fs = []
  hs = []
  for i in options.signal.split(','):
    fs.append(ROOT.TFile(i))
    hs.append(fs[-1].Get(options.histogram))

  [binning, binEdges] = getBinning(hb, hs, threshold)
  print "binning found: ", binning, binEdges

  hbrebin = hb.Rebin(len(binEdges)-1, hb.GetName()+"rebin", array('d', binEdges))
  gstat = ROOT.TGraph(hb.GetNbinsX()-1)
  grelstat = ROOT.TGraph(hb.GetNbinsX()-1)
  grstat = ROOT.TGraph(hbrebin.GetNbinsX()-1)
  grrelstat = ROOT.TGraph(hbrebin.GetNbinsX()-1)

  gsstat = []
  gsrelstat = []
  gsrstat = []
  gsrrelstat = []

  hsrebin = []
  for i in range(len(hs)):
    hsrebin.append(hs[i].Rebin(len(binEdges)-1, hs[i].GetName()+"rebin", array('d', binEdges)))
    gsstat.append(ROOT.TGraph(hb.GetNbinsX()-1))
    gsrelstat.append(ROOT.TGraph(hb.GetNbinsX()-1))
    gsrstat.append(ROOT.TGraph(hbrebin.GetNbinsX()-1))
    gsrrelstat.append(ROOT.TGraph(hbrebin.GetNbinsX()-1))

  fillStat(gstat, grelstat, hb)
  fillStat(grstat, grrelstat, hbrebin)

  for i in range(len(hs)):
    fillStat(gsstat[i], gsrelstat[i], hs[i])
    fillStat(gsrstat[i], gsrrelstat[i], hsrebin[i])

  suf = "bkg"
  plotImpact([gstat, grelstat, grstat, grrelstat], ["Statistical unc.", "Relative stat. unc. [%]", "Statistical unc.", "Relative stat. unc. [%]"], ["stat_%s.eps" % suf, "statrel_%s.eps" %suf, "stat_rebin_%s.eps" %suf, "statrel_rebin_%s.eps" %suf])
  for i in range(len(hs)):
    suf = "signal%d" % i
    plotImpact([gsstat[i], gsrelstat[i], gsrstat[i], gsrrelstat[i]], ["Statistical unc.", "Relative stat. unc. [%]", "Statistical unc.", "Relative stat. unc. [%]"], ["stat_%s.eps" % suf, "statrel_%s.eps" %suf, "stat_rebin_%s.eps" %suf, "statrel_rebin_%s.eps" %suf])


def plotImpact(glist, tlist, nlist):
  for g in range(0, len(glist)):
    c = ROOT.TCanvas("c", "", 800, 600)
    glist[g].GetXaxis().SetTitle("m_{tt} [GeV]")
    glist[g].GetYaxis().SetTitle(tlist[g])
    if "statrel" in nlist[g]:
      glist[g].GetYaxis().SetRangeUser(0, 1)
      glist[g].SetMinimum(0.0)
      glist[g].SetMaximum(1.0)
    glist[g].Draw("ac*")
    if "statrel" in nlist[g]:
      l = ROOT.TLine(glist[g].GetX()[0], threshold, glist[g].GetX()[glist[g].GetN()-1], threshold)
      l.SetLineColor(ROOT.kBlack)
      l.SetLineWidth(2)
      l.SetLineStyle(ROOT.kDashed)
      l.Draw()
    c.SaveAs(nlist[g])

if __name__ == "__main__":
  main()

