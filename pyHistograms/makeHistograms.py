#!/usr/bin/env python
import os
import helpers
from helpers import *
# from ROOT import *
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import analysis

run_path = os.path.join(os.path.dirname(__file__))
root_path = os.path.join(run_path, os.pardir)
data_path = os.path.join(root_path, 'share')
def main():
    helpers.doPRW = not options.noPRW
    accept_prob = float(options.accept_prob)
    randGen = ROOT.TRandom3(4357)

    print "-> Initialising wrapper"
    ROOT.initWrapper(options.data)

    pdfList = options.pdf.split(',')
    Xsec = {}

    sumOfWeights = {} # map of DSID to sum of weights
    # TODO
    pdfSumOfWeights = {} # map of DSID to map of PDF variation names to sum of weights

    sumOfWeightsAF2 = {} # map of DSID to sum of weights

    if not options.data:
        if options.pdf != "":
            pfs = open(os.path.join(data_path, "sumOfWeightspdf_new.txt"))
            for line in pfs.readlines():
                line_spl = line.split()
                if not int(line_spl[0]) in pdfSumOfWeights:
                    pdfSumOfWeights[int(line_spl[0])] = {}
                if not line_spl[1] in pdfSumOfWeights[int(line_spl[0])]:
                    pdfSumOfWeights[int(line_spl[0])][line_spl[1]] = {}
                if line_spl[1] == "nominal": # nominal for PDF variation sample
                    sumOfWeights[int(line_spl[0])] = float(line_spl[3])
                else:
                    pdfSumOfWeights[int(line_spl[0])][line_spl[1]][int(line_spl[2])] = float(line_spl[3])
            pfs.close()
            pfs = open(os.path.join(data_path, "sumOfWeightswjpdf_new.txt"))
            for line in pfs.readlines():
                line_spl = line.split()
                if not int(line_spl[0]) in pdfSumOfWeights:
                    pdfSumOfWeights[int(line_spl[0])] = {}
                if not line_spl[1] in pdfSumOfWeights[int(line_spl[0])]:
                    pdfSumOfWeights[int(line_spl[0])][line_spl[1]] = {}
                if line_spl[1] == "nominal": # nominal for PDF variation sample
                    sumOfWeights[int(line_spl[0])] = float(line_spl[3])
                else:
                    pdfSumOfWeights[int(line_spl[0])][line_spl[1]][int(line_spl[2])] = float(line_spl[3])
            pfs.close()
        else:
            fs = open(os.path.join(data_path, "sumOfWeights_new.txt"))
            for line in fs.readlines():
                line_spl = line.split()
                sumOfWeights[int(line_spl[0])] = float(line_spl[1])
            fs.close()
            fs = open(os.path.join(data_path, "sumOfWeightssyst_new.txt"))
            for line in fs.readlines():
                line_spl = line.split()
                sumOfWeights[int(line_spl[0])] = float(line_spl[1])
            fs.close()

            fs = open(os.path.join(data_path, "sumOfWeightssystaf2_new.txt"))
            for line in fs.readlines():
                line_spl = line.split()
                sumOfWeightsAF2[int(line_spl[0])] = float(line_spl[1])
            fs.close()

    #print pdfSumOfWeights

    print "Loading xsec."
    loadXsec(Xsec, os.path.join(root_path, "scripts/XSection-MC15-13TeV-ttres.data"))
    loadXsec(Xsec, os.path.join(root_path, "../TopDataPreparation/data/XSection-MC15-13TeV.data"))
    #loadXsec(Xsec, "../share/MC15c-SherpaWZ.data")

    # check if there is any W+jets sample there
    isWjets = False
    doEWK = False
    isTtbar = False
    isSingleTop = False

    print "Loading first event"
    mt_load = ROOT.TChain("nominal")
    sel = mt_load
    addFilesInChain(mt_load, options.files)

    mt_load.GetEntry(0)
    if sel.mcChannelNumber in helpers.listWjets22:
        isWjets = True
    if sel.mcChannelNumber in [410000, 301528, 301529, 301530, 301531, 301532]:
        isTtbar = True
    if sel.mcChannelNumber in [410011, 410012, 410013, 410014, 410015, 410016, 410025, 410026]:
        isSingleTop = True
    if sel.mcChannelNumber in helpers.listEWK:
        doEWK = True


    doQCD = False
    doRew = False
    doKKgluonRew = False
    doDMRew = False
    if options.qcd != "False":
        doQCD = True
    if options.EFT != '':
        doRew = True
    if options.KKgluon != '':
        doKKgluonRew = True
    if options.DM:
        doDMRew = True


    # systematics list
    if options.systs[0:3] == 'all':
        systList = []
        systList.append('nominal')
        systList.append('ttNNLO_seq__1up')
        systList.append('ttNNLO_seqExtended__1up')
        systList.append('ttNNLO_topPt__1up')
        systList.append('ttNNLO_topPtDiff__1up')
        systList.append('mttSlope')
        if isWjets:
            systList.append('CAallMCAsym')
            systList.append('wnorm__1up')
            systList.append('wnorm__1down')
            systList.append('wc__1up')
            systList.append('wc__1down')
            systList.append('wbb__1up')
            systList.append('wbb__1down')
            systList.append('wl__1up')
            systList.append('wl__1down')
            systList.append('ttgenup')
            systList.append('ttgendw')
            systList.append('ttpsup')
            systList.append('ttpsdw')
            systList.append('ttpspp8up')
            systList.append('ttpspp8dw')
            systList.append('ttpsoldup')
            systList.append('ttpsolddw')
            systList.append('ttisrfsrup')
            systList.append('ttisrfsrdw')
            systList.append('2to3ex')
            for k in range(0, 30+1):
                systList.append('pdf_PDF4LHC15_nlo_30_%d' % (k))
            systList.append('elMisIDpos_up')
            systList.append('elMisIDpos_down')
            systList.append('ttEWK__1up')
            systList.append('ttEWK__1down')
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
        if isWjets or isTtbar:
            systList.append('ttxsecup')
            systList.append('ttxsecdw')
        if isWjets or isSingleTop:
            systList.append('singletopup')
            systList.append('singletopdw')
        systList.extend(weightChangeSystematics)
        systList.remove('')
        if doEWK:
            systList.append('ttEWK__1up')
            systList.append('ttEWK__1down')
        if options.EFT != '':
            systList.append("eftScale__1up")
            systList.append("eftScale__1down")
        systematics  = 'EG_RESOLUTION_ALL__1down,EG_RESOLUTION_ALL__1up,EG_SCALE_ALL__1down,EG_SCALE_ALL__1up'
        systematics += ',JET_JER_SINGLE_NP__1up'
        # 3NP for the akt4 jets
        #systematics += ',JET_NPScenario1_JET_EtaIntercalibration_NonClosure__1down,JET_NPScenario1_JET_EtaIntercalibration_NonClosure__1up'
        #systematics += ',JET_NPScenario1_JET_GroupedNP_2__1down,JET_NPScenario1_JET_GroupedNP_2__1up,JET_NPScenario1_JET_GroupedNP_3__1down,JET_NPScenario1_JET_GroupedNP_3__1up,JET_NPScenario1_JET_GroupedNP_1__1up,JET_NPScenario1_JET_GroupedNP_1__1down'
        # 19 NP for the akt4 jets
        #systematics += ',JET_21NP_JET_EffectiveNP_3__1down,JET_21NP_JET_EffectiveNP_6restTerm__1up,JET_21NP_JET_EffectiveNP_6restTerm__1down,JET_21NP_JET_Pileup_RhoTopology__1down,JET_21NP_JET_Pileup_OffsetNPV__1down,JET_21NP_JET_BJES_Response__1up,JET_21NP_JET_Pileup_RhoTopology__1up,JET_21NP_JET_EtaIntercalibration_TotalStat__1up,JET_21NP_JET_EffectiveNP_1__1up,JET_21NP_JET_EtaIntercalibration_NonClosure__1up,JET_21NP_JET_EffectiveNP_1__1down,JET_21NP_JET_BJES_Response__1down,JET_21NP_JET_Flavor_Response__1up,JET_21NP_JET_Pileup_OffsetMu__1up,JET_21NP_JET_EffectiveNP_4__1down,JET_21NP_JET_EffectiveNP_5__1up,JET_21NP_JET_EffectiveNP_5__1down,JET_21NP_JET_EffectiveNP_2__1down,JET_21NP_JET_PunchThrough_MC15__1down,JET_21NP_JET_EffectiveNP_2__1up,JET_21NP_JET_SingleParticle_HighPt__1up,JET_21NP_JET_EffectiveNP_3__1up,JET_21NP_JET_SingleParticle_HighPt__1down,JET_21NP_JET_Flavor_Composition__1up,JET_21NP_JET_Pileup_PtTerm__1down,JET_21NP_JET_PunchThrough_MC15__1up,JET_21NP_JET_Flavor_Response__1down,JET_21NP_JET_EtaIntercalibration_Modelling__1down,JET_21NP_JET_Flavor_Composition__1down,JET_21NP_JET_Pileup_PtTerm__1up,JET_21NP_JET_EtaIntercalibration_Modelling__1up,JET_21NP_JET_EffectiveNP_4__1up,JET_21NP_JET_Pileup_OffsetMu__1down,JET_21NP_JET_EtaIntercalibration_TotalStat__1down,JET_21NP_JET_Pileup_OffsetNPV__1up,JET_21NP_JET_EtaIntercalibration_NonClosure__1down'
        systematics += ',JET_21NP_JET_EffectiveNP_3__1down,JET_21NP_JET_Pileup_RhoTopology__1down,JET_21NP_JET_Pileup_OffsetNPV__1down,JET_21NP_JET_BJES_Response__1up,JET_21NP_JET_Pileup_RhoTopology__1up,JET_21NP_JET_EtaIntercalibration_TotalStat__1up,JET_21NP_JET_EffectiveNP_1__1up,JET_21NP_JET_EtaIntercalibration_NonClosure__1up,JET_21NP_JET_EffectiveNP_1__1down,JET_21NP_JET_BJES_Response__1down,JET_21NP_JET_Flavor_Response__1up,JET_21NP_JET_Pileup_OffsetMu__1up,JET_21NP_JET_EffectiveNP_4__1down,JET_21NP_JET_EffectiveNP_5__1up,JET_21NP_JET_EffectiveNP_5__1down,JET_21NP_JET_EffectiveNP_2__1down,JET_21NP_JET_PunchThrough_MC15__1down,JET_21NP_JET_EffectiveNP_2__1up,JET_21NP_JET_SingleParticle_HighPt__1up,JET_21NP_JET_EffectiveNP_3__1up,JET_21NP_JET_SingleParticle_HighPt__1down,JET_21NP_JET_Flavor_Composition__1up,JET_21NP_JET_Pileup_PtTerm__1down,JET_21NP_JET_PunchThrough_MC15__1up,JET_21NP_JET_Flavor_Response__1down,JET_21NP_JET_EtaIntercalibration_Modelling__1down,JET_21NP_JET_Flavor_Composition__1down,JET_21NP_JET_Pileup_PtTerm__1up,JET_21NP_JET_EtaIntercalibration_Modelling__1up,JET_21NP_JET_EffectiveNP_4__1up,JET_21NP_JET_Pileup_OffsetMu__1down,JET_21NP_JET_EtaIntercalibration_TotalStat__1down,JET_21NP_JET_Pileup_OffsetNPV__1up,JET_21NP_JET_EtaIntercalibration_NonClosure__1down'
        systematics += ',JET_21NP_JET_EffectiveNP_7__1down,JET_21NP_JET_EffectiveNP_7__1up,JET_21NP_JET_EffectiveNP_6__1up,JET_21NP_JET_EffectiveNP_6__1down,JET_21NP_JET_EffectiveNP_8restTerm__1up,JET_21NP_JET_EffectiveNP_8restTerm__1down'
        systematics += ',MET_SoftTrk_ResoPara,MET_SoftTrk_ResoPerp,MET_SoftTrk_ScaleDown,MET_SoftTrk_ScaleUp'
        # muon scale and resolution
        systematics += ',MUON_SAGITTA_RESBIAS__1up,MUON_SAGITTA_RHO__1up,MUON_SAGITTA_RHO__1down,MUON_SAGITTA_RESBIAS__1down'
        systematics += ',MUON_ID__1down,MUON_ID__1up,MUON_MS__1down,MUON_MS__1up,MUON_SCALE__1down,MUON_SCALE__1up'
        # strong systematics for large-R jets
        systematics += ',LARGERJET_Strong_JET_Comb_Modelling_All__1up,LARGERJET_Strong_JET_Comb_Modelling_All__1down,LARGERJET_Strong_JET_Comb_Baseline_All__1down,LARGERJET_Strong_JET_Comb_Baseline_All__1up,LARGERJET_Strong_JET_Comb_Tracking_All__1down,LARGERJET_Strong_JET_Comb_Tracking_All__1up,LARGERJET_Strong_JET_Comb_TotalStat_All__1down,LARGERJET_Strong_JET_Comb_TotalStat_All__1up'
        # medium systematics for large-R jets
        systematics += ',LARGERJET_Medium_JET_Comb_Baseline_Kin__1up,LARGERJET_Medium_JET_Comb_Baseline_Kin__1down,LARGERJET_Medium_JET_Comb_Modelling_Kin__1up,LARGERJET_Medium_JET_Comb_Modelling_Kin__1down,LARGERJET_Medium_JET_Comb_TotalStat_Kin__1up,LARGERJET_Medium_JET_Comb_TotalStat_Kin__1down,LARGERJET_Medium_JET_Comb_Tracking_Kin__1up,LARGERJET_Medium_JET_Comb_Tracking_Kin__1down,LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1up,LARGERJET_Medium_JET_Rtrk_Baseline_Sub__1down,LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1up,LARGERJET_Medium_JET_Rtrk_Modelling_Sub__1down,LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1up,LARGERJET_Medium_JET_Rtrk_TotalStat_Sub__1down,LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1up,LARGERJET_Medium_JET_Rtrk_Tracking_Sub__1down'
        # correlate large-R jets and small-R jets
        ###systematics += ',CORR_LargeRSmallR_A__1up,CORR_LargeRSmallR_A__1down,CORR_LargeRSmallR_B__1up,CORR_LargeRSmallR_B__1down,CORR_LargeRSmallR_C__1up,CORR_LargeRSmallR_C__1down'
        # large-R jet res.
        systematics += ',LARGERJET_JER_LARGERJET_JER_PT__1up,LARGERJET_JER_LARGERJET_JER_TAU32__1up,LARGERJET_JER_LARGERJET_JER_MASS__1up'
        systList.extend(systematics.split(','))
        l = int(len(systList)/4)
        systListTmp = []
        if 'all1' in options.systs:
            systListTmp.extend(systList[0:l])
        if 'all2' in options.systs:
            systListTmp.extend(systList[l:2*l])
        if 'all3' in options.systs:
            systListTmp.extend(systList[2*l:3*l])
        if 'all4' in options.systs:
            systListTmp.extend(systList[3*l:])
        if 'all' in options.systs:
            systListTmp = systList
        systList = systListTmp
        print "--> Setup to run over following systs.", systList
    elif options.systs == 'pdf':
        systList = []
        systList.append('nominal')
        for m in pdfList:
            dsidWithThisPdf = -1
            for k in pdfSumOfWeights.keys():
                if m in pdfSumOfWeights[k]:
                    dsidWithThisPdf = k
                    break
            nvar = len(pdfSumOfWeights[dsidWithThisPdf][m])
            for k in range(0, nvar):
                systList.append('pdf_%s_%d' % (m, k))
    elif options.systs == 'wjttpdf':
        systList = []
        systList.append('nominal')
        for k in range(0, 30+1):
            systList.append('pdf_PDF4LHC15_nlo_30_%d' % (k))
    elif options.systs == 'qcd':
        systList = []
        systList.append('nominal')
        systList.append('qcdcenup')
        systList.append('qcdcendw')
        systList.append('qcdfwdup')
        systList.append('qcdfwddw')
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
    for k in options.output.split('\;'):
        channels.__setitem__(*k.split(',', 1))
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
        helpers.ROOT.initPDF(options.pdfForWeight)
        helpers.ROOT.setEFT(eftLambda, eftCvv)
    if options.SCALAR != "":
        scalarStr  = options.SCALAR.split(",")
        scalarMH   = float(scalarStr[0])
        scalarMA   = float(scalarStr[1])
        scalarSBA  = float(scalarStr[2])
        scalarTANB = float(scalarStr[3])
        scalarTYPE = int(scalarStr[4])
        helpers.ROOT.initPDF(options.pdfForWeight)
        helpers.init2HDM(scalarMH,scalarMA,scalarSBA,scalarTANB,scalarTYPE)
        print "2HDM setup: mH=%g, mA=%g, sba=%g, tanb=%g, type=%g" % (scalarMH, scalarMA, scalarSBA, scalarTANB, scalarTYPE)
    for k in channels:
        analysisCode[k] = anaClass(k, histSuffixes, channels[k])
        analysisCode[k].keep = options.WjetsHF
        analysisCode[k].applyQCD = False
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
        print k, analysisCode[k], channels[k]
        analysisCode[k].set_top_tagger(options.top_tagger)

    isFirstEvent = True

    for s in systList:
        # s is nominal, or the name of systematic
        treeName = s # systematic name is the same as the TTree name
        if treeName in weightChangeSystematics or 'btag' in treeName or 'wnorm' in treeName or 'wc__' in treeName or 'wl__' in treeName or 'wbb__' in treeName or 'CAallMCAsym' in treeName or 'ttEWK_' in treeName or 'pdf_' in treeName or 'ttNNLO_' in treeName:
            treeName = 'nominal'
        if isWjets and (('ttgen' in treeName) or ('ttpsold' in treeName) or ('ttpspp7' in treeName) or ('ttps' in treeName) or ('ttisrfsr' in treeName) or ('pdf_PDF4LHC15_nlo_30' in treeName) or ('ttxsec' in treeName) or ('singletop' in treeName) or ('elMisIDpos' in treeName) or ('2to3ex' in treeName)): # DANGER remember to change when doing W+jets PDF variation
            treeName = 'nominal'
        if 'ttxsec' in treeName and isTtbar:
            treeName = 'nominal'
        if 'singletop' in treeName and isSingleTop:
            treeName = 'nominal'
        if options.qcd != "False":
            treeName = 'nominal_Loose'
        mt = ROOT.TChain(treeName)
        suffix = s
        if suffix == 'nominal':
            suffix = ''
        addFilesInChain(mt, options.files)
        sel = mt
        ent = mt.GetEntries()
        for k in range(0, ent):
            if options.data and accept_prob > 0:
                randomNumber = randGen.Uniform(0, 1)
                if randomNumber > accept_prob:
                    continue
            mt.GetEntry(k)
            if k % 10000 == 0:
                print "(tree = ",treeName,", syst = ",suffix,") Entry ", k, "/", ent
            if isFirstEvent:
                if not options.data and sel.mcChannelNumber in [410000, 301528, 301529, 301530, 301531, 301532, 410009, 410120, 410121, 407009, 407010, 407011, 407012, 410004, 410003, 410002, 410001, 410500, 410159, 410501, 410502, 410503, 410504, 410505, 410506, 410509, 410511, 410512, 410225, 410250, 410251, 410252]: #410525]:
                    m = sel.mcChannelNumber
                    if sel.mcChannelNumber in [301528, 301529, 301530, 301531, 301532]:
                        m = 410000
                    ROOT.InitNNLO(m)
                isFirstEvent = False

            # common part of the weight
            weight = 1
            if not options.data:
                if not (isWjets and options.systs == 'pdf' and 'pdf_' in suffix): # use internal weights in this case
                    weight *= sel.weight_mc
                channel = sel.mcChannelNumber
                weight *= Xsec[channel]
                if options.systs != 'pdf': #'pdf_' in suffix:
                    if not options.af2:
                        if not channel in sumOfWeights:
                            print "Could not find DSID ",channel, " in sum of weights."
                            weight = 0
                        else:
                            weight /= sumOfWeights[channel]
                    else:
                        if not channel in sumOfWeightsAF2:
                            print "Could not find DSID ",channel, " in sum of weights."
                            weight = 0
                        else:
                            weight /= sumOfWeightsAF2[channel]
                else:
                    if not 'pdf_' in suffix:
                        weight /= sumOfWeights[channel]
                    else:
                        pdfName = (suffix.split('_', 1)[1]).rsplit('_', 1)[0]
                        pdfNumber = int(suffix.rsplit('_', 1)[1])
                        if not channel in pdfSumOfWeights:
                            print "Could not find DSID ",channel, " in sum of weights."
                            weight = 0
                        else:
                            weight /= pdfSumOfWeights[channel][pdfName][pdfNumber]


            for ana in analysisCode:
                weight_reco = analysisCode[ana].getWeight(sel, suffix)
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
                if not options.data and sel.mcChannelNumber in [410000, 301528, 301529, 301530, 301531, 301532, 410009, 410120, 410121, 407009, 407010, 407011, 407012, 410004, 410003, 410002, 410001, 410500, 410159, 410501, 410502, 410503, 410504, 410505, 410506, 410509, 410511, 410512, 10225, 410250, 410251, 410252]: #410525]:
                    if 'ttNNLO_seq_' in suffix:
                        weight_reco *= ROOT.getNNLOWeight(sel.MC_ttbar_afterFSR_pt, sel.MC_t_afterFSR_pt, 1)
                    if 'ttNNLO_topPt_' in suffix:
                        weight_reco *= ROOT.getNNLOWeight(sel.MC_ttbar_afterFSR_pt, sel.MC_t_afterFSR_pt, 0)
                    if 'ttNNLO_topPtDiff_' in suffix:
                        weight_reco *= ROOT.getNNLOWeight(sel.MC_ttbar_afterFSR_pt, sel.MC_t_afterFSR_pt, 2)
                    if 'ttNNLO_seqExtended_' in suffix:
                        weight_reco *= ROOT.getNNLOWeight(sel.MC_ttbar_afterFSR_pt, sel.MC_t_afterFSR_pt, 2)*ROOT.getNNLOWeight(sel.MC_ttbar_afterFSR_pt, sel.MC_t_afterFSR_pt, 1)
                analysisCode[ana].run(sel, suffix, weight*weight_reco, weight)

    for k in analysisCode:
        analysisCode[k].end()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-d", "--data",
                        action="store_true",
                        dest="data",
                        help="Is this data?")
    parser.add_argument("-f", "--files",
                        dest="files", default="input.txt",
                        help="Text file with list of input files.",
                        metavar="FILE")
    parser.add_argument("-A", "--analysis",
                        dest="analysis",
                        default="AnaTtresSL",
                        help="Analysis code to run.",
                        metavar="ANALYSIS")
    parser.add_argument("-o", "--output",
                        dest="output",
                        default="re:hist_re.root,rmu:hist_rmu.root,be:hist_be.root,bmu:hist_bmu.root",
                        help="Comma-separated list of output ROOT files.",
                        metavar="FILES")
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
    parser.add_argument("-N", "--noMttSlices",
                        action='store_true',
                        dest="noMttSlices",
                        default=False,
                        help="If set, stop vetoing high mtt events in 410000 sample.")
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
                        default='isTopTagged_80',
                        help='Boosted top tagger which will applied to the large-R jet for the hadronic-top reconstruction in the boost selection. Simple logical operation are supported.')
    options = parser.parse_args()

    print "-> Initialising binds now."
    ROOT.gSystem.Load(os.path.join(root_path, "libTopNtupleAnalysis.so"))
    ROOT.gSystem.Load(os.path.join(root_path, "G__TopNtupleAnalysis.cxx"))
    print "-> Calling main"
    main()
    print "The end."
