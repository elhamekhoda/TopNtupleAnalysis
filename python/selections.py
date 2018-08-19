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
    def __init__(self, bot_tagger, max_chi2 = float('inf'), strategy = 'rebel'):
        self.strategy = strategy
        self.met = ROOT.TLorentzVector()
        self.bot_tagger = bot_tagger
        self.max_chi2 = max_chi2
        self.bcategory = -1
        if self.strategy == 'rebel':
            logger.debug('The ttres-chi2 strategy is "rebel", which means ttres-chi2 will be re-computed internally')
        elif self.strategy == 'obey':
            logger.debug('The ttres-chi2 strategy is "obey", which means using the ttres-chi2 is done by external program. (i.e. HQTTtResonancesTools)')
        self.bcategorize = getattr(self, '_bcategorize_{}'.format(self.strategy))
        self._lepton = ROOT.TLorentzVector()
    def passes(self, ev, lepton = None):
        self.reset()
        self.met.SetPtEtaPhiE(ev.met_met, 0, ev.met_phi, ev.met_met)
        lepton = lepton or self._lepton
        if len(ev.el_pt) == 1:
            lepton.SetPtEtaPhiE(ev.el_pt[0], ev.el_eta[0], ev.el_phi[0], ev.el_e[0])
        elif len(ev.mu_pt) == 1:
            lepton.SetPtEtaPhiE(ev.mu_pt[0], ev.mu_eta[0], ev.mu_phi[0], ev.mu_e[0])
        ROOT.TopNtupleAnalysis.getMtt(lepton, self.bot_tagger._jet_p4, self.bot_tagger.jet_isbtagged, self.met)
        self.mtt = ROOT.TopNtupleAnalysis.res_mtt()*1e-3
        self.mtl = ROOT.TopNtupleAnalysis.res_mtl()*1e-3
        self.mth = ROOT.TopNtupleAnalysis.res_mth()*1e-3
        self.mwh = ROOT.TopNtupleAnalysis.res_mwh()*1e-3
        self.chi2 = ROOT.TopNtupleAnalysis.res_chi2()
        self.bcategorize(ev)
        return (self.chi2 < self.max_chi2)
    def reset(self):
        self.mtt = -1
        self.mtl = -1
        self.mth = -1
        self.mwh = -1
        self.chi2 = 100000
        self.bcategory = -1
    def _bcategorize_obey(self, ev):
        raise DeprecationWarning("This is temporarily deprecated til we fix the bug of TtresChi2 btagging categorization in HQTTtResonancesTools -- 16.07.2018")
        self.bcategory = ev.Btagcat
    def _bcategorize_rebel(self, ev):
        self.bcategory = ROOT.TopNtupleAnalysis.res_bcat()


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
    def __init__(self, _callable = None, num_top = 1, min_pt = 300000, strategy = 'rebel', bot_tagger = None):
        logger.info("Select events contain at least {} hadronic-top candidate(s) with pt larger than {} MeV".format(num_top, min_pt))
        if not callable(_callable):
            logger.info('StrExpression: "{}"'.format(_callable))
        self.num_top = num_top
        self.min_pt = min_pt
        self.bcategory = -1
        if not callable(_callable):
            self._expr = _callable
            def _callable(ev):
                _top_tagger = lambda i: eval(helpers.branch_parser(self._expr,
                                                                   name_fmt = "ljet_{}",
                                                                   index_id = "i"),
                                             {'char2int': helpers.char2int, 'sel': ev, 'i': i})
                n = 0
                for i in range(len(ev.ljet_pt)):
                    if ev.ljet_pt[i] < self.min_pt:
                        continue
                    if _top_tagger(i):
                        self.thad_indices.append(i)
                        n += 1
                    if n >= self.num_top:
                        break

        self._alg = _callable
        self.thad_indices = []
        self.passed = False
        self._bot_tagger = bot_tagger
    def bcategorize(self, ev, bot_tagger = None):
        btagCat = 0
        for i in self.thad_indices:
            if self._bot_tagger.ljet_isbtagged[i]:
                btagCat += 1
        self.bcategory = btagCat
    def passes(self, ev):
        self.thad_indices = []
        self._alg(ev)
        self.passed = len(self.thad_indices) >= self.num_top
        if self._bot_tagger != None:
            self.bcategorize(ev)
        return self.passed

class TrackJetBotTagger(Selection):
    WP2D = {'AntiKt2PV0TrackJets':
            {'MV2c10':    {'60':  0.86, '70':  0.66, '77':  0.38, '85': -0.15, 'pt': 10e3},
             'MV2c10mu':  {'60':  0.95, '70':  0.87, '77':  0.71, '85':  0.23, 'pt': 10e3},
             'MV2c10rnn': {'60':  0.96, '70':  0.87, '77':  0.71, '85':  0.26, 'pt': 10e3}},
            'AntiKtVR30Rmax4Rmin02TrackJets':
            {'MV2c10':    {'60':  0.92, '70':  0.79, '77':  0.58, '85':  0.05, 'pt':  7e3}}
            }
    # https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/BTaggingBenchmarksRelease21 -- 01.18.2018
    def __init__(self, algorithm = 'MV2c10', WP = '70', trackjet_alg = 'AntiKt2PV0TrackJets', systematic_variation = '', strategy = 'rebel', do_association = True, do_ljet_association = False, do_truth_matching = True):
        self.algorithm = algorithm
        self.WP = WP
        self.trackjet_alg = trackjet_alg
        self.max_deltaR = 0.4 # Used for `do_association`
        self.max_ljet_deltaR = 1.0 # Used for `do_ljet_association`
        self.systematic_variation = systematic_variation
        self.do_association = do_association
        self.do_ljet_association = do_ljet_association
        self.do_truth_matching = do_truth_matching
        if self.systematic_variation != '':
            logger.warn('Please be informed: b-tagging scale factor with systematic variations is currently not valid'
                        +' because the eigen matrix are not stored in the ttres ntuple produced by the current-version `HQTTtResonancesTools`.'
                        +' Please consult us and make sure you really know what you\'re doing!')
        self._branch_map = {'tjet_isbtagged': 'tjet_isbtagged_{alg}_{WP}'.format(alg = self.algorithm, WP = self.WP),
                            'tjet_SF': 'tjet_btag_SF_{alg}_{WP}'.format(alg = self.algorithm, WP = self.WP),
                            'tjet_discriminant': 'tjet_{alg}'.format(alg = self.algorithm.lower())}
        self.strategy = strategy
        recomm = self.WP2D.get(self.trackjet_alg, {}).get(self.algorithm, {})
        self.min_discriminant = recomm.get(WP, -999)
        self.min_pt = recomm.get('pt', 10e3)
        if self.strategy == 'rebel':
            logger.debug('The b-tagging strategy is "rebel", which means b-tagging will be re-computed internally')
        elif self.strategy == 'obey':
            logger.debug('The b-tagging strategy is "obey", which means using the b-tagging is done by external program. (i.e. HQTTtResonancesTools)')
            if self.min_discriminant == -999:
                raise KeyError('For STRATEGY("rebel"), you always need an available "Alg./WP" stored in WP2D!')
        self.passes = getattr(self, '_passes_{}'.format(self.strategy))
        self._jet_p4 = ROOT.vector('TLorentzVector')() # Used for `do_association`
        self.jet_isbtagged = ROOT.vector('bool')() # if any of the associated track jets is b-tagged. Not used in boosted channel
        self.jet_associated_btaggedtjet_index = ROOT.vector('int')()
        self._ljet_p4 = ROOT.vector('TLorentzVector')() # Used for `do_association`
        self.ljet_isbtagged = ROOT.vector('bool')() # if any of the associated track jets is b-tagged. Used in boosted full-hadronic analysis
        self.ljet_associated_btaggedtjet_index = ROOT.vector('int')()

    def _passes_obey(self, ev):
        raise DeprecationWarning("This is temporarily deprecated til we fix the bug of trk b-tagging selector in HQTTtResonancesTools -- 01.07.2018")
        self.tjet_isbtagged = getattr(ev, self._branch_map['tjet_isbtagged'])
        self._tjet_p4 = ROOT.vector('TLorentzVector')()
        for i in range(len(ev.tjet_pt)):
            p4 = ROOT.TLorentzVector()
            p4.SetPtEtaPhiE(ev.tjet_pt[i], ev.tjet_eta[i], ev.tjet_phi[i], ev.tjet_e[i])
            self._tjet_p4.push_back(p4)
        if self.do_association:
            self.association(ev)
        if self.do_truth_matching:
            self.truth_matching(ev)
        return True

    def _passes_rebel(self, ev):
        self.tjet_isbtagged = ROOT.vector(int)()
        self._tjet_p4 = ROOT.vector('TLorentzVector')()
        for i, discriminant in enumerate(getattr(ev, self._branch_map['tjet_discriminant'])):
            p4 = ROOT.TLorentzVector()
            p4.SetPtEtaPhiE(ev.tjet_pt[i], ev.tjet_eta[i], ev.tjet_phi[i],ev.tjet_e[i])
            if p4.Perp() > self.min_pt and math.fabs(p4.Eta()) < 2.5 and ev.tjet_numConstituents[i] >= 2:
                self._tjet_p4.push_back(p4)
                self.tjet_isbtagged.push_back(discriminant > self.min_discriminant)
        if self.do_association:
            self.association(ev)
        if self.do_ljet_association:
            self.ljet_association(ev)
        if self.do_truth_matching:
            self.truth_matching(ev)
        return any(self.tjet_isbtagged)


    def associated(self, tjet_i, jet_i, max_deltaR, ev):
        deltaR = self._jet_p4[jet_i].DeltaR(self._tjet_p4[tjet_i])
        return (deltaR < max_deltaR)

    def association(self, ev):
        self.jet_isbtagged.clear()
        self._jet_p4.clear()
        self.jet_associated_btaggedtjet_index.clear()
        for jet_i in range(len(ev.jet_pt)):
            jet_p4 = ROOT.TLorentzVector()
            jet_p4.SetPtEtaPhiE(ev.jet_pt[jet_i], ev.jet_eta[jet_i], ev.jet_phi[jet_i], ev.jet_e[jet_i])
            self._jet_p4.push_back(jet_p4)
            trkbjet_associated = False
            associated_btaggedtjet_index = -1
            for tjet_i in range(len(ev.tjet_pt)):
                if self.tjet_isbtagged[tjet_i] and self.associated(tjet_i, jet_i, self.max_deltaR, ev):
                    trkbjet_associated = True
                    associated_btaggedtjet_index = tjet_i
                    break
            self.jet_isbtagged.push_back(trkbjet_associated)
            self.jet_associated_btaggedtjet_index.push_back(associated_btaggedtjet_index)

    def ljet_association(self, ev):
        self.ljet_isbtagged.clear()
        self._ljet_p4.clear()
        self.ljet_associated_btaggedtjet_index.clear()
        for ljet_i in range(len(ev.ljet_pt)):
            ljet_p4 = ROOT.TLorentzVector()
            ljet_p4.SetPtEtaPhiE(ev.ljet_pt[ljet_i], ev.ljet_eta[ljet_i], ev.ljet_phi[ljet_i], ev.ljet_e[ljet_i])
            self._ljet_p4.push_back(ljet_p4)
            trkbjet_associated = False
            associated_btaggedtjet_index = -1
            for tjet_i in range(len(ev.tjet_pt)):
                if self.tjet_isbtagged[tjet_i] and self.associated(tjet_i, ljet_i, self.max_ljet_deltaR, ev):
                    trkbjet_associated = True
                    associated_btaggedtjet_index = tjet_i
                    break
            self.ljet_isbtagged.push_back(trkbjet_associated)
            self.ljet_associated_btaggedtjet_index.push_back(associated_btaggedtjet_index)

    def truth_matching(self, ev):
        self.tjet_istrueb = [label==5 for label in ev.tjet_label]

    def scale_factor(self, ev):
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
        systematic_variation = self.systematic_variation
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
            if 'btagcSF_' in systematic_variation:
                varName = pref+'_eigen_C_'+direction
                # get eigenvector index
                eig = int(systematic_variation.split('_')[1])
            if 'btaglSF_' in systematic_variation:
                varName = pref+'_eigen_Light_'+direction
                # get eigenvector index
                eig = int(systematic_variation.split('_')[1])
            if 'btageSF_0' in systematic_variation:
                varName = pref+'_syst_extrapolation_'+direction
                eig = -1
            if 'btageSF_1' in systematic_variation:
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