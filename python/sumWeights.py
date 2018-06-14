#!/usr/bin/env python
import ROOT
import os
import helpers
logger = helpers.getLogger('TopNtupleAnalysis.sumWeights')

pdfList = ['PDF4LHC15_nlo_30']
wjpdfList = [7]+range(11, 110+1)

def main(files, types, suffix):
    files = files.split(',')
    types = types.split(',')
    assert len(files) == len(types), '"types" must be of the same size of "files"'
    for f, t in zip(files, types):
        if t == "pdf":
            pdfSumOfWeights = {} # map of DSID to map of PDF variation names to sum of weights
            t_pdfSumWeights = ROOT.TChain("PDFsumWeights")
            helpers.addFilesInChain(t_pdfSumWeights, [f])
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
                        pdfSumOfWeights[t_pdfSumWeights.dsid][l][m] += pdfAttr[m]

            pfs = open(os.path.join(helpers.data_path, "sumOfWeights%s%s.txt") % (t, suffix), "w")
            for channel in sorted(pdfSumOfWeights.keys()):
                for pdfName in sorted(pdfSumOfWeights[channel].keys()):
                    for pdfNumber in range(0, len(pdfSumOfWeights[channel][pdfName])):
                        pfs.write("%20d%20s%20s%20s%20d%20s%20f\n" % (channel, "", pdfName, "", pdfNumber, "", pdfSumOfWeights[channel][pdfName][pdfNumber]))
                        logger.debug("%20d%20s%20s%20s%20d%20s%20f\n" % (channel, "", pdfName, "", pdfNumber, "", pdfSumOfWeights[channel][pdfName][pdfNumber]))

            sumOfWeights = {} # map of DSID to sum of weights
            t_sumWeights =  ROOT.TChain("sumWeights")
            helpers.addFilesInChain(t_sumWeights, [f])
            for k in range(0, t_sumWeights.GetEntries()):
                t_sumWeights.GetEntry(k)
                if not t_sumWeights.dsid in sumOfWeights:
                    sumOfWeights[t_sumWeights.dsid] = 0
                sumOfWeights[t_sumWeights.dsid] += t_sumWeights.totalEventsWeighted

            for channel in sorted(sumOfWeights.keys()):
                pfs.write("%20d%20s%20s%20s%20d%20s%20f\n" % (channel, "", "nominal", "", -1, "", sumOfWeights[channel]))
                logger.debug("%20d%20s%20s%20s%20d%20s%20f\n" % (channel, "", "nominal", "", -1, "", sumOfWeights[channel]))
            pfs.close()
        elif t == "wjpdf":
            pdfName = "NNPDF30_nnlo_as_0118"
            wjpdfSumOfWeights = {} # map of DSID to map of PDF variation names to sum of weights
            t_wjpdfSumWeights = ROOT.TChain("sumWeights")
            helpers.addFilesInChain(t_wjpdfSumWeights, [f])
            for k in range(0, t_wjpdfSumWeights.GetEntries()):
                t_wjpdfSumWeights.GetEntry(k)
                if not t_wjpdfSumWeights.dsid in wjpdfSumOfWeights:
                    wjpdfSumOfWeights[t_wjpdfSumWeights.dsid] = {}
                pdfAttr = t_wjpdfSumWeights.totalEventsWeighted_mc_generator_weights
                for l in range(0, len(wjpdfList)):
                    if l not in wjpdfSumOfWeights[t_wjpdfSumWeights.dsid]:
                        wjpdfSumOfWeights[t_wjpdfSumWeights.dsid][l] = 0
                    value = float(pdfAttr[wjpdfList[l]])
                    #if value < -200000: print "Read ", value, " in item ", wjpdfList[l], " in file ", t_wjpdfSumWeights.GetCurrentFile().GetName()
                    #if value > 200000: print "Read ", value, " in item ", wjpdfList[l], " in file ", t_wjpdfSumWeights.GetCurrentFile().GetName()
                    if (value > 60000 or value < -60000) and l in [42]: 
                        logger.info(" ".join("Read ", value, " in item ", wjpdfList[l], " in file ", t_wjpdfSumWeights.GetCurrentFile().GetName()))
                    wjpdfSumOfWeights[t_wjpdfSumWeights.dsid][l] += value

            pfs = open(os.path.join(helpers.data_path, "sumOfWeights%s%s.txt") % (t, suffix), "w")
            for channel in sorted(wjpdfSumOfWeights.keys()):
                for pdfNumber in range(0, len(wjpdfSumOfWeights[channel])):
                    pfs.write("%20d%20s%20s%20s%20d%20s%20f\n" % (channel, "", pdfName, "", pdfNumber, "", wjpdfSumOfWeights[channel][pdfNumber]))
                    logger.debug("%20d%20s%20s%20s%20d%20s%20f\n" % (channel, "", pdfName, "", pdfNumber, "", wjpdfSumOfWeights[channel][pdfNumber]))

            sumOfWeights = {} # map of DSID to sum of weights
            t_sumWeights = ROOT.TChain("sumWeights")
            helpers.addFilesInChain(t_sumWeights, [f])
            for k in range(0, t_sumWeights.GetEntries()):
                t_sumWeights.GetEntry(k)
                if not t_sumWeights.dsid in sumOfWeights:
                    sumOfWeights[t_sumWeights.dsid] = 0
                sumOfWeights[t_sumWeights.dsid] += t_sumWeights.totalEventsWeighted

            for channel in sorted(sumOfWeights.keys()):
                pfs.write("%20d%20s%20s%20s%20d%20s%20f\n" % (channel, "", "nominal", "", -1, "", sumOfWeights[channel]))
                logger.debug("%20d%20s%20s%20s%20d%20s%20f\n" % (channel, "", "nominal", "", -1, "", sumOfWeights[channel]))
            pfs.close()
        else:
            sumOfWeights = {} # map of DSID to sum of weights
            t_sumWeights = ROOT.TChain("sumWeights")
            helpers.addFilesInChain(t_sumWeights, [f])

            for k in range(0, t_sumWeights.GetEntries()):
                t_sumWeights.GetEntry(k)
                if not t_sumWeights.dsid in sumOfWeights:
                    sumOfWeights[t_sumWeights.dsid] = 0
                sumOfWeights[t_sumWeights.dsid] += t_sumWeights.totalEventsWeighted

            fs = open(os.path.join(helpers.data_path, "sumOfWeights%s%s.txt") % (t, suffix), "w")
            for channel in sorted(sumOfWeights.keys()):
                fs.write("%20d%20s%20f\n" % (channel, "", sumOfWeights[channel]))
                logger.debug("{:d}:{:>40.2f}".format(channel, sumOfWeights[channel]))
            fs.close()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-f", "--files",
                        #dest="files", default="/nfs/dust/atlas/user/danilo/hists_sr2416/inputSW_all.txt,/nfs/dust/atlas/user/danilo/hists_sr2416/inputSW_syst.txt,/nfs/dust/atlas/user/danilo/hists_sr2416/inputSW_pdf.txt",
                        #dest="files", default="inputSW_all.txt,inputSW_syst.txt,inputSW_pdf.txt,inputSW_systaf2.txt",
                        #dest="files", default="inputSW_pdf.txt",
                        #dest="files", default="inputSW_systaf2.txt",
                        dest="files", default = '',
                        help="Text file with list of input files.", metavar="FILELIST")
    parser.add_argument("-t", "--types",
                        #dest="types", default=",syst,pdf,systaf2",
                        #dest="types", default="pdf",
                        #dest="types", default="systaf2",
                        dest="types", default = '',
                        help="Categories they should be added in.", metavar="LIST")
    parser.add_argument("-s", "--suffix",
                        dest="suffix", default="_new",
                        #dest="suffix", default="_test",
                        help="Suffix to be added in the output file.", metavar="SUFFIX")

    options = parser.parse_args()
    main(options.files, options.types, options.suffix)
