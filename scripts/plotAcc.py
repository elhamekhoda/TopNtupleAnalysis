#!/usr/bin/env python
from os import path

from ROOT import *

Internal = True
#Internal = False

files = "/nfs/dust/atlas/user/danilo/ntuples_2429/"

label_signal = "Z'"
did_list = []
# zprime
did_list = range(301322, 301335+1)
# KK grav
#did_list = range(305012, 305017+1)
# KK gluon 30%
#did_list = range(307522, 307533+1)


chs  = []

chs += ["be"]
#chs += ["be%d" % i for i in [0,1,2,3]]

chs += ["bmu"]
#chs += ["bmu%d" % i for i in [0,1,2,3]]

chs += ["re"]
#chs += ["re%d" % i for i in [0,1,2,3]]

chs += ["rmu"]
#chs += ["rmu%d" % i for i in [0,1,2,3]]

gStyle.SetOptStat(0)
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)

def stampATLAS(text, x, y):
  t = TLatex()
  t.SetNDC()
  t.SetTextFont(72)
  t.SetTextColor(1)
  delx = 0.115*696*gPad.GetWh()/(472*gPad.GetWw()) + 0.05
  t.SetTextSize(0.06)
  t.DrawLatex(x,y,"ATLAS")
  t.SetTextFont(42)
  t.SetTextSize(0.06)
  t.DrawLatex(x+delx, y, text)

def stampLumiText(lumi, x, y, text, size):
  t = TLatex()
  t.SetNDC()
  t.SetTextFont(42)
  t.SetTextColor(1)
  t.SetTextSize(size)
  #t.DrawLatex(x,y,"#int L dt = "+str(lumi)+" fb^{-1}, "+text)
  t.DrawLatex(x,y, text+", "+str(lumi)+" fb^{-1}")

def stampText(x, y, text, size):
  t = TLatex()
  t.SetNDC()
  t.SetTextFont(42)
  t.SetTextColor(1)
  t.SetTextSize(size)
  t.DrawLatex(x,y, text)


def setStyle(h, col, sty):
    h.GetYaxis().SetRangeUser(0, 10);
    h.GetYaxis().SetTitle("Acceptance #times Efficiency [%]");
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

def cutChannel(ct, i):
  p = False
  if "be" in i:
    if ct.bejets_2015 or ct.bejets_2016:
      p = True
  elif "bmu" in i:
    if ct.bmujets_2015 or ct.bmujets_2016:
      p = True
  elif "re" in i:
    if ct.rejets_2015 or ct.rejets_2016:
      p = True
  elif "rmu" in i:
    if ct.rmujets_2015 or ct.rmujets_2016:
      p = True
  if p:
    b = -1
    if "3" in i:
      b = 3
    elif "2" in i:
      b = 2
    elif "1" in i:
      b = 1
    elif "0" in i:
      b = 0
    if b > 0:
      if ct.Btagcat != b:
        p = False
    else: # remove btag category 0
      if ct.Btagcat == 0:
        p = False
  return p

ct = TChain("truth")
cn = TChain("nominal")

ht = {}
hn = {}
hr = {}
for i in chs:
  ht[i] = TH1F("ht_%s"%i, "", 20, 0.0, 5.0)
  hn[i] = TH1F("hn_%s"%i, "", 20, 0.0, 5.0)
  hr[i] = TH1F("hr_%s"%i, "", 20, 0.0, 5.0)

for i in chs:
  st_color = kRed
  st_line = 1
  if "be" in i:
    st_color = kRed
    st_line = 1
  if "bmu" in i:
    st_color = kRed
    st_line = 2
  if "re" in i:
    st_color = kBlue
    st_line = 1
  if "rmu" in i:
    st_color = kBlue
    st_line = 2
  setStyle(ht[i], st_color,  st_line)
  setStyle(hn[i], st_color,  st_line)
  setStyle(hr[i], st_color,  st_line)

import glob
for did in did_list:
  for d in glob.glob(files+"/user.dferreir.%d.*"%did):
    for f in glob.glob(d+"/*"):
      ct.Add(f)
      cn.Add(f)

for i in xrange(ct.GetEntries()):
  ct.GetEntry(i)
  for i in chs:
    ht[i].Fill(ct.MC_ttbar_beforeFSR_m*1e-6, ct.weight_mc)

for i in xrange(cn.GetEntries()):
  cn.GetEntry(i)
  for k in chs:
    if not cutChannel(cn, k):
      continue
    hn[i].Fill(cn.MC_ttbar_beforeFSR_m*1e-6, cn.weight_mc*cn.weight_leptonSF*cn.weight_trackjet_bTagSF_70)

for k in chs:
  hr[k].Divide(hn[k], ht[k], 1, 1, "B")
  hr[k].Scale(100)
  hr[k].GetYaxis().SetRangeUser(0, 10);

def drawIt(hr, channels, label):
  cacc = TCanvas("cacc", "", 800, 600);
  cacc.SetBottomMargin(0.2)
  cacc.SetLeftMargin(0.14)
  l = TLegend(0.7,0.75,0.87,0.89)
  l.SetBorderSize(0)

  first = True
  for i in channels:
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
  stampLumiText(3.2, 0.18, 0.75, "#sqrt{s} = 13 TeV", 0.05)
  stampText(0.18, 0.70, label, 0.05)

  suf = ""
  if not Internal:
    suf = "_ATLASSimul"
  for i in [".eps", ".png", ".pdf"]:
    cacc.SaveAs("accept"+suf+i)

drawIt(hr, {"be": "e+jets", "bmu": "#mu+jets"}, label_signal+", boosted")
drawIt(hr, {"re": "e+jets", "rmu": "#mu+jets"}, label_signal+", resolved")

