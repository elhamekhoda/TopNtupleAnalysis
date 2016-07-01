#!/usr/bin/env python

from helpers import *
import math
from ROOT import *
from analysis import *
from optparse import OptionParser

def main():

	parser = OptionParser()
	parser.add_option("-d", "--data",
							 action="store_true", dest="data", default=False,
							 help="Is this data?", metavar="BOOL")
	parser.add_option("-f", "--files",
							 dest="files", default="input.txt",
				  help="Text file with list of input files.", metavar="FILE")
	parser.add_option("-F", "--fullFiles",
							 dest="fullFiles", default="",
				  help="Text file with list of all input files for normalisation calculation.", metavar="FILE")
	parser.add_option("-A", "--analysis",
							 dest="analysis", default="AnaTtresSL",
				  help="Analysis code to run.", metavar="ANALYSIS")
	parser.add_option("-o", "--output",
							 dest="output", default="re:hist_re.root,rmu:hist_rmu.root,be:hist_be.root,bmu:hist_bmu.root",
				  help="Comma-separated list of output ROOT files.", metavar="FILES")
	parser.add_option("-s", "--systs",
							 dest="systs", default="nominal",
				  help="Comma-separated list of systematic uncertainties in TTrees in the input file. Use 'all' to run over all the default ones.", metavar="SYSTEMATICS")
	parser.add_option("-W", "--WjetsHF",
							 dest="WjetsHF", default="all",
				  help="Which W+jets HF to keep. Can be all, bb, cc, c or l.", metavar="FLAVOURS")
	parser.add_option("-P", "--pdf",
							 dest="pdf", default="",
				  help="Which PDFs to reweight to.", metavar="PDFS")
	parser.add_option("-Q", "--qcd",
							 dest="qcd", default="",
				  help="Apply QCD weights?", metavar="BOOL")
	 
	(options, args) = parser.parse_args()
	 
	if options.fullFiles == '':
		options.fullFiles = options.files

	pdfList = options.pdf.split(',')
	Xsec = {}
	 
	sumOfWeights = {} # map of DSID to sum of weights
	# TODO
	pdfSumOfWeights = {} # map of DSID to map of PDF variation names to sum of weights
	
	if not options.data:
		t_sumWeights = TChain("sumWeights")
		t_pdfSumWeights = TChain("PDFsumWeights")
		addFilesInChain(t_sumWeights, options.fullFiles)
		for k in range(0, t_sumWeights.GetEntries()):
			t_sumWeights.GetEntry(k)
			if not t_sumWeights.dsid in sumOfWeights:
				sumOfWeights[t_sumWeights.dsid] = 0
			sumOfWeights[t_sumWeights.dsid] += t_sumWeights.totalEventsWeighted
		for k in range(0, t_pdfSumWeights.GetEntries()):
			t_pdfSumWeights.GetEntry(k)
			if not t_pdfSumWeights.dsid in pdfSumOfWeights:
				pdfSumOfWeights[t_pdfSumWeights.dsid] = {}
			for l in pdfList:
				if l not in pdfSumOfWeights[t_pdfSumWeights.dsid]:
					pdfSumOfWeights[t_pdfSumWeights.dsid][l] = []
				pdfAttr = getattr(t_pdfSumWeights, l)
				if len(pdfSumOfWeights[t_pdfSumWeights.dsid][l]) == 0:
					pdfSumOfWeights[t_pdfSumWeights.dsid][l] = [0]*len(pdfAttr)
				for m in range(0, len(pdfAttr)):
					pdfSumOfWeights[t_pdfSumWeights.dsid][l][m] += pdfAttr[l][m]
				
	 
	loadXsec(Xsec, "../scripts/XSection-MC15-13TeV-ttres.data")
	loadXsec(Xsec, "../../TopDataPreparation/data/XSection-MC15-13TeV.data")
	#loadXsec(Xsec, "../share/MC15c-SherpaWZ.data")
	 
	# systematics list
	if options.systs == 'all':
		systList = []
		systList.append('nominal')
		for i in range(0, 4):
			systList.append('btagbSF_'+str(i)+'__1up')
			systList.append('btagbSF_'+str(i)+'__1down')
			if i == 0:
				for j in range(1, 4):
					systList.append('btagbSF_'+str(i)+'_pt'+str(j)+'__1up')
					systList.append('btagbSF_'+str(i)+'_pt'+str(j)+'__1down')
		for i in range(0, 4):
			systList.append('btagcSF_'+str(i)+'__1up')
			systList.append('btagcSF_'+str(i)+'__1down')
			if i == 0:
				for j in range(1, 4):
					systList.append('btagcSF_'+str(i)+'_pt'+str(j)+'__1up')
					systList.append('btagcSF_'+str(i)+'_pt'+str(j)+'__1down')
		for i in range(0, 11):
			systList.append('btaglSF_'+str(i)+'__1up')
			systList.append('btaglSF_'+str(i)+'__1down')
			if i == 0:
				for j in range(1, 4):
					systList.append('btaglSF_'+str(i)+'_pt'+str(j)+'__1up')
					systList.append('btaglSF_'+str(i)+'_pt'+str(j)+'__1down')
		systList.append('btageSF_0__1up')
		systList.append('btageSF_0__1down')
		systList.append('btageSF_1__1up')
		systList.append('btageSF_1__1down')
		systList.extend(weightChangeSystematics)
		systList.remove('')
		systList.append('ttEWK__1up')
		systList.append('ttEWK__1down')
		systList.append('wnorm__1up')
		systList.append('wnorm__1down')
		systList.append('wbb__1up')
		systList.append('wbb__1down')
		systList.append('wcc__1up')
		systList.append('wcc__1down')
		systList.append('wc__1up')
		systList.append('wc__1down')
		systList.append('wl__1up')
		systList.append('wl__1down')
		systematics  = 'EG_RESOLUTION_ALL__1down,EG_RESOLUTION_ALL__1up,EG_SCALE_ALL__1down,EG_SCALE_ALL__1up'
		systematics += ',JET_JER_SINGLE_NP__1up'
		systematics += ',JET_NPScenario1_JET_EtaIntercalibration_NonClosure__1down,JET_NPScenario1_JET_EtaIntercalibration_NonClosure__1up'
		systematics += ',JET_NPScenario1_JET_GroupedNP_2__1down,JET_NPScenario1_JET_GroupedNP_2__1up,JET_NPScenario1_JET_GroupedNP_3__1down,JET_NPScenario1_JET_GroupedNP_3__1up,JET_NPScenario1_JET_GroupedNP_1__1up,JET_NPScenario1_JET_GroupedNP_1__1down'
		systematics += ',MET_SoftTrk_ResoPara,MET_SoftTrk_ResoPerp,MET_SoftTrk_ScaleDown,MET_SoftTrk_ScaleUp'
		systematics += ',MUONS_ID__1down,MUONS_ID__1up,MUONS_MS__1down,MUONS_MS__1up,MUONS_SCALE__1down,MUONS_SCALE__1up'
		systematics += ',LARGERJET_Strong_JET_Rtrk_Modelling_All__1up,LARGERJET_Strong_JET_Rtrk_Modelling_All__1down,LARGERJET_Strong_JET_Rtrk_Baseline_All__1down,LARGERJET_Strong_JET_Rtrk_Baseline_All__1up,LARGERJET_Strong_JET_Rtrk_Tracking_All__1down,LARGERJET_Strong_JET_Rtrk_Tracking_All__1up,LARGERJET_Strong_JET_Rtrk_TotalStat_All__1down,LARGERJET_Strong_JET_Rtrk_TotalStat_All__1up'
		systList.extend(systematics.split(','))
	elif options.systs == 'pdf':
		systList.append('nominal')
		for m in pdfList:
			nvar = len(pdfSumOfWeights[pdfSumOfWeights.keys()[0]][m])
			for k in range(0, nvar):
				systList.append('pdf_%s_%d' % (m, k))
	else:
		systList = options.systs.split(',')
	 
	# load analysis code
	histSuffixes = []
	for item in systList:
		if item == 'nominal':
			histSuffixes.append('')
		else:
			histSuffixes.append(item)
	channels = {}
	for k in options.output.split(','):
		channels[k.split(':')[0]] = k.split(':')[1]
	analysisCode = {}
	import analysis
	#print "Systematics: ", histSuffixes
	#print "To loop over: ", systList
	anaClass = getattr(analysis, options.analysis) 
	for k in channels:
		analysisCode[k] = anaClass(k, histSuffixes, channels[k])
		analysisCode[k].keep = options.WjetsHF
		analysisCode[k].applyQcd = False
		if options.qcd == "True":
			analysisCode[k].applyQcd = True
		print k, analysisCode[k], channels[k]
	 
	for s in systList:
		# s is nominal, or the name of systematic
		treeName = s # systematic name is the same as the TTree name
		if treeName in weightChangeSystematics or 'btag' in treeName or 'wnorm' in treeName or 'wbb_' in treeName or 'wcc_' in treeName or 'wc_' in treeName or 'wl_' in treeName or 'ttEWK_' in treeName or 'pdf_' in treeName:
			treeName = 'nominal'
		if options.qcd == 'True':
			treeName += '_Loose'
		mt = TChain(treeName)
		suffix = s
		if suffix == 'nominal':
			suffix = ''
		addFilesInChain(mt, options.files)

		for k in range(0, mt.GetEntries()):
			mt.GetEntry(k)
			if k % 10000 == 0:
				print "(tree = ",treeName,", syst = ",suffix,") Entry ", k, "/", mt.GetEntries()
			sel = readEvent(mt)

			# common part of the weight
			weight = 1
			if not options.data:
				weight *= sel.weight_mc
				channel = sel.mcChannelNumber
				weight *= Xsec[channel]
				if not 'pdf_' in suffix:
					if not channel in sumOfWeights:
						print "Could not find DSID ",channel, " in sum of weights."
						weight = 0
					else:
						weight /= sumOfWeights[channel]
				else:
					pdfName = suffix.split('_', 1)[1]
					pdfNumber = int(suffix.rsplit('_', 1)[1])
					if not channel in pdfSumOfWeights:
						print "Could not find DSID ",channel, " in sum of weights."
						weight = 0
					else:
						weight /= pdfSumOfWeights[channel][pdfName][pdfNumber]
					

			for ana in analysisCode:
				weight_reco = analysisCode[ana].getWeight(sel, suffix)
				if 'pdf_' in suffix:
					pdfName = suffix.split('_', 1)[1]
					pdfNumber = int(suffix.rsplit('_', 1)[1])
					pdfAttr = getattr(sel, pdfName)
					weight_reco *= pdfAttr[pdfNumber]
				analysisCode[ana].run(sel, suffix, weight*weight_reco, weight)
	 
	for k in analysisCode:
		analysisCode[k].end()

if __name__ == "__main__":
	main()

