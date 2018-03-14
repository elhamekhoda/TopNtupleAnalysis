#!/usr/bin/env python
import os
import math
from array import array
import ROOT
from ROOT import *
import subprocess
import ttjets_style
import argparse
## usage:
## python ttjets_plots.py -S A -M 500 -SBA 1 -TANB 0.4 -TYPE 2
parser = argparse.ArgumentParser(description='ttjets plot')
parser.add_argument('-S', metavar='<resonance name>', required=True, help='The resonance name [A/H]')
parser.add_argument('-M', metavar='<resonance mass>', required=True, help='The resonance mass [500,...]')
parser.add_argument('-SBA', metavar='<sin(beta-alpha)>', required=True, help='Sin(beta-alpha) [1,...]')
parser.add_argument('-TANB', metavar='<tan(beta)>', required=True, help='Tan(beta) [0.3,...]')
parser.add_argument('-TYPE', metavar='<type>', required=True, help='Type [1/2]')
args = parser.parse_args()
S=str(args.S)
M=int(args.M)
SBA=float(args.SBA)
TANB=float(args.TANB)
TYPE=int(args.TYPE)
print "S=%s, M=%s, SBA=%s, TANB=%s, TYPE=%s" % (S,M,SBA,TANB,TYPE)

ROOT.gROOT.SetBatch(1)
ROOT.gErrorIgnoreLevel = ROOT.kWarning

'''
ntupdir = "/afs/cern.ch/user/h/hod/data/mc15_13TeV/MGPy8EG_A14N30NLO_ttbarNp012p/"
tree = TChain("truth")
tree.Add(ntupdir+"/user.hod.407204.MGPy8EG.DAOD_EXOT4.e5146_s2726_r7772_r7676_p2711.03-08-15_output.root/*.root")
W = 0
for event in tree: W += event.weight_mc
print "407204: Nevents=%i, SumOfWeights=%g" % (tree.GetEntries(),W)
# 407200: Nevents=15565000, SumOfWeights=599144   GenFiltEff=4.9442E-01
# 407201: Nevents=2448000,  SumOfWeights=6665.36  GenFiltEff=3.4418E-02
# 407202: Nevents=4908000,  SumOfWeights=19494.6  GenFiltEff=1.1386E-02
# 407203: Nevents=3904000,  SumOfWeights=14708    GenFiltEff=9.3391E-03
# 407204: Nevents=489500,   SumOfWeights=1362.09  GenFiltEff=3.6975E-03
samples = {
   407200:{"Slice":"MET0to200_HT0to500",    "N":15725000, "Sigma":435.44, "GenEff":4.9442E-01, "SumW":599144,  "Col":ROOT.kBlack},
   407201:{"Slice":"MET0to200_HT500to700",  "N":2500000,  "Sigma":436.63, "GenEff":3.4418E-02, "SumW":6665.36, "Col":ROOT.kBlue},
   407202:{"Slice":"MET0to200_HT700to1000", "N":5000000,  "Sigma":436.48, "GenEff":1.1386E-02, "SumW":19494.6, "Col":ROOT.kRed},
   407203:{"Slice":"MET200p_HT0to1000",     "N":3968000,  "Sigma":436.48, "GenEff":9.3391E-03, "SumW":14708,   "Col":ROOT.kGreen},
   407204:{"Slice":"HT1000p",               "N":499500,   "Sigma":436.58, "GenEff":3.6975E-03, "SumW":1362.09, "Col":ROOT.kGray+1},
}
'''


pb2fb = 1.e3
lumi  = 20.3 # fb-1

################################ model+channel setup ############################
MH=-1
MA=-1
if(S=="H"):
   MH=M
   MA=-1
else:
   MH=-1
   MA=M
sSBA  = str(SBA).replace(".","")
sTANB = str(TANB).replace(".","")
##################################################################################

prefix  = "/afs/cern.ch/user/h/hod/data/figs/"
hnames  = ["trueMtt8TeV", "mtt8TeV", "trueMtt", "mtt", ]
hnamesr = ["trueMtt8TeV", "mtt8TeV", "trueMtt", "mtt", ]
htitles = { "trueMtt8TeV":";True #it{m}_{tt} [GeV];Events / 40 GeV",
            "trueMtt":";True #it{m}_{tt} [GeV];Events / 10 GeV",
            "mtt8TeV":";#it{m}_{tt} [GeV];Events / 40 GeV",
            "mtt":";#it{m}_{tt} [GeV];Events / 10 GeV",}
#channels = ["re", "rmu", "be", "bmu"]
channels = ["re", "rmu"]
schannels = {"re":"Resolved electron", "rmu":"Resolved muon", "be":"Boosted electron", "bmu":"Boosted muon"}
dsids = ["410000","40720X"]
powheg = "_SM_410000"
madgsm = "_SM_40720X"
madgxx = "_XX_40720X"

def getminmax(h):
   Min = +1.e10
   Max = -1.e10
   for b in xrange(1,h.GetNbinsX()+1):
      y = h.GetBinContent(b)
      if(y==0): continue
      Min = y if(y<Min) else Min
      Max = y if(y>Max) else Max
   return (Min,Max)

def normalizeToBinWidth(h, unit=40.): ## normalize to nEvts/40 GeV
   for b in xrange(h.GetNbinsX()+1):
      sf = unit/h.GetBinWidth(b)
      h.SetBinContent(b, h.GetBinContent(b)*sf)
      h.SetBinError(b,   h.GetBinError(b)*sf)
   return h


def geth(dsid,channel,hname,model):
  jobconf = channel+"."+dsid
  if(model!="SM"): jobconf = jobconf+".s"+str(S)+"_m"+str(M)+"_sba"+sSBA+"_tanb"+sTANB+"_t"+str(TYPE)
  fname = jobconf+".merged.root"
  tfile = TFile(prefix+fname,"READ")
  htmp = tfile.Get(hname)
  htitle = htitles[hname]
  htmp.SetTitle(htitle)
  htmp.Scale(lumi*pb2fb)
  if("Events / " in htitle):
     unit = float(htitle.split(";")[2].split(" ")[2])
     htmp = normalizeToBinWidth(htmp,unit)
  htmp.SetDirectory(0)
  return htmp

def gethr(dsid,channel,hname,xtitle,ytitle=""):
  jobconf = channel+"."+dsid+".s"+str(S)+"_m"+str(M)+"_sba"+sSBA+"_tanb"+sTANB+"_t"+str(TYPE)
  fname = jobconf+".merged.root"
  tfile = TFile(prefix+fname,"READ")
  htmpr = tfile.Get(hname)
  htmpr.Scale(lumi*pb2fb)
  if(ytitle!=""):
     htmpr.GetYaxis().SetTitle(ytitle)
     htmpr.GetXaxis().SetTitle(xtitle)
  if("Events / " in htitles[hname[:-1]]):
     unit = float(htitles[hname[:-1]].split(";")[2].split(" ")[2])
     htmpr = normalizeToBinWidth(htmpr,unit)
  htmpr.SetDirectory(0)
  return htmpr


## get all histos
histos = {}
for channel in channels:
   for hname in hnames:
      chname = channel+"_"+hname
      for dsid in dsids:
         if(dsid=="40720X"):
            hSM = geth(dsid,channel,hname,"SM")
            hXX = geth(dsid,channel,hname,"XX")
            histos.update({chname+"_SM_"+dsid:hSM})
            histos.update({chname+"_XX_"+dsid:hXX})
            if(hname in hnamesr):
               xtitle = histos[chname+"_SM_"+dsid].GetXaxis().GetTitle()
               ytitle = "("+S+"^{2}+Interf[SM,"+S+"])/SM [%]"
               hrXX = gethr(dsid,channel,hname+"r",xtitle,ytitle)
               histos.update({chname+"r_XX_"+dsid:hrXX})
         else:
            hSM = geth(dsid,channel,hname,"SM")
            histos.update({chname+"_SM_"+dsid:hSM})

outhistos = {}
## draw
for channel in channels:
   outname = channel+".s"+str(S)+"_m"+str(M)+"_sba"+sSBA+"_tanb"+sTANB+"_t"+str(TYPE)
   schannel = schannels[channel]
   r = 0
   n  = len(hnames)
   nr = len(hnamesr)
   for j in xrange(n):
      hname = hnames[j]
      chname = channel+"_"+hname

      if(hname in hnamesr):
         histos[chname+"r"+madgxx].SetLineColor(ROOT.kBlack)
         histos[chname+"r"+madgxx].SetMarkerColor(ROOT.kBlack)
         histos[chname+"r"+madgxx].SetMarkerStyle(20)
         histos[chname+"r"+madgxx].SetMarkerSize(0.8)

      histos[chname+madgsm].SetLineColor(ROOT.kBlack)
      histos[chname+madgsm].SetMarkerColor(ROOT.kBlack)
      histos[chname+madgsm].SetMarkerStyle(20)
      histos[chname+madgsm].SetMarkerSize(0.8)
 
      histos[chname+madgxx].SetLineColor(ROOT.kOrange+10)
      histos[chname+madgxx].SetMarkerColor(ROOT.kOrange+10)
      histos[chname+madgxx].SetMarkerStyle(24)
      histos[chname+madgxx].SetMarkerSize(0.8)

      histos[chname+powheg].SetLineColor(ROOT.kBlue)
      histos[chname+powheg].SetMarkerColor(ROOT.kBlue)
      histos[chname+powheg].SetMarkerStyle(24)
      histos[chname+powheg].SetMarkerSize(0.8)
      hmin = histos[chname+madgsm].GetMinimum() if (histos[chname+powheg].GetMinimum()>histos[chname+madgsm].GetMinimum()) else histos[chname+powheg].GetMinimum()
      hmax = histos[chname+madgsm].GetMaximum() if (histos[chname+powheg].GetMaximum()<histos[chname+madgsm].GetMaximum()) else histos[chname+powheg].GetMaximum()
      hmin = histos[chname+madgsm].GetMinimum() if (histos[chname+madgsm].GetMinimum()>0) else 0.2
      
      histos[chname+madgsm].SetMinimum(hmin)
      histos[chname+madgsm].SetMaximum(hmax*2)
      histos[chname+madgxx].SetMinimum(hmin)
      histos[chname+madgxx].SetMaximum(hmax*2)

      histos[chname+madgsm].GetXaxis().SetLabelSize(histos[chname+madgsm].GetXaxis().GetLabelSize()*1.5)
      histos[chname+madgsm].GetYaxis().SetLabelSize(histos[chname+madgsm].GetYaxis().GetLabelSize()*1.5)
      histos[chname+madgsm].GetXaxis().SetTitleSize(histos[chname+madgsm].GetXaxis().GetTitleSize()*1.5)
      histos[chname+madgsm].GetYaxis().SetTitleSize(histos[chname+madgsm].GetYaxis().GetTitleSize()*1.5)
      histos[chname+madgsm].GetYaxis().SetTitleOffset(0.8)
      histos[chname+madgsm].GetXaxis().SetTitleOffset(0.93)

      histos[chname+madgxx].GetXaxis().SetLabelSize(histos[chname+madgxx].GetXaxis().GetLabelSize()*1.5)
      histos[chname+madgxx].GetYaxis().SetLabelSize(histos[chname+madgxx].GetYaxis().GetLabelSize()*1.5)
      histos[chname+madgxx].GetXaxis().SetTitleSize(histos[chname+madgxx].GetXaxis().GetTitleSize()*1.5)
      histos[chname+madgxx].GetYaxis().SetTitleSize(histos[chname+madgxx].GetYaxis().GetTitleSize()*1.5)
      histos[chname+madgxx].GetYaxis().SetTitleOffset(0.8)
      histos[chname+madgxx].GetXaxis().SetTitleOffset(0.93)

      histos[chname+powheg].GetXaxis().SetLabelSize(histos[chname+powheg].GetXaxis().GetLabelSize()*1.5)
      histos[chname+powheg].GetYaxis().SetLabelSize(histos[chname+powheg].GetYaxis().GetLabelSize()*1.5)
      histos[chname+powheg].GetXaxis().SetTitleSize(histos[chname+powheg].GetXaxis().GetTitleSize()*1.5)
      histos[chname+powheg].GetYaxis().SetTitleSize(histos[chname+powheg].GetYaxis().GetTitleSize()*1.5)
      histos[chname+powheg].GetYaxis().SetTitleOffset(0.8)
      histos[chname+powheg].GetXaxis().SetTitleOffset(0.93)

      ### Residuals
      if(hname in hnamesr):
         histos[chname+madgsm].GetXaxis().SetLabelSize(histos[chname+madgsm].GetXaxis().GetLabelSize()/1.5)
         histos[chname+madgsm].GetYaxis().SetLabelSize(histos[chname+madgsm].GetYaxis().GetLabelSize()/1.5)
         histos[chname+madgsm].GetXaxis().SetTitleSize(histos[chname+madgsm].GetXaxis().GetTitleSize()/1.5)
         histos[chname+madgsm].GetYaxis().SetTitleSize(histos[chname+madgsm].GetYaxis().GetTitleSize()/1.5)
         #histos[chname+madgsm].GetYaxis().SetTitleOffset(0.8)
         #histos[chname+madgsm].GetXaxis().SetTitleOffset(0.93)
         histos[chname+madgxx].GetXaxis().SetLabelSize(histos[chname+madgxx].GetXaxis().GetLabelSize()/1.5)
         histos[chname+madgxx].GetYaxis().SetLabelSize(histos[chname+madgxx].GetYaxis().GetLabelSize()/1.5)
         histos[chname+madgxx].GetXaxis().SetTitleSize(histos[chname+madgxx].GetXaxis().GetTitleSize()/1.5)
         histos[chname+madgxx].GetYaxis().SetTitleSize(histos[chname+madgxx].GetYaxis().GetTitleSize()/1.5)
         #histos[chname+madgxx].GetYaxis().SetTitleOffset(0.8)
         #histos[chname+madgxx].GetXaxis().SetTitleOffset(0.93)
         MinSM,MaxSM = getminmax(histos[chname+madgsm])
         MinXX,MaxXX = getminmax(histos[chname+madgxx])
         Min = MinSM if(MinSM<MinXX) else MinXX 
         Max = MaxSM if(MaxSM>MaxXX) else MaxXX

         lzero = TLine(histos[chname+madgsm].GetXaxis().GetXmin(), 0, histos[chname+madgsm].GetXaxis().GetXmax(), 0)
         lzero.SetLineColor(kRed)

         leg = TLegend(0.5,0.55,0.87,0.95,"","brNDC")
         leg.SetFillStyle(4000) # will be transparent
         leg.SetFillColor(0)
         leg.SetTextFont(42)
         leg.SetBorderSize(0)
         leg.AddEntry(0,                     schannel,  "")
         leg.AddEntry(0,                     "MadGraph+Pythia8", "")
         leg.AddEntry(histos[chname+madgsm], "SM t#bar{t}+jets", "ple")
         leg.AddEntry(histos[chname+madgxx], "SM+#it{"+S+"} t#bar{t}+jets", "ple")
         leg.AddEntry(0,                     "m_{#it{"+S+"}}="+str(M)+" GeV", "")
         leg.AddEntry(0,                     "sin(#beta-#alpha)="+str(SBA), "")
         leg.AddEntry(0,                     "tan#beta="+str(TANB), "")

         cnvr = TCanvas("cnvr"+channel+"."+hname, "", 1200,1200)
         cnvr.Divide(2,2)
         cnvr.Draw()

         p1 = cnvr.cd(1)
         p1.cd()
         histos[chname+madgsm].SetMaximum(Max*1.1)
         histos[chname+madgsm].SetMinimum(0)
         histos[chname+madgsm].Draw()
         histos[chname+madgxx].Draw("same")
         leg.Draw("same")
         p1.RedrawAxis()
         p1.Update()

         p2 = cnvr.cd(2)
         p2.cd()
         p2.SetGridy()
         htmp = histos[chname+"r"+madgxx].Clone(chname+"r"+madgxx+"_abs")
         htmp.GetYaxis().SetTitle(S+"^{2}+Interf[SM,"+S+"] "+histos[chname+madgsm].GetYaxis().GetTitle())
         h8TeVabs = histos[chname+"r"+madgxx].Clone(chname+"r"+madgxx+"_a")
         h8TeVsm = histos[chname+"r"+madgxx].Clone(chname+"r"+madgxx+"_sm")
         h8TeVabs.Reset()
         h8TeVsm.Reset()
         if(hname=="mtt8TeV" and str(S)=="A" and M==500):
            f8TeVa = TFile("out.root","READ")
            if(channel=="rmu"):
               h8TeVabs = f8TeVa.Get("SI_0") # 6
               h8TeVsm = f8TeVa.Get("tt_0") # 6
            if(channel=="re"):
               h8TeVabs = f8TeVa.Get("SI_3") # 7
               h8TeVsm = f8TeVa.Get("tt_3") # 7
               h8TeVabs.SetDirectory(0)
            h8TeVsm = normalizeToBinWidth(h8TeVsm,40)
            h8TeVabs.Multiply(h8TeVsm)
            h8TeVabs.SetDirectory(0)
            h8TeVabs.SetTitle("")
            h8TeVabs.GetXaxis().SetTitle(histos[chname+"r"+madgxx].GetXaxis().GetTitle())
            h8TeVabs.GetYaxis().SetTitle(histos[chname+"r"+madgxx].GetYaxis().GetTitle())
            h8TeVabs.SetMarkerStyle(25)
            h8TeVabs.SetMarkerSize(0.8)
            h8TeVabs.SetMarkerColor(ROOT.kGreen+2)
            h8TeVabs.SetLineColor(ROOT.kGreen+2)
            leg_abs = TLegend(0.5,0.75,0.87,0.95,"","brNDC")
            leg_abs.SetFillStyle(4000) # will be transparent
            leg_abs.SetFillColor(0)
            leg_abs.SetTextFont(42)
            leg_abs.SetBorderSize(0)
            leg_abs.AddEntry(0,       schannel,  "")
            leg_abs.AddEntry(0,       "Norm to "+str(lumi)+" fb^{-1}",  "")
            leg_abs.AddEntry(htmp,    "13 TeV", "ple")
            leg_abs.AddEntry(h8TeVabs,"8 TeV", "ple")
            # hmax = h8TeVabs.GetMaximum() if(h8TeVabs.GetMaximum()>htmp.GetMaximum()) else htmp.GetMaximum()
            # hmin = h8TeVabs.GetMinimum() if(h8TeVabs.GetMinimum()<htmp.GetMinimum()) else htmp.GetMinimum()
            # h8TeVabs.SetMinimum(hmin*1.2)
            # h8TeVabs.SetMaximum(hmax*1.2)
            h8TeVabs.Draw()
            htmp.Draw("same")
            leg_abs.Draw("same")
         else:
            htmp.Draw()
         lzero.Draw("same")
         htmp.Draw("same")
         p2.RedrawAxis()
         p2.Update()

         p3 = cnvr.cd(3)
         p3.cd()
         histos[chname+powheg].SetLineColor(ROOT.kBlue)
         histos[chname+powheg].SetMarkerColor(ROOT.kBlue)
         histos[chname+powheg].SetMarkerStyle(24)
         histos[chname+powheg].SetMarkerSize(0.8)
         leg_norm = TLegend(0.45,0.75,0.82,0.93,"","brNDC")
         leg_norm.SetFillStyle(4000) # will be transparent
         leg_norm.SetFillColor(0)
         leg_norm.SetTextFont(42)
         leg_norm.SetBorderSize(0)
         leg_norm.AddEntry(0,                     schannel,  "")
         leg_norm.AddEntry(histos[chname+powheg], "13 TeV Powheg+Pythia",    "ple")
         leg_norm.AddEntry(histos[chname+madgsm], "13 TeV MadGraph+Pythia8", "ple")
         h8TeV = histos[chname+powheg].Clone(chname+powheg+"_8TeV")
         h8TeV.Reset()
         if(hname=="mtt8TeV"):
            f8TeV = TFile("out.root","READ")
            if(channel=="rmu"):
               h8TeV = f8TeV.Get("tt_0")
               h8TeV.SetDirectory(0)
            if(channel=="re"):
               h8TeV = f8TeV.Get("tt_3")
               h8TeV.SetDirectory(0)
            h8TeV.SetTitle("")
            h8TeV.GetXaxis().SetTitle(histos[chname+powheg].GetXaxis().GetTitle())
            h8TeV.GetYaxis().SetTitle(histos[chname+powheg].GetYaxis().GetTitle())
            h8TeV.SetMarkerStyle(25)
            h8TeV.SetMarkerSize(0.8)
            h8TeV.SetMarkerColor(ROOT.kGreen+2)
            h8TeV.SetLineColor(ROOT.kGreen+2)
            h8TeV = normalizeToBinWidth(h8TeV,40)
            '''
            leg_norm.AddEntry(h8TeV, "8TeV (Po+Py)", "ple")
            h8TeV.GetYaxis().SetTitle("Normalised ( / 40 GeV)")
            histos[chname+madgsm].GetYaxis().SetTitle("Normalised ( / 40 GeV)")
            histos[chname+powheg].GetYaxis().SetTitle("Normalised ( / 40 GeV)")
            h8TeV.DrawNormalized()
            histos[chname+madgsm].DrawNormalized("same")
            histos[chname+powheg].DrawNormalized("same")
            h8TeV.DrawNormalized("same")
            '''
            leg_norm.AddEntry(h8TeV, "8 TeV Powheg+Pythia", "ple")
            leg_norm.AddEntry(0, "(normed. to 13 TeV integral)", "")
            h8TeV.Scale(histos[chname+powheg].Integral()/h8TeV.Integral())
            h8TeV.SetMaximum(h8TeV.GetMaximum()*1.2)
            h8TeV.Draw()
            histos[chname+madgsm].Draw("same")
            histos[chname+powheg].Draw("same")
            h8TeV.Draw("same")
         else:
            '''
            histos[chname+madgsm].DrawNormalized()
            histos[chname+powheg].DrawNormalized("same")
            '''
            histos[chname+madgsm].SetMaximum(histos[chname+madgsm].GetMaximum()*1.2)
            histos[chname+madgsm].Draw()
            histos[chname+powheg].Draw("same")
         leg_norm.Draw("same")
         p3.RedrawAxis()
         p3.Update()


         p4 = cnvr.cd(4)
         p4.cd()
         p4.SetGridy()
         histos[chname+"r"+madgxx].Divide(histos[chname+madgsm])
         #histos[chname+"r"+madgxx] = ttjets_style.divide(histos[chname+"r"+madgxx],histos[chname+madgsm])
         #histos[chname+"r"+madgxx] = ttjets_style.divide(histos[chname+"r"+madgxx],histos[chname+madgsm])
         histos[chname+"r"+madgxx].Scale(100)
         h8TeV = histos[chname+"r"+madgxx].Clone(chname+"r"+madgxx+"_8TeV")
         h8TeV.Reset()
         if(hname=="mtt8TeV" and str(S)=="A" and M==500):
            f8TeV = TFile("out.root","READ")
            if(channel=="rmu"):
               h8TeV = f8TeV.Get("SI_0")
               h8TeV.SetDirectory(0)
            if(channel=="re"):
               h8TeV = f8TeV.Get("SI_3")
               h8TeV.SetDirectory(0)
            h8TeV.Scale(100)
            h8TeV.SetTitle("")
            h8TeV.GetXaxis().SetTitle(histos[chname+"r"+madgxx].GetXaxis().GetTitle())
            h8TeV.GetYaxis().SetTitle(histos[chname+"r"+madgxx].GetYaxis().GetTitle())
            h8TeV.SetMarkerStyle(25)
            h8TeV.SetMarkerSize(0.8)
            h8TeV.SetMarkerColor(ROOT.kGreen+2)
            h8TeV.SetLineColor(ROOT.kGreen+2)
            hmax = h8TeV.GetMaximum() if(h8TeV.GetMaximum()>histos[chname+"r"+madgxx].GetMaximum()) else histos[chname+"r"+madgxx].GetMaximum()
            hmin = h8TeV.GetMinimum() if(h8TeV.GetMinimum()<histos[chname+"r"+madgxx].GetMinimum()) else histos[chname+"r"+madgxx].GetMinimum()
            h8TeV.SetMinimum(hmin*1.2)
            h8TeV.SetMaximum(hmax*1.2)
            h8TeV.Draw()
            histos[chname+"r"+madgxx].Draw("same")
            leg_dev = TLegend(0.5,0.75,0.87,0.95,"","brNDC")
            leg_dev.SetFillStyle(4000) # will be transparent
            leg_dev.SetFillColor(0)
            leg_dev.SetTextFont(42)
            leg_dev.SetBorderSize(0)
            leg_dev.AddEntry(0,                          schannel,  "")
            leg_dev.AddEntry(histos[chname+"r"+madgxx], "13 TeV", "ple")
            leg_dev.AddEntry(h8TeV,                     "8 TeV", "ple")
            leg_dev.Draw("same")
         else:
            histos[chname+"r"+madgxx].Draw()
         lzero.Draw("same")
         histos[chname+"r"+madgxx].Draw("same")
         p4.RedrawAxis()
         p4.Update()

         ##### write out the relative deviation histos
         outhistos.update({chname+"r"+madgxx:histos[chname+"r"+madgxx]})

         cnvr.Update()
         suffix = ""
         if(r==0    and nr>1): suffix = "("
         if(r==nr-1 and nr>1): suffix = ")"
         cnvr.SaveAs("figs/histosr."+outname+"."+hname+".pdf")
         cnvr.SaveAs("figs/histosr."+outname+".all.pdf"+suffix)
         r = r+1

outname = "s"+str(S)+"_m"+str(M)+"_sba"+sSBA+"_tanb"+sTANB+"_t"+str(TYPE)
outfile = TFile("figs/histosr."+outname+".reldev.root","recreate")
for hname,hist in outhistos.iteritems():
   hist.Write()
outfile.Write()
outfile.Close()

print "see figs/histos*"+"s"+str(S)+"_m"+str(M)+"_sba"+sSBA+"_tanb"+sTANB+"_t"+str(TYPE)+".*  (pdf/root)"
