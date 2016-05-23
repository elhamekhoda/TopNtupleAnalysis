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
    		  help="Comma-separated list of systematic uncertainties in TTrees in the input file.", metavar="SYSTEMATICS")
    
    (options, args) = parser.parse_args()
    
    if options.fullFiles == '':
        options.fullFiles = options.files
    
    Xsec = {}
    
    sumOfWeights = {} # map of DSID to sum of weights
    # TODO
    pdfSumOfWeights = {} # map of DSID to map of PDF variation names to sum of weights
    
    if not options.data:
        t_sumWeights = TChain("sumWeights")
        addFilesInChain(t_sumWeights, options.fullFiles)
        for k in range(0, t_sumWeights.GetEntries()):
            t_sumWeights.GetEntry(k)
    	    if not t_sumWeights.dsid in sumOfWeights:
    	        sumOfWeights[t_sumWeights.dsid] = 0
    	    sumOfWeights[t_sumWeights.dsid] += t_sumWeights.totalEventsWeighted
    
    loadXsec(Xsec, "../scripts/XSection-MC15-13TeV-ttres.data")
    loadXsec(Xsec, "../../TopDataPreparation/data/XSection-MC15-13TeV.data")
    loadXsec(Xsec, "../share/MC15c-SherpaWZ.data")
    
    # systematics list
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
    anaClass = getattr(analysis, options.analysis) 
    for k in channels:
        analysisCode[k] = anaClass(k, histSuffixes, channels[k])
	#print k, analysisCode[k]
    
    for s in systList:
        # s is nominal, or the name of systematic
        treeName = s # systematic name is the same as the TTree name
        mt = TChain(treeName)
	suffix = s
	if suffix == 'nominal':
	    suffix = ''
        addFilesInChain(mt, options.files)
        for k in range(0, mt.GetEntries()):
	    mt.GetEntry(k)
            if k % 1000 == 0:
    	        print "(",treeName,") Entry ", k, "/", mt.GetEntries()
    	    sel = readEvent(mt)
    	    channel = sel.mcChannelNumber
    	    weight = 1
    	    if not options.data:
    	        weight *= sel.weight_mc
    	        weight *= Xsec[channel]
		# put the remainder in a function to calculate the reweighting
    	        weight *= sel.weight_pileup
    	        if channel in listEWK:
    	            weight *= applyEWK(sel)
                    weight *= sel.weight_leptonSF
    	        btagsf = 1.0
    	        for bidx in range(0, len(sel.tjet_mv2c20)):
    	            pb = TLorentzVector(sel.tjet_pt[bidx], sel.tjet_eta[bidx], sel.tjet_phi[bidx], sel.tjet_e[bidx])
    	            if pb.Perp() > 10e3 and math.fabs(pb.Eta()) < 2.5 and sel.tjet_numConstituents[bidx] >= 2:
    	                btagsf *= sel.tjet_bTagSF_70[bidx]
    	        #weight *= btagsf
		if not channel in sumOfWeights:
		    print "Could not find DSID ",channel, " in TopDataPreparation files."
		    weight = 0
		else:
    	            weight /= sumOfWeights[channel]
    	    nBtags = 0
    	    for bidx in range(0, len(sel.tjet_mv2c20)):
    	        pb = TLorentzVector(sel.tjet_pt[bidx], sel.tjet_eta[bidx], sel.tjet_phi[bidx], sel.tjet_e[bidx])
    	        if pb.Perp() > 10e3 and math.fabs(pb.Eta()) < 2.5 and sel.tjet_numConstituents[bidx] >= 2:
                    if sel.tjet_mv2c20 > MV2C20_CUT:
    	                nBtags += 1
    
    	    if nBtags < 1:
    	        continue
            for ana in analysisCode:
    	        analysisCode[ana].run(sel, suffix, weight)
    
    for k in analysisCode:
        analysisCode[k].end()

if __name__ == "__main__":
    main()

    
