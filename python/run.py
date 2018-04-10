#!/usr/bin/env python2.7
import os
import sys
import re
import subprocess

import helpers
import clusters
import samples

class Run(object):
    def __init__(self, samples = [], output_dir = None, log_dir = None, analysis_type = 'AnaTtresSL', cluster = None):
        self.samples = [samples.Sample(s) if isinstance(s, str) else s for s in samples]
        self.source_dir = os.path.abspath(os.path.dirname(__file__))
        self.output_dir = os.path.abspath(output_dir or os.path.join(os.curdir, 'output'))
        self.log_dir = os.path.abspath(log_dir or os.path.join(os.curdir, 'log'))
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        self.selections = [('(be,     good_smooth_ts80)', '{channel}_{sample}.root'),
                           ('(bmu,    good_smooth_ts80)', '{channel}_{sample}.root'),
                           ('(re,     good_smooth_ts80)', '{channel}_{sample}.root'),
                           ('(rmu,    good_smooth_ts80)', '{channel}_{sample}.root'),
                           ('(be2015, good_smooth_ts80)', '{channel}_{sample}.root'),
                           ('(bmu2015,good_smooth_ts80)', '{channel}_{sample}.root'),
                           ('(re2015, good_smooth_ts80)', '{channel}_{sample}.root'),
                           ('(rmu2015,good_smooth_ts80)', '{channel}_{sample}.root'),
                           ('(be2016, good_smooth_ts80)', '{channel}_{sample}.root'),
                           ('(bmu2016,good_smooth_ts80)', '{channel}_{sample}.root'),
                           ('(re2016, good_smooth_ts80)', '{channel}_{sample}.root'),
                           ('(rmu2016,good_smooth_ts80)', '{channel}_{sample}.root')]
        self.analysis_type = analysis_type
        self.analysis_exts = []
        self.cluster = clusters.from_name.get(cluster)(cluster_type = None, cluster_status_update=(600,30)) if isinstance(cluster, str) else cluster

    def write_runfile(self, sample, runfile = sys.stdout, selections = None, output_fname_fmt = None):
        selections = selections or self.selections
        job_name = sample.sample_name
        download_cmd = ''.join(sample.commit(only_retrieve_cmd = bool(sample.download_to)) or [])
        with open(os.path.join(self.output_dir, "input_"+sample.sample_name+'.txt'), 'w') as infile:
            infile.writelines('\n'.join(sample.input_files))
        with open(runfile, 'w') as fr:
            fr.write('#!/bin/sh\n')
            if self.cluster != None:
                fr.write('pwd="$PWD"\n')
                fr.write('source /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/user/atlasLocalSetup.sh\n')
                fr.write('export X509_USER_PROXY=$HOME/.globus/job_proxy.pem\n')
                fr.write('cd {}\n'.format(os.path.join(os.getenv("WorkDir_DIR"), '..')))
                fr.write('asetup --restore && source */setup.sh\n')
                fr.write('cd {}\n'.format("$pwd"))
                fr.write('lsetup -f pyami rucio\n')
            if download_cmd:
                fr.write(''.join(download_cmd))
            output_files = ' '.join(['-o "{selection}:file://{output_file}"'.format(selection = selection,
                                                                                    output_file = os.path.join(self.output_dir, output_fname.format(channel = re.search('\((\S+)\s*,', selection).group(1), sample = job_name)))
                                     for selection, output_fname in (selections.iteritems() if isinstance(selections, dict) else selections)])
            fr.write(os.path.join(self.source_dir,'makeHistograms.py')
                     + sample.is_data
                     + sample.extra
                     + '  --files '    + infile.name
                     + ' --analysis '  + self.analysis_type
                     + ' '             + output_files
                     + '   --systs '   + sample.systematics
                     + ' ' + ' '.join(self.analysis_exts))

    def execute(self, runfile_dir = os.curdir, use_cluster = True):
        runfile_dir = os.path.abspath(runfile_dir)
        for sample in self.samples:
            runfile = os.path.join(runfile_dir, sample.sample_name+'.submit')
            self.write_runfile(sample = sample, runfile = runfile)
            subprocess.call(['chmod', 'u+x', runfile])
            if not use_cluster or self.cluster == None:
                subprocess.call([runfile])
            else:
                self.cluster.submit2(runfile,
                                     stdout = os.path.join(self.log_dir, 'out.$(Cluster).$(Process)'),
                                     stderr = os.path.join(self.log_dir, 'out.$(Cluster).$(Process)'),
                                     log = os.path.join(self.log_dir, 'log.$(Cluster).$(Process)'))

    def wait(self):
        if self.cluster != None:
            self.cluster.wait(None, fct = get_fct(logger = helpers.getLogger('TopNtupleAnalysis.cluster')))

    def run(self, runfile_dir = os.curdir, use_cluster = True, monitor = True):
        self.execute(runfile_dir = runfile_dir, use_cluster = use_cluster)
        if monitor:
            self.wait()

def get_fct(logger = None):
    if logger == None:
        def fct(idle, run, finish):
            l = "Idle: {:3},  Running: {:3},  Completed: {:3}".format(idle, run, finish)
            print l
    else:
        def fct(idle, run, finish):
            l = "Idle: {:3},  Running: {:3},  Completed: {:3}".format(idle, run, finish)
            logger.info(l)
    return fct

if __name__ == '__main__':
    """
    An example of histogramming signal sample w/ M(Z')=[400, ... , 5000]GeV in l+jets analysis using batch system `HTCondor`
    """
    s = [samples.Sample(sample_name = 'zprime1000',
                        ds_fmt_options = {'suffix': '13022018v1_output.root'},
                        download_to = None)]

    def main(samples, systematics, **run_kwds):
        run = Run(samples = samples, **run_kwds)
        for sample in run.samples:
            sample.systematics = systematics
        run.selections = run.selections[:4] # only channels be, bmu, re, rmu 2015+2016
        run.analysis_exts = ['--do-tree'] # comment it out if you don't want a mini-tree output
        run.run(use_cluster = True, monitor = True)

    main(samples = s,
         systematics = 'nominal',
         output_dir = None,
         analysis_type = 'AnaTtresSL',
         cluster = None) 
