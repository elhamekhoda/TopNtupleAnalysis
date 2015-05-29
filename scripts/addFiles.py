#!/usr/bin/env python

# to run this, be sure you have checked out TopExamples
# alternatively, if you want to run this without RootCore:
# mkdir TopExamples
# cp [from TopExamples main directory]/python/grid.py TopExamples/
# touch TopExamples/__init__.py
# export PYTHONPATH=$PYTHONPATH:$PWD
# and copy DC14MC13TeV.py to the current directory
#
# you are free to add the Grid results in any other way you prefer
import HQTTtResonancesTools.DC15MC13TeV_EXOT4_p2352
import HQTTtResonancesTools.DC14MC13TeV_EXOT4_p1845

inputDirectory = '/afs/cern.ch/user/d/dferreir/work/eos/atlas/user/d/dferreir/topana/28052015'
runDirectory = 'test13/'

names  = ['MC15_13TeV_FS_EXOT4_ttbarPowhegPythia']
#name   += ['MC15_13TeV_FS_EXOT4_ZmassivebcSherpa', 'MC15_13TeV_FS_EXOT4_SingleTopPowhegPythia_e4', 'MC15_13TeV_FS_EXOT4_WmassivebcSherpa_e4']
#names += ['MC15_13TeV_FS_EXOT4_ZprimePythia500', 'MC15_13TeV_FS_EXOT4_ZprimePythia1000_e4', 'MC15_13TeV_FS_EXOT4_ZprimePythia2000_e4', 'MC15_13TeV_FS_EXOT4_ZprimePythia3000_e4', 'MC15_13TeV_FS_EXOT4_ZprimePythia5000_e4']

import TopExamples.grid

samples = TopExamples.grid.Samples(names)
#for sample in samples:
#  print sample.name
#  print sample.datasets

import glob
import os
dirs = glob.glob(inputDirectory+'/*')
for sample in samples:
  command = 'hadd -f '+sample.name+'.root '
  for dir in dirs:
    print dir
    justfile = dir.split('/')[-1]
    if not justfile.split('.')[0] == 'user':
      continue
    dsid_dir = justfile.split('.')[2]
    for mys in sample.datasets:
      s = mys
      if len(s.split(':')) > 1:
        s = s.split(':')[1]
      if s.split('.')[0] == 'mc15_13TeV':
        dsid_sample = s.split('.')[1]
      elif s.split('.')[0] == 'mc14_13TeV':
        dsid_sample = s.split('.')[1]
      elif s.split('.')[0] == 'user':
        dsid_sample = s.split('.')[2]
      if dsid_dir == dsid_sample:
        command = command + ' '+dir+'/*.root*'
        break
  os.system(command)

