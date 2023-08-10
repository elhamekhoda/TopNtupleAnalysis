#!/usr/bin/env python2.7
import os
from TopNtupleAnalysis import samples, run, clusters, systematics
#from pathlib2 import Path
from TopNtupleAnalysis import helpers
import sys
from collections import OrderedDict
import glob
import argparse

"""
An example of histogramming signal sample w/ M(Z')=[400, ... , 5000]GeV in l+jets analysis using batch system `HTCondor`
"""
import TopExamples.grid
import re

from datetime import datetime
today = datetime.date(datetime.now())

parser = argparse.ArgumentParser()
parser.add_argument("sample", help="the input sample name", choices=['tt', 'tt_af2', 'tt_hs', 'tt_had', 'tt_hdamp', 'tt_meoff', 'ttallhad', 'singletop', 'diboson', 'wjets2211', 'zjets2211', 'ttv', 'zprime', 'data'])
parser.add_argument('--max-inputs-per-job', type=int, default=500, help='Maximum number of input files per job')
parser.add_argument('--max-files-open-hadd', type=int, default=10, help='Maximum number of input files per job')

args = parser.parse_args()

runMCData = [args.sample]
MAX_INPUTS_PER_JOB =  args.max_inputs_per_job

############## SETTINGS ##############
# runMCData = ['zprime', 'wjets2211', 'zjets2211', 'singletop', 'diboson']
zp_map = {'zprime400':'301322', 'zprime500':'301323', 'zprime750':'301324', 'zprime1000':'301325', 'zprime1250':'301326', 'zprime1500':'301327', 'zprime1750':'301328', 'zprime2000':'301329', 'zprime2250':'301330', 'zprime2500':'301331', 'zprime2750':'301332', 'zprime3000':'301333', 'zprime4000':'301334', 'zprime5000':'301335'}
# zp_map = {'zprime3000': '301333'}
# PERIODS = ['2015+2016', '2017', '2018']
PERIODS = ['2018']
PERIODS_TO_RUN = ['2018']
ntup_dir = '/data/schuya/ttbar_resonance/ntuples/mc16e/'
outpath = '/data/schuya/ttbar_resonance/histograms/2023_07/mc16e/'
HYPER = {
         # '2015+2016':{'MC': {'suffix': '1lep.MC16a.21-02-180v10_output_root', 'period': '276262-311481', 'periodFraction': None, 'dir': 'mc16a_21.2.180', 'campaign': '2015+2016'}, 'data': {'suffix': 'FH.2015and2016.rel21.65v3_output_root', 'dir': 'mc16a_21.2.74', 'campaign': '2015+2016'}},
        #  '2017'     :{'MC': {'suffix': '1lep.ttbar.21-02-180v3_mc16d_output_root', 'period': '325713-340453', 'periodFraction': None, 'dir': 'mc16d_21.2.180', 'campaign': '2017'}, 'data': {'suffix': 'FH.2017.rel21.65v4_output_root', 'campaign': '2017'}},
         # '2017'     :{'MC': {'suffix': '1lep.MC16d_ttbar_systematics_output_root', 'period': '325713-340453', 'periodFraction': None, 'dir': 'mc16d_21.2.180', 'campaign': '2017'}, 'data': {'suffix': 'FH.2017.rel21.65v4_output_root', 'campaign': '2017'}},
         # '2017'     :{'MC': {'suffix': '1lep.zjets.21-04_systematics_mc16d2T_output_root', 'period': '325713-340453', 'periodFraction': None, 'dir': 'mc16d_21.2.180', 'campaign': '2017'}, 'data': {'suffix': 'FH.2017.rel21.65v4_output_root', 'campaign': '2017'}},
         # '2018'     :{'MC': {'suffix': '1lep.MC16d_ttbar_systematics_output_root', 'period': '348885-999999', 'periodFraction': None, 'dir': 'mc16d_21.2.180', 'campaign': '2018'}, 'data': {'suffix': '1lep.data18.21-02-155v0_output_root', 'dir': 'mc16e_21.2.155', 'campaign': '2018'}},
         '2018'     :{'MC': {'suffix': '1lep.MC16e.21-02-243_syst_output_root', 'period': '348885-999999', 'periodFraction': None, 'dir': 'mc16e_21.2.243', 'campaign': '2018'}, 'data': {'suffix': '1lep.data18.21-02-180v0_output_root', 'dir': 'mc16e_21.2.180', 'campaign': '2018'}},
                      }
TRACKJET_CLEANING = ''
BLINDING = False
RECOMPUTE_WEIGHT = False
CORRECTION = 'none'
# un-comment it for ttbar sample
# CORRECTION = 'NNLORecursive2d'
TTGENSYST = False
weight_mode = 'auto' # set to 'auto' to append to existing weights file, 'w' to overwrite
RSE_preferred = 'MWT2_UC_LOCALGROUPDISK'
SPLIT_SYSTEMATICS = True # If true, run each systematic separately. Otherwise, group systematics by tree name.
USE_CLUSTER = True
############## END SETTINGS ##############

LUMI = OrderedDict((
('2015', dict(lumi=3.21956)),
('2016', dict(lumi=32.9881)),
('2017', dict(lumi=44.3074)),
('2018', dict(lumi=58.4501)))
)

def get_lumi(*periods):
    lumi = 0
    for p in periods:
        for pp in p.split('+'):
            lumi += LUMI[pp.strip()]['lumi']
    return lumi

for hyper, d in HYPER.iteritems():
    d['MC']['periodFraction'] = get_lumi(hyper)/get_lumi(*PERIODS)

def add_sliced_dijet_samples(slices = xrange(0,13)):
    for i in slices:
        sliced_i = 'JZ%sW' % i
        ds_collection = 'MC16_13TeV_25ns_FS_EXOT4_dijets'+sliced_i
        sample_name = 'dijets_'+sliced_i
        s = TopExamples.grid.Add(ds_collection)
        dsid = 361020 + i
        s.datasets = ['mc16_13TeV.%s.Pythia8EvtGen_A14NNPDF23LO_jetjet_%s.deriv.DAOD_EXOT4.e3668_s3126_r10201_p3729' % (dsid, sliced_i)]
        samples.register_samples({(sample_name, 'EXOT4'): [ds_collection]})

add_sliced_dijet_samples()

# samples going to be processed.
# dijets sample
s = []

def compute_weight(sa):
    print(sa)
    global weight_mode
    if RECOMPUTE_WEIGHT:
        if TTGENSYST:
            samples.write_totalweight_of_samples(sa, systs = ['ttgen'], online = False, mode=weight_mode)
        else:
            samples.write_totalweight_of_samples(sa, systs = [''], online = False, mode=weight_mode)
        weight_mode = 'auto'

campaign = [HYPER[p]['MC'] for p in PERIODS_TO_RUN ]#, 'e']

if 'tt' in runMCData:
    ss = None
    for c in campaign:
        print ("c['periodFraction'] = ", c['periodFraction'])
        _ss = samples.Sample(sample_name = 'tt',
                            deriv = 'EXOT4',
                            ds_scope = 'user.elham',
                            ds_fmt_options = {'suffix': c['suffix']},
                            RSE_preferred = RSE_preferred,
                            #input_files=glob.glob(ntup_dir+c['dir']+'ttbar/user.elham.410470.PhPy8EG.DAOD_EXOT4.e6337_s3126_r10724_p4149.1lep.MC16e.21-02-155v00_syst_output_root/*'),
                            # input_files=glob.glob(ntup_dir+c['dir']+'ttbar/user.elham.410470.PhPy8EG.DAOD_EXOT4.e6337_a875_*_p4396.%s/*'%(c['suffix'])),
                            input_files=glob.glob(ntup_dir+c['dir']+'ttbar/user.bngair.410470.PhPy8EG.DAOD_EXOT4.e6337_s3126_r10201_p4396.1lep.ttbar.21-02-180v3_mc16d_output_root/*'),
                            commit_when_init = True,
                            runNumber = c['period'],
                            periodFraction = c['periodFraction']
                            )
        compute_weight([_ss])
        if ss is None:
            ss = _ss

        else:
            ss._input_files.extend(_ss._input_files)
    s += [ss]

if 'tt_af2' in runMCData:
    ss = None
    for c in campaign:
        print ("c['periodFraction'] = ", c['periodFraction'])
        _ss = samples.Sample(sample_name = 'tt_af2',
                            deriv = 'EXOT4',
                            ds_scope = 'user.bngair',
                            ds_fmt_options = {'suffix': c['suffix']},
                            RSE_preferred = RSE_preferred,
                            #input_files=glob.glob(ntup_dir+c['dir']+'ttbar/user.elham.410470.PhPy8EG.DAOD_EXOT4.e6337_s3126_r10724_p4149.1lep.MC16e.21-02-155v00_syst_output_root/*'),
                            input_files=glob.glob(ntup_dir+c['dir']+'tt_af2/user.bngair.410470.PhPy8EG.DAOD_EXOT4.e6337_a875_*_p4149.%s/*'%(c['suffix'])),
                            # input_files=glob.glob(ntup_dir+c['dir']+'ttbar/user.elham.410470.PhPy8EG.DAOD_EXOT4.e6337_s3126_*_p4396.%s/*'%(c['suffix'])),
                            commit_when_init = True,
                            runNumber = c['period'],
                            periodFraction = c['periodFraction']
                            )
        compute_weight([_ss])
        if ss is None:
            ss = _ss

        else:
            ss._input_files.extend(_ss._input_files)
    s += [ss]

if 'tt_hs' in runMCData:
    ss = None
    for c in campaign:
        print ("c['periodFraction'] = ", c['periodFraction'])
        _ss = samples.Sample(sample_name = 'tt_hs',
                            deriv = 'EXOT4',
                            ds_scope = 'user.elham',
                            ds_fmt_options = {'suffix': c['suffix']},
                            RSE_preferred = RSE_preferred,
                            input_files=glob.glob(ntup_dir+c['dir']+'tt_hs/user.bngair.41046*.*.e6762_a875_*_p4396.%s/*'%(c['suffix'])),
                            # input_files=glob.glob(ntup_dir+c['dir']+'ttbar/user.elham.410470.PhPy8EG.DAOD_EXOT4.e6337_s3126_*_p4396.%s/*'%(c['suffix'])),
                            commit_when_init = True,
                            runNumber = c['period'],
                            periodFraction = c['periodFraction']
                            )
        compute_weight([_ss])
        if ss is None:
            ss = _ss

        else:
            ss._input_files.extend(_ss._input_files)
    s += [ss]

if 'tt_had' in runMCData:
    ss = None
    for c in campaign:
        print ("c['periodFraction'] = ", c['periodFraction'])
        _ss = samples.Sample(sample_name = 'tt_had',
                            deriv = 'EXOT4',
                            ds_scope = 'user.elham',
                            ds_fmt_options = {'suffix': c['suffix']},
                            RSE_preferred = RSE_preferred,
                            input_files=glob.glob(ntup_dir+c['dir']+'tt_had/user.bngair.41055*.*_p4396.%s/*'%(c['suffix'])),
                            # input_files=glob.glob(ntup_dir+c['dir']+'ttbar/user.elham.410470.PhPy8EG.DAOD_EXOT4.e6337_s3126_*_p4396.%s/*'%(c['suffix'])),
                            commit_when_init = True,
                            runNumber = c['period'],
                            periodFraction = c['periodFraction']
                            )
        compute_weight([_ss])
        if ss is None:
            ss = _ss

        else:
            ss._input_files.extend(_ss._input_files)
    s += [ss]

if 'tt_hdamp' in runMCData:
    ss = None
    for c in campaign:
        print ("c['periodFraction'] = ", c['periodFraction'])
        _ss = samples.Sample(sample_name = 'tt_hdamp',
                            deriv = 'EXOT4',
                            ds_scope = 'user.elham',
                            ds_fmt_options = {'suffix': c['suffix']},
                            RSE_preferred = RSE_preferred,
                            input_files=glob.glob(ntup_dir+c['dir']+'tt_hdamp/user.bngair.41048*.*_p4149.%s/*'%(c['suffix'])),
                            # input_files=glob.glob(ntup_dir+c['dir']+'ttbar/user.elham.410470.PhPy8EG.DAOD_EXOT4.e6337_s3126_*_p4396.%s/*'%(c['suffix'])),
                            commit_when_init = True,
                            runNumber = c['period'],
                            periodFraction = c['periodFraction']
                            )
        compute_weight([_ss])
        if ss is None:
            ss = _ss

        else:
            ss._input_files.extend(_ss._input_files)
    s += [ss]


if 'tt_meoff' in runMCData:
    ss = None
    for c in campaign:
        print ("c['periodFraction'] = ", c['periodFraction'])
        _ss = samples.Sample(sample_name = 'tt_meoff',
                            deriv = 'TOPQ1',
                            ds_scope = 'user.elham',
                            ds_fmt_options = {'suffix': c['suffix']},
                            RSE_preferred = RSE_preferred,
                            input_files=glob.glob(ntup_dir+c['dir']+'ttbar_MECoff/user.elham.411288.*_p4346.%s/*'%(c['suffix'])),
                            # input_files=glob.glob(ntup_dir+c['dir']+'ttbar/user.elham.410470.PhPy8EG.DAOD_EXOT4.e6337_s3126_*_p4396.%s/*'%(c['suffix'])),
                            commit_when_init = True,
                            runNumber = c['period'],
                            periodFraction = c['periodFraction']
                            )
        compute_weight([_ss])
        if ss is None:
            ss = _ss

        else:
            ss._input_files.extend(_ss._input_files)
    s += [ss]

if 'ttallhad' in runMCData:
    ss = None
    for c in campaign:
        _ss = samples.Sample(sample_name = 'ttallhad',
                            #ds_pattern = '{s.ds_scope}.{{{{s.DSID[{{i}}]}}}}.*.DAOD_*.*{suffix}',
                            deriv = 'EXOT4',
                            ds_scope = 'user.elham',
                            ds_fmt_options = {'suffix': c['suffix']},
                            input_files=glob.glob(ntup_dir+c['dir']+'ttallhad/user.elham.410471.PhPy8EG.DAOD_EXOT4.*_p3729.%s/*'%(c['suffix'])),
                            #RSE_preferred = 'DESY-HH_LOCALGROUPDISK',
                            commit_when_init = True,
                            runNumber = c['period'],
                            periodFraction = c['periodFraction']
                            )
        compute_weight([_ss])
        if ss is None:
            ss = _ss

        else:
            ss._input_files.extend(_ss._input_files)
    s += [ss]

if 'singletop' in runMCData:
    ss = None
    for c in campaign:
        _ss = samples.Sample(sample_name = 'singletop',
                            #ds_pattern = '{s.ds_scope}.{{{{s.DSID[{{i}}]}}}}.*.DAOD_*.*{suffix}',
                            deriv = 'EXOT4',
                            ds_scope = 'user.elham',
                            # ds_scope = 'user.kkrowpma',
                            ds_fmt_options = {'suffix': c['suffix']},
                            input_files=glob.glob(ntup_dir+'singletop/user.elham.*.*.DAOD_EXOT4.*_p4149.%s/*'%(c['suffix'])),
                            # input_files=glob.glob(ntup_dir+c['dir']+'singletop/user.kkrowpma.*.*.DAOD_EXOT4.*_p4149.%s/*'%(c['suffix'])),
                            RSE_preferred = RSE_preferred,
                            commit_when_init = True,
                            runNumber = c['period'],
                            periodFraction = c['periodFraction']
                            )
        compute_weight([_ss])
        if ss is None:
            ss = _ss

        else:
            ss._input_files.extend(_ss._input_files)
    s += [ss]

if 'diboson' in runMCData:
    ss = None
    for c in campaign:
        _ss = samples.Sample(sample_name = 'vv',
                            #ds_pattern = '{s.ds_scope}.{{{{s.DSID[{{i}}]}}}}.*.DAOD_*.*{suffix}',
                            deriv = 'EXOT4',
                            ds_scope = 'user.elham',
                            ds_fmt_options = {'suffix': c['suffix']},
                            input_files=glob.glob(ntup_dir+'diboson/user.elham.*.*.DAOD_EXOT4.*_p4149.%s/*'%(c['suffix'])),
                            RSE_preferred = RSE_preferred,
                            commit_when_init = True,
                            runNumber = c['period'],
                            periodFraction = c['periodFraction']
                            )
        compute_weight([_ss])
        if ss is None:
            ss = _ss

        else:
            ss._input_files.extend(_ss._input_files)
    s += [ss]
    
if 'wjets2211' in runMCData:
    ss = None
    for c in campaign:
        _ss = samples.Sample(sample_name = 'wjets2211',
                            #ds_pattern = '{s.ds_scope}.{{{{s.DSID[{{i}}]}}}}.*.DAOD_*.*{suffix}',
                            deriv = 'EXOT4',
                            ds_scope = 'user.elham',
                            ds_fmt_options = {'suffix': c['suffix']},
                            input_files=glob.glob(ntup_dir+'Wjets/user.elham.*.*.DAOD_EXOT4.*_p4149.%s/*'%(c['suffix'])),
                            RSE_preferred = RSE_preferred,
                            commit_when_init = True,
                            runNumber = c['period'],
                            periodFraction = c['periodFraction']
                            )
        compute_weight([_ss])
        if ss is None:
            ss = _ss

        else:
            ss._input_files.extend(_ss._input_files)
    s += [ss]


if 'zjets2211' in runMCData:
    ss = None
    for c in campaign:
        _ss = samples.Sample(sample_name = 'zjets',
                            deriv = 'EXOT4',
                            ds_scope = 'user.elham',
                            ds_fmt_options = {'suffix': c['suffix']},
                            input_files=glob.glob(ntup_dir+'Zjets/user.elham.*.*.DAOD_EXOT4.*_p4149.%s/*'%(c['suffix'])),
                            RSE_preferred = RSE_preferred,
                            commit_when_init = True,
                            runNumber = c['period'],
                            periodFraction = c['periodFraction']
                            )
        compute_weight([_ss])
        if ss is None:
            ss = _ss

        else:
            ss._input_files.extend(_ss._input_files)
    s += [ss]


if 'ttV' in runMCData:
    ss = None
    for c in campaign:
        print ("c['periodFraction'] = ", c['periodFraction'])
        _ss = samples.Sample(sample_name = 'ttV',
                            #ds_pattern = '{s.ds_scope}.{{{{s.DSID[{{i}}]}}}}.*.DAOD_*.*{suffix}',
                            deriv = 'EXOT4',
                            ds_scope = 'user.elham',
                            ds_fmt_options = {'suffix': c['suffix']},
                            input_files=glob.glob(ntup_dir+c['dir']+'ttV/user.elham.*.*.DAOD_EXOT4.*_p4149.%s/*'%(c['suffix'])),
                            #RSE_preferred = 'CA-SFU-T2_LOCALGROUPDISK',
                            commit_when_init = True,
                            runNumber = c['period'],
                            periodFraction = c['periodFraction']
                            )
        compute_weight([_ss])
        if ss is None:
            ss = _ss

        else:
            ss._input_files.extend(_ss._input_files)
    s += [ss]

if 'zprime' in runMCData:
    for sn, deriv in samples.MAP_TO_SAMPLES:
        print(sn)
        if BLINDING:
            break
        if 'zprime' not in sn:
            continue
        if deriv != 'EXOT4':
            continue
        if sn not in zp_map:
            continue
        ss = None
        for c in campaign:
            _ss = samples.Sample(sample_name = sn,
                                deriv = deriv,
                                ds_scope = 'user.elham',
                                ds_fmt_options = {'suffix': c['suffix']},
                                #input_files=glob.glob(ntup_dir+c['dir']+'zprime/user.kkrowpma.%s.Pythia8EvtGen.DAOD_EXOT4.*_p3992.%s/*'%(zp_map[sn],c['suffix'])),
                                input_files=glob.glob(ntup_dir+'Zprime/user.elham.%s.Pythia8EvtGen.DAOD_EXOT4.*_p4149.%s/*'%(zp_map[sn],c['suffix'])),
                                #RSE_preferred = 'AGLT2_LOCALGROUPDISK',
                                RSE_preferred = 'CA-SFU-T2_LOCALGROUPDISK',
                                #download_to = os.path.join(os.curdir, 'data'),
                                commit_when_init = False,
                                runNumber = c['period'],
                                periodFraction = c['periodFraction']
                                )
            compute_weight([_ss])
            if ss is None:
                ss = _ss
            else:
                ss._input_files.extend(_ss._input_files)
        s += [ss]


if 'data' in runMCData:
    import HQTTtResonancesTools.Data_EXOT4_rel21
    campaign = [HYPER[p]['data'] for p in PERIODS_TO_RUN]#
    ss = None
    for c in campaign:
        _ss = samples.Sample(sample_name = 'data',
                              deriv = 'EXOT4',
                              ds_scope = 'user.hpang',
                              ds_fmt_options = {'suffix': c['suffix']},
                              input_files=glob.glob(ntup_dir+c['dir']+'data/user.elham.period*p4150.1lep.data18.21-02-180v0_output_root/*'),
                              RSE_preferred = 'DESY-HH_LOCALGROUPDISK',
                              commit_when_init = True
                              )
        if ss is None:
            ss = _ss
        else:
            ss._input_files.extend(_ss._input_files)
    s += [ss]

systs_nom = [
#usually useed
'nominal',
'jvtSF__1down', 
'jvtSF__1up',
'pileupSF__1down', 
'pileupSF__1up', 
# # #-----

'eChargeMisIDStatSF__1down',
'eChargeMisIDStatSF__1up',
'eChargeMisIDSystSF__1down',
'eChargeMisIDSystSF__1up',
'eChargeSF__1down',
'eChargeSF__1up',
'eIDSF__1down',
'eIDSF__1up',
'eIsolSF__1down',
'eIsolSF__1up',
'eRecoSF__1down',
'eRecoSF__1up',
'eTrigSF__1down',
'eTrigSF__1up',
'muIDStatSF__1down',
'muIDStatSF__1up',
'muIDSystSF__1down',
'muIDSystSF__1up',
'muIsolStatSF__1down',
'muIsolStatSF__1up',
'muIsolSystSF__1down',
'muIsolSystSF__1up',
'muTrigStatSF__1down',
'muTrigStatSF__1up',
'muTrigSystSF__1down',
'muTrigSystSF__1up',

#usually used
'btagbSF_0__1down',
'btagbSF_0__1up',
'btagbSF_1__1down',
'btagbSF_1__1up',
'btagbSF_2__1down',
'btagbSF_2__1up',
'btagbSF_3__1down',
'btagbSF_3__1up',
'btagbSF_4__1down',
'btagbSF_4__1up',
'btagbSF_5__1down',
'btagbSF_5__1up',
'btagbSF_6__1down',
'btagbSF_6__1up',
'btagbSF_7__1down',
'btagbSF_7__1up',
'btagbSF_8__1down',
'btagbSF_8__1up',
'btagcSF_0__1down',
'btagcSF_0__1up',
'btagcSF_1__1down',
'btagcSF_1__1up',
'btagcSF_2__1down',
'btagcSF_2__1up',
'btagcSF_3__1down',
'btagcSF_3__1up',
'btageSF_0__1down',
'btageSF_0__1up',
'btageSF_1__1down',
'btageSF_1__1up',
'btaglSF_0__1down',
'btaglSF_0__1up',
'btaglSF_1__1down',
'btaglSF_1__1up',
'btaglSF_2__1down',
'btaglSF_2__1up',
'btaglSF_3__1down',
'btaglSF_3__1up',

#top-tag SF
'toptagSF_0__1up',
'toptagSF_0__1down',
'toptagSF_1__1up',
'toptagSF_1__1down',
'toptagSF_2__1up',
'toptagSF_2__1down',
'toptagSF_3__1up',
'toptagSF_3__1down',
'toptagSF_4__1up',
'toptagSF_4__1down',
'toptagSF_5__1up',
'toptagSF_5__1down',
'toptagSF_6__1up',
'toptagSF_6__1down',
'toptagSF_7__1up',
'toptagSF_7__1down',
'toptagSF_8__1up',
'toptagSF_8__1down',
'toptagSF_9__1up',
'toptagSF_9__1down',
'toptagSF_10__1up',
'toptagSF_10__1down',
'toptagSF_11__1up',
'toptagSF_11__1down',
'toptagSF_12__1up',
'toptagSF_12__1down',
'toptagSF_13__1up',
'toptagSF_13__1down',
'toptagSF_14__1up',
'toptagSF_14__1down',
'toptagSF_15__1up',
'toptagSF_15__1down',
'toptagSF_16__1up',
'toptagSF_16__1down',
'toptagSF_17__1up',
'toptagSF_17__1down',
]

syst_ttgen = [
'tt_muF__1up',
'tt_muF__1down',
'tt_muR__1up',
'tt_muR__1down',
'tt_ISR__1up', 
'tt_ISR__1down',
'tt_FSR__1up', 
'tt_FSR__1down', 
'tt_pdf_0',
'tt_pdf_1',
'tt_pdf_2',
'tt_pdf_3',
'tt_pdf_4',
'tt_pdf_5',
'tt_pdf_6',
'tt_pdf_7',
'tt_pdf_8',
'tt_pdf_9',
'tt_pdf_10',
'tt_pdf_11',
'tt_pdf_12',
'tt_pdf_13',
'tt_pdf_14',
'tt_pdf_15',
'tt_pdf_16',
'tt_pdf_17',
'tt_pdf_18',
'tt_pdf_19',
'tt_pdf_20',
'tt_pdf_21',
'tt_pdf_22',
'tt_pdf_23',
'tt_pdf_24',
'tt_pdf_25',
'tt_pdf_26',
'tt_pdf_27',
'tt_pdf_28',
'tt_pdf_29',
'tt_pdf_30',
]

if CORRECTION == 'NNLOQCDNLOEWK':
    systs_ttbar = [
    #'ttNNLOQCDNLOEWK__1up', 
    #'ttNNLOQCDNLOEWK__1down',
    ]
elif CORRECTION == 'Rel20EWK':
    systs_ttbar = [
    'ttNNLO_seqExtended__1up', 
    'ttNNLO_seq__1up', 
    'ttNNLO_topPtDiff__1up', 
    'ttNNLO_topPt__1up',
    'ttEWK__1up',
    'ttEWK__1down'
    ]
elif CORRECTION == 'NNLORecursive2d':
    systs_ttbar = [
    # 'ttNNLOrec_toppt__1up',
    # 'ttNNLOrec_toppt__1down',
    # 'ttNNLOrec_ttmass__1up',
    # 'ttNNLOrec_ttmass__1down',
    'ttNNLOrec_muRtoppt__1up',
    'ttNNLOrec_muRtoppt__1down',
    'ttNNLOrec_muFtoppt__1up',
    'ttNNLOrec_muFtoppt__1down',
    'ttNNLOrec_muRttmass__1up',
    'ttNNLOrec_muRttmass__1down',
    'ttNNLOrec_muFttmass__1up',
    'ttNNLOrec_muFttmass__1down',
    ]
elif CORRECTION == 'NNLORecursive3d':
    systs_ttbar.extend([
    'ttNNLOrec_ttpt__1up',
    'ttNNLOrec_ttpt__1down'
    ])
else:
    systs_ttbar = [
    ]
systs_ext = [
# #MET 
'MET_SoftTrk_Scale__1up',
'MET_SoftTrk_Scale__1down',
'MET_SoftTrk_ResoPara',
'MET_SoftTrk_ResoPerp',
# #EGAMMA
'EG_RESOLUTION_ALL__1down', 
'EG_RESOLUTION_ALL__1up', 
'EG_SCALE_ALL__1down', 
'EG_SCALE_ALL__1up',

# #MCP
'MUON_CB__1down', 
'MUON_CB__1up',  
'MUON_SAGITTA_RESBIAS__1down', 
'MUON_SAGITTA_RESBIAS__1up', 
'MUON_SAGITTA_DATASTAT__1down', 
'MUON_SAGITTA_DATASTAT__1up', 
'MUON_SCALE__1down', 
'MUON_SCALE__1up', 


#Category reduction
'JET_EffectiveNP_Modelling1__1up',
'JET_EffectiveNP_Modelling2__1up',
'JET_EffectiveNP_Modelling3__1up',
'JET_EffectiveNP_Modelling4__1up',
'JET_EffectiveNP_Mixed1__1up',
'JET_EffectiveNP_Mixed2__1up',
'JET_EffectiveNP_Mixed3__1up',
'JET_EffectiveNP_Detector1__1up',
'JET_EffectiveNP_Detector2__1up',
'JET_EffectiveNP_Statistical1__1up',
'JET_EffectiveNP_Statistical2__1up',
'JET_EffectiveNP_Statistical3__1up',
'JET_EffectiveNP_Statistical4__1up',
'JET_EffectiveNP_Statistical5__1up',
'JET_EffectiveNP_Statistical6__1up',
'JET_Pileup_OffsetMu__1up',
'JET_Pileup_OffsetNPV__1up',
'JET_Pileup_PtTerm__1up',
'JET_Pileup_RhoTopology__1up',
'JET_Flavor_Composition_prop__1up',
'JET_Flavor_Response_prop__1up',
'JET_Flavour_PerJet_Hadronization_HF__1up',
'JET_Flavour_PerJet_Hadronization__1up',
'JET_Flavour_PerJet_GenShower__1up',
'JET_Flavour_PerJet_GenShower_HF__1up',
'JET_Flavour_PerJet_Shower__1up',
'JET_Flavour_PerJet_Shower_HF__1up',
'JET_PunchThrough_MC16__1up',
'JET_SingleParticle_HighPt__1up',
'JET_EtaIntercalibration_Modelling__1up',
'JET_EtaIntercalibration_TotalStat__1up',
'JET_EtaIntercalibration_NonClosure_highE__1up',
'JET_EtaIntercalibration_NonClosure_posEta__1up',
'JET_EtaIntercalibration_NonClosure_negEta__1up',
'JET_EtaIntercalibration_NonClosure_2018data__1up',
'JET_EffectiveNP_Modelling1__1down',
'JET_EffectiveNP_Modelling2__1down',
'JET_EffectiveNP_Modelling3__1down',
'JET_EffectiveNP_Modelling4__1down',
'JET_EffectiveNP_Mixed1__1down',
'JET_EffectiveNP_Mixed2__1down',
'JET_EffectiveNP_Mixed3__1down',
'JET_EffectiveNP_Detector1__1down',
'JET_EffectiveNP_Detector2__1down',
'JET_EffectiveNP_Statistical1__1down',
'JET_EffectiveNP_Statistical2__1down',
'JET_EffectiveNP_Statistical3__1down',
'JET_EffectiveNP_Statistical4__1down',
'JET_EffectiveNP_Statistical5__1down',
'JET_EffectiveNP_Statistical6__1down',
'JET_Pileup_OffsetMu__1down',
'JET_Pileup_OffsetNPV__1down',
'JET_Pileup_PtTerm__1down',
'JET_Pileup_RhoTopology__1down',
'JET_Flavor_Composition_prop__1down',
'JET_Flavor_Response_prop__1down',
'JET_Flavour_PerJet_Hadronization_HF__1down',
'JET_Flavour_PerJet_Hadronization__1down',
'JET_Flavour_PerJet_GenShower__1down',
'JET_Flavour_PerJet_GenShower_HF__1down',
'JET_Flavour_PerJet_Shower__1down',
'JET_Flavour_PerJet_Shower_HF__1down',
'JET_PunchThrough_MC16__1down',
'JET_SingleParticle_HighPt__1down',
'JET_EtaIntercalibration_TotalStat__1down',
'JET_EtaIntercalibration_Modelling__1down',
'JET_EtaIntercalibration_NonClosure_highE__1down',
'JET_EtaIntercalibration_NonClosure_posEta__1down',
'JET_EtaIntercalibration_NonClosure_negEta__1down',
'JET_EtaIntercalibration_NonClosure_2018data__1down',
# JER: small-R jets
'JET_JER_DataVsMC_MC16__1up',
'JET_JER_EffectiveNP_1__1up',
'JET_JER_EffectiveNP_2__1up',
'JET_JER_EffectiveNP_3__1up',
'JET_JER_EffectiveNP_4__1up',
'JET_JER_EffectiveNP_5__1up',
'JET_JER_EffectiveNP_6__1up',
'JET_JER_EffectiveNP_7__1up',
'JET_JER_EffectiveNP_8__1up',
'JET_JER_EffectiveNP_9__1up',
'JET_JER_EffectiveNP_10__1up',
'JET_JER_EffectiveNP_11__1up',
'JET_JER_EffectiveNP_12restTerm__1up',
'JET_JER_DataVsMC_MC16__1down',
'JET_JER_EffectiveNP_1__1down',
'JET_JER_EffectiveNP_2__1down',
'JET_JER_EffectiveNP_3__1down',
'JET_JER_EffectiveNP_4__1down',
'JET_JER_EffectiveNP_5__1down',
'JET_JER_EffectiveNP_6__1down',
'JET_JER_EffectiveNP_7__1down',
'JET_JER_EffectiveNP_8__1down',
'JET_JER_EffectiveNP_9__1down',
'JET_JER_EffectiveNP_10__1down',
'JET_JER_EffectiveNP_11__1down',
'JET_JER_EffectiveNP_12restTerm__1down',
# JES: large-R jet
'JET_EffectiveNP_R10_Modelling1__1up',
'JET_EffectiveNP_R10_Modelling2__1up',
'JET_EffectiveNP_R10_Modelling3__1up',
'JET_EffectiveNP_R10_Modelling4__1up',
'JET_EffectiveNP_R10_Mixed2__1up',
'JET_EffectiveNP_R10_Mixed1__1up',
'JET_EffectiveNP_R10_Mixed3__1up',
'JET_EffectiveNP_R10_Mixed4__1up',
'JET_EffectiveNP_R10_Statistical1__1up',
'JET_EffectiveNP_R10_Statistical2__1up',
'JET_EffectiveNP_R10_Statistical3__1up',
'JET_EffectiveNP_R10_Statistical4__1up',
'JET_EffectiveNP_R10_Statistical5__1up',
'JET_EffectiveNP_R10_Statistical6__1up',
'JET_EffectiveNP_R10_Detector1__1up',
'JET_EffectiveNP_R10_Detector2__1up',
'JET_EtaIntercalibration_R10_TotalStat__1up',
'JET_LargeR_TopologyUncertainty_top__1up',
'JET_LargeR_TopologyUncertainty_V__1up',
'JET_Flavor_Composition__1up',
'JET_Flavor_Response__1up',
'JET_EffectiveNP_R10_Modelling1__1down',
'JET_EffectiveNP_R10_Modelling2__1down',
'JET_EffectiveNP_R10_Modelling3__1down',
'JET_EffectiveNP_R10_Modelling4__1down',
'JET_EffectiveNP_R10_Mixed1__1down',
'JET_EffectiveNP_R10_Mixed2__1down',
'JET_EffectiveNP_R10_Mixed3__1down',
'JET_EffectiveNP_R10_Mixed4__1down',
'JET_EffectiveNP_R10_Statistical1__1down',
'JET_EffectiveNP_R10_Statistical2__1down',
'JET_EffectiveNP_R10_Statistical3__1down',
'JET_EffectiveNP_R10_Statistical4__1down',
'JET_EffectiveNP_R10_Statistical5__1down',
'JET_EffectiveNP_R10_Statistical6__1down',
'JET_EffectiveNP_R10_Detector1__1down',
'JET_EffectiveNP_R10_Detector2__1down',
'JET_EtaIntercalibration_R10_TotalStat__1down',
'JET_LargeR_TopologyUncertainty_top__1down',
'JET_LargeR_TopologyUncertainty_V__1down',
'JET_Flavor_Composition__1down',
'JET_Flavor_Response__1down',
# JER large-R jets
'JET_JER_DataVsMC_R10_MC16__1up',
'JET_JER_dijet_R10_closure__1up',
'JET_JER_dijet_R10_selection__1up',
'JET_JER_dijet_R10_jesEffNP1__1up',
'JET_JER_dijet_R10_jesEffNP3__1up',
'JET_JER_dijet_R10_jesEffNP4__1up',
'JET_JER_dijet_R10_jesEtaIntMod__1up',
'JET_JER_dijet_R10_jesFlavComp__1up',
'JET_JER_dijet_R10_jesFlavResp__1up',
'JET_JER_dijet_R10_mcgenerator__1up',
'JET_JER_dijet_R10_stat__1up',
'JET_JER_AllOthers__1up',
'JET_JER_DataVsMC_R10_MC16__1down',
'JET_JER_dijet_R10_closure__1down',
'JET_JER_dijet_R10_selection__1down',
'JET_JER_dijet_R10_jesEffNP1__1down',
'JET_JER_dijet_R10_jesEffNP3__1down',
'JET_JER_dijet_R10_jesEffNP4__1down',
'JET_JER_dijet_R10_jesEtaIntMod__1down',
'JET_JER_dijet_R10_jesFlavComp__1down',
'JET_JER_dijet_R10_jesFlavResp__1down',
'JET_JER_dijet_R10_mcgenerator__1down',
'JET_JER_dijet_R10_stat__1down',
'JET_JER_AllOthers__1down',
#JMS
'JET_JMS_Rtrk_Stat1__1up',
'JET_JMS_Rtrk_Stat2__1up',
'JET_JMS_Rtrk_Stat3__1up',
'JET_JMS_Rtrk_Stat4__1up',
'JET_JMS_Rtrk_Stat5__1up',
'JET_JMS_Rtrk_Stat6__1up',
'JET_JMS_FF_LargerSample__1up',
'JET_JMS_FF_MatrixElement__1up',
'JET_JMS_FF_PartonShower__1up',
'JET_JMS_FF_Shape__1up',
'JET_JMS_FF_Stat__1up',
'JET_JMS_FF_InterpolationDifference__1up',
'JET_JMS_FF_AllOthers__1up',
'JET_JMS_Rtrk_Tracking__1up',
'JET_JMS_Rtrk_Generator__1up',
'JET_JMS_Rtrk_Generator_InterpolationDifference__1up',
'JET_JMS_Rtrk_InterpolationDifference__1up',
'JET_JMS_Topology_QCD__1up',
'JET_JMS_Rtrk_Stat1__1down',
'JET_JMS_Rtrk_Stat2__1down',
'JET_JMS_Rtrk_Stat3__1down',
'JET_JMS_Rtrk_Stat4__1down',
'JET_JMS_Rtrk_Stat5__1down',
'JET_JMS_Rtrk_Stat6__1down',
'JET_JMS_FF_LargerSample__1down',
'JET_JMS_FF_MatrixElement__1down',
'JET_JMS_FF_PartonShower__1down',
'JET_JMS_FF_Shape__1down',
'JET_JMS_FF_Stat__1down',
'JET_JMS_FF_InterpolationDifference__1down',
'JET_JMS_FF_AllOthers__1down',
'JET_JMS_Rtrk_Tracking__1down',
'JET_JMS_Rtrk_Generator__1down',
'JET_JMS_Rtrk_Generator_InterpolationDifference__1down',
'JET_JMS_Rtrk_InterpolationDifference__1down',
'JET_JMS_Topology_QCD__1down',
#JMR
'COMB_MCData_JMR__1up',
'COMB_MCME_JMR__1up',
'COMB_MCPS_JMR__1up',
'COMB_MCRAD_JMR__1up',
'COMB_MCSmallJET_JMR__1up',
'COMB_MCLargeR_JMR__1up',
'COMB_Stat_JMR__1up',
'COMB_SHAPE_JMR__1up',
'COMB_Smoothing_JMR__1up',
'COMB_Flat20Smoothed_JMR__1up',
'COMB_OutsideCalib_JMR__1up',
'COMB_MCData_JMR__1down',
'COMB_MCME_JMR__1down',
'COMB_MCPS_JMR__1down',
'COMB_MCRAD_JMR__1down',
'COMB_MCSmallJET_JMR__1down',
'COMB_MCLargeR_JMR__1down',
'COMB_Stat_JMR__1down',
'COMB_SHAPE_JMR__1down',
'COMB_Smoothing_JMR__1down',
'COMB_Flat20Smoothed_JMR__1down',
'COMB_OutsideCalib_JMR__1down',
]

def grouped_systs(systs):
    if SPLIT_SYSTEMATICS:
        key = lambda tup: tup.name
    else:
        key = lambda tup: tup.tree
    return [','.join(syst.name for syst in sg.systematics) for sg in systematics.grouped_systs(map(systematics.syst, systs), key=key)]

def max_input(x):
    if 'dijets' in x.sample_name:
        match = re.match(r"dijets_JZ(\d+)W", x.sample_name)
        if match:
            slice_i = int(match.group(1))
            if slice_i < 4:
                return 0
    elif 'data' in x.sample_name:
        return 15
    elif 'tt_mttsliced' in x.sample_name:
        return 20
    elif 'ttnonallhad_mttsliced' in x.sample_name:
        return 20
    return 2

jet_collection = {'AntiKtVR30Rmax4Rmin02TrackJets': 'VRTrackJets',
                  'AntiKt4EMPFlowJets_BTagging201903': 'EMPFlowJets'}

if True:
    runs = {}
    #btaggings = ['AntiKtVR30Rmax4Rmin02TrackJets.DL1r_FixedCutBEff77']
    btaggings = ['AntiKt4EMPFlowJets_BTagging201903.DL1r_FixedCutBEff77']
    for btagging in btaggings:
        for l in ('e', 'mu'):
            runs.setdefault(btagging.split('.')[1]+'_DNNincl80', []).append(dict(aux_selector = TRACKJET_CLEANING, topo='b',lepton=l,b_category ='',top_tagger='isTagged_JSSWTopTaggerDNN_DNNTaggerTopQuarkInclusive80*angular_cuts', bot_tagger = btagging,fname = '{channel}_{s.sample_name}_{s.tag}_'+btagging.split('.')[1]+'_DNNincl80.root'))  #angular_cuts
            runs.setdefault(btagging.split('.')[1]+'_DNNincl80', []).append(dict(aux_selector = TRACKJET_CLEANING, topo='r',lepton=l,b_category ='',top_tagger='isTagged_JSSWTopTaggerDNN_DNNTaggerTopQuarkInclusive80*angular_cuts', bot_tagger = btagging,fname = '{channel}_{s.sample_name}_{s.tag}_'+btagging.split('.')[1]+'_DNNincl80.root'))
    for _r in runs.values():
        _r.sort()

    def main(samples, systematics, analysis_exts=['--do-tree', '--noMttSlices', '--ttbar-high-order', 'NNLOQCDNLOEWK'], **run_kwds):
        sels = []
        i = run_kwds.pop('i',None)
        if i == None:
            for v in runs.values():
              for vv in v:
                sels.append(vv)
        else:
            for k in runs:
                if re.match(i, k):
                    for vv in runs[k]:
                        sels.append(vv)
        for c in campaign:
            print ("c['periodFraction']: = ", c['periodFraction'])

        r = run.Run(samples = samples, **run_kwds)
        for sample in r.samples:
            if 'dijets' in sample.sample_name:
                #print 'For dijets sample, we don\'t need their ljet uncertainties'
                sample.systematics = grouped_systs(systs_nom+systs_ext)
                # sample.systematics = 'nominal'
            elif ('af2' in sample.sample_name) or ('tt_hs' in sample.sample_name) or ('tt_had' in sample.sample_name) or ('tt_hdamp' in sample.sample_name) or ('tt_meoff' in sample.sample_name):
              sample.systematics = grouped_systs(systs_nom)
            elif 'tt' in sample.sample_name and TTGENSYST:
              sample.systematics = grouped_systs(syst_ttgen)
            elif 'tt' in sample.sample_name:
              # sample.systematics = grouped_systs(systs_nom+systs_ext+systs_ttbar)
              sample.systematics = grouped_systs(systs_ttbar)
            else:
                sample.systematics = grouped_systs(systs_nom+systs_ext)
            print (sample.systematics)
        # only channels be, bmu, re, rmu 2015+2016
        r.selections = []
        for sel in sels:
            r.add_selection(**sel)
        # comment it out if you don't want a mini-tree output
        r.analysis_exts = analysis_exts#['--do-tree', '--noMttSlices', '--ttbar-high-order', 'NNLOQCDNLOEWK']#[:2]
        # outDS suffix. Only matters if you use 'grid' as cluster
        #r.tag = 'histTNA_22-02-2021_T'+str(i)+'v1'
        #r.tag = 'histTNA_21.2.155_syst_'+jet_collection[btagging.split('.')[0]]
        r.tag = 'v4'
        r.system = 'naf'
        if r.cluster != None:
            setattr(r.cluster, 'max_runtime', 3600*2)
            r.cluster.isFirst = not bool(i)
        r.run(use_cluster = USE_CLUSTER,
              monitor = False,  #Usually I use Flase 
              # rerun_strategy = 'none', # avalible: ['merge', 'force', 'none']
              delete_sources_after_merged = True,  # Elham changed to False (June 2021)
              # execute_kwds = {'compress_outputs': True, 'submit_kwds': {'argument': ['--site', 'DESY-HH,AUTO', '--destSE', 'DESY-HH_SCRATCHDISK']}},
            #   execute_kwds = {'compress_outputs': True, 'submit_kwds': {'argument': ['--qos', 'shared', '-C', 'cpu', '--account', 'atlas', '--image', 'zlmarshall/atlas-grid-centos7:20230424']}},
            #   execute_kwds = {'compress_outputs': True, 'submit_kwds': {'argument': ['--qos', 'shared', '-C', 'haswell', '--account', 'atlas', '--image', 'zlmarshall/atlas-grid-centos7:20230424']}},
              finalize_kwds = {'num_of_workers': 8, 'skip_merge_when_fail': True, 'hadd_ext_options': ['-n',str(args.max_files_open_hadd)]}#, 'hadd_ext_options': ['-n','100']}#, 'do_merge':False}
              # This is to control `Run.execute` and can be also used to control batch submission,
              # like site name where jobs are sent in grid for example. Comment it out to use it.
              )
        return r
    c = clusters.from_name.get('condor')(cluster_type = None, cluster_status_update=(600,30), cluster_queue='None')

    for i in runs:#range(len(runs)):
        print (i, runs)
        #print grouped_systs
        if 'NoTopTagging' in i:
            analysis_exts = ['--do-tree', '--noMttSlices', '--ttbar-high-order', CORRECTION]
        elif TTGENSYST:
            analysis_exts = ['--do-tree', '--noMttSlices', '--ttbar-high-order', CORRECTION, '--pdf ttgen'] #'--do-tree','--nevents', 1000,
        else:
            analysis_exts = ['--do-tree', '--noMttSlices', '--ttbar-high-order', CORRECTION] # , '--pdf ttgen' '--do-tree','--nevents', 1000,
            #if not BLINDING:
            #    analysis_exts.insert(0, '--do-tree')
        if BLINDING:
            analysis_exts.append('--blinding')
        r = main(samples = s,
             systematics = grouped_systs,
            #  log_dir=
             output_dir = '{}{}_{}'.format(outpath,i,runMCData[0]),
             analysis_type = 'AnaTtresSL',
             analysis_exts=analysis_exts,
             i = i,
             max_inputs_per_job = MAX_INPUTS_PER_JOB,
             cluster = 'condor') # known to work: 'condor', 'lsf' and 'grid'
    r.wait()


    