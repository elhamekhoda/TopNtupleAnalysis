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
'''

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
#hnames  = ["trueMttLow1", "trueMttLow2", "trueMtt8TeV", "trueMtt", "mttLow1", "mttLow2", "mttLow3", "mttLow4", "mtt8TeV", "mtt", "chi2", "MET", "mwt", "mwhad_res", "mthad_res", "mtlep_res", "lepPt", "lepPtLow1", "lepPtLow2", "lepPtLow3", "lepEta", "vtxz", "npv", "btagSF", "nTrkBtagJets", "nJets", "mtt_resolution", ]
hnames  = ["trueMtt8TeV", "mtt8TeV", "trueMtt", "mtt", ]
hnamesr = ["trueMtt8TeV", "mtt8TeV", "trueMtt", "mtt", ]
htitles = { "trueMtt8TeV":";True #it{m}_{tt} [GeV];Events / 40 GeV",
            "trueMtt":";True #it{m}_{tt} [GeV];Events / 40 GeV",
            "mtt8TeV":";#it{m}_{tt} [GeV];Events / 40 GeV",
            "mtt":";#it{m}_{tt} [GeV];Events / 40 GeV",
            "chi2":";#chi^{2};Events",
            "MET":";#it{E}_{T}^{miss} [GeV];Events / 10 GeV",
            "mwt":";MWT [GeV];Events",
            "mwhad_res":";#it{m}_{#it{W}}^{had} [GeV];Events",
            "mthad_res":";#it{m}_{#it{t}-had} [GeV];Events / 40 GeV",
            "mtlep_res":";#it{m}_{#it{t}-lep} [GeV];Events / 40 GeV",
            "lepPt":";Lepton #it{p}_{T} [GeV];Events",
            "lepPtLow2":";Lepton #it{p}_{T} [GeV];Events",
            "lepEta":";Lepton #it{#eta};Events",
            "vtxz":";Vertex #it{z} [?];Events",
            "npv":";#it{N}_{PV};Events",
            "btagSF":";b-tagging SF;Events",
            "nTrkBtagJets":";#it{N}_{b-jets}^{trk};Events",
            "nJets":";#it{N}_{jets};Events",
            "mtt_resolution":";#it{m}_{tt}^{rec}/#it{m}_{tt}^{tru}-1;Events",
            "trueHT_ME":";True H_{T}(partons) [GeV];Events",
            "trueHT_jets":";True H_{T}(truth jets) [GeV];Events",}
#channels = ["re", "rmu", "be", "bmu"]
channels = ["re", "rmu"]
schannels = {"re":"Resolved electron", "rmu":"Resolved muon", "be":"Boosted electron", "bmu":"Boosted muon"}
dsids   = [407200,407201,407202,407203,407204]
hSum    = {}

## Norm MG = L_data/L_mc = L_data / (SumW/(Sigma_AMI*GenEff)) = L_data * (Sigma_AMI*GenEff)/SumW
## Norm Po = L_data/L_mc = L_data / (SumW/(Sigma_NLO*GenEff*kFNNLO)) = L_data * (Sigma_NLO*GenEff*kFNNLO)/SumW
## Norm MG = Norm Po ==> Norm MG = 

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


#SigmaNNLO = (377.9932/5.4383E-01)*1.1949
def geth(dsid,channel,hname,scale=False):
  #print "trying to get %g, %s, %s" % (dsid,channel,hname)
  jobconfXX = channel+"."+str(dsid)+".s"+str(S)+"_m"+str(M)+"_sba"+sSBA+"_tanb"+sTANB+"_t"+str(TYPE)
  jobconfSM = channel+"."+str(dsid)
  if(dsid==410000): jobconfXX = jobconfSM
  fnameXX = jobconfXX+".merged.root"
  fnameSM = jobconfSM+".merged.root"
  tfileXX = TFile(prefix+fnameXX,"READ")
  tfileSM = TFile(prefix+fnameSM,"READ")
  htmpXX = tfileXX.Get(hname)
  htmpSM = tfileSM.Get(hname)
  htitle = htitles[hname]
  htmpXX.SetTitle(htitle)
  htmpSM.SetTitle(htitle)
  htmpXX.Scale(lumi*pb2fb)
  htmpSM.Scale(lumi*pb2fb)
  if("Events / " in htitle):
     unit = float(htitle.split(";")[2].split(" ")[2])
     htmpXX = normalizeToBinWidth(htmpXX,unit)
     htmpSM = normalizeToBinWidth(htmpSM,unit)
  htmpXX.SetDirectory(0)
  htmpSM.SetDirectory(0)
  return (htmpXX,htmpSM)

def gethr(dsid,channel,hname,xtitle,ytitle=""):
  jobconfXX = channel+"."+str(dsid)+".s"+str(S)+"_m"+str(M)+"_sba"+sSBA+"_tanb"+sTANB+"_t"+str(TYPE)
  jobconfSM = channel+"."+str(dsid)
  chname = channel+"_"+hname
  if(dsid==410000): jobconfXX = jobconfSM
  fname = jobconfXX+".merged.root"
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


## get all histos and sum up
for channel in channels:
   for hname in hnames:
      chname = channel+"_"+hname
      for i in xrange(len(dsids)):
         dsid = dsids[i]
         hXX, hSM = geth(dsid,channel,hname,True)
         if(i==0):
            hSum.update({chname+"_XX":hXX})
            hSum.update({chname+"_SM":hSM})
            if(hname in hnamesr):
               hrXX = gethr(dsid,channel,hname+"r",hSum[chname+"_SM"].GetXaxis().GetTitle(),"("+S+"^{2}+Interf[SM,"+S+"])/SM [%]")
               hSum.update({chname+"r_XX":hrXX})
         else:
            hSum[chname+"_XX"].Add(hXX)
            hSum[chname+"_SM"].Add(hSM)
            if(hname in hnamesr):
               hrXX = gethr(dsid,channel,hname+"r",hSum[chname+"_SM"].GetXaxis().GetTitle(),"("+S+"^{2}+Interf[SM,"+S+"])/SM [%]")
               hSum[chname+"r_XX"].Add(hrXX)

## make the figs dir if not already made
p = subprocess.Popen("mkdir figs", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate()

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
      hPoPyXX,hPoPySM = geth(410000,channel,hname,False)
      hrSM = hPoPySM.Clone("ratio_"+channel+"_SM")
      hrXX = hPoPyXX.Clone("ratio_"+channel+"_XX")

      if(hname in hnamesr):
         #hSum[chname+"r_XX"].SetMinimum(-10)
         #hSum[chname+"r_XX"].SetMaximum(+10)
         hSum[chname+"r_XX"].SetLineColor(ROOT.kBlack)
         hSum[chname+"r_XX"].SetMarkerColor(ROOT.kBlack)
         hSum[chname+"r_XX"].SetMarkerStyle(20)
         hSum[chname+"r_XX"].SetMarkerSize(0.8)
         

      cnv = TCanvas("cnv"+channel+"."+hname, "", 1200,600)
      cnv.Divide(2,1)
      cnv.Draw()
      p1 = cnv.cd(1)
      p1.Divide(1,2)
      tvp_hists = p1.cd(1)
      tvp_ratio = p1.cd(2)
      tvp_hists.SetPad(0.00, 0.305, 1.00, 0.99)
      tvp_ratio.SetPad(0.00, 0.050, 1.00, 0.32)
      tvp_hists.SetBottomMargin(0.012)
      tvp_ratio.SetBottomMargin(0.35)
      tvp_ratio.SetTopMargin(0.012)
      tvp_hists.SetTicks(1,1)
      tvp_ratio.SetTicks(1,1)

      tvp_hists.cd()
      tvp_hists.SetLogy()
      tvp_hists.SetTicks(1,1)
      hSum[chname+"_SM"].SetLineColor(ROOT.kBlack)
      hSum[chname+"_SM"].SetMarkerColor(ROOT.kBlack)
      hSum[chname+"_SM"].SetMarkerStyle(20)
      hSum[chname+"_SM"].SetMarkerSize(0.8)
 
      hSum[chname+"_XX"].SetLineColor(ROOT.kOrange+10)
      hSum[chname+"_XX"].SetMarkerColor(ROOT.kOrange+10)
      hSum[chname+"_XX"].SetMarkerStyle(24)
      hSum[chname+"_XX"].SetMarkerSize(0.8)

      hPoPySM.SetLineColor(ROOT.kBlue)
      hPoPySM.SetMarkerColor(ROOT.kBlue)
      hPoPySM.SetMarkerStyle(24)
      hPoPySM.SetMarkerSize(0.8)
      hmin = hSum[chname+"_SM"].GetMinimum() if (hPoPySM.GetMinimum()>hSum[chname+"_SM"].GetMinimum()) else hPoPySM.GetMinimum()
      hmax = hSum[chname+"_SM"].GetMaximum() if (hPoPySM.GetMaximum()<hSum[chname+"_SM"].GetMaximum()) else hPoPySM.GetMaximum()
      hmin = hSum[chname+"_SM"].GetMinimum() if (hSum[chname+"_SM"].GetMinimum()>0) else 0.2
      
      hSum[chname+"_SM"].SetMinimum(hmin)
      hSum[chname+"_SM"].SetMaximum(hmax*2)
      hSum[chname+"_XX"].SetMinimum(hmin)
      hSum[chname+"_XX"].SetMaximum(hmax*2)
      '''
      hSum[chname+"_SM"].SetMinimum(0)
      hSum[chname+"_SM"].SetMaximum(hmax*1.1)
      hSum[chname+"_XX"].SetMinimum(0)
      hSum[chname+"_XX"].SetMaximum(hmax*1.1)
      '''

      hSum[chname+"_SM"].GetXaxis().SetLabelSize(hSum[chname+"_SM"].GetXaxis().GetLabelSize()*1.5)
      hSum[chname+"_SM"].GetYaxis().SetLabelSize(hSum[chname+"_SM"].GetYaxis().GetLabelSize()*1.5)
      hSum[chname+"_SM"].GetXaxis().SetTitleSize(hSum[chname+"_SM"].GetXaxis().GetTitleSize()*1.5)
      hSum[chname+"_SM"].GetYaxis().SetTitleSize(hSum[chname+"_SM"].GetYaxis().GetTitleSize()*1.5)
      hSum[chname+"_SM"].GetYaxis().SetTitleOffset(0.8)
      hSum[chname+"_SM"].GetXaxis().SetTitleOffset(0.93)

      hSum[chname+"_XX"].GetXaxis().SetLabelSize(hSum[chname+"_XX"].GetXaxis().GetLabelSize()*1.5)
      hSum[chname+"_XX"].GetYaxis().SetLabelSize(hSum[chname+"_XX"].GetYaxis().GetLabelSize()*1.5)
      hSum[chname+"_XX"].GetXaxis().SetTitleSize(hSum[chname+"_XX"].GetXaxis().GetTitleSize()*1.5)
      hSum[chname+"_XX"].GetYaxis().SetTitleSize(hSum[chname+"_XX"].GetYaxis().GetTitleSize()*1.5)
      hSum[chname+"_XX"].GetYaxis().SetTitleOffset(0.8)
      hSum[chname+"_XX"].GetXaxis().SetTitleOffset(0.93)

      hPoPySM.GetXaxis().SetLabelSize(hPoPySM.GetXaxis().GetLabelSize()*1.5)
      hPoPySM.GetYaxis().SetLabelSize(hPoPySM.GetYaxis().GetLabelSize()*1.5)
      hPoPySM.GetXaxis().SetTitleSize(hPoPySM.GetXaxis().GetTitleSize()*1.5)
      hPoPySM.GetYaxis().SetTitleSize(hPoPySM.GetYaxis().GetTitleSize()*1.5)
      hPoPySM.GetYaxis().SetTitleOffset(0.8)
      hPoPySM.GetXaxis().SetTitleOffset(0.93)

      #leg_hists = TLegend(0.5,0.55,0.87,0.95,"","brNDC")
      leg_hists = TLegend(0.5,0.65,0.87,0.95,"","brNDC")
      leg_hists.SetFillStyle(4000) # will be transparent
      leg_hists.SetFillColor(0)
      leg_hists.SetTextFont(42)
      leg_hists.SetBorderSize(0)
      leg_hists.AddEntry(0,                  schannel,  "")
      leg_hists.AddEntry(hPoPySM,            "SM Powheg+Pythia",    "ple")
      leg_hists.AddEntry(hSum[chname+"_SM"], "SM MadGraph+Pythia8", "ple")
      #leg_hists.AddEntry(hSum[chname+"_XX"], "2HDM MadGraph+Pythia8", "ple")
      #leg_hists.AddEntry(0,                  "m_{#it{"+S+"}}="+str(M)+" GeV", "")
      #leg_hists.AddEntry(0,                  "sin(#beta-#alpha)="+str(SBA), "")
      #leg_hists.AddEntry(0,                  "tan#beta="+str(TANB), "")

      hSum[chname+"_SM"].Draw()
      hPoPySM.Draw("same")
      #hSum[chname+"_XX"].Draw("same")
      leg_hists.Draw("same")
      tvp_hists.RedrawAxis()

      sXtitle = hrSM.GetXaxis().GetTitle()
      hrSM.SetTitle(";"+sXtitle+";Ratio")
      hrSM.SetLineColor(ROOT.kBlue)
      hrSM.SetMarkerColor(ROOT.kBlue)
      hrSM.SetMarkerStyle(24)
      hrSM.SetMarkerSize(0.8)
      hrSM.Divide(hPoPySM,hSum[chname+"_SM"])
      #hrSM = ttjets_style.divide(hPoPySM,hSum[chname+"_SM"])
      #hrSM = ttjets_style.divide(hPoPySM,hSum[chname+"_SM"])
      hrSM.SetMinimum(0.75)
      hrSM.SetMaximum(1.25)

      hrXX.Reset()
      hrXX.SetTitle(";"+sXtitle+";Ratio")
      hrXX.SetLineColor(ROOT.kOrange+10)
      hrXX.SetMarkerColor(ROOT.kOrange+10)
      hrXX.SetMarkerStyle(24)
      hrXX.SetMarkerSize(0.8)
      hrXX.Divide(hSum[chname+"_XX"],hSum[chname+"_SM"])
      #hrXX = ttjets_style.divide(hSum[chname+"_XX"],hSum[chname+"_SM"])
      #hrXX = ttjets_style.divide(hSum[chname+"_XX"],hSum[chname+"_SM"])
      hrXX.SetMinimum(0.75)
      hrXX.SetMaximum(1.25)
   
      hrSM.GetXaxis().SetLabelSize(hrSM.GetXaxis().GetLabelSize()*3.5)
      hrSM.GetYaxis().SetLabelSize(hrSM.GetYaxis().GetLabelSize()*2.7)
      hrSM.GetXaxis().SetTitleSize(hrSM.GetXaxis().GetTitleSize()*3.5)
      hrSM.GetYaxis().SetTitleSize(hrSM.GetYaxis().GetTitleSize()*3.5)
      hrSM.GetYaxis().SetTitleOffset(0.35)
      hrSM.GetXaxis().SetTitleOffset(0.93)

      hrXX.GetXaxis().SetLabelSize(hrXX.GetXaxis().GetLabelSize()*3.5)
      hrXX.GetYaxis().SetLabelSize(hrXX.GetYaxis().GetLabelSize()*2.7)
      hrXX.GetXaxis().SetTitleSize(hrXX.GetXaxis().GetTitleSize()*3.5)
      hrXX.GetYaxis().SetTitleSize(hrXX.GetYaxis().GetTitleSize()*3.5)
      hrXX.GetYaxis().SetTitleOffset(0.35)
      hrXX.GetXaxis().SetTitleOffset(0.93)

      tvp_ratio.cd()
      tvp_ratio.SetGridy()
      hrSM.Draw("e1p")
      #hrXX.Draw("e1p same")
      tvp_ratio.Update()
      tvp_ratio.RedrawAxis()
  
      p2 = cnv.cd(2)
      p2.SetLogy()
      p2.SetTicks(1,1)

      leg_singles = TLegend(0.5,0.55,0.87,0.93,"","brNDC")
      leg_singles.SetFillStyle(4000) # will be transparent
      leg_singles.SetFillColor(0)
      leg_singles.SetTextFont(42)
      leg_singles.SetBorderSize(0)
      leg_singles.AddEntry(0, schannel, "")
      leg_singles.AddEntry(0, "MadGraph+Pythia8", "")
      for i in xrange(len(dsids)):
         dsid = dsids[i]
         htmp1XX,htmp1SM = geth(dsid,channel,hname,True)
         htmp1SM.SetLineColor(samples[dsid]["Col"])
         htmp1SM.SetMarkerColor(samples[dsid]["Col"])
         htmp1SM.SetMarkerStyle(20)
         htmp1SM.SetMarkerSize(0.8)
         hmin = hSum[chname+"_SM"].GetMinimum() if (hSum[chname+"_SM"].GetMinimum()>0) else 0.1
         htmp1SM.SetMinimum(hmin)
         #htmp1SM.SetMinimum(0)
         if(i==0): htmp1SM.DrawCopy()
         else:     htmp1SM.DrawCopy("same")
         leg_singles.AddEntry(htmp1SM, samples[dsid]["Slice"], "ple")
      leg_singles.Draw("same")
      p2.RedrawAxis()
      cnv.Update()
      suffix = ""
      if(j==0   and n>1): suffix = "("
      if(j==n-1 and n>1): suffix = ")"
      cnv.SaveAs("figs/histos."+outname+"."+hname+".pdf")
      cnv.SaveAs("figs/histos."+outname+".all.pdf"+suffix)

      ### Residuals
      if(hname in hnamesr):
         cnvr = TCanvas("cnvr"+channel+"."+hname, "", 1200,1200)
         cnvr.Divide(2,2)
         cnvr.Draw()
         p1 = cnvr.cd(1)
         #p1.SetLogy()
         p1.cd()

         hSum[chname+"_SM"].GetXaxis().SetLabelSize(hSum[chname+"_SM"].GetXaxis().GetLabelSize()/1.5)
         hSum[chname+"_SM"].GetYaxis().SetLabelSize(hSum[chname+"_SM"].GetYaxis().GetLabelSize()/1.5)
         hSum[chname+"_SM"].GetXaxis().SetTitleSize(hSum[chname+"_SM"].GetXaxis().GetTitleSize()/1.5)
         hSum[chname+"_SM"].GetYaxis().SetTitleSize(hSum[chname+"_SM"].GetYaxis().GetTitleSize()/1.5)
         #hSum[chname+"_SM"].GetYaxis().SetTitleOffset(0.8)
         #hSum[chname+"_SM"].GetXaxis().SetTitleOffset(0.93)

         hSum[chname+"_XX"].GetXaxis().SetLabelSize(hSum[chname+"_XX"].GetXaxis().GetLabelSize()/1.5)
         hSum[chname+"_XX"].GetYaxis().SetLabelSize(hSum[chname+"_XX"].GetYaxis().GetLabelSize()/1.5)
         hSum[chname+"_XX"].GetXaxis().SetTitleSize(hSum[chname+"_XX"].GetXaxis().GetTitleSize()/1.5)
         hSum[chname+"_XX"].GetYaxis().SetTitleSize(hSum[chname+"_XX"].GetYaxis().GetTitleSize()/1.5)
         #hSum[chname+"_XX"].GetYaxis().SetTitleOffset(0.8)
         #hSum[chname+"_XX"].GetXaxis().SetTitleOffset(0.93)

         MinSM,MaxSM = getminmax(hSum[chname+"_SM"])
         MinXX,MaxXX = getminmax(hSum[chname+"_XX"])
         Min = MinSM if(MinSM<MinXX) else MinXX 
         Max = MaxSM if(MaxSM>MaxXX) else MaxXX 
         hSum[chname+"_SM"].SetMaximum(Max*1.1)
         hSum[chname+"_SM"].SetMinimum(0)
         hSum[chname+"_SM"].Draw()
         hSum[chname+"_XX"].Draw("same")     
 
         leg = TLegend(0.5,0.55,0.87,0.95,"","brNDC")
         leg.SetFillStyle(4000) # will be transparent
         leg.SetFillColor(0)
         leg.SetTextFont(42)
         leg.SetBorderSize(0)
         leg.AddEntry(0,                  schannel,  "")
         leg.AddEntry(0,                  "MadGraph+Pythia8", "")
         leg.AddEntry(hSum[chname+"_SM"], "SM t#bar{t}+jets", "ple")
         leg.AddEntry(hSum[chname+"_XX"], "SM+#it{"+S+"} t#bar{t}+jets", "ple")
         leg.AddEntry(0,                  "m_{#it{"+S+"}}="+str(M)+" GeV", "")
         leg.AddEntry(0,                  "sin(#beta-#alpha)="+str(SBA), "")
         leg.AddEntry(0,                  "tan#beta="+str(TANB), "")
         leg.Draw("same")
         p1.RedrawAxis()
         p1.Update()

         lzero = TLine(hSum[chname+"_SM"].GetXaxis().GetXmin(), 0, hSum[chname+"_SM"].GetXaxis().GetXmax(), 0)
         lzero.SetLineColor(kRed)

         p2 = cnvr.cd(2)
         p2.cd()
         p2.SetGridy()
         htmp = hSum[chname+"r_XX"].Clone("r")
         htmp.GetYaxis().SetTitle(S+"^{2}+Interf[SM,"+S+"] "+hSum[chname+"_SM"].GetYaxis().GetTitle())
         htmp.Draw()
         h8TeVabs = htmp.Clone("a")
         h8TeVsm = htmp.Clone("sm")
         h8TeVabs.Reset()
         h8TeVsm.Reset()
         if(hname=="mtt8TeV"):
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
            h8TeVabs.GetXaxis().SetTitle(htmp.GetXaxis().GetTitle())
            h8TeVabs.GetYaxis().SetTitle(htmp.GetYaxis().GetTitle())
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
            hmax = h8TeVabs.GetMaximum() if(h8TeVabs.GetMaximum()>htmp.GetMaximum()) else htmp.GetMaximum()
            hmin = h8TeVabs.GetMinimum() if(h8TeVabs.GetMinimum()<htmp.GetMinimum()) else htmp.GetMinimum()
            h8TeVabs.SetMinimum(hmin*1.2)
            h8TeVabs.SetMaximum(hmax*1.2)
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
         hSumSM = hSum[chname+"_SM"].Clone("sm")
         hPoPyXXtmp,hPoPySMtmp = geth(410000,channel,hname,False)
         hPoPySMtmp.SetLineColor(ROOT.kBlue)
         hPoPySMtmp.SetMarkerColor(ROOT.kBlue)
         hPoPySMtmp.SetMarkerStyle(24)
         hPoPySMtmp.SetMarkerSize(0.8)
         leg_norm = TLegend(0.45,0.75,0.82,0.93,"","brNDC")
         leg_norm.SetFillStyle(4000) # will be transparent
         leg_norm.SetFillColor(0)
         leg_norm.SetTextFont(42)
         leg_norm.SetBorderSize(0)
         leg_norm.AddEntry(0,                  schannel,  "")
         leg_norm.AddEntry(hPoPySMtmp,         "13 TeV Powheg+Pythia",    "ple")
         leg_norm.AddEntry(hSum[chname+"_SM"], "13 TeV MadGraph+Pythia8", "ple")
         h8TeV = hPoPySMtmp.Clone("8tev")
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
            h8TeV.GetXaxis().SetTitle(hPoPySMtmp.GetXaxis().GetTitle())
            h8TeV.GetYaxis().SetTitle(hPoPySMtmp.GetYaxis().GetTitle())
            h8TeV.SetMarkerStyle(25)
            h8TeV.SetMarkerSize(0.8)
            h8TeV.SetMarkerColor(ROOT.kGreen+2)
            h8TeV.SetLineColor(ROOT.kGreen+2)
            h8TeV = normalizeToBinWidth(h8TeV,40)
            '''
            leg_norm.AddEntry(h8TeV, "8TeV (Po+Py)", "ple")
            h8TeV.GetYaxis().SetTitle("Normalised ( / 40 GeV)")
            hSumSM.GetYaxis().SetTitle("Normalised ( / 40 GeV)")
            hPoPySMtmp.GetYaxis().SetTitle("Normalised ( / 40 GeV)")
            h8TeV.DrawNormalized()
            hSumSM.DrawNormalized("same")
            hPoPySMtmp.DrawNormalized("same")
            h8TeV.DrawNormalized("same")
            '''
            leg_norm.AddEntry(h8TeV, "8 TeV Powheg+Pythia", "ple")
            leg_norm.AddEntry(0, "(normed. to 13 TeV integral)", "")
            h8TeV.Scale(hPoPySMtmp.Integral()/h8TeV.Integral())
            h8TeV.SetMaximum(h8TeV.GetMaximum()*1.2)
            h8TeV.Draw()
            hSumSM.Draw("same")
            hPoPySMtmp.Draw("same")
            h8TeV.Draw("same")
         else:
            '''
            hSumSM.DrawNormalized()
            hPoPySMtmp.DrawNormalized("same")
            '''
            hSumSM.SetMaximum(hSumSM.GetMaximum()*1.2)
            hSumSM.Draw()
            hPoPySMtmp.Draw("same")
         leg_norm.Draw("same")
         p3.RedrawAxis()
         p3.Update()


         p4 = cnvr.cd(4)
         p4.cd()
         p4.SetGridy()

         hSum[chname+"r_XX"].Divide(hSum[chname+"_SM"])
         #hSum[chname+"r_XX"] = ttjets_style.divide(hSum[chname+"r_XX"],hSum[chname+"_SM"])
         #hSum[chname+"r_XX"] = ttjets_style.divide(hSum[chname+"r_XX"],hSum[chname+"_SM"])
         hSum[chname+"r_XX"].Scale(100)
         h8TeV = hSum[chname+"r_XX"].Clone("8tev")
         h8TeV.Reset()
         if(hname=="mtt8TeV"):
            f8TeV = TFile("out.root","READ")
            if(channel=="rmu"):
               h8TeV = f8TeV.Get("SI_0")
               h8TeV.SetDirectory(0)
            if(channel=="re"):
               h8TeV = f8TeV.Get("SI_3")
               h8TeV.SetDirectory(0)
            h8TeV.Scale(100)
            h8TeV.SetTitle("")
            h8TeV.GetXaxis().SetTitle(hSum[chname+"r_XX"].GetXaxis().GetTitle())
            h8TeV.GetYaxis().SetTitle(hSum[chname+"r_XX"].GetYaxis().GetTitle())
            h8TeV.SetMarkerStyle(25)
            h8TeV.SetMarkerSize(0.8)
            h8TeV.SetMarkerColor(ROOT.kGreen+2)
            h8TeV.SetLineColor(ROOT.kGreen+2)
            hmax = h8TeV.GetMaximum() if(h8TeV.GetMaximum()>hSum[chname+"r_XX"].GetMaximum()) else hSum[chname+"r_XX"].GetMaximum()
            hmin = h8TeV.GetMinimum() if(h8TeV.GetMinimum()<hSum[chname+"r_XX"].GetMinimum()) else hSum[chname+"r_XX"].GetMinimum()
            h8TeV.SetMinimum(hmin*1.2)
            h8TeV.SetMaximum(hmax*1.2)
            h8TeV.Draw()
            hSum[chname+"r_XX"].Draw("same")

            leg_dev = TLegend(0.5,0.75,0.87,0.95,"","brNDC")
            leg_dev.SetFillStyle(4000) # will be transparent
            leg_dev.SetFillColor(0)
            leg_dev.SetTextFont(42)
            leg_dev.SetBorderSize(0)
            leg_dev.AddEntry(0,                  schannel,  "")
            leg_dev.AddEntry(hSum[chname+"r_XX"], "13 TeV", "ple")
            leg_dev.AddEntry(h8TeV,               "8 TeV", "ple")
            leg_dev.Draw("same")
         else:
            hSum[chname+"r_XX"].Draw()
         lzero.Draw("same")
         hSum[chname+"r_XX"].Draw("same")
         p4.RedrawAxis()
         p4.Update()
         cnvr.Update()
         suffix = ""
         if(r==0    and nr>1): suffix = "("
         if(r==nr-1 and nr>1): suffix = ")"
         cnvr.SaveAs("figs/histosr."+outname+"."+hname+".pdf")
         cnvr.SaveAs("figs/histosr."+outname+".all.pdf"+suffix)
         r = r+1
print "see figs/histos*"+"s"+str(S)+"_m"+str(M)+"_sba"+sSBA+"_tanb"+sTANB+"_t"+str(TYPE)+".*.pdf"
