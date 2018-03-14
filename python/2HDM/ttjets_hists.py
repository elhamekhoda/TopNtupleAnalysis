#!/usr/bin/env python
import os
import sys
import ROOT
from ROOT import *
from array import *
import ttjets_style

nameX    = ["A","H"]
mX       = [500,800]
tanbX    = [0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.2,1.4,1.6,1.8,2.0]
sba      = 1
typeX    = 2
channels = ["re","rmu"]
htypes   = ["mtt8TeVr"] # ["mtt8TeVr","trueMtt8TeVr","trueMttr","mttr"]

ROOT.gROOT.SetBatch(1)
ROOT.gErrorIgnoreLevel = ROOT.kWarning

################# FUNCTIONS #################
def getminmax(h):
   Min = +1.e10
   Max = -1.e10
   for b in xrange(1,h.GetNbinsX()+1):
      y = h.GetBinContent(b)
      if(y==0): continue
      Min = y if(y<Min) else Min
      Max = y if(y>Max) else Max
   return (Min,Max)

def BinsFromArray(arr):
   N = len(arr)
   arrx = []
   for i in xrange(N):
      if(i==N-1):
         pN = arr[N-1]+(arr[N-1]-arr[N-2])/2.
         arrx.append(pN)
      elif(i==0):
         p0 = arr[0]-(arr[1]-arr[0])/2.
         arrx.append(p0)
         p1 = arr[0]+(arr[1]-arr[0])/2.
         arrx.append(p1)
      else:
         pi = arr[i]+(arr[i+1]-arr[i])/2.
         arrx.append(pi)
   bins = array('d',arrx)
   return bins

def BinsFromHisto(h,cut=-1,axis="X"):
   taxis = h.GetXaxis() if(axis=="X") else h.GetYaxis()
   arrx = []
   for b in xrange(1,taxis.GetNbins()+1):
      if(cut>0 and taxis.GetBinCenter(b)>cut): break
      xmin = taxis.GetBinLowEdge(b)
      xmax = taxis.GetBinUpEdge(b)
      if(xmin not in arrx): arrx.append(xmin)
      if(xmax not in arrx): arrx.append(xmax)
   bins = array('d',arrx)
   return bins

def MakeTemplate(htype,channel,nameX,mX,histos,cut=-1):
   h2name = htype+"."+channel+".s"+nameX+"_m"+str(mX)+"_sba10_t2"
   h1name = htype+"."+channel+".s"+nameX+"_m"+str(mX)+"_sba10_tanb*_t2"
   stanb0 = ('%.1f' % tanbX[0]).replace(".","")
   binsx = BinsFromHisto(histos[h1name.replace("*",stanb0)],cut)
   binsy = BinsFromArray(tanbX)
   xtitle = histos[h1name.replace("*",stanb0)].GetXaxis().GetTitle()
   ytitle = "tan#beta"
   ztitle = histos[h1name.replace("*",stanb0)].GetYaxis().GetTitle()
   title  = "Channel="+channel+", Scalar="+nameX+", m_{"+nameX+"}="+str(mX)+", sin(#beta-#alpha)=1, Type 2"
   htitle = title+";"+xtitle+";"+ytitle+";"+ztitle
   h2 = TH2D(h2name,htitle,len(binsx)-1,binsx,len(binsy)-1,binsy)
   for tanb in tanbX:
      stanb = ('%.1f' % tanb).replace(".","")
      h1nametmp = h1name.replace("*",stanb)
      by = h2.GetYaxis().FindBin(tanb)
      for bx in range(1,histos[h1nametmp].GetNbinsX()+1):
         if(cut>0 and histos[h1nametmp].GetBinCenter(bx)>cut): break
         z = histos[h1nametmp].GetBinContent(bx)
         # if(val<0): print "mtt="+str(histos[h1nametmp].GetBinCenter(x))+", tan(beta)="+stanb+" --> A+I="+str(val)
         h2.SetBinContent(bx,by,z)
   return h2

def Plot2D(h,fname,drawopt,htype,channel,nameX,mX,minz=+1.e11,maxz=-1.e11,phi=-35,theta=15):
   c = TCanvas("c"+h.GetName(),"c"+h.GetName(),1000,600)
   c.cd()
   c.Draw()
   c.SetTopMargin(0.1)
   if(minz<+1.e10): h.SetMinimum(minz)
   if(maxz>-1.e10): h.SetMaximum(maxz)
   h.SetTitleOffset(0.5)
   if(("SURF" in drawopt) or ("LEGO" in drawopt)):
      c.SetPhi(phi)
      c.SetTheta(theta)
      h.GetZaxis().SetTitleOffset(1.10)
      h.GetXaxis().SetTitleOffset(1.60)
      h.GetYaxis().SetTitleOffset(1.30)
   h.Draw(drawopt)
   c.Modified()
   c.Update()
   c.SaveAs(fname)
   c.SaveAs("figs/"+h.GetName()+".root")



def Plot1D(fname,htype,channel,nameX,mX):
   h1name = htype+"."+channel+".s"+nameX+"_m"+str(mX)+"_sba10_tanb*_t2"
   c = TCanvas("c"+h.GetName(),"c"+h.GetName(),1200,1200)
   c.Divide(3,4)
   ymin = -1
   ymax = -1
   lines = []
   for i in xrange(len(tanbX)):
      stanb = ('%.1f' % tanbX[i]).replace(".","")
      h1nametmp = h1name.replace("*",stanb)
      title  = "Channel="+channel+", Scalar="+nameX+", m_{"+nameX+"}="+str(mX)+", sin(#beta-#alpha)=1, Type 2, tan#beta="+('%.1f' % tanbX[i])
      p = c.cd(i+1)
      p.SetGridx()
      p.SetGridy()
      if(i==0): ymin,ymax = getminmax(histos[h1nametmp])
      histos[h1nametmp].SetMaximum(1.2*ymax)
      histos[h1nametmp].SetMinimum(1.2*ymin)
      histos[h1nametmp].SetTitle(title)
      histos[h1nametmp].Draw()
      lines.append(TLine(histos[h1nametmp].GetXaxis().GetXmin(),0,histos[h1nametmp].GetXaxis().GetXmax(),0))
      lines[i].SetLineColor(ROOT.kRed)
      lines[i].Draw("same")
      histos[h1nametmp].Draw("same")
      p.Update()
      p.RedrawAxis()
   c.Modified()
   c.Update()
   c.SaveAs(fname)
   c.SaveAs("figs/"+h.GetName()+".root")



### get all 1D histos
histos = {}
for S in nameX:
   for m in mX:
      for tanb in tanbX:
         stanb = ('%.1f' % tanb).replace(".","")
         rootname = "figs/histosr.s"+S+"_m"+str(m)+"_sba10_tanb"+stanb+"_t2.reldev.root"
         tfile = TFile(rootname,"read")
         for channel in channels:
            for htype in htypes:
               # print "getting %s from file %s" % (htype+channel,rootname)
               h = tfile.Get(htype+channel)
               h.SetDirectory(0)
               hname = htype+"."+channel+".s"+S+"_m"+str(m)+"_sba10_tanb"+stanb+"_t2"
               histos.update({hname:h})
               h.SetName(hname)


### draw the templates
foutname1 = "figs/templates1d.pdf"
foutname2 = "figs/templates2d.pdf"
c = TCanvas("c","c",600,600)
c.SaveAs(foutname1+"(")
c.SaveAs(foutname2+"(")
for channel in channels:
   for S in nameX:
      for m in mX:
         for htype in htypes:
            cut = 1280 if("8TeV" not in htype) else -1
            h2 = MakeTemplate(htype,channel,S,m,histos,cut)
            Plot2D(h2,foutname2,"SURF3",htype,channel,S,m)
            Plot1D(foutname1,htype,channel,S,m)
c.SaveAs(foutname1+")")
c.SaveAs(foutname2+")")
