import re
import helpers
import ROOT
import math
logger = helpers.getLogger('TopNtupleAnalysis.selections')

class Selection(object):
    def __init__(self, _callable = None, *args, **kwds):
        self._alg = _callable(*args, **kwds)
        raise NotImplementedError
    def passes(self, event):
        return self._alg(event)
    def scale_factor(self, event):
        raise NotImplementedError

class TtresChi2(Selection):
    def __init__(self, bot_tagger, max_chi2 = 10**0.9, strategy = 'deltaR'):
        self.strategy = strategy
        self.met = ROOT.Math.PtEtaPhiEVector()
        self.bot_tagger = bot_tagger
        self.max_chi2 = max_chi2
        self.bcategory = -1
        if self.strategy == 'rebel':
            logger.debug('The ttres-chi2 strategy is "rebel", which means ttres-chi2 will be re-computed internally')
        elif self.strategy == 'obey':
            logger.debug('The ttres-chi2 strategy is "obey", which means using the ttres-chi2 is done by external program. (i.e. HQTTtResonancesTools)')
        else:
            logger.debug('The ttres-chi2 strategy is "{}"'.format(self.strategy))
        self.bcategorize = getattr(self, '_bcategorize_{}'.format(self.strategy))
        self._lepton = ROOT.Math.PtEtaPhiEVector()
    def passes(self, ev, lepton = None):
        self.reset()
        self.met.SetCoordinates(ev.met_met, 0, ev.met_phi, ev.met_met)
        lepton = lepton or self._lepton
        if len(ev.el_pt) == 1:
            lepton.SetCoordinates(ev.el_pt[0], ev.el_eta[0], ev.el_phi[0], ev.el_e[0])
        elif len(ev.mu_pt) == 1:
            lepton.SetCoordinates(ev.mu_pt[0], ev.mu_eta[0], ev.mu_phi[0], ev.mu_e[0])
        ROOT.TopNtupleAnalysis.getMtt(lepton, self.bot_tagger._jet_p4, self.bot_tagger.jet_isbtagged, self.met)
        self.mtt = ROOT.TopNtupleAnalysis.res_mtt()*1e-3
        self.mtl = ROOT.TopNtupleAnalysis.res_mtl()*1e-3
        self.mth = ROOT.TopNtupleAnalysis.res_mth()*1e-3
        self.mwh = ROOT.TopNtupleAnalysis.res_mwh()*1e-3
        self.chi2 = ROOT.TopNtupleAnalysis.res_chi2()
        self.bcategorize(ev)
        return (0 <= self.chi2 < self.max_chi2)
    def reset(self):
        self.mtt = -1
        self.mtl = -1
        self.mth = -1
        self.mwh = -1
        self.chi2 = -999
        self.bcategory = -1
    def _bcategorize_obey(self, ev):
        raise DeprecationWarning("This is temporarily deprecated til we fix the bug of TtresChi2 btagging categorization in HQTTtResonancesTools -- 16.07.2018")
        self.bcategory = ev.Btagcat
    def _bcategorize_rebel(self, ev):
        self.bcategory = ROOT.TopNtupleAnalysis.res_bcat()
    def _bcategorize_deltaR(self, ev):
        '''
        
        This is to replicate the deltaR association used in HQTTtResonancesTools for debugging purpose.
        
        '''
        p4_th = self.get_tv("Th")
        p4_tl = self.get_tv("Tl")
        btagCat = 0
        if not any(self.bot_tagger.tjet_isbtagged):
            btagCat = -1
        else:
            for tjet_p4, isbtagged in zip(self.bot_tagger._tjet_p4, self.bot_tagger.tjet_isbtagged):
                if not isbtagged:
                    continue
                if ROOT.Math.VectorUtil.DeltaR(p4_tl, tjet_p4) < 1.:
                    btagCat = 1
                if ROOT.Math.VectorUtil.DeltaR(p4_th, tjet_p4) < 1.:
                    if btagCat != 1:
                        btagCat = 2
                    else:
                        btagCat = 3
                        break
        self.bcategory = btagCat


    def get_tv(self, target):
        return ROOT.TopNtupleAnalysis.res_tv(target)*1e-3

class BoostedTopTagger(Selection):
    """Boosted hadronic-top tagger

    Used for hadronic-top tagging flag specification. 
    Note that in the case of resolved selections, this is also used in order to __veto__ the event which has at least one boosted top.

    Parameters
    ----------
    expr : {str}
            Input expression. e.g., (isTopTagged_50|isTopTagged_80)&isWTagged_80
    ljet_prefix : {str}, optional
    index_id : {str}, optional
            which translates "(isTopTagged_50|isTopTagged_80)&isWTagged_80" to "(ljet_isTopTagged_50[i]|isTopTagged_80[i])&isWTagged_80[i]"), where 'i' is the id of the item.
    """
    WP2D = {'DNNTopQuarkContained80': {'short':'dnn_contained80', 'status': ('calibrated',)},
            'DNNTopQuarkContained50': {'short':'dnn_contained50'},
            'DNNTopQuarkInclusive80': {'short':'dnn_inclusive80'},
            'DNNTopQuarkInclusive50': {'short':'dnn_inclusive50'},
            }
    def __init__(self, _callable = None, num_top = 1, min_pt = 300000, strategy = 'obey', bot_tagger = None, do_truth_matching = False, leading_only = False, _SF_callable = None):
        logger.info("Select events contain at least {} hadronic-top candidate(s) with pt > {} MeV".format(num_top, min_pt))
        if not callable(_callable):
            logger.info('StrExpression: "{}"'.format(_callable))
        self.num_top = num_top
        self.min_pt = min_pt
        self.leading_only = leading_only
        if self.leading_only:
            logger.info('`Leading-only` scenario is chosen. Only events with leading {} large-R jets all top-tagged will pass.'.format(self.num_top))
        else:
            logger.info('`Leading-only` scenario is NOT chosen. All events with at least {} top-tagged large-R jets will pass.'.format(self.num_top))
        self.do_truth_matching = do_truth_matching
        self.absdPhiJJRange = (1.6, float('inf'))
        self.absdYJJRange = (float('-inf'), 1.8)
        self.bcategory = -1
        self.ljet_istoptagged = []
        self.ljet_angularcuts = []
        self.ljet_selected = []
        self.ljet_truthjetid = []
        self.ljet_toptagSF = []
        self.ljet_p4 = ROOT.vector('ROOT::Math::PtEtaPhiMVector')()
        if self.do_truth_matching:
            self.truth_ljet_p4 = ROOT.vector('ROOT::Math::PtEtaPhiMVector')()
        if not callable(_callable):
            _callable, SF = helpers.branch_parser(_callable, name_fmt = "ljet_{}", index_id = "i",
                                          ast_kwds = dict(calib_taggers_expr = [d['short'] for d in self.WP2D.itervalues() if 'calibrated' in d.setdefault('status', tuple())]))
        self._top_tagger = _callable
        self._SF = SF if _SF_callable is None else _SF_callable
        self._SFreader = re.compile(r'^toptagSF_(?P<row>\d+)__1(?P<direction>(up|down))$')
        self.scale_factor = getattr(self, '_perjet_scale_factor')
        self.passed = False
        self._bot_tagger = bot_tagger
        self.strategy = strategy
        if self.strategy == 'obey':
            self.passes = self._passes_obey
        elif self.strategy == 'rebel':
            self.passes = self._passes_rebel
    def _alg(self, ev):
        del self.ljet_istoptagged[:]
        for i in xrange(len(ev.ljet_pt)):
            if ev.ljet_pt[i] < self.min_pt:
                self.ljet_istoptagged.append(0)
            else:
                self.ljet_istoptagged.append(self._top_tagger(ev, i))
    def retrieve_ljet_p4(self, ev):
        self.ljet_p4.clear()
        for i in xrange(ev.ljet_pt.size()):
            self.ljet_p4.push_back((ev.ljet_pt[i], ev.ljet_eta[i], ev.ljet_phi[i],ev.ljet_m[i]))
    def retrieve_truth_ljet_p4(self, ev):
        self.truth_ljet_p4.clear()
        for i in xrange(ev.akt10truthjet_pt.size()):
            self.truth_ljet_p4.push_back((ev.akt10truthjet_pt[i], ev.akt10truthjet_eta[i], ev.akt10truthjet_phi[i], ev.akt10truthjet_m[i]))
    def bcategorize(self, ev, bot_tagger = None):
        if not any(helpers.char2int(tagged) for tagged in self._bot_tagger.tjet_isbtagged):
            self.bcategory = -1
            return 
        if self.num_top == 1:
            # In l+jets analysis, we have the b-tagging categories properly stored
            self.bcategory = ev.Btagcat
        else:
            # In fully hadronic channel, we need to do it manually
            btagCat = 0
            i_top = 0
            for i, isselected in enumerate(self.ljet_selected):
                if not isselected:
                    continue
                i_top += 1
                if self._bot_tagger.ljet_isbtagged[i]:
                    if btagCat == 1:
                        btagCat = 3
                    else:
                        btagCat = i_top
            self.bcategory = btagCat
    def _passes_obey(self, ev):
        del self.ljet_selected[:]
        self.retrieve_ljet_p4(ev)
        self._alg(ev)
        self.ljet_selected[:] = self.ljet_istoptagged[:]
        self.passed = sum(self.ljet_selected if not self.leading_only else self.ljet_selected[:self.num_top]) >= self.num_top
        if self._bot_tagger != None:
            self.bcategorize(ev)
        if self.do_truth_matching:
            self.truth_matching(ev)
        return self.passed
    def angularcuts(self, ev):
        # This is a temporary solution. will be implemented in HQTTtresTools and be utilized directly here in the future
        ret = []
        _ljet_selected = []
        for i1, p4_i1 in enumerate(self.ljet_p4):
            ret.append([])
            _ljet_selected.append(0)
            for i2, p4_i2 in enumerate(self.ljet_p4):
                ret[-1].append(int((i1 < i2) and \
                                   (self.absdPhiJJRange[0] < abs(ROOT.Math.VectorUtil.DeltaPhi(p4_i1,p4_i2)) < self.absdPhiJJRange[1]) and \
                                   (self.absdYJJRange[0] < abs(p4_i1.Rapidity()-p4_i2.Rapidity()) < self.absdYJJRange[1])
                                   ))
        self.ljet_angularcuts = ret
        for i in xrange(len(self.ljet_angularcuts)):
            for j in xrange(len(self.ljet_angularcuts[i])):
                if i >= j:
                    continue
                if self.ljet_istoptagged[i] * self.ljet_istoptagged[j]:
                    if self.ljet_angularcuts[i][j]:
                        _ljet_selected[i] = _ljet_selected[j] = 1
                    self.ljet_selected = _ljet_selected
                    return
        self.ljet_selected = _ljet_selected

    def _passes_rebel(self, ev):
        del self.ljet_selected[:]
        self.retrieve_ljet_p4(ev)
        self._alg(ev)
        self.angularcuts(ev)
        self.passed = sum(self.ljet_selected if not self.leading_only else self.ljet_selected[:self.num_top]) >= self.num_top
        if self._bot_tagger != None:
            self.bcategorize(ev)
        if self.do_truth_matching:
            self.truth_matching(ev)
        return self.passed

    def truth_matching(self, ev):
        if ev.mcChannelNumber == 0:
            return
        self.retrieve_truth_ljet_p4(ev)
        ljet_truthjetid = []
        for ljet_p4 in self.ljet_p4:
            truth_ljet_i = -999 # -999 means no match
            for i, truth_ljet_p4 in enumerate(self.truth_ljet_p4):
                if (ROOT.Math.VectorUtil.DeltaR(ljet_p4, truth_ljet_p4) < 0.8):
                    # minimum double matching
                    # >>> 1. if find no unique match so far, continue searching.
                    # >>> 2. if in the end still find no unique match, retrieve the one with highest pT
                    if i in ljet_truthjetid:
                        if truth_ljet_i < 0:
                            truth_ljet_i = i
                    else:
                        truth_ljet_i = i
                        break
            ljet_truthjetid.append(truth_ljet_i)
        self.ljet_truthjetid[:] = ljet_truthjetid[:]

    def parton_matching(self, ev):
        raise NotImplementedError

    def _perjet_scale_factor(self, ev, systematic_variation = ''):
        del self.ljet_toptagSF[:]
        matched = self._SFreader.match(systematic_variation)
        if matched:
            temp = matched.groupdict()
            direction = temp['direction']
            row_i = int(temp['row'])
        else: #not a top-tagging variation, so take the nominal
            direction = ''
            row_i = 0
        for i in xrange(len(ev.ljet_pt)):
            if ev.ljet_pt[i] < self.min_pt:
                self.ljet_toptagSF.append(1)
            else:
                self.ljet_toptagSF.append(self._SF(ev, i, direction, row_i))
        scale_factor = 1.
        for SF in self.ljet_toptagSF[:self.num_top if self.leading_only else None]:
            scale_factor *= SF
        return scale_factor

class TrackJetBotTagger(Selection):
    WP2D = {'AntiKt2PV0TrackJets':
            {
             'MV2c10':    {'FixedCutBEff60':  0.86, 'FixedCutBEff70':  0.66, 'FixedCutBEff77':  0.38, 'FixedCutBEff85': -0.15, 'pt': 10e3},
             'MV2c10mu':  {'FixedCutBEff60':  0.95, 'FixedCutBEff70':  0.87, 'FixedCutBEff77':  0.71, 'FixedCutBEff85':  0.23, 'pt': 10e3, 'status': ('deprecated',)},
             'MV2c10rnn': {'FixedCutBEff60':  0.96, 'FixedCutBEff70':  0.87, 'FixedCutBEff77':  0.71, 'FixedCutBEff85':  0.26, 'pt': 10e3, 'status': ('deprecated',)},
             'DL1':       {'FixedCutBEff60':  2.74, 'FixedCutBEff70':  2.02, 'FixedCutBEff77':  1.45, 'FixedCutBEff85':  0.46, 'pt': 10e3},
             'DL1mu':     {'FixedCutBEff60':  2.72, 'FixedCutBEff70':  1.83, 'FixedCutBEff77':  1.10, 'FixedCutBEff85':  0.12, 'pt': 10e3, 'status': ('deprecated',)},
             'DL1rnn':    {'FixedCutBEff60':  4.31, 'FixedCutBEff70':  2.98, 'FixedCutBEff77':  2.23, 'FixedCutBEff85':  1.32, 'pt': 10e3, 'status': ('deprecated',)}
            },

            'AntiKtVR30Rmax4Rmin02TrackJets':
            {
             'MV2c10':    {'FixedCutBEff60':  0.92, 'FixedCutBEff70':  0.79, 'FixedCutBEff77':  0.58, 'FixedCutBEff85':  0.05, 'pt':  10e3},
             'MV2r': {'pt': 10e3, 'status': ('uncalibrated',)},
             'MV2rmu': {'pt': 10e3, 'status': ('uncalibrated',)},
             'DL1':    {'pt': 10e3},
             'DL1r': {'pt': 10e3, 'status': ('uncalibrated',)},
             'DL1rmu': {'pt': 10e3, 'status': ('uncalibrated',)},
            }
            }
    # https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/BTaggingBenchmarksRelease21 -- 01.18.2018
    def __init__(self, algorithm = 'MV2c10',
                       WP = 'FixedCutBEff70',
                       trackjet_alg = 'AntiKtVR30Rmax4Rmin02TrackJets',
                       strategy = 'obey',
                       do_association = True,
                       do_ljet_association = False,
                       do_truth_matching = True,
                       SF_type = 'eventlevel',
                       min_nbjets = 1):
        self.algorithm = algorithm
        self.WP = WP
        self.trackjet_alg = trackjet_alg
        self.max_deltaR = 0.4 # Used for `do_association`
        self.max_ljet_deltaR = 1.0 # Used for `do_ljet_association`
        self.do_association = do_association
        self.do_ljet_association = do_ljet_association
        self.do_truth_matching = do_truth_matching
        is_HybWP = 'HybBEff' in self.WP
        self._branch_map = {'tjet_isbtagged': 'tjet_isbtagged_{alg}_{WP}'.format(alg = self.algorithm, WP = ('HybBEff_' if is_HybWP else '') + self.WP.split('BEff')[-1]),
                            'tjet_SF': 'tjet_btag_SF_{alg}_{WP}'.format(alg = self.algorithm, WP = ('HybBEff_' if is_HybWP else '') + self.WP.split('BEff')[-1]),
                            'weight_SF': 'weight_trackjet_bTagSF_{alg}_{WP}'.format(alg = self.algorithm, WP = ('HybBEff_' if is_HybWP else '') + self.WP.split('BEff')[-1]),
                            'tjet_discriminant': 'tjet_{alg}'.format(alg = self.algorithm.lower())}
        if is_HybWP and strategy == 'rebel':
            logger.warn('When using Hybrid WP, the b-tagging strategy should always be `obey`!')
            self.strategy = 'obey'
        else:
            self.strategy = strategy
        recomm = self.WP2D.get(self.trackjet_alg, {}).get(self.algorithm, {})
        if 'uncalibrated' in recomm.get('status', tuple()):
            logger.warn('This b-tagging WP is not yet calibrated. Unity scale factor will be used')
            SF_type = 'uncalib'
        self.scale_factor = getattr(self, '_' + SF_type + '_scale_factor')
        self.min_discriminant = recomm.get(WP, -999) # Note that this will not be considered if the strategy is `obey`
        self.min_pt = recomm.get('pt', 10e3) # Note that this will not be considered if the strategy is `obey`
        self.min_nbjets = min_nbjets
        logger.info("Select events contain at least {} b-tagged trk-jets with pt > {} MeV".format(self.min_nbjets, self.min_pt))
        if self.strategy == 'rebel':
            logger.debug('The b-tagging strategy is "rebel", which means b-tagging will be re-computed internally')
            if self.min_discriminant == -999:
                raise KeyError('For STRATEGY("rebel"), you always need an available "Alg./WP" stored in WP2D!')
        elif self.strategy == 'obey':
            logger.debug('The b-tagging strategy is "obey", which means using the b-tagging is done by external program. (i.e. HQTTtResonancesTools)')
        self.passes = getattr(self, '_passes_{}'.format(self.strategy))
        self._tjet_p4 = ROOT.vector('ROOT::Math::PtEtaPhiEVector')()
        self._jet_p4 = ROOT.vector(ROOT.Math.PtEtaPhiEVector)() # Used for `do_association`
        self.jet_isbtagged = ROOT.vector('bool')() # if any of the associated track jets is b-tagged. Not used in boosted channel
        self.jet_associated_btaggedtjet_index = ROOT.vector('int')()
        self._ljet_p4 = ROOT.vector('ROOT::Math::PtEtaPhiMVector')() # Used for `do_association`
        self.ljet_isbtagged = ROOT.vector('bool')() # if any of the associated track jets is b-tagged. Used in boosted full-hadronic analysis
        self.ljet_associated_btaggedtjet_index = ROOT.vector('int')()
        self.tjet_isbtagged = ROOT.vector(int)()

    def _passes_obey(self, ev):
        self.tjet_isbtagged.clear()
        self._tjet_p4.clear()
        for tagged in getattr(ev, self._branch_map['tjet_isbtagged']):
            self.tjet_isbtagged.push_back(helpers.char2int(tagged))
        for i in xrange(len(ev.tjet_pt)):
            self._tjet_p4.push_back((ev.tjet_pt[i], ev.tjet_eta[i], ev.tjet_phi[i], ev.tjet_e[i]))
        if self.do_association:
            self.association(ev)
        if self.do_ljet_association:
            self.ljet_association(ev)
        if self.do_truth_matching:
            self.truth_matching(ev)
        if self.min_nbjets == 0:
            return True
        return (sum(self.tjet_isbtagged) >= self.min_nbjets)

    def _passes_rebel(self, ev):
        self.tjet_isbtagged.clear()
        self._tjet_p4.clear()
        for i, discriminant in enumerate(getattr(ev, self._branch_map['tjet_discriminant'])):
            if ev.tjet_pt[i] > self.min_pt and math.fabs(ev.tjet_eta[i]) < 2.5 and ev.tjet_numConstituents[i] >= 2:
                self._tjet_p4.push_back((ev.tjet_pt[i], ev.tjet_eta[i], ev.tjet_phi[i],ev.tjet_e[i]))
                self.tjet_isbtagged.push_back(discriminant > self.min_discriminant)
            else:
                self._tjet_p4.push_back((ev.tjet_pt[i], ev.tjet_eta[i], ev.tjet_phi[i],ev.tjet_e[i]))
                self.tjet_isbtagged.push_back(False)
        if self.do_association:
            self.association(ev)
        if self.do_ljet_association:
            self.ljet_association(ev)
        if self.do_truth_matching:
            self.truth_matching(ev)
        if self.min_nbjets == 0:
            return True
        return (sum(self.tjet_isbtagged) >= self.min_nbjets)


    def associated(self, p4_1, p4_2, max_deltaR):
        deltaR = ROOT.Math.VectorUtil.DeltaR(p4_1, p4_2)
        return (deltaR < max_deltaR)

    def association(self, ev):
        self.jet_isbtagged.clear()
        self._jet_p4.clear()
        self.jet_associated_btaggedtjet_index.clear()
        for jet_i in xrange(len(ev.jet_pt)):
            self._jet_p4.push_back(((ev.jet_pt[jet_i], ev.jet_eta[jet_i], ev.jet_phi[jet_i], ev.jet_e[jet_i])))
            trkbjet_associated = False
            associated_btaggedtjet_index = -999
            for tjet_i in xrange(len(ev.tjet_pt)):
                if self.tjet_isbtagged[tjet_i] and self.associated(self._tjet_p4[tjet_i], self._jet_p4[jet_i], self.max_deltaR):
                    trkbjet_associated = True
                    associated_btaggedtjet_index = tjet_i
                    break
            self.jet_isbtagged.push_back(trkbjet_associated)
            self.jet_associated_btaggedtjet_index.push_back(associated_btaggedtjet_index)

    def ljet_association(self, ev):
        self.ljet_isbtagged.clear()
        self._ljet_p4.clear()
        self.ljet_associated_btaggedtjet_index.clear()
        for ljet_i in xrange(len(ev.ljet_pt)):
            self._ljet_p4.push_back((ev.ljet_pt[ljet_i], ev.ljet_eta[ljet_i], ev.ljet_phi[ljet_i], ev.ljet_m[ljet_i]))
            trkbjet_associated = False
            associated_btaggedtjet_index = -999
            for tjet_i in xrange(len(ev.tjet_pt)):
                if self.tjet_isbtagged[tjet_i] and self.associated(self._tjet_p4[tjet_i], self._ljet_p4[ljet_i], self.max_ljet_deltaR):
                    trkbjet_associated = True
                    associated_btaggedtjet_index = tjet_i
                    break
            self.ljet_isbtagged.push_back(trkbjet_associated)
            self.ljet_associated_btaggedtjet_index.push_back(associated_btaggedtjet_index)

    def truth_matching(self, ev):
        if ev.mcChannelNumber == 0:
            return
        self.tjet_istrueb = [label==5 for label in ev.tjet_label]

    def _uncalib_scale_factor(self, ev, systematic_variation = ''):
        return 1.

    def _perjet_scale_factor(self, ev, systematic_variation = ''):
        """
        Retrieve the b-tagging scale factor with systematic variations specified accordingly

        systematic variations are specified according to this syntax:
        btag[A]SF_[eig][_pt[X]]__1[up/down]
        where:
        [A] = b,c,l,e for b-jet, c-jet, light-jet or extrapolation variations
        [eig] is the number of the eigen vector
        [X] is the number of the pt bin if we want to vary only jets within a pt bin
        if there is no 'btag' in the name of the variation, then the nominal SF is used
        
        Parameters
        ----------
        ev : [TChain]
            selected event chain
        systematic_variation : [str]
            systematic variation flag
        
        Returns
        -------
        btagSF: [float]
            b-tagging scale factor
        
        """
        pref =  self._branch_map['tjet_SF']
        varName = ''
        nomName = pref
        ptbinInS = 0
        eig = -1
        # if this is a b-tagging variation
        # then check which branch to take to apply the variation
        if 'btag' in systematic_variation:
            # if we are also varying only jets in a specific pt bin, the pt bin is identified as "ptX", where X is an integer
            # get "X" as an integer from the systematic name
            if 'pt' in systematic_variation:
                ptbinInS = int(systematic_variation.split('pt')[1][0])
                # later, if this is != -1, we will use it to apply the variation only at the jets within this pt bin
            # get direction
            direction = 'up'
            if 'down' in systematic_variation:
                direction = 'down'
            # check if it is a b,c,light or extrapolation variation and set name
            if 'btagbSF_' in systematic_variation:
                varName = pref+'_eigen_B_'+direction
                # get eigenvector index
                eig = int(systematic_variation.split('_')[1])
            elif 'btagcSF_' in systematic_variation:
                varName = pref+'_eigen_C_'+direction
                # get eigenvector index
                eig = int(systematic_variation.split('_')[1])
            elif 'btaglSF_' in systematic_variation:
                varName = pref+'_eigen_Light_'+direction
                # get eigenvector index
                eig = int(systematic_variation.split('_')[1])
            elif 'btageSF_0' in systematic_variation:
                varName = pref+'_syst_extrapolation_'+direction
                eig = -1
            elif 'btageSF_1' in systematic_variation:
                varName = pref+'_syst_extrapolation_from_charm_'+direction
                eig = -1
        else: # not a b-tagging variation, so take the nominal
            varName = pref

        scale_factor = 1.
        # loop over track jets
        for i, tjet_p4 in enumerate(self._tjet_p4):
            # if we requested to vary only jets in a specific pt bin, check if this jet is in the pt bin
            vetoed = False
            if ptbinInS != 0:
                ptbin = 0
                if tjet_p4.Perp() < 50e3:
                    ptbin = 1
                elif tjet_p4.Perp() < 100e3:
                    ptbin = 2
                else:
                    ptbin = 3
                if ptbinInS == ptbin:
                    # if this jet is in the correct pt bin, apply the syst. variation
                    tjet_SF = getattr(ev, varName)
                else:
                    # otherwise, take the nominal SF for this jet
                    # even if we are supposed to vary it for any other criteria
                    tjet_SF = getattr(ev, nomName)
                    vetoed = True
            else: # we have not requested the pt binned variation
                # so we always vary all jets, regardless of the pt bin
                # if no variation was requested, varName will be set to the nominal above
                tjet_SF = getattr(ev, varName)
            if eig > -1 and not vetoed: # branches in b,c,light variation have a second index related to the eigenvector number
                scale_factor *= tjet_SF[i][eig]
            else: # extrapolation branches or the nominal, have no second index
                scale_factor *= tjet_SF[i]
        return scale_factor
    def _eventlevel_scale_factor(self, ev, systematic_variation = ''):
        '''
        Use the event-level b-tagging efficiency scale factors from AnalysisTop. 
        trk jet pT-dependent SF is not available.
        '''
        pref = self._branch_map['weight_SF']
        if 'btag' in systematic_variation:
            # get direction
            direction = 'up'
            if 'down' in systematic_variation:
                direction = 'down'
            # check if it is a b,c,light or extrapolation variation and set name
            if 'btagbSF_' in systematic_variation:
                varName = '{}_eigenvars_B_{}'.format(pref, direction)
                # get eigenvector index
                eig = int(systematic_variation.split('_')[1])
                scale_factor = getattr(ev, varName)[eig]
            elif 'btagcSF_' in systematic_variation:
                varName = '{}_eigenvars_C_{}'.format(pref, direction)
                # get eigenvector index
                eig = int(systematic_variation.split('_')[1])
                scale_factor = getattr(ev, varName)[eig]
            elif 'btaglSF_' in systematic_variation:
                varName = '{}_eigenvars_Light_{}'.format(pref, direction)
                # get eigenvector index
                eig = int(systematic_variation.split('_')[1])
                scale_factor = getattr(ev, varName)[eig]
            elif 'btageSF_0' in systematic_variation:
                varName = '{}_extrapolation_{}'.format(pref, direction)
                scale_factor = getattr(ev, varName)
            elif 'btageSF_1' in systematic_variation:
                varName = '{}_extrapolation_from_charm_{}'.format(pref, direction)
                scale_factor = getattr(ev, varName)
            
        else: # not a b-tagging variation, so take the nominal
            varName = pref
            scale_factor = getattr(ev, varName)
        return scale_factor

class AuxSelector(Selection):
    def __init__(self, _callable = ''):
        if type(_callable) == str and bool(_callable):
            self._alg = lambda ev: eval(compile(_callable, '<auxiliary-selector>', 'eval'), {'ev': ev})
        else:
            self._alg = lambda ev: True
        self.passed = False
    def passes(self, ev):
        self.passed = self._alg(ev)
        return self.passed