#!/usr/bin/env python
from os import system,getcwd
from time import time
from inputs import *
import socket, random, re

# change those:
setdir = '/afs/desy.de/user/d/danilo/xxl/af-atlas/Top2421'
mydir = '/nfs/dust/atlas/user/danilo/hists_2421/TRexFitter'

def fixFile(template, final, sig, dirname, doBOnlyFit):
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
''' % ('hist_'+sig))
      if 'eft' in sig:
        f.write('''
Systematic: "eftScale"
  Title: "EFT scale unc."
  Type: HISTO
  HistoNameSufUp: "eftScaleup"
  HistoNameSufDown: "eftScaledw"
  Samples: Signal
  Symmetrisation: TwoSided
  Smoothing: 40
''')
      continue
    
    nline = line
    if 'Ttres' in nline:
      nline = nline.replace('Ttres', 'Ttres_'+dirname)
    if 'SystControlPlots' in nline and (not doBOnlyFit):
      nline = nline.replace('TRUE', 'FALSE')
    if 'FitType' in nline and doBOnlyFit:
      nline = nline.replace('SPLUSB', 'BONLY')
    if 'POIAsimov' in nline and 'inj' in dirname:
      nline = nline.replace('POIAsimov: 0', 'POIAsimov: 1')
    if 'eft' in sig and 'Binning: ' in nline:
      nline = "  Binning: 2000,6000\n"
    f.write(nline)

  f.close()
  fr.close()


def jobSubmit(suf, extra = ""):
	runfile = 'submit_%s%s.sh' % (suf, extra)
	logfile = mydir+'/stdout_%s%s.txt'%(suf, extra)
	queue = 'long.q'
	if 'bkg' in suf:
		queue = 'short.q'
	email = 'dferreir@cern.ch'
	jobName = 'ttlim_%s%s'%(suf, extra)
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
	fr.write('./myFit.exe h ttres_%s%s.config\n'%(suf, extra))
	fr.write('./myFit.exe d ttres_%s%s.config\n'%(suf, extra))
	fr.write('./myFit.exe w ttres_%s%s.config\n'%(suf, extra))
	fr.write('./myFit.exe f ttres_%s%s.config\n'%(suf, extra))
	fr.write('./myFit.exe p ttres_%s%s.config\n'%(suf, extra))
	if not 'bkg' in suf:
		fr.write('./myFit.exe l ttres_%s.config\n'%suf)
		fr.write('./myFit.exe s ttres_%s.config\n'%suf)
	fr.close()
	system('chmod a+x %s'%runfile)
	system('qsub %s'%runfile)
	#system('./%s > %s 2>&1 '% (runfile, logfile))


# B ONLY fit
suf = ""
import sys
if len(sys.argv) > 1:
  suf = sys.argv[1]
#fixFile('ttres.config', 'ttres_bkg%s.config' % suf, "bkg%s" %suf, "bkg%s" %suf, True)
#system('cp -f hist_zprime1000.root hist_bkg%s.root' %suf) ## use a dummy signal for the background only fit
#jobSubmit('bkg%s' %suf)

fixFile('ttres.config', 'ttres_zprime2000_inj%s.config' % suf, "zprime2000%s" %suf, "zprime2000_inj%s" %suf, False)
jobSubmit('zprime2000_inj%s' %suf)

# now go over to signal
#for t in signalList:
#  if "eft" in t:
#    continue
#  for i in signalList[t]:
#    fixFile('ttres.config', 'ttres_%s%s.config' %(i, suf), i, "%s%s" % (i, suf), False)
#    jobSubmit("%s%s" % (i, suf))

