# -*- coding: utf-8 -*-
import sys
import ROOT
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
logger.info("{:<30} [{}]".format('Check "NNLOReweighter"', "4/4"))
ROOT.TopNtupleAnalysis.InitNNLO(410501) 
logger.debug(u"NNLOWeight(ttbar pT=1000GeV, t pT=1000GeV)={:.4g}".format(ROOT.TopNtupleAnalysis.getNNLOWeight(1000, 1000, 1)))
logger.info("All Tests Passed!")