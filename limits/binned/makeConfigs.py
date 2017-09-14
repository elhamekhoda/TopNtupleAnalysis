#!/usr/bin/env python
from os import system,getcwd
from time import time
from inputs import *
import socket, random, re

# change those:
setdir = '/nfs/dust/atlas/user/danilo/topana2429'
mydir = '/nfs/dust/atlas/user/danilo/plots2/TRExFitter'

systlist = []
systlist += ['WtDRDS', 'akt10baseline', 'akt10jertau32', 'akt10model', 'akt10track']
systlist += ['akt4jer', 'akt4jes1', 'akt4jes2', 'akt4jes3', 'akt4jes5', 'akt4jes6', 'akt4jesetamod', 'akt4jesetanc', 'akt4jesetastat', 'akt4jesfchf', 'akt4jesfclf', 'akt4jesfr', 'akt4jespuoffmu', 'akt4jespuoffnpv', 'akt4jespupt', 'akt4jespurho']
systlist += ['btagb0', 'btagb1', 'btagc0pt1', 'btagc0pt2', 'btagc0pt3', 'btagc1', 'btagc2', 'btagc3', 'btage0', 'btagl0pt1', 'btagl0pt2', 'btagl0pt3', 'btagl1', 'btagl2', 'btagl3', 'btagl4']
systlist += ['lumi', 'metrespara', 'metresperp', 'metscale', 'pileupsf']
systlist += ['qcde_boo12c', 'qcde_boo12f', 'qcde_boo3c', 'qcde_boo3f', 'qcde_res12c', 'qcde_res12f', 'qcde_res3c', 'qcde_res3f', 'qcdmu_boo12', 'qcdmu_boo3', 'qcdmu_res12', 'qcdmu_res3']
systlist += ['singletop', 'ttgen', 'ttisrfsr', 'ttpdf0', 'ttpdf22', 'ttpdf5', 'ttpdf6', 'ttps_boo', 'ttps_res', 'ttxsec', 'wasym', 'wbb', 'wc']
systlist += ['wjpdf%d' % x for x in range(1,101)]

def fixFile(template, final, sig, dirname, doBOnlyFit):
  fr = open(template, 'r')
  f = open(final, 'w')

  beginSysts = False
  for line in fr:
    if '% SIGNAL' in line:
      f.write('''
Sample: "Signal"
  Type: SIGNAL
  Title: "Signal"
  LineColor: 632
  NormFactor: "SigXsecOverSM",1,0,100
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
    if 'SystControlPlots' in nline and ((not doBOnlyFit) or 'cat' in dirname):
      nline = nline.replace('TRUE', 'FALSE')
      if 'stat' in dirname:
        nline += '  StatOnly: TRUE\n'
    if 'FitType' in nline and doBOnlyFit:
      nline = nline.replace('SPLUSB', 'BONLY')
    if 'POIAsimov' in nline and 'inj' in dirname:
      nline = nline.replace('POIAsimov: 0', 'POIAsimov: 1')
    if ('Systematic:' in nline or beginSysts) and 'stat' in dirname:
      beginSysts = True
      nline = '###'+nline
    if 'eft' in sig and 'Binning: ' in nline:
      nline = "  Binning: 2000,6000\n"
    f.write(nline)

  f.close()
  fr.close()


def jobSubmit(suf, extra = ""):
	runfile = 'submit_%s%s.sh' % (suf, extra)
	logfile = mydir+'/stdout_%s%s.txt'%(suf, extra)
	queue = 'long.q'
	#if 'bkg' in suf:
	#	queue = 'short.q'
	email = 'dferreir@cern.ch'
	jobName = 'ttlim_%s%s'%(suf, extra)
	fr = open(runfile, 'w')
	fr.write('#!/bin/sh\n')
	#fr.write('#$ -cwd\n')
	fr.write('#$ -j y\n')
	fr.write('#$ -l cvmfs\n')
	#fr.write('#$ -l distro=sld6\n')
	fr.write('#$ -l distro=el7\n')
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
	if 'bkg' in suf or ('zprime3000_binning' in suf or 'zprime5000_binning' in suf):
		fr.write('./myFit.exe d ttres_%s%s.config\n'%(suf, extra))
	fr.write('./myFit.exe w ttres_%s%s.config\n'%(suf, extra))
	fr.write('./myFit.exe f ttres_%s%s.config\n'%(suf, extra))
	if 'bkg' in suf:
		fr.write('./myFit.exe p ttres_%s%s.config\n'%(suf, extra))
	if not 'bkg' in suf:
		fr.write('./myFit.exe l ttres_%s.config\n'%suf)
		fr.write('./myFit.exe s ttres_%s.config\n'%suf)
	if not ('stat' in suf or 'binning' in suf or 'nnlo' in suf or 'boottnorm' in suf) and ('zprime2000' in suf or 'zprime3000' in suf):
		for sitem in systlist:
			fr.write('./myFit.exe r ttres_%s.config Ranking=%s\n'%(suf, sitem))
		fr.write('./myFit.exe r ttres_%s.config Ranking=plot\n'%suf)
	fr.close()
	system('chmod a+x %s'%runfile)
	print("Running %s" % runfile)
	system('qsub %s'%runfile)
	#system('./%s > %s 2>&1 '% (runfile, logfile))
	#import time
	#time.sleep(40*60)


# B ONLY fit
suf = ""
import sys
if len(sys.argv) > 1:
  suf = sys.argv[1]

# nominal
fixFile('ttres.config', 'ttres_bkg%s.config' % suf, "bkg%s" %suf, "bkg%s" %suf, True)
system('cp -f hist_zprime1000.root hist_bkg%s.root' %suf) ## use a dummy signal for the background only fit
jobSubmit('bkg%s' %suf)

# mtt slope
fixFile('ttres_slope.config', 'ttres_bkg_slope%s.config' % suf, "bkg_slope%s" %suf, "bkg_slope%s" %suf, True)
system('cp -f hist_zprime1000.root hist_bkg_slope%s.root' %suf) ## use a dummy signal for the background only fit
jobSubmit('bkg_slope%s' %suf)

# decorrelate ISR/FSR between boosted and resolved
fixFile('ttres_decscale.config', 'ttres_bkg_decscale%s.config' % suf, "bkg_decscale%s" %suf, "bkg_decscale%s" %suf, True)
system('cp -f hist_zprime1000.root hist_bkg_decscale%s.root' %suf) ## use a dummy signal for the background only fit
jobSubmit('bkg_decscale%s' %suf)

# fine binning
fixFile('ttres_binning.config', 'ttres_bkg_binning%s.config' % suf, "bkg_binning%s" %suf, "bkg_binning%s" %suf, True)
system('cp -f hist_zprime1000.root hist_bkg_binning%s.root' %suf) ## use a dummy signal for the background only fit
jobSubmit('bkg_binning%s' %suf)

# fit tt norm in boosted
fixFile('ttres_boottnorm.config', 'ttres_bkg_boottnorm%s.config' % suf, "bkg_boottnorm%s" %suf, "bkg_boottnorm%s" %suf, True)
system('cp -f hist_zprime1000.root hist_bkg_boottnorm%s.root' %suf) ## use a dummy signal for the background only fit
jobSubmit('bkg_boottnorm%s' %suf)

# nnlo rew.
fixFile('ttres_nnlo.config', 'ttres_bkg_nnlo%s.config' % suf, "bkg_nnlo%s" %suf, "bkg_nnlo%s" %suf, True)
system('cp -f hist_zprime1000.root hist_bkg_nnlo%s.root' %suf) ## use a dummy signal for the background only fit
jobSubmit('bkg_nnlo%s' %suf)

# category only
#fixFile('ttres_cat3.config', 'ttres_bkg_cat3%s.config' % suf, "bkg_cat3%s" %suf, "bkg_cat3%s" %suf, True)
#system('cp -f hist_zprime1000.root hist_bkg_cat3%s.root' %suf) ## use a dummy signal for the background only fit
#jobSubmit('bkg_cat3%s' %suf)
#
#fixFile('ttres_cat2.config', 'ttres_bkg_cat2%s.config' % suf, "bkg_cat2%s" %suf, "bkg_cat2%s" %suf, True)
#system('cp -f hist_zprime1000.root hist_bkg_cat2%s.root' %suf) ## use a dummy signal for the background only fit
#jobSubmit('bkg_cat2%s' %suf)
#
#fixFile('ttres_cat1.config', 'ttres_bkg_cat1%s.config' % suf, "bkg_cat1%s" %suf, "bkg_cat1%s" %suf, True)
#system('cp -f hist_zprime1000.root hist_bkg_cat1%s.root' %suf) ## use a dummy signal for the background only fit
#jobSubmit('bkg_cat1%s' %suf)

## now go over to signal
#for t in signalList:
#  if "eft" in t:
#    continue
#  # veto reweighted KKG for now
#  if "kkg" in t and "w" in t:
#    continue
#  for i in signalList[t]:
#    if not ( 'zprime2000' in i or 'zprime3000' in i):
#      continue
#    # nominal
#    fixFile('ttres.config', 'ttres_%s%s.config' %(i, suf), i, "%s%s" % (i, suf), False)
#    jobSubmit("%s%s" % (i, suf))
#    # stat only
#    fixFile('ttres.config', 'ttres_%s%s_stat.config' %(i, suf), i, "%s%s_stat" % (i, suf), False)
#    jobSubmit("%s%s_stat" % (i, suf))
#    # ranking nominal
#    if 'zprime2000' in i or 'zprime3000' in i:
#      fixFile('ttres.config', 'ttres_%s%s_inj.config' %(i, suf), i, "%s%s_inj" % (i, suf), False)
#      jobSubmit("%s%s_inj" % (i, suf))
#
#    # fine binning
#    fixFile('ttres_binning.config', 'ttres_%s%s_binning.config' % (i, suf), i, "%s%s_binning" % (i, suf), False)
#    jobSubmit('%s%s_binning' % (i, suf))
#
#    # boosted tt norm
#    fixFile('ttres_boottnorm.config', 'ttres_%s%s_boottnorm.config' % (i, suf), i, "%s%s_boottnorm" % (i, suf), False)
#    jobSubmit('%s%s_boottnorm' % (i, suf))
#
#    # NNLO rew.
#    fixFile('ttres_nnlo.config', 'ttres_%s%s_nnlo.config' % (i, suf), i, "%s%s_nnlo" % (i, suf), False)
#    jobSubmit('%s%s_nnlo' % (i, suf))
#
## now KK gluon reweighted
#for t in signalList:
#  if "eft" in t:
#    continue
#  #if not ("kkg" in t and "w" in t):
#  if not ("kkg" in t and "w15" in t):
#    continue
#  for i in signalList[t]:
#    # nominal
#    fixFile('ttres.config', 'ttres_%s%s.config' %(i, suf), i, "%s%s" % (i, suf), False)
#    jobSubmit("%s%s" % (i, suf))
#    # stat only
#    fixFile('ttres.config', 'ttres_%s%s_stat.config' %(i, suf), i, "%s%s_stat" % (i, suf), False)
#    jobSubmit("%s%s_stat" % (i, suf))

