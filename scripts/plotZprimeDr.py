#!/usr/bin/env python
from os import path

from ROOT import *

Internal = True
#Internal = False

files = "/nfs/dust/atlas/user/danilo/plots2/"

L = 36.09e3

chs  = {}

chs["be"] = ["be3", "be2", "be1"]
chs["bmu"] = ["bmu3", "bmu2", "bmu1"]

gStyle.SetOptStat(0)
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)

def stampATLAS(text, x, y):
  t = TLatex()
  t.SetNDC()
  t.SetTextFont(72)
  t.SetTextColor(1)
  delx = 0.115*696*gPad.GetWh()/(472*gPad.GetWw()) + 0.04
  t.SetTextSize(0.06)
  t.DrawLatex(x,y,"ATLAS")
  t.SetTextFont(42)
  t.SetTextSize(0.05)
  t.DrawLatex(x+delx, y, text)

def stampLumiText(lumi, x, y, text, size):
  t = TLatex()
  t.SetNDC()
  t.SetTextFont(42)
  t.SetTextColor(1)
  t.SetTextSize(size)
  #t.DrawLatex(x,y,"#int L dt = "+str(lumi)+" fb^{-1}, "+text)
  if lumi > 0:
    t.DrawLatex(x,y, text+", "+str(lumi)+" fb^{-1}")
  else:
    t.DrawLatex(x,y, text)

def stampText(x, y, text, size):
  t = TLatex()
  t.SetNDC()
  t.SetTextFont(42)
  t.SetTextColor(1)
  t.SetTextSize(size)
  t.DrawLatex(x,y, text)


def setStyle(h, col, sty):
    h.GetYaxis().SetTitle("Arbitrary units")
    h.GetXaxis().SetTitle("min #Delta R(lepton, jet)");
    h.GetXaxis().SetTitleOffset(1.0);
    h.GetYaxis().SetTitleOffset(1.0);
    h.GetXaxis().SetLabelSize(0.05);
    h.GetXaxis().SetTitleSize(0.05);
    h.GetYaxis().SetLabelSize(0.05);
    h.GetYaxis().SetTitleSize(0.05);
    h.SetLineWidth(3);
    h.SetLineStyle(sty);
    h.SetLineColor(col);

def drawIt(hr, channels, label, suf = ""):
  cacc = TCanvas("c", "", 800, 600);
  cacc.SetBottomMargin(0.2)
  cacc.SetLeftMargin(0.14)
  l = TLegend(0.7,0.75,0.87,0.89)
  l.SetBorderSize(0)

  ymax = 0.1
  for i in sorted(channels.keys()):
    if hr[i].GetBinContent(hr[i].GetMaximumBin()) > ymax:
      ymax = hr[i].GetBinContent(hr[i].GetMaximumBin())
  ymax *= 1.4

  first = True
  for i in sorted(channels.keys()):
    hr[i].GetYaxis().SetRangeUser(0, ymax)
    if first:
      hr[i].Draw("hist");
    else:
      hr[i].Draw("hist same");
    first = False
    l.AddEntry(hr[i], channels[i], "L")
  
  l.Draw()
  gPad.RedrawAxis()

  if Internal:
    stampATLAS("Simulation Internal", 0.18, 0.83)
  else:
    stampATLAS("Simulation", 0.18, 0.83)
  stampLumiText(-1, 0.18, 0.75, "#sqrt{s} = 13 TeV", 0.04)
  stampText(0.18, 0.70, label, 0.04)

  suf += ""
  if not Internal:
    suf += "_ATLASSimul"
  for i in [".eps", ".png", ".pdf"]:
    cacc.SaveAs("zprimeDr"+suf+i)

def doIt(suf, extratitle, samples):
  import array

  histname = "closestJetDr"

  f = {}
  hr = {}
  htotal = {}
  for k in chs:
    htotal[k] = {}
  for k in chs:
    for i in chs[k]:
      f[i] = {}
      hr[i] = {}
      for s in samples:
        f[i][s] = TFile.Open("%s/%s_%s.root" % (files, i, s), "read")
        h = f[i][s].Get(histname)
        hr[i][s] = h.Clone("hist_%s_%s_%s" % (histname, i, s))
        #h.Rebin(len(binning) - 1, "hist_%s_%s_%s" % (histname, i, s), array.array('d', binning))
        if not "qcd" in s:
          hr[i][s].Scale(L)
  for k in chs:
    for i in chs[k]:
      for s in samples:
        if not s in htotal[k]:
          htotal[k][s] = hr[i][s].Clone("htotal_%s_%s" % (histname, k))
        else:
          htotal[k][s].Add(hr[i][s])
      
  st_color = kRed
  st_line = 1
  scount = 0
  for s in samples:
    if scount == 0: st_color = kRed
    if scount == 1: st_color = kBlue
    for k in chs:
      setStyle(htotal[k][s], st_color,  st_line)
      htotal[k][s].Scale(1.0/htotal[k][s].Integral())
    scount += 1

  drawIt(htotal["be"], samples, "boosted e+jets "+extratitle, suf = "be"+suf)
  drawIt(htotal["bmu"], samples, "boosted #mu+jets "+extratitle, suf = "bmu"+suf)

# call it
total = ["ttall", "wbbccjets", "wcjets", "wljets", "zjets", "vv", "ttv", "singletop", "qcde", "qcdmu"]
doIt("", "", {"zprime1000": "Z' @ 1 TeV", "zprime2000": "Z' @ 2 TeV"})

