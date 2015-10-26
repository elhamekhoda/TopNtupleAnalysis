#!/usr/bin/env python
import os
from ROOT import *

gROOT.Reset()

gROOT.SetStyle('Plain')
gStyle.SetPaintTextFormat('4.2f')
gStyle.SetPalette(1)
gStyle.SetTextSize(3)

doprint = ".png,.eps"

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

def MergeFiles(oname, list_dir):
	com = "hadd -f "+oname
	for Dir in list_dir:
		com += " "+Dir
	#print com	
	os.system(com)
	
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

def effRates(channels):

	channels  = []
	channels += [('resolved','e' )]
	channels += [('resolved','mu')]
	channels += [('boosted', 'e' )]
	channels += [('boosted', 'mu')]

	outfile = TFile('eff_ttbar.root','RECREATE')
	
	for ichan in channels:
				
		hadd_in=""
		hadd_in = inputDir+ichan[0]+"_"+ichan[1]+"_ttbar*root"
	
		ttbarFile = ichan[0]+"_ttbar_"+ichan[1]+".root "
		
		print "hadd -f " + ttbarFile + hadd_in
		os.system("hadd -f " + ttbarFile + hadd_in)
		
		inputfile = TFile(ttbarFile,'READ')

		#pT
		hTmp_t_pt = inputfile.Get("LepMa_pt_vs_DR").ProjectionX().Clone()
		hTmp_l_pt = inputfile.Get("LepMa_pt_vs_DR_Loose").ProjectionX().Clone()
		
		#DR
		hTmp_t_dr = inputfile.Get("LepMa_pt_vs_DR").ProjectionY().Clone()
		hTmp_l_dr = inputfile.Get("LepMa_pt_vs_DR_Loose").ProjectionY().Clone()
		
		#pT and DR	
		hTmp_t_pTdr = inputfile.Get("LepMa_pt_vs_DR").Clone()		     
		hTmp_l_pTdr = inputfile.Get("LepMa_pt_vs_DR_Loose").Clone()
		
		#eff using TH1 lepton pT
		h_ratio_pt = hTmp_t_pt
		h_ratio_pt.Divide(hTmp_t_pt, hTmp_l_pt, 1.0, 1.0, "B")
		
		c = TCanvas("c_"+ichan[0]+'_eff_pt_'+ichan[1])
                maxi = 0
		mini = 0
		h_ratio_pt.Draw("e")			               	
		maxi = h_ratio_pt.GetMaximum()
		mini = h_ratio_pt.GetMinimum()
                h_ratio_pt.SetMaximum(maxi*1.3)
		h_ratio_pt.SetMinimum(mini*0.7)
		c.SetGridy(1)
		c.Update()
                c.Modified()		
		saveCanvas(c, 'h_eff_pt_'+ichan[0]+'_'+ichan[1], outfile, 'eff_plots')
				
		#eff using TH1 minDR
		h_ratio_dr = hTmp_t_dr
		h_ratio_dr.Divide(hTmp_t_dr, hTmp_l_dr, 1.0, 1.0, "B")
		
		c1 = TCanvas("c_"+'eff_dr_'+ichan[0]+'_'+ichan[1])
                maxi = 0
		mini = 0
		h_ratio_dr.Draw("e")			               	
		maxi = h_ratio_dr.GetMaximum()
		mini = h_ratio_dr.GetMinimum()
                h_ratio_dr.SetMaximum(maxi*1.3)
		h_ratio_dr.SetMinimum(0.5)
		c.SetGridy(1)
		c1.Update()
                c1.Modified()
		saveCanvas(c1, 'h_eff_dr_'+ichan[0]+'_'+ichan[1], outfile, 'eff_plots')
		
		#eff using TH2 lepton pT and minDR
		h_ratio_pTdr = hTmp_t_pTdr
		h_ratio_pTdr.Divide(hTmp_t_pTdr, hTmp_l_pTdr, 1.0, 1.0, "B")
		
		gStyle.SetPaintTextFormat("1.3f")
		c2 = TCanvas("c_"+'eff2D_dr_'+ichan[0]+'_'+ichan[1])
		c2.cd()
		h_ratio_pTdr.Draw()
		h_ratio_pTdr.Draw("colz TEXT e1 SAME")
		h_ratio_pTdr.GetZaxis().SetRangeUser(0.7, 1.0)
		h_ratio_pTdr.SetStats(0)
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
		h_ratio_pt.Write('eff_pt_'+ichan[0]+'_'+ichan[1])
		h_ratio_dr.Write('eff_dr_'+ichan[0]+'_'+ichan[1])
		h_ratio_pTdr.Write('eff_pTdr_'+ichan[0]+'_'+ichan[1])

	return
	
	
def fakeRates(inputDir, lumi):

	merge = 1
	
	channels  = []
	channels += [('resolved','e' )]
	channels += [('resolved','mu')]
	channels += [('boosted', 'e' )]
	channels += [('boosted', 'mu')]
	
	outfile = TFile("fake.root","RECREATE")
		
	for ichan in channels:
	
		hadd_in= []		
		
		# --> Merging the bkg
		for ibkg in ["ttbar", "Wjets", "Zjets", "st"]:			
			
			if ibkg=="ttbar":				
				for File in os.popen("ls "+inputDir+ichan[0]+"_fake_"+ichan[1]+"_ttbar.root ").readlines():
					hadd_in.append(File[:-1])
			elif ibkg=="Wjets":
				for File in os.popen("ls "+inputDir+ichan[0]+"_fake_"+ichan[1]+"_W*root ").readlines():
					hadd_in.append(File[:-1])
			elif ibkg=="Zjets":
				for File in os.popen("ls "+inputDir+ichan[0]+"_fake_"+ichan[1]+"_Z*root ").readlines():
					hadd_in.append(File[:-1])
			elif ibkg=="st":
				for File in os.popen("ls "+inputDir+ichan[0]+"_fake_"+ichan[1]+"_st.root ").readlines():
					hadd_in.append(File[:-1])	


		hadd_bkgPath = ichan[0]+"_BKG_"+ichan[1]+".root"
		if merge:	MergeFiles(hadd_bkgPath, hadd_in)
		
		# --> Merging the datasets
		hadd_in=[]
		'''
		for idata in ["DTD", "DTE"]:			
			
			if idata=="DTD":
				for File in os.popen("ls "+inputDir+ichan[0]+"_fake_"+ichan[1]+"_DTD*root ").readlines():
					hadd_in.append(File[:-1])
			elif idata=="DTE":
				for File in os.popen("ls "+inputDir+ichan[0]+"_fake_"+ichan[1]+"_DTE*root ").readlines():
					hadd_in.append(File[:-1])
			
		hadd_dataPath =  ichan[0]+"_DATA_"+ichan[1]+".root"
		if merge:	MergeFiles(hadd_dataPath, hadd_in)
		'''
		
		for File in os.popen("ls "+inputDir+ichan[0]+"_fake_"+ichan[1]+"_DT*root ").readlines():
			hadd_in.append(File[:-1])
		
		hadd_dataPath =  ichan[0]+"_DATA_"+ichan[1]+".root"
		if merge:	MergeFiles(hadd_dataPath, hadd_in)
		
		# --> Check QCD at low MWT
		
		bkgFile  = TFile(hadd_bkgPath,'READ')
		dataFile = TFile(hadd_dataPath,'READ')
		
		#tight
		c_mwt_t = TCanvas("c_"+ichan[0]+'_mwt_tight_'+ichan[1])
		leg = TLegend(0.6, 0.65, 0.8, 0.88, ichan[0]+" "+ichan[1]+" channel (tight):")
                leg.SetTextSize(0.03)
                leg.SetFillColor(10)
                leg.SetBorderSize(0)
		
		h_data = dataFile.Get("mwt").Clone()
		h_data.Draw("e")
		h_data.SetMarkerStyle(20)
		h_data.SetStats(0)
		
		h_bkg = bkgFile.Get("mwt").Clone()
		h_bkg.Scale(lumi)
		h_bkg.Draw("histo SAME")
		h_bkg.SetLineColor(4) 
		h_bkg.SetLineWidth(3)
		h_bkg.SetStats(0)
		
		leg.AddEntry(h_data, "Data: "+`h_data.Integral()`[:7], "P")
		leg.AddEntry(h_bkg,  "bkg: "+`h_bkg.Integral()`[:7], "L")
		leg.Draw()
		
		if h_data.GetMaximum()>h_bkg.GetMaximum():	h_data.SetMaximum(h_data.GetMaximum()*1.3)
		else: 						h_data.SetMaximum(h_bkg.GetMaximum()*1.3)
		
		c_mwt_t.SetLogy(1)
		c_mwt_t.SetGridy(1)
		c_mwt_t.Update()
                c_mwt_t.Modified()		
		saveCanvas(c_mwt_t, 'h_'+ichan[0]+'_mwt_tight_'+ichan[1], outfile, 'fake_plots')
		
		#loose
		c_mwt_l = TCanvas("c_"+ichan[0]+'_mwt_loose_'+ichan[1])
		leg = TLegend(0.6, 0.65, 0.8, 0.88, ichan[0]+" "+ichan[1]+" channel (loose):")
                leg.SetTextSize(0.03)
                leg.SetFillColor(10)
                leg.SetBorderSize(0)
		
		h_data = dataFile.Get("mwt_Loose").Clone()
		h_data.Draw("e")
		h_data.SetMarkerStyle(20)
		h_data.SetStats(0)
		
		h_bkg = bkgFile.Get("mwt_Loose").Clone()
		h_bkg.Scale(lumi)
		h_bkg.Draw("histo SAME")
		h_bkg.SetLineColor(4) 
		h_bkg.SetLineWidth(3)
		h_bkg.SetStats(0)
		
                if h_data.GetMaximum()>h_bkg.GetMaximum():	h_data.SetMaximum(h_data.GetMaximum()*1.3)
		else: 						h_data.SetMaximum(h_bkg.GetMaximum()*1.3)
		
		leg.AddEntry(h_data, "Data: "+`h_data.Integral()`[:7], "P")
		leg.AddEntry(h_bkg,  "bkg: "+`h_bkg.Integral()`[:7], "L")
		leg.Draw()
		
		c_mwt_l.SetLogy(1)
		c_mwt_l.SetGridy(1)
		c_mwt_l.Update()
                c_mwt_l.Modified()		
		saveCanvas(c_mwt_l, 'h_'+ichan[0]+'_mwt_loose_'+ichan[1], outfile, 'fake_plots')

		# --> Fake rate
		
		h_leptPt_t 	= []
		h_leptPt_l 	= []
		h_closeJL_pt_t	= []
		h_closeJL_pt_l  = []
		h2D_fakeParam_t = []
		h2D_fakeParam_l = []
		
		for item in ["BKG","DATA"]:	
			
			if item=="BKG":		inputfile = bkgFile
			elif item=="DATA":	inputfile = dataFile
								
			#lept pT
			h_leptPt_t.append( inputfile.Get("lepPt_vs_closeJL_pt").ProjectionX().Clone() )		  	  
			h_leptPt_l.append( inputfile.Get("lepPt_vs_closeJL_pt_Loose").ProjectionX().Clone() )
			
			#pT of the closest jet to the lepton
			h_closeJL_pt_t.append( inputfile.Get("lepPt_vs_closeJL_pt").ProjectionY().Clone() )			
			h_closeJL_pt_l.append( inputfile.Get("lepPt_vs_closeJL_pt_Loose").ProjectionY().Clone() )
				
			#lept pT vs pT of the closest jet to the lepton
			h2D_fakeParam_t.append( inputfile.Get("lepPt_vs_closeJL_pt").Clone() )		      
			h2D_fakeParam_l.append( inputfile.Get("lepPt_vs_closeJL_pt_Loose").Clone() )
			
			
		# ---> 1D fake rates: 
		#lept Pt
		h1 = h_leptPt_t[1]
		h1.Add(h_leptPt_t[0].Scale(lumi),-1)
		
		h2 = h_leptPt_l[1]
		h2.Add(h_leptPt_l[0].Scale(lumi),-1)		
		
		h_ratio_leptPt = h1
		h_ratio_leptPt.Divide(h1, h2, 1.0, 1.0, "B")
		
		c = TCanvas("c_"+'fake_leptPt_'+ichan[0]+'_'+ichan[1])
                maxi = 0
		mini = 0
		h_ratio_leptPt.Draw("e")			               	
		maxi = h_ratio_leptPt.GetMaximum()
		mini = h_ratio_leptPt.GetMinimum()
                h_ratio_leptPt.SetMaximum(maxi*1.3)
		h_ratio_leptPt.SetMinimum(mini*0.7)
		c.SetGridy(1)
		c.Update()
                c.Modified()		
		saveCanvas(c, 'h_fake_leptPt_'+ichan[0]+'_'+ichan[1], outfile, 'fake_plots')
				
		#pT of the closest jet to the lepton
		
		h1 = h_closeJL_pt_t[1]		
		h1.Add(h_closeJL_pt_t[0].Scale(lumi),-1)		
		h2 = h_closeJL_pt_l[1]
		h2.Add(h_closeJL_pt_l[0].Scale(lumi),-1)			
		
		h_ratio_closeJL_pt = h1
		h_ratio_closeJL_pt.Divide(h1, h2, 1.0, 1.0, "B")	
		
		c1 = TCanvas("c_"+'fake_closeJL_pt_'+ichan[0]+'_'+ichan[1])
                maxi = 0
		mini = 0
		h_ratio_closeJL_pt.Draw("e")			               	
		maxi = h_ratio_closeJL_pt.GetMaximum()
		mini = h_ratio_closeJL_pt.GetMinimum()
                h_ratio_closeJL_pt.SetMaximum(maxi*1.3)
		h_ratio_closeJL_pt.SetMinimum(0.5)
		c1.SetGridy(1)
		c1.Update()
                c1.Modified()
		saveCanvas(c1, 'h_fake_closeJL_pt_'+ichan[0]+'_'+ichan[1], outfile, 'fake_plots')
		
		# ---> 2D fake rates

		h12D = h2D_fakeParam_t[1]
		h12D.Add(h2D_fakeParam_t[0].Scale(lumi),-1)		
		h22D = h2D_fakeParam_l[1]
		h22D.Add(h2D_fakeParam_l[0].Scale(lumi),-1) 		
		
		h_ratio_fake = h12D
		h_ratio_fake.Divide(h12D, h22D, 1.0, 1.0, "B")
		
		gStyle.SetPaintTextFormat("1.3f")
		c2 = TCanvas("c_"+'fake2D_'+ichan[0]+'_'+ichan[1])
		c2.cd()
		h_ratio_fake.Draw()
		h_ratio_fake.Draw("colz TEXT e1 SAME")
		#h_ratio_fake.GetZaxis().SetRangeUser(0.7, 1.0)
		h_ratio_fake.SetStats(0)
		gPad.RedrawAxis()	
		gStyle.SetPaintTextFormat("1.3f")               	
		c2.SetLogx(1)
		c2.SetLogy(1)
		c2.Update()
                c2.Modified()		
		saveCanvas(c2, '2Dh_fake_'+ichan[0]+'_'+ichan[1], outfile, 'fake_plots')
			
		outfile.cd()	
		h_ratio_fake.Write('2Dfake_'+ichan[0]+'_'+ichan[1])
		h_ratio_closeJL_pt.Write('fake_closeJL_pt_'+ichan[0]+'_'+ichan[1])
		h_ratio_leptPt.Write('fake_leptPt_'+ichan[0]+'_'+ichan[1])


	return
			
#--------------------------------#
#         QCD estimation         #
#--------------------------------#

#Produce eff rate plots

#inputDir = path/to/files/processed/with/TopNtupleAnalysis
inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.23c/TopNtupleAnalysis/effSave/'

if 0:
	effRates(inputDir)

#Produce fake rate plots

#new
inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.30/TopNtupleAnalysis/25ns_fake/' 
lumi = 1037.23 #pb-1

#old
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.30/TopNtupleAnalysis/save_523/25ns_fake/4j1bj/' 
#lumi = 523.3 #pb-1

if 1:	
	fakeRates(inputDir, lumi)

















