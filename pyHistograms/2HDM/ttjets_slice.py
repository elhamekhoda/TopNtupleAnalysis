#!/usr/bin/env python
import os
import sys
import subprocess
import ROOT
from ROOT import *
import ttjets_style

ROOT.gROOT.SetBatch(1)
ROOT.gErrorIgnoreLevel = ROOT.kWarning

figdir  = "/afs/cern.ch/user/h/hod/data/figs/"

runnums = ["410000", "407200", "407201", "407202", "407203", "407204"]
colors  = {"410000":ROOT.kOrange, "407200":ROOT.kBlack, "407201":ROOT.kBlue, "407202":ROOT.kRed, "407203":ROOT.kGray, "407204":ROOT.kGreen}
channels = ["re","rmu"]
#channels = ["re","rmu","be","bmu"]

for channel in channels:
   histos = []
   cnv = TCanvas("cnv"+channel, "", 1200,600)
   cnv.Divide(2,1)
   cnv.Draw()
   p1 = cnv.cd(1)
   p2 = cnv.cd(2)
   p1.SetLogy()
   #p2.SetLogy()
   for runnum in runnums:
      fname = figdir+channel+"."+runnum+".merged.root"
      tfile = TFile(fname,"READ")
      h  = tfile.Get("trueHT_jets")
      h.SetMarkerStyle(20)
      h.SetMarkerSize(0.8)
      h.SetMarkerColor(colors[runnum])
      h.SetLineColor(colors[runnum])
      h.SetDirectory(0)
      h.Scale(1000)
      histos.append(h)

   p1.cd()
   hSum = histos[1].Clone("x")
   hSum.Reset()
   for i in xrange(len(histos)):
      if(i==0):   continue
      elif(i==1): histos[i].Draw()
      else:       histos[i].Draw("same")
      hSum.Add(histos[i])

   p2.cd()
   histos[0].Draw()
   hSum.Draw("same")

   cnv.cd()
   cnv.SaveAs("figs/HT."+channel+".pdf")
