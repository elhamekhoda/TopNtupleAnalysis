#!/usr/bin/env python
from os import path
from inputs import *

from ROOT import *

gStyle.SetOptStat(0)
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)

cacc = TCanvas("cacc", "", 800, 600);
l = TLegend(0.5,0.65,0.87,0.89)
l.SetBorderSize(0)

ct = TChain("truth")
cn = TChain("nominal")

ht_e = TH1F("ht_e", "", 20, 0.0, 5.0)
hn_e = TH1F("hn_e", "", 20, 0.0, 5.0)
hr_e = TH1F("hr_e", "", 20, 0.0, 5.0)

ht_mu = TH1F("ht_mu", "", 20, 0.0, 5.0)
hn_mu = TH1F("hn_mu", "", 20, 0.0, 5.0)
hr_mu = TH1F("hn_mu", "", 20, 0.0, 5.0)

def setStyle(h, col, sty):
    h.GetYaxis().SetRangeUser(0, 1.0);
    h.GetYaxis().SetTitle("Acceptance #times Efficiency");
    h.GetXaxis().SetTitle("m_{t#bar{t}} [TeV]");
    h.GetXaxis().SetTitleOffset(0.9);
    h.GetXaxis().SetLabelSize(0.05);
    h.GetXaxis().SetTitleSize(0.05);
    h.SetLineWidth(2);
    h.SetLineStyle(sty);
    h.SetLineColor(col);

setStyle(ht_e, kRed,  1)
setStyle(hn_e, kRed,  1)
setStyle(hr_e, kRed,  1)

setStyle(ht_mu, kBlue, 2)
setStyle(hn_mu, kBlue, 2)
setStyle(hr_mu, kBlue, 2)

files = "/afs/cern.ch/user/d/dferreir/work/eos/atlas/user/d/dferreir/topana/12032016Accv1/"
import glob
for d in glob.glob(files+"/*"):
    for f in glob.glob(d+"/*"):
        ct.Add(f)
        cn.Add(f)

for i in xrange(ct.GetEntries):
    ct.GetEntry(i)
    ht_e.Fill(ct.MC_ttbar_afterFSR_m, ct.weight_mc*ct.weight_pileup)
    ht_mu.Fill(ct.MC_ttbar_afterFSR_m, ct.weight_mc*ct.weight_pileup)

for i in xrange(cn.GetEntries):
    cn.GetEntry(i)
    if len(cn.el_pt) == 1 and len(cn.mu_pt) == 0:
        hn_e.Fill(cn.MC_ttbar_afterFSR_m, cn.weight_mc*cn.weight_pileup*cn.weight_leptonSF*cn.weight_trackjet_bTagSF_70)
    elif len(cn.el_pt) == 0 and len(cn.mu_pt) == 1:
        hn_mu.Fill(cn.MC_ttbar_afterFSR_m, cn.weight_mc*cn.weight_pileup*cn.weight_leptonSF*cn.weight_trackjet_bTagSF_70)
    else
        print "Neither electron nor muon! Panic!"

hr_e.Divide(hn_e, ht_e, 1, 1, "B")
hr_mu.Divide(hn_mu, ht_mu, 1, 1, "B")

hr_e.Draw("hist");
hr_mu.Draw("hist same");
  
l.AddEntry(hr_e, "e+jets", "L")
l.AddEntry(hr_mu, "#mu+jets", "L")

l.Draw()

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

for i in [".eps", ".png", ".pdf"]:
    cacc.SaveAs("accept"+i)

  
