import os
import sys
import subprocess
import glob
try:
    import HQTTtResonancesTools.DC15Data13TeV_25ns_207_EXOT4
    import HQTTtResonancesTools.MC16a_EXOT4
except ImportError:
    raise ImportError("HQTTtResonancesTools is not installed or dataset does not exist.")
import rucio.client
import TopExamples.grid

import helpers

logger = helpers.getLogger('TopNtupleAnalysis.samples')

DS_PATTERN = '{s.ds_scope}.{{{{s.DSID[{{i}}]}}}}.*{suffix}'
DS_SCOPE = 'user.{s._client.account}'

MAP_TO_SAMPLES = {# <sample>: <physics_short>
                'wbbjets': 'MC16_13TeV_25ns_FS_EXOT4_Wjets22',
                'wccjets': 'MC16_13TeV_25ns_FS_EXOT4_Wjets22',
                'wcjets': 'MC16_13TeV_25ns_FS_EXOT4_Wjets22',
                'wljets': 'MC16_13TeV_25ns_FS_EXOT4_Wjets22',
                'data': 'Data15_13TeV_25ns_207_EXOT4,Data16_13TeV_25ns_207_EXOT4',
                'qcde': 'Data15_13TeV_25ns_207_EXOT4,Data16_13TeV_25ns_207_EXOT4',
                'qcdmu': 'Data15_13TeV_25ns_207_EXOT4,Data16_13TeV_25ns_207_EXOT4',
                'tt':'MC16_13TeV_25ns_FS_EXOT4_ttbar_nonallhad',
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
                if obj.split('._')[0] == dataset_name:
                    sample.name = dataset_name
                    sample.datasets.extend(TopExamples.grid.Samples(physics_short.split(','))[0].datasets)
                    return sample
        assert True, "Houston we've got a problem"

    def __init__(self, sample_name, input_files = None, ds_scope = DS_SCOPE, ds_pattern = DS_PATTERN, ds_fmt_options = {'suffix': '13022018v1_output.root'}, download_to = None, commit_when_init = True):
        self.parent = self
        self.ds_scope = ds_scope.format(s = self, **ds_fmt_options)
        self.sample_name = sample_name
        self.sample = self.parse_dataset(sample_name)
        self._ds_pattern_fmt = ds_pattern.format(s = self, **ds_fmt_options)
        self.download_to = download_to if download_to is not True else os.curdir
        self.commited = False
        self.set_systematics()
        if commit_when_init or input_files:
            self.commit(input_files)

    def _list_dids(self, scope = None, filters = {}):
        ret = []
        scope = scope or self.ds_scope
        for ds_pattern in self.ds_pattern:
            _filters = dict({'name': ds_pattern}, **filters)
            _ret = list(self._client.list_dids(scope = scope, filters = _filters))
            if not _ret:
                p = "{scope}:{pattern}".format(scope = scope, pattern = _filters.get('name'))
                if 'type' in _filters:
                    p += ' [' + _filters['type'] + ']'
                logger.critical('{}: DIDs with pattern "{}" not found. Please check if it really exists on grid.'.format(self, p))
            ret.extend(_ret)
        ret.sort()
        return ret

    @property
    def ds_pattern(self):
        return sorted(set(self._ds_pattern_fmt.format(i=i).format(s=self) for i in range(len(self.shortNameDatasets))))
    @property
    def physics_short(self):
        return self.sample.name
    @property
    def shortNameDatasets(self):
        return self.sample.shortNameDatasets()
    @property
    def ami_tag(self):
        return [shortNameDataset.split('.')[1] for shortNameDataset in self.shortNameDatasets]
    @property
    def DSID(self):
        return [shortNameDataset.split('.')[0] for shortNameDataset in self.shortNameDatasets]
    @property
    def datasets(self):
        return self.sample.datasets

    def get_systematics(self):
        return self._systematics
    def set_systematics(self, astr = None):
        if astr != None:
            self._systematics = astr
            return
        for name in ["data", "qcde", "qcdmu"]:
            if name in self.sample_name:
                self._systematics = "nominal"
                return
        self._systematics = "all"
    systematics = property(get_systematics, set_systematics)
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
        if not self._input_files:
            logger.critical('{!r}: inputs list is empty!'.format(self))
        return self._input_files
    def set_input_files(self, alist = None, force = True, sort = True):
        input_files = []
        if alist == None:
            if not force and getattr(self, '_input_files', None):
                return
            for files in (replica['pfns'].keys() for replica in self._client.list_replicas([{'scope': self.ds_scope, 'name': dids} for dids in self._list_dids()], schemes = ['root'])):
                input_files.append(files[0])
        elif type(alist) == str:
            input_files = [alist]
        else:
            input_files = list(alist)
        input_files.sort()
        self._input_files = input_files
    input_files = property(get_input_files, set_input_files)
    def download_dataset(self, ds_name = None, only_retrieve_cmd = False):
        dirname = os.path.abspath(ds_name or self.download_to)
        input_files = []
        if only_retrieve_cmd:
            cmds = []
        for s in self._list_dids():
            cmd = ['rucio','download', s, '--dir', dirname]
            if only_retrieve_cmd:
                cmds.append(' '.join(cmd)+'\n')
                input_files.extend([os.path.join(dirname, s, d['name']) for d in self._client.list_files(scope = self.ds_scope, name = s)])
                continue
            subprocess.call(cmd)
            input_files.extend(map(os.path.abspath, glob.iglob(os.path.join(dirname, s, '*.root*'))))
        self.input_files = input_files
        if only_retrieve_cmd:
            return cmds
    def remove_dataset(self, ds_name = None):
        # dirname = ds_name or self.download_to
        for f in self.input_files:
            os.remove(f)
        self.input_files = []
    def commit(self, input_files = None, only_retrieve_cmd = False):
        if self.commited and not only_retrieve_cmd:
            return
        elif not self.download_to:
            self.set_input_files(input_files, force = False)
            self.commited = True
            return
        else:
            cmds = self.download_dataset(self.download_to, only_retrieve_cmd = only_retrieve_cmd)
        self.commited = True
        if only_retrieve_cmd:
            assert type(cmds) == list, "Houston we've got a problem"
            return cmds
    def __repr__(self):
        return '<{}.{}("{}")>'.format(self.__class__.__module__, self.__class__.__name__, self.sample_name)
    def sum_of_weights(self):
        raise NotImplementedError
    def write_inputsfile(self, fname):
        with open(fname, 'w') as infile:
            infile.writelines('\n'.join(self.input_files))

class SubSample(Sample):
    def __init__(self, parent, input_files, suffix):
        self.parent = parent
        self.sample_name = self.parent.sample_name + '._{}'.format(suffix)
        self.input_files = input_files
        self.commited = False
    def __getattr__(self, attr):
        try:
            return self.__getattribute__(attr)
        except AttributeError:
            return self.parent.__getattribute__(attr)
    def download_dataset(self, ds_name = None, only_retrieve_cmd = False):
        if only_retrieve_cmd:
            cmds = []
        cluster = {}
        for dataset, file in map(os.path.split, self.input_files):
            dataset = dataset.rstrip('/').rpartition('/')[-1]
            dirname = os.path.join(os.path.abspath(ds_name or self.parent.download_to), dataset)
            cluster.setdefault(dirname, []).append(file)
        for dirname, files in cluster.iteritems():
            cmd = ['rucio','download'] + files + ['--dir', dirname, '--no-subdir']
            if only_retrieve_cmd:
                cmds.append(' '.join(cmd)+'\n')
            else:
                subprocess.call(cmd)
        if only_retrieve_cmd:
            return cmds

def part_sample(sample, max_input_files = 5, sort = True):
    if not sample.commited:
        sample.commit(only_retrieve_cmd = True)
    l = len(sample.input_files)
    if l <= max_input_files or max_input_files == None:
        return [sample]
    ret = [SubSample(sample, sample.input_files[i:min(i+max_input_files, l)], suffix = '{:06d}'.format(suffix)) for suffix, i in enumerate(range(0, l, max_input_files), 1)]
    return ret

