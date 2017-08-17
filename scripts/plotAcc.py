#!/usr/bin/env python
from os import path

from ROOT import *
import math

Internal = True
#Internal = False

files = "/nfs/dust/atlas/user/danilo/ntuple_2429/"


chs  = []

chs += ["be"]
chs += ["be%d" % i for i in [1,2,3]]

chs += ["bmu"]
chs += ["bmu%d" % i for i in [1,2,3]]

chs += ["re"]
chs += ["re%d" % i for i in [1,2,3]]

chs += ["rmu"]
chs += ["rmu%d" % i for i in [1,2,3]]

chs += ["b"]
chs += ["r"]
chs += ["all"]

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
  elif "b" in i:
    if ct.bejets_2015 or ct.bejets_2016 or ct.bmujets_2015 or ct.bmujets_2016:
      p = True
  elif "r" in i:
    if ct.rejets_2015 or ct.rejets_2016 or ct.rmujets_2015 or ct.rmujets_2016:
      p = True
  elif "all" in i:
    if ct.bejets_2015 or ct.bejets_2016 or ct.bmujets_2015 or ct.bmujets_2016 or ct.rejets_2015 or ct.rejets_2016 or ct.rmujets_2015 or ct.rmujets_2016:
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

def drawIt(hr, channels, label, suf = ""):
  cacc = TCanvas("cacc", "", 800, 600);
  cacc.SetBottomMargin(0.2)
  cacc.SetLeftMargin(0.14)
  l = TLegend(0.7,0.75,0.87,0.89)
  l.SetBorderSize(0)

  bestYmax = 2.0
  for i in channels:
    ymaxHist = hr[i].GetBinContent(hr[i].GetMaximumBin())
    if ymaxHist > bestYmax:
      bestYmax = ymaxHist
  bestYmax = math.ceil(bestYmax*1.3)*1.0
  for i in channels:
    #hr[i].GetYaxis().SetRangeUser(0, bestYmax);
    hr[i].SetMaximum(bestYmax);

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
  stampLumiText(-1, 0.18, 0.75, "#sqrt{s} = 13 TeV", 0.05)
  stampText(0.18, 0.70, label, 0.05)

  suf += ""
  if not Internal:
    suf += "_ATLASSimul"
  for i in [".eps", ".png", ".pdf"]:
    cacc.SaveAs("accept"+suf+i)

def doIt(signal):
  ct = TChain("truth")
  cn = TChain("nominal")
  import array
  binning = array.array('d', [x*0.25 for x in range(0, int(1.0/0.25))]+[1.0+x*0.5 for x in range(0, int(3.0/0.5))]+[5.0])

  ht = {}
  hn = {}
  hr = {}
  for i in chs:
    ht[i] = TH1F("ht_%s"%i, "", len(binning)-1, binning)
    hn[i] = TH1F("hn_%s"%i, "", len(binning)-1, binning)
    hr[i] = TH1F("hr_%s"%i, "", len(binning)-1, binning)

  did_list = []
  if signal == "Zp":
    # zprime
    did_list = range(301322, 301335+1)
    suf_signal = "Zp"
    label_signal = "Z'"
  elif signal == "KKgrav":
    # KK grav
    did_list = range(305012, 305017+1)
    suf_signal = "KKgrav"
    label_signal = "Kaluza-Klein graviton"
  elif signal == "KKgluon":
    # KK gluon 30%
    did_list = range(307522, 307533+1)
    suf_signal = "KKgluon"
    label_signal = "Kaluza-Klein gluon #Gamma=30%"

  import glob
  for did in did_list:
    for d in glob.glob(files+"/user.dferreir.%d.*"%did):
      for f in glob.glob(d+"/*"):
        ct.Add(f)
        cn.Add(f)

  for i in xrange(ct.GetEntries()):
    ct.GetEntry(i)
    for k in chs:
      ht[k].Fill(ct.MC_ttbar_beforeFSR_m*1e-6, ct.weight_mc)

  for i in xrange(cn.GetEntries()):
    cn.GetEntry(i)
    for k in chs:
      if not cutChannel(cn, k):
        continue
      hn[k].Fill(cn.MC_ttbar_beforeFSR_m*1e-6, cn.weight_mc*cn.weight_leptonSF*cn.weight_trackjet_bTagSF_70)

  for k in chs:
    hr[k].Divide(hn[k], ht[k], 1, 1, "B")
    hr[k].Scale(100)

  for i in chs:
    st_color = kRed
    st_line = 1
    cat = 0
    if "3" in i: cat = 3
    if "2" in i: cat = 2
    if "1" in i: cat = 1
    if "be" in i:
      st_color = kRed+cat
      st_line = 1
    elif "bmu" in i:
      st_color = kRed+cat
      st_line = 2
    elif "re" in i:
      st_color = kBlue+cat
      st_line = 1
    elif "rmu" in i:
      st_color = kBlue+cat
      st_line = 2
    elif "b" in i:
      st_color = kGreen+2
      st_line = 1
    elif "r" in i:
      st_color = kMagenta
      st_line = 1
    setStyle(ht[i], st_color,  st_line)
    setStyle(hn[i], st_color,  st_line)
    setStyle(hr[i], st_color,  st_line)


  drawIt(hr, {"be": "e+jets", "bmu": "#mu+jets"}, label_signal+", boosted", suf = "boosted%s"%suf_signal)
  drawIt(hr, {"re": "e+jets", "rmu": "#mu+jets"}, label_signal+", resolved", suf = "resolved%s"%suf_signal)

  drawIt(hr, {"be3": "e+jets (cat. 3)", "be2": "e+jets (cat. 2)", "be1": "e+jets (cat. 1)"}, label_signal+", boosted", suf = "becat%s"%suf_signal)
  drawIt(hr, {"bmu3": "#mu+jets (cat. 3)", "bmu2": "#mu+jets (cat. 2)", "bmu1": "#mu+jets (cat. 1)"}, label_signal+", boosted", suf = "bmucat%s"%suf_signal)
  drawIt(hr, {"re3": "e+jets (cat. 3)", "re2": "e+jets (cat. 2)", "re1": "e+jets (cat. 1)"}, label_signal+", resolved", suf = "recat%s"%suf_signal)
  drawIt(hr, {"rmu3": "#mu+jets (cat. 3)", "rmu2": "#mu+jets (cat. 2)", "rmu1": "#mu+jets (cat. 1)"}, label_signal+", resolved", suf = "rmucat%s"%suf_signal)

  drawIt(hr, {"b": "boosted", "r": "resolved", "all": "combination"}, label_signal, suf = "summary%s"%suf_signal)

# call it
for i in ["Zp", "KKgluon", "KKgrav"]:
  doIt(i)

