#!/usr/bin/env python
import os
import helpers
import ROOT
import csv
import analysis
import reweighting
import systematics

# ROOT.ROOT.EnableImplicitMT(4) # Not sure if it works
logger = helpers.getLogger('TopNtupleAnalysis.makeHistograms')

def main(parallel = False):
    helpers.doPRW = not options.noPRW
    systematics.DO_PRW = not options.noPRW
    accept_prob = float(options.accept_prob)
    randGen = ROOT.TRandom3(4357)
    do_tree = options.do_tree
    ROOT.TopNtupleAnalysis.initWrapper(options.data)

    pdfList = options.pdf.split(',')
    Xsec = {}

    InvsumOfWeights = {} # map of DSID to inversed sum of weights
    # TODO
    InvpdfSumOfWeights = {} # map of DSID to map of PDF variation names to inversed sum of weights

    InvsumOfWeightsAF2 = {} # map of DSID to sum of inversed weights

    fname_pat = "sumOfWeights{}_R21.txt"
    if not options.data:
        csv.register_dialect('sumOfWeightsDATA', delimiter = ' ', skipinitialspace = True, quoting = csv.QUOTE_NONE)
        for t in ('', 'syst', 'systaf2', 'pdf', 'wjpdf'):
            if options.pdf == '' and t in ('pdf', 'wjpdf'):
                continue
            try:
                fname = os.path.join(helpers.data_path, fname_pat.format(t))
                logger.info('Retrieve TOTAL MC weights from FILE("{}")'.format(fname))
                with open(fname, 'rb') as fs:
                    csv_reader = csv.DictReader(fs, dialect = 'sumOfWeightsDATA')
                    for r in csv_reader:
                        if r['pdfName'] == 'nominal': # nominal for PDF variation sample
                            if t == 'systaf2':
                                InvsumOfWeightsAF2[int(r['channel'])] = 1./float(r['SumOfWeights'])
                            else:
                                InvsumOfWeights[int(r['channel'])] = 1./float(r['SumOfWeights'])
                        else:
                            InvpdfSumOfWeights.setdefault(r['channel'], {}).setdefault(r['pdfName'], {})[r['pdfNumber']] = 1./float(r['SumOfWeights'])
            except IOError:
                logger.warn('FILE("{}") not found.'.format(fname))
        if {} == InvsumOfWeights == InvpdfSumOfWeights == InvsumOfWeightsAF2:
            raise IOError('TotalMCWeights files not found. Did you create them first?\nUse samples.write_totalweight_of_samples() to create TotalMCWeights files.')

    logger.info("Loading xsec.")
    helpers.loadXsec(Xsec, "dev/AnalysisTop/TopDataPreparation/XSection-MC15-13TeV.data")
    Xsec[0] = 0 # No idea why there are these events in dijets samples @yu-heng

    # check if there is any W+jets sample there
    isWjets = False
    doEWK = False
    isTtbar = False
    isSingleTop = False

    @helpers.lru_cache(maxsize=100)
    def _common_mc_weight(mc_weight, channel, suffix):
        weight = 1
        if not (isWjets and options.systs == 'pdf' and 'pdf_' in suffix): # use internal weights in this case
            weight *= mc_weight
        weight *= Xsec[channel]
        if options.systs != 'pdf': #'pdf_' in suffix:
            if not options.af2:
                try:
                    weight *= InvsumOfWeights[channel]
                except:
                    raise NameError('Could not find <DSID: %s> in DICT("sumOfWeights").' % channel)
            else:
                try:
                    weight *= InvsumOfWeightsAF2[channel]
                except:
                    raise NameError('Could not find <DSID: %s> in DICT("sunOfWeightsAF2")' % channel)      
        else:
            if not 'pdf_' in suffix:
                weight *= InvsumOfWeights[channel]
            else:
                pdfName, pdfNumber = suffix.split('_', 1)[1].rsplit('_', 1)
                try:
                    weight *= InvpdfSumOfWeights[channel][pdfName][int(pdfNumber)]
                except:
                    raise NameError('Could not find <DSID: %s> in DICT("pdfSumOfWeights").' % channel)
        return weight

    logger.info("Loading first event")
    mt_load = ROOT.TChain("nominal")
    sel = mt_load
    helpers.addFilesInChain(mt_load, options.files)

    mt_load.GetEntry(0)
    if sel.mcChannelNumber in helpers.listWjets22:
        isWjets = True
    if sel.mcChannelNumber in [410000, 301528, 301529, 301530, 301531, 301532]:
        isTtbar = True
    if sel.mcChannelNumber in [410011, 410012, 410013, 410014, 410015, 410016, 410025, 410026]:
        isSingleTop = True
    if options.ttbar_high_order == 'Rel20EWK':
        if (sel.mcChannelNumber not in reweighting.EWKCorrection.RUN_NUMBERS):
            options.ttbar_high_order = 'none'
    elif options.ttbar_high_order == 'NNLOQCDNLOEWK':
        if (sel.mcChannelNumber not in reweighting.TTbarNNLOReweighting.RUN_NUMBERS):
            options.ttbar_high_order = 'none'

    # systematics list
    systList = systematics.get_systs(options.systs, isTtbar, isSingleTop, isWjets, options.EFT, pdfList, InvpdfSumOfWeights, options.ttbar_high_order, analysis = options.analysis)
    systgroups = list(systematics.grouped_systs(systList))
    if '\;' in options.output:
        logger.warn('The "-o <channel1>,<ouput_fname1>\;<channel2>,<ouput_fname2>..." syntax is deprecated.\nPlease use the "-o <channel1>:<ouput_fname1>, [[-o <channel2>:<ouput_fname2>] -o ...]" syntax.', DeprecationWarning)
        channels = helpers.output_expr_reader_old(options.output)
    else:
        channels = dict(helpers.output_expr_reader_new(options.output))
    # Use default top-tagger if top-tagger is not set for this channel
    for ch in channels.keys():
        if len(ch) == 1:
            channels[ch + (options.top_tagger, )] = channels.pop(ch)
        if len(ch) == 2:
            channels[ch + (options.bot_tagger, )] = channels.pop(ch)
        if len(ch) == 3:
            channels[ch + ('', )] = channels.pop(ch)


    analysisCode = {}
    #print "Systematics: ", histSuffixes
    #print "To loop over: ", systList
    anaClass = getattr(analysis, options.analysis)
    KKgluonWidth = -1
    eftLambda = -1
    eftCvv = 0
    scalarMH   = -1
    scalarMA   = -1
    scalarSBA  = -999
    scalarTANB = -1
    scalarTYPE = -1
    if options.KKgluon != "":
        KKgluonWidth = float(options.KKgluon.split(",")[0])
    if options.EFT != "":
        eftStr = options.EFT.split(",")
        eftLambda = float(eftStr[0])
        eftCvv = float(eftStr[1])
        ROOT.TopNtupleAnalysis.initPDF(options.pdfForWeight)
        ROOT.TopNtupleAnalysis.setEFT(eftLambda, eftCvv)
    if options.SCALAR != "":
        scalarStr  = options.SCALAR.split(",")
        scalarMH   = float(scalarStr[0])
        scalarMA   = float(scalarStr[1])
        scalarSBA  = float(scalarStr[2])
        scalarTANB = float(scalarStr[3])
        scalarTYPE = int(scalarStr[4])
        ROOT.TopNtupleAnalysis.initPDF(options.pdfForWeight)
        helpers.init2HDM(scalarMH,scalarMA,scalarSBA,scalarTANB,scalarTYPE)
        logger.info("2HDM setup: mH=%g, mA=%g, sba=%g, tanb=%g, type=%g" % (scalarMH, scalarMA, scalarSBA, scalarTANB, scalarTYPE))
    for k in channels:
        ch, top_tagger, bot_tagger, aux_selector = k
        analysisCode[k] = anaClass(ch, systgroups, channels[k])
        analysisCode[k].doTree = do_tree
        analysisCode[k].keep = options.WjetsHF
        analysisCode[k].applyQCD = False
        analysisCode[k].ttbarHighOrder = options.ttbar_high_order
        if isinstance(analysisCode[k], analysis.AnaTtresFH):
            analysisCode[k].blinded = options.blinding
        if options.qcd != "False":
            analysisCode[k].applyQCD = options.qcd
        if options.noMttSlices:
            analysisCode[k].noMttSlices = True
        if options.applyMET != "":
            analysisCode[k].applyMET = float(options.applyMET)
        if options.KKgluon != "":
            analysisCode[k].KKgluonWidth = KKgluonWidth
        if options.DM:
            analysisCode[k].DMMass = True
        else:
            analysisCode[k].DMMass = False
        if options.EFT != "":
            eftStr = options.EFT.split(",")
            analysisCode[k].eftLambda = eftLambda
            analysisCode[k].eftCvv = eftCvv
        if options.SCALAR != "":
            scalarStr = options.SCALAR.split(",")
            analysisCode[k].scalarMH   = scalarMH
            analysisCode[k].scalarMA   = scalarMA
            analysisCode[k].scalarSBA  = scalarSBA
            analysisCode[k].scalarTANB = scalarTANB
            analysisCode[k].scalarTYPE = scalarTYPE
        analysisCode[k].set_top_tagger(top_tagger)
        analysisCode[k].set_bot_tagger(bot_tagger)
        analysisCode[k].set_aux_selector(aux_selector)
        if isinstance(analysisCode[k], analysis.AnaTtresSL):
            if ch.startswith('r') or ch.startswith('ovr'):
                analysisCode[k].set_TtresChi2()
        logger.info('({:^6},{:^6},{:^12}): {}'.format(ch.strip(), top_tagger, bot_tagger, channels[k]))

    isFirstEvent = True

    for systgroup in systgroups:
        treeName = systgroup.tree # systematic name is the same as the TTree name

        sel = ROOT.TChain(treeName)

        helpers.addFilesInChain(sel, options.files)
        if parallel:
            sel.SetImplicitMT(True)
        ent = options.nevents or sel.GetEntries()
        ent_length = len(str(ent))
        for k in xrange(ent):
            if options.data and accept_prob > 0:
                randomNumber = randGen.Uniform(0, 1)
                if randomNumber > accept_prob:
                    continue
            sel.GetEntry(k)

            for syst in systgroup.systematics:
                suffix = syst.hist_suffix
                if k % 10000 == 0:
                    logger.info("(tree = {:^10}, syst = {:^5}) Entry: {{:>{}}} / {}".format('<'+treeName+'>', '<'+suffix+'>', ent_length, ent).format(k))
                if isFirstEvent:
                    if options.ttbar_high_order == 'NNLOQCDNLOEWK':
                        reweighting.TTbarNNLOReweighting.init(sel.mcChannelNumber)
                    else:
                        reweighting.EWKCorrection.init(sel.mcChannelNumber)
                        reweighting.NNLOReweighting.init(sel.mcChannelNumber)
                    isFirstEvent = False

                # common part of the weight
                if options.data:
                    weight = 1.
                else:
                    weight = _common_mc_weight(sel.weight_mc, sel.mcChannelNumber, suffix if 'pdf_' in suffix else '')

                for ana in analysisCode.itervalues():
                    if not ana.selectChannel(sel, suffix):
                        continue
                    weight_reco = ana.getWeight(sel, syst)
                    if options.systs == 'pdf' and 'pdf_' in suffix and not isWjets: # for W+jets, use internal weights
                        pdfName = (suffix.split('_', 1)[1]).rsplit('_', 1)[0]
                        pdfNumber = int(suffix.rsplit('_', 1)[1])
                        pdfAttr = getattr(sel, pdfName)
                        weight_reco *= pdfAttr[pdfNumber]
                    elif (isWjets and options.systs == 'pdf' and 'pdf_' in suffix): # use internal weights in this case
                        pdfName = (suffix.split('_', 1)[1]).rsplit('_', 1)[0]
                        pdfNumber = int(suffix.rsplit('_', 1)[1])
                        wjpdfList = [7]+range(11, 110+1)
                        weight_reco *= sel.mc_generator_weights[wjpdfList[pdfNumber]]
                    ana.run(sel, suffix, weight*weight_reco, weight)

            for ana in analysisCode.itervalues():
                ana.unlock()

    for k in analysisCode:
        analysisCode[k].end()

if __name__ == "__main__":
    import argparse
    class AppendActionCleanDefault(argparse._AppendAction):
        def __init__(self, *args, **kwargs):
            super(argparse._AppendAction, self).__init__(*args,**kwargs)
            self.index = 0
        def __call__(self, parser, namespace, values, option_string = None):
            items = argparse._copy.copy(argparse._ensure_value(namespace, self.dest, [])) if self.index else []
            if values:
                self.index += 1
                items.append(values)
                setattr(namespace, self.dest, items)
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter, add_help=False)

    parser.add_argument("-d", "--data",
                        action="store_true",
                        dest="data",
                        help="Is this data?")
    parser.add_argument("-f", "--files",
                        dest="files", default=["input.txt"],
                        action = AppendActionCleanDefault,
                        nargs = '?',
                        help="Text file with list of input files.",
                        metavar="FILE")
    parser.add_argument("-s", "--systs",
                        dest="systs",
                        default="nominal",
                        help="Comma-separated list of systematic uncertainties in TTrees in the input file. Use 'all' to run over all the default ones.",
                        metavar="SYSTEMATICS")
    parser.add_argument("-W", "--WjetsHF",
                        dest="WjetsHF",
                        default="all",
                        help="Which W+jets HF to keep. Can be all, bb, cc, bbcc, c or l.",
                        metavar="FLAVOURS")
    parser.add_argument("-P", "--pdf",
                        dest="pdf",
                        default="",
                        help="Which PDFs to reweight to.",
                        metavar="PDFS")
    parser.add_argument("-Q", "--qcd",
                        dest="qcd",
                        default="False",
                        help="Apply QCD weights?",
                        metavar="CHANNEL")
    # parser.add_argument("--no-EWKCorrection",
    #                     action="store_true",
    #                     help="Don't do Electroweak correction when running SM ttbar sample including the following:\n"
    #                         +str(reweighting.EWKCorrection.RUN_NUMBERS))
    parser.add_argument("--ttbar-high-order",
                        default =  'NNLOQCDNLOEWK',
                        choices = ['Rel20EWK', 'NNLOQCDNLOEWK', 'none'],
                        help = 'High Order Correction applied to registered ttbar sample.')
    parser.add_argument("-N", "--noMttSlices",
                        dest="noMttSlices",
                        action="store_true",
                        help="If set, stop vetoing high mtt ( > 1.1TeV) events in inclusive ttbar sample [410000, 410470, 410471].\n"
                            +"This is mainly for running it together with mtt sliced ttbar samples")
    parser.add_argument("-M", "--applyMET",
                        dest="applyMET",
                        default="0",
                        help="Extra MET cut to be applied.",
                        metavar="CUT")
    parser.add_argument("-S", "--SCALAR",
                        dest="SCALAR",
                        default="",
                        help="Parameters to use when reweighting LO ttbar+jets to a scalar 2HDM setup with a configuration of {mH,mA,sin(b-a), tan(b) and the model type}.", metavar="MH,MA,SBA,TANB,TYPE")
    parser.add_argument("-E", "--EFT",
                        dest="EFT",
                        default="",
                        help="Parameters to use when reweighting LO ttbar to an EFT setup with a lambda and cvv configuration. Set lambda to a negative value to disable this.", metavar="LAMBDA,CVV")
    parser.add_argument("-K", "--KKgluon",
                        dest="KKgluon",
                        default="",
                        help="Parameters to use when reweighting KK gluon samples. The parameter should be the destination width as an integer, which is a percentage of the mass.", metavar="WIDTH")
    parser.add_argument("-D", "--DM",
                        action='store_true',
                        dest="DM",
                        help="Do Zprime to DM reweighting?")
    parser.add_argument("-p", "--pdfForWeight",
                        dest="pdfForWeight",
                        default="NNPDF30_nlo_as_0118", # this is the PDF used for LO, so it should be used for the alphaS
                        help="PDF to use to get alpha_S when doing either the EFT or the scalar model reweighting.",
                        metavar="PDF")
    parser.add_argument("-F", "--af2",
                        action='store_true',
                        dest="af2",
                        help="Is this AF2?")
    parser.add_argument("-w", "--noPRW",
                        action='store_true',
                        dest="noPRW",
                        help="Don't do pile up reweighting.")
    parser.add_argument("-u", "--accept_prob",
                        dest="accept_prob",
                        default=1,
                        help="Probability of accepting an event. Factor to use when dropping events in data to reduce luminosity available.",
                        metavar="FLOAT")
    parser.add_argument('-t', '--top-tagger',
                        default='good',
                        help='"GLOBAL" Boosted top tagger which will applied to the large-R jet for the hadronic-top reconstruction in the boost selection. Simple logical operation are supported. ONLY WORK IF YOU DON\'T USE ANY TOP-TAGGER IN THE _OUTPUT_ SELECTIONS.')
    parser.add_argument('-b', '--bot-tagger',
                        default='MV2c10_70',
                        help='"GLOBAL" b-quark tagger. ONLY WORK IF YOU DON\'T USE ANY BOT-TAGGER IN THE _OUTPUT_ SELECTIONS.')
    parser.add_argument('--nevents',
                        default = None,
                        type = int,
                        help='Number of events are going to be processed for test-only purpose.')
    parser.add_argument('--do-tree',
                        action='store_true',
                        help='Make a mini-tree.')

    parent_parser = argparse.ArgumentParser(formatter_class = argparse.ArgumentDefaultsHelpFormatter, parents = [parser]) 
    subparsers = parent_parser.add_subparsers(title = 'SL/FH ttbar resonances anaylsis', dest = 'analysis')
    SLttres_parser = subparsers.add_parser('AnaTtresSL', parents = [parser], formatter_class = argparse.ArgumentDefaultsHelpFormatter, help = 'Semi-leptonic ttbar resonances anaylsis')
    SLttres_parser.add_argument("-o", "--output",
                        dest="output",
                        default = ["(re,good,MV2c10_70):hist_re.root",
                                   "(rmu,good,MV2c10_70):hist_rmu.root",
                                   "(be,good,MV2c10_70):hist_be.root",
                                   "(bmu,good,MV2c10_70):hist_bmu.root"],
                        action = AppendActionCleanDefault,
                        nargs = '?',
                        help='You can run more than 1 channels in the same time. The syntax is "-o (<topo><lep>[<b-cat>], [<top-tagger>, [<bot-tagger>]]):<output_fname> [-o ... [-o ...]]". See Also: `--top-tagger`',
                        metavar="FILES")
    FHttres_parser = subparsers.add_parser('AnaTtresFH', parents = [parser], formatter_class = argparse.ArgumentDefaultsHelpFormatter, help = 'Full-Hadronic ttbar resonances anaylsis')
    FHttres_parser.add_argument("-o", "--output",
                        dest="output",
                        default = ["(bFH,good,MV2c10_70):hist_bFH.root"],
                        action = AppendActionCleanDefault,
                        nargs = '?',
                        help='You can run more than 1 channels in the same time. The syntax is "-o (<topo><lep>[<b-cat>], [<top-tagger>, [<bot-tagger>]]):<output_fname> [-o ... [-o ...]]". See Also: `--top-tagger`',
                        metavar="FILES")
    FHttres_parser.add_argument('--blinding',
                        action='store_true',
                        help='Invert the deltaY cut')
    options = parent_parser.parse_args()
    logger.info("-> Calling main")
    helpers.initialise_binds()
    main()
    logger.info("The end.")
