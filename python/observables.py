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
# Observable("trackJetPt", (50, 0, 500), """(tjet.Pt()*1e-3 for tjet in analysis.bot_tagger._tjet_p4)""", style = 'foreach', do = ['tree', 'hist']).queue()
# Observable("trackJetIsBtagged", dtype = int, do = ['tree'], script = '''analysis.bot_tagger.tjet_isbtagged''', style = 'foreach').queue()
# Observable("trackJetTrueFlav", dtype = int, do = ['tree'], script = '''sel.tjet_label''', style = 'foreach').queue()
# Observable("trackJetPhi", (50, -math.pi, math.pi), """(tjet.Phi() for tjet in analysis.bot_tagger._tjet_p4)""", style = 'foreach').queue()
# Observable("btaggedtrackJetEta", (50, -4, 4), do = ['tree','hist'], script = """(tjet.Eta() for i, tjet in enumerate(analysis.bot_tagger._tjet_p4) if helpers.char2int(analysis.bot_tagger.tjet_isbtagged[i]))""", style = 'foreach').queue()
# Observable("btaggedtrackJetPt", (50, 0, 500), do = ['tree','hist'], script = """(tjet.Pt()*1e-3 for i, tjet in enumerate(analysis.bot_tagger._tjet_p4) if helpers.char2int(analysis.bot_tagger.tjet_isbtagged[i]))""", style = 'foreach').queue()
# Observable("btaggedtrackJetPhi", (50, -math.pi, math.pi), do = ['tree','hist'], script = """(tjet.Phi() for i, tjet in enumerate(analysis.bot_tagger._tjet_p4) if helpers.char2int(analysis.bot_tagger.tjet_isbtagged[i]))""", style = 'foreach').queue()
# Observable("trackJetdeltaPhilep", (50, -math.pi, math.pi), """(ROOT.Math.VectorUtil.DeltaPhi(tjet, l) for tjet in analysis.bot_tagger._tjet_p4)""", style = 'foreach').queue()
# Observable("trackJetdeltaRlep", (50, 0, (math.pi**2+2.5**2)**0.5), """(ROOT.Math.VectorUtil.DeltaR(tjet, l) for tjet in analysis.bot_tagger._tjet_p4)""", style = 'foreach').queue()
# Observable("btaggedtrackJetdeltaPhilep", (50, -math.pi, math.pi), """(ROOT.Math.VectorUtil.DeltaPhi(tjet, l) for i, tjet in enumerate(analysis.bot_tagger._tjet_p4) if helpers.char2int(analysis.bot_tagger.tjet_isbtagged[i]))""", style = 'foreach').queue()
# Observable("btaggedtrackJetdeltaRlep", (50, 0, (math.pi**2+2.5**2)**0.5), """(ROOT.Math.VectorUtil.DeltaR(tjet, l) for i, tjet in enumerate(analysis.bot_tagger._tjet_p4) if helpers.char2int(analysis.bot_tagger.tjet_isbtagged[i]))""", style = 'foreach').queue()
#Observable("dNtruthMatchedBTrackJetdPt", (30, 0, 3000), do = ['hist', 'tree'], script = """(p4.Pt()*1e-3 for (p4, isbtagged, istrueb) in zip(analysis.bot_tagger._tjet_p4, analysis.bot_tagger.tjet_isbtagged, analysis.bot_tagger.tjet_istrueb) if (isbtagged and istrueb))""", style = 'foreach', need_truth = True).queue()
#Observable("dNtruedBTrackJetdPt", (30, 0, 3000), do = ['hist', 'tree'], script = """(p4.Pt()*1e-3 for (p4, istrueb) in zip(analysis.bot_tagger._tjet_p4, analysis.bot_tagger.tjet_istrueb) if istrueb)""", style = 'foreach', need_truth = True).queue()
# Observable("NtrueB", (6, 0, 6), do = ['tree','hist'], dtype = int, style = 'single', script = """sum(analysis.bot_tagger.tjet_istrueb)""", need_truth = True).queue()
# Observable("NtaggedtrueB", (6, 0, 6), do = ['tree','hist'], dtype = int, style = 'single', script = """sum(isbtagged*istrueb for isbtagged, istrueb in zip(analysis.bot_tagger.tjet_isbtagged,analysis.bot_tagger.tjet_istrueb))""", need_truth = True).queue()

# Observable("NtrueBfromT", (3, 0, 3), do = ['tree','hist'], need_truth = True, style = 'single', dtype = int,
#            script = """any(ROOT.Math.VectorUtil.DeltaR(ROOT.Math.PtEtaPhiMVector(sel.MC_b_from_t_pt, sel.MC_b_from_t_eta, sel.MC_b_from_t_phi, sel.MC_b_from_t_m), tjet_p4)<0.4 for tjet_p4, isbtagged in zip(analysis.bot_tagger._tjet_p4, analysis.bot_tagger.tjet_isbtagged) if helpers.char2int(isbtagged))""" + 
#                    """+any(ROOT.Math.VectorUtil.DeltaR(ROOT.Math.PtEtaPhiMVector(sel.MC_b_from_tbar_pt, sel.MC_b_from_tbar_eta, sel.MC_b_from_tbar_phi, sel.MC_b_from_tbar_m), tjet_p4)<0.4 for tjet_p4, isbtagged in zip(analysis.bot_tagger._tjet_p4, analysis.bot_tagger.tjet_isbtagged) if helpers.char2int(isbtagged))""").queue()
# Observable("dNtruthMatchedBTrackJetdPt_lepside", (25, 0, 2500), """(p4.Pt()*1e-3 for (p4, isbtagged, istrueb) in zip(analysis.bot_tagger._tjet_p4, analysis.bot_tagger.tjet_isbtagged, analysis.bot_tagger.tjet_istrueb) if (isbtagged and istrueb and ROOT.Math.VectorUtil.DeltaR(p4, tlep)<1.0))""", style = 'foreach').queue()
# Observable("dNtruedBTrackJetdPt_lepside", (25, 0, 2500), """(p4.Pt()*1e-3 for (p4, istrueb) in zip(analysis.bot_tagger._tjet_p4, analysis.bot_tagger.tjet_istrueb) if istrueb and ROOT.Math.VectorUtil.DeltaR(p4, tlep)<1.0)""", style = 'foreach').queue()
# Observable("dNtruthMatchedBTrackJetdPt_hadside", (25, 0, 2500), """(p4.Pt()*1e-3 for (p4, isbtagged, istrueb) in zip(analysis.bot_tagger._tjet_p4, analysis.bot_tagger.tjet_isbtagged, analysis.bot_tagger.tjet_istrueb) if (isbtagged and istrueb and ROOT.Math.VectorUtil.DeltaR(p4, lj)<1.0))""", style = 'foreach').queue()
# Observable("dNtruedBTrackJetdPt_hadside", (25, 0, 2500), """(p4.Pt()*1e-3 for (p4, istrueb) in zip(analysis.bot_tagger._tjet_p4, analysis.bot_tagger.tjet_istrueb) if istrueb and ROOT.Math.VectorUtil.DeltaR(p4, lj)<1.0)""", style = 'foreach').queue()
# Observable("NB_lepside", (4, 0, 4), """sel.NB_lepside""").queue()
# Observable("NB_hadside", (4, 0, 4), """sel.NB_hadside""").queue()
# Observable("MC_b_from_t", do = ['tree'], only = ['bFH'], style = 'foreach', dtype = 'ROOT::Math::PtEtaPhiMVector', need_truth = True,
#            script = """[(sel.MC_b_from_t_pt, sel.MC_b_from_t_eta, sel.MC_b_from_t_phi, sel.MC_b_from_t_m)]""").queue()
# Observable("MC_b_from_tbar", do = ['tree'], only = ['bFH'], style = 'foreach', dtype = 'ROOT::Math::PtEtaPhiMVector', need_truth = True,
#            script = """[(sel.MC_b_from_tbar_pt, sel.MC_b_from_tbar_eta, sel.MC_b_from_tbar_phi, sel.MC_b_from_tbar_m)]""").queue()


# Observable("jet_pt", do = ['tree'], style = 'foreach', script = """(pt*1e-3 for pt in sel.jet_pt)""").queue()
# Observable("jet_eta", do = ['tree'], style = 'foreach', script = """(eta for eta in sel.jet_eta)""").queue()
# Observable("jet_phi", do = ['tree'], style = 'foreach', script = """(phi for phi in sel.jet_phi)""").queue()
# Observable("jet_e", do = ['tree'], style = 'foreach', script = """(e*1e-3 for e in sel.jet_e)""").queue()
# Observable("jet_DL1", do = ['tree'], style = 'foreach', script = """(e*1e-3 for e in sel.jet_DL1)""").queue()
# Observable("jet_DL1_pu", do = ['tree'], style = 'foreach', script = """(x for x in sel.jet_DL1_pu)""").queue()
# Observable("jet_DL1_pc", do = ['tree'], style = 'foreach', script = """(x for x in sel.jet_DL1_pc)""").queue()
# Observable("jet_DL1_pb", do = ['tree'], style = 'foreach', script = """(x for x in sel.jet_DL1_pb)""").queue()
# Observable("jet_mv2c10", do = ['tree'], style = 'foreach', script = """(x for x in sel.jet_mv2c10)""").queue()
# Observable("jet_DL1r", do = ['tree'], style = 'foreach', script = """(x for x in sel.jet_DL1r)""").queue()
# Observable("jet_DL1r_pu", do = ['tree'], style = 'foreach', script = """(x for x in sel.jet_DL1r_pu)""").queue()
# Observable("jet_DL1r_pc", do = ['tree'], style = 'foreach', script = """(x for x in sel.jet_DL1r_pc)""").queue()
# Observable("jet_DL1r_pb", do = ['tree'], style = 'foreach', script = """(x for x in sel.jet_DL1r_pb)""").queue()
# Observable("jet_DL1rmu", do = ['tree'], style = 'foreach', script = """(x for x in sel.jet_DL1rmu)""").queue()
# Observable("jet_DL1rmu_pu", do = ['tree'], style = 'foreach', script = """(x for x in sel.jet_DL1rmu_pu)""").queue()
# Observable("jet_DL1rmu_pc", do = ['tree'], style = 'foreach', script = """(x for x in sel.jet_DL1rmu_pc)""").queue()
# Observable("jet_DL1rmu_pb", do = ['tree'], style = 'foreach', script = """(x for x in sel.jet_DL1rmu_pb)""").queue()
# Observable("jet_NumTrkPt500", do = ['tree'], style = 'foreach', script = """(Ntrk for Ntrk in sel.jet_NumTrkPt500)""").queue()

#Observable("jet_isbtag_DL185", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.jet_isbtagged_DL1_85)""").queue()
# Observable("jet_isbtag_DL177", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.jet_isbtagged_DL1_77)""").queue()
#Observable("jet_isbtag_DL170", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.jet_isbtagged_DL1_70)""").queue()
#Observable("jet_isbtag_DL160", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.jet_isbtagged_DL1_60)""").queue()
#Observable("jet_isbtag_DL1r85", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.jet_isbtagged_DL1r_85)""").queue()
# Observable("jet_isbtag_DL1r77", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.jet_isbtagged_DL1r_77)""").queue()
#Observable("jet_isbtag_DL1r70", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.jet_isbtagged_DL1r_70)""").queue()
#Observable("jet_isbtag_DL1r60", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.jet_isbtagged_DL1r_60)""").queue()

# all large jets
# Observable("ljet_pt", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(pt*1e-3 for pt in sel.ljet_pt)""").queue()
# Observable("ljet_eta", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(eta for eta in sel.ljet_eta)""").queue()
# Observable("ljet_phi", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(phi for phi in sel.ljet_phi)""").queue()
# Observable("ljet_m", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(m*1e-3 for m in sel.ljet_m)""").queue()

# Observable("ljet_istoptag_dnn_contained80", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(x for x in sel.ljet_isTagged_JSSWTopTaggerDNN_DNNTaggerTopQuarkContained80)""").queue()
# Observable("ljet_istoptag_dnn_inclusive80", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(x for x in sel.ljet_isTagged_JSSWTopTaggerDNN_DNNTaggerTopQuarkInclusive80)""").queue()

### Basic Object ###
# MET and jet  variables
# Observable("met_met", do = ['tree'],   script = """sel.met_met*1e-3""").queue()
# Observable("met_phi", do = ['tree'],   script = """sel.met_phi""").queue()
# Observable("mwt", do = ['tree'],   script = """math.sqrt(2*l.Pt()*sel.met_met*(1 - math.cos(l.Phi() - sel.met_phi)))*1e-3""").queue()
# Observable("jet_N", do = ['tree'], style = 'single', dtype = int,  script = """sel.jet_pt.size()""").queue()
# Observable("ljet_N", do = ['tree'], style = 'single', dtype = int,  script = """sel.ljet_pt.size()""").queue()
# Observable("tjet_N", do = ['tree'], style = 'single', dtype = int,  script = """sel.tjet_pt.size()""").queue()
# Observable("btjet_N", do = ['tree'], style = 'single', dtype = int,  script = """sum(helpers.char2int(tjet_isbtagged) for tjet_isbtagged in analysis.bot_tagger.tjet_isbtagged)""").queue()
Observable("bjet_N", do = ['tree'], style = 'single', dtype = int,  script = """sum(helpers.char2int(calojet_isbtagged) for calojet_isbtagged in analysis.bot_tagger.calojet_isbtagged)""").queue()

# Observable("ljet_pt", do = ['tree'], only = ['re', 'rmu', 'be', 'bmu'], script = """lj.Pt()*1e-3""").queue()
# Observable("ljet_eta", do = ['tree'], only = ['re', 'rmu', 'be', 'bmu'], script = """lj.Eta()""").queue()
# Observable("ljet_phi", do = ['tree'], only = ['re', 'rmu', 'be', 'bmu'], script = """lj.Phi()""").queue()
# Observable("ljet_m", do = ['tree'], only = ['re', 'rmu', 'be', 'bmu'], script = """lj.M()*1e-3""").queue()
# #large-R jet substructure variables
# Observable("ljet_tau21_wta", do = ['tree'], only = ['be', 'bmu'], script = """sel.ljet_tau21_wta[goodJetIdx] if goodJetIdx != -1 else -999""").queue()
# Observable("ljet_tau32_wta", do = ['tree'], only = ['be', 'bmu'], script = """sel.ljet_tau32_wta[goodJetIdx] if goodJetIdx != -1 else -999""").queue()
# Observable("ljet_tau21_wta", do = ['tree'], only = ['re', 'rmu'], script = """sel.ljet_tau21_wta[0] if len(sel.ljet_tau21_wta) != 0 else -999""").queue()
# Observable("ljet_tau32_wta", do = ['tree'], only = ['re', 'rmu'], script = """sel.ljet_tau32_wta[0] if len(sel.ljet_tau32_wta) != 0 else -999""").queue()

# Observable("closestJetDr", do = ['tree'], only = ['re', 'rmu', 'be', 'bmu'], script = """closestJetDr""").queue()
# Observable("closestJetPt", do = ['tree'], only = ['re', 'rmu', 'be', 'bmu'], script = """closestJetPt*1e-3""").queue()

# # Lepton variables
# Observable("lep_pt", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """l.Pt()*1e-3""").queue()
# Observable("lep_eta", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """l.Eta()""").queue()
# Observable("lep_phi", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """l.Phi()""").queue()
# Observable("lep_m", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """l.M()*1e-3""").queue()
# Observable("lep_true_type", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """l_true_type""").queue()
# Observable("lep_true_origin", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """l_true_origin""").queue()

# # Reconstructed top-quarks
# Observable("mtlep_boo", do = ['tree'], only = ['be', 'bmu'], script = """tlep.M()*1e-3""").queue()
# Observable("mtlep_res", do = ['tree'], only = ['re', 'rmu'], script = """analysis.TtresChi2.mtl""").queue()
# Observable("mthad_res", do = ['tree'], only = ['re', 'rmu'], script = """analysis.TtresChi2.mth""").queue()
# Observable("mwhad_res", do = ['tree'], only = ['re', 'rmu'], script = """analysis.TtresChi2.mwh""").queue()
# Observable("chi2", do = ['tree'], only = ['re','rmu'],   script = """analysis.TtresChi2.chi2""").queue()

#Observable("MA_thFJ_pt", do = ['tree'], only = ['be', 'bmu'], script = """sel.MA_thFJ_pt""").queue()
#Observable("MA_thFJ_eta", do = ['tree'], only = ['be', 'bmu'], script = """sel.MA_thFJ_eta""").queue()
#Observable("MA_thFJ_phi", do = ['tree'], only = ['be', 'bmu'], script = """sel.MA_thFJ_phi""").queue()
#Observable("MA_thFJ_m", do = ['tree'], only = ['be', 'bmu'], script = """sel.MA_thFJ_m""").queue()

#Observable("th_pt_MC", do = ['tree'], only = ['be', 'bmu'], script = """sel.MC_th_pt*1e-3""", need_truth = True).queue()
#Observable("th_eta_MC", do = ['tree'], only = ['be', 'bmu'], script = """sel.MC_th_eta""", need_truth = True).queue()
#Observable("th_phi_MC", do = ['tree'], only = ['be', 'bmu'], script = """sel.MC_th_phi""", need_truth = True).queue()
#Observable("th_m_MC", do = ['tree'], only = ['be', 'bmu'], script = """sel.MC_th_m*1e-3""", need_truth = True).queue()

#MC variables
'''
Observable("MC_th_pt", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """sel.MC_th_pt*1e-3""", need_truth = True).queue()
Observable("MC_th_eta", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """sel.MC_th_eta""", need_truth = True).queue()
Observable("MC_th_phi", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """sel.MC_th_phi""", need_truth = True).queue()
Observable("MC_th_m", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """sel.MC_th_m*1e-3""", need_truth = True).queue()

Observable("MC_tl_pt", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """sel.MC_tl_pt*1e-3""", need_truth = True).queue()
Observable("MC_tl_eta", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """sel.MC_tl_eta""", need_truth = True).queue()
Observable("MC_tl_phi", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """sel.MC_tl_phi""", need_truth = True).queue()
Observable("MC_tl_m", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """sel.MC_tl_m*1e-3""", need_truth = True).queue()

Observable("MC_wh_pt", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """sel.MC_wh_pt*1e-3""", need_truth = True).queue()
Observable("MC_wh_eta", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """sel.MC_wh_eta""", need_truth = True).queue()
Observable("MC_wh_phi", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """sel.MC_wh_phi""", need_truth = True).queue()
Observable("MC_wh_m", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """sel.MC_wh_m*1e-3""", need_truth = True).queue()

Observable("MC_wl_pt", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """sel.MC_wl_pt*1e-3""", need_truth = True).queue()
Observable("MC_wl_eta", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """sel.MC_wl_eta""", need_truth = True).queue()
Observable("MC_wl_phi", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """sel.MC_wl_phi""", need_truth = True).queue()
Observable("MC_wl_m", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """sel.MC_wl_m*1e-3""", need_truth = True).queue()

Observable("MC_bh_pt", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """sel.MC_bh_pt*1e-3""", need_truth = True).queue()
Observable("MC_bh_eta", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """sel.MC_bh_eta""", need_truth = True).queue()
Observable("MC_bh_phi", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """sel.MC_bh_phi""", need_truth = True).queue()
Observable("MC_bh_m", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """sel.MC_th_m*1e-3""", need_truth = True).queue()

Observable("MC_bl_pt", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """sel.MC_bl_pt*1e-3""", need_truth = True).queue()
Observable("MC_bl_eta", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """sel.MC_bl_eta""", need_truth = True).queue()
Observable("MC_bl_phi", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """sel.MC_bl_phi""", need_truth = True).queue()
Observable("MC_bl_m", do = ['tree'], only = ['be', 'bmu', 're', 'rmu'], script = """sel.MC_bl_m*1e-3""", need_truth = True).queue()
'''
Observable("th1_pt", do = ['tree'], only = ['bFH'],  script = """lj1.Pt()""").queue()
Observable("th1_eta", do = ['tree'], only = ['bFH'], script = """lj1.Eta()""").queue()
Observable("th1_phi", do = ['tree'], only = ['bFH'], script = """lj1.Phi()""").queue()
Observable("th1_m", do = ['tree'], only = ['bFH'],   script = """lj1.M()""").queue()
Observable("th1_DNN", do = ['tree'], only = ['bFH'], script = """sel.ljet_DNNContainedTopTag_score[goodJetIdx1] if goodJetIdx1 != -1 else -999""").queue()
Observable("th1_SF", do = ['tree'], only = ['bFH'], script = """analysis.top_tagger.ljet_toptagSF[goodJetIdx1]""", need_truth = True).queue()
Observable("th1_isleading", do = ['tree'], only = ['bFH'], dtype = int,  script = """goodJetIdx1==0""").queue()
Observable("th2_pt", do = ['tree'], only = ['bFH'],  script = """lj2.Pt()""").queue()
Observable("th2_eta", do = ['tree'], only = ['bFH'], script = """lj2.Eta()""").queue()
Observable("th2_phi", do = ['tree'], only = ['bFH'], script = """lj2.Phi()""").queue()
Observable("th2_m", do = ['tree'], only = ['bFH'],   script = """lj2.M()""").queue()
Observable("th2_DNN", do = ['tree'], only = ['bFH'],   script = """sel.ljet_DNNContainedTopTag_score[goodJetIdx2] if goodJetIdx2 != -1 else -999""").queue()
Observable("th2_SF", do = ['tree'], only = ['bFH'], script = """analysis.top_tagger.ljet_toptagSF[goodJetIdx2]""", need_truth = True).queue()
Observable("th2_issubleading", do = ['tree'], only = ['bFH'], dtype = int,  script = """goodJetIdx2==1""").queue()

Observable("toptagged_N", (4, 0, 4), do = ['hist', 'tree'], only = ['bFH'], style = 'single', dtype = int,  script = """sum(analysis.top_tagger.ljet_istoptagged)""").queue()

# Observable("truth_ljet_pt_MA",  do = ['tree'], style = 'foreach', dtype = float, script = """(analysis.top_tagger.truth_ljet_p4[i].Pt()*1e-3 for i in analysis.top_tagger.ljet_truthjetid if i >= 0)""", need_truth = True).queue()
# Observable("truth_ljet_eta_MA", do = ['tree'], style = 'foreach', dtype = float, script = """(analysis.top_tagger.truth_ljet_p4[i].Eta() for i in analysis.top_tagger.ljet_truthjetid if i >= 0)""",     need_truth = True).queue()
# Observable("truth_ljet_phi_MA", do = ['tree'], style = 'foreach', dtype = float, script = """(analysis.top_tagger.truth_ljet_p4[i].Phi() for i in analysis.top_tagger.ljet_truthjetid if i >= 0)""",     need_truth = True).queue()
# Observable("truth_ljet_m_MA"  , do = ['tree'], style = 'foreach', dtype = float, script = """(analysis.top_tagger.truth_ljet_p4[i].M()*1e-3 for i in analysis.top_tagger.ljet_truthjetid if i >= 0)""",  need_truth = True).queue()
#Observable("truth", do = ['tree'], need_truth = True, style = 'foreach', dtype = 'ROOT::Math::PtEtaPhiMVector', script = """[ROOT.Math.PtEtaPhiMVector(sel.truthparticle_pt.at(i), sel.truthparticle_eta.at(i), sel.truthparticle_phi.at(i), sel.truthparticle_m.at(i))*1e-3 for i in xrange(sel.truthparticle_pt.size())]""").queue()
#Observable("truth_id", do = ['tree'], need_truth = True, style = 'foreach', dtype = int, script = """sel.truthparticle_type""").queue()
#Observable("akt10truthjet", do = ['tree'], only = ['bFH'], style = 'foreach', dtype = 'TLorentzVector', need_truth = True,
#           script = """[P4fromPtEtaPhiM(sel.akt10truthjet_pt[i], sel.akt10truthjet_eta[i], sel.akt10truthjet_phi[i], sel.akt10truthjet_m[i]) for i in xrange(sel.akt10truthjet_pt.size())]""").queue()


# Observable('trkbjets_N', (4, 0, 5), do = ['hist', 'tree'], dtype = int, script = """sum(map(helpers.char2int, analysis.bot_tagger.tjet_isbtagged))""").queue()


Observable("btag_SF", do = ['tree'], need_truth = True, only = ['truebFH', 'bFH'],  script = """sel.weight_trackjet_bTagSF_DL1_77""").queue()
#Observable("btag_SF_beff", do = ['tree'], style = 'foreach', need_truth = True, only = [ 'bFH'],  script = """(x for x in sel.weight_trackjet_bTagSF_DL1_77_eigenvars_B_up)""").queue()
#Observable("btag_SF_b_extrap", do = ['tree'], need_truth = True, only = ['bFH'],  script = """sel.weight_trackjet_bTagSF_DL1_77_extrapolation_up""").queue()
#Observable("btag_SF_c_extrap", do = ['tree'], need_truth = True, only = ['bFH'],  script = """sel.weight_trackjet_bTagSF_DL1_77_extrapolation_from_charm_up""").queue()
#Observable("btag_SF_beff", do = ['tree'], style = 'foreach', need_truth = True, only = [ 'bFH'],  script = """sel.weight_trackjet_bTagSF_DL1_77_eigenvars_B_up""").queue()

## track jet ####
# Observable("tjet_pt",  do = ['tree'], style = 'foreach', script = """(tjet.Pt()*1e-3 for tjet in analysis.bot_tagger._tjet_p4)""").queue()
# Observable("tjet_eta", do = ['tree'], style = 'foreach', script = """(tjet.Eta() for tjet in analysis.bot_tagger._tjet_p4)""").queue()
# Observable("tjet_phi", do = ['tree'], style = 'foreach', script = """(tjet.Phi() for tjet in analysis.bot_tagger._tjet_p4)""").queue()
# Observable("tjet_e",   do = ['tree'], style = 'foreach', script = """(tjet.E()*1e-3 for tjet in analysis.bot_tagger._tjet_p4)""").queue()
#Observable("tjet_isbtag_DL185", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.tjet_isbtagged_DL1_85)""").queue()
# Observable("tjet_isbtag_DL177", do = ['tree'], style = 'foreach', script = """(ord(x) for x in sel.tjet_isbtagged_DL1_77)""").queue()
# Observable("tjet_isbtag_DL170", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.tjet_isbtagged_DL1_70)""").queue()
#Observable("tjet_isbtag_DL160", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.tjet_isbtagged_DL1_60)""").queue()
#Observable("tjet_isbtag_DL1r85", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.tjet_isbtagged_DL1r_85)""").queue()
# Observable("tjet_isbtag_DL1r77", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.tjet_isbtagged_DL1r_77)""").queue()
#Observable("tjet_isbtag_DL1r70", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.tjet_isbtagged_DL1r_70)""").queue()
#Observable("tjet_isbtag_DL1r60", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.tjet_isbtagged_DL1r_60)""").queue()
#DL1rmu MV2 
#Observable("tjet_isbtag_DL1rmu85", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.tjet_isbtagged_DL1rmu_85)""").queue()
#Observable("tjet_isbtag_DL1rmu77", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.tjet_isbtagged_DL1rmu_77)""").queue()
#Observable("tjet_isbtag_DL1rmu70", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.tjet_isbtagged_DL1rmu_70)""").queue()
#Observable("tjet_isbtag_DL1rmu60", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.tjet_isbtagged_DL1rmu_60)""").queue()
#Observable("tjet_isbtag_MV2c1085", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.tjet_isbtagged_MV2c10_85)""").queue()
#Observable("tjet_isbtag_MV2c1077", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.tjet_isbtagged_MV2c10_77)""").queue()
#Observable("tjet_isbtag_MV2c1070", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.tjet_isbtagged_MV2c10_70)""").queue()
#Observable("tjet_isbtag_MV2c1060", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.tjet_isbtagged_MV2c10_60)""").queue()
#Observable("tjet_isbtag_MV2r85", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.tjet_isbtagged_MV2r_85)""").queue()
#Observable("tjet_isbtag_MV2r77", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.tjet_isbtagged_MV2r_77)""").queue()
#Observable("tjet_isbtag_MV2r70", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.tjet_isbtagged_MV2r_70)""").queue()
#Observable("tjet_isbtag_MV2r60", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.tjet_isbtagged_MV2r_60)""").queue()
#Observable("tjet_isbtag_MV2rmu85", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.tjet_isbtagged_MV2rmu_85)""").queue()
#Observable("tjet_isbtag_MV2rmu77", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.tjet_isbtagged_MV2rmu_77)""").queue()
#Observable("tjet_isbtag_MV2rmu70", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.tjet_isbtagged_MV2rmu_70)""").queue()
#Observable("tjet_isbtag_MV2rmu60", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(ord(x) for x in sel.tjet_isbtagged_MV2rmu_60)""").queue()
#tjet DL1 discriinants
# Observable("tjet_DL1_pu", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(x for x in sel.tjet_DL1_pu)""").queue()
# Observable("tjet_DL1_pb", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(x for x in sel.tjet_DL1_pb)""").queue()
# Observable("tjet_DL1_pc", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(x for x in sel.tjet_DL1_pc)""").queue()
# Observable("tjet_DL1r_pu", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(x for x in sel.tjet_DL1r_pu)""").queue()
# Observable("tjet_DL1r_pb", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(x for x in sel.tjet_DL1r_pb)""").queue()
# Observable("tjet_DL1r_pc", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(x for x in sel.tjet_DL1r_pc)""").queue()
# Observable("tjet_DL1rmu_pu", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(x for x in sel.tjet_DL1rmu_pu)""").queue()
# Observable("tjet_DL1rmu_pb", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(x for x in sel.tjet_DL1rmu_pb)""").queue()
# Observable("tjet_DL1rmu_pc", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(x for x in sel.tjet_DL1rmu_pc)""").queue()

# Observable("tjet_MV2c10", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(x for x in sel.tjet_mv2c10)""").queue()
# Observable("tjet_MV2r", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(x for x in sel.tjet_MV2r)""").queue()
# Observable("tjet_MV2rmu", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu'], script = """(x for x in sel.tjet_MV2rmu)""").queue()
# Observable("tjet_label", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu', 'bFH'], script = """(x for x in sel.tjet_label)""").queue()
# Observable("tjet_ghostlabel", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu', 'bFH'], script = """(x for x in sel.tjet_ghostlabel)""").queue()
# Observable("tjet_numConstituents", do = ['tree'], style = 'foreach', only = ['be', 'bmu', 're', 'rmu', 'bFH'], script = """(x for x in sel.tjet_numConstituents)""").queue()


#truth variables
# Observable("t_afterFSR_SC_pt", do = ['tree'], only = ['re', 'rmu', 'be', 'bmu'], script = """sel.MC_t_afterFSR_SC_pt*1e-3""").queue()
# Observable("t_afterFSR_SC_eta", do = ['tree'], only = ['re', 'rmu', 'be', 'bmu'], script = """sel.MC_t_afterFSR_SC_eta""").queue()
# Observable("t_afterFSR_SC_phi", do = ['tree'], only = ['re', 'rmu', 'be', 'bmu'], script = """sel.MC_t_afterFSR_SC_phi""").queue()
# Observable("t_afterFSR_SC_m", do = ['tree'], only = ['re', 'rmu', 'be', 'bmu'], script = """sel.MC_t_afterFSR_SC_m*1e-3""").queue()

# Observable("tbar_afterFSR_SC_pt", do = ['tree'], only = ['re', 'rmu', 'be', 'bmu'], script = """sel.MC_tbar_afterFSR_SC_pt*1e-3""").queue()
# Observable("tbar_afterFSR_SC_eta", do = ['tree'], only = ['re', 'rmu', 'be', 'bmu'], script = """sel.MC_tbar_afterFSR_SC_eta""").queue()
# Observable("tbar_afterFSR_SC_phi", do = ['tree'], only = ['re', 'rmu', 'be', 'bmu'], script = """sel.MC_tbar_afterFSR_SC_phi""").queue()
# Observable("tbar_afterFSR_SC_m", do = ['tree'], only = ['re', 'rmu', 'be', 'bmu'], script = """sel.MC_tbar_afterFSR_SC_m*1e-3""").queue()


# Observable("ttbar_afterFSR_SC_m", do = ['tree'], only = ['re', 'rmu', 'be', 'bmu'], script = """sel.MC_ttbar_afterFSR_SC_m*1e-3""").queue()




### Jet Substructure ###
Observable("th1_tau21_wta", do = ['tree'], only = ['bFH'], script = """sel.ljet_tau21_wta[goodJetIdx1] if goodJetIdx1 != -1 else -999""").queue()
Observable("th1_tau32_wta", do = ['tree'], only = ['bFH'], script = """sel.ljet_tau32_wta[goodJetIdx1] if goodJetIdx1 != -1 else -999""").queue()
Observable("th2_tau21_wta", do = ['tree'], only = ['bFH'], script = """sel.ljet_tau21_wta[goodJetIdx2] if goodJetIdx2 != -1 else -999""").queue()
Observable("th2_tau32_wta", do = ['tree'], only = ['bFH'], script = """sel.ljet_tau32_wta[goodJetIdx2] if goodJetIdx2 != -1 else -999""").queue()
# Observable("th_C2", (26, 0, 2), do = ['hist','tree'], only = ['b'], script = """sel.ljet_C2[analysis.top_tagger.thad_index] if analysis.top_tagger.thad_index != -1 else -999""").queue()
# Observable("th_D2", (26, 0, 5), do = ['hist','tree'], only = ['b'], script = """sel.ljet_D2[analysis.top_tagger.thad_index] if analysis.top_tagger.thad_index != -1 else -999""").queue()
# Observable("th_MClike", (4, -1, 3), dtype = int, do = ['hist','tree'], only = ['b'], script = """sel.ljet_MClike[analysis.top_tagger.thad_index] if analysis.top_tagger.thad_index != -1 else -1""").queue()

### Pileup ###
# Observable("mu", do = ['tree'], style = 'single', script = """sel.mu""").queue()
# Observable("npv", do = ['tree'], style = 'single', dtype = int, script = """sel.npv""").queue()
# Observable("vtxz", do = ['tree'], style = 'single', script = """sel.vtxz""").queue()
# Observable("lumiblock", do = ['tree'], style = 'single', script = """sel.lumiblock""").queue()
