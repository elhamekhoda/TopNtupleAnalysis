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

def plot(t, dir1, dir2, mu = False):
  gStyle.SetOptStat(0)
  gStyle.SetPadTickX(1)
  gStyle.SetPadTickY(1)

  clim = TCanvas("clim", "", 800, 600);
  if not 'eft' in t:
    l = TLegend(0.5,0.8,0.87,0.89)
  else:
    l = TLegend(0.5,0.8,0.87,0.89)
  l.SetBorderSize(0)

  maxm = mass[t][-1]
  minm = mass[t][0]
  if minm == maxm:
    maxm += 0.5 
    minm -= 0.5 
  if 'eft' in t:
    maxm = eff[t][-1]
    minm = eff[t][0]
    tmp = maxm
    maxm = minm
    minm = tmp
  h = TH1F("h", "", 50, minm, maxm);
  miny = 0.8
  maxy = 5.0
  h.GetYaxis().SetRangeUser(miny, maxy);
  maxy = 1.0
  if not ('eft' in t and mu):
    h.GetYaxis().SetTitle("Ratio of #sigma #times BR");
  else:
    h.GetYaxis().SetTitle("Ratio of #sigma_{lim} / #sigma_{EFT}");
  if 'zprime' in t:
    h.GetXaxis().SetTitle("m_{Z'} [TeV]");
  elif 'kkG' in t:
    h.GetXaxis().SetTitle("m_{G_{KK}} [TeV]");
  if 'eft' in t:
    h.GetXaxis().SetTitle("c_{Vv} #Lambda^{-2} [TeV^{-2}]");
  h.GetXaxis().SetTitleOffset(0.9);
  h.GetXaxis().SetLabelSize(0.05);
  h.GetXaxis().SetTitleSize(0.05);
  h.Draw("hist");

  length = len(xs[t])
  nom = TGraph(length);
  obs = TGraph(length);
  sigma1 = TGraphAsymmErrors(length);
  sigma2 = TGraphAsymmErrors(length);
  i=0
  for I in range(0,length):
    if path.exists(dir1+"/Ttres_"+signalList[t][I]+"/Limits/Ttres_"+signalList[t][I]+".root")==0:
    	print "missing "+dir1+"/Ttres_"+signalList[t][I]+"/Limits/Ttres_"+signalList[t][I]+".root"
    	continue
    if path.exists(dir2+"/Ttres_"+signalList[t][I]+"/Limits/Ttres_"+signalList[t][I]+".root")==0:
    	print "missing "+dir2+"/Ttres_"+signalList[t][I]+"/Limits/Ttres_"+signalList[t][I]+".root"
    	continue
    muobs = []
    muexp_c = []
    muexp_p2 = []
    muexp_p1 = []
    muexp_m1 = []
    muexp_m2 = []
    for d in [dir1, dir2]:
      f = TFile(d+"/Ttres_"+signalList[t][I]+"/Limits/Ttres_"+signalList[t][I]+".root")
      hi = f.Get("limit")
      obs_v = hi.GetBinContent(1)
      exp_c = hi.GetBinContent(2)
      exp_p2 = abs(-exp_c + hi.GetBinContent(3))
      exp_p1 = abs(-exp_c + hi.GetBinContent(4))
      exp_m1 = abs(-exp_c + hi.GetBinContent(5))
      exp_m2 = abs(-exp_c + hi.GetBinContent(6))
      if ('eft' in t and not mu) or True:
        muexp_c.append(exp_c*xs[t][I])
        muobs.append(obs_v*xs[t][I])
        muexp_m1.append(exp_m1*xs[t][I])
        muexp_p1.append(exp_p1*xs[t][I])
        muexp_m2.append(exp_m2*xs[t][I])
        muexp_p2.append(exp_p2*xs[t][I])
    x = mass[t][I]
    if 'eft' in t:
      x = eff[t][I]
    sigma1.SetPoint(i, x, muexp_c[1]/muexp_c[0])
    sigma1.SetPointError(i, 0, 0, muexp_m1[1]/muexp_m1[0], muexp_p1[1]/muexp_p1[0])
    sigma2.SetPoint(i, x, muexp_c[1]/muexp_c[0])
    sigma2.SetPointError(i, 0, 0, muexp_m2[1]/muexp_m2[0], muexp_p2[1]/muexp_p2[0])
    nom.SetPoint(i, x, muexp_c[1]/muexp_c[0])
    obs.SetPoint(i, x, muobs[1]/muobs[0])
    if muexp_c[1]/muexp_c[0] > maxy:
      maxy = muexp_c[1]/muexp_c[0]
    i+=1
  
  maxy *= 1.2
  h.GetYaxis().SetRangeUser(miny, maxy);
  nom.SetLineWidth(2);
  nom.SetLineStyle(kDashed);
  obs.SetLineWidth(2);
  nom.SetMarkerStyle(20);
  obs.SetMarkerStyle(20);
  nom.SetMarkerSize(1.0);
  obs.SetMarkerSize(1.0);
  obs.SetMarkerColor(kRed);
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
  #l.AddEntry(sigma1, "Expected 95% CLs upper limit #pm 1 #sigma", "F")
  #l.AddEntry(sigma2, "Expected 95% CLs upper limit #pm 2 #sigma", "F")

  #sigma2.Draw("3");
  #sigma1.Draw("3");
  nom.Draw("L")
  #obs.Draw("LP")
  l.Draw()

  gPad.RedrawAxis()

  stampATLAS("Internal", 0.15, 0.83)
  stampLumiText(36.5, 0.15, 0.75, "#sqrt{s} = 13 TeV", 0.04)

  suf = ""
  if mu:
    suf = "_mu"

  clim.SaveAs("ratio_mass_limit_%s%s.eps" % (t, suf))
  clim.SaveAs("ratio_mass_limit_%s%s.png" % (t, suf))
  clim.SaveAs("ratio_mass_limit_%s%s.pdf" % (t, suf))
  clim.SaveAs("ratio_mass_limit_%s%s.C" % (t, suf))

plot('zprime', 'manybins_boosted_cat3', 'manybins_boosted')
plot('kkG', 'manybins_boosted_cat3', 'manybins_boosted')
#plot('eft10', mu=True)
#plot('eft10', mu=False)

