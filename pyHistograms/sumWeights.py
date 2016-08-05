#!/usr/bin/env python

import math
from ROOT import *
from optparse import OptionParser

def addFilesInChain(c, txtFileOption):
    for f in txtFileOption.split(','):
        txtf = open(f)
        for l in txtf.readlines():
	    if l[-1] == '\n':
	        l = l[0:-1]
            c.Add(l)

def main():

	parser = OptionParser()
	parser.add_option("-f", "--files",
							 dest="files", default="input.txt",
				  help="Text file with list of input files.", metavar="FILE")

	(options, args) = parser.parse_args()

	sumOfWeights = {} # map of DSID to sum of weights
	pdfSumOfWeights = {} # map of DSID to map of PDF variation names to sum of weights

	t_sumWeights = TChain("sumWeights")
	t_pdfSumWeights = TChain("PDFsumWeights")
	addFilesInChain(t_sumWeights, options.files)
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

	fs = open("sumOfWeights.txt", "w")
	for channel in sorted(sumOfWeights.keys()):
		fs.write("%20d%20s%20f\n" % (channel, "", sumOfWeights[channel]))
	fs.close()

	pfs = open("pdfSumOfWeights.txt", "w")
	for channel in sorted(pdfSumOfWeights.keys()):
		for pdfName in sorted(pdfSumOfWeights[channel].keys()):
			for pdfNumber in range(0, len(pdfSumOfWeights[channel][pdfName])):
				fs.write("%20d%20s%20s%20s%20d%20s%20f\n" % (channel, "", pdfName, "", pdfNumber, "", pdfSumOfWeights[channel][pdfName]))
	pfs.close()

if __name__ == "__main__":
	main()

