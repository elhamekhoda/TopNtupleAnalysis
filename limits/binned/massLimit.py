#!/usr/bin/env python
from os import path
from inputs import *

from ROOT import *

gStyle.SetOptStat(0)
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)

clim = TCanvas("clim", "", 800, 600);
l = TLegend(0.5,0.5,0.87,0.89)
l.SetBorderSize(0)

h = TH1F("h", "", 50, 0, 5.0);
h.GetYaxis().SetRangeUser(1e-2, 2000);
h.GetYaxis().SetTitle("95% CL upper limit on #sigma #times BR [pb]");
h.GetXaxis().SetTitle("m_{Z'} [TeV]");
h.GetXaxis().SetTitleOffset(0.9);
h.GetXaxis().SetLabelSize(0.05);
h.GetXaxis().SetTitleSize(0.05);
h.Draw("hist");

length =len(xs)
xsec = TGraph(length);
nom = TGraph(length);
obs = TGraph(length);
sigma1 = TGraphAsymmErrors(length);
sigma2 = TGraphAsymmErrors(length);
i=0
for I in range(0,length):
  if path.exists("JobTtres_"+signalList[I]+"/Limits/JobTtres_"+signalList[I]+".root")==0:
  	print "missing JobTtres_"+signalList[I]+"/Limits/JobTtres_"+signalList[I]+".root"
	continue
  f = TFile("JobTtres_"+signalList[I]+"/Limits/JobTtres_"+signalList[I]+".root")
  hi = f.Get("limit")
  muobs = hi.GetBinContent(1)
  muexp = hi.GetBinContent(2)
  muexp_p2 = abs(-muexp + hi.GetBinContent(3))
  muexp_p1 = abs(-muexp + hi.GetBinContent(4))
  muexp_m1 = abs(-muexp + hi.GetBinContent(5))
  muexp_m2 = abs(-muexp + hi.GetBinContent(6))
  ftxt = open('lim_'+signalList[i]+'.txt', 'w')
  ftxt.write('muobs     '+str(muobs)+'\n')
  ftxt.write('muexp     '+str(muexp)+'\n')
  ftxt.write('muexp_p2  '+str(muexp_p2)+'\n')
  ftxt.write('muexp_p1  '+str(muexp_p1)+'\n')
  ftxt.write('muexp_m1  '+str(muexp_m1)+'\n')
  ftxt.write('muexp_m2  '+str(muexp_m2)+'\n')
  ftxt.write('xsec      '+str(xs[i])+'\n')
  ftxt.close()
  print mass[I]*1000,"GeV\texp: ", muexp*xs[I], "\tobs:",muobs*xs[I],"pb"
  sigma1.SetPoint(i, mass[I], muexp*xs[I])
  sigma1.SetPointError(i, 0, 0, muexp_m1*xs[I], muexp_p1*xs[I])
  sigma2.SetPoint(i, mass[I], muexp*xs[I])
  sigma2.SetPointError(i, 0, 0, muexp_m2*xs[I], muexp_p2*xs[I])
  xsec.SetPoint(i, mass[I], xs[I])
  nom.SetPoint(i, mass[I], muexp*xs[I])
  obs.SetPoint(i, mass[I], muobs*xs[I])
  i+=1
  
nom.SetLineWidth(2);
nom.SetLineStyle(kDashed);
obs.SetLineWidth(2);
nom.SetMarkerStyle(20);
obs.SetMarkerStyle(20);
nom.SetMarkerSize(1.0);
obs.SetMarkerSize(1.0);
obs.SetMarkerColor(kRed);
xsec.SetLineWidth(3);
xsec.SetLineColor(kRed);
sigma2.SetFillStyle(1001);
sigma2.SetFillColor(5);
sigma2.SetLineColor(5);
sigma2.SetMarkerColor(5);
sigma1.SetFillStyle(1001);
sigma1.SetFillColor(3);
sigma1.SetMarkerColor(3);

l.AddEntry(nom, "Expected", "L")
l.AddEntry(obs, "Observed", "LP")
l.AddEntry(sigma1, "#pm 1 #sigma", "F")
l.AddEntry(sigma2, "#pm 2 #sigma", "F")
l.AddEntry(xsec, "LO Z'_{#it{TC2}} cross section #times 1.3", "L")

sigma2.Draw("3");
sigma1.Draw("3");
nom.Draw("L")
obs.Draw("LP")
xsec.Draw("L")
l.Draw()
clim.SetLogy(1)

gPad.RedrawAxis()

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

stampATLAS("Internal", 0.15, 0.83)
stampLumiText(3.2, 0.25, 0.75, "#sqrt{s} = 13 TeV", 0.04)

clim.SaveAs("mass_limit.eps")
clim.SaveAs("mass_limit.png")

  
