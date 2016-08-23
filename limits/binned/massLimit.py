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

def plot(t):
  gStyle.SetOptStat(0)
  gStyle.SetPadTickX(1)
  gStyle.SetPadTickY(1)

  clim = TCanvas("clim", "", 800, 600);
  l = TLegend(0.5,0.45,0.87,0.89)
  l.SetBorderSize(0)

  maxm = mass[t][-1]
  minm = mass[t][0]
  h = TH1F("h", "", 50, minm, maxm);
  h.GetYaxis().SetRangeUser(1e-2, 2000);
  h.GetYaxis().SetTitle("#sigma #times BR [pb]");
  if 'zprime' in t:
    h.GetXaxis().SetTitle("m_{Z'} [TeV]");
  elif 'kkG' in t:
    h.GetXaxis().SetTitle("m_{G_{KK}} [TeV]");
  h.GetXaxis().SetTitleOffset(0.9);
  h.GetXaxis().SetLabelSize(0.05);
  h.GetXaxis().SetTitleSize(0.05);
  h.Draw("hist");

  length = len(xs[t])
  xsec12 = TGraph(length);
  xsec3 = TGraph(length);
  nom = TGraph(length);
  obs = TGraph(length);
  sigma1 = TGraphAsymmErrors(length);
  sigma2 = TGraphAsymmErrors(length);
  i=0
  for I in range(0,length):
    if path.exists("JobTtres_"+signalList[t][I]+"/Limits/JobTtres_"+signalList[t][I]+".root")==0:
    	print "missing JobTtres_"+signalList[t][I]+"/Limits/JobTtres_"+signalList[t][I]+".root"
    	continue
    f = TFile("JobTtres_"+signalList[t][I]+"/Limits/JobTtres_"+signalList[t][I]+".root")
    hi = f.Get("limit")
    muobs = hi.GetBinContent(1)
    muexp = hi.GetBinContent(2)
    muexp_p2 = abs(-muexp + hi.GetBinContent(3))
    muexp_p1 = abs(-muexp + hi.GetBinContent(4))
    muexp_m1 = abs(-muexp + hi.GetBinContent(5))
    muexp_m2 = abs(-muexp + hi.GetBinContent(6))
    ftxt = open('lim_'+signalList[t][i]+'.txt', 'w')
    ftxt.write('muobs     '+str(muobs)+'\n')
    ftxt.write('muexp     '+str(muexp)+'\n')
    ftxt.write('muexp_p2  '+str(muexp_p2)+'\n')
    ftxt.write('muexp_p1  '+str(muexp_p1)+'\n')
    ftxt.write('muexp_m1  '+str(muexp_m1)+'\n')
    ftxt.write('muexp_m2  '+str(muexp_m2)+'\n')
    ftxt.write('xsec      '+str(xs[t][i])+'\n')
    ftxt.close()
    print t,'\t',mass[t][I]*1000,"GeV\texp: ", muexp, "\tobs:",muobs,"pb"
    sigma1.SetPoint(i, mass[t][I], muexp)
    sigma1.SetPointError(i, 0, 0, muexp_m1, muexp_p1)
    sigma2.SetPoint(i, mass[t][I], muexp)
    sigma2.SetPointError(i, 0, 0, muexp_m2, muexp_p2)
    xsec12.SetPoint(i, mass[t][I], xs[t][I])
    if 'zprime' in t:
      xsec3.SetPoint(i, mass[t][I], xs3[t][I])
    nom.SetPoint(i, mass[t][I], muexp)
    obs.SetPoint(i, mass[t][I], muobs)
    i+=1
  
  nom.SetLineWidth(2);
  nom.SetLineStyle(kDashed);
  obs.SetLineWidth(2);
  nom.SetMarkerStyle(20);
  obs.SetMarkerStyle(20);
  nom.SetMarkerSize(1.0);
  obs.SetMarkerSize(1.0);
  obs.SetMarkerColor(kRed);
  xsec12.SetLineWidth(3);
  xsec12.SetLineColor(kRed);
  xsec3.SetLineWidth(3);
  xsec3.SetLineColor(kRed);
  xsec3.SetLineStyle(2);
  sigma2.SetFillStyle(1001);
  sigma2.SetFillColor(5);
  sigma2.SetLineColor(5);
  sigma2.SetMarkerColor(5);
  sigma1.SetFillStyle(1001);
  sigma1.SetFillColor(3);
  sigma1.SetMarkerColor(3);
  sigma1.SetLineColor(3);

  l.AddEntry(nom, "Expected 95% CLs upper limit", "L")
  #l.AddEntry(obs, "Observed 95% CLs upper limit", "LP")
  l.AddEntry(sigma1, "#pm 1 #sigma", "F")
  l.AddEntry(sigma2, "#pm 2 #sigma", "F")
  if 'zprime' in t:
    l.AddEntry(xsec12, "LO Z'_{#it{TC2}} #Gamma=1.2% cross section #times 1.3", "L")
  elif 'kkG' in t:
    l.AddEntry(xsec12, "LO KK graviton cross section", "L")
  if 'zprime' in t:
    l.AddEntry(xsec3, "LO Z'_{#it{TC2}} #Gamma=3% cross section #times 1.3", "L")

  sigma2.Draw("3");
  sigma1.Draw("3");
  nom.Draw("L")
  obs.Draw("LP")
  xsec12.Draw("L")
  if 'zprime' in t:
    xsec3.Draw("L")
  l.Draw()
  clim.SetLogy(1)

  gPad.RedrawAxis()

  stampATLAS("Internal", 0.15, 0.83)
  stampLumiText(15.8, 0.25, 0.75, "#sqrt{s} = 13 TeV", 0.04)

  clim.SaveAs("mass_limit_%s.eps" % t)
  clim.SaveAs("mass_limit_%s.png" % t)
  clim.SaveAs("mass_limit_%s.pdf" % t)
  clim.SaveAs("mass_limit_%s.C" % t)

plot('zprime')
plot('kkG')

