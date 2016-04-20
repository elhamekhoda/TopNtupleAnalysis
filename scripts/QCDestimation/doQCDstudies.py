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

def effRates(inputDir):

	channels  = []
	channels += [('resolved','e' )]
	channels += [('resolved','mu')]
	#channels += [('boosted', 'e' )]
	#channels += [('boosted', 'mu')]

	outfile = TFile('eff_ttbar.root','RECREATE')
	#outfile = TFile('eff_wjets_wev.root','RECREATE')
	
	for ichan in channels:

		if(ichan[0]=='resolved'):	regime = "r";
		elif(ichan[0]=='boosted'):	regime = "b";
				
		hadd_in=""
		hadd_in = inputDir+regime+ichan[1]+"_nom_ttbar*root"
		#hadd_in = inputDir+regime+ichan[1]+"_nom_wev.root"
		
		ttbarFile = ichan[0]+"_ttbar_"+ichan[1]+".root "
		
		print "hadd -f " + ttbarFile + hadd_in
		os.system("hadd -f " + ttbarFile + hadd_in)
		
		inputfile = TFile(ttbarFile,'READ')

		#pT
		hTmp_t_pt = inputfile.Get("eff_LepPt_DR").ProjectionX().Clone()
		hTmp_l_pt = inputfile.Get("eff_LepPt_DR_Loose").ProjectionX().Clone()
		hTmp_l_pt.Add(hTmp_t_pt,+1)
		
		#DR
		hTmp_t_dr = inputfile.Get("eff_LepPt_DR").ProjectionY().Clone()
		hTmp_l_dr = inputfile.Get("eff_LepPt_DR_Loose").ProjectionY().Clone()
		hTmp_l_dr.Add(hTmp_t_dr,+1)
		
		#pT and DR	
		hTmp_t_pTdr = inputfile.Get("eff_LepPt_DR").Clone()		     
		hTmp_l_pTdr = inputfile.Get("eff_LepPt_DR_Loose").Clone()
		hTmp_l_pTdr.Add(hTmp_t_pTdr,+1)
		
		#eff using TH1 lepton pT
		c = TCanvas("c_hP_pt_"  +ichan[0]+'_'+ichan[1])
		leg = TLegend(0.6, 0.7, 0.8, 0.9, "Lept Pt")
		hTmp_t_pt.Draw()		
		hTmp_t_pt.SetStats(0)
		hTmp_t_pt.SetLineColor(2)
		hTmp_t_pt.SetLineWidth(2)
		leg.AddEntry(hTmp_t_pt, "tight: "+`hTmp_t_pt.Integral()`[:10], "L")
		
		hTmp_l_pt.Draw("same")
		hTmp_l_pt.SetStats(0)
		hTmp_l_pt.SetLineColor(4)
		hTmp_l_pt.SetLineWidth(2)
		leg.AddEntry(hTmp_l_pt, "loose: "+`hTmp_l_pt.Integral()`[:10], "L")
		
		c.SetGridy(1)
		c.SetLogy(1)
		c.SetLogx(1)
		c.Update()
                c.Modified()
		leg.Draw()		
		saveCanvas(c, 'hP_pt_'+ichan[0]+'_'+ichan[1], outfile, 'eff_plots')
		
		
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
		c = TCanvas("c_hP_dr_"  +ichan[0]+'_'+ichan[1])
		leg = TLegend(0.6, 0.7, 0.8, 0.9, "min #Delta R")
		hTmp_t_dr.Draw()		
		hTmp_t_dr.SetStats(0)
		hTmp_t_dr.SetLineColor(2)
		hTmp_t_dr.SetLineWidth(2)
		leg.AddEntry(hTmp_t_dr, "tight: "+`hTmp_t_dr.Integral()`[:10], "L")
		
		hTmp_l_dr.Draw("same")
		hTmp_l_dr.SetStats(0)
		hTmp_l_dr.SetLineColor(4)
		hTmp_l_dr.SetLineWidth(2)
		leg.AddEntry(hTmp_l_dr, "loose: "+`hTmp_l_dr.Integral()`[:10], "L")
		
		c.SetGridy(1)
		c.SetLogy(1)
		c.Update()
                c.Modified()
		leg.Draw()		
		saveCanvas(c, 'hP_dr_'+ichan[0]+'_'+ichan[1], outfile, 'eff_plots')
				
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
		c = TCanvas("c_hP_pTdr_tight_"  +ichan[0]+'_'+ichan[1])
		hTmp_t_pTdr.Draw("colzTEXT")
		hTmp_t_pTdr.SetStats(0)
		c.SetLogx(1)
		saveCanvas(c, 'hP_pTdr_tight_'+ichan[0]+'_'+ichan[1], outfile, 'eff_plots')
		
		c = TCanvas("c_hP_pTdr_loose_"  +ichan[0]+'_'+ichan[1])
		hTmp_l_pTdr.Draw("colzTEXT")
		hTmp_l_pTdr.SetStats(0)	
		c.SetLogx(1)
		saveCanvas(c, 'hP_pTdr_loose_'+ichan[0]+'_'+ichan[1], outfile, 'eff_plots')
				
		h_ratio_pTdr = hTmp_t_pTdr
		h_ratio_pTdr.Divide(hTmp_t_pTdr, hTmp_l_pTdr, 1.0, 1.0, "B")
		
		gStyle.SetPaintTextFormat("1.3f")
		c2 = TCanvas("c_"+'eff2D_dr_'+ichan[0]+'_'+ichan[1])
		c2.cd()
		h_ratio_pTdr.Draw()
		h_ratio_pTdr.Draw("colz TEXT e1 SAME")
		
		h_ratio_pTdr.GetZaxis().SetRangeUser(0.5, 1.0)
		
		if(ichan[0]=='boosted'):	h_ratio_pTdr.GetYaxis().SetRangeUser(0., 1.5)
		else:				h_ratio_pTdr.GetYaxis().SetRangeUser(0., 5.0)
		
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
	verbose = 0
		
	channels  = []
	
	
	#channels += [('r','e' )]
	channels += [('r','mu')]
	#channels += [('b', 'e' )]
	#channels += [('b', 'mu')]	
	
	regime  = []
	regime += ['resolved']
	regime += ['boosted']
	
	iPad = 0
	
	outfile = TFile("fake.root","RECREATE")
		
	for ichan in channels:
	
		if(ichan[0]=='r'):	regime = 'resolved'
		if(ichan[0]=='b'):	regime = 'boosted'
	
		hadd_in= []		
		
		# --> Merging the bkg
		for ibkg in ["ttbar", "Wjets", "Zjets", "st"]:			
			
			if ibkg=="ttbar":				
				for File in os.popen("ls "+inputDir+ichan[0]+ichan[1]+"_nom_ttbar.root ").readlines():
					hadd_in.append(File[:-1])
			elif ibkg=="Wjets":
				for File in os.popen("ls "+inputDir+ichan[0]+ichan[1]+"_nom_W*root ").readlines():
					hadd_in.append(File[:-1])
			elif ibkg=="Zjets":
				for File in os.popen("ls "+inputDir+ichan[0]+ichan[1]+"_nom_Z*root ").readlines():
					hadd_in.append(File[:-1])
			elif ibkg=="st":
				for File in os.popen("ls "+inputDir+ichan[0]+ichan[1]+"_nom_st.root ").readlines():
					hadd_in.append(File[:-1])	


		hadd_bkgPath = ichan[0]+"_BKG_"+ichan[1]+".root"
		if merge:	MergeFiles(hadd_bkgPath, hadd_in)
		
		# --> Merging the datasets
		hadd_in=[]		
		#print "ls "+inputDir+ichan[0]+"_fake_"+ichan[1]+"_DT*root "
		
		for File in os.popen("ls "+inputDir+ichan[0]+ichan[1]+"_nom_DT*root ").readlines():
			hadd_in.append(File[:-1])
		
		hadd_dataPath =  ichan[0]+"_DATA_"+ichan[1]+".root"
		if merge:	MergeFiles(hadd_dataPath, hadd_in)
		
		# --> Check QCD at low MWT
		
		bkgFile  = TFile(hadd_bkgPath,'READ')
		dataFile = TFile(hadd_dataPath,'READ')
		
		varList = [] 
		varList += ['mwt','lepPt_effBins','lepPt','minDeltaR_effBins','minDeltaR','closJetPt','MET', 'MET_effBins', 'mwt_met', 'z0sin', 'd0sig']
		varList += ['ljet_m', 'ljet_pt', 'ljet_tau32', 'ljet_tau32_wta', 'cos_metPhi_lepPhi','lepEta','nTrkBtagJets','nJets', 'closJetJVT']
		#varList += ['chi2']
		
		for var in varList:
			
			print var
			
			if (var.find("ljet")!=-1):	
				if (ichan[0]=='r'):	
					continue
					
			if (var.find("chi2")!=-1):	
				if (ichan[0]=='b'):	
					continue		
		
			#tight
			c_t = TCanvas("c_"+ichan[0]+'_'+var+'_tight_'+ichan[1])
			leg = TLegend(0.6, 0.6, 0.8, 0.88, regime+" "+ichan[1]+" channel (tight):")
                	leg.SetTextSize(0.028)
                	leg.SetFillColor(10)
                	leg.SetBorderSize(0)
		
			h_data = dataFile.Get("fake_"+var).Clone()
			h_data.Draw("e")
			h_data.SetMarkerStyle(20)
			h_data.SetStats(0)
			leg.AddEntry(h_data, "Data: "+`h_data.Integral()`[:7], "P")
			if(verbose):	print ichan, "tight:"
			if(verbose):	print 'data &' , `h_data.Integral()`[:7], '\\\ \\hline'
			
			pallete   = [2, 3, 3, 3, 6, 6, 6, 7]
			styleLine = [1, 1 ,2, 3, 1, 2, 3, 1]
			name 	  = ["ttbar", "We#nu", "W#mu#nu", "W#tau#nu", "Zee", "Z#mu#mu", "Z#tau#tau", "st"]
			h_ibkg = []
			i=0
			
			bkgList = ["ttbar", "Wev", "Wmv", "Wtv", "Zee", "Zmm", "Ztt", "st"]
						
			for ibkg in bkgList:
				
				tmp_bkgFile  = TFile(inputDir+ichan[0]+ichan[1]+"_nom_"+ibkg+".root",'READ')	
				if(verbose):	print ibkg, i, var
				#if not tmp_bkgFile.IsOpen():	continue
								
				h_ibkg.append(tmp_bkgFile.Get("fake_"+var).Clone())
				h_ibkg[i].SetDirectory(0)
				h_ibkg[i].Scale(lumi)
				
				
				#print h_ibkg[i].Integral()
				
				if h_ibkg[i].Integral()>0:	
					if h_ibkg[i].Integral()>0.0001: #for better visualization
						if(verbose):	print ibkg, '&' , `h_ibkg[i].Integral()`[:7], '\\\ \\hline'	
						h_ibkg[i].Draw("histo SAME")
						h_ibkg[i].SetStats(0)
					h_ibkg[i].SetLineColor(pallete[i]) 
					h_ibkg[i].SetLineStyle(styleLine[i])
					h_ibkg[i].SetLineWidth(3)					
					#print h_ibkg[i].Integral(), i
					leg.AddEntry(h_ibkg[i],  name[i]+": "+`h_ibkg[i].Integral()`[:7], "L")
				i += 1
			
			h_bkg = bkgFile.Get("fake_"+var).Clone()
			h_bkg.Scale(lumi)
			h_bkg.Draw("histo SAME")
			h_bkg.SetLineColor(4) 
			h_bkg.SetLineWidth(3)
			h_bkg.SetStats(0)
						
			leg.AddEntry(h_bkg,  "total bkg: "+`h_bkg.Integral()`[:7], "L")
			leg.Draw()
			if(verbose):	print 'total bkg &' , `h_bkg.Integral()`[:7], '\\\ \\hline'
			
			
			if h_data.GetMaximum()>h_bkg.GetMaximum():	h_data.SetMaximum(h_data.GetMaximum()*1.3)
			else: 						h_data.SetMaximum(h_bkg.GetMaximum()*1.3)
		
			c_t.SetLogy(0)
			#if var=='lepPt':	c_t.SetLogx(1)
			c_t.SetGridy(1)
			c_t.Update()
                	c_t.Modified()  	    
			saveCanvas(c_t, 'h_'+regime+'_'+var+'_tight_'+ichan[1], outfile, 'fake_plots')
			
			#loose
			c_l = TCanvas("c_"+ichan[0]+'_'+var+'_loose_'+ichan[1])
			leg = TLegend(0.6, 0.6, 0.8, 0.88, regime+" "+ichan[1]+" channel (anti Tight):")
                	leg.SetTextSize(0.028)
	                leg.SetFillColor(10)
        	        leg.SetBorderSize(0)
		
			h_data = dataFile.Get('fake_'+var+'_Loose').Clone()
			h_data.Draw("e")
			h_data.SetMarkerStyle(20)
			h_data.SetStats(0)
			leg.AddEntry(h_data, "Data: "+`h_data.Integral()`[:7], "P")
			if(verbose):	print ichan, "Loose:"
			if(verbose):	print 'data &' , `h_data.Integral()`[:7], '\\\ \\hline'
			
			pallete   = [2, 3, 3, 3, 6, 6, 6, 7]
			styleLine = [1, 1 ,2, 3, 1, 2, 3, 1]
			name 	  = ["ttbar", "We#nu", "W#mu#nu", "W#tau#nu", "Zee", "Z#mu#mu", "Z#tau#tau", "st"]
			h_ibkg = []
			i=0
			for ibkg in ["ttbar", "Wev", "Wmv", "Wtv", "Zee", "Zmm", "Ztt", "st"]:
				tmp_bkgFile  = TFile(inputDir+ichan[0]+ichan[1]+"_nom_"+ibkg+".root",'READ')
				h_ibkg.append(tmp_bkgFile.Get("fake_"+var+'_Loose').Clone())
				h_ibkg[i].SetDirectory(0)
				h_ibkg[i].Scale(lumi)
				if h_ibkg[i].Integral()>0:	
					if h_ibkg[i].Integral()>0.0001:	
						h_ibkg[i].Draw("histo SAME")
						if(verbose):	print ibkg, '&' , `h_ibkg[i].Integral()`[:7], '\\\ \\hline'
						h_ibkg[i].SetStats(0)
					h_ibkg[i].SetLineColor(pallete[i]) 
					h_ibkg[i].SetLineStyle(styleLine[i])
					h_ibkg[i].SetLineWidth(3)					
					#print h_ibkg[i].Integral(), i
					leg.AddEntry(h_ibkg[i],  name[i]+": "+`h_ibkg[i].Integral()`[:7], "L")
				tmp_bkgFile.Close()	
				i += 1
						
			h_bkg = bkgFile.Get('fake_'+var+'_Loose').Clone()
			h_bkg.Scale(lumi)
			h_bkg.Draw("histo SAME")
			h_bkg.SetLineColor(4) 
			h_bkg.SetLineWidth(3)
			h_bkg.SetStats(0)		
		
                	if h_data.GetMaximum()>h_bkg.GetMaximum():	h_data.SetMaximum(h_data.GetMaximum()*1.3)
			else: 						h_data.SetMaximum(h_bkg.GetMaximum()*1.3)	
			
			leg.AddEntry(h_bkg,  "bkg: "+`h_bkg.Integral()`[:7], "L")
			leg.Draw()
			if(verbose):	print 'total bkg &' , `h_bkg.Integral()`[:7], '\\\ \\hline'
			c_l.SetLogy(0)
			c_l.SetGridy(1)
			c_l.Update()
        	        c_l.Modified()  	    
			saveCanvas(c_l, 'h_'+regime+'_'+var+'_loose_'+ichan[1], outfile, 'fake_plots')
			
			
		# --> Fake rate
		
		parametrization1D =  ["lepPt_effBins","lepEta", "minDeltaR_effBins", "closJetPt_effBins", "cos_metPhi_lepPhi", "MET", "d0sig", "MET_effBins", "mwt_effBins", "mwt_met_effBins"]
				
		for ipar in parametrization1D:
		
			histo_t = []
			histo_l = []
			
			iPad=0
			for item in ["BKG","DATA"]:	
			
				if item=="BKG":		inputfile = bkgFile
				elif item=="DATA":	inputfile = dataFile

				histo_t.append( inputfile.Get("fake_"+ipar).Clone() )			   
				histo_l.append( inputfile.Get("fake_"+ipar+"_Loose").Clone() )
				histo_l[iPad].Add(histo_t[iPad],+1)
				
				iPad+=1
				
			histo_t[0].Scale(lumi)
			h1 = histo_t[1]
			h1.Add(histo_t[0],-1)
			if extraPlots:	h1.Write("hP_"+ipar+"_tight_"+ichan[0]+'_'+ichan[1])
		
			histo_l[0].Scale(lumi)
			h2 = histo_l[1]
			h2.Add(histo_l[0],-1)		
			if extraPlots:	h2.Write("hP_"+ipar+"_loose_"+ichan[0]+'_'+ichan[1])
						
			h_ratio = h1
			h_ratio.Divide(h1, h2, 1.0, 1.0, "B")
				
			c = TCanvas("c_"+"fake_"+ipar+"_"+ichan[0]+"_"+ichan[1])
                	maxi = 0
			mini = 0
			h_ratio.Draw("e")
			h_ratio.SetStats(0)
			h_ratio.GetYaxis().SetRangeUser(0,1)
			h_ratio.SetMarkerStyle(20)
			h_ratio.SetMarkerSize(0.8)		 
			c.SetGridy(1)
			c.SetLogx(1)
			if ipar in ["lepEta", "cos_metPhi_lepPhi"]:
				c.SetLogx(0)
			c.SetLogy(0)
			c.Update()
               		c.Modified()
			h_ratio.Write("fakeRate_"+ipar+"_"+regime+"_"+ichan[1])	               			
			saveCanvas(c, "h_fake_"+ipar+"_"+regime+"_"+ichan[1], outfile, "fake_plots")
		

		parametrization2D =  ["lepPt_lepEta", "lepPt_closJetPt", "lepPt_minDeltaR", "lepPt_minDeltaR_lowCos", "lepPt_minDeltaR_highCos"]
		parametrization2D += ["lepPt_cosDPhi", "minDeltaR_cosDPhi", "lepPt_cosDPhi_lowEta", "lepPt_cosDPhi_highEta"]
		parametrization2D += ["minDeltaR_cosDPhi_highLepPt", "minDeltaR_cosDPhi_lowLepPt", "lepPt_met", "lepPt_met_lowDR", "lepPt_met_highDR"]
		parametrization2D += ["minDeltaR_met_highLepPt", "minDeltaR_met_lowLepPt", "lepPt_closJetPt"]
		
		for ipar in parametrization2D:
		
			histo_t = []
			histo_l = []
			
			iPad=0
			for item in ["BKG","DATA"]:	
			
				if item=="BKG":		inputfile = bkgFile
				elif item=="DATA":	inputfile = dataFile

				histo_t.append( inputfile.Get("fake_"+ipar).Clone() )			   
				histo_l.append( inputfile.Get("fake_"+ipar+"_Loose").Clone() )
				histo_l[iPad].Add(histo_t[iPad],+1)
				
				iPad+=1
			
			# ---> 2D fake rates: leptPt vs leptEta
			histo_t[0].Scale(lumi)
			h1_2D = histo_t[1].Clone()
			h1_2D.Add(histo_t[0],-1)	
			if extraPlots:	h1_2D.Write("hP_2D_"+ipar+"_tight_"+regime+'_'+ichan[1])
		
			histo_l[0].Scale(lumi)		
			h2_2D = histo_l[1].Clone()
			h2_2D.Add(histo_l[0],-1) 
			if extraPlots:	h2_2D.Write("hP_2D_"+ipar+"_loose_"+regime+'_'+ichan[1])
		
			if extraPlots:
				c = TCanvas("c_"+"hP_2D_"+ipar+"_t_"+ichan[0]+"_"+ichan[1])
				ht_DTMC = histo_t[1].Clone()
				ht_DTMC.Divide(histo_t[0].Clone())
				ht_DTMC.Draw("colz TEXT e")
				ht_DTMC.SetStats(0)
				c.SetLogx(1)
				ht_DTMC.Write("hP_2D_"+ipar+"_tight_"+regime+"_"+ichan[1])
				saveCanvas(c, "c_hP_2D_"+ipar+"_tight_"+regime+"_"+ichan[1], outfile, 'fake_plots')
			
				c = TCanvas("c_"+"hP_2D_"+ipar+"_l_"+ichan[0]+"_"+ichan[1])
				hl_DTMC = histo_l[1].Clone()
				hl_DTMC.Divide(histo_l[0].Clone())
				hl_DTMC.Draw("colz TEXT e")
				hl_DTMC.SetStats(0)
				c.SetLogx(1)
				hl_DTMC.Write("hP_2D_"+ipar+"_loose_"+regime+"_"+ichan[1])
				saveCanvas(c, "c_hP_2D_"+ipar+"_loose_"+regime+"_"+ichan[1], outfile, 'fake_plots')
		
			h2D_ratio = h1_2D.Clone()
			h2D_ratio.Divide(h1_2D, h2_2D, 1.0, 1.0, "B")
		
			gStyle.SetPaintTextFormat("1.2f")
			c2 = TCanvas("c_"+"2D_"+ipar+"_"+ichan[0]+"_"+ichan[1])
			c2.cd()
			h2D_ratio.Draw()
			h2D_ratio.Draw("colz TEXT e1 SAME")
			h2D_ratio.SetStats(0)
			gPad.RedrawAxis()	
			c2.SetLogx(1)
			if ipar in ["lepPt_met", "lepPt_met_lowDR", "lepPt_met_highDR", "minDeltaR_met_highLepPt", "minDeltaR_met_lowLepPt"]:
				h2D_ratio.GetYaxis().SetRangeUser(20, 150)
			c2.Update()
               		c2.Modified()	
		
			l = TLatex()
			l.SetNDC()
			l.SetTextFont(72)
			l.SetTextSize(0.03)
			l.SetTextColor(kBlack)
			l.DrawLatex(0.1,0.92, "#intLdt ="+`lumi/1000.`[:3]+" fb^{-1}")	
			h2D_ratio.Write("2Dfake_"+ipar+"_"+regime+"_"+ichan[1])
			saveCanvas(c2, "2Dh_"+ipar+"_"+regime+"_"+ichan[1], outfile, "fake_plots")	
	
	bkgFile.Close()
	dataFile.Close()	
	outfile.Close()
	return


def doQCDplots(inputDir, lumi):

	merge = 1
	extraPlots = 1
	verbose = 0
	
	channels  = []

	#channels += [('resolved','e' )]
	#channels += [('resolved','mu')]
	channels += [('boosted', 'e' )]
	#channels += [('boosted', 'mu')]

	iPad = 0

	outfile = TFile("QCDplots.root","RECREATE")
		
	for ichan in channels:
		
		hadd_in= []		
		
		# --> Merging the bkg
		for ibkg in ["ttbar", "Wjets", "Zjets", "st", "QCD"]:			
			
			if ibkg=="ttbar":				
				for File in os.popen("ls "+inputDir+ichan[0]+"_"+ichan[1]+"_ttbar.root ").readlines():
					hadd_in.append(File[:-1])
			elif ibkg=="Wjets":
				for File in os.popen("ls "+inputDir+ichan[0]+"_"+ichan[1]+"_W*root ").readlines():
					hadd_in.append(File[:-1])
			elif ibkg=="Zjets":
				for File in os.popen("ls "+inputDir+ichan[0]+"_"+ichan[1]+"_Z*root ").readlines():
					hadd_in.append(File[:-1])
			elif ibkg=="st":
				for File in os.popen("ls "+inputDir+ichan[0]+"_"+ichan[1]+"_st.root ").readlines():
					hadd_in.append(File[:-1])	
			elif ibkg=="QCD":
				for File in os.popen("ls "+inputDir+ichan[0]+"_"+ichan[1]+"_QCD.root ").readlines():
					hadd_in.append(File[:-1])	

		hadd_bkgPath = ichan[0]+"_BKG_"+ichan[1]+".root"
		if merge:	MergeFiles(hadd_bkgPath, hadd_in)
		
		# --> Merging the datasets
		hadd_in=[]		
		#print "ls "+inputDir+ichan[0]+"_fake_"+ichan[1]+"_DT*root "
		
		for File in os.popen("ls "+inputDir+ichan[0]+"_"+ichan[1]+"_DT*root ").readlines():
			hadd_in.append(File[:-1])
		
		hadd_dataPath =  ichan[0]+"_DATA_"+ichan[1]+".root"
		if merge:	MergeFiles(hadd_dataPath, hadd_in)
		
		# --> Check QCD at low MWT
		
		bkgFile  = TFile(hadd_bkgPath,'READ')
		dataFile = TFile(hadd_dataPath,'READ')
		varList = [] 
		varList += ['mwt','lepPt_effBins','lepPt','closejl_minDeltaR_effBins','closejl_minDeltaR','closejl_pt','MET']
		#varList += ['ljet_m', 'ljet_pt', 'ljet_tau32', 'ljet_tau32_wta', 'lepEta'] 
		
		for var in varList:
			
			print var
			
			if (var.find("ljet")!=-1):	
				if (ichan[0]=='resolved'):	
					continue
		
			#tight
			c_t = TCanvas("c_"+ichan[0]+'_'+var+'_tight_'+ichan[1])
			leg = TLegend(0.6, 0.6, 0.8, 0.88, ichan[0]+" "+ichan[1]+" channel (tight):")
                	leg.SetTextSize(0.028)
                	leg.SetFillColor(10)
                	leg.SetBorderSize(0)
		
			h_data = dataFile.Get(var).Clone()
			h_data.Draw("e")
			h_data.SetMarkerStyle(20)
			h_data.SetStats(0)
			leg.AddEntry(h_data, "Data: "+`h_data.Integral()`[:7], "P")
			if verbose:	print ichan, "tight:"
			if verbose:	print 'data &' , `h_data.Integral()`[:7], '\\\ \\hline'
			
			pallete   = [2, 3, 3, 3, 6, 6, 6, 7, 9]
			styleLine = [1, 1 ,2, 3, 1, 2, 3, 1, 1]
			h_ibkg = []
			i=0
									
			for ibkg in ["ttbar", "Wev", "Wmv", "Wtv", "Zee", "Zmm", "Ztt", "st", "QCD"]:
				
				tmp_bkgFile  = TFile(inputDir+ichan[0]+"_"+ichan[1]+"_"+ibkg+".root",'READ')				
				
				h_ibkg.append(tmp_bkgFile.Get(var).Clone())
				h_ibkg[i].SetDirectory(0)
				if not (ibkg=="QCD"):	h_ibkg[i].Scale(lumi)
				if h_ibkg[i].Integral()>0:	
					if h_ibkg[i].Integral()>0.0001: #for better visualization
						if verbose:	print ibkg, '&' , `h_ibkg[i].Integral()`[:7], '\\\ \\hline'	
						h_ibkg[i].Draw("histo SAME")
						h_ibkg[i].SetStats(0)
					h_ibkg[i].SetLineColor(pallete[i]) 
					h_ibkg[i].SetLineStyle(styleLine[i])
					h_ibkg[i].SetLineWidth(3)					
					#print h_ibkg[i].Integral(), i
					leg.AddEntry(h_ibkg[i],  ibkg+": "+`h_ibkg[i].Integral()`[:7], "L")
				i += 1

			h_bkg = bkgFile.Get(var).Clone()
			h_bkg.Scale(lumi)
			h_bkg.Draw("histo SAME")
			h_bkg.SetLineColor(4) 
			h_bkg.SetLineWidth(3)
			h_bkg.SetStats(0)
						
			leg.AddEntry(h_bkg,  "total bkg: "+`h_bkg.Integral()`[:7], "L")
			leg.Draw()
			if verbose:	print 'total bkg &' , `h_bkg.Integral()`[:7], '\\\ \\hline'
			
			
			if h_data.GetMaximum()>h_bkg.GetMaximum():	h_data.SetMaximum(h_data.GetMaximum()*1.3)
			else: 						h_data.SetMaximum(h_bkg.GetMaximum()*1.3)
		
			c_t.SetLogy(1)
			#if var=='lepPt':	c_t.SetLogx(1)
			c_t.SetGridy(1)
			c_t.Update()
                	c_t.Modified()  	    
			saveCanvas(c_t, 'h_'+ichan[0]+'_'+var+'_tight_'+ichan[1], outfile, 'fake_plots')

def real_fake_eff(inputDir_real, inputDir_fake, lumi):

	channels  = []
	channels += [('resolved','e' )]
	channels += [('resolved','mu')]
	channels += [('boosted', 'e' )]
	channels += [('boosted', 'mu')]

	outfile = TFile('real_fake_eff.root','RECREATE')
	
	for ichan in channels:
		
		#########################################
		#### real eff as function of lept Pt ####
		#########################################
		
		hadd_in_real = ""
		hadd_in_real = inputDir_real+ichan[0]+"_"+ichan[1]+"_ttbar*root"
	
		ttbarFile = ichan[0]+"_ttbar_"+ichan[1]+".root "
		
		print "hadd -f " + ttbarFile + hadd_in_real
		os.system("hadd -f " + ttbarFile + hadd_in_real)
		
		inputfile_real = TFile(ttbarFile,'READ')

		#pT
		hReal_t_pt = inputfile_real.Get("eff_LepPt_DR").ProjectionX().Clone()
		hReal_l_pt = inputfile_real.Get("eff_LepPt_DR_Loose").ProjectionX().Clone()
		
		#eff using TH1 lepton pT
		hReal_ratio_pt = hReal_t_pt
		hReal_ratio_pt.Divide(hReal_t_pt, hReal_l_pt, 1.0, 1.0, "B")
		
		#########################################
		#### fake eff as function of lept Pt ####
		#########################################

		hadd_in_fake = []
		
		for File in os.popen("ls "+inputDir_fake+ichan[0]+"_fake_"+ichan[1]+"_ttbar.root ").readlines():
			print File[:-1]
			hadd_in_fake.append(File[:-1])
		
		for File in os.popen("ls "+inputDir_fake+ichan[0]+"_fake_"+ichan[1]+"_W*root ").readlines():
			hadd_in_fake.append(File[:-1])
		
		for File in os.popen("ls "+inputDir_fake+ichan[0]+"_fake_"+ichan[1]+"_Z*root ").readlines():
			hadd_in_fake.append(File[:-1])

		for File in os.popen("ls "+inputDir_fake+ichan[0]+"_fake_"+ichan[1]+"_st.root ").readlines():
			hadd_in_fake.append(File[:-1])	


		hadd_bkgPath = ichan[0]+"_BKG_"+ichan[1]+".root"
		MergeFiles(hadd_bkgPath, hadd_in_fake)

		# --> Merging the datasets
		hadd_in_fake=[]		
		
		for File in os.popen("ls "+inputDir_fake+ichan[0]+"_fake_"+ichan[1]+"_DT*root ").readlines():
			hadd_in_fake.append(File[:-1])
		
		hadd_dataPath =  ichan[0]+"_DATA_"+ichan[1]+".root"
		MergeFiles(hadd_dataPath, hadd_in_fake)
		
		# --> Check QCD at low MWT
		
		bkgFile  = TFile(hadd_bkgPath,'READ')
		dataFile = TFile(hadd_dataPath,'READ')
		
		hFake_t_pt = []
		hFake_l_pt = []

		for item in ["BKG","DATA"]:	
			
			if item=="BKG":		inputfile_fake = bkgFile
			elif item=="DATA":	inputfile_fake = dataFile
								
			#lept pT
			hFake_t_pt.append( inputfile_fake.Get("fake_lepPt_jetPt").ProjectionX().Clone() )		  	  
			hFake_l_pt.append( inputfile_fake.Get("fake_lepPt_jetPt_Loose").ProjectionX().Clone() )
			
		# ---> 1D fake rates: 
		#lept Pt

		hFake_t_pt[0].Scale(lumi)
		h1 = hFake_t_pt[1]
		h1.Add(hFake_t_pt[0],-1)
		
		hFake_l_pt[0].Scale(lumi)
		h2 = hFake_l_pt[1]
		h2.Add(hFake_l_pt[0],-1)		
		
		hFake_ratio_pt = h1
		hFake_ratio_pt.Divide(h1, h2, 1.0, 1.0, "B")

		##################################################
		#### real and fake eff as function of lept Pt ####
		##################################################
		
		c = TCanvas("c_"+'fake_leptPt_'+ichan[0]+'_'+ichan[1])
		leg = TLegend(0.7, 0.78, 0.85, 0.88, ichan[0]+" "+ichan[1]+" channel:")
		leg.SetTextSize(0.028)
		leg.SetFillColor(10)
		leg.SetBorderSize(0)
			
		#hReal_ratio_pt.Draw("e")
		hReal_ratio_pt.SetMarkerStyle(20)
		hReal_ratio_pt.SetMarkerColor(4)
		hReal_ratio_pt.GetYaxis().SetRangeUser(0., 1.0)
		hReal_ratio_pt.GetXaxis().SetTitle("Pt of lepton [GeV]")
		hReal_ratio_pt.GetYaxis().SetTitle("Efficiency")
		hReal_ratio_pt.SetStats(0)

		hFake_ratio_pt.Draw("eSAME")
		hFake_ratio_pt.SetMarkerStyle(24)
		hFake_ratio_pt.SetMarkerColor(4)
		hFake_ratio_pt.SetStats(0)
		hFake_ratio_pt.GetYaxis().SetRangeUser(0., 1.0)
		hFake_ratio_pt.GetXaxis().SetTitle("Pt of lepton [GeV]")
		hFake_ratio_pt.GetYaxis().SetTitle("fake eff.")
		outfile.cd()
		hFake_ratio_pt.Write('histo_rates_leptPt_'+ichan[0]+'_'+ichan[1])
		'''
		if (hReal_ratio_pt.GetMaximum()>hFake_ratio_pt.GetMaximum()):
			maxi = hReal_ratio_pt.GetMaximum()
		else:
			maxi = hFake_ratio_pt.GetMaximum()	
			
		if (hReal_ratio_pt.GetMinimum()>hFake_ratio_pt.GetMinimum()):
			mini = hFake_ratio_pt.GetMinimum()
		else:
			mini = hReal_ratio_pt.GetMinimum()		
		
		hReal_ratio_pt.SetMaximum(maxi*1.3)
		hReal_ratio_pt.SetMinimum(mini*0.3)
		'''
		leg.AddEntry(hReal_ratio_pt, "real eff.", "P")
		leg.AddEntry(hFake_ratio_pt, "fake eff.", "P")
		
		#leg.Draw()
		
		c.SetLogx(1)
		c.SetGridy(1)
		c.Update()
                c.Modified()		
		saveCanvas(c, 'h_rates_leptPt_'+ichan[0]+'_'+ichan[1], outfile, 'real_fake_eff')

	return	

def get_MM_StatErr(inputDir, lumi):

	merge = 1
	extraPlots = 1
	
	channels  = []
	channels += [('resolved','e' )]
	channels += [('resolved','mu')]
	channels += [('boosted', 'e' )]
	channels += [('boosted', 'mu')]
	
	outfile = TFile("MM_StatErr.root","RECREATE")
	
	for ichan in channels:
		
		inFile_std  = TFile(inputDir+"StatErr_QCD/"+ichan[0]+"_"+ichan[1]+"_QCD.root",'READ')
		inFile_up   = TFile(inputDir+"StatErr_QCD/"+ichan[0]+"_"+ichan[1]+"_QCD_up.root",'READ')
		inFile_down = TFile(inputDir+"StatErr_QCD/"+ichan[0]+"_"+ichan[1]+"_QCD_down.root",'READ')
		
		for var in ['mtt','lepPt']:
		
			c   = TCanvas("c_"+ichan[0]+'_'+var+'_tight_'+ichan[1])
			leg = TLegend(0.6, 0.6, 0.8, 0.88, ichan[0]+" "+ichan[1]+" channel:")
                	leg.SetTextSize(0.028)
                	leg.SetFillColor(10)
                	leg.SetBorderSize(0)
		
			h_QCD_std  = inFile_std.Get(var).Clone()
			h_QCD_up   = inFile_up.Get(var).Clone()
			h_QCD_down = inFile_down.Get(var).Clone()
			
			h_QCD_std.Draw("histo")
			h_QCD_std.SetLineColor(2)
			h_QCD_std.SetLineStyle(1)
			h_QCD_std.SetLineWidth(3)
			#leg.AddEntry(h_QCD_std,  "total bkg: "+`h_bkg.Integral()`[:7], "L")
			
			h_QCD_up.Draw("histoSAME")
			h_QCD_up.SetLineColor(4)
			h_QCD_up.SetLineStyle(2)
			h_QCD_up.SetLineWidth(3)
			leg.AddEntry(h_QCD_up,  "realRate + #sigma and fakeRate - #sigma", "L")
			
			h_QCD_down.Draw("histoSAME")
			h_QCD_down.SetLineColor(4)
			h_QCD_down.SetLineStyle(2)
			h_QCD_down.SetLineWidth(3)
			leg.AddEntry(h_QCD_down,  "realRate - #sigma and fakeRate + #sigma", "L")
			
			leg.Draw()
			saveCanvas(c, ichan[0]+'_'+ichan[1]+'_'+var, outfile, 'MM_StatErr')

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
	
def storeFakeRates():

        channels  = []
        channels += [('resolved','e' )]
        channels += [('resolved','mu')]
        channels += [('boosted', 'e' )]
        channels += [('boosted', 'mu')]

	outfile = TFile("fake_merged.root","RECREATE")
	
	for ichan in channels:
		
		if (ichan[1]=='e'):	path = 'forNote_v4.0/'
		if (ichan[1]=='mu'):	path = 'forNote_v2.0/'
	
		inFile_fake = TFile(path + 'real_fake_eff.root','READ')
		#inFile_fake = TFile(path + 'fake.root','READ')
		
		h = inFile_fake.Get("h_rates_leptPt_"+ichan[0]+"_"+ichan[1]).Clone()
		#h = inFile_fake.Get("2Dfake_"+ichan[0]+"_"+ichan[1]).Clone()
		
		h.Draw()
		
		saveCanvas(h, 'fakeRates_'+ichan[0]+'_'+ichan[1], outfile, 'fakeRates_1D')
		
		#outfile_fake.cd()		
		#h.Write("2Dfake_"+ichan[0]+"_"+ichan[1])
		#inFile_fake.Close()
	
	#outfile_fake.Close()
		
	return	
	
def FakeRatesInSameCanvas():

        channels  = []
        channels += [('resolved','e' )]
        channels += [('resolved','mu')]
        channels += [('boosted', 'e' )]
        channels += [('boosted', 'mu')]
	
	path = ''
	inFile_fake_leptPt = TFile(path + 'real_fake_eff.root','READ')
	outfile = TFile("fake.root","RECREATE")
	
	histo = []
	i=0
	for ilep in ['e','mu']:

		for ichan in ['resolved','boosted']:
			histo.append( inFile_fake_leptPt.Get("histo_rates_leptPt_"+ichan+"_"+ilep).Clone() )
			histo[i].SetDirectory(0)
			outfile.cd()
			histo[i].Write("fakeRate_pt_"+ichan+"_"+ilep)
			i+=1

		
	c = TCanvas("fake_leptPt_e","fake_leptPt_e")
	
	leg = TLegend(0.6, 0.2, 0.8, 0.4, "e channel (leptPt param.):")
	leg.SetTextSize(0.028)
	leg.SetFillColor(10)
	leg.SetBorderSize(0)
	
	histo[0].Draw()
	histo[0].SetMarkerStyle(20)
	histo[0].SetMarkerColor(4)
	histo[0].GetYaxis().SetRangeUser(0., 1.0)
	histo[0].SetLineColor(4)
	leg.AddEntry(histo[0], "resolved", "P")
	
	histo[1].Draw("SAME")
	histo[1].SetMarkerStyle(21)
	histo[1].SetMarkerColor(2)
	histo[1].SetLineColor(2)
	histo[1].SetLineWidth(2)
	histo[1].SetLineStyle(2)
	leg.AddEntry(histo[1], "boosted", "P")
	
	leg.Draw()	
	c.SetLogx(1)
	saveCanvas(c, 'fakeRates_leptPt_e', outfile, 'fake_resolve_boosted_LeptPt')
		
		
	c = TCanvas("fake_leptPt_mu","fake_leptPt_mu")
	leg = TLegend(0.6, 0.2, 0.8, 0.4, "mu channel (leptPt param.):")
	leg.SetTextSize(0.028)
	leg.SetFillColor(10)
	leg.SetBorderSize(0)
	
	histo[2].Draw()
	histo[2].SetMarkerStyle(20)
	histo[2].SetMarkerColor(4)
	histo[2].GetYaxis().SetRangeUser(0., 1.0)
	histo[2].SetLineColor(4)
	leg.AddEntry(histo[2], "resolved", "P")
	
	histo[3].Draw("SAME")
	histo[3].SetMarkerStyle(21)
	histo[3].SetMarkerColor(2)
	histo[3].SetLineColor(2)
	histo[3].SetLineWidth(2)
	histo[3].SetLineStyle(2)
	leg.AddEntry(histo[3], "boosted", "P")
	
	leg.Draw()	
	c.SetLogx(1)
		
	saveCanvas(c, 'fakeRates_leptPt_mu', outfile, 'fake_resolve_boosted_LeptPt')	
		
        channels  = []
        channels += [('resolved','e' )]
        channels += [('resolved','mu')]
        channels += [('boosted', 'e' )]
        channels += [('boosted', 'mu')]
	
	path = 'dr_fakeRate/'
	
	inFile_fake_leptPt = TFile(path + 'fake.root','READ')
	#outfile = TFile("fakes1D.root","RECREATE")
	
	histo = []
	i=0
	for ilep in ['e','mu']:

		for ichan in ['resolved','boosted']:
			outfile.cd()			
			histo.append( inFile_fake_leptPt.Get("h_fake_closeJL_dr_"+ichan+"_"+ilep).Clone() )		
			histo[i].Write("fakeRate_dr_"+ichan+"_"+ilep)
			i+=1
	
	c = TCanvas("fake_DR_e","fake_DR_e")
	leg = TLegend(0.6, 0.2, 0.8, 0.4, "e channel (dr param.):")
	leg.SetTextSize(0.028)
	leg.SetFillColor(10)
	leg.SetBorderSize(0)
	
	histo[0].Draw()
	histo[0].SetMarkerStyle(20)
	histo[0].SetMarkerColor(4)
	histo[0].GetYaxis().SetRangeUser(0., 1.0)
	histo[0].SetStats(0)
	histo[0].SetLineColor(4)
	leg.AddEntry(histo[0], "resolved", "P")
	
	histo[1].Draw("SAME")
	histo[1].SetMarkerStyle(21)
	histo[1].SetMarkerColor(2)
	histo[1].SetStats(0)
	histo[1].SetLineColor(2)
	histo[1].SetLineWidth(2)
	histo[1].SetLineStyle(2)
	
	leg.AddEntry(histo[1], "boosted", "P")
	
	leg.Draw()	
	#c.SetLogx(1)
	saveCanvas(c, 'fakeRates_dr_e', outfile, 'fake_resolve_boosted_DR')
		
		
	c = TCanvas("fake_leptPt_mu","fake_leptPt_mu")
	leg = TLegend(0.6, 0.2, 0.8, 0.4, "mu channel (dr param.):")
	leg.SetTextSize(0.028)
	leg.SetFillColor(10)
	leg.SetBorderSize(0)
	
	histo[2].Draw()
	histo[2].SetMarkerStyle(20)
	histo[2].SetMarkerColor(4)
	histo[2].GetYaxis().SetRangeUser(0., 1.0)
	histo[2].SetStats(0)
	histo[2].SetLineColor(4)
	leg.AddEntry(histo[2], "resolved", "P")
	
	histo[3].Draw("SAME")
	histo[3].SetMarkerStyle(21)
	histo[3].SetMarkerColor(2)
	histo[3].SetStats(0)
	histo[3].SetLineColor(2)
	histo[3].SetLineWidth(2)
	histo[3].SetLineStyle(2)
	leg.AddEntry(histo[3], "boosted", "P")
	
	leg.Draw()	
	#c.SetLogx(1)
		
	saveCanvas(c, 'fakeRates_dr_mu', outfile, 'fake_resolve_boosted_DR')		
	outfile.Close()	
				
	return		real_fake_eff
	

def mergeFakeRates():

	extraPlots = 1

	channels  = []
        channels += [('resolved','e' )]
        channels += [('resolved','mu')]
        #channels += [('boosted', 'e' )]
        #channels += [('boosted', 'mu')]
		
	outfile = TFile("fake_merged.root","RECREATE")
		
		
	for ichan in channels:
		if ichan[0]=='boosted':		
			inFile_fj  = TFile('fake_1FJpt200.root','READ')
			for var in ["pt", "dr"]:			
				h   = inFile_fj.Get('fakeRate_'+var+'_'+ichan[0]+'_'+ichan[1]).Clone()
				outfile.cd()
				h.Write('fakeRate_'+var+'_'+ichan[0]+'_'+ichan[1])

		if (ichan[0]=='resolved' and ichan[1]=='e'):
			#path   = '040416_WJetsCR_noBtag'
			path   = '040416_WJetsCR_Btag'
			inFile = TFile(path +'/fake.root','READ')
			#inFile.ls()
			for var in ["leptPt_cosDPhi", "leptPt_cosDPhi_lowEta", "leptPt_cosDPhi_highEta"]: 
				print '2Dfake_'+var+'_'+ichan[0]+'_'+ichan[1]
				h   = inFile.Get('2Dfake_'+var+'_'+ichan[0]+'_'+ichan[1]).Clone()
				outfile.cd()
				h.Write('2Dfake_'+var+'_'+ichan[0]+'_'+ichan[1])
			'''	
			for var in ["lepPt","lepEta", "minDeltaR_effBins", "closJetPt_effBins", "cos_metPhi_lepPhi", "MET", "d0sig", "MET_effBins", "mwt_effBins", "mwt_met_effBins"]:	
				print 'fakeRate_'+var+'_'+ichan[0]+'_'+ichan[1]
				h   = inFile.Get('fakeRate_'+var+'_'+ichan[0]+'_'+ichan[1]).Clone()
				outfile.cd()
				h.Write('fake_'+var+'_'+ichan[0]+'_'+ichan[1])
			'''	
				
		if (ichan[0]=='resolved' and ichan[1]=='mu'):
			#path   = '190416_metmwtCuts_v2.7_fakeRates'
			path   = '190416_metmwtCuts_Btag_v2.7_fakeRates'
			inFile = TFile(path +'/fake.root','READ')
			#inFile.ls()
			for var in ["lepPt_closJetPt"]:
				print '2Dfake_'+var+'_'+ichan[0]+'_'+ichan[1]
				h   = inFile.Get('2Dfake_'+var+'_'+ichan[0]+'_'+ichan[1]).Clone()
				outfile.cd()
				h.Write('fake_'+var+'_'+ichan[0]+'_'+ichan[1])	
			'''
			for var in ["lepPt_effBins","lepEta", "minDeltaR_effBins", "closJetPt_effBins", "cos_metPhi_lepPhi", "MET", "d0sig", "MET_effBins", "mwt_effBins", "mwt_met_effBins"]:	
				print 'fakeRate_'+var+'_'+ichan[0]+'_'+ichan[1]
				h   = inFile.Get('fakeRate_'+var+'_'+ichan[0]+'_'+ichan[1]).Clone()
				outfile.cd()
				h.Write('fake_'+var+'_'+ichan[0]+'_'+ichan[1])	
		
			'''
				
	return			
				
				
def forWJets(inputDir):

	extraPlots = 1

	channels  = []
        channels += [('resolved','e' )]
        channels += [('resolved','mu')]
        #channels += [('boosted', 'e' )]
        #channels += [('boosted', 'mu')]
	
	for iCR in ['Btag','noBtag']:
	
		outfile = TFile('WjetsCR_'+iCR+'.root',"RECREATE")
		
		for ichan in channels:						
			
			path = inputDir+iCR+'_v1.0_'+ichan[0]+'_WjetsCR/'
			inFile = TFile(path+ichan[0]+'_'+ichan[1]+'_WjetsCR.root','READ')
			
			varList = [] 
			varList += ['mwt','lepPt_effBins','lepPt','closejl_minDeltaR_effBins','closejl_minDeltaR']
			varList += ['closejl_pt','MET', 'MET_phi', 'nJets', 'nTrkBtagJets','yields']
		
			for var in varList:
				print var
				c = TCanvas(var+"_"+ichan[0]+'_'+ichan[1]+'_'+iCR, var+"_"+ichan[0]+'_'+ichan[1]+'_'+iCR)
				histo   = inFile.Get(var).Clone()
				histo.Draw("histo")
				histo.SetStats(0)
				outfile.cd()
				histo.Write(var)
				c.SetGridy(1)
				saveCanvas(c, var+"_"+ichan[0]+'_'+ichan[1]+'_'+iCR, outfile, 'WjetsCR_'+iCR)
	return							

#--------------------------------#
#       Multijet estimation      #
#--------------------------------#

#Produce eff rate plots

#FOR W+JETS:

#>2jets (resolved) && Btag
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis/Wjets_v1.0_Btag_real/'

#>2jets (resolved) && noBtag
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis/Wjets_v1.0_noBtag_real/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis/wjets_newBins_noBtag_real/'

#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis/290316_WJets_wev_real/'

inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis_commit/310316_newCode_ttbar_real/'
if 0:
	effRates(inputDir)

#NOMINAL

#bmu
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis/CR2_withFJ_bmu_nom_fake/'

#be
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis/CR5_be_180216_nom_fake/' 

#FOR W+JETS: 

#>2jets (resolved) && Btag
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis/Wjets_v1.1_Btag_el_fake/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis/Wjets_v1.1_Btag_mu_fake/'

#>2jets (resolved) && noBtag
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis/Wjets_v1.1_noBtag_el_fake/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis/Wjets_v1.1_noBtag_mu_fake/'


#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis/Wjets_noBtag_newBins1_fake/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis/re_invChi2_fake/'


#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis/2Dfake_par_mu_2_fake/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis/2Dfake_invChi2_090316_v1.0_e_fake/'

#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis_commit/310316_newCode_fake/'

#WJETS electron
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis_commit/040316_Wjets_pretag_v1.0_e_fake/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis_commit/040316_Wjets_tag_v1.0_e_fake/'

#WJETS muon
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis_commit/040316_Wjets_pretag_v7.0_mu_fake/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis_commit/040316_Wjets_tag_v1.1_mu_fake/'

#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis_commit/040316_Wjets_pretag_CR2_v1.0_mu_fake/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis_commit/080416_Wjets_pretag_CR2_v2.0_mu_fake/'

#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis_commit/120416_noCuts_v2.2_fake/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis_commit/140416_z0Inv_v1.0_fake/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis_commit/100416_METMWT60_fake/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis_commit/100416_MET20_fake/'

#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis_commit/150416_SRCuts_v1.2_fake/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis_commit/150416_noMETMWTCuts_v1.2_fake/'

#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis_commit/180416_newBinning_v1.2_fake/'

#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis_commit/180416_newBinning_metmwtCuts_v1.0_fake/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis_commit/180416_metmwtCuts_v2.1_fake/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis_commit/180416_NometmwtCuts_v2.1_fake/'
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis_commit/180416_NometmwtCuts_d0sig5_v2.1_fake/'
inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis_commit/190416_metmwtCuts_Btag_v2.8_fake/'

lumi = 3209.05 #pb-1

if 0:	
	fakeRates(inputDir, lumi)

#NOMINAL

#bmuQCD
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis/CR2_withFJ_bmu_dr_v1.0_boosted_QCD/'

#beQCD
#inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis/CR4_noFJ_2_boosted_QCD/'

lumi = 3209.05 #pb-1

if 0:	
	doQCDplots(inputDir, lumi)


# Draw real/fake eff
inputDir_real = '/AtlasDisk/users/romano/fakeStudies/2.3.37/TopNtupleAnalysis/realEff_moreBins_real/'
#inputDir_fake = '/AtlasDisk/users/romano/fakeStudies/2.3.37/TopNtupleAnalysis/fakeRates_070116_16h00_v2.0_fake/'

#fornote
#inputDir_fake = '/AtlasDisk/users/romano/fakeStudies/2.3.37/TopNtupleAnalysis/fakeRates_070116_16h00_v2.0_fake/'
#inputDir_fake = '/AtlasDisk/users/romano/fakeStudies/2.3.37/TopNtupleAnalysis/fakeRates_070116_17h30_v4.0_fake/'

lumi = 3200 #pb-1

inputDir_real = '/AtlasDisk/users/romano/fakeStudies/2.3.37/TopNtupleAnalysis/v5_nom_real/'
inputDir_fake = '/AtlasDisk/users/romano/fakeStudies/2.3.37/TopNtupleAnalysis/afterChanges_nom_fake/'

if 0:
	real_fake_eff(inputDir_real, inputDir_fake, lumi)


#Plot the QCD weiths
if 0:
	plot_multijet_weights()

#get stat bands
inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.37/TopNtupleAnalysis/'
lumi = 3200 #pb-1

if 0:	get_MM_StatErr(inputDir, lumi)

if 0:	storeFakeRates()
	
if 0:	FakeRatesInSameCanvas()

if 1:	mergeFakeRates()

inputDir = '/AtlasDisk/users/romano/fakeStudies/2.3.41/TopNtupleAnalysis_SR/'
if 0:	forWJets(inputDir)
