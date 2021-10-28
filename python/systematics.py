from collections import namedtuple, OrderedDict
import helpers
import itertools
logger = helpers.getLogger('TopNtupleAnalysis.systematics')
DO_PRW = helpers.doPRW
Systematic = namedtuple('Systematics', ['name', 'tree', 'signature', 'hist_suffix', 'weight_map'])

class SystematicsGroup(object):
    def __init__(self, systematics):
        iter_systs = iter(systematics)
        tree = next(iter_systs).tree
        for syst in iter_systs:
              assert syst.tree == tree, 'A SystematicsGroup must contain only systematics using the same tree.'
        self.systematics = systematics
        self.tree = tree
    def __repr__(self):
        return 'SystematicsGroup({})'.format(self.tree)

def _syst(name, tree = None, weight_map = ['pileup', 'leptonSF', 'jvt'], signature = None, hist_suffix = None):
    if type(name) == Systematic:
        return name
    if tree is None:
        tree = name
    if signature is None:
        signature = name
    if hist_suffix is None:
        hist_suffix = name if name != 'nominal' else ''
    weight_map = [w if w.startswith('weight_') else 'weight_'+w for w in weight_map if not (not DO_PRW and 'prw' in w)]
    return (name, Systematic(name, tree, signature, hist_suffix, list(weight_map)))

def syst(name):
    try:
        return ALLSYSTS[name]
    except KeyError:
        logger.warning('Systematic({}) not registered. Will be considered as name of systematic tree.'.format(name))
        return _syst(name)

def grouped_systs(systematics, key = lambda tup: tup.tree):
    for k, g in itertools.groupby(sorted(systematics, key = key), key):
        yield SystematicsGroup(list(g))

def get_systs(expr, isTtbar, isSingleTop, isWjets, EFT, pdfList, pdfSumOfWeights, ttbarHighOrderCorrection, applyQCD, analysis = None):
    # systematics list
    systList = []
    analysis = analysis if analysis is not None else 'AnaTtresSL'
    
    if expr[0:3] == 'all':
        systList.extend([
            'jvtSF__1down',
            'jvtSF__1up',
            'pileupSF__1down',
            'pileupSF__1up',
            ## B-tagging
            'btagbSF_0__1up',
            'btagbSF_0__1down',
            'btagbSF_1__1down',
            'btagbSF_1__1up',
            'btagbSF_2__1down',
            'btagbSF_2__1up',
            'btagbSF_3__1down',
            'btagbSF_3__1up',
            'btagbSF_4__1down',
            'btagbSF_4__1up',
            'btagbSF_5__1down',
            'btagbSF_5__1up',
            'btagbSF_6__1down',
            'btagbSF_6__1up',
            'btagbSF_7__1down',
            'btagbSF_7__1up',
            'btagbSF_8__1down',
            'btagbSF_8__1up',
            'btagcSF_0__1down',
            'btagcSF_0__1up',
            'btagcSF_1__1down',
            'btagcSF_1__1up',
            'btagcSF_2__1down',
            'btagcSF_2__1up',
            'btagcSF_3__1down',
            'btagcSF_3__1up',
            'btageSF_0__1down',
            'btageSF_0__1up',
            'btageSF_1__1down',
            'btageSF_1__1up',
            'btaglSF_0__1down',
            'btaglSF_0__1up',
            'btaglSF_1__1down',
            'btaglSF_1__1up',
            'btaglSF_2__1down',
            'btaglSF_2__1up',
            'btaglSF_3__1down',
            'btaglSF_3__1up',
            #top-tag
            'toptagSF_0__1up',
            'toptagSF_0__1down',
            'toptagSF_1__1up',
            'toptagSF_1__1down',
            'toptagSF_2__1up',
            'toptagSF_2__1down',
            'toptagSF_3__1up',
            'toptagSF_3__1down',
            'toptagSF_4__1up',
            'toptagSF_4__1down',
            'toptagSF_5__1up',
            'toptagSF_5__1down',
            'toptagSF_6__1up',
            'toptagSF_6__1down',
            'toptagSF_7__1up',
            'toptagSF_7__1down',
            'toptagSF_8__1up',
            'toptagSF_8__1down',
            'toptagSF_9__1up',
            'toptagSF_9__1down',
            'toptagSF_10__1up',
            'toptagSF_10__1down',
            'toptagSF_11__1up',
            'toptagSF_11__1down',
            ## EGamma
            'EG_RESOLUTION_ALL__1down',
            'EG_RESOLUTION_ALL__1up',
            'EG_SCALE_ALL__1down',
            'EG_SCALE_ALL__1up',
            #JET (small-R and large-R, Category Reduction)
            'JET_EffectiveNP_Modelling1__1up',
            'JET_EffectiveNP_Modelling2__1up',
            'JET_EffectiveNP_Modelling3__1up',
            'JET_EffectiveNP_Modelling4__1up',
            'JET_EffectiveNP_Mixed1__1up',
            'JET_EffectiveNP_Mixed2__1up',
            'JET_EffectiveNP_Mixed3__1up',
            'JET_EffectiveNP_Detector1__1up',
            'JET_EffectiveNP_Detector2__1up',
            'JET_EffectiveNP_Statistical1__1up',
            'JET_EffectiveNP_Statistical2__1up',
            'JET_EffectiveNP_Statistical3__1up',
            'JET_EffectiveNP_Statistical4__1up',
            'JET_EffectiveNP_Statistical5__1up',
            'JET_EffectiveNP_Statistical6__1up',
            'JET_JER_DataVsMC_MC16__1up',
            'JET_Pileup_OffsetMu__1up',
            'JET_Pileup_OffsetNPV__1up',
            'JET_Pileup_PtTerm__1up',
            'JET_Pileup_RhoTopology__1up',
            'JET_Flavor_Composition__1up',
            'JET_Flavor_Response__1up',
            'JET_BJES_Response__1up',
            'JET_PunchThrough_MC16__1up',
            'JET_SingleParticle_HighPt__1up',
            'JET_EtaIntercalibration_Modelling__1up',
            'JET_EtaIntercalibration_TotalStat__1up',
            'JET_EtaIntercalibration_NonClosure_highE__1up',
            'JET_EtaIntercalibration_NonClosure_posEta__1up',
            'JET_EtaIntercalibration_NonClosure_negEta__1up',
            'JET_EtaIntercalibration_NonClosure_2018data__1up',
            'JET_EffectiveNP_Modelling1__1down',
            'JET_EffectiveNP_Modelling2__1down',
            'JET_EffectiveNP_Modelling3__1down',
            'JET_EffectiveNP_Modelling4__1down',
            'JET_EffectiveNP_Mixed1__1down',
            'JET_EffectiveNP_Mixed2__1down',
            'JET_EffectiveNP_Mixed3__1down',
            'JET_EffectiveNP_Detector1__1down',
            'JET_EffectiveNP_Detector2__1down',
            'JET_EffectiveNP_Statistical1__1down',
            'JET_EffectiveNP_Statistical2__1down',
            'JET_EffectiveNP_Statistical3__1down',
            'JET_EffectiveNP_Statistical4__1down',
            'JET_EffectiveNP_Statistical5__1down',
            'JET_EffectiveNP_Statistical6__1down',
            'JET_Pileup_OffsetMu__1down',
            'JET_Pileup_OffsetNPV__1down',
            'JET_Pileup_PtTerm__1down',
            'JET_Pileup_RhoTopology__1down',
            'JET_Flavor_Composition__1down',
            'JET_Flavor_Response__1down',
            'JET_BJES_Response__1down',
            'JET_PunchThrough_MC16__1down',
            'JET_SingleParticle_HighPt__1down',
            'JET_EtaIntercalibration_TotalStat__1down',
            'JET_EtaIntercalibration_Modelling__1down',
            'JET_EtaIntercalibration_NonClosure_highE__1down',
            'JET_EtaIntercalibration_NonClosure_posEta__1down',
            'JET_EtaIntercalibration_NonClosure_negEta__1down',
            'JET_EtaIntercalibration_NonClosure_2018data__1down',
            # JER: small-R jets
            'JET_JER_DataVsMC_MC16__1up',
            'JET_JER_EffectiveNP_1__1up',
            'JET_JER_EffectiveNP_2__1up',
            'JET_JER_EffectiveNP_3__1up',
            'JET_JER_EffectiveNP_4__1up',
            'JET_JER_EffectiveNP_5__1up',
            'JET_JER_EffectiveNP_6__1up',
            'JET_JER_EffectiveNP_7__1up',
            'JET_JER_EffectiveNP_8__1up',
            'JET_JER_EffectiveNP_9__1up',
            'JET_JER_EffectiveNP_10__1up',
            'JET_JER_EffectiveNP_11__1up',
            'JET_JER_EffectiveNP_12restTerm__1up',
            'JET_JER_DataVsMC_MC16__1down',
            'JET_JER_EffectiveNP_1__1down',
            'JET_JER_EffectiveNP_2__1down',
            'JET_JER_EffectiveNP_3__1down',
            'JET_JER_EffectiveNP_4__1down',
            'JET_JER_EffectiveNP_5__1down',
            'JET_JER_EffectiveNP_6__1down',
            'JET_JER_EffectiveNP_7__1down',
            'JET_JER_EffectiveNP_8__1down',
            'JET_JER_EffectiveNP_9__1down',
            'JET_JER_EffectiveNP_10__1down',
            'JET_JER_EffectiveNP_11__1down',
            'JET_JER_EffectiveNP_12restTerm__1down',
            # JES: large-R jet
            'JET_EffectiveNP_R10_Modelling1__1up',
            'JET_EffectiveNP_R10_Modelling2__1up',
            'JET_EffectiveNP_R10_Modelling3__1up',
            'JET_EffectiveNP_R10_Modelling4__1up',
            'JET_EffectiveNP_R10_Mixed2__1up',
            'JET_EffectiveNP_R10_Mixed1__1up',
            'JET_EffectiveNP_R10_Mixed3__1up',
            'JET_EffectiveNP_R10_Mixed4__1up',
            'JET_EffectiveNP_R10_Statistical1__1up',
            'JET_EffectiveNP_R10_Statistical2__1up',
            'JET_EffectiveNP_R10_Statistical3__1up',
            'JET_EffectiveNP_R10_Statistical4__1up',
            'JET_EffectiveNP_R10_Statistical5__1up',
            'JET_EffectiveNP_R10_Statistical6__1up',
            'JET_EffectiveNP_R10_Detector1__1up',
            'JET_EffectiveNP_R10_Detector2__1up',
            'JET_EtaIntercalibration_R10_TotalStat__1up',
            'JET_LargeR_TopologyUncertainty_top__1up',
            'JET_LargeR_TopologyUncertainty_V__1up',
            'JET_EffectiveNP_R10_Modelling1__1down',
            'JET_EffectiveNP_R10_Modelling2__1down',
            'JET_EffectiveNP_R10_Modelling3__1down',
            'JET_EffectiveNP_R10_Modelling4__1down',
            'JET_EffectiveNP_R10_Mixed1__1down',
            'JET_EffectiveNP_R10_Mixed2__1down',
            'JET_EffectiveNP_R10_Mixed3__1down',
            'JET_EffectiveNP_R10_Mixed4__1down',
            'JET_EffectiveNP_R10_Statistical1__1down',
            'JET_EffectiveNP_R10_Statistical2__1down',
            'JET_EffectiveNP_R10_Statistical3__1down',
            'JET_EffectiveNP_R10_Statistical4__1down',
            'JET_EffectiveNP_R10_Statistical5__1down',
            'JET_EffectiveNP_R10_Statistical6__1down',
            'JET_EffectiveNP_R10_Detector1__1down',
            'JET_EffectiveNP_R10_Detector2__1down',
            'JET_EtaIntercalibration_R10_TotalStat__1down',
            'JET_LargeR_TopologyUncertainty_top__1down',
            'JET_LargeR_TopologyUncertainty_V__1down',
            # JER large-R jets
            'JET_JER_DataVsMC_R10_MC16__1up',
            'JET_JER_dijet_R10_closure__1up',
            'JET_JER_dijet_R10_selection__1up',
            'JET_JER_dijet_R10_jesEffNP1__1up',
            'JET_JER_dijet_R10_jesEffNP3__1up',
            'JET_JER_dijet_R10_jesEffNP4__1up',
            'JET_JER_dijet_R10_jesEtaIntMod__1up',
            'JET_JER_dijet_R10_jesFlavComp__1up',
            'JET_JER_dijet_R10_jesFlavResp__1up',
            'JET_JER_dijet_R10_mcgenerator__1up',
            'JET_JER_dijet_R10_stat__1up',
            'JET_JER_AllOthers__1up',
            'JET_JER_DataVsMC_R10_MC16__1down',
            'JET_JER_dijet_R10_closure__1down',
            'JET_JER_dijet_R10_selection__1down',
            'JET_JER_dijet_R10_jesEffNP1__1down',
            'JET_JER_dijet_R10_jesEffNP3__1down',
            'JET_JER_dijet_R10_jesEffNP4__1down',
            'JET_JER_dijet_R10_jesEtaIntMod__1down',
            'JET_JER_dijet_R10_jesFlavComp__1down',
            'JET_JER_dijet_R10_jesFlavResp__1down',
            'JET_JER_dijet_R10_mcgenerator__1down',
            'JET_JER_dijet_R10_stat__1down',
            'JET_JER_AllOthers__1down',
            #JMS
            'JET_JMS_Rtrk_Stat1__1up',
            'JET_JMS_Rtrk_Stat2__1up',
            'JET_JMS_Rtrk_Stat3__1up',
            'JET_JMS_Rtrk_Stat4__1up',
            'JET_JMS_Rtrk_Stat5__1up',
            'JET_JMS_Rtrk_Stat6__1up',
            'JET_JMS_FF_LargerSample__1up',
            'JET_JMS_FF_MatrixElement__1up',
            'JET_JMS_FF_PartonShower__1up',
            'JET_JMS_FF_Shape__1up',
            'JET_JMS_FF_Stat__1up',
            'JET_JMS_FF_InterpolationDifference__1up',
            'JET_JMS_FF_AllOthers__1up',
            'JET_JMS_Rtrk_Tracking__1up',
            'JET_JMS_Rtrk_Generator__1up',
            'JET_JMS_Rtrk_Generator_InterpolationDifference__1up',
            'JET_JMS_Rtrk_InterpolationDifference__1up',
            'JET_JMS_Topology_QCD__1up',
            'JET_JMS_Rtrk_Stat1__1down',
            'JET_JMS_Rtrk_Stat2__1down',
            'JET_JMS_Rtrk_Stat3__1down',
            'JET_JMS_Rtrk_Stat4__1down',
            'JET_JMS_Rtrk_Stat5__1down',
            'JET_JMS_Rtrk_Stat6__1down',
            'JET_JMS_FF_LargerSample__1down',
            'JET_JMS_FF_MatrixElement__1down',
            'JET_JMS_FF_PartonShower__1down',
            'JET_JMS_FF_Shape__1down',
            'JET_JMS_FF_Stat__1down',
            'JET_JMS_FF_InterpolationDifference__1down',
            'JET_JMS_FF_AllOthers__1down',
            'JET_JMS_Rtrk_Tracking__1down',
            'JET_JMS_Rtrk_Generator__1down',
            'JET_JMS_Rtrk_Generator_InterpolationDifference__1down',
            'JET_JMS_Rtrk_InterpolationDifference__1down',
            'JET_JMS_Topology_QCD__1down',
            #JMR
            'COMB_MCData_JMR__1up',
            'COMB_MCME_JMR__1up',
            'COMB_MCPS_JMR__1up',
            'COMB_MCRAD_JMR__1up',
            'COMB_MCSmallJET_JMR__1up',
            'COMB_MCLargeR_JMR__1up',
            'COMB_Stat_JMR__1up',
            'COMB_SHAPE_JMR__1up',
            'COMB_Smoothing_JMR__1up',
            'COMB_Flat20Smoothed_JMR__1up',
            'COMB_OutsideCalib_JMR__1up',
            'COMB_MCData_JMR__1down',
            'COMB_MCME_JMR__1down',
            'COMB_MCPS_JMR__1down',
            'COMB_MCRAD_JMR__1down',
            'COMB_MCSmallJET_JMR__1down',
            'COMB_MCLargeR_JMR__1down',
            'COMB_Stat_JMR__1down',
            'COMB_SHAPE_JMR__1down',
            'COMB_Smoothing_JMR__1down',
            'COMB_Flat20Smoothed_JMR__1down',
            'COMB_OutsideCalib_JMR__1down',
            #MET
            'MET_SoftTrk_Scale__1up',
            'MET_SoftTrk_Scale__1down',
            'MET_SoftTrk_ResoPara',
            'MET_SoftTrk_ResoPerp',
            ## muon scale and resolution
            'MUON_SAGITTA_RESBIAS__1up',
            'MUON_SAGITTA_RHO__1up',
            'MUON_SCALE__1up',
            'MUON_ID__1up',
            'MUON_MS__1up',
            'MUON_SAGITTA_RESBIAS__1down',
            'MUON_SAGITTA_RHO__1down',
            'MUON_SCALE__1down',
            'MUON_ID__1down',
            'MUON_MS__1down',
            ## large-R jet JES (strong scenario)
            #'CombMass_strong_JET_Comb_Modelling_All__1up',
            #'CombMass_strong_JET_Comb_Modelling_All__1down',
            #'CombMass_strong_JET_Comb_Baseline_All__1down',
            #'CombMass_strong_JET_Comb_Baseline_All__1up',
            #'CombMass_strong_JET_Comb_Tracking_All__1down',
            #'CombMass_strong_JET_Comb_Tracking_All__1up',
            #'CombMass_strong_JET_Comb_TotalStat_All__1down',
            #'CombMass_strong_JET_Comb_TotalStat_All__1up',
            
            ## large-R jet JES (medium scenario)
            # 'CombMass_medium_JET_Comb_Baseline_Kin__1up',
            # 'CombMass_medium_JET_Comb_Baseline_Kin__1down',
            # 'CombMass_medium_JET_Comb_Modelling_Kin__1up',
            # 'CombMass_medium_JET_Comb_Modelling_Kin__1down',
            # 'CombMass_medium_JET_Comb_TotalStat_Kin__1up',
            # 'CombMass_medium_JET_Comb_TotalStat_Kin__1down',
            # 'CombMass_medium_JET_Comb_Tracking_Kin__1up',
            # 'CombMass_medium_JET_Comb_Tracking_Kin__1down',
            # 'CombMass_medium_JET_Rtrk_Baseline_Sub__1up',
            # 'CombMass_medium_JET_Rtrk_Baseline_Sub__1down',
            # 'CombMass_medium_JET_Rtrk_Modelling_Sub__1up',
            # 'CombMass_medium_JET_Rtrk_Modelling_Sub__1down',
            # 'CombMass_medium_JET_Rtrk_TotalStat_Sub__1up',
            # 'CombMass_medium_JET_Rtrk_TotalStat_Sub__1down',
            # 'CombMass_medium_JET_Rtrk_Tracking_Sub__1up',
            # 'CombMass_medium_JET_Rtrk_Tracking_Sub__1down',

            ## large-R jet JMR (strong scenario)
            #'CombMass_strong_JET_MassRes_Top__1up'
            # 'LARGERJET_JER_LARGERJET_JER_PT__1up',
            # 'LARGERJET_JER_LARGERJET_JER_TAU32__1up',
            # 'LARGERJET_JER_LARGERJET_JER_MASS__1up'

            ## correlate large-R jets and small-R jets
            # 'CORR_LargeRSmallR_A__1up',
            # 'CORR_LargeRSmallR_A__1down',
            # 'CORR_LargeRSmallR_B__1up',
            # 'CORR_LargeRSmallR_B__1down',
            # 'CORR_LargeRSmallR_C__1up',
            # 'CORR_LargeRSmallR_C__1down'
            ])
        if ttbarHighOrderCorrection == 'NNLOQCDNLOEWK':
            systList.append('ttNNLOQCDNLOEWK__1up')
            systList.append('ttNNLOQCDNLOEWK__1down')
        elif ttbarHighOrderCorrection == 'Rel20EWK':
            systList.append('ttEWK__1up')
            systList.append('ttEWK__1down')
            systList.extend([
                'ttNNLO_seqExtended__1up',
                'ttNNLO_seq__1up',
                'ttNNLO_topPtDiff__1up',
                'ttNNLO_topPt__1up',
                ])
        elif ttbarHighOrderCorrection in ('NNLORecursive2d', 'NNLORecursive3d'):
            systList.extend(['ttNNLOrec_toppt__1up',
                             'ttNNLOrec_toppt__1down',
                             'ttNNLOrec_ttmass__1up',
                             'ttNNLOrec_ttmass__1down',
                             ])
            if ttbarHighOrderCorrection == 'NNLORecursive3d':
                systList.extend(['ttNNLOrec_ttpt__1up',
                                 'ttNNLOrec_ttpt__1down'])
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
        if isWjets or isTtbar:
            systList.append('ttxsecup')
            systList.append('ttxsecdw')
        if isWjets or isSingleTop:
            systList.append('singletopup')
            systList.append('singletopdw')

        if analysis == 'AnaTtresSL':
            systList.append('nominal')
            #systList.append('mttSlope')
            systList.extend([
                '',
                'eChargeMisIDStatSF__1down',
                'eChargeMisIDStatSF__1up',
                'eChargeMisIDSystSF__1down',
                'eChargeMisIDSystSF__1up',
                'eChargeSF__1down',
                'eChargeSF__1up',
                'eIDSF__1down',
                'eIDSF__1up',
                'eIsolSF__1down',
                'eIsolSF__1up',
                'eRecoSF__1down',
                'eRecoSF__1up',
                'eTrigSF__1down',
                'eTrigSF__1up',
                'muIDStatSF__1down',
                'muIDStatSF__1up',
                'muIDSystSF__1down',
                'muIDSystSF__1up',
                'muIsolStatSF__1down',
                'muIsolStatSF__1up',
                'muIsolSystSF__1down',
                'muIsolSystSF__1up',
                'muTrigStatSF__1down',
                'muTrigStatSF__1up',
                'muTrigSystSF__1down',
                'muTrigSystSF__1up'
                ])
        elif analysis == 'AnaTtresFH':
            systList.extend([
                '',
                'CombMass_strong_JET_Comb_Baseline_All__1down',
                'CombMass_strong_JET_Comb_Baseline_All__1up',
                'CombMass_strong_JET_Comb_Modelling_All__1down',
                'CombMass_strong_JET_Comb_Modelling_All__1up',
                'CombMass_strong_JET_Comb_TotalStat_All__1down',
                'CombMass_strong_JET_Comb_TotalStat_All__1up',
                'CombMass_strong_JET_Comb_Tracking_All__1down',
                'CombMass_strong_JET_Comb_Tracking_All__1up',
                'CombMass_strong_JET_MassRes_Top__1up',
                'CombMass_weak_JET_Rtrk_Baseline_pT__1up',
                'CombMass_weak_JET_Rtrk_Baseline_pT__1down',
                'CombMass_weak_JET_Rtrk_Modelling_pT__1up',
                'CombMass_weak_JET_Rtrk_Modelling_pT__1down',
                'CombMass_weak_JET_Rtrk_TotalStat_pT__1up',
                'CombMass_weak_JET_Rtrk_TotalStat_pT__1down',
                'CombMass_weak_JET_Rtrk_Tracking_pT__1up',
                'CombMass_weak_JET_Rtrk_Tracking_pT__1down',
                'CombMass_weak_JET_Comb_Baseline_mass__1up',
                'CombMass_weak_JET_Comb_Baseline_mass__1down',
                'CombMass_weak_JET_Comb_Modelling_mass__1up',
                'CombMass_weak_JET_Comb_Modelling_mass__1down',
                'CombMass_weak_JET_Comb_TotalStat_mass__1up',
                'CombMass_weak_JET_Comb_TotalStat_mass__1down',
                'CombMass_weak_JET_Comb_Tracking_mass__1up',
                'CombMass_weak_JET_Comb_Tracking_mass__1down',
                'CombMass_weak_JET_MassRes_Top__1up',
                'CombMass_weak_JET_MassRes_Top__1down',
                             ])
        systList.remove('')

        if EFT != '':
            systList.append("eftScale__1up")
            systList.append("eftScale__1down")


        l = int(len(systList)/4)
        systListTmp = []
        if 'all1' in expr:
            systListTmp.extend(systList[0:l])
        elif 'all2' in expr:
            systListTmp.extend(systList[l:2*l])
        elif 'all3' in expr:
            systListTmp.extend(systList[2*l:3*l])
        elif 'all4' in expr:
            systListTmp.extend(systList[3*l:])
        elif 'all' in expr:
            systListTmp = systList
        systList = systListTmp
    elif expr == 'pdf':
        systList.append('nominal')
        for pdf in pdfList.iterkeys():
            try:
                for channel, channelWeights in pdfSumOfWeights.iteritems():
                    for runNumber, runNumberWeights in channelWeights.itervalues():
                        if pdf in runNumberWeights:
                            raise StopIteration
            except StopIteration:
                nvar = len(runNumberWeights[pdf].keys())
                for k in range(0, nvar):
                    syst_name = 'pdf_%s_%d' % (channel, k)
                    logger.warning('PDFSystematic({}) not registered. This warning is usually harmless.'.format(syst_name))
                    systList.append(_syst(syst_name, 'nominal'))
    elif expr == 'wjttpdf':
        systList.append('nominal')
        for k in range(0, 30+1):
            systList.append('pdf_PDF4LHC15_nlo_30_%d' % (k))
    elif expr == 'qcdall':
        systList.append('nominal')
        systList.append('qcdcenup')
        systList.append('qcdcendw')
        systList.append('qcdfwdup')
        systList.append('qcdfwddw')
    else:
        systList = expr.split(',')
    ret = []

    for syst_name in systList:
        if applyQCD and syst_name == 'nominal':
            syst_name = 'qcd'
        s = ALLSYSTS.get(syst_name, None)
        if s is None:
            logger.warning('Systematic({}) not registered. Will be considered as name of systematic tree.'.format(syst_name))
            s = _syst(syst_name)[1]
        ret.append(s)

        s.weight_map[:] = [w for w in s.weight_map if not (not DO_PRW and 'prw' in w)]
    assert len(ret) == len(systList)
    logger.info("--> Setup to run over following systs. {}".format(systList))
    return ret




ALLSYSTS = OrderedDict((
    _syst('nominal'),
    _syst('mttSlope', 'nominal'), 
    _syst('pileupSF__1down', 'nominal', ['pileup_DOWN', 'leptonSF', 'jvt']),
    _syst('pileupSF__1up', 'nominal', ['pileup_UP', 'leptonSF', 'jvt']),
    _syst('jvtSF__1down', 'nominal', ['pileup', 'leptonSF', 'jvt_DOWN']),
    _syst('jvtSF__1up', 'nominal', ['pileup', 'leptonSF', 'jvt_UP']),
    _syst('ttNNLO_seqExtended__1up', 'nominal'),
    _syst('ttNNLO_seq__1up', 'nominal'),
    _syst('ttNNLO_topPtDiff__1up', 'nominal'),
    _syst('ttNNLO_topPt__1up', 'nominal'),
    _syst('ttEWK__1up', 'nominal'),
    _syst('ttEWK__1down', 'nominal'),
    _syst('ttNNLOQCDNLOEWK__1up', 'nominal'),
    _syst('ttNNLOQCDNLOEWK__1down', 'nominal'),
    _syst('ttNNLOrec_toppt__1up', 'nominal'),
    _syst('ttNNLOrec_toppt__1down', 'nominal'),
    _syst('ttNNLOrec_ttmass__1up', 'nominal'),
    _syst('ttNNLOrec_ttmass__1down', 'nominal'),
    _syst('ttNNLOrec_ttpt__1up', 'nominal'),
    _syst('ttNNLOrec_ttpt__1down', 'nominal'),
    # top-tagging efficiency: JET_JetTagSF_Dijet_Modelling
    _syst('toptagSF_0__1down', 'nominal'),
    _syst('toptagSF_0__1up',   'nominal'),
    # top-tagging efficiency: JET_JetTagSF_Gammajet_Modelling
    _syst('toptagSF_1__1down', 'nominal'),
    _syst('toptagSF_1__1up',   'nominal'),
    # top-tagging efficiency: JET_JetTagSF_Hadronisation
    _syst('toptagSF_2__1down', 'nominal'),
    _syst('toptagSF_2__1up',   'nominal'),
    # top-tagging efficiency: JET_JetTagSF_MatrixElement
    _syst('toptagSF_3__1down', 'nominal'),
    _syst('toptagSF_3__1up',   'nominal'),
    # top-tagging efficiency: JET_JetTagSF_Radiation
    _syst('toptagSF_4__1down', 'nominal'),
    _syst('toptagSF_4__1up',   'nominal'),
    # top-tagging efficiency: SigEff80_BGSF_Dijet_Stat
    _syst('toptagSF_5__1down', 'nominal'),
    _syst('toptagSF_5__1up',   'nominal'),
    # top-tagging efficiency: SigEff80_BGSF_Gammajet_Stat
    _syst('toptagSF_6__1down', 'nominal'),
    _syst('toptagSF_6__1up',   'nominal'),
    # top-tagging efficiency: SigEff80_BGSF_Propagated_AllOthers
    _syst('toptagSF_7__1down', 'nominal'),
    _syst('toptagSF_7__1up',   'nominal'),
    # top-tagging efficiency: SigEff80_SigSF_BinVariation
    _syst('toptagSF_8__1down', 'nominal'),
    _syst('toptagSF_8__1up',   'nominal'),
    # top-tagging efficiency: SigEff80_SigSF_ExtrapolationPt
    _syst('toptagSF_9__1down', 'nominal'),
    _syst('toptagSF_9__1up',   'nominal'),
    # top-tagging efficiency: SigEff80_SigSF_Propagated_AllOthers
    _syst('toptagSF_10__1down', 'nominal'),
    _syst('toptagSF_10__1up',   'nominal'),
    # top-tagging efficiency: JET_TopTagContained_SigEff80_SigSF_Statistics
    _syst('toptagSF_11__1down', 'nominal'),
    _syst('toptagSF_11__1up',   'nominal'),
    # top-tagging efficiency: SigEff80_TagEffUnc_GlobalBackground
    _syst('toptagSF_12__1down', 'nominal'),
    _syst('toptagSF_12__1up',   'nominal'),
    # top-tagging efficiency: JET_TopTagInclusive_SigEff80_TagEffUnc_GlobalOther
    _syst('toptagSF_13__1down', 'nominal'),
    _syst('toptagSF_13__1up',   'nominal'),
    # top-tagging efficiency:JET_TopTagInclusive_SigEff80_TagEffUnc_GlobalSignal
    _syst('toptagSF_14__1down', 'nominal'),
    _syst('toptagSF_14__1up',   'nominal'),
    # top-tagging efficiency:bTag_B_0
    _syst('toptagSF_15__1down', 'nominal'),
    _syst('toptagSF_15__1up',   'nominal'),
    # top-tagging efficiency:bTag_Light_0
    _syst('toptagSF_16__1down', 'nominal'),
    _syst('toptagSF_16__1up',   'nominal'),
    # top-tagging efficiency:bTag_Light_1
    _syst('toptagSF_17__1down', 'nominal'),
    _syst('toptagSF_17__1up',   'nominal'),
    # b-tagging efficiency
    _syst('btagbSF_0__1down', 'nominal'),
    _syst('btagbSF_0__1up', 'nominal'),
    # _syst('btagbSF_0_pt1__1down', 'nominal'),
    # _syst('btagbSF_0_pt1__1up', 'nominal'),
    # _syst('btagbSF_0_pt2__1down', 'nominal'),
    # _syst('btagbSF_0_pt2__1up', 'nominal'),
    # _syst('btagbSF_0_pt3__1down', 'nominal'),
    # _syst('btagbSF_0_pt3__1up', 'nominal'),
    _syst('btagbSF_1__1down', 'nominal'),
    _syst('btagbSF_1__1up', 'nominal'),
    _syst('btagbSF_2__1down', 'nominal'),
    _syst('btagbSF_2__1up', 'nominal'),
    _syst('btagbSF_3__1down', 'nominal'),
    _syst('btagbSF_3__1up', 'nominal'),
    _syst('btagbSF_4__1down', 'nominal'),
    _syst('btagbSF_4__1up', 'nominal'),
    _syst('btagbSF_5__1down', 'nominal'),
    _syst('btagbSF_5__1up', 'nominal'),
    _syst('btagbSF_6__1down', 'nominal'),
    _syst('btagbSF_6__1up', 'nominal'),
    _syst('btagbSF_7__1down', 'nominal'),
    _syst('btagbSF_7__1up', 'nominal'),
    _syst('btagbSF_8__1down', 'nominal'),
    _syst('btagbSF_8__1up', 'nominal'),
    # c-mistag efficiency
    _syst('btagcSF_0__1down', 'nominal'),
    _syst('btagcSF_0__1up', 'nominal'),
    # _syst('btagcSF_0_pt1__1down', 'nominal'),
    # _syst('btagcSF_0_pt1__1up', 'nominal'),
    # _syst('btagcSF_0_pt2__1down', 'nominal'),
    # _syst('btagcSF_0_pt2__1up', 'nominal'),
    # _syst('btagcSF_0_pt3__1down', 'nominal'),
    # _syst('btagcSF_0_pt3__1up', 'nominal'),
    _syst('btagcSF_1__1down', 'nominal'),
    _syst('btagcSF_1__1up', 'nominal'),
    _syst('btagcSF_2__1down', 'nominal'),
    _syst('btagcSF_2__1up', 'nominal'),
    _syst('btagcSF_3__1down', 'nominal'),
    _syst('btagcSF_3__1up', 'nominal'),
    # b-tagging efficiency high-pT extrap.
    _syst('btageSF_0__1down', 'nominal'),
    _syst('btageSF_0__1up', 'nominal'),
    # c-mistag efficiency high-pT extrap.
    _syst('btageSF_1__1down', 'nominal'),
    _syst('btageSF_1__1up', 'nominal'),
    # light-mistag efficiency
    _syst('btaglSF_0__1down', 'nominal'),
    _syst('btaglSF_0__1up', 'nominal'),
    # _syst('btaglSF_0_pt1__1down', 'nominal'),
    # _syst('btaglSF_0_pt1__1up', 'nominal'),
    # _syst('btaglSF_0_pt2__1down', 'nominal'),
    # _syst('btaglSF_0_pt2__1up', 'nominal'),
    # _syst('btaglSF_0_pt3__1down', 'nominal'),
    # _syst('btaglSF_0_pt3__1up', 'nominal'),
    _syst('btaglSF_10__1down', 'nominal'),
    _syst('btaglSF_10__1up', 'nominal'),
    _syst('btaglSF_1__1down', 'nominal'),
    _syst('btaglSF_1__1up', 'nominal'),
    _syst('btaglSF_2__1down', 'nominal'),
    _syst('btaglSF_2__1up', 'nominal'),
    _syst('btaglSF_3__1down', 'nominal'),
    _syst('btaglSF_3__1up', 'nominal'),
    _syst('btaglSF_4__1down', 'nominal'),
    _syst('btaglSF_4__1up', 'nominal'),
    _syst('btaglSF_5__1down', 'nominal'),
    _syst('btaglSF_5__1up', 'nominal'),
    _syst('btaglSF_6__1down', 'nominal'),
    _syst('btaglSF_6__1up', 'nominal'),
    _syst('btaglSF_7__1down', 'nominal'),
    _syst('btaglSF_7__1up', 'nominal'),
    _syst('btaglSF_8__1down', 'nominal'),
    _syst('btaglSF_8__1up', 'nominal'),
    _syst('btaglSF_9__1down', 'nominal'),
    _syst('btaglSF_9__1up', 'nominal'),
    # electron trigger
    _syst('eChargeMisIDStatSF__1down', 'nominal', ['pileup', 'leptonSF', 'jvt', 'indiv_SF_EL_ChargeMisID_STAT_DOWN']),
    _syst('eChargeMisIDStatSF__1up', 'nominal', ['pileup', 'leptonSF', 'jvt', 'indiv_SF_EL_ChargeMisID_STAT_UP']),
    _syst('eChargeMisIDSystSF__1down', 'nominal', ['pileup', 'leptonSF', 'jvt', 'indiv_SF_EL_ChargeMisID_SYST_DOWN']),
    _syst('eChargeMisIDSystSF__1up', 'nominal', ['pileup', 'leptonSF', 'jvt', 'indiv_SF_EL_ChargeMisID_SYST_UP']),
    _syst('eChargeSF__1down', 'nominal', ['pileup', 'leptonSF', 'jvt', 'indiv_SF_EL_ChargeID_DOWN']),
    _syst('eChargeSF__1up', 'nominal', ['pileup', 'leptonSF', 'jvt', 'indiv_SF_EL_ChargeID_UP']),
    _syst('eIDSF__1down', 'nominal', ['pileup', 'leptonSF_EL_SF_ID_DOWN']),
    _syst('eIDSF__1up', 'nominal', ['pileup', 'leptonSF_EL_SF_ID_UP']),
    _syst('eIsolSF__1down', 'nominal', ['pileup', 'leptonSF_EL_SF_Isol_DOWN', 'jvt']),
    _syst('eIsolSF__1up', 'nominal', ['pileup', 'leptonSF_EL_SF_Isol_UP', 'jvt']),
    _syst('eRecoSF__1down', 'nominal', ['pileup', 'leptonSF_EL_SF_Reco_DOWN']),
    _syst('eRecoSF__1up', 'nominal', ['pileup', 'leptonSF_EL_SF_Reco_UP']),
    _syst('eTrigSF__1down', 'nominal', ['pileup', 'leptonSF_EL_SF_Trigger_DOWN', 'jvt']),
    _syst('eTrigSF__1up', 'nominal', ['pileup', 'leptonSF_EL_SF_Trigger_UP', 'jvt']),
    # muon trigger
    _syst('muIDStatSF__1down', 'nominal', ['pileup', 'leptonSF_MU_SF_ID_STAT_DOWN', 'jvt']),
    _syst('muIDStatSF__1up', 'nominal', ['pileup', 'leptonSF_MU_SF_ID_STAT_UP', 'jvt']),
    _syst('muIDSystSF__1down', 'nominal', ['pileup', 'leptonSF_MU_SF_ID_SYST_DOWN', 'jvt']),
    _syst('muIDSystSF__1up', 'nominal', ['pileup', 'leptonSF_MU_SF_ID_SYST_UP', 'jvt']),
    _syst('muIsolStatSF__1down', 'nominal', ['pileup', 'leptonSF_MU_SF_Isol_STAT_DOWN', 'jvt']),
    _syst('muIsolStatSF__1up', 'nominal', ['pileup', 'leptonSF_MU_SF_Isol_STAT_UP', 'jvt']),
    _syst('muIsolSystSF__1down', 'nominal', ['pileup', 'leptonSF_MU_SF_Isol_SYST_DOWN', 'jvt']),
    _syst('muIsolSystSF__1up', 'nominal', ['pileup', 'leptonSF_MU_SF_Isol_SYST_UP', 'jvt']),
    _syst('muTrigStatSF__1down', 'nominal', ['pileup', 'leptonSF_MU_SF_Trigger_STAT_DOWN', 'jvt']),
    _syst('muTrigStatSF__1up', 'nominal', ['pileup', 'leptonSF_MU_SF_Trigger_STAT_UP', 'jvt']),
    _syst('muTrigSystSF__1down', 'nominal', ['pileup', 'leptonSF_MU_SF_Trigger_SYST_DOWN', 'jvt']),
    _syst('muTrigSystSF__1up', 'nominal', ['pileup', 'leptonSF_MU_SF_Trigger_SYST_UP', 'jvt']),
    _syst('EG_RESOLUTION_ALL__1down'),
    _syst('EG_RESOLUTION_ALL__1up'),
    _syst('EG_SCALE_ALL__1down'),
    _syst('EG_SCALE_ALL__1up'),
    ##### Category Reduction Scheme #####
    #JES: small-R jet (akt4)
    _syst('JET_EffectiveNP_Modelling1__1up'),
    _syst('JET_EffectiveNP_Modelling2__1up'),
    _syst('JET_EffectiveNP_Modelling3__1up'),
    _syst('JET_EffectiveNP_Modelling4__1up'),
    _syst('JET_EffectiveNP_Mixed1__1up'),
    _syst('JET_EffectiveNP_Mixed2__1up'),
    _syst('JET_EffectiveNP_Mixed3__1up'),
    _syst('JET_EffectiveNP_Detector1__1up'),
    _syst('JET_EffectiveNP_Detector2__1up'),
    _syst('JET_EffectiveNP_Statistical1__1up'),
    _syst('JET_EffectiveNP_Statistical2__1up'),
    _syst('JET_EffectiveNP_Statistical3__1up'),
    _syst('JET_EffectiveNP_Statistical4__1up'),
    _syst('JET_EffectiveNP_Statistical5__1up'),
    _syst('JET_EffectiveNP_Statistical6__1up'),
    _syst('JET_Pileup_OffsetMu__1up'),
    _syst('JET_Pileup_OffsetNPV__1up'),
    _syst('JET_Pileup_PtTerm__1up'),
    _syst('JET_Pileup_RhoTopology__1up'),
    _syst('JET_Flavor_Composition__1up'),
    _syst('JET_Flavor_Response__1up'),
    _syst('JET_BJES_Response__1up'),
    _syst('JET_PunchThrough_MC16__1up'),
    _syst('JET_SingleParticle_HighPt__1up'),
    _syst('JET_EtaIntercalibration_Modelling__1up'),
    _syst('JET_EtaIntercalibration_TotalStat__1up'),
    _syst('JET_EtaIntercalibration_NonClosure_highE__1up'),
    _syst('JET_EtaIntercalibration_NonClosure_posEta__1up'),
    _syst('JET_EtaIntercalibration_NonClosure_negEta__1up'),
    _syst('JET_EtaIntercalibration_NonClosure_2018data__1up'),
    _syst('JET_EffectiveNP_Modelling1__1down'),
    _syst('JET_EffectiveNP_Modelling2__1down'),
    _syst('JET_EffectiveNP_Modelling3__1down'),
    _syst('JET_EffectiveNP_Modelling4__1down'),
    _syst('JET_EffectiveNP_Mixed1__1down'),
    _syst('JET_EffectiveNP_Mixed2__1down'),
    _syst('JET_EffectiveNP_Mixed3__1down'),
    _syst('JET_EffectiveNP_Detector1__1down'),
    _syst('JET_EffectiveNP_Detector2__1down'),
    _syst('JET_EffectiveNP_Statistical1__1down'),
    _syst('JET_EffectiveNP_Statistical2__1down'),
    _syst('JET_EffectiveNP_Statistical3__1down'),
    _syst('JET_EffectiveNP_Statistical4__1down'),
    _syst('JET_EffectiveNP_Statistical5__1down'),
    _syst('JET_EffectiveNP_Statistical6__1down'),
    _syst('JET_Pileup_OffsetMu__1down'),
    _syst('JET_Pileup_OffsetNPV__1down'),
    _syst('JET_Pileup_PtTerm__1down'),
    _syst('JET_Pileup_RhoTopology__1down'),
    _syst('JET_Flavor_Composition__1down'),
    _syst('JET_Flavor_Response__1down'),
    _syst('JET_BJES_Response__1down'),
    _syst('JET_PunchThrough_MC16__1down'),
    _syst('JET_SingleParticle_HighPt__1down'),
    _syst('JET_EtaIntercalibration_TotalStat__1down'),
    _syst('JET_EtaIntercalibration_Modelling__1down'),
    _syst('JET_EtaIntercalibration_NonClosure_highE__1down'),
    _syst('JET_EtaIntercalibration_NonClosure_posEta__1down'),
    _syst('JET_EtaIntercalibration_NonClosure_negEta__1down'),
    _syst('JET_EtaIntercalibration_NonClosure_2018data__1down'),

    #JER: small-R jet (akt4)
    _syst('JET_JER_DataVsMC_MC16__1up'),
    _syst('JET_JER_EffectiveNP_1__1up'),
    _syst('JET_JER_EffectiveNP_2__1up'),
    _syst('JET_JER_EffectiveNP_3__1up'),
    _syst('JET_JER_EffectiveNP_4__1up'),
    _syst('JET_JER_EffectiveNP_5__1up'),
    _syst('JET_JER_EffectiveNP_6__1up'),
    _syst('JET_JER_EffectiveNP_7__1up'),
    _syst('JET_JER_EffectiveNP_8__1up'),
    _syst('JET_JER_EffectiveNP_9__1up'),
    _syst('JET_JER_EffectiveNP_10__1up'),
    _syst('JET_JER_EffectiveNP_11__1up'),
    _syst('JET_JER_EffectiveNP_12restTerm__1up'),
    _syst('JET_JER_DataVsMC_MC16__1down'),
    _syst('JET_JER_EffectiveNP_1__1down'),
    _syst('JET_JER_EffectiveNP_2__1down'),
    _syst('JET_JER_EffectiveNP_3__1down'),
    _syst('JET_JER_EffectiveNP_4__1down'),
    _syst('JET_JER_EffectiveNP_5__1down'),
    _syst('JET_JER_EffectiveNP_6__1down'),
    _syst('JET_JER_EffectiveNP_7__1down'),
    _syst('JET_JER_EffectiveNP_8__1down'),
    _syst('JET_JER_EffectiveNP_9__1down'),
    _syst('JET_JER_EffectiveNP_10__1down'),
    _syst('JET_JER_EffectiveNP_11__1down'),
    _syst('JET_JER_EffectiveNP_12restTerm__1down'),

    #JES: large-R jet (akt10)
    # --- up ---
    _syst('JET_EffectiveNP_R10_Modelling1__1up'),
    _syst('JET_EffectiveNP_R10_Modelling2__1up'),
    _syst('JET_EffectiveNP_R10_Modelling3__1up'),
    _syst('JET_EffectiveNP_R10_Modelling4__1up'),
    _syst('JET_EffectiveNP_R10_Mixed2__1up'),
    _syst('JET_EffectiveNP_R10_Mixed1__1up'),
    _syst('JET_EffectiveNP_R10_Mixed3__1up'),
    _syst('JET_EffectiveNP_R10_Mixed4__1up'),
    _syst('JET_EffectiveNP_R10_Statistical1__1up'),
    _syst('JET_EffectiveNP_R10_Statistical2__1up'),
    _syst('JET_EffectiveNP_R10_Statistical3__1up'),
    _syst('JET_EffectiveNP_R10_Statistical4__1up'),
    _syst('JET_EffectiveNP_R10_Statistical5__1up'),
    _syst('JET_EffectiveNP_R10_Statistical6__1up'),
    _syst('JET_EffectiveNP_R10_Detector1__1up'),
    _syst('JET_EffectiveNP_R10_Detector2__1up'),
    _syst('JET_EtaIntercalibration_R10_TotalStat__1up'),
    _syst('JET_LargeR_TopologyUncertainty_top__1up'),
    _syst('JET_LargeR_TopologyUncertainty_V__1up'),
    # --- down ---
    _syst('JET_EffectiveNP_R10_Modelling1__1down'),
    _syst('JET_EffectiveNP_R10_Modelling2__1down'),
    _syst('JET_EffectiveNP_R10_Modelling3__1down'),
    _syst('JET_EffectiveNP_R10_Modelling4__1down'),
    _syst('JET_EffectiveNP_R10_Mixed1__1down'),
    _syst('JET_EffectiveNP_R10_Mixed2__1down'),
    _syst('JET_EffectiveNP_R10_Mixed3__1down'),
    _syst('JET_EffectiveNP_R10_Mixed4__1down'),
    _syst('JET_EffectiveNP_R10_Statistical1__1down'),
    _syst('JET_EffectiveNP_R10_Statistical2__1down'),
    _syst('JET_EffectiveNP_R10_Statistical3__1down'),
    _syst('JET_EffectiveNP_R10_Statistical4__1down'),
    _syst('JET_EffectiveNP_R10_Statistical5__1down'),
    _syst('JET_EffectiveNP_R10_Statistical6__1down'),
    _syst('JET_EffectiveNP_R10_Detector1__1down'),
    _syst('JET_EffectiveNP_R10_Detector2__1down'),
    _syst('JET_EtaIntercalibration_R10_TotalStat__1down'),
    _syst('JET_LargeR_TopologyUncertainty_top__1down'),
    _syst('JET_LargeR_TopologyUncertainty_V__1down'),
    #JER: large-R jet (akt10)
    # --- up ---
    _syst('JET_JER_DataVsMC_R10_MC16__1up'),
    _syst('JET_JER_dijet_R10_closure__1up'),
    _syst('JET_JER_dijet_R10_selection__1up'),
    _syst('JET_JER_dijet_R10_jesEffNP1__1up'),
    _syst('JET_JER_dijet_R10_jesEffNP3__1up'),
    _syst('JET_JER_dijet_R10_jesEffNP4__1up'),
    _syst('JET_JER_dijet_R10_jesEtaIntMod__1up'),
    _syst('JET_JER_dijet_R10_jesFlavComp__1up'),
    _syst('JET_JER_dijet_R10_jesFlavResp__1up'),
    _syst('JET_JER_dijet_R10_mcgenerator__1up'),
    _syst('JET_JER_dijet_R10_stat__1up'),
    _syst('JET_JER_AllOthers__1up'),
    # --- down ---
    _syst('JET_JER_DataVsMC_R10_MC16__1down'),
    _syst('JET_JER_dijet_R10_closure__1down'),
    _syst('JET_JER_dijet_R10_selection__1down'),
    _syst('JET_JER_dijet_R10_jesEffNP1__1down'),
    _syst('JET_JER_dijet_R10_jesEffNP3__1down'),
    _syst('JET_JER_dijet_R10_jesEffNP4__1down'),
    _syst('JET_JER_dijet_R10_jesEtaIntMod__1down'),
    _syst('JET_JER_dijet_R10_jesFlavComp__1down'),
    _syst('JET_JER_dijet_R10_jesFlavResp__1down'),
    _syst('JET_JER_dijet_R10_mcgenerator__1down'),
    _syst('JET_JER_dijet_R10_stat__1down'),
    _syst('JET_JER_AllOthers__1down'),

    #JMS
    # --- up ---
    _syst('JET_JMS_Rtrk_Stat1__1up'),
    _syst('JET_JMS_Rtrk_Stat2__1up'),
    _syst('JET_JMS_Rtrk_Stat3__1up'),
    _syst('JET_JMS_Rtrk_Stat4__1up'),
    _syst('JET_JMS_Rtrk_Stat5__1up'),
    _syst('JET_JMS_Rtrk_Stat6__1up'),
    _syst('JET_JMS_FF_LargerSample__1up'),
    _syst('JET_JMS_FF_MatrixElement__1up'),
    _syst('JET_JMS_FF_PartonShower__1up'),
    _syst('JET_JMS_FF_Shape__1up'),
    _syst('JET_JMS_FF_Stat__1up'),
    _syst('JET_JMS_FF_InterpolationDifference__1up'),
    _syst('JET_JMS_FF_AllOthers__1up'),
    _syst('JET_JMS_Rtrk_Tracking__1up'),
    _syst('JET_JMS_Rtrk_Generator__1up'),
    _syst('JET_JMS_Rtrk_Generator_InterpolationDifference__1up'),
    _syst('JET_JMS_Rtrk_InterpolationDifference__1up'),
    _syst('JET_JMS_Topology_QCD__1up'),
    # --- down ---
    _syst('JET_JMS_Rtrk_Stat1__1down'),
    _syst('JET_JMS_Rtrk_Stat2__1down'),
    _syst('JET_JMS_Rtrk_Stat3__1down'),
    _syst('JET_JMS_Rtrk_Stat4__1down'),
    _syst('JET_JMS_Rtrk_Stat5__1down'),
    _syst('JET_JMS_Rtrk_Stat6__1down'),
    _syst('JET_JMS_FF_LargerSample__1down'),
    _syst('JET_JMS_FF_MatrixElement__1down'),
    _syst('JET_JMS_FF_PartonShower__1down'),
    _syst('JET_JMS_FF_Shape__1down'),
    _syst('JET_JMS_FF_Stat__1down'),
    _syst('JET_JMS_FF_InterpolationDifference__1down'),
    _syst('JET_JMS_FF_AllOthers__1down'),
    _syst('JET_JMS_Rtrk_Tracking__1down'),
    _syst('JET_JMS_Rtrk_Generator__1down'),
    _syst('JET_JMS_Rtrk_Generator_InterpolationDifference__1down'),
    _syst('JET_JMS_Rtrk_InterpolationDifference__1down'),
    _syst('JET_JMS_Topology_QCD__1down'),

    #JMR
    #--- up ---
    _syst('COMB_MCData_JMR__1up'),
    _syst('COMB_MCME_JMR__1up'),
    _syst('COMB_MCPS_JMR__1up'),
    _syst('COMB_MCRAD_JMR__1up'),
    _syst('COMB_MCSmallJET_JMR__1up'),
    _syst('COMB_MCLargeR_JMR__1up'),
    _syst('COMB_Stat_JMR__1up'),
    _syst('COMB_SHAPE_JMR__1up'),
    _syst('COMB_Smoothing_JMR__1up'),
    _syst('COMB_Flat20Smoothed_JMR__1up'),
    _syst('COMB_OutsideCalib_JMR__1up'),
    #--- down ---
    _syst('COMB_MCData_JMR__1down'),
    _syst('COMB_MCME_JMR__1down'),
    _syst('COMB_MCPS_JMR__1down'),
    _syst('COMB_MCRAD_JMR__1down'),
    _syst('COMB_MCSmallJET_JMR__1down'),
    _syst('COMB_MCLargeR_JMR__1down'),
    _syst('COMB_Stat_JMR__1down'),
    _syst('COMB_SHAPE_JMR__1down'),
    _syst('COMB_Smoothing_JMR__1down'),
    _syst('COMB_Flat20Smoothed_JMR__1down'),
    _syst('COMB_OutsideCalib_JMR__1down'),


    # _syst('LARGERJET_JER_LARGERJET_JER_MASS__1up'),
    # _syst('LARGERJET_JER_LARGERJET_JER_PT__1up'),
    # _syst('LARGERJET_JER_LARGERJET_JER_TAU32__1up'),
    _syst('CombMass_medium_JET_Comb_Baseline_Kin__1down'),
    _syst('CombMass_medium_JET_Comb_Baseline_Kin__1up'),
    _syst('CombMass_medium_JET_Comb_Modelling_Kin__1down'),
    _syst('CombMass_medium_JET_Comb_Modelling_Kin__1up'),
    _syst('CombMass_medium_JET_Comb_TotalStat_Kin__1down'),
    _syst('CombMass_medium_JET_Comb_TotalStat_Kin__1up'),
    _syst('CombMass_medium_JET_Comb_Tracking_Kin__1down'),
    _syst('CombMass_medium_JET_Comb_Tracking_Kin__1up'),
    _syst('CombMass_medium_JET_Rtrk_Baseline_Sub__1down'),
    _syst('CombMass_medium_JET_Rtrk_Baseline_Sub__1up'),
    _syst('CombMass_medium_JET_Rtrk_Modelling_Sub__1down'),
    _syst('CombMass_medium_JET_Rtrk_Modelling_Sub__1up'),
    _syst('CombMass_medium_JET_Rtrk_TotalStat_Sub__1down'),
    _syst('CombMass_medium_JET_Rtrk_TotalStat_Sub__1up'),
    _syst('CombMass_medium_JET_Rtrk_Tracking_Sub__1down'),
    _syst('CombMass_medium_JET_Rtrk_Tracking_Sub__1up'),
    _syst('CombMass_strong_JET_Comb_Baseline_All__1down', signature = 'toptagSF_4__1down'),
    _syst('CombMass_strong_JET_Comb_Baseline_All__1up', signature = 'toptagSF_4__1up'),
    _syst('CombMass_strong_JET_Comb_Modelling_All__1down', signature = 'toptagSF_5__1down'),
    _syst('CombMass_strong_JET_Comb_Modelling_All__1up', signature = 'toptagSF_5__1up'),
    _syst('CombMass_strong_JET_Comb_TotalStat_All__1down', signature = 'toptagSF_6__1down'),
    _syst('CombMass_strong_JET_Comb_TotalStat_All__1up', signature = 'toptagSF_6__1down'),
    _syst('CombMass_strong_JET_Comb_Tracking_All__1down', signature = 'toptagSF_7__1down'),
    _syst('CombMass_strong_JET_Comb_Tracking_All__1up', signature = 'toptagSF_7__1up'),
    _syst('CombMass_weak_JET_Rtrk_Baseline_pT__1up', signature = 'toptagSF_4__1up'),
    _syst('CombMass_weak_JET_Rtrk_Baseline_pT__1down', signature = 'toptagSF_4__1down'),
    _syst('CombMass_weak_JET_Rtrk_Modelling_pT__1up', signature = 'toptagSF_5__1up'),
    _syst('CombMass_weak_JET_Rtrk_Modelling_pT__1down', signature = 'toptagSF_5__1down'),
    _syst('CombMass_weak_JET_Rtrk_TotalStat_pT__1up', signature = 'toptagSF_6__1up'),
    _syst('CombMass_weak_JET_Rtrk_TotalStat_pT__1down', signature = 'toptagSF_6__1down'),
    _syst('CombMass_weak_JET_Rtrk_Tracking_pT__1up', signature = 'toptagSF_7__1up'),
    _syst('CombMass_weak_JET_Rtrk_Tracking_pT__1down', signature = 'toptagSF_7__1down'),
    _syst('CombMass_weak_JET_Comb_Baseline_mass__1up'),
    _syst('CombMass_weak_JET_Comb_Baseline_mass__1down'),
    _syst('CombMass_weak_JET_Comb_Modelling_mass__1up'),
    _syst('CombMass_weak_JET_Comb_Modelling_mass__1down'),
    _syst('CombMass_weak_JET_Comb_TotalStat_mass__1up'),
    _syst('CombMass_weak_JET_Comb_TotalStat_mass__1down'),
    _syst('CombMass_weak_JET_Comb_Tracking_mass__1up'),
    _syst('CombMass_weak_JET_Comb_Tracking_mass__1down'),



    _syst('CombMass_strong_JET_MassRes_Top__1up'),
    _syst('CombMass_weak_JET_MassRes_Top__1up'),
    _syst('CombMass_weak_JET_MassRes_Top__1down'),
    _syst('MET_SoftTrk_ResoPara'),
    _syst('MET_SoftTrk_ResoPerp'),
    _syst('MET_SoftTrk_Scale__1down'),
    _syst('MET_SoftTrk_Scale__1up'),
    _syst('MUON_ID__1down'),
    _syst('MUON_ID__1up'),
    _syst('MUON_MS__1down'),
    _syst('MUON_MS__1up'),
    _syst('MUON_SAGITTA_RESBIAS__1down'),
    _syst('MUON_SAGITTA_RESBIAS__1up'),
    _syst('MUON_SAGITTA_RHO__1down'),
    _syst('MUON_SAGITTA_RHO__1up'),
    _syst('MUON_SCALE__1down'),
    _syst('MUON_SCALE__1up'),
    # EFT
    _syst('eftScale__1down', 'nominal'),
    _syst('eftScale__1up', 'nominal'),
    # W+jets
    _syst('wnorm__1up', 'nominal'),
    _syst('wnorm__1down', 'nominal'),
    _syst('wc__1up', 'nominal'),
    _syst('wc__1down', 'nominal'),
    _syst('wl__1up', 'nominal'),
    _syst('wl_1down', 'nominal'),
    _syst('wbb__1up', 'nominal'),
    _syst('wbb__1down', 'nominal'),
    _syst('CAallMCAsym', 'nominal'),

    _syst('2to3ex', 'nominal'),

    _syst('elMisIDpos_down', 'nominal'),
    _syst('elMisIDpos_up', 'nominal'),
    _syst('singletopdw', 'nominal'),
    _syst('singletopup', 'nominal'),
    _syst('ttgenup', 'nominal'),
    _syst('ttgendw', 'nominal'),
    _syst('ttisrfsrdw', 'nominal'),
    _syst('ttisrfsrup', 'nominal'),
    _syst('ttpsdw', 'nominal'),
    _syst('ttpsolddw', 'nominal'),
    _syst('ttpsoldup', 'nominal'),
    _syst('ttpspp8dw', 'nominal'),
    _syst('ttpspp8up', 'nominal'),
    _syst('ttpsup', 'nominal'),
    _syst('ttxsecdw', 'nominal'),
    _syst('ttxsecup', 'nominal'),
    _syst('wl__1down', 'nominal'),
    # wjttpdf
    _syst('pdf_PDF4LHC15_nlo_30_0', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_1', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_2', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_3', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_4', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_5', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_6', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_7', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_8', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_9', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_10', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_11', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_12', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_13', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_14', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_15', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_16', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_17', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_18', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_19', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_20', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_21', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_22', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_23', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_24', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_25', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_26', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_27', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_28', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_29', 'nominal'),
    _syst('pdf_PDF4LHC15_nlo_30_30', 'nominal'),
    # QCD
    _syst('qcd'     , 'nominal_Loose', hist_suffix = ''),
    _syst('qcdcenup', 'nominal_Loose'),
    _syst('qcdcendw', 'nominal_Loose'),
    _syst('qcdfwddw', 'nominal_Loose'),
    _syst('qcdfwdup', 'nominal_Loose'),
    ))