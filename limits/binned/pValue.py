#!/usr/bin/env python
from os import path
from inputs import *

from ROOT import *

gStyle.SetOptStat(0)
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)

clim = TCanvas("clim", "", 800, 600);
l = TLegend(0.70,0.6,0.85,0.5)
l.SetBorderSize(0)

h = TH1F("h", "", 50, 0, 5.0);
h.GetYaxis().SetRangeUser(1e-5, 1);
h.GetYaxis().SetTitle("p_{0}")
h.GetXaxis().SetTitle("m_{Z'} [TeV]");
h.Draw("hist");

length =len(xs)-3
exp = TGraph(length);
obs = TGraph(length);
i=0
#for I in range(0,length):
# skip 3 first points as they are not there yet
for Is in range(0,length):
  I = Is+3
  if path.exists("JobTtres_"+signalList[I]+"/Significance/JobTtres_"+signalList[I]+".root")==0:
  	print "missing JobTtres_"+signalList[I]+"/Significance/JobTtres_"+signalList[I]+".root"
	continue
  f = TFile("JobTtres_"+signalList[I]+"/Significance/JobTtres_"+signalList[I]+".root")
  hi = f.Get("hypo")
  s_obs = hi.GetBinContent(1)
  s_exp = hi.GetBinContent(2)
  if s_exp < 0:
    s_exp = 0
  if s_obs < 0:
    s_obs = 0
  h_obs = ROOT.Math.normal_cdf_c(s_obs);
  h_exp = ROOT.Math.normal_cdf_c(s_exp);
  ftxt = open('hypo_'+signalList[i]+'.txt', 'w')
  ftxt.write('p_obs     '+str(h_obs)+'\n')
  ftxt.write('p_exp     '+str(h_exp)+'\n')
  ftxt.write('s_obs     '+str(s_obs)+'\n')
  ftxt.write('s_exp     '+str(s_exp)+'\n')
  ftxt.close()
  print mass[I]*1000,"GeV\texp: ", h_exp, "\tobs:",h_obs
  exp.SetPoint(i, mass[I], h_exp)
  obs.SetPoint(i, mass[I], h_obs)
  i+=1
  
exp.SetLineWidth(2);
exp.SetLineStyle(kDashed);
obs.SetLineWidth(2);
exp.SetMarkerStyle(20);
obs.SetMarkerStyle(20);
exp.SetMarkerSize(1.0);
obs.SetMarkerSize(1.0);
obs.SetMarkerColor(kRed);

l.AddEntry(exp, "Expected", "L")
l.AddEntry(obs, "Observed", "LP")


exp.Draw("L")
obs.Draw("LP")
l.Draw()

t = TLatex()
t.SetNDC(0)
t.SetTextFont(42)
t.SetTextColor(1)
t.SetTextSize(0.04)
lsig = {}
for isig in [1, 2, 3, 4]:
    s = ROOT.Math.normal_cdf_c(isig)
    lsig[isig] = TLine(0, s, mass[len(xs)-1], s)
    lsig[isig].SetLineStyle(3)
    lsig[isig].SetLineColor(kBlack)
    lsig[isig].SetLineWidth(2)
    lsig[isig].Draw("L")
    t.DrawLatex(mass[len(xs)-1]*1.03, s, str(isig)+" #sigma")

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

stampATLAS("Internal", 0.5, 0.30)
stampLumiText(3.2, 0.5, 0.24, "#sqrt{s} = 13 TeV", 0.04)

clim.SaveAs("hypo.eps")
clim.SaveAs("hypo.png")

  
