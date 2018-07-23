import math
ObservableList = []
class Observable(object):
    def __init__(self, name, binning = (20, -1000, 1000), script = None, style = 'single', do = ['hist'], only = None, title = '{self.name}'):
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
        self.script = script
        self.style = style
        self.only = only
    def __call__(self, analysis, _type = None, _locals = None):
        if self.script != None:
            _globals = {'analysis': analysis}
            _globals.update(analysis.run.im_func.func_globals)
            if _locals != None:
                _globals.update(_locals)
            ret = eval(self.script, _globals)
            if _type != None:
                return _type(ret)
            else:
                return ret
    def register(self):
        ObservableList.append(self)

Observable("trackJetEta", (50, -4, 4), """(tjet.Eta() for tjet in analysis.bot_tagger._tjet_p4)""", style = 'foreach').register()
Observable("trackJetPt", (50, 0, 500), """(tjet.Pt()/1000 for tjet in analysis.bot_tagger._tjet_p4)""", style = 'foreach').register()
Observable("trackJetPhi", (50, -math.pi, math.pi), """(tjet.Phi() for tjet in analysis.bot_tagger._tjet_p4)""", style = 'foreach').register()
Observable("btaggedtrackJetEta", (50, -4, 4), """(tjet.Eta() for i, tjet in enumerate(analysis.bot_tagger._tjet_p4) if helpers.char2int(analysis.bot_tagger.tjet_isbtagged[i]))""", style = 'foreach').register()
Observable("btaggedtrackJetPt", (50, 0, 500), """(tjet.Pt()/1000 for i, tjet in enumerate(analysis.bot_tagger._tjet_p4) if helpers.char2int(analysis.bot_tagger.tjet_isbtagged[i]))""", style = 'foreach').register()
Observable("btaggedtrackJetPhi", (50, -math.pi, math.pi), """(tjet.Phi() for i, tjet in enumerate(analysis.bot_tagger._tjet_p4) if helpers.char2int(analysis.bot_tagger.tjet_isbtagged[i]))""", style = 'foreach').register()


Observable("trackJetdeltaPhilep", (50, -math.pi, math.pi), """(tjet.DeltaPhi(l) for tjet in analysis.bot_tagger._tjet_p4)""", style = 'foreach').register()
Observable("trackJetdeltaRlep", (50, 0, (math.pi**2+2.5**2)**0.5), """(tjet.DeltaR(l) for tjet in analysis.bot_tagger._tjet_p4)""", style = 'foreach').register()
Observable("btaggedtrackJetdeltaPhilep", (50, -math.pi, math.pi), """(tjet.DeltaPhi(l) for i, tjet in enumerate(analysis.bot_tagger._tjet_p4) if helpers.char2int(analysis.bot_tagger.tjet_isbtagged[i]))""", style = 'foreach').register()
Observable("btaggedtrackJetdeltaRlep", (50, 0, (math.pi**2+2.5**2)**0.5), """(tjet.DeltaR(l) for i, tjet in enumerate(analysis.bot_tagger._tjet_p4) if helpers.char2int(analysis.bot_tagger.tjet_isbtagged[i]))""", style = 'foreach').register()

Observable("NB_lepside", (4, 0, 4), """sel.NB_lepside""").register()
Observable("NB_hadside", (4, 0, 4), """sel.NB_hadside""").register()