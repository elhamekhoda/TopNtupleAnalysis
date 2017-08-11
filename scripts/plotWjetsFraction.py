#!/usr/bin/env python
from os import path

from ROOT import *

Internal = True
#Internal = False

files = "/nfs/dust/atlas/user/danilo/hists2429_local/"


chs  = []

chs += ["be%d" % i for i in [1,2,3]]
chs += ["bmu%d" % i for i in [1,2,3]]
chs += ["re%d" % i for i in [1,2,3]]
chs += ["rmu%d" % i for i in [1,2,3]]

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
    h.GetYaxis().SetTitle("Background fraction")
    h.GetXaxis().SetTitle("m_{t#bar{t}} [TeV]");
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

  ymax = 0.10
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
    cacc.SaveAs("wjetsfrac"+suf+i)

def doIt(suf, extratitle, samples, numerator):
  import array

  histname = "mtt"

  f = {}
  hr = {}
  hratio = {}
  hnum = {}
  htotal = {}
  for i in chs:
    binning = [430, 600, 810, 1010, 1220, 1440, 2000]
    if "b" in i:
      binning = [480,720,1040,1400,1700,2000,2600,6000]
    f[i] = {}
    hr[i] = {}
    for s in samples:
      f[i][s] = TFile.Open("%s/%s_%s.root" % (files, i, s), "read")
      h = f[i][s].Get(histname)
      hr[i][s] = h.Rebin(len(binning) - 1, "hist_%s_%s_%s" % (histname, i, s), array.array('d', binning))
      if s in numerator:
        if not i in hnum:
          hnum[i] = hr[i][s].Clone("hnum_%s_%s" % (histname, i))
	else:
          hnum[i].Add(hr[i][s])
      if not i in htotal:
        htotal[i] = hr[i][s].Clone("htotal_%s_%s" % (histname, i))
      else:
        htotal[i].Add(hr[i][s])

  for i in chs:
    hratio[i] = hnum[i].Clone("ratio_%s_%s" % (histname, i))
    hratio[i].Divide(hnum[i], htotal[i], 1, 1)

  for i in chs:
    st_color = kRed
    st_line = 1
    cat = 0
    if "3" in i: cat = kRed
    if "2" in i: cat = kBlue
    if "1" in i: cat = kMagenta
    st_color = cat
    #if "be" in i:
    #  st_color = kRed+cat
    #  st_line = 1
    #elif "bmu" in i:
    #  st_color = kRed+cat
    #  st_line = 1
    #elif "re" in i:
    #  st_color = kBlue+cat
    #  st_line = 1
    #elif "rmu" in i:
    #  st_color = kBlue+cat
    #  st_line = 1
    setStyle(hratio[i], st_color,  st_line)

  drawIt(hratio, {"be3": "Cat. 3", "be2": "Cat. 2", "be1": "Cat. 1"}, "boosted e+jets "+extratitle, suf = "becat"+suf)
  drawIt(hratio, {"bmu3": "Cat. 3", "bmu2": "Cat. 2", "bmu1": "Cat. 1"}, "boosted #mu+jets "+extratitle, suf = "bmucat"+suf)
  drawIt(hratio, {"re3": "Cat. 3", "re2": "Cat. 2", "re1": "Cat. 1"}, "resolved e+jets "+extratitle, suf = "recat"+suf)
  drawIt(hratio, {"rmu3": "Cat. 3", "rmu2": "Cat. 2", "rmu1": "Cat. 1"}, "resolved #mu+jets "+extratitle, suf = "rmucat"+suf)

# call it
doIt("", "W+jets/Total", ["ttall", "wbbjets", "wccjets", "wcjets", "wljets", "zjets", "vv", "ttv", "singletop"], ["wbbjets", "wccjets", "wcjets", "wljets"])
doIt("bb", "W+bb+jets/Total", ["wbbjets", "wccjets", "wcjets", "wljets", "zjets", "vv", "ttv", "singletop", "ttall"], ["wbbjets"])
doIt("cc", "W+cc+jets/Total", ["wbbjets", "wccjets", "wcjets", "wljets", "zjets", "vv", "ttv", "singletop", "ttall"], ["wccjets"])
doIt("c", "W+c+jets/Total", ["wbbjets", "wccjets", "wcjets", "wljets", "zjets", "vv", "ttv", "singletop", "ttall"], ["wcjets"])
doIt("l", "W+l+jets/Total", ["wbbjets", "wccjets", "wcjets", "wljets", "zjets", "vv", "ttv", "singletop", "ttall"], ["wljets"])

