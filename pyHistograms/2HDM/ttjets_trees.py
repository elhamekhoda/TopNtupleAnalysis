import sys
import os
import math
import ROOT
from ROOT import *
from array import *

nameX = "H"
channels = ["re","rmu"]
channel = channels[1]
figdir  = "/afs/cern.ch/user/h/hod/data/figs/"
filename = ".s"+nameX+"_m600_sba10_tanb04_t2.allmerged.root"
pb2fb = 1.e3
lumi  = 40 # fb-1

# gROOT.ProcessLine(".L Loader.C+")
gROOT.SetBatch(1)

######## FUNCTIONS
def normalizeToBinWidth(h, unit=0): ## normalize to nEvts/40 GeV
   for b in xrange(h.GetNbinsX()+1):
      sf = unit/h.GetBinWidth(b) if(unit>0) else 1./h.GetBinWidth(b)
      h.SetBinContent(b, h.GetBinContent(b)*sf)
      h.SetBinError(b,   h.GetBinError(b)*sf)
   return h

def setStyle():
   gROOT.Reset()
   icol=0;  # WHITE
   font=42; # Helvetica
   tsize=0.05;
   gStyle.SetFrameBorderMode(icol);
   gStyle.SetFrameFillColor(icol);
   gStyle.SetCanvasBorderMode(icol);
   gStyle.SetCanvasColor(icol);
   gStyle.SetPadBorderMode(icol);
   gStyle.SetPadColor(icol);
   gStyle.SetStatColor(icol);
   gStyle.SetPaperSize(20,26);
   gStyle.SetPadTopMargin(0.05);
   gStyle.SetPadRightMargin(0.08);
   gStyle.SetPadBottomMargin(0.15);
   gStyle.SetPadLeftMargin(0.12);
   gStyle.SetTitleXOffset(1.05);
   gStyle.SetTitleYOffset(0.95);
   gStyle.SetTextFont(font);
   gStyle.SetTextSize(tsize);
   gStyle.SetLabelFont(font,"x");
   gStyle.SetTitleFont(font,"x");
   gStyle.SetLabelFont(font,"y");
   gStyle.SetTitleFont(font,"y");
   gStyle.SetLabelFont(font,"z");
   gStyle.SetTitleFont(font,"z");
   gStyle.SetLabelSize(tsize*0.85,"x");
   gStyle.SetTitleSize(tsize*1.10,"x");
   gStyle.SetLabelSize(tsize*0.85,"y");
   gStyle.SetTitleSize(tsize*1.10,"y");
   gStyle.SetLabelSize(tsize*0.85,"z");
   gStyle.SetTitleSize(tsize*1.10,"z");
   gStyle.SetMarkerStyle(20);
   gStyle.SetMarkerSize(0.2);
   gStyle.SetHistLineWidth(2);
   gStyle.SetLineStyleString(2,"[12 12]"); # postscript dashes
   gStyle.SetEndErrorSize(0.);
   # gStyle.SetOptTitle(0);
   gStyle.SetOptStat(0);
   gStyle.SetOptFit(0);
   gStyle.SetPadTickX(1);
   gStyle.SetPadTickY(1);
   ROOT.TGaxis.SetMaxDigits(4)
setStyle()

####### HISTOS
listbins = [0,80,160,240,320,360,400,440,500,560,600,640,680,720,760,800,860,920,1040,1160,1280]
arrbins = array("d", listbins)
nbins = len(listbins)-1

hMEall = TGraph()
hMEbad = TGraph()
hmSM = TH1D("hmSM",";#it{m}_{#it{t}#bar{#it{t}}} [GeV];Events / 40 GeV",nbins,arrbins)
hmXX = TH1D("hmXX",";#it{m}_{#it{t}#bar{#it{t}}} [GeV];Events / 40 GeV",nbins,arrbins)

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



######## ANALYSIS
tfile = TFile(figdir+channel+filename,"READ")
ttree = tfile.Get("debug")
n = 1
b = 1
for event in ttree:
   if(n%50000==0): print "processed %s and reweighting %g" % (ttree.GetName(),n)
   # if(event.w2HDM[0]>100): continue
   if(event.w2HDM[0]>100): event.w[0] = event.w0[0]
   hmSM.Fill(event.mttReco[0],event.w0[0])
   hmXX.Fill(event.mttReco[0],event.w[0])
   hMEall.SetPoint(hMEall.GetN(),event.me2SM[0],event.me2XX[0])
   if(event.w2HDM[0]>100): hMEbad.SetPoint(hMEbad.GetN(),event.me2SM[0],event.me2XX[0])
   if(event.w2HDM[0]>100):
      ids = ""
      p4 = "p=["
      for i in xrange(event.id.size()):
         ids += str(int(event.id[i]))+" "
         p4 += "\n   [%g,%g,%g,%g]," % (event.e[i],event.px[i],event.py[i],event.pz[i])
      p4 += "\n]\n"
      print "bad event[%g], me2SM=%g, me2XX=%g, w2HDM=%g, ME size=%g --> %s\n%s" % (b,event.me2SM[0],event.me2XX[0],event.w2HDM[0],event.id.size(),ids,p4)
      b += 1
   n += 1


######## PLOT
hmSM.Scale(lumi*pb2fb)
hmXX.Scale(lumi*pb2fb)
hmSM = normalizeToBinWidth(hmSM,40)
hmXX = normalizeToBinWidth(hmXX,40)

pdfname = "figs/"+channel+filename.replace(".root",".pdf")

cnv = TCanvas("cnv","",500,500)
cnv.Draw()
cnv.cd()
cnv.SetGrid(1,1)
hmax = hmSM.GetMaximum() if(hmSM.GetMaximum()>hmXX.GetMaximum()) else hmXX.GetMaximum()
hmSM.SetMaximum(hmax*2)
hmSM.SetMinimum(0)
hmSM.Draw()
hmXX.Draw("same")
cnv.RedrawAxis()
cnv.Update()
cnv.SaveAs(pdfname)

cnv = TCanvas("cnv","",500,500)
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
cnv.RedrawAxis()
cnv.Update()
cnv.SaveAs(pdfname.replace("pdf","png"))
