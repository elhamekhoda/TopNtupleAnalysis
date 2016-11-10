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

def plot(t, mu = False):
  gStyle.SetOptStat(0)
  gStyle.SetPadTickX(1)
  gStyle.SetPadTickY(1)

  clim = TCanvas("clim", "", 800, 600);
  if not 'eft' in t:
    l = TLegend(0.5,0.45,0.87,0.89)
  else:
    l = TLegend(0.5,0.6,0.87,0.89)
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
  miny = 1e-2
  maxy = 2000
  if 'eft' in t:
    miny = 10
    maxy = 400
  h.GetYaxis().SetRangeUser(miny, maxy);
  if not ('eft' in t and mu):
    h.GetYaxis().SetTitle("#sigma #times BR [pb]");
  else:
    h.GetYaxis().SetTitle("#sigma_{lim} / #sigma_{EFT}");
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
    if 'eft' in t and not mu:
      muexp = muexp*xs[t][I]
      muobs = muobs*xs[t][I]
      muexp_m1 = muexp_m1*xs[t][I]
      muexp_p1 = muexp_p1*xs[t][I]
      muexp_m2 = muexp_m2*xs[t][I]
      muexp_p2 = muexp_p2*xs[t][I]
    ftxt = open('lim_'+signalList[t][i]+'.txt', 'w')
    ftxt.write('muobs     '+str(muobs)+'\n')
    ftxt.write('muexp     '+str(muexp)+'\n')
    ftxt.write('muexp_p2  '+str(muexp_p2)+'\n')
    ftxt.write('muexp_p1  '+str(muexp_p1)+'\n')
    ftxt.write('muexp_m1  '+str(muexp_m1)+'\n')
    ftxt.write('muexp_m2  '+str(muexp_m2)+'\n')
    ftxt.write('xsec      '+str(xs[t][i])+'\n')
    ftxt.close()
    print t,'\t',mass[t][I],"TeV\texp: ", muexp, "\tobs:",muobs,"pb"
    x = mass[t][I]
    if 'eft' in t:
      x = eff[t][I]
    sigma1.SetPoint(i, x, muexp)
    sigma1.SetPointError(i, 0, 0, muexp_m1, muexp_p1)
    sigma2.SetPoint(i, x, muexp)
    sigma2.SetPointError(i, 0, 0, muexp_m2, muexp_p2)
    xsec12.SetPoint(i, x, xs[t][I])
    if 'zprime' in t:
      xsec3.SetPoint(i, x, xs3[t][I])
    nom.SetPoint(i, x, muexp)
    obs.SetPoint(i, x, muobs)
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
  l.AddEntry(sigma1, "Expected 95% CLs upper limit #pm 1 #sigma", "F")
  l.AddEntry(sigma2, "Expected 95% CLs upper limit #pm 2 #sigma", "F")
  if 'zprime' in t:
    l.AddEntry(xsec12, "LO Z'_{#it{TC2}} #Gamma=1.2% cross section #times 1.3", "L")
  elif 'kkG' in t:
    l.AddEntry(xsec12, "LO KK graviton cross section", "L")
  if 'zprime' in t:
    l.AddEntry(xsec3, "LO Z'_{#it{TC2}} #Gamma=3% cross section #times 1.3", "L")

  sigma2.Draw("3");
  sigma1.Draw("3");
  nom.Draw("L")
  #obs.Draw("LP")
  if not 'eft' in t:
    xsec12.Draw("L")
  if 'zprime' in t:
    xsec3.Draw("L")
  l.Draw()
  if not 'eft' in t:
    clim.SetLogy(1)

  gPad.RedrawAxis()

  stampATLAS("Internal", 0.15, 0.83)
  stampLumiText(15.8, 0.15, 0.75, "#sqrt{s} = 13 TeV", 0.04)

  suf = ""
  if mu:
    suf = "_mu"

  clim.SaveAs("mass_limit_%s%s.eps" % (t, suf))
  clim.SaveAs("mass_limit_%s%s.png" % (t, suf))
  clim.SaveAs("mass_limit_%s%s.pdf" % (t, suf))
  clim.SaveAs("mass_limit_%s%s.C" % (t, suf))

#plot('zprime')
#plot('kkG')
plot('eft10', mu=True)
plot('eft10', mu=False)

