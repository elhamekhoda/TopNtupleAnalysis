import os
import glob
import math
import datetime
import subprocess
import urlparse


try:
    import HQTTtResonancesTools.Data_EXOT4_rel21
    import HQTTtResonancesTools.Data_EXOT7_rel21
    import HQTTtResonancesTools.MC16a_EXOT4
    import HQTTtResonancesTools.MC16a_EXOT7
    import HQTTtResonancesTools.MC16a_TOPQ1
except ImportError as e:
    print e.message
    raise ImportError("HQTTtResonancesTools is not installed or dataset does not exist.")
import rucio.client
try:
    import TopExamples.grid
    __TopExamples__ = True
except:
    __TopExamples__ = False
import helpers

logger = helpers.getLogger('TopNtupleAnalysis.samples')

DS_PATTERN = '{s.ds_scope}.{{{{s.DSID[{{i}}]}}}}.*.DAOD_{s.deriv}.{{{{s.ami_tag[{{i}}]}}}}.*{suffix}'
DS_SCOPE = 'user.{s._client.account}'

MAP_TO_SAMPLES = {# (<sample>, <derivation>): <physics_short>
                  # EXOT4
                  ('wbbjets', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_Wjets221'],
                  ('wccjets', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_Wjets221'],
                  ('wcjets', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_Wjets221'],
                  ('wljets', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_Wjets221'],
                  ('wjets', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_Wjets221'],
                  ('wjets2211', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_Wjets2211'],
                  ('data', 'EXOT4'): ['Data15_13TeV_25ns_EXOT4','Data16_13TeV_25ns_EXOT4','Data17_13TeV_25ns_EXOT4','Data18_13TeV_25ns_EXOT4'],
                  ('qcde', 'EXOT4'): ['Data15_13TeV_25ns_EXOT4', 'Data16_13TeV_25ns_EXOT4'],
                  ('qcdmu', 'EXOT4'): ['Data15_13TeV_25ns_EXOT4','Data16_13TeV_25ns_EXOT4'],
                  ('tt', 'EXOT4'):['MC16a_13TeV_25ns_FS_EXOT4_ttbar_nonallhad'],
                  ('tt_af2', 'EXOT4'):['MC16a_13TeV_25ns_FS_EXOT4_ttbar_nonallhad_af2'],
                  ('tt_had', 'EXOT4'):['MC16a_13TeV_25ns_FS_EXOT4_ttbar_nonallhad_had'],
                  ('tt_hdamp', 'EXOT4'):['MC16a_13TeV_25ns_FS_EXOT4_ttbar_nonallhad_hdamp'],
                  ('tt_hs', 'EXOT4'):['MC16a_13TeV_25ns_FS_EXOT4_ttbar_nonallhad_HS'],
                  ('tt_meoff', 'TOPQ1'):['MC16a_13TeV_25ns_FS_EXOT4_ttbar_nonallhad_MECoff'],
                  ('tt_mttsliced', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_ttbar_nonallhad', 'MC16a_13TeV_25ns_FS_EXOT4_ttbar_nonallhad_mttsliced'],
                  ('singletop', 'EXOT4'):['MC16a_13TeV_25ns_FS_EXOT4_singletop'],
                  ('zjets', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_Zjets221'],
                  ('dijets', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_dijets'],
                  ('vv', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_VV'],
                  ('ttV', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_ttbarV'],
                  ('zprime400', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_Zprime400'],
                  ('zprime500', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_Zprime500'],
                  ('zprime750', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_Zprime750'],
                  ('zprime1000', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_Zprime1000'],
                  ('zprime1250', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_Zprime1250'],
                  ('zprime1500', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_Zprime1500'],
                  ('zprime1750', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_Zprime1750'],
                  ('zprime2000', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_Zprime2000'],
                  ('zprime2250', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_Zprime2250'],
                  ('zprime2500', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_Zprime2500'],
                  ('zprime2750', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_Zprime2750'],
                  ('zprime3000', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_Zprime3000'],
                  ('zprime4000', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_Zprime4000'],
                  ('zprime5000', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_Zprime5000'],
                  ('kkgrav400', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_Gtt400'],
                  ('kkgrav500', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_Gtt500'],
                  ('kkgrav750', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_Gtt750'],
                  ('kkgrav1000', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_Gtt1000'],
                  ('kkgrav2000', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_Gtt2000'],
                  ('kkgrav3000', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_Gtt3000'],
                  ('zprimeMG400', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_MGZprime400'],
                  ('zprimeMG500', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_MGZprime500'],
                  ('zprimeMG750', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_MGZprime750'],
                  ('zprimeMG1000', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_MGZprime1000'],
                  ('zprimeMG1250', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_MGZprime1250'],
                  ('zprimeMG1500', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_MGZprime1500'],
                  ('zprimeMG1750', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_MGZprime1750'],
                  ('zprimeMG2000', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_MGZprime2000'],
                  ('zprimeMG2250', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_MGZprime2250'],
                  ('zprimeMG2500', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_MGZprime2500'],
                  ('zprimeMG2750', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_MGZprime2750'],
                  ('zprimeMG3000', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_MGZprime3000'],
                  ('zprimeMG4000', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_MGZprime4000'],
                  ('zprimeMG5000', 'EXOT4'): ['MC16a_13TeV_25ns_FS_EXOT4_MGZprime5000'],
                  # EXOT7
                  ('wbbjets', 'EXOT7'): ['MC16a_13TeV_25ns_FS_EXOT7_Wjets221'],
                  ('wccjets', 'EXOT7'): ['MC16a_13TeV_25ns_FS_EXOT7_Wjets221'],
                  ('wcjets', 'EXOT7'): ['MC16a_13TeV_25ns_FS_EXOT7_Wjets221'],
                  ('wljets', 'EXOT7'): ['MC16a_13TeV_25ns_FS_EXOT7_Wjets221'],
                  ('data', 'EXOT7'): ['Data15_13TeV_25ns_EXOT7','Data16_13TeV_25ns_EXOT7','Data17_13TeV_25ns_EXOT7','Data18_13TeV_25ns_EXOT7'],
                  ('data_debug', 'EXOT7'): ['Data15_13TeV_25ns_debug_stream_EXOT7','Data16_13TeV_25ns_debug_stream_EXOT7','Data17_13TeV_25ns_debug_stream_EXOT7','Data18_13TeV_25ns_debug_stream_EXOT7'],
                  ('tt', 'EXOT7'): ['MC16a_13TeV_25ns_FS_EXOT7_ttbar_allhad'],
                  ('tt_mttsliced', 'EXOT7'): ['MC16a_13TeV_25ns_FS_EXOT7_ttbar_allhad', 'MC16a_13TeV_25ns_FS_EXOT7_ttbar_allhad_mttsliced'],
                  ('ttnonallhad', 'EXOT7'): ['MC16a_13TeV_25ns_FS_EXOT7_ttbar_allhad'],
                  ('ttnonallhad_mttsliced', 'EXOT7'): ['MC16a_13TeV_25ns_FS_TOPQ1_ttbar_nonallhad', 'MC16a_13TeV_25ns_FS_EXOT7_ttbar_nonallhad_mttsliced'],
                  ('ttV', 'EXOT7'): ['MC16a_13TeV_25ns_FS_EXOT7_ttbarV'],
                  ('singletop', 'EXOT7'):['MC16a_13TeV_25ns_FS_EXOT7_singletop'],
                  ('zjets', 'EXOT7'): ['MC16a_13TeV_25ns_FS_EXOT7_Zjets221'],
                  ('dijets', 'EXOT7'): ['MC16a_13TeV_25ns_FS_EXOT7_dijets'],
                  ('vv', 'EXOT7'): ['MC16a_13TeV_25ns_FS_EXOT7_VV'],
                  ('zprime400', 'EXOT7'): ['MC16a_13TeV_25ns_FS_EXOT7_Zprime400'],
                  ('zprime500', 'EXOT7'): ['MC16a_13TeV_25ns_FS_EXOT7_Zprime500'],
                  ('zprime750', 'EXOT7'): ['MC16a_13TeV_25ns_FS_EXOT7_Zprime750'],
                  ('zprime1000', 'EXOT7'): ['MC16a_13TeV_25ns_FS_EXOT7_Zprime1000'],
                  ('zprime1250', 'EXOT7'): ['MC16a_13TeV_25ns_FS_EXOT7_Zprime1250'],
                  ('zprime1500', 'EXOT7'): ['MC16a_13TeV_25ns_FS_EXOT7_Zprime1500'],
                  ('zprime1750', 'EXOT7'): ['MC16a_13TeV_25ns_FS_EXOT7_Zprime1750'],
                  ('zprime2000', 'EXOT7'): ['MC16a_13TeV_25ns_FS_EXOT7_Zprime2000'],
                  ('zprime2250', 'EXOT7'): ['MC16a_13TeV_25ns_FS_EXOT7_Zprime2250'],
                  ('zprime2500', 'EXOT7'): ['MC16a_13TeV_25ns_FS_EXOT7_Zprime2500'],
                  ('zprime2750', 'EXOT7'): ['MC16a_13TeV_25ns_FS_EXOT7_Zprime2750'],
                  ('zprime3000', 'EXOT7'): ['MC16a_13TeV_25ns_FS_EXOT7_Zprime3000'],
                  ('zprime4000', 'EXOT7'): ['MC16a_13TeV_25ns_FS_EXOT7_Zprime4000'],
                  ('zprime5000', 'EXOT7'): ['MC16a_13TeV_25ns_FS_EXOT7_Zprime5000'],
                  ('zprime6000', 'EXOT7'): ['MC16a_13TeV_25ns_FS_EXOT7_Zprime6000'],
                  # TOPQ1
                  ('tt_mttsliced', 'TOPQ1'): ['MC16a_13TeV_25ns_FS_TOPQ1_ttbar_nonallhad', 'MC16a_13TeV_25ns_FS_TOPQ1_ttbar_nonallhad_mttsliced'],
                 }

MAP_TO_SAMPLES.update(
                 {
                 # EXOT4
                 ('data2015', 'EXOT4'): ['Data15_13TeV_25ns_EXOT4'],
                 ('data2016', 'EXOT4'): ['Data16_13TeV_25ns_EXOT4'],
                 ('data2017', 'EXOT4'): ['Data17_13TeV_25ns_EXOT4'],
                 ('data2018', 'EXOT4'): ['Data18_13TeV_25ns_EXOT4'],
                 # EXOT7
                 ('data2015', 'EXOT7'): ['Data15_13TeV_25ns_EXOT7'],
                 ('data2016', 'EXOT7'): ['Data16_13TeV_25ns_EXOT7'],
                 ('data2017', 'EXOT7'): ['Data17_13TeV_25ns_EXOT7'],
                 ('data2018', 'EXOT7'): ['Data18_13TeV_25ns_EXOT7'],
                 }

  )
def register_samples(mapping):
    MAP_TO_SAMPLES.update(mapping)

def write_totalweight_of_samples(list_of_samples, systs = [''], online = True, mode = 'auto'):
    isFirst = True
    for s in list_of_samples:
        s.sum_of_weights(systs = systs, online = online, mode = mode if isFirst else 'a', runNumber = s.runNumber, periodFraction = s.periodFraction)
        isFirst = False

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
                    print "dataset_name: ", dataset_name
                    return sample
        else:
            if not isinstance(obj, str):
                obj, deriv = obj
            for (dataset_name, dataset_deriv), physics_short in MAP_TO_SAMPLES.iteritems():
                if (obj.split('._')[0], deriv) == (dataset_name,  dataset_deriv):
                    sample.name = dataset_name
                    for s in TopExamples.grid.Samples(physics_short):
                        sample.datasets.extend(s.datasets)
                    return sample
        raise NameError('"{}" not found in the current sample list.\nNote that a user-defined sample must be first registered to {} using {}.\nAlready Registered Samples: {}'
                        .format(obj, '`{}`'.format(__name__ + '.MAP_TO_SAMPLES'), '`{}`'.format(__name__ + '.register_samples'), sorted(MAP_TO_SAMPLES.iterkeys())))

    def __init__(self, sample_name,
                       input_files = None,
                       ds_scope = DS_SCOPE,
                       ds_pattern = DS_PATTERN,
                       ds_fmt_options = {'suffix': '_output.root'},
                       tag = '',
                       download_to = None,
                       commit_when_init = True,
                       deriv = 'EXOT4',
                       periodFraction = 1,
                       runNumber = 'ALL',
                       RSE_preferred = None,
                       priority_key = None,
                       force_amitag = None
                       ):
        self.parent = self
        self.ds_scope = ds_scope.format(s = self, **ds_fmt_options)
        if not isinstance(sample_name, str):
            sample_name, deriv = sample_name
        self.sample_name = sample_name
        self.periodFraction = periodFraction
        self.runNumber = runNumber
        self.sample = self.parse_dataset((sample_name, deriv))
        self.deriv = deriv
        self.RSE_preferred = RSE_preferred
        self.priority_key = priority_key or (lambda pfns: ((pfns[1].get('rse') or pfns[1]['rse_expression']) == self.RSE_preferred, pfns[1]['priority']))
        
        force_amitag = force_amitag if (force_amitag is not None) else (sample_name is 'data') # default to use ami-tag to prevent ambiguity caused by the period containers
        if not force_amitag:
            ds_pattern = ds_pattern.replace('{{{{s.ami_tag[{{i}}]}}}}.', '')
        self._ds_pattern_fmt = ds_pattern.format(s = self, **ds_fmt_options)

        if self._ds_pattern_fmt.startswith('user.'):
            head, _, tail = self._ds_pattern_fmt.partition(':')
            self.ds_scope = head if tail else '.'.join(head.split('.')[:2])
        self.download_to = download_to if download_to is not True else os.curdir
        self.commited = False
        self.tag = tag if (not tag or tag.startswith('_')) else ('_'+tag) # Note this is a custom tag mainly for differentiate samples with the same type
                       # e.g. two different zprime1000 samples with different object definitions and etc.
                       # So, this "doesn't necessarily" mean ami-tag yet it can be
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
    def ntuples(self):
      return self._list_dids()

    @property
    def ds_pattern(self):
        return sorted(set(self._ds_pattern_fmt.format(i=i).format(s=self) for i in xrange(len(self.shortNameDatasets))))
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
            if type(astr) == str:
                systematics = [astr]
            else:
                systematics = list(astr)
        else:
            systematics = ["all"]
        if any(name in self.parent.sample_name for name in ["data", "qcde", "qcdmu"]):
            systematics = ["nominal"]
        self._systematics = systematics

    systematics = property(get_systematics, set_systematics)
    @property
    def is_data(self):
        if "data" in self.parent.sample_name:
            return " -d "
        if "qcde" in self.parent.sample_name:
            return " -d -Q e "
        if "qcdmu" in self.parent.sample_name:
            return " -d -Q mu "
        return ""
    @property
    def extra(self):
        if "wbbjets" in self.parent.sample_name:
            return ' --WjetsHF bb '
        elif 'wccjets' in self.parent.sample_name:
            return ' --WjetsHF cc'
        elif 'wcjets' in self.parent.sample_name:
            return ' --WjetsHF c'
        elif 'wljets' in self.parent.sample_name:
            return ' --WjetsHF l'
        if 'tt' == self.parent.sample_name:
            logger.debug('When using inclusive ttbar sample exclusively, the `--noMttSlices` option is activated automatically.\n'
                        +'\tIf you want to use it together with sliced mtt ttbar samples, use samples.Sample(\'tt_mttsliced\') instead.')
            return ' --noMttSlices'
        return ''
    def get_input_files(self):
        if not self._input_files:
            logger.critical('{!r}: inputs list is empty!'.format(self))
        return self._input_files
    def set_input_files(self, alist = None, force = True, sort = True, inplace = True, priority_key = None):
        input_files = []
        if alist == None:
            if not force and inplace and bool(getattr(self, '_input_files', False)):
                return self._input_files
            priority_key = priority_key or self.priority_key
            for replica in self._client.list_replicas([{'scope': self.ds_scope, 'name': dids} for dids in self._list_dids()], schemes = ['root']):
                if replica['pfns']:
                    file, _ = max(replica['pfns'].iteritems(), key = priority_key)
                    input_files.append(file)
        elif type(alist) == str:
            input_files = [alist]
        else:
            input_files = list(alist)
        input_files.sort()
        if not inplace:
            return input_files
        else:
            self._input_files = input_files
            return self._input_files
    input_files = property(get_input_files, set_input_files)
    def get_replication_rules(self):
        for f in self._input_files:
            yield tuple(self._client.list_associated_rules_for_file(self.ds_scope, os.path.basename(urlparse.urlparse(f).path)))
    def set_replication_lifetime(self, t = datetime.timedelta(days=14), only = range(1)):
        for rules in self.get_replication_rules():
            i = 0
            for _, rule in sorted(enumerate(rules), key = self.priority_key):
                if not (only and i not in only):
                    seconds = int(math.floor(t.total_seconds()))
                    try:
                        logger.info('Update replication rule:')
                        logger.info('\tname:{}'.format(rule['name']))
                        logger.info('\tid:{}'.format(rule['id']))
                        logger.info('\tRSE:{}'.format(rule['rse_expression']))
                        logger.info('\tfor {} days'.format(t.days))
                        self._client.update_replication_rule(rule['id'], {'lifetime': seconds})
                        logger.info('\tSuccess!')
                    except Exception as e:
                        logger.exception(e)
                i += 1
    def extend_replication_lifetime(self, max_extend = datetime.timedelta(days=14), only = range(1), lower_limit = datetime.timedelta(days=3)):
        now = datetime.datetime.now()
        for rules in self.get_replication_rules():
            i = 0
            for _, rule in sorted(enumerate(rules), key = self.priority_key):
                if not (only and i not in only):
                    expires_at = rule['expires_at']
                    if expires_at is None:
                      expires_at = datetime.datetime.max
                    remained = expires_at - now
                    to_extended = max_extend - remained
                    seconds = int(math.floor(to_extended.total_seconds()))
                    try:
                        logger.info('Update replication rule:')
                        logger.info('\tname:{}'.format(rule['name']))
                        logger.info('\tid:{}'.format(rule['id']))
                        logger.info('\tRSE:{}'.format(rule['rse_expression']))
                        if remained >= lower_limit:
                            logger.info('\tSkip! Remaining lifetime is long enough (>={} days).'.format(lower_limit.days))
                            i += 1
                            continue
                        logger.info('\tfor {} days'.format(to_extended.days))
                        self._client.update_replication_rule(rule['id'], {'lifetime': seconds})
                        logger.info('\tSuccess!')
                    except Exception as e:
                        logger.exception(e)
                i += 1
    def add_replication_rule(self, rse = None, only = range(1), allow_fail = True, **kwds):
        rse = rse or self.RSE_preferred
        try:
            logger.info('Adding replication rule:')
            dids = [{'scope': self.ds_scope, 'name': dids} for dids in self._list_dids()]
            for did in dids:
                logger.info('\tname:{}'.format(did['name']))
                logger.info('\tRSE:{}'.format(rse))
            self._client.add_replication_rule(dids, len(only), rse, **kwds)
        except Exception as e:
            logger.warning(e)
            if not allow_fail:
                raise
            else:
                logger.info('\tSKIP!')

    def download_dataset(self, ds_name = None, only_retrieve_cmd = False):
        dirname = os.path.abspath(ds_name or self.download_to)
        input_files = []
        if only_retrieve_cmd:
            cmds = []
        for s in self._list_dids():
            cmd = ['rucio','download', s, '--dir', dirname, '--transfer-timeout', '3600']
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
        return '<{}.{}("{}"{})>'.format(self.__class__.__module__, self.__class__.__name__, self.sample_name, self.tag and '[{}]'.format(self.tag))
    def sum_of_weights(self, systs = [''], online = True, mode = 'return', runNumber = None, periodFraction = None):
        if self.sample_name == 'data':
            raise TypeError('DO NOT use DATA Weights')
        elif self.sample_name == 'data_debug':
            raise TypeError('DO NOT use DATA Weights')
        runNumber = runNumber or self.runNumber
        periodFraction = periodFraction or self.periodFraction
        if not self.commited:
            online = True
        logger.info('Compute TOTAL MC Weights using {} datasets'.format('online' if online else 'offline'))
        import tempfile
        from TopNtupleAnalysis.sumWeights import sumWeights
        infile = tempfile.NamedTemporaryFile(delete = False)
        infile.close()
        self.write_inputsfile(infile.name, inplace = False if online else True)
        total_weights = sumWeights([infile.name]*len(systs), systs, suffix = '_R21',  mode = mode, runNumber = runNumber, periodFraction = periodFraction)[0]['SumOfWeights']
        os.remove(infile.name)
        return total_weights
    def write_inputsfile(self, fname, **set_input_files_kwds):
        with open(fname, 'w') as infile:
            infile.writelines('\n'.join(self.set_input_files(force = False, **set_input_files_kwds)))

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
        cmds = []
        cluster = {}
        for dataset, file in map(os.path.split, self.input_files):
            dataset = dataset.rstrip('/').rpartition('/')[-1]
            dirname = os.path.join(os.path.abspath(ds_name or self.parent.download_to), dataset)
            cluster.setdefault(dirname, []).append(file)
        for dirname, _files in cluster.iteritems():
            files = []
            for f in _files:
                if os.path.exists(os.path.join(dirname, f)):
                    cmds.append(['echo', '"{}: file already found locally. Won\'t be downloaded"'.format(f)])
                else:
                    files.append(f)
            if files:
                cmds.append(['rucio','download'] + files + ['--dir', dirname, '--no-subdir'])
            if only_retrieve_cmd:
                cmds = [' '.join(cmd)+'\n' for cmd in cmds]
            else:
                for cmd in cmds:
                    subprocess.call(cmd)
        if only_retrieve_cmd:
            return cmds
    def sum_of_weights(self):
        raise NotImplementedError('I don\'t think you really want to do this.')

def part_sample(sample, max_input_files = 5, sort = True):
    if callable(max_input_files):
        max_input_files = max_input_files(sample)
    if not sample.commited:
        sample.commit(only_retrieve_cmd = True)
    l = len(sample.input_files)
    systs = [sample.systematics] if type(sample.systematics) == str else list(sample.systematics)
    if l <= max_input_files or max_input_files in (None, 0, 'none', False):
        max_input_files = l
    ret = []
    n = 1
    if max_input_files in (None, 0):
        max_input_files = l
    if max_input_files == 0:
        max_input_files = 1
    for i in xrange(0, l, max_input_files):
        for syst in systs:
            subsample = SubSample(sample, sample.input_files[i:min(i+max_input_files, l)], suffix = '{:06d}'.format(n))
            subsample.systematics = syst
            ret.append(subsample)
            n += 1
    return ret

