import math
import ROOT
ObservableList = []

class Observable(object):
    def __init__(self, name, binning = (20, -1000, 1000), script = None, style = 'single', do = ['hist'], only = None, title = '{self.name}', dtype = float, default = -1, need_truth = False):
            """Observable for filling histograms or trees
            
            Parameters
            ----------
            name : {str}
                Name of the histogram/branch
            binning : {tuple, array-like}, optional
                If bining is an tuple, it defines equal-width bins in the given range. If bins is an array-like, it defines the bin edges, including the rightmost edge, allowing for non-uniform bin widths.
                (the default is (20, -1000, 1000))
            script : {str}, optional
                [description] (the default is None, which does nothing)
            style : {str}, optional
                This should be either "foreach" or "single". Decide how you fill the hist/branch (the default is 'single')
            do : {list[str]}, optional
                This should be either or both "hist" and "tree"
            only : {list[str]}, optional
                This should be either or both "be", "bmu", "re" or "rmu" (the default is None, which means fill it for all channels)
            title : {str}, optional
                Title of the histogram (the default is '{self.name}')
            """
            self.name = name
            self.binning = binning
            self.title = title.format(self = self)
            self.script = compile(script, '<TopNtupleAnalysis.Observable>', 'eval')
            self.style = style
            self.only = only
            self.do = do
            self.dtype = dtype
            self.default = default
            self.need_truth = need_truth
    def registered(self, analysis):
        return  _Observable(self.name, analysis, binning = self.binning, script = self.script, style = self.style, only = self.only, title = self.title, do = self.do, dtype = self.dtype, default = self.default, need_truth = self.need_truth)
    def queue(self):
        ObservableList.append(self)

class _Observable(object):
    def __init__(self, name, analysis, binning = (20, -1000, 1000), script = None, style = 'single', do = ['hist'], only = None, title = '{self.name}', dtype = None, default = -1, need_truth = False):
        self.name = name
        self.binning = binning
        self.title = title.format(self = self)
        self.script = script
        self.style = style
        self.only = only
        self.analysis = analysis
        self.do = do
        self.dtype = dtype
        self.default = default
        self.need_truth = need_truth
        self._globals = {'analysis': self.analysis}
        self._globals.update(self.analysis.run.im_func.func_globals)
        self._globals.update(globals())
    def __call__(self, _type = None, _locals = None):
        if self.script != None:
            if _locals != None:
                self._globals.update(_locals)
            ret = eval(self.script, self._globals)
            if _type != None:
                return _type(ret)
            else:
                return ret

def P4fromPtEtaPhiM(pt, eta, phi, m):
    p4 = ROOT.TLorentzVector()
    p4.SetPtEtaPhiM(pt, eta, phi, m)
    return p4

### Chi2 ###
# Observable("chi2", do = ['tree'], only = ['re','rmu'],   script = """analysis.TtresChi2.chi2""").queue()
# Observable("chi2_mtl", (150, 0, 300), do = ['tree','hist'], only = ['re','rmu'],   script = """analysis.TtresChi2.mtl""").queue()
# Observable("chi2_mth", (150, 0, 300), do = ['tree','hist'], only = ['re','rmu'],   script = """analysis.TtresChi2.mth""").queue()
# Observable("chi2_mwh", (150, 0, 300), do = ['tree','hist'], only = ['re','rmu'],   script = """analysis.TtresChi2.mwh""").queue()

# Observable("chi2_Th", do = ['tree'], only = ['re','rmu'], dtype = 'TLorentzVector', style = 'foreach', script = """[analysis.TtresChi2.get_tv("Th")]""").queue()
# Observable("chi2_Wh", do = ['tree'], only = ['re','rmu'], dtype = 'TLorentzVector', style = 'foreach', script = """[analysis.TtresChi2.get_tv("Wh")]""").queue()
# Observable("chi2_Tl", do = ['tree'], only = ['re','rmu'], dtype = 'TLorentzVector', style = 'foreach', script = """[analysis.TtresChi2.get_tv("Tl")]""").queue()
# Observable("chi2_Wl", do = ['tree'], only = ['re','rmu'], dtype = 'TLorentzVector', style = 'foreach', script = """[analysis.TtresChi2.get_tv("Wl")]""").queue()
### Track Jets ###
# Observable("trackJetEta", (50, -4, 4), """(tjet.Eta() for tjet in analysis.bot_tagger._tjet_p4)""", style = 'foreach').queue()
# Observable("trackJetPt", (50, 0, 500), """(tjet.Pt()/1000 for tjet in analysis.bot_tagger._tjet_p4)""", style = 'foreach').queue()
# Observable("trackJetPhi", (50, -math.pi, math.pi), """(tjet.Phi() for tjet in analysis.bot_tagger._tjet_p4)""", style = 'foreach').queue()
# Observable("btaggedtrackJetEta", (50, -4, 4), do = ['tree','hist'], script = """(tjet.Eta() for i, tjet in enumerate(analysis.bot_tagger._tjet_p4) if helpers.char2int(analysis.bot_tagger.tjet_isbtagged[i]))""", style = 'foreach').queue()
# Observable("btaggedtrackJetPt", (50, 0, 500), do = ['tree','hist'], script = """(tjet.Pt()*1e-3 for i, tjet in enumerate(analysis.bot_tagger._tjet_p4) if helpers.char2int(analysis.bot_tagger.tjet_isbtagged[i]))""", style = 'foreach').queue()
# Observable("btaggedtrackJetPhi", (50, -math.pi, math.pi), do = ['tree','hist'], script = """(tjet.Phi() for i, tjet in enumerate(analysis.bot_tagger._tjet_p4) if helpers.char2int(analysis.bot_tagger.tjet_isbtagged[i]))""", style = 'foreach').queue()
# Observable("trackJetdeltaPhilep", (50, -math.pi, math.pi), """(tjet.DeltaPhi(l) for tjet in analysis.bot_tagger._tjet_p4)""", style = 'foreach').queue()
# Observable("trackJetdeltaRlep", (50, 0, (math.pi**2+2.5**2)**0.5), """(tjet.DeltaR(l) for tjet in analysis.bot_tagger._tjet_p4)""", style = 'foreach').queue()
# Observable("btaggedtrackJetdeltaPhilep", (50, -math.pi, math.pi), """(tjet.DeltaPhi(l) for i, tjet in enumerate(analysis.bot_tagger._tjet_p4) if helpers.char2int(analysis.bot_tagger.tjet_isbtagged[i]))""", style = 'foreach').queue()
# Observable("btaggedtrackJetdeltaRlep", (50, 0, (math.pi**2+2.5**2)**0.5), """(tjet.DeltaR(l) for i, tjet in enumerate(analysis.bot_tagger._tjet_p4) if helpers.char2int(analysis.bot_tagger.tjet_isbtagged[i]))""", style = 'foreach').queue()
# Observable("dNtruthMatchedBTrackJetdPt", (25, 0, 2500), """(p4.Pt()*1e-3 for (p4, isbtagged, istrueb) in zip(analysis.bot_tagger._tjet_p4, analysis.bot_tagger.tjet_isbtagged, analysis.bot_tagger.tjet_istrueb) if (isbtagged and istrueb))""", style = 'foreach').queue()
# Observable("dNtruedBTrackJetdPt", (25, 0, 2500), """(p4.Pt()*1e-3 for (p4, istrueb) in zip(analysis.bot_tagger._tjet_p4, analysis.bot_tagger.tjet_istrueb) if istrueb)""", style = 'foreach').queue()
# Observable("NtrueB", (6, 0, 6), do = ['tree','hist'], dtype = int, style = 'single', script = """sum(analysis.bot_tagger.tjet_istrueb)""", need_truth = True).queue()
# Observable("NtaggedtrueB", (6, 0, 6), do = ['tree','hist'], dtype = int, style = 'single', script = """sum(isbtagged*istrueb for isbtagged, istrueb in zip(analysis.bot_tagger.tjet_isbtagged,analysis.bot_tagger.tjet_istrueb))""", need_truth = True).queue()

# Observable("NtrueBfromT", (3, 0, 3), do = ['tree','hist'], need_truth = True, style = 'single', dtype = int,
#            script = """any(P4fromPtEtaPhiM(sel.MC_b_from_t_pt, sel.MC_b_from_t_eta, sel.MC_b_from_t_phi, sel.MC_b_from_t_m).DeltaR(tjet_p4)<0.4 for tjet_p4, isbtagged in zip(analysis.bot_tagger._tjet_p4, analysis.bot_tagger.tjet_isbtagged) if helpers.char2int(isbtagged))""" + 
#                    """+any(P4fromPtEtaPhiM(sel.MC_b_from_tbar_pt, sel.MC_b_from_tbar_eta, sel.MC_b_from_tbar_phi, sel.MC_b_from_tbar_m).DeltaR(tjet_p4)<0.4 for tjet_p4, isbtagged in zip(analysis.bot_tagger._tjet_p4, analysis.bot_tagger.tjet_isbtagged) if helpers.char2int(isbtagged))""").queue()
# Observable("dNtruthMatchedBTrackJetdPt_lepside", (25, 0, 2500), """(p4.Pt()*1e-3 for (p4, isbtagged, istrueb) in zip(analysis.bot_tagger._tjet_p4, analysis.bot_tagger.tjet_isbtagged, analysis.bot_tagger.tjet_istrueb) if (isbtagged and istrueb and p4.DeltaR(tlep)<1.0))""", style = 'foreach').queue()
# Observable("dNtruedBTrackJetdPt_lepside", (25, 0, 2500), """(p4.Pt()*1e-3 for (p4, istrueb) in zip(analysis.bot_tagger._tjet_p4, analysis.bot_tagger.tjet_istrueb) if istrueb and p4.DeltaR(tlep)<1.0)""", style = 'foreach').queue()
# Observable("dNtruthMatchedBTrackJetdPt_hadside", (25, 0, 2500), """(p4.Pt()*1e-3 for (p4, isbtagged, istrueb) in zip(analysis.bot_tagger._tjet_p4, analysis.bot_tagger.tjet_isbtagged, analysis.bot_tagger.tjet_istrueb) if (isbtagged and istrueb and p4.DeltaR(lj)<1.0))""", style = 'foreach').queue()
# Observable("dNtruedBTrackJetdPt_hadside", (25, 0, 2500), """(p4.Pt()*1e-3 for (p4, istrueb) in zip(analysis.bot_tagger._tjet_p4, analysis.bot_tagger.tjet_istrueb) if istrueb and p4.DeltaR(lj)<1.0)""", style = 'foreach').queue()
# Observable("NB_lepside", (4, 0, 4), """sel.NB_lepside""").queue()
# Observable("NB_hadside", (4, 0, 4), """sel.NB_hadside""").queue()
# Observable("MC_b_from_t", do = ['tree'], only = ['bFH'], style = 'foreach', dtype = 'TLorentzVector' , need_truth = True,
#            script = """[P4fromPtEtaPhiM(sel.MC_b_from_t_pt, sel.MC_b_from_t_eta, sel.MC_b_from_t_phi, sel.MC_b_from_t_m)]""").queue()
# Observable("MC_b_from_tbar", do = ['tree'], only = ['bFH'], style = 'foreach', dtype = 'TLorentzVector', need_truth = True,
#            script = """[P4fromPtEtaPhiM(sel.MC_b_from_tbar_pt, sel.MC_b_from_tbar_eta, sel.MC_b_from_tbar_phi, sel.MC_b_from_tbar_m)]""").queue()

### Basic Object ###
Observable("met_met", do = ['tree'],   script = """sel.met_met*1e-3""").queue()
Observable("met_phi", do = ['tree'],   script = """sel.met_phi""").queue()
Observable("jet_N", do = ['tree'], style = 'single', dtype = int,  script = """sel.jet_pt.size()""").queue()
Observable("ljet_N", do = ['tree'], style = 'single', dtype = int,  script = """sel.ljet_pt.size()""").queue()
Observable("tjet_N", do = ['tree'], style = 'single', dtype = int,  script = """sel.tjet_pt.size()""").queue()
Observable("btjet_N", do = ['tree'], style = 'single', dtype = int,  script = """sum(helpers.char2int(tjet_isbtagged) for tjet_isbtagged in analysis.bot_tagger.tjet_isbtagged)""").queue()

Observable("th_pt", do = ['tree'], only = ['be', 'bmu'], script = """lj.Perp()*1e-3""").queue()
Observable("th_eta", do = ['tree'], only = ['be', 'bmu'], script = """lj.Eta()""").queue()
Observable("th_phi", do = ['tree'], only = ['be', 'bmu'], script = """lj.Phi()""").queue()
Observable("th_m", do = ['tree'], only = ['be', 'bmu'], script = """lj.M()*1e-3""").queue()

Observable("th_pt_MC", do = ['tree'], only = ['be', 'bmu'], script = """sel.MC_th_pt*1e-3""", need_truth = True).queue()
Observable("th_eta_MC", do = ['tree'], only = ['be', 'bmu'], script = """sel.MC_th_eta""", need_truth = True).queue()
Observable("th_phi_MC", do = ['tree'], only = ['be', 'bmu'], script = """sel.MC_th_phi""", need_truth = True).queue()
Observable("th_m_MC", do = ['tree'], only = ['be', 'bmu'], script = """sel.MC_th_m*1e-3""", need_truth = True).queue()

Observable("th1_pt", do = ['tree'], only = ['bFH'],  script = """lj1.Perp()""").queue()
Observable("th1_eta", do = ['tree'], only = ['bFH'], script = """lj1.Eta()""").queue()
Observable("th1_phi", do = ['tree'], only = ['bFH'], script = """lj1.Phi()""").queue()
Observable("th1_m", do = ['tree'], only = ['bFH'],   script = """lj1.M()""").queue()
Observable("th1_DNN", do = ['tree'], only = ['bFH'],   script = """sel.ljet_DNNTopTag_score[goodJetIdx1] if goodJetIdx1 != -1 else -999""").queue()
Observable("th2_pt", do = ['tree'], only = ['bFH'],  script = """lj2.Perp()""").queue()
Observable("th2_eta", do = ['tree'], only = ['bFH'], script = """lj2.Eta()""").queue()
Observable("th2_phi", do = ['tree'], only = ['bFH'], script = """lj2.Phi()""").queue()
Observable("th2_m", do = ['tree'], only = ['bFH'],   script = """lj2.M()""").queue()
Observable("th2_DNN", do = ['tree'], only = ['bFH'],   script = """sel.ljet_DNNTopTag_score[goodJetIdx2] if goodJetIdx2 != -1 else -999""").queue()

#Observable("akt10truthjet", do = ['tree'], only = ['bFH'], style = 'foreach', dtype = 'TLorentzVector', need_truth = True,
#           script = """[P4fromPtEtaPhiM(sel.akt10truthjet_pt[i], sel.akt10truthjet_eta[i], sel.akt10truthjet_phi[i], sel.akt10truthjet_m[i]) for i in xrange(sel.akt10truthjet_pt.size())]""").queue()


# Observable('trkbjets_N', (4, 0, 5), do = ['hist', 'tree'], dtype = int, script = """sum(map(helpers.char2int, analysis.bot_tagger.tjet_isbtagged))""").queue()

### Jet Substructure ###
Observable("th_tau21_wta", do = ['tree'], only = ['b'], script = """sel.ljet_tau21_wta[analysis.top_tagger.thad_index] if analysis.top_tagger.thad_index != -1 else -999""").queue()
Observable("th_tau32_wta", do = ['tree'], only = ['b'], script = """sel.ljet_tau32_wta[analysis.top_tagger.thad_index] if analysis.top_tagger.thad_index != -1 else -999""").queue()
# Observable("th_C2", (26, 0, 2), do = ['hist','tree'], only = ['b'], script = """sel.ljet_C2[analysis.top_tagger.thad_index] if analysis.top_tagger.thad_index != -1 else -999""").queue()
# Observable("th_D2", (26, 0, 5), do = ['hist','tree'], only = ['b'], script = """sel.ljet_D2[analysis.top_tagger.thad_index] if analysis.top_tagger.thad_index != -1 else -999""").queue()
# Observable("th_MClike", (4, -1, 3), dtype = int, do = ['hist','tree'], only = ['b'], script = """sel.ljet_MClike[analysis.top_tagger.thad_index] if analysis.top_tagger.thad_index != -1 else -1""").queue()

### Pileup ###
Observable("mu", do = ['tree'], style = 'single', script = """sel.mu""").queue()
Observable("npv", do = ['tree'], style = 'single', script = """sel.npv""").queue()
Observable("vtxz", do = ['tree'], style = 'single', script = """sel.vtxz""").queue()
