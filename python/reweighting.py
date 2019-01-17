import helpers
import ROOT
logger = helpers.getLogger('TopNtupleAnalysis.reweighting')

class Reweighter(object):
    SYSTS = {'*': 0}
    @classmethod
    def get_SF(cls, ev, syst):
        raise NotImplementedError
    @classmethod
    def get_weight(cls, ev, syst = '', w0 = 1):
        """Retrieve the scale factor
        
        Parameters
        ----------
        ev : {TTree}
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
        return w0*cls.get_SF(ev, cls.SYSTS[syst])

class EWKCorrection(Reweighter):
    RUN_NUMBERS = [410471, 410470, 410000, 301528, 301529, 301530, 301531, 301532]
    RUN_NUMBERS += [410633, 410634, 410635, 410636, 410637] # mttsliced nonallhad
    RUN_NUMBERS += [410284, 410285, 410286, 410287, 410288] # mttsliced allhad
    SYSTS = {'ttEWK__1up': 1, 'ttEWK__1down': 2, '*': 0}
    top = ROOT.TLorentzVector()
    topbar = ROOT.TLorentzVector()
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
    def initNNLO(cls, mcChannelNumber):
        if mcChannelNumber not in cls.RUN_NUMBERS:
            logger.info('<{}> is not a registered ttbar sample. NNLO Reweighter will not be activated.'.format(mcChannelNumber))
        else:
            logger.info('<{}> is a registered ttbar sample. NNLO Reweighter will be activated.'.format(mcChannelNumber))
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
