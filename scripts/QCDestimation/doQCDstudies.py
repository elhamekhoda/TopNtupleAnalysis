#!/usr/bin/env python
import os, sys
from ROOT import *

gROOT.Reset()

gROOT.SetStyle('Plain')
gStyle.SetPaintTextFormat('4.2f')
gStyle.SetPalette(1)
gStyle.SetTextSize(3)

doprint = ".png,.eps,.pdf"

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
		hTmp_t_pt = inputfile.Get("eff_LepPt_DR").ProjectionX().Clone()
		hTmp_l_pt = inputfile.Get("eff_LepPt_DR_Loose").ProjectionX().Clone()
		
		#DR
		hTmp_t_dr = inputfile.Get("eff_LepPt_DR").ProjectionY().Clone()
		hTmp_l_dr = inputfile.Get("eff_LepPt_DR_Loose").ProjectionY().Clone()
		
		#pT and DR	
		hTmp_t_pTdr = inputfile.Get("eff_LepPt_DR").Clone()		     
		hTmp_l_pTdr = inputfile.Get("eff_LepPt_DR_Loose").Clone()
		
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
		
		h_ratio_pTdr.GetZaxis().SetRangeUser(0.5, 1.0)
		
		h_ratio_pTdr.GetYaxis().SetRangeUser(0., 5.0)
		h_ratio_pTdr.SetStats(0)
		#h_ratio_pTdr[i].GetYaxis().SetMoreLogLabels(1)	
		#h_ratio_pTdr[i].GetXaxis().SetMoreLogLabels(1)	
		gPad.RedrawAxis()	
		gStyle.SetPaintTextFormat("1.3f")               	
		c2.SetLogx(1)
		#c2.SetLogy(1)
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
	extraPlots = 1
	
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
		#print "ls "+inputDir+ichan[0]+"_fake_"+ichan[1]+"_DT*root "
		
		for File in os.popen("ls "+inputDir+ichan[0]+"_fake_"+ichan[1]+"_DT*root ").readlines():
			hadd_in.append(File[:-1])
		
		hadd_dataPath =  ichan[0]+"_DATA_"+ichan[1]+".root"
		if merge:	MergeFiles(hadd_dataPath, hadd_in)
		
		# --> Check QCD at low MWT
		
		bkgFile  = TFile(hadd_bkgPath,'READ')
		dataFile = TFile(hadd_dataPath,'READ')
		
		for var in ['mwt','lepPt','minDeltaR','closJetPt','MET', 'z0sin', 'd0sig', 'jvt_lowLepPt', 'jvt_highLepPt']:
		
			#tight
			c_t = TCanvas("c_"+ichan[0]+'_'+var+'_tight_'+ichan[1])
			leg = TLegend(0.6, 0.6, 0.8, 0.88, ichan[0]+" "+ichan[1]+" channel (tight):")
                	leg.SetTextSize(0.028)
                	leg.SetFillColor(10)
                	leg.SetBorderSize(0)
		
			h_data = dataFile.Get("fake_"+var).Clone()
			h_data.Draw("e")
			h_data.SetMarkerStyle(20)
			h_data.SetStats(0)
			if (ichan[0]=='boosted'):	
				#h_data.Rebin(2)
				if (var=='lepPt' or var=='closJetPt'):	h_data.Rebin(4)
			leg.AddEntry(h_data, "Data: "+`h_data.Integral()`[:7], "P")
			print ichan, "tight:"
			print 'data &' , `h_data.Integral()`[:7], '\\\ \\hline'
			
			pallete   = [2, 3, 3, 3, 6, 6, 6, 7]
			styleLine = [1, 1 ,2, 3, 1, 2, 3, 1]
			h_ibkg = []
			i=0
			
			for ibkg in ["ttbar", "Wev", "Wmv", "Wtv", "Zee", "Zmm", "Ztt", "st"]:
				
				#print inputDir+ichan[0]+"_fake_"+ichan[1]+"_"+ibkg+".root"
				tmp_bkgFile  = TFile(inputDir+ichan[0]+"_fake_"+ichan[1]+"_"+ibkg+".root",'READ')
				h_ibkg.append(tmp_bkgFile.Get("fake_"+var).Clone())
				h_ibkg[i].SetDirectory(0)
				h_ibkg[i].Scale(lumi)
				if h_ibkg[i].Integral()>0:	
					if h_ibkg[i].Integral()>0.0001: #for better visualization
						print ibkg, '&' , `h_ibkg[i].Integral()`[:7], '\\\ \\hline'	
						h_ibkg[i].Draw("histo SAME")
						if (ichan[0]=='boosted'):
							#h_ibkg[i].Rebin()	
							if (var=='lepPt' or var=='closJetPt'):	h_ibkg[i].Rebin(4)
						h_ibkg[i].SetStats(0)
					h_ibkg[i].SetLineColor(pallete[i]) 
					h_ibkg[i].SetLineStyle(styleLine[i])
					h_ibkg[i].SetLineWidth(3)					
					#print h_ibkg[i].Integral(), i
					leg.AddEntry(h_ibkg[i],  ibkg+": "+`h_ibkg[i].Integral()`[:7], "L")
				i += 1
			
			h_bkg = bkgFile.Get("fake_"+var).Clone()
			h_bkg.Scale(lumi)
			h_bkg.Draw("histo SAME")
			h_bkg.SetLineColor(4) 
			h_bkg.SetLineWidth(3)
			h_bkg.SetStats(0)
			if (ichan[0]=='boosted'):
				#h_bkg.Rebin(2)	
				if (var=='lepPt' or var=='closJetPt'):	h_bkg.Rebin(4)
			
			leg.AddEntry(h_bkg,  "total bkg: "+`h_bkg.Integral()`[:7], "L")
			leg.Draw()
			print 'total bkg &' , `h_bkg.Integral()`[:7], '\\\ \\hline'
			
			
			if h_data.GetMaximum()>h_bkg.GetMaximum():	h_data.SetMaximum(h_data.GetMaximum()*1.3)
			else: 						h_data.SetMaximum(h_bkg.GetMaximum()*1.3)
		
			c_t.SetLogy(1)
			#if var=='lepPt':	c_t.SetLogx(1)
			c_t.SetGridy(1)
			c_t.Update()
                	c_t.Modified()  	    
			saveCanvas(c_t, 'h_'+ichan[0]+'_'+var+'_tight_'+ichan[1], outfile, 'fake_plots')
			
			#loose
			c_l = TCanvas("c_"+ichan[0]+'_'+var+'_loose_'+ichan[1])
			leg = TLegend(0.6, 0.6, 0.8, 0.88, ichan[0]+" "+ichan[1]+" channel (loose):")
                	leg.SetTextSize(0.028)
	                leg.SetFillColor(10)
        	        leg.SetBorderSize(0)
		
			h_data = dataFile.Get('fake_'+var+'_Loose').Clone()
			h_data.Draw("e")
			h_data.SetMarkerStyle(20)
			h_data.SetStats(0)
			if (ichan[0]=='boosted'):
				#h_data.Rebin(2)	
				if (var=='lepPt' or var=='closJetPt'):	h_data.Rebin(4)
			leg.AddEntry(h_data, "Data: "+`h_data.Integral()`[:7], "P")
			print ichan, "Loose:"
			print 'data &' , `h_data.Integral()`[:7], '\\\ \\hline'
			
			pallete   = [2, 3, 3, 3, 6, 6, 6, 7]
			styleLine = [1, 1 ,2, 3, 1, 2, 3, 1]
			h_ibkg = []
			i=0
			for ibkg in ["ttbar", "Wev", "Wmv", "Wtv", "Zee", "Zmm", "Ztt", "st"]:
				
				#print inputDir+ichan[0]+"_fake_"+ichan[1]+"_"+ibkg+".root"
				tmp_bkgFile  = TFile(inputDir+ichan[0]+"_fake_"+ichan[1]+"_"+ibkg+".root",'READ')
				h_ibkg.append(tmp_bkgFile.Get("fake_"+var+'_Loose').Clone())
				h_ibkg[i].SetDirectory(0)
				h_ibkg[i].Scale(lumi)
				if h_ibkg[i].Integral()>0:	
					if h_ibkg[i].Integral()>0.0001:	
						h_ibkg[i].Draw("histo SAME")
						print ibkg, '&' , `h_ibkg[i].Integral()`[:7], '\\\ \\hline'
						if (ichan[0]=='boosted'):
							#h_ibkg[i].Rebin()	
							if (var=='lepPt' or var=='closJetPt'):	h_ibkg[i].Rebin(4)
						h_ibkg[i].SetStats(0)
					h_ibkg[i].SetLineColor(pallete[i]) 
					h_ibkg[i].SetLineStyle(styleLine[i])
					h_ibkg[i].SetLineWidth(3)					
					#print h_ibkg[i].Integral(), i
					leg.AddEntry(h_ibkg[i],  ibkg+": "+`h_ibkg[i].Integral()`[:7], "L")
				tmp_bkgFile.Close()	
				i += 1
			
			
			
			h_bkg = bkgFile.Get('fake_'+var+'_Loose').Clone()
			h_bkg.Scale(lumi)
			h_bkg.Draw("histo SAME")
			h_bkg.SetLineColor(4) 
			h_bkg.SetLineWidth(3)
			h_bkg.SetStats(0)		
			if (ichan[0]=='boosted'):	
				#h_bkg.Rebin(2)
				if (var=='lepPt' or var=='closJetPt'):	h_bkg.Rebin(4)
		
                	if h_data.GetMaximum()>h_bkg.GetMaximum():	h_data.SetMaximum(h_data.GetMaximum()*1.3)
			else: 						h_data.SetMaximum(h_bkg.GetMaximum()*1.3)
		
			
			leg.AddEntry(h_bkg,  "bkg: "+`h_bkg.Integral()`[:7], "L")
			leg.Draw()
			print 'total bkg &' , `h_bkg.Integral()`[:7], '\\\ \\hline'
			c_l.SetLogy(1)
			#if var=='lepPt':	c_l.SetLogx(1)
			c_l.SetGridy(1)
			c_l.Update()
        	        c_l.Modified()  	    
			saveCanvas(c_l, 'h_'+ichan[0]+'_'+var+'_loose_'+ichan[1], outfile, 'fake_plots')
			
			
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
			h_leptPt_t.append( inputfile.Get("fake_lepPt_jetPt").ProjectionX().Clone() )		  	  
			h_leptPt_l.append( inputfile.Get("fake_lepPt_jetPt_Loose").ProjectionX().Clone() )
			
			#pT of the closest jet to the lepton
			h_closeJL_pt_t.append( inputfile.Get("fake_lepPt_jetPt").ProjectionY().Clone() )			
			h_closeJL_pt_l.append( inputfile.Get("fake_lepPt_jetPt_Loose").ProjectionY().Clone() )
				
			#lept pT vs pT of the closest jet to the lepton
			h2D_fakeParam_t.append( inputfile.Get("fake_lepPt_jetPt").Clone() )		      
			h2D_fakeParam_l.append( inputfile.Get("fake_lepPt_jetPt_Loose").Clone() )
			
			
		# ---> 1D fake rates: 
		#lept Pt
		
		h_leptPt_t[0].Scale(lumi)
		h1 = h_leptPt_t[1]
		h1.Add(h_leptPt_t[0],-1)
		if extraPlots:	h1.Write("hP_leptPt_tight_"+ichan[0]+'_'+ichan[1])
		
		h_leptPt_l[0].Scale(lumi)
		h2 = h_leptPt_l[1]
		h2.Add(h_leptPt_l[0],-1)		
		if extraPlots:	h2.Write("hP_leptPt_loose_"+ichan[0]+'_'+ichan[1])
		
		h_ratio_leptPt = h1
		h_ratio_leptPt.Divide(h1, h2, 1.0, 1.0, "B")
		
		c = TCanvas("c_"+'fake_leptPt_'+ichan[0]+'_'+ichan[1])
                maxi = 0
		mini = 0
		h_ratio_leptPt.Draw("e")			               	
		#maxi = h_ratio_leptPt.GetMaximum()
		#mini = h_ratio_leptPt.GetMinimum()
                #h_ratio_leptPt.SetMaximum(maxi*1.3)
		#h_ratio_leptPt.SetMinimum(mini*0.7)
		h_ratio_leptPt.SetStats(0)		
		c.SetGridy(1)
		c.Update()
                c.Modified()		
		if extraPlots:	saveCanvas(c, 'h_fake_leptPt_'+ichan[0]+'_'+ichan[1], outfile, 'fake_plots')

		#pT of the closest jet to the lepton
		
		h_closeJL_pt_t[0].Scale(lumi)
		h1 = h_closeJL_pt_t[1]		
		h1.Add(h_closeJL_pt_t[0],-1)
		if extraPlots:	h1.Write("hP_closeJL_pt_tight_"+ichan[0]+'_'+ichan[1])
		
		h_closeJL_pt_l[0].Scale(lumi)						
		h2 = h_closeJL_pt_l[1]
		h2.Add(h_closeJL_pt_l[0],-1)			
		if extraPlots:	h2.Write("hP_closeJL_pt_loose_"+ichan[0]+'_'+ichan[1])
		
		h_ratio_closeJL_pt = h1
		h_ratio_closeJL_pt.Divide(h1, h2, 1.0, 1.0, "B")	
		
		c1 = TCanvas("c_"+'fake_closeJL_pt_'+ichan[0]+'_'+ichan[1])
                maxi = 0
		mini = 0
		h_ratio_closeJL_pt.Draw("e")			               	
		#maxi = h_ratio_closeJL_pt.GetMaximum()
		#mini = h_ratio_closeJL_pt.GetMinimum()
                #h_ratio_closeJL_pt.SetMaximum(maxi*1.3)
		#h_ratio_closeJL_pt.SetMinimum(0.5)
		#h_ratio_closeJL_pt.SetStats(0)
		c1.SetGridy(1)
		c1.Update()
                c1.Modified()
		if extraPlots:	saveCanvas(c1, 'h_fake_closeJL_pt_'+ichan[0]+'_'+ichan[1], outfile, 'fake_plots')
		
		# ---> 2D fake rates

		h2D_fakeParam_t[0].Scale(lumi)
		h1_2D = h2D_fakeParam_t[1]
		h1_2D.Add(h2D_fakeParam_t[0],-1)	
		if extraPlots:	h1_2D.Write("hP_fakeParam_tight_"+ichan[0]+'_'+ichan[1])
		
		h2D_fakeParam_l[0].Scale(lumi)		
		h2_2D = h2D_fakeParam_l[1]
		h2_2D.Add(h2D_fakeParam_l[0],-1) 
		if extraPlots:	h2_2D.Write("hP_fakeParam_loose_"+ichan[0]+'_'+ichan[1])
		
		h_ratio_fake = h1_2D.Clone()
		h_ratio_fake.Divide(h1_2D, h2_2D, 1.0, 1.0, "B")
		
		gStyle.SetPaintTextFormat("1.2f")
		c2 = TCanvas("c_"+'fake2D_'+ichan[0]+'_'+ichan[1])
		c2.cd()
		h_ratio_fake.Draw()
		h_ratio_fake.Draw("colz TEXT e1 SAME")
		#h_ratio_fake.GetZaxis().SetRangeUser(0.4, 1.0)
		h_ratio_fake.SetStats(0)
		gPad.RedrawAxis()	
		#gStyle.SetPaintTextsize(0.04)               	
		c2.SetLogx(1)
		c2.SetLogy(1)
		c2.Update()
                c2.Modified()	
		
		l = TLatex()
		l.SetNDC()
		l.SetTextFont(72)
		l.SetTextSize(0.03)
		l.SetTextColor(kBlack)
		l.DrawLatex(0.1,0.92, "#intLdt ="+`lumi/1000.`[:3]+" fb^{-1}")	
		
		saveCanvas(c2, '2Dh_fake_'+ichan[0]+'_'+ichan[1], outfile, 'fake_plots')
			
		outfile.cd()	
		h_ratio_fake.Write('2Dfake_'+ichan[0]+'_'+ichan[1])
	
	bkgFile.Close()
	dataFile.Close()	
	outfile.Close()
	return

def plot_multijet_weights():

        channels  = []
        channels += [('resolved','e' )]
        channels += [('resolved','mu')]
        channels += [('boosted', 'e' )]
        channels += [('boosted', 'mu')]

        outfile = TFile("QCDweigths.root","RECREATE")

        for ichan in channels:
		inFile = TFile('../../fakeCR_v2.0_weights_'+ichan[0]+'_QCD/'+ichan[0]+'_'+ichan[1]+'_QCD.root',"READ")
		h = inFile.Get("weight")
		h.GetXaxis().SetRangeUser(-5, 5)
		gStyle.SetOptStat(1111111111)
		print h.GetEntries()
		c = TCanvas("w_"+ichan[0]+'_'+ichan[1],"w_"+ichan[0]+'_'+ichan[1])		
		h.Draw("histo")
		c.SetLogy(1)
		saveCanvas(c, 'QCDweiths_'+ichan[0]+'_'+ichan[1], outfile, 'QCDweiths')

	return	
#--------------------------------#
#       Multijet estimation      #
#--------------------------------#

#Produce eff rate plots

#inputDir = path/to/files/processed/with/TopNtupleAnalysis
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.23c/TopNtupleAnalysis/effSave/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.30/TopNtupleAnalysis/effReal_2/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.30/TopNtupleAnalysis/effReal_3/'

#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.30/TopNtupleAnalysis/realEff_real/'
inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.37/TopNtupleAnalysis/realEff_real/'

if 0:
	effRates(inputDir)

#Produce fake rate plots

#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.33/TopNtupleAnalysis/wPresTrigg_d0sig_z0sin4/' 
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.33/TopNtupleAnalysis/wPresTrigg_d0sig_noz0sin4/' 

#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.37/TopNtupleAnalysis/fakeRates_141215_16h30_fake/' 
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.37/TopNtupleAnalysis/fakeRates_151215_10h00_fake/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.37/TopNtupleAnalysis/fakeRates_151215_12h00_fake/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.37/TopNtupleAnalysis/fakeRates_161215_17h30_fake/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.37/TopNtupleAnalysis/fakeRates_161215_18h00_fake/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.37/TopNtupleAnalysis/fakeRates_161215_19h00_fake/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.37/TopNtupleAnalysis/fakeRates_171215_16h30_fake/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.37/TopNtupleAnalysis/fakeRates_171215_19h30_caloBtag2_fake/'

#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.37/TopNtupleAnalysis/fakeRates_181215_09h30_fake/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.37/TopNtupleAnalysis/fakeRates_181215_09h30_v3.0_fake/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.37/TopNtupleAnalysis/fakeRates_181215_19h20_v2.0_fake/'

#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.37/TopNtupleAnalysis/fakeRates_211215_18h00_v4.0_fake/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.37/TopNtupleAnalysis/fakeRates_221215_11h00_v2.0_fake/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.37/TopNtupleAnalysis/fakeRates_221215_12h00_v4.0_fake/'
inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.37/TopNtupleAnalysis/fakeRates_221215_11h00_v2.0_fake_fake/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.37/TopNtupleAnalysis/fakeRates_221215_12h00_v4.0_fake_fake/'

lumi = 3200 #pb-1

if 1:	
	fakeRates(inputDir, lumi)


if 0:
	plot_multijet_weights()













