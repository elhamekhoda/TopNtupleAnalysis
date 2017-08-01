import os, sys
from ROOT import *
from array import array

gROOT.Reset()

gROOT.SetStyle('Plain')
gStyle.SetPaintTextFormat('4.2f')
gStyle.SetPalette(1)
gStyle.SetTextSize(3)

doprint = ".png,.eps,.pdf"

doHadd = 1
doBothYear = 0
lep = 'mu'
year = '2015'

#OUTDIR = 'PLOT_17_04_04_METL_MWTL_DS3_Combined_4J_GENL_ALT_2015/'
#OUTDIR = 'PLOT_17_06_05_NEW_QCDCR_METL_MWTL_DS3_DelR2.8_4j_fakeRates_2016_e/'
#OUTDIR = 'Debug_FakeRates_e_2016/'
if doBothYear : OUTDIR = 'New_FakeRates_RB_Merged_2015_2016_'+lep+'/'
else : OUTDIR = 'New_FakeRates_RB_'+year+'_'+lep+'/'
#OUTDIR = 'Test_h2DRebin_New_FakeRates_DRCorr_RplusB_2016_mu/'
os.system('mkdir '+OUTDIR)


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
        os.system('rm -f' + oname)
        com = "hadd -f "+oname
        for Dir in list_dir:
                com += " "+Dir
        #print com      
        os.system(com)

'''
def RebinHisto(histo, newNbins):
	Nbins = histo.GetXaxis().GetNbins()
	Name = histo.GetName()
	
	# Number of bins that will be merged into 1 bin
	ngroup = Nbins / newNbins
	binarray = []
	
	bin = 1
	while bin < Nbins+2 :
		binarray.append(histo.GetXaxis().GetBinLowEdge(bin))
		bin += 1
	
	# Rebin the hitograms
	newHisto = histo.Rebin(ngroup, Name, binarray)
	
	return newHisto
'''

def TakeAbsEta(histo, newNbins) :
	Name = histo.GetName()
	Nbins = histo.GetXaxis().GetNbins()
	xtitle = histo.GetXaxis().GetTitle()
	ytitle = histo.GetYaxis().GetTitle()
	
	binarray = []
	
	if newNbins==1 :
		binarray.append(0)
		binarray.append(2.5)
	
	elif newNbins==3 :
		binarray.append(0)
		binarray.append(0.7)
		binarray.append(1.5)
		binarray.append(2.4)
		binarray.append(2.7)
		
	elif newNbins==4 :
		binarray.append(0)
		binarray.append(0.7)
		binarray.append(1.5)	
		binarray.append(2.25)
		binarray.append(2.5)
		
	elif newNbins==20 :
		#binarray = histo.GetXaxis().GetXbins()
		b=-4
		while b<=4:
			#print b
			binarray.append(b)
			b+=8./20
	
	newhisto = TH1F(Name+`newNbins`, Name+`newNbins`, newNbins, array('d',binarray))
	newhisto.GetXaxis().SetTitle(xtitle)
	newhisto.GetYaxis().SetTitle(ytitle)
	
	bin = 1
	#for newbin in binarray :
	while bin < Nbins :
		#newhisto.Fill(abs(histo.GetXaxis().GetBinCenter(bin)), histo.GetBinContent(bin))
		if newNbins==20 :
			newhisto.Fill(abs(histo.GetXaxis().GetBinCenter(bin)), histo.GetBinContent(bin))
		else :
			newhisto.Fill(abs(histo.GetXaxis().GetBinCenter(bin)), histo.GetBinContent(bin))
		'''
		if newNbins==1 :
			newhisto.Fill(binarray[0], histo.GetBinContent(bin))
		
		elif newNbins==3 :
			newhisto.Fill(fabs(histo.GetXaxis().GetBinCenter(bin)), histo.GetBinContent(bin))
			
			if histo.GetXaxis().GetBinCenter(bin) < binarray[0+1] :
				newhisto.Fill((binarray[0]+binarray[0+1])/2., histo.GetBinContent(bin))
			elif histo.GetXaxis().GetBinCenter(bin) < binarray[1+1] :
				newhisto.Fill((binarray[1]+binarray[1+1])/2., histo.GetBinContent(bin))
			elif histo.GetXaxis().GetBinCenter(bin) < binarray[2+1] :
				newhisto.Fill((binarray[2]+binarray[2+1])/2., histo.GetBinContent(bin))
			elif histo.GetXaxis().GetBinCenter(bin) < binarray[3+1] :
				newhisto.Fill((binarray[3]+binarray[3+1])/2., histo.GetBinContent(bin))
			
		elif newNbins==4 :
			if histo.GetXaxis().GetBinCenter(bin) < 0.7 :
				newhisto.Fill(binarray[0], histo.GetBinContent(bin))
			elif histo.GetXaxis().GetBinCenter(bin) < 1.5 :
				newhisto.Fill(binarray[1], histo.GetBinContent(bin))
			elif histo.GetXaxis().GetBinCenter(bin) < 2.25 :
				newhisto.Fill(binarray[2], histo.GetBinContent(bin))
			elif histo.GetXaxis().GetBinCenter(bin) < 2.5 :
				newhisto.Fill(binarray[3], histo.GetBinContent(bin))
		'''
		#print newNbins,bin,histo.GetXaxis().GetBinCenter(bin), histo.GetBinContent(bin)
		bin += 1
	bin = 0
	while bin <  newNbins:
		#print "->",bin,newhisto.GetXaxis().GetBinCenter(bin), newhisto.GetBinContent(bin)
		bin += 1
	
	return newhisto


def RebinDeltaR2D(histo2D) :
	Name = histo2D.GetName()
	NbinsX = histo2D.GetXaxis().GetNbins()
	xtitle = histo2D.GetXaxis().GetTitle()
	ytitle = histo2D.GetYaxis().GetTitle()
	
	newNbinsY = 2
	
	Xbinarray = []
	Ybinarray = []
	
	#Xbinarray = histo2D.GetXaxis().GetXbins()
	binL = 1
	while binL < NbinsX + 1:
		print NbinsX, binL, histo2D.GetXaxis().GetBinLowEdge(binL)
		Xbinarray.append(histo2D.GetXaxis().GetBinLowEdge(binL))
		binL += 1
	
	Ybinarray.append(0)
	Ybinarray.append(0.4)
	Ybinarray.append(7)
	
	newhisto2D = TH2F(Name+`newNbinsY`, Name+`newNbinsY`, NbinsX, array('d',Xbinarray), newNbinsY, array('d',Ybinarray))
	newhisto2D.GetXaxis().SetTitle(xtitle)
	newhisto2D.GetYaxis().SetTitle(ytitle)
	
	binx = 1
	while binx < NbinsX :
		biny = 1
		while biny <= newNbinsY :
			bin = newhisto2D.GetBin(binx, biny)
			newhisto2D.SetBinContent(bin, histo2D.GetBinContent(bin))
			print histo2D.GetBinContent(bin)
			biny += 1
		binx += 1
	
	return newhisto2D


def fakeRates(inputDir, lumi, lumiP):

    parametrization2D = []
    parametrization1D = []
    
    parametrization2D += ['mwt_met_map', 'mwt_met_map_lowDR', 'mwt_met_map_medDR', 'mwt_met_map_highDR', 'lepPt_closJetPt', 'lepPt_closJetPt_lowDR', 'lepPt_closJetPt_highDR']
    parametrization2D += ["lepPt_cosDPhi", "lepPt_cosDPhi_lowDR", "lepPt_cosDPhi_highDR", "lepPt_minDeltaR"]
    parametrization2D += ["lepPt_met", "lepPt_met_lowDR", "lepPt_met_highDR", "lepPt_topoetcone",
                          "lepPt_topoetcone_lowDR", "lepPt_topoetcone_highDR"]
    

    #parametrization1D =  ["lepPt_effBins", "lepPt", "lepEta", "minDeltaR_effBins", "minDeltaR", "closJetPt_effBins", "cos_metPhi_lepPhi", "cos_metPhi_lepPhi_effBins","MET", "d0sig", "chi2", "ptvarcone", "topoetcone"]
    parametrization1D =  ["lepPt_effBins", "lepPt", "lepPt_highDR", "lepPt_lowDR", "lepEta", "lepEta_1bin", "lepEta_3bins", "lepEta_4bins", "lepEta_20bins", "lepEta_80bins", "minDeltaR_effBins", "minDeltaR", "closJetPt_effBins", "cos_metPhi_lepPhi", "cos_metPhi_lepPhi_effBins","MET", "d0sig", "chi2", "ptvarcone", "topoetcone"]
    #parametrization1D =  ["lepEta", "lepEta_1bin", "lepEta_3bins", "lepEta_4bins", "lepEta_20bins", "lepEta_80bins"]
    
    channels  = []
    #channels += [('resolved','mu')]
    channels += [('resolved',lep)]
    #channels += [('boosted',lep)]
    
    #doHadd = 1
    #doBothYear = 0
    
    for ichan in channels:
        # --> Merging the datasets
        hadd_in=[]
        print "ls "+inputDir+ichan[0]+"_"+ichan[1]+"_DT*.root "

        for File in os.popen("ls "+inputDir+ichan[0]+"_"+ichan[1]+"_DT*.root ").readlines():
                 hadd_in.append(File[:-1])
	if doBothYear :
		for File in os.popen("ls "+inputDir2+ichan[0]+"_"+ichan[1]+"_DT*.root ").readlines():
                	hadd_in.append(File[:-1])

        hadd_dataPath = OUTDIR+ichan[0]+"_DATA_"+ichan[1]+".root"
        if doHadd: MergeFiles(hadd_dataPath, hadd_in)


        for ibkg in ["ttbar", "Wev", "Wmv", "Zee", "Zmm"]:

            if doHadd: os.system('rm -f ' + inputDir+ichan[0]+"_"+ichan[1]+"_"+ibkg+".root")
	    
            hadd_intmp= []
            for File in os.popen("ls "+inputDir+ichan[0]+"_"+ichan[1]+"_"+ibkg+"*.root ").readlines():
                hadd_intmp.append(File[:-1])
                #hadd_Path = inputDir+ichan[0]+"_"+ichan[1]+"_"+ibkg+".root"
		
	    if doBothYear :
	    	for File in os.popen("ls "+inputDir2+ichan[0]+"_"+ichan[1]+"_"+ibkg+"*.root ").readlines():
                	hadd_intmp.append(File[:-1])
                
	    hadd_Path = OUTDIR+ichan[0]+"_"+ichan[1]+"_"+ibkg+".root"
            if doHadd: MergeFiles(hadd_Path, hadd_intmp)




        for ibtag in ["btag0_","btag1_","btag2_"] :

            outfile = TFile(OUTDIR+ichan[0]+'_'+ichan[1]+'_'+ibtag+"fake.root","RECREATE")
            #outfile.cd()

            # ---------- 1D fake-rates ---------------------------------------------------# 
            for ipar in parametrization1D :

                #ttbarfile = TFile(inputDir+ichan[0]+"_"+ichan[1]+"_"+"ttbar"+".root",'READ')
		ttbarfile = TFile(OUTDIR+ichan[0]+"_"+ichan[1]+"_"+"ttbar"+".root",'READ')
		#BKGHist_1D = ttbarfile.Get(ibtag+"fake_"+ipar).Clone()
                #BKGHist_Loose_1D = ttbarfile.Get(ibtag+"fake_"+ipar+"_Loose").Clone()
		
		
		#absEtafile = TFile(absEtaDir+"fake_abs_lepEta.root",'READ')
		
		if ipar=="lepEta_1bin" :
			BKGHist_1D = TakeAbsEta(ttbarfile.Get(ibtag+"fake_lepEta").Clone(), 1)
                	BKGHist_Loose_1D = TakeAbsEta(ttbarfile.Get(ibtag+"fake_lepEta_Loose").Clone(), 1)
			
		elif ipar=="lepEta_3bins" :
			BKGHist_1D = TakeAbsEta(ttbarfile.Get(ibtag+"fake_lepEta").Clone(), 3)
			BKGHist_Loose_1D = TakeAbsEta(ttbarfile.Get(ibtag+"fake_lepEta_Loose").Clone(), 3)
		
		elif ipar=="lepEta_4bins" :
			BKGHist_1D = TakeAbsEta(ttbarfile.Get(ibtag+"fake_lepEta").Clone(), 4)
			BKGHist_Loose_1D = TakeAbsEta(ttbarfile.Get(ibtag+"fake_lepEta_Loose").Clone(), 4)
			
		elif ipar=="lepEta_20bins" :
			BKGHist_1D = TakeAbsEta(ttbarfile.Get(ibtag+"fake_lepEta").Clone(), 20)
			BKGHist_Loose_1D = TakeAbsEta(ttbarfile.Get(ibtag+"fake_lepEta_Loose").Clone(), 20)
		
		else:
                	BKGHist_1D = ttbarfile.Get(ibtag+"fake_"+ipar).Clone()
                	BKGHist_Loose_1D = ttbarfile.Get(ibtag+"fake_"+ipar+"_Loose").Clone()
		

		'''
		# Rebin BKG histograms
		if ipar=="lepEta_1bin" :
			BKGHist_1D = RebinHisto(oldBKGHist_1D, 1)
			BKGHist_Loose_1D = RebinHisto(oldBKGHist_Loose_1D, 1)
		
		elif ipar=="lepEta_3bins" :
			BKGHist_1D = RebinHisto(oldBKGHist_1D, 3)
			BKGHist_Loose_1D = RebinHisto(oldBKGHist_Loose_1D, 3)
		
		elif ipar=="lepEta_4bins" :
			BKGHist_1D = RebinHisto(oldBKGHist_1D, 4)
			BKGHist_Loose_1D = RebinHisto(oldBKGHist_Loose_1D, 4)
		
		else :
			BKGHist_1D = oldBKGHist_1D
			BKGHist_Loose_1D = oldBKGHist_Loose_1D
		'''
		
                for ibkg in [("Wev",0.8), ("Wmv",0.8), ("Wtv",0.8), ("Zee",1), ("Zmm",1), ("Ztt",1), ("st",1), ("VV",1)]:

                    if ibkg[0] == "Wtv" or ibkg[0] == "Ztt" or ibkg[0] == "st" or ibkg[0] == "VV" :
		    	bkgfile = TFile(inputDir+ichan[0]+"_"+ichan[1]+"_"+ibkg[0]+".root",'READ')
		    else :
		    	bkgfile = TFile(OUTDIR+ichan[0]+"_"+ichan[1]+"_"+ibkg[0]+".root",'READ')
		    
                    print inputDir+ichan[0]+"_"+ichan[1]+"_"+ibkg[0]+".root"


                    #tmpBKG_1D = bkgfile.Get(ibtag+"fake_"+ipar).Clone()
                    #tmpBKG_Loose_1D = bkgfile.Get(ibtag+"fake_"+ipar+"_Loose").Clone()
		    
		    
		    if ipar=="lepEta_1bin" :
		    	tmpBKG_1D = TakeAbsEta(bkgfile.Get(ibtag+"fake_lepEta").Clone(), 1)
                    	tmpBKG_Loose_1D = TakeAbsEta(bkgfile.Get(ibtag+"fake_lepEta_Loose").Clone(), 1)
		    
		    elif ipar=="lepEta_3bins" :
		    	tmpBKG_1D = TakeAbsEta(bkgfile.Get(ibtag+"fake_lepEta").Clone(), 3)
                    	tmpBKG_Loose_1D = TakeAbsEta(bkgfile.Get(ibtag+"fake_lepEta_Loose").Clone(), 3)
		    
		    elif ipar=="lepEta_4bins" :
		    	tmpBKG_1D = TakeAbsEta(bkgfile.Get(ibtag+"fake_lepEta").Clone(), 4)
                    	tmpBKG_Loose_1D = TakeAbsEta(bkgfile.Get(ibtag+"fake_lepEta_Loose").Clone(), 4)
			
		    elif ipar=="lepEta_20bins" :
		    	tmpBKG_1D = TakeAbsEta(bkgfile.Get(ibtag+"fake_lepEta").Clone(), 20)
                    	tmpBKG_Loose_1D = TakeAbsEta(bkgfile.Get(ibtag+"fake_lepEta_Loose").Clone(), 20)
			
		    else :
		    	tmpBKG_1D = bkgfile.Get(ibtag+"fake_"+ipar).Clone()
                    	tmpBKG_Loose_1D = bkgfile.Get(ibtag+"fake_"+ipar+"_Loose").Clone()
		    
		    
                    tmpBKG_1D.Scale(ibkg[1])
                    tmpBKG_Loose_1D.Scale(ibkg[1])
		    
		    '''
		    if ipar=="lepEta_1bin" :
		    	new_tmpBKG_1D = RebinHisto(tmpBKG_1D, 1)
		    	new_tmpBKG_Loose_1D = RebinHisto(tmpBKG_Loose_1D, 1)
			
		    elif ipar=="lepEta_3bins" :
		    	new_tmpBKG_1D = RebinHisto(tmpBKG_1D, 3)
		    	new_tmpBKG_Loose_1D = RebinHisto(tmpBKG_Loose_1D, 3)
		    
		    elif ipar=="lepEta_4bins" :
		    	new_tmpBKG_1D = RebinHisto(tmpBKG_1D, 4)
		    	new_tmpBKG_Loose_1D = RebinHisto(tmpBKG_Loose_1D, 4)

                    else :
		    	new_tmpBKG_1D = tmpBKG_1D
		    	new_tmpBKG_Loose_1D = tmpBKG_Loose_1D
		    '''
		    
		    BKGHist_1D.Add(tmpBKG_1D)
                    BKGHist_Loose_1D.Add(tmpBKG_Loose_1D)
		    #BKGHist_1D.Add(new_tmpBKG_1D)
                    #BKGHist_Loose_1D.Add(new_tmpBKG_Loose_1D)

                # --- for ibkg in ["ttbar", "Wev", "Wmv", "Wtv", "Zee", "Zmm", "Ztt", "st", "VV"]:

                datafile = TFile(hadd_dataPath, 'READ')

                #DATAHist_1D = datafile.Get(ibtag+"fake_"+ipar).Clone()
                #DATAHist_Loose_1D = datafile.Get(ibtag+"fake_"+ipar+"_Loose").Clone()
		
		
		if ipar=="lepEta_1bin" :
			DATAHist_1D = TakeAbsEta(datafile.Get(ibtag+"fake_lepEta").Clone(), 1)
                	DATAHist_Loose_1D = TakeAbsEta(datafile.Get(ibtag+"fake_lepEta_Loose").Clone(), 1)
		
		elif ipar=="lepEta_3bins" :
			DATAHist_1D = TakeAbsEta(datafile.Get(ibtag+"fake_lepEta").Clone(), 3)
			DATAHist_Loose_1D = TakeAbsEta(datafile.Get(ibtag+"fake_lepEta_Loose").Clone(), 3)
		
		elif ipar=="lepEta_4bins" :
			DATAHist_1D = TakeAbsEta(datafile.Get(ibtag+"fake_lepEta").Clone(), 4)
			DATAHist_Loose_1D = TakeAbsEta(datafile.Get(ibtag+"fake_lepEta_Loose").Clone(), 4)
		
		elif ipar=="lepEta_20bins" :
			DATAHist_1D = TakeAbsEta(datafile.Get(ibtag+"fake_lepEta").Clone(), 20)
			DATAHist_Loose_1D = TakeAbsEta(datafile.Get(ibtag+"fake_lepEta_Loose").Clone(), 20)
		
		else:
                	DATAHist_1D = datafile.Get(ibtag+"fake_"+ipar).Clone()
                	DATAHist_Loose_1D = datafile.Get(ibtag+"fake_"+ipar+"_Loose").Clone()
		'''
		for bb in range(BKGHist_1D.GetXaxis().GetNbins()):
			print bb,BKGHist_1D.GetXaxis().GetBinCenter(bb),BKGHist_1D.GetBinContent(bb)
			print bb,BKGHist_Loose_1D.GetXaxis().GetBinCenter(bb),BKGHist_Loose_1D.GetBinContent(bb)
		'''
		'''
		# Rebin BKG histograms
		if ipar=="lepEta_1bin" :
			DATAHist_1D = RebinHisto(oldDATAHist_1D, 1)
			DATAHist_Loose_1D = RebinHisto(oldDATAHist_Loose_1D, 1)
		
		elif ipar=="lepEta_3bins" :
			DATAHist_1D = RebinHisto(oldDATAHist_1D, 3)
			DATAHist_Loose_1D = RebinHisto(oldDATAHist_Loose_1D, 3)
		
		elif ipar=="lepEta_4bins" :
			DATAHist_1D = RebinHisto(oldDATAHist_1D, 4)
			DATAHist_Loose_1D = RebinHisto(oldDATAHist_Loose_1D, 4)
		
		else :
			DATAHist_1D = oldDATAHist_1D
			DATAHist_Loose_1D = oldDATAHist_Loose_1D
		'''
		
                # --- scaling the BKG by luminosity --- #
                BKGHist_1D.Scale(lumi)
                BKGHist_Loose_1D.Scale(lumi)

                # ---- adding Loose to tight ---- #
                BKGHist_Loose_1D.Add(BKGHist_1D)
                DATAHist_Loose_1D.Add(DATAHist_1D)

                # ---- computing fake-rates ----- #
                h1_1D = DATAHist_1D.Clone()
                h1_1D.Add(BKGHist_1D,-1)

                h2_1D = DATAHist_Loose_1D.Clone()
                h2_1D.Add(BKGHist_Loose_1D,-1)

                #if(ipar == "lepPt_topoetcone" or ipar == "lepPt_topoetcone_lowDR" or ipar == "lepPt_topoetcone_highDR") : 
                #  print (ibtag+ ","+ ipar+ "," + "Num = "+str( h1_2D.GetBinContent(5,1))+ ", Denom = "+str( h2_2D.GetBinContent(5,1)) )                

                h1D_ratio = h1_1D.Clone()
                h1D_ratio.Divide(h1_1D, h2_1D, 1.0, 1.0, "B")

                #gStyle.SetPaintTextFormat("1.2f")
                gStyle.SetOptStat(0)
                c1 = TCanvas("c_"+"1D_"+ipar+"_"+ichan[0]+"_"+ichan[1])
                c1.cd()
                h1D_ratio.SetMarkerStyle(20)
                h1D_ratio.SetLineColor(1)
                h1D_ratio.Draw("e")
                #h1D_ratio.Draw("e1 SAME")
                h1D_ratio.SetStats(0)
                #gPad.RedrawAxis()
                c1.SetLogx(0)


                c1.Update()
                c1.Modified()

                l = TLatex()
                l.SetNDC()
                l.SetTextFont(72)
                l.SetTextSize(0.03)
                l.SetTextColor(kBlack)
                l.DrawLatex(0.1,0.92, "#intLdt ="+`lumiP/1000.`[:3]+" fb^{-1}")
                outfile.cd()
                #h1D_ratio.GetXaxis().SetMoreLogLabels(1)
                h1D_ratio.Write("fakeRate_"+ipar+"_"+ichan[0]+"_"+ichan[1])
                saveCanvas(c1, "h_fake_"+ipar+"_"+ichan[0]+"_"+ichan[1], outfile, OUTDIR+ichan[0]+'_'+ichan[1]+'_'+ibtag+"fake_plots")


            # ---------- 2D fake-rates ---------------------------------------------------#
            for ipar in parametrization2D :

                #ttbarfile = TFile(inputDir+ichan[0]+"_"+ichan[1]+"_"+"ttbar"+".root",'READ')
		ttbarfile = TFile(OUTDIR+ichan[0]+"_"+ichan[1]+"_"+"ttbar"+".root",'READ')
                BKGHist = ttbarfile.Get(ibtag+"fake_"+ipar).Clone()
                BKGHist_Loose = ttbarfile.Get(ibtag+"fake_"+ipar+"_Loose").Clone()

                for ibkg in [("Wev",0.8), ("Wmv",0.8), ("Wtv",0.8), ("Zee",1), ("Zmm",1), ("Ztt",1), ("st",1), ("VV",1)]:

                    #bkgfile = TFile(inputDir+ichan[0]+"_"+ichan[1]+"_"+ibkg[0]+".root",'READ')
		    if ibkg[0] == "Wtv" or ibkg[0] == "Ztt" or ibkg[0] == "st" or ibkg[0] == "VV" :
		    	bkgfile = TFile(inputDir+ichan[0]+"_"+ichan[1]+"_"+ibkg[0]+".root",'READ')
		    else :
		    	bkgfile = TFile(OUTDIR+ichan[0]+"_"+ichan[1]+"_"+ibkg[0]+".root",'READ')
		    
                    print inputDir+ichan[0]+"_"+ichan[1]+"_"+ibkg[0]+".root"
                    
		    tmpBKG = bkgfile.Get(ibtag+"fake_"+ipar).Clone()
                    tmpBKG_Loose = bkgfile.Get(ibtag+"fake_"+ipar+"_Loose").Clone()
		
                    tmpBKG.Scale(ibkg[1])
                    tmpBKG_Loose.Scale(ibkg[1])

                    BKGHist.Add(tmpBKG)
                    BKGHist_Loose.Add(tmpBKG_Loose)

                # --- for ibkg in ["ttbar", "Wev", "Wmv", "Wtv", "Zee", "Zmm", "Ztt", "st", "VV"]:      

                datafile = TFile(hadd_dataPath, 'READ') 

		DATAHist = datafile.Get(ibtag+"fake_"+ipar).Clone()
                DATAHist_Loose = datafile.Get(ibtag+"fake_"+ipar+"_Loose").Clone()

                # --- scaling the BKG by luminosity --- #
                BKGHist.Scale(lumi)
                BKGHist_Loose.Scale(lumi)

                if(ipar == "lepPt_topoetcone" or ipar == "lepPt_topoetcone_lowDR" or ipar == "lepPt_topoetcone_highDR") :
                  print (ibtag+ ","+ ipar+ "," + "Data = "+str( DATAHist.GetBinContent(5,1))+", DataErr = "+str( DATAHist.GetBinError(5,1))+ ", Data_Loose = "+str( DATAHist_Loose.GetBinContent(5,1))+"Data_LooseErr = "+str(DATAHist_Loose.GetBinError(5,1))+"Bkg = "+str(BKGHist.GetBinContent(5,1))+"BkgErr = "+str(BKGHist.GetBinError(5,1))+", Bkg_Loose = "+str(BKGHist_Loose.GetBinContent(5,1))+", Bkg_LooseErr = "+str(BKGHist_Loose.GetBinError(5,1))+", ybin=1" )
                  print (ibtag+ ","+ ipar+ "," + "Data = "+str( DATAHist.GetBinContent(5,2))+", DataErr = "+str( DATAHist.GetBinError(5,2))+ ", Data_Loose = "+str( DATAHist_Loose.GetBinContent(5,2))+"Data_LooseErr = "+str(DATAHist_Loose.GetBinError(5,2))+"Bkg = "+str(BKGHist.GetBinContent(5,2))+"BkgErr = "+str(BKGHist.GetBinError(5,2))+", Bkg_Loose = "+str(BKGHist_Loose.GetBinContent(5,2))+", Bkg_LooseErr = "+str(BKGHist_Loose.GetBinError(5,2))+", ybin=2" )

                # ---- adding Loose to tight ---- #
                BKGHist_Loose.Add(BKGHist) 
                DATAHist_Loose.Add(DATAHist)

                # ---- computing fake-rates ----- #
                h1_2D = DATAHist.Clone()
                h1_2D.Add(BKGHist,-1) 

                h2_2D = DATAHist_Loose.Clone()  
                h2_2D.Add(BKGHist_Loose,-1)

                #if(ipar == "lepPt_topoetcone" or ipar == "lepPt_topoetcone_lowDR" or ipar == "lepPt_topoetcone_highDR") : 
                #  print (ibtag+ ","+ ipar+ "," + "Num = "+str( h1_2D.GetBinContent(5,1))+ ", Denom = "+str( h2_2D.GetBinContent(5,1)) )                

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


                c2.Update()
                c2.Modified()

                l = TLatex()
                l.SetNDC()
                l.SetTextFont(72)
                l.SetTextSize(0.03)
                l.SetTextColor(kBlack)
                l.DrawLatex(0.1,0.92, "#intLdt ="+`lumiP/1000.`[:3]+" fb^{-1}")
                outfile.cd()
                h2D_ratio.GetXaxis().SetMoreLogLabels(1)
                h2D_ratio.Write("2Dfake_"+ipar+"_"+ichan[0]+"_"+ichan[1])
                saveCanvas(c2, "2Dh_"+ipar+"_"+ichan[0]+"_"+ichan[1], outfile, OUTDIR+ichan[0]+'_'+ichan[1]+'_'+ibtag+"fake_plots") 
            # --- for ipar in parametrization2D :  
            #outfile.close()
        # --- for ibtag in ["btag0_","btag1_"] :
    # --- for ichan in channels:

    print 'Clean Exit'



#inputDir = '/AtlasDisk/users/sanmay/TTBar/AnalysisTop-2.4.29/LPCTools/ProduceMiniTuple/17_03_28_NEW_QCDCR_METL_MWTL_DS3_4j_fakeRates_2015_e/'
#inputDir = '/AtlasDisk/users/barbe/FakeRates/AnalysisTop-2.4.29_TopNtupleAnalysis/LPCTools/ProduceMiniTuple/17_06_05_NEW_QCDCR_METL_MWTL_DS3_DelR2.8_4j_fakeRates_2016_e/'
#inputDir = '/AtlasDisk/users/barbe/FakeRates/AnalysisTop-2.4.29_TopNtupleAnalysis/LPCTools/ProduceMiniTuple/Debug_4j_fakeRates_2016_e/'
inputDir =  '/AtlasDisk/users/barbe/FakeRates/AnalysisTop-2.4.29_TopNtupleAnalysis/LPCTools/ProduceMiniTuple/NewFake_RB_4j_fakeRates_'+year+'_'+lep+'/'
inputDir2 = '/AtlasDisk/users/barbe/FakeRates/AnalysisTop-2.4.29_TopNtupleAnalysis/LPCTools/ProduceMiniTuple/NewFake_RB_4j_fakeRates_2015_'+lep+'/'

if year == '2015' :
	ver = '2015'
elif year == '2016' :
	ver = '2016'

if doBothYear :
	ver = '2015+2016'

#lumi = 3200+11571
lumi15,lumi16 = 3200,33257

lumi = lumi15+lumi16

lumiP = 0
if ver == '2015' :
   lumiP = lumi15
elif ver == "2016":
   lumiP = lumi16
else :
   lumiP = lumi

#lumiP = 6000
fakeRates(inputDir, lumi, lumiP)
