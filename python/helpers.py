import ROOT
import math
import sys
import ast
import os
import re
sys.path.append('2HDM')

run_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
root_path = os.path.join(run_path, os.pardir)
data_path = os.path.join(root_path, 'share')

BINDS_INITIASIZED = False

import logging

msgfmt = '%(asctime)s %(levelname)-7s %(name)-20s %(message)s'
datefmt = '%H:%M:%S'

def getLogger(name = None, level = logging.DEBUG):
    logger = logging.getLogger(name)
    try:
        import coloredlogs
        coloredlogs.install(logger = logger, level = level, fmt = msgfmt, datefmt = datefmt)
    except ImportError:
        logging.basicConfig(format = msgfmt, datefmt = datefmt)
        logger.setLevel(level)
    return logger
logger = getLogger('TopNtupleAnalysis')

## Initialise the T2HDM class and load the precompiled modules
nameX = ""
noX   = ""
mX    = -1
tanb  = -1
typeX = -1
sba   = -999
cutsX = ""
def init2HDM(MH,MA,SBA,TANB,TYPE):
    import T2HDM
    ### Needed to modify global copies of these vars:
    global T2HDM
    global nameX
    global noX
    global mX
    global tanb
    global typeX
    global sba
    global cutsX
    ### No need for global declaration to read value of these vars
    ############
    nameX = "H" if(MH>0) else "A"
    noX   = "h" if(nameX=="A") else "h1"
    mX    = MH if(MH>0) else MA
    tanb  = TANB
    typeX = TYPE
    sba   = SBA
    #############################################
    T2HDM.reset(nameX,mX,typeX,sba,tanb,True) ###
    #############################################
    print "cuts:",T2HDM.model.cuts
    print "parameters:",T2HDM.model.parameters
    print T2HDM.model.modules


def loadXsec(m, fName):
    f = open(fName)
    for l in f.readlines():
        if l[0] == '#':
            continue
        lsplit = l.split()
        if len(lsplit) == 0:
            continue
        if len(lsplit) < 3:
            print "I cannot understand this line:", lsplit
            continue
        m[int(lsplit[0])] = float(lsplit[1])*float(lsplit[2])

def addFilesInChain(c, txtFileOption, n = -1):
    counter = 0
    for f in txtFileOption.split(','):
        txtf = open(f)
        for l in txtf.readlines():
            if l[-1] == '\n':
                l = l[0:-1]
            if counter > n and n > 0:
                break
            c.Add(l)
            counter += 1
        if counter > n:
            break

class Event:
    def __init__(self):
        pass

MV2C10_CUT = 0.66
# systematic variations are specified according to this syntax:
# btag[A]SF_[eig][_pt[X]]__1[up/down]
# where:
# [A] = b,c,l,e for b-jet, c-jet, light-jet or extrapolation variations
# [eig] is the number of the eigen vector
# [X] is the number of the pt bin if we want to vary only jets within a pt bin
# if there is no 'btag' in the name of the variation, then the nominal SF is used
def applyBtagSF(sel, s):
    if sel.mcChannelNumber == 0:
        return 1
    ptbinInS = -1
    if 'btag' in s and 'pt' in s:
        ptbinInS = int(s.split('pt')[1][0])

    jetList = ROOT.vector('TLorentzVector')()
    jetFlavour = ROOT.vector('int')()
    jetWeight = ROOT.vector('float')()
    vetoSyst = ROOT.vector('bool')()
    for k in range(0, len(sel.tjet_pt)):
        j = ROOT.TLorentzVector()
        j.SetPtEtaPhiE(sel.tjet_pt[k], sel.tjet_eta[k], sel.tjet_phi[k], sel.tjet_e[k])
        jetList.push_back(j)
        jetFlavour.push_back(int(sel.tjet_label[k]))
        jetWeight.push_back(float(sel.tjet_mv2c10[k]))
        ptbin = -1
        if ptbinInS >= 0:
            if jetList[k].Perp() < 50e3:
                ptbin = 1
            elif jetList[k].Perp() < 100e3:
                ptbin = 2
            else:
                ptbin = 3
        if ptbinInS == ptbin:
            # if this jet is in the correct pt bin, apply the syst. variation
            vetoSyst.push_back(False)
        else:
            # otherwise, take the nominal SF for this jet
            # even if we are supposed to vary it for any other criteria
            vetoSyst.push_back(True)
    syst = ""
    if 'down' in s:
        direction = 'down'
    else:
        direction = 'up'
    eig = -1
    if 'btagbSF_' in s:
        eig = int(s.split('_')[1])
        syst = "FT_EFF_Eigen_B_%d__1%s" % (eig, direction)
    elif 'btagcSF_' in s:
        eig = int(s.split('_')[1])
        syst = "FT_EFF_Eigen_C_%d__1%s" % (eig, direction)
    elif 'btaglSF_' in s:
        eig = int(s.split('_')[1])
        syst = "FT_EFF_Eigen_Light_%d__1%s" % (eig, direction)
    elif 'btageSF_0' in s:
        syst = "FT_EFF_Eigen_extrapolation__1%s" % (direction)
    elif 'btageSF_1' in s:
        syst = "FT_EFF_Eigen_extrapolation from charm__1%s" % (direction)
    return ROOT.getBtaggingSF(jetList, jetFlavour, jetWeight, vetoSyst, syst)

# same as above, but it reads the SFs from the file
def applyBtagSFFromFile(sel, s):
    pref = 'tjet_bTagSF_70'
    varName = ''
    nomName = pref
    ptbinInS = 0
    eig = -1
    # if this is a b-tagging variation
    # then check which branch to take to apply the variation
    if 'btag' in s:
        # if we are also varying only jets in a specific pt bin, the pt bin is identified as "ptX", where X is an integer
        # get "X" as an integer from the systematic name
        if 'pt' in s:
            ptbinInS = int(s.split('pt')[1][0])
            # later, if this is != -1, we will use it to apply the variation only at the jets within this pt bin
        # get direction
        direction = 'up'
        if 'down' in s:
            direction = 'down'
        # check if it is a b,c,light or extrapolation variation and set name
        if 'btagbSF_' in s:
            varName = pref+'_eigen_B_'+direction
            # get eigenvector index
            eig = int(s.split('_')[1])
        if 'btagcSF_' in s:
            varName = pref+'_eigen_C_'+direction
            # get eigenvector index
            eig = int(s.split('_')[1])
        if 'btaglSF_' in s:
            varName = pref+'_eigen_Light_'+direction
            # get eigenvector index
            eig = int(s.split('_')[1])
        if 'btageSF_0' in s:
            varName = pref+'_syst_extrapolation_'+direction
            eig = -1
        if 'btageSF_1' in s:
            varName = pref+'_syst_extrapolation_from_charm_'+direction
            eig = -1
    else: # not a b-tagging variation, so take the nominal
        varName = pref

    btagsf = 1.0
    # loop over track jets
    for bidx in range(0, len(sel.tjet_mv2c20)):
        pb = ROOT.TLorentzVector()
        pb.SetPtEtaPhiE(sel.tjet_pt[bidx], sel.tjet_eta[bidx], sel.tjet_phi[bidx], sel.tjet_e[bidx])
        # and apply object definition cuts (should already have been applied)
        if pb.Perp() > 10e3 and math.fabs(pb.Eta()) < 2.5 and sel.tjet_numConstituents[bidx] >= 2:
            # if we requested to vary only jets in a specific pt bin, check if this jet is in the pt bin
            vetoed = False
            if ptbinInS != 0:
                ptbin = 0
                if pb.Perp() < 50e3:
                    ptbin = 1
                elif pb.Perp() < 100e3:
                    ptbin = 2
                else:
                    ptbin = 3
                if ptbinInS == ptbin:
                    # if this jet is in the correct pt bin, apply the syst. variation
                    theWeight = getattr(sel, varName)
                else:
                    # otherwise, take the nominal SF for this jet
                    # even if we are supposed to vary it for any other criteria
                    theWeight = getattr(sel, nomName)
                    vetoed = True
            else: # we have not requested the pt binned variation
                # so we always vary all jets, regardless of the pt bin
                # if no variation was requested, varName will be set to the nominal above
                theWeight = getattr(sel, varName)
            if eig > -1 and not vetoed: # branches in b,c,light variation have a second index related to the eigenvector number
                btagsf *= theWeight[bidx][eig]
            else: # extrapolation branches or the nominal, have no second index
                btagsf *= theWeight[bidx]
    return btagsf

# TODO
def readEvent(mt):
    return mt

listEWK = [410000, 301528, 301529, 301530, 301531, 301532]
def applyEWK(sel, s):
    if sel.mcChannelNumber == 0:
        return 1
    top = ROOT.TLorentzVector()
    top.SetPtEtaPhiM(sel.MC_t_pt, sel.MC_t_eta, sel.MC_t_phi, sel.MC_t_m)
    topbar = ROOT.TLorentzVector()
    topbar.SetPtEtaPhiM(sel.MC_tbar_pt, sel.MC_tbar_eta, sel.MC_tbar_phi, sel.MC_tbar_m)
    if s == 'ttEWK__1up':
        w = ROOT.TopNtupleAnalysis.getEWK(top, topbar, sel.initial_type, 1)
    elif s == 'ttEWK__1down':
        w = ROOT.TopNtupleAnalysis.getEWK(top, topbar, sel.initial_type, 2)
    else:
        w = ROOT.TopNtupleAnalysis.getEWK(top, topbar, sel.initial_type, 0)
    return w


'''
SM topo's         |  H/A matched topo's  | H/A partially matched topo's
------------------+----------------------+-------------------------------
P0_gg_ttx         |  P0_gg_ttx           |
P0_uux_ttx        |  P0_uux_ttx          |  P0_bbx_ttx
P1_uux_ttxg       |  P1_uux_ttxg         |  P1_bbx_ttxg
P1_gux_ttxux      |  P1_gux_ttxux        |  P1_gbx_ttxbx
P1_gu_ttxu        |  P1_gu_ttxu          |  P1_gb_ttxb
P1_gg_ttxg        |  P1_gg_ttxg          |
P2_gu_ttxgu       |  P2_gu_ttxgu         |  P2_gb_ttxgb
P2_uxux_ttxuxux   |  P2_uxux_ttxuxux     |  P2_bxbx_ttxbxbx
P2_uxcx_ttxuxcx   |  P2_uxcx_ttxuxcx     |  P2_uxbx_ttxuxbx
P2_uux_ttxuux     |  P2_uux_ttxuux       |  P2_bbx_ttxbbx
P2_uux_ttxgg      |  P2_uux_ttxgg        |  P2_bbx_ttxgg
P2_uux_ttxccx     |  P2_uux_ttxccx       |  P2_uux_ttxbbx  P2_bbx_ttxuux(?)
P2_uu_ttxuu       |  P2_uu_ttxuu         |  P2_bb_ttxbb
P2_ucx_ttxucx     |  P2_ucx_ttxucx       |  P2_ubx_ttxubx
P2_uc_ttxuc       |  P2_uc_ttxuc         |  P2_ub_ttxub
P2_gux_ttxgux     |  P2_gux_ttxgux       |  P2_gbx_ttxgbx
P2_gg_ttxgg       |  P2_gg_ttxgg         |
P2_gg_ttxuux      |  P2_gg_ttxuux        |  P2_gg_ttxbbx

H/A unmatched topo's:
P2_uxb_ttxuxb (?)
'''

def getTopology(prod,id1,id2=999):
    isProd = True if(prod!="") else False
    topology = ""
    GLU=21
    TOP=6
    CHM=4
    idsum = id1+id2
    absidsum = abs(id1)+abs(id2)
    absidsub = abs(abs(id1)-abs(id2))
    if(abs(id2)>GLU):
        if(id1==GLU):                            topology = "g"
        if(abs(id1)<TOP and id1>0):              topology = "u"
        if(abs(id1)<TOP and id1<0):              topology = "ux"
    elif(idsum==2*GLU):                          topology = "gg"
    elif(idsum==0 and id1<TOP):                  topology = "uux"
    elif(idsum==0 and id1>=CHM and prod=="uux"): topology = "ccx"
    elif(idsum>GLU and idsum<2*GLU):             topology = "gu"
    elif(idsum<GLU and idsum>=GLU-TOP):          topology = "gux"
    elif(absidsum<2*TOP):
        if(id1>0           and absidsub==0):     topology = "uu"
        if(id1<0           and absidsub==0):     topology = "uxux"
        if(id1>0 and id2>0 and absidsub>0):      topology = "uc"
        if(id1*id2<0       and absidsub>0):      topology = "ucx"
        if(id1<0 and id2<0 and absidsub>0):      topology = "uxcx"
    else:
        logger.critical("Cannot understand the topology - quitting")
        quit()
    return topology

def combineTopology(ids):
    topology = ""
    n = len(ids)
    if(n==4): topology += "P0_"
    if(n==5): topology += "P1_"
    if(n==6): topology += "P2_"
    prod = getTopology("",ids[0],ids[1])
    topology += prod
    topology += "_ttx" ## should be always there...
    decay = ""
    if(n==5): decay = getTopology(prod,ids[4])
    if(n==6): decay = getTopology(prod,ids[4],ids[5])
    topology += decay
    return topology

def stripTopology(topology):
    topology = topology.replace("P0_","")
    topology = topology.replace("P1_","")
    topology = topology.replace("P2_","")
    topology = topology.replace("_","")
    return topology

def correct2HDMTopology(sel,topology):
    n = len(sel.MC_id_me)
    topoparts = topology.split("_")
    if(len(topoparts)<3):
        logger.error("Error: topoparts=%s",topoparts)
        logger.error("Too few topo parts - quitting")
        quit()
    BOT=5
    if(n==4 and abs(sel.MC_id_me[0])!=BOT and abs(sel.MC_id_me[1])!=BOT): return topology
    if(n==5 and abs(sel.MC_id_me[0])!=BOT and abs(sel.MC_id_me[1])!=BOT and abs(sel.MC_id_me[4])!=BOT): return topology
    if(n==6 and abs(sel.MC_id_me[0])!=BOT and abs(sel.MC_id_me[1])!=BOT and abs(sel.MC_id_me[4])!=BOT and abs(sel.MC_id_me[5])!=BOT): return topology
    prod  = topoparts[1]
    decay = topoparts[2].replace("ttx","")
    if(abs(sel.MC_id_me[0])==BOT or abs(sel.MC_id_me[1])==BOT):
        if(prod=="uux"):                                               prod = "bbx"
        elif(prod=="gu" or prod=="gux" or prod=="uu" or prod=="uxux"): prod = prod.replace("u","b")
        elif(prod=="uc" or prod=="ucx" or prod=="uxcx"):               prod = prod.replace("c","b")
        else:
            logger.error("Cannot understand the production with b's - quitting:%s",prod)
            logger.error("Topology is:%s",topology)
            quit()
    if(n==5 and abs(sel.MC_id_me[4])==BOT):
        if(decay=="u" or decay=="ux"): decay = decay.replace("u","b")
        else:
            print "Cannot understand the decay with b's (n=5)- quitting:",decay
            quit()
    if(n==6 and (abs(sel.MC_id_me[4])==BOT or abs(sel.MC_id_me[5])==BOT)):
        if(decay=="uux"):                                                    decay = "bbx"
        elif(decay=="gu" or decay=="gux" or decay=="uu"   or decay=="uxux"): decay = decay.replace("u","b")
        elif(decay=="uc" or decay=="ucx" or decay=="uxcx" or decay=="ccx"):  decay = decay.replace("c","b")
        else:
            print "Cannot understand the decay with b's (n=6) - quitting:",decay
            quit()
    topology = topoparts[0]+"_"+prod+"_ttx"+decay
    for i in xrange(3,len(topoparts)): topology += "_"+topoparts[i]
    return topology

def getMomenta(sel,topology):
    n = len(sel.MC_id_me)
    topoparts = topology.split("_")
    if(len(topoparts)<3):
        print "Error: topoparts=",topoparts
        print "Too few topo parts - quitting"
        quit()
    prod  = topoparts[1]
    decay = topoparts[2].replace("ttx","")
    GLU=21
    TOP=6
    CHM=4
    me = {}
    ### Fill production partons' momenta ###
    if(prod=="gg" or prod=="uu" or prod=="uxux"):
        me.update({"p1":{"id":sel.MC_id_me[0],"idx":0}})
        me.update({"p2":{"id":sel.MC_id_me[1],"idx":1}})
    elif(prod=="uux"):
        q  = 0 if(sel.MC_id_me[0]>0) else 1
        qx = 1 if(sel.MC_id_me[0]>0) else 0
        me.update({"p1":{"id":sel.MC_id_me[q], "idx":q}})
        me.update({"p2":{"id":sel.MC_id_me[qx],"idx":qx}})
    elif(prod=="gu" or prod=="gux"):
        g = 0 if(sel.MC_id_me[0]==GLU) else 1
        q = 1 if(sel.MC_id_me[0]==GLU) else 0
        me.update({"p1":{"id":sel.MC_id_me[g],"idx":g}})
        me.update({"p2":{"id":sel.MC_id_me[q],"idx":q}})
    elif(prod=="uc" or prod=="ucx" or prod=="uxcx"):
        qLight = 0 if(abs(sel.MC_id_me[0])<abs(sel.MC_id_me[1])) else 1
        qHeavy = 1 if(abs(sel.MC_id_me[0])<abs(sel.MC_id_me[1])) else 0
        me.update({"p1":{"id":sel.MC_id_me[qLight],"idx":qLight}})
        me.update({"p2":{"id":sel.MC_id_me[qHeavy],"idx":qHeavy}})
    else:
        print "Cannot understand the production - quitting"
        quit()
    ### Fill top quarks' momenta ###
    t  = 2 if(sel.MC_id_me[2]>0) else 3
    tx = 3 if(sel.MC_id_me[2]>0) else 2
    me.update({"t1":{"id":sel.MC_id_me[t], "idx":t}})
    me.update({"t2":{"id":sel.MC_id_me[tx],"idx":tx}})
    ### Fill extra partons' momenta ###
    if(n==5):
        if(decay=="g" or decay=="u" or decay=="ux"):
            me.update({"j1":{"id":sel.MC_id_me[4],"idx":4}})
    if(n==6):
        if(decay=="gg" or decay=="uu" or decay=="uxux"):
            me.update({"j1":{"id":sel.MC_id_me[4],"idx":4}})
            me.update({"j2":{"id":sel.MC_id_me[5],"idx":5}})
        elif(decay=="uux" or decay=="ccx"):
            q  = 4 if(sel.MC_id_me[4]>0) else 5
            qx = 5 if(sel.MC_id_me[4]>0) else 4
            me.update({"j1":{"id":sel.MC_id_me[q], "idx":q}})
            me.update({"j2":{"id":sel.MC_id_me[qx],"idx":qx}})
        elif(decay=="gu" or decay=="gux"):
            g = 4 if(sel.MC_id_me[4]==GLU) else 5
            q = 5 if(sel.MC_id_me[4]==GLU) else 4
            me.update({"j1":{"id":sel.MC_id_me[g],"idx":g}})
            me.update({"j2":{"id":sel.MC_id_me[q],"idx":q}})
        elif(decay=="uc" or decay=="ucx" or decay=="uxcx"):
            qLight = 4 if(abs(sel.MC_id_me[4])<abs(sel.MC_id_me[5])) else 5
            qHeavy = 5 if(abs(sel.MC_id_me[4])<abs(sel.MC_id_me[5])) else 4
            me.update({"j1":{"id":sel.MC_id_me[qLight],"idx":qLight}})
            me.update({"j2":{"id":sel.MC_id_me[qHeavy],"idx":qHeavy}})
        else:
            print "Cannot understand the decay - quitting"
            quit()
    ### Fill the momenta array
    p = [[ sel.MC_e_me[me["p1"]["idx"]], sel.MC_px_me[me["p1"]["idx"]], sel.MC_py_me[me["p1"]["idx"]], sel.MC_pz_me[me["p1"]["idx"]] ],
         [ sel.MC_e_me[me["p2"]["idx"]], sel.MC_px_me[me["p2"]["idx"]], sel.MC_py_me[me["p2"]["idx"]], sel.MC_pz_me[me["p2"]["idx"]] ],
         [ sel.MC_e_me[me["t1"]["idx"]], sel.MC_px_me[me["t1"]["idx"]], sel.MC_py_me[me["t1"]["idx"]], sel.MC_pz_me[me["t1"]["idx"]] ],
         [ sel.MC_e_me[me["t2"]["idx"]], sel.MC_px_me[me["t2"]["idx"]], sel.MC_py_me[me["t2"]["idx"]], sel.MC_pz_me[me["t2"]["idx"]] ]]
    if(n>4): p.append([ sel.MC_e_me[me["j1"]["idx"]], sel.MC_px_me[me["j1"]["idx"]], sel.MC_py_me[me["j1"]["idx"]], sel.MC_pz_me[me["j1"]["idx"]] ])
    if(n>5): p.append([ sel.MC_e_me[me["j2"]["idx"]], sel.MC_px_me[me["j2"]["idx"]], sel.MC_py_me[me["j2"]["idx"]], sel.MC_pz_me[me["j2"]["idx"]] ])
    return p

def getDMWeight(sel):
    # mass in GeV
    massMap = {301322: 500, 301323: 500, 305786: 600, 301324: 750, 305787: 800, 301325: 1000, 301326: 1250, 301327: 1500, 301328: 1750, 301329: 2000, 301330: 2250, 301331: 2500,301332: 2750, 301333: 3000, 301334: 4000, 301335: 5000}
    try:
        mass = massMap[sel.mcChannelNumber]
    except: # no mc id in this map, do not reweight
        return 1.0
    return ROOT.TopNtupleAnalysis.wfunction(mass, sel.MC_ttbar_beforeFSR_m*1e-3)

def getKKgluonWidthWeight(width, sel, s = ""):
    if sel.MC_ttbar_beforeFSR_m < 0:
        return 0             # strange cases where no ttbar system can be found
    # mass in GeV integer
    # width in percent of the mass (integer)
    # s-hat in GeV^2

    # mass in TeV
    massMap = {307522: 0.5, 307523: 1.0, 307524: 1.5, 307527: 2.0, 307528: 2.5, 307529: 3.0, 307530: 3.5, 307531: 4.0, 307532: 4.5, 307533: 5.0}
    try:
        mass = massMap[sel.mcChannelNumber]*1e3 # convert to GeV
    except: # no mc id in this map, do not reweight
        return 1.0

    # define constants here
    gL = 1.0  # Left handed coupling
    #c = 0.897597901026  # this is 12 pi / (2*21) (6 flavour) sqrt(shat)
    c = 1.7951958020 #     this is 12*pi/21 (6 flavour)
    #c = 1.6390918193 #   this is 12*pi/23 (5 flavour)
    lambd = 0.020736 # LambdaQCD^2 (lambda =0.114 GeV)
    mtop = 172.5 # value used in Pythia GeV
    widthgenerated = 30 # generation with 30% width
    widthdict = {10:0, 15:1, 20:2, 25:3, 30:4, 35:5, 40:6} #width in % of the mass corresponding to the elements of the coupling tuples, in order.
    couplings = { 500: (3.35864, 4.36281, 5.18957, 5.90898, 6.55443, 7.1449,  7.69242),
                 1000: (3.15336, 4.03605, 4.76074, 5.39045, 5.95493, 6.47103, 6.94941),
                 1500: (3.19865, 4.07595, 4.79675, 5.42331, 5.98509, 6.49881, 6.97502),
                 2000: (3.24571, 4.12691, 4.85131, 5.48118, 6.04603, 6.56261, 7.04151),
                 2500: (3.28571, 4.17137, 4.89963, 5.53294, 6.10091, 6.62038, 7.10198),
                 3000: (3.31913, 4.21034, 4.94371, 5.58171, 6.15402, 6.67753, 7.16293),
                 3500: (3.34819, 4.24361, 4.98054, 5.62167, 6.1968,  6.72291, 7.21073),
                 4000: (3.37301, 4.27332, 5.01479, 5.66009, 6.23910, 6.76882, 7.26003),
                 4500: (3.39536, 4.29965, 5.04467, 5.69319, 6.27514, 6.8076,  7.30138),
                 5000: (3.41544, 4.32278, 5.07040, 5.72120, 6.30523, 6.8396,  7.33516)
                }

    #top = ROOT.TLorentzVector()
    #topbar = ROOT.TLorentzVector()
    #if sel.MC_id_me[2] > 0:
    #    top.SetPxPyPzE(sel.MC_px_me[2], sel.MC_py_me[2], sel.MC_pz_me[2], sel.MC_e_me[2])
    #    topbar.SetPxPyPzE(sel.MC_px_me[3], sel.MC_py_me[3], sel.MC_pz_me[3], sel.MC_e_me[3])
    #else:
    #    top.SetPxPyPzE(sel.MC_px_me[3], sel.MC_py_me[3], sel.MC_pz_me[3], sel.MC_e_me[3])
    #    topbar.SetPxPyPzE(sel.MC_px_me[2], sel.MC_py_me[2], sel.MC_pz_me[2], sel.MC_e_me[2])
    #shatt = (top + topbar).M2()
    shatt = ((sel.MC_ttbar_beforeFSR_m*1e-3)**2.0) # convert from MeV to GeV and then square

    alphastrong = c / math.log (shatt / lambd)  # running coupling constant
    #alphastrong=0.1;

    # uncomment these two lines if you like to reweight with fixed width, and comment corresponding lines below
    #gammag = float(widthgenerated) * float(mass) / 100.0
    #gamma  = float(width)*float(mass)/100.0

    genpos = widthdict[widthgenerated]
    gR30 = couplings[mass][genpos]
    reqpos =  widthdict[width]
    gRW =  couplings[mass][reqpos]
    x = mtop*mtop/ shatt
    gvgen = (gL + gR30)/2.
    gagen = (gL - gR30)/2.
    gvrw  = (gL + gRW)/ 2.
    garw  = (gL - gRW)/ 2.

    # comment these two lines to run with fixed width
    gammag = 12.5*math.sqrt(shatt)/1120. + 1./6.* alphastrong * math.sqrt(shatt * ( 1 - 4.* x )) * ( gvgen * gvgen * (1.+2.* x) + gagen * gagen * (1. - 4.*x))
    gamma  = 12.5*math.sqrt(shatt)/1120. + 1./6.* alphastrong * math.sqrt(shatt * ( 1 - 4.* x )) * ( gvrw  * gvrw  * (1.+2.* x) + garw  * garw  * (1. - 4.*x))

    # Breit Wigner reweight
    m2 = float (mass * mass)
    bwgen =   (shatt-m2)*(shatt-m2) + (shatt*gammag/float(mass))*(shatt*gammag/float(mass))
    bwrw =    (shatt-m2)*(shatt-m2) + (shatt*gamma/float(mass))*(shatt*gamma/float(mass))

    # now calculating the numerator
    weinumgen =  (gL *gL + gR30 * gR30 ) - x * ( gL*gL + gR30*gR30 - 6*gR30*gL)
    weinumrw  =  (gL *gL + gRW  * gRW  ) - x * ( gL*gL + gRW *gRW  - 6*gRW *gL)

    wr = (bwgen/bwrw) * (weinumrw / weinumgen)
    return wr


def getEFTSMWeight(sel, s = ""):
    #double getEFTSMWeight(int i1_pid, int i2_pid, std::vector<int> f_pid, TLorentzVector i1, TLorentzVector i2, TLorentzVector t, TLorentzVector tbar, std::vector<TLorentzVector> f, double Q2) {
    if sel.mcChannelNumber == 0:
        return 1
    #if not sel.mcChannelNumber in [407200, 407201, 407202, 407203, 407204]:
    #    return 1
    i1 = ROOT.TLorentzVector()
    i2 = ROOT.TLorentzVector()
    top = ROOT.TLorentzVector()
    topbar = ROOT.TLorentzVector()
    i1.SetPxPyPzE(sel.MC_px_me[0], sel.MC_py_me[0], sel.MC_pz_me[0], sel.MC_e_me[0])
    i1_pid = sel.MC_id_me[0]
    i2.SetPxPyPzE(sel.MC_px_me[1], sel.MC_py_me[1], sel.MC_pz_me[1], sel.MC_e_me[1])
    i2_pid = sel.MC_id_me[1]
    if sel.MC_id_me[2] > 0:
        top.SetPxPyPzE(sel.MC_px_me[2], sel.MC_py_me[2], sel.MC_pz_me[2], sel.MC_e_me[2])
        topbar.SetPxPyPzE(sel.MC_px_me[3], sel.MC_py_me[3], sel.MC_pz_me[3], sel.MC_e_me[3])
    else:
        top.SetPxPyPzE(sel.MC_px_me[3], sel.MC_py_me[3], sel.MC_pz_me[3], sel.MC_e_me[3])
        topbar.SetPxPyPzE(sel.MC_px_me[2], sel.MC_py_me[2], sel.MC_pz_me[2], sel.MC_e_me[2])
    f = ROOT.vector('TLorentzVector')()
    f_pid = ROOT.vector('int')()
    for idx in range(4,len(sel.MC_px_me)):
        f_pid.push_back(sel.MC_id_me[idx])
        f.push_back(ROOT.TLorentzVector(sel.MC_px_me[idx], sel.MC_py_me[idx], sel.MC_pz_me[idx], sel.MC_e_me[idx]))
    Q2 = (1e-3*sel.MC_Q_me)**2
    if 'eftScale' in s and 'up' in s:
        Q2 *= 4
    elif 'eftScale' in s and 'down' in s:
        Q2 *= 0.25
    w = getEFTSMWeight(i1_pid, i2_pid, f_pid, i1, i2, top, topbar, f, Q2)
    return w


def getTruth4momenta(sel):
    p = []
    for i in xrange(len(sel.MC_px_me)):
        p.append(ROOT.TLorentzVector())
        p[i].SetPxPyPzE(sel.MC_px_me[i],sel.MC_py_me[i],sel.MC_pz_me[i],sel.MC_e_me[i])
    return p

def print2HDM(sel,topology,alphaS,ids,pCpp,me2XX,me2SM):
    pME = getTruth4momenta(sel)
    truPttbar = (pME[2]+pME[3]).M()
    if(abs(truPttbar.M()-mX)<100):
        weightX = me2XX/me2SM
        print "# 2HDM setup: mX=%g, sba=%g, tanb=%g, type=%g --> topo=%s, mtt=%g, me2XX/me2SM=%g/%g=%g" % (mX,sba,tanb,typeX,topology,(pt1+pt2).M(),me2XX,me2SM,weightX)
        print "# ME ids are: ",ids
        print "# Q =",sel.MC_Q_me/1000.
        print "alphaS =",alphaS
        print "p=["
        for x in xrange(len(ids)):
            print "  [%g,%g,%g,%g]," % (sel.MC_e_me[x],sel.MC_px_me[x],sel.MC_py_me[x],sel.MC_pz_me[x])
        print "]"
        print "used p =", pCpp

def get2HDMWeight(sel):
    if sel.mcChannelNumber == 0:
        return 1
    if not sel.mcChannelNumber in [407200, 407201, 407202, 407203, 407204]:
        return 1
    topologySM_name = combineTopology(sel.MC_id_me)
    topologyXX_name = topologySM_name+"_no_"+noX
    topologyXX_name = correct2HDMTopology(sel,topologyXX_name)
    topologySM_lib = 'matrix2SM'+stripTopology(topologySM_name)+'py'
    topologyXX_lib = 'matrix2'+nameX+stripTopology(topologyXX_name)+'py'
    ids = []
    for i in xrange(sel.MC_id_me.size()): ids.append(sel.MC_id_me[i])
    if(topologySM_lib not in T2HDM.model.modules or topologyXX_lib not in T2HDM.model.modules):
        print "topology %s or %s (or both) is not in T2HDM.model.modules" % (topologySM_lib,topologyXX_lib)
        print "ME id's are: ",ids
        return 1
    pCpp = getMomenta(sel,topologySM_name)
    pPython = T2HDM.invert_momenta(pCpp)
    Q2 = sel.MC_Q_me*sel.MC_Q_me
    alphaS = ROOT.TopNtupleAnalysis.alphaS(Q2)
    nhel = 0 # sum over all helicities
    me2SM = T2HDM.model.modules[topologySM_lib].get_me(pPython,alphaS,nhel) ### calculate the SM ME^2
    me2XX = T2HDM.model.modules[topologyXX_lib].get_me(pPython,alphaS,nhel) ### calculate the X ME^2
    weightX = me2XX/me2SM                                                   ### calculate the weight
    #print2HDM(sel,topologySM_name,alphaS,ids,pCpp,me2XX,me2SM)             ### print basic info
    if(weightX>5 and nameX=="H"): weightX = 1.                              ### protection for a potential bug (?) in the mg model implementation
    return (weightX,me2SM,me2XX,alphaS)




listWjets22 = []
listWjets22.extend(range(363330, 363354+1))
listWjets22.extend(range(363436, 363483+1))
# 2.2.1
listWjets22.extend(range(364156, 364197+1))
#def applyWjets22Weight(sel):
#    if not sel.mcChannelNumber in listWjets22:
#        return 1.0
#    njet = 0
#    for i in range(0, len(sel.akt4truthjet_pt)):
#        if sel.akt4truthjet_pt[i] > 20e3 and fabs(sel.akt4truthjet_eta[i]) < 4.5:
#           njet += 1
#    return ROOT.TopNtupleAnalysis.getWjets22Weight(njet)

doPRW = True

# list of systematics related to changes in the weights only
weightSF = {'' : ['pileup', 'leptonSF', 'jvt'], #, 'indiv_SF_EL_ChargeID', 'indiv_SF_EL_ChargeMisID'],
            'eChargeSF__1up': ['pileup', 'leptonSF', 'jvt', 'indiv_SF_EL_ChargeID_UP'],
            'eChargeSF__1down': ['pileup', 'leptonSF', 'jvt', 'indiv_SF_EL_ChargeID_DOWN'],
            'eChargeMisIDStatSF__1up': ['pileup', 'leptonSF', 'jvt', 'indiv_SF_EL_ChargeMisID_STAT_UP'],
            'eChargeMisIDStatSF__1down': ['pileup', 'leptonSF', 'jvt', 'indiv_SF_EL_ChargeMisID_STAT_DOWN'],
            'eChargeMisIDSystSF__1up': ['pileup', 'leptonSF', 'jvt', 'indiv_SF_EL_ChargeMisID_SYST_UP'],
            'eChargeMisIDSystSF__1down': ['pileup', 'leptonSF', 'jvt', 'indiv_SF_EL_ChargeMisID_SYST_DOWN'],
            'eTrigSF__1up': ['pileup', 'leptonSF_EL_SF_Trigger_UP', 'jvt'], # 'indiv_SF_EL_ChargeMisID'],
            'eTrigSF__1down': ['pileup', 'leptonSF_EL_SF_Trigger_DOWN', 'jvt'], # 'indiv_SF_EL_ChargeMisID'],
            'eIDSF__1up': ['pileup', 'leptonSF_EL_SF_ID_UP'], #, 'jvt', 'indiv_SF_EL_ChargeID', 'indiv_SF_EL_ChargeMisID'],
            'eIDSF__1down': ['pileup', 'leptonSF_EL_SF_ID_DOWN'], #, 'jvt', 'indiv_SF_EL_ChargeID', 'indiv_SF_EL_ChargeMisID'],
            'eRecoSF__1up': ['pileup', 'leptonSF_EL_SF_Reco_UP'], #, 'jvt', 'indiv_SF_EL_ChargeID', 'indiv_SF_EL_ChargeMisID'],
            'eRecoSF__1down': ['pileup', 'leptonSF_EL_SF_Reco_DOWN'], #, 'jvt', 'indiv_SF_EL_ChargeID', 'indiv_SF_EL_ChargeMisID'],
            'eIsolSF__1up': ['pileup', 'leptonSF_EL_SF_Isol_UP', 'jvt'], # 'indiv_SF_EL_ChargeID', 'indiv_SF_EL_ChargeMisID'],
            'eIsolSF__1down': ['pileup', 'leptonSF_EL_SF_Isol_DOWN', 'jvt'], # 'indiv_SF_EL_ChargeID', 'indiv_SF_EL_ChargeMisID'],
            'muTrigStatSF__1up': ['pileup', 'leptonSF_MU_SF_Trigger_STAT_UP', 'jvt'], # 'indiv_SF_EL_ChargeID', 'indiv_SF_EL_ChargeMisID'],
            'muTrigStatSF__1down': ['pileup', 'leptonSF_MU_SF_Trigger_STAT_DOWN', 'jvt'], # 'indiv_SF_EL_ChargeID', 'indiv_SF_EL_ChargeMisID'],
            'muTrigSystSF__1up': ['pileup', 'leptonSF_MU_SF_Trigger_SYST_UP', 'jvt'], # 'indiv_SF_EL_ChargeID', 'indiv_SF_EL_ChargeMisID'],
            'muTrigSystSF__1down': ['pileup', 'leptonSF_MU_SF_Trigger_SYST_DOWN', 'jvt'], # 'indiv_SF_EL_ChargeID', 'indiv_SF_EL_ChargeMisID'],
            'muIDStatSF__1up': ['pileup', 'leptonSF_MU_SF_ID_STAT_UP', 'jvt'], # 'indiv_SF_EL_ChargeID', 'indiv_SF_EL_ChargeMisID'],
            'muIDStatSF__1down': ['pileup', 'leptonSF_MU_SF_ID_STAT_DOWN', 'jvt'], # 'indiv_SF_EL_ChargeID', 'indiv_SF_EL_ChargeMisID'],
            'muIDSystSF__1up': ['pileup', 'leptonSF_MU_SF_ID_SYST_UP', 'jvt'], # 'indiv_SF_EL_ChargeID', 'indiv_SF_EL_ChargeMisID'],
            'muIDSystSF__1down': ['pileup', 'leptonSF_MU_SF_ID_SYST_DOWN', 'jvt'], # 'indiv_SF_EL_ChargeID', 'indiv_SF_EL_ChargeMisID'],
            'muIsolStatSF__1up': ['pileup', 'leptonSF_MU_SF_Isol_STAT_UP', 'jvt'], # 'indiv_SF_EL_ChargeID', 'indiv_SF_EL_ChargeMisID'],
            'muIsolStatSF__1down': ['pileup', 'leptonSF_MU_SF_Isol_STAT_DOWN', 'jvt'], # 'indiv_SF_EL_ChargeID', 'indiv_SF_EL_ChargeMisID'],
            'muIsolSystSF__1up': ['pileup', 'leptonSF_MU_SF_Isol_SYST_UP', 'jvt'], # 'indiv_SF_EL_ChargeID', 'indiv_SF_EL_ChargeMisID'],
            'muIsolSystSF__1down': ['pileup', 'leptonSF_MU_SF_Isol_SYST_DOWN', 'jvt'], # 'indiv_SF_EL_ChargeID', 'indiv_SF_EL_ChargeMisID'],
            'pileupSF__1up': ['pileup_UP', 'leptonSF', 'jvt'], #, 'indiv_SF_EL_ChargeID', 'indiv_SF_EL_ChargeMisID'],
            'pileupSF__1down': ['pileup_DOWN', 'leptonSF', 'jvt'], # 'indiv_SF_EL_ChargeID', 'indiv_SF_EL_ChargeMisID'],
            'jvtSF__1up': ['pileup', 'leptonSF', 'jvt_UP'], # 'indiv_SF_EL_ChargeID', 'indiv_SF_EL_ChargeMisID'],
            'jvtSF__1down': ['pileup', 'leptonSF', 'jvt_DOWN'], # 'indiv_SF_EL_ChargeID', 'indiv_SF_EL_ChargeMisID'],
           }

weightChangeSystematics = weightSF.keys()

def branch_parser(expr, name_fmt = "ljet_{}", index_id = 'i', tree_name = 'sel'):
    """Intuitive Python ast-style expression parser

    Used for hadronic-top tagging flag specification

    Parameters
    ----------
    expr : {str}
        Input expression. e.g., (isTopTagged_50|isTopTagged_80)&isWTagged_80
    name_fmt : {str}, optional
    index_id : {str}, optional
        which translates "(isTopTagged_50|isTopTagged_80)&isWTagged_80" to "(ljet_isTopTagged_50[i]|isTopTagged_80[i])&isWTagged_80[i]"),
        where 'i' is the id of the item.

    Returns
    -------
    program
        A program can evaluate the input expression. eval(program) := (ljet_isTopTagged_50[i]|isTopTagged_80[i])&isWTagged_80[i]
    """
    class RewriteName(ast.NodeTransformer):
        def visit_Name(self, node):
            attr = ast.Attribute(value=ast.Name(id=tree_name, ctx=ast.Load()), attr=name_fmt.format(node.id), ctx=ast.Load())
            node = ast.Subscript(value=attr, slice=ast.Index(value=ast.Name(id=index_id, ctx=ast.Load())), ctx=node.ctx)
            node = ast.Call(func=ast.Name(id='char2int',ctx=ast.Load()), args = [node], keywords=[], ctx=ast.Load())
            ast.fix_missing_locations(node)
            return node
        def visit_Str(self, node):
            node = ast.Name(id=node.s, ctx=node.ctx)
            return self.visit_Name(node)
    node_renamer = RewriteName()
    if isinstance(expr, str):
        expr = ast.parse(expr.strip(), mode = 'eval')
    else:
        expr = ast.Expression(body=expr)
    node_renamer.visit(expr)
    return compile(expr, '<top-tagger>', 'eval')

def output_expr_reader_old(expr):
    expr = expr.strip()
    if not expr.startswith('{'):
        expr = '{' + expr
    if not expr.endswith('}'):
        expr += '}'
        expr = re.sub(r"(?=[^\{]*)(.+?):(.+?)(?=[,$\}])",r'\1:"\2"', expr)
    class RewriteAsStr(ast.NodeTransformer):
        def visit_Name(self, node):
            node = ast.Str(node.id, ctx=node.ctx)
            ast.fix_missing_locations(node)
            return node
    d = ast.parse(expr, mode = 'eval')
    values = []
    for v in d.body.values:
        if isinstance(v, ast.Attribute):
            v = ast.Str("{0.value.id}.{0.attr}".format(v))
        elif isinstance(v, ast.Num):
            v = ast.Str("{.n}".format(v))
        values.append(v)
    d.body.values = values
    RewriteAsStr().visit(d.body.keys)
    d.body.keys = [k if isinstance(k, ast.Tuple) else ast.Tuple(elts=[k], ctx=k.ctx) for k in d.body.keys]
    ast.fix_missing_locations(d)
    return compile(d, '<output-expr-reader>', 'eval')

def output_expr_reader_new(expr, _type = tuple):
    if not isinstance(expr, str):
        return map(output_expr_reader_new, expr)
    expr = expr.strip()
    url_pattern = '://'
    url_like = re.match(r'(.+):([^:]+{}.+)'.format(url_pattern), expr)
    matched = url_like if url_like else re.match(r'(.+):(.+)', expr)
    selections, output_fname = map(str.strip, matched.groups())
    selections = tuple(selections.strip('()').split(','))
    return selections, output_fname

def initialise_binds():
    global BINDS_INITIASIZED
    if BINDS_INITIASIZED:
        return
    logger.info("-> Initialising binds now.")
    lib_dir = os.path.join(os.getenv("WorkDir_DIR"), "lib") if "WorkDir_DIR" in os.environ else root_path
    cintdict_dir = os.path.join(os.getenv("WorkDir_DIR"), '..', "TopNtupleAnalysis", 'CMakeFiles') if "WorkDir_DIR" in os.environ else root_path
    shared_lib = os.path.join(lib_dir, "libTopNtupleAnalysis.so")
    if os.path.exists(shared_lib):
        ROOT.gSystem.Load(shared_lib)
    else:
        ROOT.gSystem.Load(shared_lib.rsplit(".so", 1)[0] + ".dylib")
    ROOT.gROOT.LoadMacro(os.path.join(cintdict_dir, "TopNtupleAnalysisCintDict.cxx"))
    BINDS_INITIASIZED = True

# if not BINDS_INITIASIZED:
#     initialise_binds()

def char2int(char):
    if type(char) is not str:
        return char
    return ord(char)