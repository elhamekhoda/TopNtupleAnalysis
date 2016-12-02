#!/usr/bin/env python

import math
import ROOT
from optparse import OptionParser
from array import array

def getBinning(h, threshold):
  pos = 1
  binning = [1]
  binEdges = [h.GetXaxis().GetBinLowEdge(1)]
  while pos < h.GetNbinsX()+1:
    currentBin = h.GetXaxis().GetBinLowEdge(pos)
    contentFromLastBin = 0
    errorFromLastBin = 0
    binAfterLast = 1
    if len(binning) > 1:
      binAfterLast = binning[-1]+1
    for k in range(binAfterLast, pos):
      contentFromLastBin += h.GetBinContent(k)
      errorFromLastBin += h.GetBinError(k)**2
    errorFromLastBin = errorFromLastBin**0.5
    if contentFromLastBin == 0:
      pos += 1
      continue
    if errorFromLastBin/contentFromLastBin < threshold:
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
                    dest="file", default="re_ttall.root",
                    help="Input file.", metavar="FILE")
  parser.add_option("-t", "--threshold",
                    dest="threshold", default="0.05",
                    help="Maximum allowed statistical error.", metavar="STATERROR")
  parser.add_option("-H", "--histogram",
                    dest="histogram", default="mtt",
                    help="Histogram to choose binning", metavar="HISTOGRAM")
  (options, args) = parser.parse_args()

  infile = options.file
  threshold = float(options.threshold)

  f = ROOT.TFile(infile)
  h = f.Get(options.histogram)

  [binning, binEdges] = getBinning(h, threshold)
  print "binning found: ", binning, binEdges

  hrebin = h.Rebin(len(binEdges)-1, h.GetName()+"rebin", array('d', binEdges))

  gstat = ROOT.TGraph(h.GetNbinsX()-1)
  grelstat = ROOT.TGraph(h.GetNbinsX()-1)

  grstat = ROOT.TGraph(hrebin.GetNbinsX()-1)
  grrelstat = ROOT.TGraph(hrebin.GetNbinsX()-1)

  fillStat(gstat, grelstat, h)
  fillStat(grstat, grrelstat, hrebin)

  glist = [gstat, grelstat, grstat, grrelstat]
  tlist = ["Statistical unc.", "Relative stat. unc. [%]", "Statistical unc.", "Relative stat. unc. [%]"]
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
      l = ROOT.TLine(glist[g].GetX()[0], threshold, glist[g].GetX()[glist[g].GetN()-1], threshold)
      l.SetLineColor(ROOT.kBlack)
      l.SetLineWidth(2)
      l.SetLineStyle(ROOT.kDashed)
      l.Draw()
    c.SaveAs(nlist[g])

if __name__ == "__main__":
  main()

