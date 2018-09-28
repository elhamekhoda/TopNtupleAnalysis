import math
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
    def __call__(self, _type = None, _locals = None):
        if self.script != None:
            if _locals != None:
                self._globals.update(_locals)
            ret = eval(self.script, self._globals)
            if _type != None:
                return _type(ret)
            else:
                return ret

### Track Jets ###
# Observable("trackJetEta", (50, -4, 4), """(tjet.Eta() for tjet in analysis.bot_tagger._tjet_p4)""", style = 'foreach').queue()
# Observable("trackJetPt", (50, 0, 500), """(tjet.Pt()/1000 for tjet in analysis.bot_tagger._tjet_p4)""", style = 'foreach').queue()
# Observable("trackJetPhi", (50, -math.pi, math.pi), """(tjet.Phi() for tjet in analysis.bot_tagger._tjet_p4)""", style = 'foreach').queue()
# Observable("btaggedtrackJetEta", (50, -4, 4), """(tjet.Eta() for i, tjet in enumerate(analysis.bot_tagger._tjet_p4) if helpers.char2int(analysis.bot_tagger.tjet_isbtagged[i]))""", style = 'foreach').queue()
# Observable("btaggedtrackJetPt", (50, 0, 500), """(tjet.Pt()/1000 for i, tjet in enumerate(analysis.bot_tagger._tjet_p4) if helpers.char2int(analysis.bot_tagger.tjet_isbtagged[i]))""", style = 'foreach').queue()
# Observable("btaggedtrackJetPhi", (50, -math.pi, math.pi), """(tjet.Phi() for i, tjet in enumerate(analysis.bot_tagger._tjet_p4) if helpers.char2int(analysis.bot_tagger.tjet_isbtagged[i]))""", style = 'foreach').queue()
# Observable("trackJetdeltaPhilep", (50, -math.pi, math.pi), """(tjet.DeltaPhi(l) for tjet in analysis.bot_tagger._tjet_p4)""", style = 'foreach').queue()
# Observable("trackJetdeltaRlep", (50, 0, (math.pi**2+2.5**2)**0.5), """(tjet.DeltaR(l) for tjet in analysis.bot_tagger._tjet_p4)""", style = 'foreach').queue()
# Observable("btaggedtrackJetdeltaPhilep", (50, -math.pi, math.pi), """(tjet.DeltaPhi(l) for i, tjet in enumerate(analysis.bot_tagger._tjet_p4) if helpers.char2int(analysis.bot_tagger.tjet_isbtagged[i]))""", style = 'foreach').queue()
# Observable("btaggedtrackJetdeltaRlep", (50, 0, (math.pi**2+2.5**2)**0.5), """(tjet.DeltaR(l) for i, tjet in enumerate(analysis.bot_tagger._tjet_p4) if helpers.char2int(analysis.bot_tagger.tjet_isbtagged[i]))""", style = 'foreach').queue()
# Observable("dNtruthMatchedBTrackJetdPt", (25, 0, 2500), """(p4.Pt()*1e-3 for (p4, isbtagged, istrueb) in zip(analysis.bot_tagger._tjet_p4, analysis.bot_tagger.tjet_isbtagged, analysis.bot_tagger.tjet_istrueb) if (isbtagged and istrueb))""", style = 'foreach').queue()
# Observable("dNtruedBTrackJetdPt", (25, 0, 2500), """(p4.Pt()*1e-3 for (p4, istrueb) in zip(analysis.bot_tagger._tjet_p4, analysis.bot_tagger.tjet_istrueb) if istrueb)""", style = 'foreach').queue()
# Observable("NtrueB", (4, 0, 4), """sum(analysis.bot_tagger.tjet_istrueb)""").queue()
# Observable("dNtruthMatchedBTrackJetdPt_lepside", (25, 0, 2500), """(p4.Pt()*1e-3 for (p4, isbtagged, istrueb) in zip(analysis.bot_tagger._tjet_p4, analysis.bot_tagger.tjet_isbtagged, analysis.bot_tagger.tjet_istrueb) if (isbtagged and istrueb and p4.DeltaR(tlep)<1.0))""", style = 'foreach').queue()
# Observable("dNtruedBTrackJetdPt_lepside", (25, 0, 2500), """(p4.Pt()*1e-3 for (p4, istrueb) in zip(analysis.bot_tagger._tjet_p4, analysis.bot_tagger.tjet_istrueb) if istrueb and p4.DeltaR(tlep)<1.0)""", style = 'foreach').queue()
# Observable("dNtruthMatchedBTrackJetdPt_hadside", (25, 0, 2500), """(p4.Pt()*1e-3 for (p4, isbtagged, istrueb) in zip(analysis.bot_tagger._tjet_p4, analysis.bot_tagger.tjet_isbtagged, analysis.bot_tagger.tjet_istrueb) if (isbtagged and istrueb and p4.DeltaR(lj)<1.0))""", style = 'foreach').queue()
# Observable("dNtruedBTrackJetdPt_hadside", (25, 0, 2500), """(p4.Pt()*1e-3 for (p4, istrueb) in zip(analysis.bot_tagger._tjet_p4, analysis.bot_tagger.tjet_istrueb) if istrueb and p4.DeltaR(lj)<1.0)""", style = 'foreach').queue()
# Observable("NB_lepside", (4, 0, 4), """sel.NB_lepside""").queue()
# Observable("NB_hadside", (4, 0, 4), """sel.NB_hadside""").queue()

### Basic Object ###
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
Observable("th2_pt", do = ['tree'], only = ['bFH'],  script = """lj2.Perp()""").queue()
Observable("th2_eta", do = ['tree'], only = ['bFH'], script = """lj2.Eta()""").queue()
Observable("th2_phi", do = ['tree'], only = ['bFH'], script = """lj2.Phi()""").queue()
Observable("th2_m", do = ['tree'], only = ['bFH'],   script = """lj2.M()""").queue()

Observable('trkbjets_N', (4, 0, 5), do = ['hist', 'tree'], dtype = int, script = """sum(map(helpers.char2int, analysis.bot_tagger.tjet_isbtagged))""").queue()

### Jet Substructure ###
# Observable("th_tau21_wta", do = ['tree'], only = ['b'], script = """sel.ljet_tau21_wta[analysis.top_tagger.thad_index] if analysis.top_tagger.thad_index != -1 else -999""").queue()
# Observable("th_tau32_wta", do = ['tree'], only = ['b'], script = """sel.ljet_tau32_wta[analysis.top_tagger.thad_index] if analysis.top_tagger.thad_index != -1 else -999""").queue()
# Observable("th_C2", (26, 0, 2), do = ['hist','tree'], only = ['b'], script = """sel.ljet_C2[analysis.top_tagger.thad_index] if analysis.top_tagger.thad_index != -1 else -999""").queue()
# Observable("th_D2", (26, 0, 5), do = ['hist','tree'], only = ['b'], script = """sel.ljet_D2[analysis.top_tagger.thad_index] if analysis.top_tagger.thad_index != -1 else -999""").queue()
# Observable("th_MClike", (4, -1, 3), dtype = int, do = ['hist','tree'], only = ['b'], script = """sel.ljet_MClike[analysis.top_tagger.thad_index] if analysis.top_tagger.thad_index != -1 else -1""").queue()
