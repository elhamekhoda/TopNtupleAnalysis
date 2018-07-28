#!/usr/bin/env python2.7
import os
import sys
import re
import copy
import datetime
import subprocess

import helpers
import clusters
import samples

logger = helpers.getLogger('TopNtupleAnalysis.run')

__grid__ = False

class Run(object):
    def __init__(self, samples = [], output_dir = None, log_dir = None, analysis_type = 'AnaTtresSL', cluster = None, max_inputs_per_job = 5, environment = 'asetup'):
        self.samples = [samples.Sample(s) if isinstance(s, str) else s for s in samples]
        self.source_dir = os.path.abspath(os.path.dirname(__file__))
        self.output_dir = os.path.abspath(output_dir or os.path.join(os.curdir, 'output'))
        self.log_dir = os.path.abspath(log_dir or os.path.join(self.output_dir, 'log'))
        self.runfile_dir = self.output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        self.selections = [('(be,     good, MV2c10_70)', '{channel}_{s.sample_name}{s.tag}.root'),
                           ('(bmu,    good, MV2c10_70)', '{channel}_{s.sample_name}{s.tag}.root'),
                           ('(re,     good, MV2c10_70)', '{channel}_{s.sample_name}{s.tag}.root'),
                           ('(rmu,    good, MV2c10_70)', '{channel}_{s.sample_name}{s.tag}.root'),
                           ('(be2015, good, MV2c10_70)', '{channel}_{s.sample_name}{s.tag}.root'),
                           ('(bmu2015,good, MV2c10_70)', '{channel}_{s.sample_name}{s.tag}.root'),
                           ('(re2015, good, MV2c10_70)', '{channel}_{s.sample_name}{s.tag}.root'),
                           ('(rmu2015,good, MV2c10_70)', '{channel}_{s.sample_name}{s.tag}.root'),
                           ('(be2016, good, MV2c10_70)', '{channel}_{s.sample_name}{s.tag}.root'),
                           ('(bmu2016,good, MV2c10_70)', '{channel}_{s.sample_name}{s.tag}.root'),
                           ('(re2016, good, MV2c10_70)', '{channel}_{s.sample_name}{s.tag}.root'),
                           ('(rmu2016,good, MV2c10_70)', '{channel}_{s.sample_name}{s.tag}.root')]
        self.analysis_type = analysis_type
        self.analysis_exts = []
        self.max_inputs_per_job = max_inputs_per_job
        self.cluster = clusters.from_name.get(cluster)(cluster_type = None, cluster_status_update=(600,30), cluster_queue='None') if isinstance(cluster, str) else cluster
        self.environment = environment
        self.system = 'lxplus'
        self.do_merge = True
        self._tag_fmt = 'histTNA_{date}{series}'

    def add_selection(self, topo, lepton, period = '', b_category = '', top_tagger = 'good', bot_tagger = 'MV2c10_70', fname = '{channel}_{s.sample_name}{s.tag}.root'):
        self.selections.append(('({}{}{}{}, {}, {})'.format(topo, lepton, period, b_category, top_tagger, bot_tagger), fname))

    @property
    def tag(self):
        return self._tag_fmt.format(date = format(datetime.date.today(), '%Y%m%d'), series = 'v0')
    @tag.setter
    def tag(self, value):
        self._tag_fmt = value
    def write_inputsfile(self, sample):
        infile_fname = "input_"+sample.sample_name+(sample.tag and '_'+sample.tag)+'.txt'
        if not __grid__:
            infile_fname = os.path.join(self.output_dir, infile_fname)
            with open(infile_fname, 'w') as infile:
                infile.writelines('\n'.join(sample.input_files))
        return infile_fname
    
    def command_lines(self, sample, output_files, infile = None):
        cmds = {'shebang': [], 'build': [], 'download': [], 'pre-exec': [], 'exec': [], 'post-exec': []}
        download_cmd = ''.join(sample.commit(only_retrieve_cmd = bool(sample.download_to)) or [])
        infile = infile or self.write_inputsfile(sample)
        cmds['shebang'].append('#!{}\n'.format(os.environ['SHELL']))
        if self.cluster != None:
            cmds['build'].append('pwd="$PWD"\n')
            cmds['build'].append('source /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/user/atlasLocalSetup.sh\n')
            cmds['build'].append('export X509_USER_PROXY=$HOME/.globus/job_proxy.pem\n')
            cmds['build'].append('cd {}\n'.format(os.path.join(os.getenv("WorkDir_DIR"), '..')))
            if self.cluster.name == 'lsf': 
                # This is needed because the default python version for LSF in lxplus is way too old.
                # , which leads to problems building athena
                cmds['build'].append('lsetup python\n')
            if self.environment == 'acmSetup':
                cmds['build'].append('acmSetup\n')
            elif self.environment == 'asetup':
                cmds['build'].append('asetup --restore && . */setup.sh && . */env_setup.sh\n')
                cmds['build'].append('lsetup git\n')
            cmds['build'].append('export LD_LIBRARY_PATH=$WorkDir_DIR/lib:$LD_LIBRARY_PATH\n')
            cmds['build'].append('cd {}\n'.format("$pwd"))
            if download_cmd:
                cmds['build'].append('lsetup pyami rucio{}\n'.format(' -f' if self.system == 'naf' else ''))
        if download_cmd:
            cmds['download'].append(''.join(download_cmd))
        cmds['exec'].append(('python $WorkDir_DIR/python/TopNtupleAnalysis/makeHistograms.py' if os.getenv('AtlasProject') and self.cluster != None else os.path.join(self.source_dir,'makeHistograms.py'))  + ' \\\n'
                            + '--analysis ' + self.analysis_type  + sample.is_data + sample.extra + ' --systs '  + sample.systematics + ' ' + ' '.join(self.analysis_exts) + ' \\\n'
                            + '--files '    + infile + ' \\\n'
                            + ' \\\n'.join(['-o "{selection}:{output_file}"'.format(selection = selection, output_file = output_file) for selection, output_file in output_files]) + '\n')
        return cmds

    def write_runfile(self, sample , output_files,
                      infile = None,
                      runfile = sys.stdout,
                      stages = ('shebang', 'build', 'download', 'pre-exec', 'exec', 'post-exec'),
                      check_exitcode = ('build', 'download', 'pre-exec', 'exec', 'post-exec')):
        infile = infile or self.write_inputsfile(sample)
        command_lines = self.command_lines(sample, output_files = output_files, infile = infile)
        checker = ['if [ $? -ne 0 ]; then\n', 'exit $?\n', 'fi\n']
        lines = []
        for stage in stages:
            for l in command_lines[stage]:
                lines.append(l)
                if check_exitcode == True or stage in check_exitcode:
                    lines.extend(checker)
            if stage in ('exec',):
                logger.debug('Executing:\n%s', ''.join(command_lines[stage]).strip())
        with open(runfile, 'w') as fr:
            fr.writelines(lines)

    def execute(self, runfile_dir = None,
                use_cluster = True,
                stages = ('shebang', 'build', 'download', 'pre-exec', 'exec', 'post-exec'),
                rerun_strategy = 'merge',
                submit_kwds = {},
                max_inputs_per_job = None,
                **write_kwds):
        max_inputs_per_job = max_inputs_per_job if max_inputs_per_job != None else self.max_inputs_per_job
        if self.cluster == None:
            use_cluster = False
        runfile_dir = os.path.abspath(runfile_dir or self.runfile_dir)
        selections = self.selections.iteritems() if isinstance(self.selections, dict) else self.selections
        self.outstreams = {}
        for sample in self.samples:
            subsamples = samples.part_sample(sample, max_input_files = max_inputs_per_job)
            outstream = self.outstreams[sample.sample_name] = {}
            for selection, output_fname in selections:
                outstream[selection] = {}
                channel = re.search('\((\S+)\s*,', selection).group(1)
                outstream[selection]['output'] = os.path.join(self.output_dir, output_fname.format(channel = channel, s = sample, sample = sample.sample_name))
                outstream[selection]['sub_outputs'] = [os.path.join(self.output_dir, output_fname.format(channel = channel, s = s, sample = s.sample_name)) for s in subsamples]
            for i, s in enumerate(subsamples):
                jobs = []
                for selection in outstream:
                    sub_output = outstream[selection]['sub_outputs'][i]
                    if (not os.path.exists(sub_output)) or rerun_strategy == 'force':
                        jobs.append((selection, sub_output))
                    elif rerun_strategy == 'merge':
                        logger.debug('OUT("{}") already exists! `rerun_strategy` is "merge" so SKIP running this job!'.format(sub_output))
                    else:
                        raise OSError('OUT("{}") already exists! Remove it or change `rerun_strategy` to "merge" or "force according to your needs"!'.format(sub_output))
                if jobs:
                    runfile = os.path.join(runfile_dir, s.sample_name + (s.tag and ('_' + s.tag)) + '.submit')
                    infile = self.write_inputsfile(s)
                    self.write_runfile(sample = s, output_files = jobs, runfile = runfile, stages = stages, infile = infile, **write_kwds)
                    subprocess.call(['chmod', 'u+x', runfile])
                    if not use_cluster:
                        subprocess.call([runfile])
                    else:
                        job_id = self.cluster.get_identifier()
                        _submit_kwds = copy.deepcopy(submit_kwds)
                        if isinstance(self.cluster, clusters.CERNGrid):
                            _submit_kwds['argument'].extend(['--inDS', ','.join(s._list_dids())])
                            _submit_kwds['argument'].extend(['--outDS',  'user.{CERN_USER}.{s.DSID[0]}.{s.physics_short}.{s.ami_tag[0]}.{r.tag}'.format(CERN_USER = samples.Sample._client.account, s = s, r = self)])
                            _submit_kwds['argument'].extend(['--writeInputToTxt=IN:' + infile])
                            _submit_kwds['argument'].extend(['--outputs', ','.join([os.path.join(self.output_dir, job[1]) for job in jobs] + [infile])])
                        self.cluster.submit2(runfile,
                                             stdout = os.path.join(self.log_dir, 'out.%s' % job_id),
                                             stderr = os.path.join(self.log_dir, 'out.%s' % job_id),
                                             log    = os.path.join(self.log_dir, 'log.%s' % job_id),
                                             **_submit_kwds)

    def finalize(self, do_merge = None, delete_sources_after_merged = False):
        do_merge = do_merge or self.do_merge
        if do_merge == True:
            for outstream in self.outstreams.viewvalues():
                for selection in outstream:
                    output = outstream[selection]['output']
                    sub_outputs = outstream[selection]['sub_outputs']
                    if len(sub_outputs) == 1 and output == sub_outputs[0]:
                        continue
                    helpers.hadd({output: sub_outputs}, delete_sources = delete_sources_after_merged)

    def wait(self):
        if self.cluster != None:
            self.cluster.wait(None, fct = get_fct(logger = helpers.getLogger('TopNtupleAnalysis.cluster')))

    def run(self, runfile_dir = None, use_cluster = True, monitor = True, rerun_strategy = 'merge', delete_sources_after_merged = False, execute_kwds = {}, finalize_kwds = {}):
        global __grid__
        execute_kwds = copy.deepcopy(execute_kwds)
        finalize_kwds = copy.deepcopy(finalize_kwds)
        cluster_arguments = execute_kwds.setdefault('submit_kwds', {}).setdefault('argument', [])

        __grid__ = isinstance(self.cluster, clusters.CERNGrid)
        if __grid__:
            self.output_dir = ''#os.path.split(self.output_dir.rstrip('/'))[-1]
            cluster_arguments.extend(["--maxNFilesPerJob=" + str(self.max_inputs_per_job)])
            cluster_arguments.extend(['--useAthenaPackages'])
            cluster_arguments.extend(['--excludeFile=./'])
#            if self.do_merge: # TODO: seems to cause some issues. commented out until resolved
#                cluster_arguments.extend(['--mergeOutput'])
#                finalize_kwds['do_merge'] = False # this is going to pass to Run.finalize so that it won't merge twice
            execute_kwds.setdefault('stages', ('exec',))
            execute_kwds.setdefault('max_inputs_per_job', False)
            execute_kwds.setdefault('check_exitcode', tuple())
        self.execute(runfile_dir = runfile_dir, use_cluster = use_cluster, rerun_strategy = rerun_strategy, **execute_kwds)
        if use_cluster and monitor:
            self.wait()
        self.finalize(delete_sources_after_merged = delete_sources_after_merged, **finalize_kwds)

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
