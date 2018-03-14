import sys
import os
import math
import ROOT
from ROOT import *
from array import *
import ttjets_style

nameX = "A"
mX    = "500"
wThrs = 10#1.e10
channels = ["re","rmu"]
channel = channels[1]
figdir  = "/afs/cern.ch/user/h/hod/data/figs/"
filename = ".s"+nameX+"_m"+mX+"_sba10_tanb04_t2.merged.root"
pb2fb = 1.e3
lumi  = 20.3 # fb-1

# gROOT.ProcessLine(".L Loader.C+")
gROOT.SetBatch(1)

######## FUNCTIONS
def normalizeToBinWidth(h, unit=0): ## normalize to nEvts/40 GeV
   for b in xrange(h.GetNbinsX()+1):
      sf = unit/h.GetBinWidth(b) if(unit>0) else 1./h.GetBinWidth(b)
      h.SetBinContent(b, h.GetBinContent(b)*sf)
      h.SetBinError(b,   h.GetBinError(b)*sf)
   return h

def getminmax(h):
   Min = +1.e10
   Max = -1.e10
   for b in xrange(1,h.GetNbinsX()+1):
      y = h.GetBinContent(b)
      if(y==0): continue
      Min = y if(y<Min) else Min
      Max = y if(y>Max) else Max
   return (Min,Max)


####### HISTOS
listbins = [0,80,160,240,320,360,400,440,500,560,600,640,680,720,760,800,860,920,1040,1160,1280]
arrbins = array("d", listbins)
nbins = len(listbins)-1

hMEall = TGraph()
hMEbad = TGraph()
hmSM = TH1D("hmSM",";#it{m}_{#it{t}#bar{#it{t}}} [GeV];Events / 40 GeV",nbins,arrbins)
hmXX = TH1D("hmXX",";#it{m}_{#it{t}#bar{#it{t}}} [GeV];Events / 40 GeV",nbins,arrbins)
hmXR = TH1D("hmXR",";#it{m}_{#it{t}#bar{#it{t}}} [GeV];Events / 40 GeV",nbins,arrbins)

hmSM.Sumw2()
hmSM.SetLineWidth(2)
hmSM.SetLineColor(ROOT.kBlack)
hmSM.SetMarkerColor(ROOT.kBlack)
hmSM.SetMarkerStyle(24)
hmSM.SetMarkerSize(0.6)

hmXX.Sumw2()
hmXX.SetLineWidth(2)
hmXX.SetLineColor(ROOT.kRed)
hmXX.SetMarkerColor(ROOT.kRed)
hmXX.SetMarkerStyle(20)
hmXX.SetMarkerSize(0.6)

hmXR.Sumw2()
hmXR.SetLineWidth(2)
hmXR.SetLineColor(ROOT.kRed)
hmXR.SetMarkerColor(ROOT.kRed)
hmXR.SetMarkerStyle(20)
hmXR.SetMarkerSize(0.6)

######## ANALYSIS
hmX0 = hmXX.Clone("X0")
hmX0.SetLineWidth(1)
hmX0.SetLineColor(ROOT.kGreen)
hmX0.SetMarkerColor(ROOT.kGreen)
hmX0.Reset()
hmXr = hmXX.Clone("Xr")
hmXr.SetLineWidth(1)
hmXr.SetLineColor(ROOT.kGreen)
hmXr.SetMarkerColor(ROOT.kGreen)
hmXr.Reset()
hmSM0 = hmXX.Clone("SM0")
hmSM0.SetLineWidth(1)
hmSM0.SetLineColor(ROOT.kGreen)
hmSM0.SetMarkerColor(ROOT.kGreen)
hmSM0.Reset()
hmXd = hmXX.Clone("Xd")
hmXd.SetLineWidth(1)
hmXd.SetLineColor(ROOT.kGreen)
hmXd.SetMarkerColor(ROOT.kGreen)
hmXd.Reset()

n = 1
b = 1
for j in xrange(1,15+1):
   sj = "j"+str(j) if(j>9) else "j0"+str(j)
   fname = figdir+channel+".40720X"+filename.replace("merged",sj)
   print "fname=",fname
   tfile = TFile(fname,"READ")
   ttree = tfile.Get("debug"+channel)
   hmX0.Add(tfile.Get("mtt8TeV"))
   hmXr.Add(tfile.Get("mtt8TeVr"))
   hmXd.Add(tfile.Get("mtt8TeVr"))
   for event in ttree:
      if(n%50000==0): print "processed %s and reweighting %g" % (ttree.GetName(),n)
      wXXtmp = event.w2HDM[0] #event.me2XX[0]/event.me2SM[0]
      wXX    = event.w0[0] if(wXXtmp>wThrs) else event.w[0]
      wSM    = event.w0[0]
      hmSM.Fill(event.mttReco[0],wSM)
      hmXX.Fill(event.mttReco[0],wXX)
      hmXR.Fill(event.mttReco[0],(wXX-wSM))
      hMEall.SetPoint(hMEall.GetN(),event.me2SM[0],event.me2XX[0])
      if(wXXtmp>wThrs): hMEbad.SetPoint(hMEbad.GetN(),event.me2SM[0],event.me2XX[0])
      if(wXXtmp>wThrs):
         ids = ""
         p4 = "p=["
         for i in xrange(event.id.size()):
            ids += str(int(event.id[i]))+" "
            p4 += "\n   [%g,%g,%g,%g]," % (event.e[i],event.px[i],event.py[i],event.pz[i])
         p4 += "\n]\n"
         print "bad event[%g], me2SM=%g, me2XX=%g, w2HDM=%g, ME size=%g --> %s\n%s" % (b,event.me2SM[0],event.me2XX[0],event.w2HDM[0],event.id.size(),ids,p4)
         b += 1
      n += 1

for j in xrange(1,15+1):
   sj = "j"+str(j) if(j>9) else "j0"+str(j)
   fname = figdir+channel+".40720X."+sj+".root"
   print "fname=",fname
   tfile = TFile(fname,"READ")
   hmSM0.Add(tfile.Get("mtt8TeV"))


######## PLOT
hmSM0.Scale(lumi*pb2fb)
hmSM.Scale(lumi*pb2fb)
hmXX.Scale(lumi*pb2fb)
hmXR.Scale(lumi*pb2fb)
hmX0.Scale(lumi*pb2fb)
hmXr.Scale(lumi*pb2fb)
hmXd.Scale(lumi*pb2fb)
hmSM0 = normalizeToBinWidth(hmSM0,40)
hmSM = normalizeToBinWidth(hmSM,40)
hmXX = normalizeToBinWidth(hmXX,40)
hmXR = normalizeToBinWidth(hmXR,40)
hmX0 = normalizeToBinWidth(hmX0,40)
hmXr = normalizeToBinWidth(hmXr,40)
hmXd = normalizeToBinWidth(hmXd,40)


pdfname = "figs/"+channel+filename.replace(".root",".pdf")

cnv = TCanvas("cnv","",1200,1200)
cnv.Divide(2,2)
cnv.Draw()
pad1 = cnv.cd(1)
pad1.SetGrid(1,1)
hmax = hmSM.GetMaximum() if(hmSM.GetMaximum()>hmXX.GetMaximum()) else hmXX.GetMaximum()
hmax = hmX0.GetMaximum() if(hmX0.GetMaximum()>hmax) else hmax
hmSM.SetMaximum(hmax*1.1)
hmSM.SetMinimum(0)
hmSM.Draw()
hmXX.Draw("same")
hmX0.Draw("hist same")
for b in xrange(1,hmXX.GetNbinsX()+1):
  x0 = hmX0.GetBinContent(b)
  xx = hmXX.GetBinContent(b)
  R = x0/xx if(xx>0) else -1
  print "R[%g]=%g" % (b,R)
pad1.RedrawAxis()
pad2 = cnv.cd(2)
pad2.SetGrid(1,1)
hmax = hmXR.GetMaximum() if(hmXR.GetMaximum()>hmXr.GetMaximum()) else hmXr.GetMaximum()
hmin = hmXR.GetMinimum() if(hmXR.GetMinimum()<hmXr.GetMinimum()) else hmXr.GetMinimum()
hmXR.SetMaximum(hmax*1.1)
hmXR.SetMinimum(hmin*1.1)
hmXR.Draw()
hmXr.Draw("hist same")
pad2.RedrawAxis()
pad3 = cnv.cd(3)
pad3.SetGrid(1,1)
pad4 = cnv.cd(4)
pad4.SetGrid(1,1)
hmXD = hmXR.Clone("relative")
hmXD.Divide(hmSM)
hmXD.Scale(100.)
hmXd0 = hmXd.Clone("relative0")
hmXd0.Divide(hmSM0)
hmXd0.Scale(100)
hmXD.GetYaxis().SetTitle("("+nameX+"^{2}+Interf[SM,"+nameX+"])/SM [%]")
hmXd.GetYaxis().SetTitle("("+nameX+"^{2}+Interf[SM,"+nameX+"])/SM [%]")
hmin1,hmax1 = getminmax(hmXD)
hmin2,hmax2 = getminmax(hmXd0)
hmax = hmax1 if(hmax1>hmax2) else hmax2
hmin = hmin1 if(hmin1<hmin2) else hmin2
hmXD.SetMaximum(hmax*1.1)
hmXD.SetMinimum(hmin*1.1)
hmXD.Draw()
hmXd0.Draw("same")
pad4.RedrawAxis()
cnv.Update()
cnv.SaveAs(pdfname)

'''
cnv = TCanvas("cnv","",1000,1000)
cnv.Draw()
cnv.cd()
cnv.SetLogy()
cnv.SetLogx()
cnv.SetGrid(1,1)
line = TLine(hMEall.GetXaxis().GetXmin(),hMEall.GetYaxis().GetXmin(), hMEall.GetXaxis().GetXmax(),hMEall.GetYaxis().GetXmax())
line.SetLineColor(ROOT.kGreen)
hMEbad.SetMarkerColor(ROOT.kRed)
mg = TMultiGraph()
mg.SetTitle(";ME_{SM}^{2};ME_{2HDM}^{2}");
mg.Add(hMEall)
if(hMEbad.GetN()>0): mg.Add(hMEbad)
mg.Draw("ap")
line.Draw("same")
mg.GetXaxis().SetLimits(1e-11,1e+2)
cnv.Modified()
mg.GetYaxis().SetLimits(1e-11,1e+2)
cnv.Modified() # either redraw your multigraph object or add cnv.Modified() once you have set the limits.
#mg.Draw("ap")
cnv.RedrawAxis()
cnv.Update()
cnv.SaveAs(pdfname.replace("pdf","png"))
'''
