#!/usr/bin/env python
from os import system,getcwd
from time import time
from inputs import *
import socket, random, re

# change those:
setdir = '/afs/desy.de/user/d/danilo/xxl/af-atlas/Top2418'
mydir = '/nfs/dust/atlas/user/danilo/hists_sr2418_jes/TRexFitter'

def fixFile(template, final, i, doBOnlyFit):
  fr = open(template, 'r')
  f = open(final, 'w')

  for line in fr:
    if '% SIGNAL' in line:
      f.write('''
Sample: "Signal"
  Type: SIGNAL
  Title: "Signal"
  LineColor: 632
  NormFactor: "SigXsecOverSM",0,0,100
  HistoFile: "%s"
''' % ('hist_'+i))
      if 'eft' in i:
        f.write('''
Systematic: "eftScale"
  Title: "EFT scale unc."
  Type: HISTO
  HistoNameSufUp: "eftScaleup"
  HistoNameSufDown: "eftScaledw"
  Samples: Signal
  Symmetrisation: TwoSided
''')
      continue
    
    nline = line
    if 'FitTtres' in nline:
      nline = nline.replace('FitTtres', 'FitTtres_'+i)
    if 'JobTtres' in nline:
      nline = nline.replace('JobTtres', 'JobTtres_'+i)
    if 'FitType' in nline and doBOnlyFit:
      nline = nline.replace('SPLUSB', 'BONLY')
    f.write(nline)

  f.close()
  fr.close()


def jobSubmit(suf):
	runfile = 'submit_%s.sh' % suf
	logfile = mydir+'/stdout_%s.txt'%suf
	queue = 'long.q'
	email = 'dferreir@cern.ch'
	jobName = 'ttlim_%s'%suf
	fr = open(runfile, 'w')
	fr.write('#!/bin/sh\n')
	fr.write('#$ -cwd\n')
	fr.write('#$ -j y\n')
	fr.write('#$ -l cvmfs\n')
	fr.write('#$ -l distro=sld6\n')
	fr.write('#$ -l arch=amd64\n')
	fr.write('#$ -l h_vmem=35G\n')
	fr.write('#$ -o '+logfile+'\n')
	fr.write('#$ -q '+queue+'\n')
	fr.write('#$ -m '+'eas'+'\n')
	fr.write('#$ -M '+email+'\n')
	fr.write('#$ -N '+jobName+'\n')
	fr.write('cd '+setdir+'\n')
	fr.write('export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase\n')
	fr.write('export DQ2_LOCAL_SITE_ID=DESY-HH_SCRATCHDISK \n')
	fr.write('source /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/user/atlasLocalSetup.sh\n')
	fr.write('lsetup rcsetup\n')
	fr.write('cd '+mydir+'\n')
	fr.write('./myFit.exe h ttres_%s.config\n'%suf)
	fr.write('./myFit.exe d ttres_%s.config\n'%suf)
	fr.write('./myFit.exe w ttres_%s.config\n'%suf)
	fr.write('./myFit.exe f ttres_%s.config\n'%suf)
	fr.write('./myFit.exe p ttres_%s.config\n'%suf)
	if not 'bkg' in suf:
		fr.write('./myFit.exe l ttres_%s.config\n'%suf)
		fr.write('./myFit.exe s ttres_%s.config\n'%suf)
	fr.close()
	system('chmod a+x %s'%runfile)
	system('qsub %s'%runfile)


# B ONLY fit
#fixFile('ttres_template.config', 'ttres_bkg.config', "bkg", True)
#system('cp -f hist_zprime2000.root hist_bkg.root') ## use a dummy signal for the background only fit
#jobSubmit('bkg')

# now go over to signal
for t in signalList:
  if t != 'eft10':
    continue
  for i in signalList[t]:
    fixFile('ttres_template.config', 'ttres_'+i+'.config', i, False)
    jobSubmit(i)

