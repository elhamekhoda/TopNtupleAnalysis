import ROOT

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
    SYSTS = {'ttEWK__1up': 1, 'ttEWK__1down': 2, '*': 0}
    @classmethod
    def get_SF(cls, ev, s):
        if ev.mcChannelNumber == 0:
            return 1.
        if ev.mcChannelNumber not in cls.RUN_NUMBERS:
            return 1.
        top = ROOT.TLorentzVector()
        top.SetPtEtaPhiM(ev.MC_t_pt, ev.MC_t_eta, ev.MC_t_phi, ev.MC_t_m)
        topbar = ROOT.TLorentzVector()
        topbar.SetPtEtaPhiM(ev.MC_tbar_pt, ev.MC_tbar_eta, ev.MC_tbar_phi, ev.MC_tbar_m)
        w = ROOT.TopNtupleAnalysis.getEWK(top, topbar, ev.initial_type, s)
        return w
