#!/usr/bin/env python2.7
import os
import sys
import glob
import re
import tempfile
import subprocess
try:
    import HQTTtResonancesTools.DC15Data13TeV_25ns_207_EXOT4
    import HQTTtResonancesTools.MC16a_EXOT4
except ImportError:
    raise ImportError("HQTTtResonancesTools is not installed or dataset does not exist.")
import rucio.client
import TopExamples.grid

DS_PATTERN = '{s.ds_scope}.{s.DSID}.*{suffix}'
DS_SCOPE = 'user.yuchen'


MAP_TO_SAMPLES = {# <sample>: <physics_short>
                'wbbjets': 'MC16_13TeV_25ns_FS_EXOT4_Wjets22',
                'wccjets': 'MC16_13TeV_25ns_FS_EXOT4_Wjets22',
                'wcjets': 'MC16_13TeV_25ns_FS_EXOT4_Wjets22',
                'wljets': 'MC16_13TeV_25ns_FS_EXOT4_Wjets22',
                'data': 'Data15_13TeV_25ns_207_EXOT4,Data16_13TeV_25ns_207_EXOT4',
                'qcde': 'Data15_13TeV_25ns_207_EXOT4,Data16_13TeV_25ns_207_EXOT4',
                'qcdmu': 'Data15_13TeV_25ns_207_EXOT4,Data16_13TeV_25ns_207_EXOT4',
                'tt':'MC16_13TeV_25ns_FS_EXOT4_ttbarPowhegPythia,MC16_13TeV_25ns_FS_EXOT4_ttbarPowhegPythia_mttsliced',
                'singletop':'MC16_13TeV_25ns_FS_EXOT4_singletop',
                'zjets':'MC16_13TeV_25ns_FS_EXOT4_Zjets22',
                'vv': 'MC16_13TeV_25ns_FS_EXOT4_VV',
                'zprime400': 'MC16_13TeV_25ns_FS_EXOT4_Zprime400',
                'zprime500': 'MC16_13TeV_25ns_FS_EXOT4_Zprime500',
                'zprime750': 'MC16_13TeV_25ns_FS_EXOT4_Zprime750',
                'zprime1000': 'MC16_13TeV_25ns_FS_EXOT4_Zprime1000',
                'zprime1250': 'MC16_13TeV_25ns_FS_EXOT4_Zprime1250',
                'zprime1500': 'MC16_13TeV_25ns_FS_EXOT4_Zprime1500',
                'zprime1750': 'MC16_13TeV_25ns_FS_EXOT4_Zprime1750',
                'zprime2000': 'MC16_13TeV_25ns_FS_EXOT4_Zprime2000',
                'zprime2250': 'MC16_13TeV_25ns_FS_EXOT4_Zprime2250',
                'zprime2500': 'MC16_13TeV_25ns_FS_EXOT4_Zprime2500',
                'zprime2750': 'MC16_13TeV_25ns_FS_EXOT4_Zprime2750',
                'zprime3000': 'MC16_13TeV_25ns_FS_EXOT4_Zprime3000',
                'zprime4000': 'MC16_13TeV_25ns_FS_EXOT4_Zprime4000',
                'zprime5000': 'MC16_13TeV_25ns_FS_EXOT4_Zprime5000',
                'kkgrav400': 'MC16_13TeV_25ns_FS_EXOT4_Gtt400',
                'kkgrav500': 'MC16_13TeV_25ns_FS_EXOT4_Gtt500',
                'kkgrav750': 'MC16_13TeV_25ns_FS_EXOT4_Gtt750',
                'kkgrav1000': 'MC16_13TeV_25ns_FS_EXOT4_Gtt1000',
                'kkgrav2000': 'MC16_13TeV_25ns_FS_EXOT4_Gtt2000',
                'kkgrav3000': 'MC16_13TeV_25ns_FS_EXOT4_Gtt3000'
                }

class Sample(object):
    _client = rucio.client.Client()
    @staticmethod
    def parse_dataset(obj):
        sample = TopExamples.grid.Sample("")
        if isinstance(obj, TopExamples.grid.Sample):
            for dataset_name, physics_short in MAP_TO_SAMPLES.iteritems():
                if set(physics_short.split(',')).issubset(obj.datasets):
                    sample.name = dataset_name
                    sample.datasets.extend(obj.datasets)
                    return sample
        else:
            for dataset_name, physics_short in MAP_TO_SAMPLES.iteritems():
                if obj == dataset_name:
                    sample.name = dataset_name
                    sample.datasets.extend(TopExamples.grid.Samples(physics_short.split(','))[0].datasets)
                    return sample
        raise KeyError()

    def __init__(self, sample_name = 'zprime1000', input_files = None, ds_scope = DS_SCOPE, ds_pattern = DS_PATTERN, ds_fmt_options = {'suffix': '13112016v2_output.root'}):
        self.ds_scope = ds_scope.format(**ds_fmt_options)
        self.sample_name = sample_name
        self.sample = self.parse_dataset(sample_name)
        self.ds_pattern = ds_pattern.format(s = self, **ds_fmt_options)
        self.set_input_files(input_files)
    def _list_dids(self, scope = None, filters = {}):
        scope = scope or self.ds_scope
        filters = dict({'name': self.ds_pattern}, **filters)
        return list(self._client.list_dids(scope = scope, filters = filters))
    @property
    def physics_short(self):
        return self.sample.name
    @property
    def shortNameDatasets(self):
        return self.sample.shortNameDatasets()[0]
    @property
    def ami_tag(self):
        return self.shortNameDatasets.split('.')[1]
    @property
    def DSID(self):
        return self.shortNameDatasets.split('.')[0]
    @property
    def datasets(self):
        return self.sample.datasets
    @property
    def systematics(self):
        for name in ["data", "qcde", "qcdmu"]:
            if name in self.sample_name:
                return "nominal"
        return "all"
    @property
    def is_data(self):
        if "data" in self.sample_name:
            return " -d "
        if "qcde" in self.sample_name:
            return " -d -Q e "
        if "qcdmu" in self.sample_name:
            return " -d -Q mu "
        return ""
    @property
    def extra(self):
        if "wbbjets" in self.sample_name:
            return ' --WjetsHF bb '
        elif 'wccjets' in self.sample_name:
            return ' --WjetsHF cc'
        elif 'wcjets' in self.sample_name:
            return ' --WjetsHF c'
        elif 'wljets' in self.sample_name:
            return ' --WjetsHF l'
        return ''
    def get_input_files(self):
        return self._input_files
    def set_input_files(self, alist = None):
        if alist == None and not self._input_files:
            self._input_files = [replica['pfns'].keys() for replica in self._client.list_replicas([{'scope': self.ds_scope, 'name': dids} for dids in self._list_dids()], schemes = ['root'])]
        else:
            self._input_files = alist
    input_files = property(get_input_files, set_input_files)


class Run(object):
    def __init__(self, samples = ['zprime1000'], output_dir = None, analysis_type = 'AnaTtresSL'):
        self.samples = [Sample(s) if isinstance(s, str) else s for s in samples]
        self.run_dir = os.path.abspath(os.path.dirname(__file__))
        self.output_dir = os.path.abspath(output_dir or os.path.join(self.run_dir, os.path.pardir, 'data', 'output'))
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        self.selections = ['be', 'bmu', 're', 'rmu', 'be2015', 'bmu2015', 're2015', 'rmu2015', 'be2016', 'bmu2016', 're2016', 'rmu2016']
        self.analysis_type = analysis_type
    def write_runfile(self, sample, runfile = "/dev/stdout", selections = None):
        selections = selections or self.selections
        job_name = sample.sample_name
        with open(os.path.join(self.output_dir, "input_"+sample.sample_name+'.txt'), 'w') as infile:
            infile.writelines((f + '\n' for f in sample.input_files))
        with open(runfile, 'w') as fr:
            fr.write('#!/bin/sh\n')
            fr.write('#cd ' + self.run_dir + '\n')
            fr.write('#export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase\n')
            fr.write('#export DQ2_LOCAL_SITE_ID=DESY-HH_SCRATCHDISK \n')
            fr.write('#source /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/user/atlasLocalSetup.sh\n')
            fr.write('export X509_USER_PROXY=$HOME/.globus/job_proxy.pem\n')
            fr.write('#lsetup rcsetup\n')
            fr.write('#cd TopNtupleAnalysis/pyHistograms\n')
            output_files = ','.join(['{selection}:file://{output_file}'.format(selection = selection,
                                                               output_file = os.path.join(self.output_dir, '{}_{}.root'.format(selection, job_name)))
                            for selection in selections])
            fr.write(os.path.join(self.run_dir,'makeHistograms.py')
                     + sample.is_data
                     + sample.extra
                     + '  --files '    + infile.name
                     + ' --analysis '  + self.analysis_type
                     + ' --output '    + output_files
                     + '   --systs '   + sample.systematics)
    def execute(self, runfile_dir = os.path.join(tempfile.gettempdir())):
        for sample in self.samples:
            # logfile = os.path.join(self.output_dir, "stdout_"+sample.sample_name+'.txt')
            runfile = os.path.join(runfile_dir, sample.sample_name+'.sh')
            self.write_runfile(sample = sample, runfile = runfile)
            subprocess.call(['chmod', 'a+x', runfile])
            subprocess.call([runfile])

def main(samples = ['zprime1000'], output_dir = None, analysis_type = 'AnaTtresSL'):
    # for QCD e
    # pattern_qcde = 'user.dferreir.*24062016QCDev1_output.root'
    # pattern_qcdmu = 'user.dferreir.*24062016QCDmuv1_output.root'
    # output directory
    #output_dir = '/afs/desy.de/user/d/danilo/xxl/af-atlas/Top2412/TopNtupleAnalysis/pyHistograms/hists_sr_nosyst'

    # the default is AnaTtresSL, which produces many control pltos for tt res.
    # The Mtt version produces a TTree to do the limit setting
    # the QCD version aims at plots for QCD studies using the matrix method
    # look into read.cxx to see what is available
    # create yours, if you wish
    #analysis_type='AnaWjetsCR'
    Run(samples = samples, output_dir = output_dir, analysis_type = analysis_type).execute()
    
if __name__ == '__main__':
    # import os
    # fr = open("get_proxy.sh", "w")
    # fr.write("export X509_USER_PROXY=$HOME/.globus/job_proxy.pem\n")
    # fr.write("voms-proxy-init --voms atlas --vomslife 96:00 --valid 96:00\n")
    # fr.close()
    # os.system("chmod a+x get_proxy.sh")
    # os.system("./get_proxy.sh")
    main()


