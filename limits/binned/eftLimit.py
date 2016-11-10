#!/usr/bin/env python
from os import path
from inputs import *

from ROOT import *

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
  t.DrawLatex(x,y, text+", "+str(lumi)+" fb^{-1}")

def plotSigma(t, useLambda = True):
  gStyle.SetOptStat(0)
  gStyle.SetPadTickX(1)
  gStyle.SetPadTickY(1)

  clim = TCanvas("clim", "", 800, 600);
  l = TLegend(0.5,0.6,0.87,0.89)

  if useLambda:
    maxm = mass[t][-1]
    minm = mass[t][0]
  else:
    maxm = eff[t][0]
    minm = eff[t][-1]
  h = TH1F("h", "", 50, minm, maxm);
  miny = 1e-2
  maxy = 2000
  h.GetYaxis().SetRangeUser(miny, maxy);
  h.GetYaxis().SetTitle("#sigma [pb]");
  if useLambda:
    h.GetXaxis().SetTitle("#Lambda [TeV]");
  else:
    h.GetXaxis().SetTitle("c_{Vv} #Lambda^{-2} [TeV^{-2}]");
  h.GetXaxis().SetTitleOffset(0.9);
  h.GetXaxis().SetLabelSize(0.05);
  h.GetXaxis().SetTitleSize(0.05);
  h.Draw("hist");

  length = len(xs[t])
  xsec = TGraph(length);
  i=0
  for I in range(0,length):
    print t,'\t',mass[t][I],"TeV\tcL^-2\t",eff[t][I],"\txs\t",xs[t][I],"pb"
    if useLambda:
      x = mass[t][I]
    else:
      x = eff[t][I]
    xsec.SetPoint(i, x, xs[t][I])
    i+=1
  
  xsec.SetLineWidth(3);
  xsec.SetLineColor(kRed);

  l.AddEntry(xsec, "EFT cross section", "L")
  xsec.Draw("L")
  l.Draw()

  gPad.RedrawAxis()

  stampATLAS("Internal", 0.15, 0.83)
  stampLumiText(15.8, 0.15, 0.75, "#sqrt{s} = 13 TeV", 0.04)

  stype = "lambda"
  if not useLambda:
    stype = "eff"
  clim.SaveAs("sigma_%s_%s.eps" % (stype, t))
  clim.SaveAs("sigma_%s_%s.png" % (stype, t))
  clim.SaveAs("sigma_%s_%s.pdf" % (stype, t))
  clim.SaveAs("sigma_%s_%s.C" % (stype, t))

plotSigma('eft10', True)
plotSigma('eft10', False)

