#!/usr/bin/env python
import os
from ROOT import *

gROOT.Reset()

gROOT.SetStyle('Plain')
gStyle.SetPaintTextFormat('4.2f')
gStyle.SetPalette(1)
gStyle.SetTextSize(3)

doprint = ".pdf"

def saveCanvas(canvas, name, File, OUTDIR):
        File.cd()
        a = 1;
        canvas.SetCanvasSize(int(700*a),int(500*a));
        canvas.SetWindowSize(int(700*a),int(500*a));
        canvas.Update();
        canvas.Write(name)
        os.system("mkdir -p "+OUTDIR)
        if doprint!="": 
                for ext in doprint.split(","):
                        canvas.Print(OUTDIR+"/"+name+ext)

	return
	
def DoPlots(sample):
		
	print sample[2]+sample[0]+'_'+sample[1]+'_ttbar.root'
	inputFile = TFile(sample[2]+sample[0]+'_'+sample[1]+'_ttbar.root','READ') 
	outfile = TFile(sample[2]+'QCDestimate_'+sample[0]+'_'+sample[1]+'_ttbar.root','RECREATE')
		
	listVar =  []
	listVar += ['MC_'+sample[1]+'_pt', 'MC_'+sample[1]+'_eta', 'MC_'+sample[1]+'_phi', 'MC_'+sample[1]+'_m'] 
	listVar += ['lepMa_pt', 'lepMa_eta', 'lepMa_phi', 'lepMa_m', 'lepMa_pdgId'] 
	listVar += ['MC'+sample[1]+'_pt_vs_eta', 'LepMa_pt_vs_DR', 'Ma_pt_vs_eta']
	listVar += ['lepMadR_pt', 'minDeltaR_jet_lept']
	
	for quality in ['','_Loose']:
	
		for i in range(len(listVar)):
		
                	print listVar[i]+quality
			maxi = 0
                	c = TCanvas("c_"+listVar[i]+quality, "c_"+listVar[i])                	
			histo = inputFile.Get(listVar[i]+quality) 			
			if listVar[i].find("_vs_")!=-1:
				histo.Draw("colz")
			else:
				histo.Draw("histo")			               	
				maxi = histo.GetMaximum()
                        	histo.SetMaximum(maxi*1.3)
			c.Update()
                	c.Modified()                	
			histo.Write(listVar[i]+quality)		
			saveCanvas(c, 'h_'+sample[0]+'_'+sample[1]+'_'+listVar[i]+quality, outfile, 'plots')
                	
	outfile.Close()
	return

def Rebin_2D(h1, ngx, ngy):

	nbinsx = h1.GetXaxis().GetNbins()
	nbinsy = h1.GetYaxis().GetNbins()
	xmin   = h1.GetXaxis().GetXmin()
	xmax   = h1.GetXaxis().GetXmax()
	ymin   = h1.GetYaxis().GetXmin()
	ymax   = h1.GetYaxis().GetXmax()
	nx = nbinsx/ngx;
	ny = nbinsy/ngy;
	print nx,xmin,xmax,ny,ymin,ymax
	h1.SetBins(nx,xmin,xmax,ny,ymin,ymax)
	
	#loop on all bins to reset contents and errors
	for biny in range(nbinsy):
		for binx in range(nbinsx):
			ibin = h1.GetBin(binx,biny)
			h1.SetBinContent(ibin,0)
	
	#loop on all bins and refill
	for biny in range(nbinsy):
		by  = h1.GetYaxis().GetBinCenter(biny)
		iy  = h1.GetYaxis().FindBin(by)
		for binx in range(nbinsx):
			bx = h1.GetXaxis().GetBinCenter(binx)
			ix  = h1.GetXaxis().FindBin(bx)
			bin = h1.GetBin(binx,biny)
			ibin= h1.GetBin(ix,iy)
			cu  = h1.GetBinContent(bin)
			h1.AddBinContent(ibin,cu)

	return h1

def efficiency(channels):

	inputfile   = []
	
	h_tight_pt = []
	h_loose_pt = []
	h_ratio_pt = []
	
	h_tight_dr = []
	h_loose_dr = []
	h_ratio_dr = []
	
	h_tight_pTdr = []
	h_loose_pTdr = []
	h_ratio_pTdr = []
	
	outfile = TFile('eff_ttbar.root','RECREATE')
	
	i = 0
	for ichan in channels:
		print ichan[2]+ichan[0]+'_'+ichan[1]+'_ttbar.root'
		
		if ichan[0].find("resolved")!=-1:
			pT_bins = [25, 35, 45, 55, 75, 95, 115, 165, 215, 275]	
			DR_bins = [0., 0.1, 0.2, 0.3, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 5]
	
		if ichan[0].find("boosted")!=-1:
			pT_bins = [25, 35, 45, 55, 75, 95, 115, 165, 215, 275, 325, 500]
			DR_bins = [0., 0.1, 0.2, 0.3, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2]
		
		
		inputfile.append(TFile(ichan[2]+ichan[0]+'_'+ichan[1]+'_ttbar.root','READ'))

		#pT
		hTmp_t_pt = inputfile[i].Get("LepMa_pt_vs_DR").ProjectionX().Clone()
		hTmp_l_pt = inputfile[i].Get("LepMa_pt_vs_DR_Loose").ProjectionX().Clone()
		#hTmp_l_pt.Add(inputfile[i].Get("LepMa_pt_vs_DR_Loose").ProjectionX().Clone())
		
		#DR
		hTmp_t_dr = inputfile[i].Get("LepMa_pt_vs_DR").ProjectionY().Clone()
		hTmp_l_dr = inputfile[i].Get("LepMa_pt_vs_DR_Loose").ProjectionY().Clone()
		#hTmp_l_dr.Add(inputfile[i].Get("LepMa_pt_vs_DR").ProjectionY().Clone())
		
		#pT and DR	
		hTmp_t_pTdr = inputfile[i].Get("LepMa_pt_vs_DR").Clone()
		#hTmp_t_pTdr = Rebin_2D(hTmp_t_pTdr, len(pT_bins)-1, len(DR_bins)-1)
		
		hTmp_l_pTdr = inputfile[i].Get("LepMa_pt_vs_DR_Loose").Clone()
		#hTmp_l_pTdr.Add(inputfile[i].Get("LepMa_pt_vs_DR").Clone())
		#hTmp_l_pTdr = Rebin_2D(hTmp_l_pTdr, len(pT_bins)-1, len(DR_bins)-1)
		
		#eff using TH1 lepton pT
		h_ratio_pt.append(hTmp_t_pt)				
		h_ratio_pt[i].Divide(hTmp_t_pt, hTmp_l_pt, 1.0, 1.0, "B")
		
		c = TCanvas("c_"+'eff_pt_'+ichan[0]+'_'+ichan[1])
                maxi = 0
		mini = 0
		h_ratio_pt[i].Draw("e")			               	
		maxi = h_ratio_pt[i].GetMaximum()
		mini = h_ratio_pt[i].GetMinimum()
                h_ratio_pt[i].SetMaximum(maxi*1.3)
		h_ratio_pt[i].SetMinimum(mini*0.7)
		c.SetGridy(1)
		c.Update()
                c.Modified()		
		saveCanvas(c, 'h_eff_pt_'+ichan[0]+'_'+ichan[1], outfile, 'eff_plots')
				
		#eff using TH1 minDR
		h_ratio_dr.append(hTmp_t_dr)
		h_ratio_dr[i].Divide(hTmp_t_dr, hTmp_l_dr, 1.0, 1.0, "B")
		
		c1 = TCanvas("c_"+'eff_dr_'+ichan[0]+'_'+ichan[1])
                maxi = 0
		mini = 0
		h_ratio_dr[i].Draw("e")			               	
		maxi = h_ratio_dr[i].GetMaximum()
		mini = h_ratio_dr[i].GetMinimum()
                h_ratio_dr[i].SetMaximum(maxi*1.3)
		h_ratio_dr[i].SetMinimum(0.5)
		c.SetGridy(1)
		c1.Update()
                c1.Modified()
		saveCanvas(c1, 'h_eff_dr_'+ichan[0]+'_'+ichan[1], outfile, 'eff_plots')
		
		#eff using TH2 lepton pT and minDR
		h_ratio_pTdr.append(hTmp_t_pTdr)
		h_ratio_pTdr[i].Divide(hTmp_t_pTdr, hTmp_l_pTdr, 1.0, 1.0, "B")
		
		gStyle.SetPaintTextFormat("1.3f")
		c2 = TCanvas("c_"+'eff2D_dr_'+ichan[0]+'_'+ichan[1])
		c2.cd()
		h_ratio_pTdr[i].Draw()
		h_ratio_pTdr[i].Draw("colz TEXT e1 SAME")
		h_ratio_pTdr[i].GetZaxis().SetRangeUser(0.7, 1.0)
		h_ratio_pTdr[i].SetStats(0)
		#h_ratio_pTdr[i].GetYaxis().SetMoreLogLabels(1)	
		#h_ratio_pTdr[i].GetXaxis().SetMoreLogLabels(1)	
		gPad.RedrawAxis()	
		gStyle.SetPaintTextFormat("1.3f")               	
		c2.SetLogx(1)
		c2.SetLogy(1)
		c2.SetGridy(1)
		c2.Update()
                c2.Modified()		
		saveCanvas(c2, '2Dh_eff_dr_'+ichan[0]+'_'+ichan[1], outfile, 'eff_plots')
			
		outfile.cd()	
		h_ratio_pt[i].Write('eff_pt_'+ichan[0]+'_'+ichan[1])
		h_ratio_dr[i].Write('eff_dr_'+ichan[0]+'_'+ichan[1])
		h_ratio_pTdr[i].Write('eff_pTdr_'+ichan[0]+'_'+ichan[1])
		i +=1
		
	return

inputDir = ''
samplesPath = []

samplesPath += [('resolved','e',  inputDir)]
samplesPath += [('resolved','mu', inputDir)]
samplesPath += [('boosted', 'e',  inputDir)]
samplesPath += [('boosted', 'mu', inputDir)]


if 0:	
	for iSample in samplesPath:
		DoPlots(iSample)


if 1:
	efficiency(samplesPath)







