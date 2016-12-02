#!/usr/bin/env python

import math
import ROOT
from optparse import OptionParser

def getBinning(h):
  pos = 1
  binning = []
  binEdges = []
  while pos < h.GetNbinsX():
    currentBin = h.GetXaxis().GetBinLowEdge(pos)
    if pos == 1:
      binning.append(pos)
      binEdges.append(currentBin)
      pos += 1
      continue
    contentFromLastBin = 0
    errorFromLastBin = 0
    for k in range(binning[-1]+1, pos+1):
      contentFromLastBin += h.GetBinContent(k)
      errorFromLastBin += h.GetBinError(k)**2
    errorFromLastBin = errorFromLastBin**0.5
    if contentFromLastBin == 0:
      pos += 1
      continue
    elif errorFromLastBin/contentFromLastBin < threshold:
      binning.append(pos)
      binEdges.append(currentBin)
      pos += 1
    # else, we need to add more bins
    pos += 1

  return [binning, binEdges]

def fillStat(s, rs, h):
  for i in range(1, h.GetNbinsX()):
    s.SetPoint(i-1, h.GetBinCenter(i), h.GetBinError(i))
    if h.GetBinContent(i) > 0:
      rs.SetPoint(i-1, h.GetBinCenter(i), h.GetBinError(i)/h.GetBinContent(i))
    else:
      rs.SetPoint(i-1, h.GetBinCenter(i), 0)


def main():

  parser = OptionParser()
  parser.add_option("-f", "--file",
                    dest="file", default="re_ttbar.root",
                    help="Input file.", metavar="FILE")
  parser.add_option("-t", "--threshold",
                    dest="threshold", default="0.05",
                    help="Maximum allowed statistical error.", metavar="STATERROR")
  parser.add_option("-h", "--histogram",
                    dest="histogram", default="mtt",
                    help="Histogram to choose binning", metavar="HISTOGRAM")
  (options, args) = parser.parse_args()

  infile = options.file
  threshold = float(options.threshold)

  f = ROOT.TFile(infile)
  h = f.Get(options.histogram)

  [binning, binEdges] = getBinning(h)
  print "binning found: ", binning, binEdges

  hrebin = h.Rebin(len(binEdges)-1, h.GetName()+"rebin", array('d', binEdges))

  gstat = ROOT.TGraph(h.GetNbinsX())
  grelstat = ROOT.TGraph(h.GetNbinsX())

  grstat = ROOT.TGraph(hrebin.GetNbinsX())
  grrelstat = ROOT.TGraph(hrebin.GetNbinsX())

  fillStat(gstat, grelstat, h)
  fillStat(grstat, grrelstat, h)

  glist = [gstat, grelstat, grstat, grrelstat]
  tlist = ["Statistical unc.", "Relative stat. unc. [\%]", "Statistical unc.", "Relative stat. unc. [\%]"]
  nlist = ["stat.eps", "statrel.eps", "stat_rebin.eps", "statrel_rebin.eps"]

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
      l = ROOT.TLine(h.GetXaxis().GetBinLowEdge(1), threshold, h.GetXaxis().GetBinUpEdge(h.GetNbinsX()), threshold)
      l.SetLineColor(ROOT.kBlack)
      l.SetLineWidth(2)
      l.SetLineStyle(ROOT.kDashed)
      l.Draw()
    c.SaveAs(nlist[g])

if __name__ == "__main__":
  main()

