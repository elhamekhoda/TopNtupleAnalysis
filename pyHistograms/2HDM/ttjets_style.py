#!/usr/bin/env python
import ROOT
from ROOT import *
import math

def setStyle():
   gROOT.Reset()
   icol=0  # WHITE
   font=42 # Helvetica
   tsize=0.05
   gStyle.SetFrameBorderMode(icol)
   gStyle.SetFrameFillColor(icol)
   gStyle.SetCanvasBorderMode(icol)
   gStyle.SetCanvasColor(icol)
   gStyle.SetPadBorderMode(icol)
   gStyle.SetPadColor(icol)
   gStyle.SetStatColor(icol)
   gStyle.SetPaperSize(20,26)
   gStyle.SetPadTopMargin(0.05)
   gStyle.SetPadRightMargin(0.08)
   gStyle.SetPadBottomMargin(0.15)
   gStyle.SetPadLeftMargin(0.12)
   gStyle.SetTitleXOffset(1.05)
   gStyle.SetTitleYOffset(0.95)
   gStyle.SetTextFont(font)
   gStyle.SetTextSize(tsize)
   gStyle.SetLabelFont(font,"x")
   gStyle.SetTitleFont(font,"x")
   gStyle.SetLabelFont(font,"y")
   gStyle.SetTitleFont(font,"y")
   gStyle.SetLabelFont(font,"z")
   gStyle.SetTitleFont(font,"z")
   gStyle.SetLabelSize(tsize*0.85,"x")
   gStyle.SetTitleSize(tsize*1.10,"x")
   gStyle.SetLabelSize(tsize*0.85,"y")
   gStyle.SetTitleSize(tsize*1.10,"y")
   gStyle.SetLabelSize(tsize*0.85,"z")
   gStyle.SetTitleSize(tsize*1.10,"z")
   gStyle.SetMarkerStyle(20)
   gStyle.SetMarkerSize(0.8)
   gStyle.SetHistLineWidth(2)
   gStyle.SetLineStyleString(2,"[12 12]") # postscript dashes
   gStyle.SetEndErrorSize(0.)
   # gStyle.SetOptTitle(0)
   gStyle.SetOptStat(0)
   gStyle.SetOptFit(0)
   gStyle.SetPadTickX(1)
   gStyle.SetPadTickY(1)
   ROOT.TGaxis.SetMaxDigits(4)

###############
setStyle() ####
###############

def divide(hNumerator,hDenominator):
   if(hNumerator.GetNbinsX()!=hDenominator.GetNbinsX()):
      print "Number of bins do not match - quitting"
      quit()
   for b in xrange(hNumerator.GetNbinsX()+1):
      N = hNumerator.GetBinContent(b)
      dN = hNumerator.GetBinError(b)
      D = hDenominator.GetBinContent(b)
      dD = hDenominator.GetBinError(b)
      hDivision = hNumerator.Clone(hNumerator.GetName()+"_division")
      hDivision.Reset()
      y = N/D if(D!=0) else 0
      dy = y*math.sqrt((dN/N)*(dN/N)+(dD/D)*(dD/D)) if(D!=0 and N!=0) else 0
      hDivision.SetBinContent(b,y)
      hDivision.SetBinError(b,dy)
      hDivision.SetDirectory(0)
      return hDivision

'''
def divide(hN,hD):
   for b in xrange(hN.GetNbinsX()+1):
      yN = hN.GetBinContent(b)
      yD = hD.GetBinContent(b)
      y = yN/yD if(yD!=0) else 0
      dyN = hN.GetBinError(b)
      dyD = hD.GetBinError(b)
      dy = y*math.sqrt( (dyN/yN)**2 + (dyD/yD)**2 ) if(yD!=0 and yN!=0) else 0
      hN.SetBinContent(b,y)
      hN.SetBinError(b,dy)
   return hN
'''

