import helpers
import ROOT
import wjets
import copy
from collections import defaultdict
logger = helpers.getLogger('TopNtupleAnalysis.reweighting')

class Reweighter(object):
    SYSTS = {'*': 0}
    @classmethod
    def get_SF(cls, ev, syst):
        raise NotImplementedError
    @classmethod
    def init(cls, mcChannelNumber):
        pass
    @classmethod
    def get_weight(cls, ev, syst = '', w0 = 1):
        """Retrieve the scale factor
        
        Parameters
        ----------
        ev : {TTree, TTchain}
        syst : {string}, optional
        w0 : {float}, optional
            original weight
        
        Returns
        -------
        float
            weight
        """
        if syst not in cls.SYSTS:
            syst = '*'
        SF = cls.get_SF(ev, cls.SYSTS[syst])
        if SF == 0.:
            logger.debug('<{cls.__name__}> retrieves ScaleFactor which is ZERO.'.format(cls = cls))
        elif SF < 0.:
            logger.debug('<{cls.__name__}> retrieves ScaleFactor which is NEGATIVE.'.format(cls = cls))
        w = w0*SF
        return w

class IDDefaultDict(defaultdict):
    def __missing__(self, key):
        return self.default_factory(key)

class EWKCorrection(Reweighter):
    RUN_NUMBERS = [410471, 410470, 410000, 301528, 301529, 301530, 301531, 301532]
    RUN_NUMBERS += [410633, 410634, 410635, 410636, 410637] # mttsliced nonallhad
    RUN_NUMBERS += [410284, 410285, 410286, 410287, 410288] # mttsliced allhad
    SYSTS = {'ttEWK__1up': 1, 'ttEWK__1down': 2, '*': 0}
    top = ROOT.TLorentzVector()
    topbar = ROOT.TLorentzVector()
    @classmethod
    def init(cls, mcChannelNumber):
        logger.warn(DeprecationWarning('{} is deprecated. Consider to use the new `TTbarNNLOReweighting`'.format(cls.__name__)))
        logger.info('Note that this is considered as a correction, i.e. change the nominal values')
    @classmethod
    def get_SF(cls, ev, s):
        if ev.mcChannelNumber == 0:
            return 1.
        if ev.mcChannelNumber not in cls.RUN_NUMBERS:
            return 1.
        cls.top.SetPtEtaPhiM(ev.MC_t_pt, ev.MC_t_eta, ev.MC_t_phi, ev.MC_t_m)
        cls.topbar.SetPtEtaPhiM(ev.MC_tbar_pt, ev.MC_tbar_eta, ev.MC_tbar_phi, ev.MC_tbar_m)
        w = ROOT.TopNtupleAnalysis.getEWK(cls.top, cls.topbar, ev.initial_type, s)
        return w

class NNLOReweighting(Reweighter):
    RUN_NUMBERS = [410471, 410470, 410000, 301528, 301529, 301530, 301531, 301532]
    RUN_NUMBERS += [410633, 410634, 410635, 410636, 410637] # mttsliced nonallhad
    RUN_NUMBERS += [410284, 410285, 410286, 410287, 410288] # mttsliced allhad
    SYSTS = {'ttNNLO_seqExtended__1up': 1, 'ttNNLO_seqExtended__1down': -1,
             'ttNNLO_topPt__1up': 2, 'ttNNLO_topPt__1down': -2,
             'ttNNLO_topPtDiff__1up': 3, 'ttNNLO_topPtDiff__1down': -3,
             'ttNNLO_seqExtended__1up': 4, 'ttNNLO_seqExtended__1down': -4,
             '*': 0
             }
    @classmethod
    def init(cls, mcChannelNumber):
        logger.warn(DeprecationWarning('{} is deprecated. Consider to use the new `TTbarNNLOReweighting`'.format(cls.__name__)))
        if mcChannelNumber not in cls.RUN_NUMBERS:
            logger.info('<{}> is not a registered ttbar sample. NNLO Reweighter will not be activated.'.format(mcChannelNumber))
        else:
            logger.info('<{}> is a registered ttbar sample. NNLO Reweighter will be activated.'.format(mcChannelNumber))
            logger.info('Note that this is only consdier as a systematic not a correction, i.e. __DON\'T__ change the nominal values')
            if mcChannelNumber in [301528, 301529, 301530, 301531, 301532]:
                mcChannelNumber = 410000
            elif mcChannelNumber in [410284, 410285, 410286, 410287, 410288]:
                mcChannelNumber = 410471
            elif mcChannelNumber in [410633, 410634, 410635, 410636, 410637]:
                mcChannelNumber = 410470
            ROOT.TopNtupleAnalysis.InitNNLO(mcChannelNumber)
    @classmethod
    def get_SF(cls, ev, s):
        if ev.mcChannelNumber == 0:
            return 1.
        abss = abs(s) # we only have 1up always
        if abss == 0:
            return 1.
        if abss == 1:
            return ROOT.TopNtupleAnalysis.getNNLOWeight(ev.MC_ttbar_afterFSR_pt, ev.MC_t_afterFSR_pt, 1)
        if abss == 2:
            return ROOT.TopNtupleAnalysis.getNNLOWeight(ev.MC_ttbar_afterFSR_pt, ev.MC_t_afterFSR_pt, 0)
        if abss == 3:
            return ROOT.TopNtupleAnalysis.getNNLOWeight(ev.MC_ttbar_afterFSR_pt, ev.MC_t_afterFSR_pt, 2)
        if abss == 4:
            return ROOT.TopNtupleAnalysis.getNNLOWeight(ev.MC_ttbar_afterFSR_pt, ev.MC_t_afterFSR_pt, 2)*ROOT.TopNtupleAnalysis.getNNLOWeight(ev.MC_ttbar_afterFSR_pt, ev.MC_t_afterFSR_pt, 1)

class TTbarNNLOReweighting(Reweighter):
    '''
    This is the latest rel.21 recommendation for NLO EWK+NNLO QCD ttbar correction.
    You shall never use it together with `EWKCorrection` or `NNLORweighting`, as it already account for both.
    TopPt, TtbarMass, TopY dependent reweighting are available. By default TopPt is considered
    '''
    RUN_NUMBERS = [410471, 410470]
    RUN_NUMBERS += [410633, 410634, 410635, 410636, 410637] # mttsliced nonallhad
    RUN_NUMBERS += [410284, 410285, 410286, 410287, 410288] # mttsliced allhad
    SYSTS = {'ttNNLOQCDNLOEWK__1up': 1, # mu_R/F=2.0
             'ttNNLOQCDNLOEWK__1down': -1, # mu_R/F = 0.5
             '*': 0
             }

    @classmethod
    def init(cls, mcChannelNumber):
        if mcChannelNumber not in cls.RUN_NUMBERS:
            logger.info('<{}> is not a registered ttbar sample. TTbarNNLOReweighting will not be activated.'.format(mcChannelNumber))
        else:
            logger.info('<{}> is a registered ttbar sample. TTbarNNLOReweighting will be activated.'.format(mcChannelNumber))
            logger.info('Note that this is considered as a correction, i.e. change the nominal values')
            if mcChannelNumber in [410284, 410285, 410286, 410287, 410288]:
                mcChannelNumber = 410471
            elif mcChannelNumber in [410633, 410634, 410635, 410636, 410637]:
                mcChannelNumber = 410470
            cls.REWEIGTER = ROOT.TTbarNNLOReweighter.TTbarNNLOReweighter(mcChannelNumber)
            cls.REWEIGTER.Init()

    @classmethod
    def get_SF(cls, ev, s):
        if ev.mcChannelNumber == 0:
            return 1.
        if ev.mcChannelNumber not in cls.RUN_NUMBERS:
            return 1.
        truth_top_pt = ev.MC_t_afterFSR_SC_pt*1e-3 # in GeV
        if s == 0:
            return cls.REWEIGTER.GetTopPt_Powheg_Pythia8_Nominal(truth_top_pt)
        if s == 1:
            return cls.REWEIGTER.GetTopPt_ScaleMax_Powheg_Pythia8_Nominal(truth_top_pt)
        if s == -1:
            return cls.REWEIGTER.GetTopPt_ScaleMin_Powheg_Pythia8_Nominal(truth_top_pt)

class WjetSystWeight(Reweighter):
    '''
    W+jets C/A and HF syst. variations
    assuming b-tagging
    '''
    RUN_NUMBERS = range(363330, 363354+1)+\
                  range(363436, 363483+1)+\
                  range(364156, 364197+1) # 2.2.1
    SYSTS = IDDefaultDict(lambda id: id)
    FLAGS = {1: 'cc', 2: 'c', 3: 'bb', 4: 'bb', 5: 'l'}
    @classmethod
    def get_SF(cls, ev, s):
        if ev.mcChannelNumber == 0:
            return 1.
        if ev.mcChannelNumber not in cls.RUN_NUMBERS:
            return 1.

        nj = 4
        if ev.jet_pt.size() > 4:
            nj = 5
        if ev.jet_pt.size() < 2:
            nj = 2

        # flavour fractions at pretag level
        frac2 = {nj: {'el': {}, 'mu': {}}}

        chan = 'not-exactly-one-charged-lepton'
        if ev.el_pt.size() == 1:
            chan = 'el'
        elif ev.mu_pt.size() == 1:
            chan = 'mu'

        # You should always have exactly one electron or muon in a good event.
        #It usually means the event selections are problematic (i.e. not exactly one electron or muon) if you get an error from here.
        syst = s if s in wjets.flav_map[nj][chan] else ''

        frac2[nj][chan][syst] = copy.deepcopy(wjets.frac[nj][chan][syst])
        for f in frac2[nj][chan][syst]:
            frac2[nj][chan][syst][f] *= wjets.flav_map[nj][chan][syst][f]

        flav = cls.FLAGS.get(ev.Wfilter_Sherpa_nT, '')

        f_ca = wjets.f_ca_map[nj][chan][syst]
        hfweight = wjets.flav_map[nj][chan][syst][flav] / sum(frac2[nj][chan][syst][f] for f in ('bb', 'cc', 'c', 'l'))
        return f_ca*hfweight