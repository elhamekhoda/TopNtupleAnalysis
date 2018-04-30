#!/usr/bin/env python2.7
import os
import sys
import re
import glob
import subprocess

import helpers
import clusters
import samples

logger = helpers.getLogger('TopNtupleAnalysis.run')

class Run(object):
    def __init__(self, samples = [], output_dir = None, log_dir = None, analysis_type = 'AnaTtresSL', cluster = None, max_inputs_per_job = 5, environment = 'asetup'):
        self.samples = [samples.Sample(s) if isinstance(s, str) else s for s in samples]
        self.source_dir = os.path.abspath(os.path.dirname(__file__))
        self.output_dir = os.path.abspath(output_dir or os.path.join(os.curdir, 'output'))
        self.log_dir = os.path.abspath(log_dir or os.path.join(os.curdir, 'log'))
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        self.selections = [('(be,     good)', '{channel}_{sample}.root'),
                           ('(bmu,    good)', '{channel}_{sample}.root'),
                           ('(re,     good)', '{channel}_{sample}.root'),
                           ('(rmu,    good)', '{channel}_{sample}.root'),
                           ('(be2015, good)', '{channel}_{sample}.root'),
                           ('(bmu2015,good)', '{channel}_{sample}.root'),
                           ('(re2015, good)', '{channel}_{sample}.root'),
                           ('(rmu2015,good)', '{channel}_{sample}.root'),
                           ('(be2016, good)', '{channel}_{sample}.root'),
                           ('(bmu2016,good)', '{channel}_{sample}.root'),
                           ('(re2016, good)', '{channel}_{sample}.root'),
                           ('(rmu2016,good)', '{channel}_{sample}.root')]
        self.analysis_type = analysis_type
        self.analysis_exts = []
        self.max_inputs_per_job = max_inputs_per_job
        self.cluster = clusters.from_name.get(cluster)(cluster_type = None, cluster_status_update=(600,30), cluster_queue='None') if isinstance(cluster, str) else cluster
        self.environment = environment


    def write_inputsfile(self, sample):
        with open(os.path.join(self.output_dir, "input_"+sample.sample_name+'.txt'), 'w') as infile:
            infile.writelines('\n'.join(sample.input_files))
        return infile.name
    
    def command_lines(self, sample, selections = None, output_fname_fmt = None):
        cmds = {'shebang': [], 'build': [], 'download': [], 'pre-exec': [], 'exec': [], 'post-exec': []}
        selections = selections or self.selections
        job_name = sample.sample_name
        download_cmd = ''.join(sample.commit(only_retrieve_cmd = bool(sample.download_to)) or [])
        infile = self.write_inputsfile(sample)
        cmds['shebang'].append('#!{}\n'.format(os.environ['SHELL']))
        if self.cluster != None:
            cmds['build'].append('pwd="$PWD"\n')
            cmds['build'].append('source /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/user/atlasLocalSetup.sh\n')
            cmds['build'].append('export X509_USER_PROXY=$HOME/.globus/job_proxy.pem\n')
            cmds['build'].append('cd {}\n'.format(os.path.join(os.getenv("WorkDir_DIR"), '..')))
            if self.cluster.name == 'lsf': 
                # this is needed because the default python version for LSF in lxplus is way too old.
                #This leads to problems building athena
                cmds['build'].append('lsetup python\n')
            if self.environment == 'acmSetup':
                cmds['build'].append('acmSetup\n')
            elif self.environment == 'asetup':
                cmds['build'].append('asetup --restore && . */setup.sh && . */env_setup.sh\n')
                cmds['build'].append('lsetup git\n')
            cmds['build'].append('export LD_LIBRARY_PATH=$WorkDir_DIR/lib:$LD_LIBRARY_PATH\n')
            cmds['build'].append('cd {}\n'.format("$pwd"))
        if download_cmd:
            cmds['download'].append('lsetup pyami rucio\n')
            cmds['download'].append(''.join(download_cmd))
        output_files = ' \\\n'.join(['-o "{selection}:file://{output_file}"'.format(selection = selection,
                                                                                    output_file = os.path.join(self.output_dir, output_fname.format(channel = re.search('\((\S+)\s*,', selection).group(1), sample = job_name)))
                                     for selection, output_fname in (selections.iteritems() if isinstance(selections, dict) else selections)])
        cmds['exec'].append(os.path.join(self.source_dir,'makeHistograms.py') + ' \\\n'
                            + '--analysis ' + self.analysis_type  + sample.is_data + sample.extra + ' --systs '  + sample.systematics + ' ' + ' '.join(self.analysis_exts) + ' \\\n'
                            + '--files '    + infile + ' \\\n'
                            + output_files)
        return cmds

    def write_runfile(self, sample, runfile = sys.stdout, selections = None, output_fname_fmt = None, stages = ('shebang', 'build', 'download', 'pre-exec', 'exec', 'post-exec')):
        command_lines = self.command_lines(sample, selections = selections, output_fname_fmt = output_fname_fmt)
        lines = []
        for stage in stages:
            lines.extend(command_lines[stage])
            if stage in ('exec',):
                logger.debug('Executing:\n%s', ''.join(command_lines[stage]))
        with open(runfile, 'w') as fr:
            fr.writelines(lines)

    def execute(self, runfile_dir = os.curdir, use_cluster = True, stages = ('shebang', 'build', 'download', 'pre-exec', 'exec', 'post-exec')):
        if self.cluster == None:
            use_cluster = False
        runfile_dir = os.path.abspath(runfile_dir)
        for sample in self.samples:
            subsamples = samples.part_sample(sample, max_input_files = self.max_inputs_per_job)
            for s in subsamples:
                runfile = os.path.join(runfile_dir, s.sample_name+'.submit')
                self.write_runfile(sample = s, runfile = runfile, stages = stages)
                subprocess.call(['chmod', 'u+x', runfile])
                if not use_cluster:
                    subprocess.call([runfile])
                else:
                    job_id = self.cluster.get_identifier()
                    self.cluster.submit2(runfile,
                                         stdout = os.path.join(self.log_dir, 'out.%s' % job_id),
                                         stderr = os.path.join(self.log_dir, 'out.%s' % job_id),
                                         log    = os.path.join(self.log_dir, 'log.%s' % job_id))

    def finalize(self):
        helpers.merge_files(glob.iglob(os.path.join(self.output_dir, '*.root*')), delete_sources = True)

    def wait(self):
        if self.cluster != None:
            self.cluster.wait(None, fct = get_fct(logger = helpers.getLogger('TopNtupleAnalysis.cluster')))

    def run(self, runfile_dir = os.curdir, use_cluster = True, monitor = True):
        self.execute(runfile_dir = runfile_dir, use_cluster = use_cluster)
        if use_cluster and monitor:
            self.wait()
        self.finalize()

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
    An example of histogramming signal sample w/ M(Z')=[400, ... , 5000]GeV in l+jets analysis `locally`
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
         max_inputs_per_job = None,
         cluster = None) 
