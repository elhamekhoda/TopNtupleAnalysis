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
import DC14MC13TeV

inputDirectory = '/afs/phas.gla.ac.uk/user/d/dferreira/atlas_data/dferreira02/tt13e4_12'
runDirectory = 'test12/'

names  = ['13TeV_FS_ttbarPowhegPythia_e4', '13TeV_FS_ZmassivebcSherpa_e4', '13TeV_FS_SingleTopPowhegPythia_e4', '13TeV_FS_WmassivebcSherpa_e4']
names += ['13TeV_FS_ZprimePythia500_e4', '13TeV_FS_ZprimePythia1000_e4', '13TeV_FS_ZprimePythia2000_e4', '13TeV_FS_ZprimePythia3000_e4', '13TeV_FS_ZprimePythia5000_e4']

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
    for s in sample.datasets:
      if s.split('.')[0] == 'mc14_13TeV':
        dsid_sample = s.split('.')[1]
      elif s.split('.')[0] == 'user':
        dsid_sample = s.split('.')[2]
      if dsid_dir == dsid_sample:
        command = command + ' '+dir+'/*.root*'
        break
  os.system(command)

