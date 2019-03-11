# -*- coding: utf-8 -*-
"""Up!fss!jt!ivnbo!.!boe!up!cmbnf!ju!po!b!dpnqvufs!jt!fwfo!npsf!tp/"""
import sys
import ROOT
try:
    import TopNtupleAnalysis.helpers as helpers
except:
    import python.helpers as helpers
logger = helpers.getLogger("TopNtupleAnalysis.test")
try:
    try:
        __IPYTHON__
    except NameError:
        from IPython.core.ultratb import AutoFormattedTB
        sys.excepthook = AutoFormattedTB()
except ImportError:
    logger.warn('IPython is not installed. Colored Traceback will not be populated.')

logger.info("Start Test!")
logger.info("{:<30} [{}]".format('Check "Main Program"', "1/4"))
helpers.initialise_binds()
ROOT.TopNtupleAnalysis.initWrapper()
logger.info("{:<30} [{}]".format('Check "DMWeight"',"2/4"))
logger.debug("w_DM(E=1000GeV, x=800GeV)={:.4g}".format(ROOT.TopNtupleAnalysis.wfunction(1000,800)))
logger.info("{:<30} [{}]".format('Check "EFTLib"', "3/4"))
ROOT.TopNtupleAnalysis.initPDF("CT10")
logger.debug(u"α(Mz)={:.4g}".format(ROOT.TopNtupleAnalysis.alphaS(91.19**2)))
# logger.info("{:<30} [{}]".format('Check "NNLOReweighter"', "4/4"))
# # try:
# #     ROOT.NNLOReweighterTool("TEST")
# # except Exception as e:
# #     logger.error('Unable to import "NNLOReweighterTool". Are you sure that it is installed?')
# #     raise e

# ROOT.TopNtupleAnalysis.InitNNLO(410470) 
# logger.debug(u"NNLOWeight(pT(ttbar)=1000GeV, pT(t)=1000GeV)={:.4g}".format(ROOT.TopNtupleAnalysis.getNNLOWeight(1000, 1000, 1)))

logger.info("{:<30} [{}]".format('Check "TTbarNNLOReweighter"', "4/4"))
class PseudoEvent(object):
    mcChannelNumber = 410470
    MC_t_afterFSR_SC_pt = 1000000
from TopNtupleAnalysis.reweighting import TTbarNNLOReweighting
TTbarNNLOReweighting.init(PseudoEvent.mcChannelNumber)
logger.debug(u"TTbarNNLOWeight(pT(t)={:.0f}GeV)={:.4g}".format(PseudoEvent.MC_t_afterFSR_SC_pt*1e-3, TTbarNNLOReweighting.get_weight(PseudoEvent)))
logger.info("All Tests Passed!")