#!/usr/bin/env python
import ROOT
import os
import helpers
import itertools
logger = helpers.getLogger('TopNtupleAnalysis.sumWeights')

pdfList = ['PDF4LHC15_nlo_30']
wjpdfList = [7]+range(11, 110+1)

def sumWeights(files, types, suffix, mode = 'auto', runNumber = 'ALL', periodFraction = 1):
    assert len(files) == len(types), '"types" must be of the same size of "files"'
    ret = []
    l_fmt = (' '*5).join(['{channel:>20}', '{pdfName:>20}', '{pdfNumber:>20}', '{totalEvents:>20}', '{SumOfWeights:>20}', '{runNumber:>20}', '{periodFraction:>20}', '{nFiles:>20}'])
    l_fmt += '\n'
    header = l_fmt.format(**{'channel': 'channel',
                             'pdfName': 'pdfName',
                             'pdfNumber': 'pdfNumber',
                             'totalEvents': 'totalEvents',
                             'SumOfWeights': 'SumOfWeights',
                             'runNumber': 'runNumber',
                             'periodFraction': 'periodFraction',
                             'nFiles': 'nFiles'})
    for f, t in zip(files, types):
        lines = []
        if t == "pdf":
            pdfSumOfWeights = {} # map of DSID to map of PDF variation names to sum of weights
            pdfTotalEvents = {}
            nFiles = {}
            t_pdfSumWeights = ROOT.TChain("PDFsumWeights")
            helpers.addFilesInChain(t_pdfSumWeights, [f])
            for k in range(0, t_pdfSumWeights.GetEntries()):
                t_pdfSumWeights.GetEntry(k)
                if not t_pdfSumWeights.dsid in pdfSumOfWeights:
                    pdfSumOfWeights[t_pdfSumWeights.dsid] = {}
                    pdfTotalEvents[t_pdfSumWeights.dsid] = {}
                    nFiles[t_pdfSumWeights.dsid] = {}
                for l in pdfList:
                    if l not in pdfSumOfWeights[t_pdfSumWeights.dsid]:
                        pdfSumOfWeights[t_pdfSumWeights.dsid][l] = []
                        pdfTotalEvents[t_pdfSumWeights.dsid][l] = []
                        nFiles[t_pdfSumWeights.dsid][l] = []
                    pdfAttr = getattr(t_pdfSumWeights, l)
                    if len(pdfSumOfWeights[t_pdfSumWeights.dsid][l]) == 0:
                        pdfSumOfWeights[t_pdfSumWeights.dsid][l] = [0]*len(pdfAttr)
                        pdfTotalEvents[t_pdfSumWeights.dsid][l] = [0]*len(pdfAttr)
                        nFiles[t_pdfSumWeights.dsid][l] = [0]*len(pdfAttr)
                    for m in range(0, len(pdfAttr)):
                        pdfSumOfWeights[t_pdfSumWeights.dsid][l][m] += pdfAttr[m]
                        pdfTotalEvents[t_pdfSumWeights.dsid][l][m] += t_pdfSumWeights.totalEvents
                        nFiles[t_pdfSumWeights.dsid][l][m] += 1

            for channel in sorted(pdfSumOfWeights.keys()):
                for pdfName in sorted(pdfSumOfWeights[channel].keys()):
                    for pdfNumber in range(0, len(pdfSumOfWeights[channel][pdfName])):
                        entry = {'channel': channel,
                                 'pdfName': pdfName,
                                 'pdfNumber': pdfNumber,
                                 'totalEvents': pdfTotalEvents[channel][pdfName][pdfNumber],
                                 'SumOfWeights':pdfSumOfWeights[channel][pdfName][pdfNumber],
                                 'runNumber': runNumber,
                                 'periodFraction': '{:.5e}'.format(periodFraction),
                                 'nFiles': nFiles[channel][pdfName][pdfNumber],
                                 }
                        lines.append(l_fmt.format(**entry))
                        logger.debug(lines[-1])
                        ret.append(entry)

        elif t == "wjpdf":
            pdfName = "NNPDF30_nnlo_as_0118"
            wjpdfSumOfWeights = {} # map of DSID to map of PDF variation names to sum of weights
            wjpdfTotalEvents = {}
            wjpdfnFiles = {}
            t_wjpdfSumWeights = ROOT.TChain("sumWeights")
            helpers.addFilesInChain(t_wjpdfSumWeights, [f])
            for k in range(0, t_wjpdfSumWeights.GetEntries()):
                t_wjpdfSumWeights.GetEntry(k)
                if not t_wjpdfSumWeights.dsid in wjpdfSumOfWeights:
                    wjpdfSumOfWeights[t_wjpdfSumWeights.dsid] = {}
                    wjpdfTotalEvents[t_wjpdfSumWeights.dsid] = {}
                    wjpdfnFiles[t_wjpdfSumWeights.dsid] = {}
                pdfAttr = t_wjpdfSumWeights.totalEventsWeighted_mc_generator_weights
                for l in range(0, len(wjpdfList)):
                    if l not in wjpdfSumOfWeights[t_wjpdfSumWeights.dsid]:
                        wjpdfSumOfWeights[t_wjpdfSumWeights.dsid][l] = 0
                        wjpdfTotalEvents[t_wjpdfSumWeights.dsid][l] = 0
                        wjpdfnFiles[t_wjpdfSumWeights.dsid][l] = 0
                    value = float(pdfAttr[wjpdfList[l]])
                    #if value < -200000: print "Read ", value, " in item ", wjpdfList[l], " in file ", t_wjpdfSumWeights.GetCurrentFile().GetName()
                    #if value > 200000: print "Read ", value, " in item ", wjpdfList[l], " in file ", t_wjpdfSumWeights.GetCurrentFile().GetName()
                    if (value > 60000 or value < -60000) and l in [42]: 
                        logger.info(" ".join("Read ", value, " in item ", wjpdfList[l], " in file ", t_wjpdfSumWeights.GetCurrentFile().GetName()))
                    wjpdfSumOfWeights[t_wjpdfSumWeights.dsid][l] += value
                    wjpdfTotalEvents[t_wjpdfSumWeights.dsid][l] += t_wjpdfSumWeights.totalEvents
                    wjpdfnFiles[t_wjpdfSumWeights.dsid][l] += 1

            for channel in sorted(wjpdfSumOfWeights.iterkeys()):
                for pdfNumber in range(0, len(wjpdfSumOfWeights[channel])):
                    entry = {'channel': channel,
                             'pdfName': pdfName,
                             'pdfNumber': pdfNumber,
                             'totalEvents': wjpdfTotalEvents[channel][pdfNumber],
                             'SumOfWeights': wjpdfSumOfWeights[channel][pdfNumber],
                             'runNumber': runNumber,
                             'periodFraction': '{:.5e}'.format(periodFraction),
                             'nFiles': wjpdfnFiles[channel][pdfNumber]
                             }
                    lines.append(l_fmt.format(**entry))
                    logger.debug(lines[-1])
                    ret.append(entry)

        nFiles = {}
        sumOfWeights = {} # map of DSID to sum of weights
        totalEvents = {}
        totalEvents_mcgen = {}
        t_sumWeights = ROOT.TChain("sumWeights")
        helpers.addFilesInChain(t_sumWeights, [f])

        for k in range(0, t_sumWeights.GetEntries()):
            t_sumWeights.GetEntry(k)
            if not t_sumWeights.dsid in sumOfWeights:
                sumOfWeights[t_sumWeights.dsid] = 0
                totalEvents[t_sumWeights.dsid] = 0
                nFiles[t_sumWeights.dsid] = 0
                if t == "ttgen":
                    if t_sumWeights.dsid != 410470:
                        logger.error('DSID = %d. This is not a registered ttbar ntuples.'%t_sumWeights.dsid )
                        return 
                    totalEvents_mcgen[t_sumWeights.dsid] = {}
            if t_sumWeights.dsid in xrange(361020, 361033):
                sumOfWeights[t_sumWeights.dsid] += t_sumWeights.totalEvents
            else:
                sumOfWeights[t_sumWeights.dsid] += t_sumWeights.totalEventsWeighted
            totalEvents[t_sumWeights.dsid] += t_sumWeights.totalEvents
            if t == "ttgen":
                for l in helpers.ttgen_uncert.keys():
                    if l not in totalEvents_mcgen[t_sumWeights.dsid]:
                        totalEvents_mcgen[t_sumWeights.dsid][l] = 0
                    totalEvents_mcgen[t_sumWeights.dsid][l] += t_sumWeights.totalEventsWeighted_mc_generator_weights[helpers.ttgen_uncert[l]]

            nFiles[t_sumWeights.dsid] += 1
        for channel in sorted(sumOfWeights.iterkeys()):
            entry = {'channel': channel,
                     'pdfName': 'nominal',
                     'pdfNumber': -1,
                     'totalEvents': totalEvents[channel],
                     'SumOfWeights': sumOfWeights[channel],
                     'runNumber': runNumber,
                     'periodFraction': '{:.5e}'.format(periodFraction),
                     'nFiles': nFiles[channel]
                     }
            lines.append(l_fmt.format(**entry))
            logger.debug(lines[-1])
            ret.append(entry)
            if t == "ttgen":
                for name,value in helpers.ttgen_uncert.items():
                    if 'tt_pdf'  in name:
                        pdf_number = int(name.replace('tt_pdf_', ''))
                    else:
                        pdf_number = -1
                    entry = {'channel': channel,
                             'pdfName': name,
                             'pdfNumber': pdf_number,
                             'totalEvents': totalEvents[channel],
                             'SumOfWeights': totalEvents_mcgen[channel][name],
                             'runNumber': runNumber,
                             'periodFraction': '{:.5e}'.format(periodFraction),
                             'nFiles': nFiles[channel]
                             }
                    lines.append(l_fmt.format(**entry))
                    logger.debug(lines[-1])
                    ret.append(entry)

        if mode != 'return':
            sumOfWeights_file = os.path.join(helpers.data_path, "sumOfWeights%s%s.txt") % (t, suffix)
            if not os.path.exists(sumOfWeights_file):
                logger.info('Creating new sumOfWeights file: FILE("%s")', sumOfWeights_file)
                if mode == 'auto':
                    mode = 'w'
                if mode == 'a':
                    logger.warn('Headers will not be correctly written in the append mode.')
            else:
                logger.info('Updating existing sumOfWeights file: FILE("%s")', sumOfWeights_file)
                if mode == 'auto':
                    mode = 'a'
            if mode == 'w':
                lines.insert(0, header)
            assert mode in ['a', 'w']
            with open(sumOfWeights_file, mode) as f:
                f.writelines(lines)
    return ret


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
                        dest="suffix", default="_R21",
                        #dest="suffix", default="_test",
                        help="Suffix to be added in the output file.", metavar="SUFFIX")
    parser.add_argument('-m', '--mode',
                        default = 'auto',
                        choices = ['auto', 'a', 'w'])
    parser.add_argument('-r', '--runNumber',
                        default = 'ALL',
                        help = 'A runNumber range to control contributed fraction of different MC samples. e.g. For mc16a "276262-284484"')
    parser.add_argument('--periodFraction',
                        default = 1,
                        type = float,
                        help = 'Contributed fraction of the MC samples of the given runNumber range'
                        )

    options = parser.parse_args()
    sumWeights(options.files.split(','), options.types.split(','), options.suffix, options.mode, options.runNumber, options.periodFraction)
