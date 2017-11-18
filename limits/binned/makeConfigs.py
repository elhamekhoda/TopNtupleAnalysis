#!/usr/bin/env python
from os import system,getcwd
from time import time
from inputs import *
import socket, random, re

# change those:
setdir = '/nfs/dust/atlas/user/danilo/topana2429'
mydir = '/nfs/dust/atlas/user/danilo/plots2/TRExFitter'

systlist = ["lumi", "akt4jes1", "akt4jes2", "akt4jes3", "akt4jes4", "akt4jes5", "akt4jes6", "akt4jespurho", "akt4jespuoffnpv", "akt4jespuoffmu", "akt4jespupt", "akt4bjes", "akt4jesetastat", "akt4jesetanc", "akt4jesetamod", "akt4jesfr", "akt4jesfchf", "akt4jesfclf", "akt4jespt", "akt4jessp", "akt4jer", "akt10model", "akt10baseline", "akt10track", "akt10stat", "metrespara", "metresperp", "metscale", "muresid", "muresms", "muscale", "eres", "escale", "etrig", "erec", "eid", "eiso", "mutrigstat", "mutrigsyst", "muidstat", "muidsyst", "muisolstat", "muisolsyst", "btagb0", "btagb1", "btagb2", "btagb3", "btagc0pt1", "btagc0pt2", "btagc0pt3", "btagc1", "btagc2", "btagc3", "btagl0pt1", "btagl0pt2", "btagl0pt3", "btagl1", "btagl2", "btagl3", "btagl4", "btagl5", "btagl6", "btagl7", "btagl8", "btagl9", "btagl10", "btage0", "btage1", "jvtsf", "pileupsf", "ttxsec", "singletop", "wbb", "wasym", "wl", "wmodel", "wc", "ttewk", "WtDRDS", "ttgen_boo", "ttgen_res", "ttps_res", "ttps_boo", "ttisrfsr_boo", "ttisrfsr_res", "qcde_res12c", "qcde_res3c", "qcde_res12f", "qcde_res3f", "qcde_boo12c", "qcde_boo3c", "qcde_boo12f", "qcde_boo3f", "qcdmu_res12", "qcdmu_res3", "qcdmu_boo12", "qcdmu_boo3", "akt10jerpt", "akt10jertau32", "akt10jermass", "wjpdf1", "wjpdf2", "wjpdf3", "wjpdf4", "wjpdf5", "wjpdf6", "wjpdf7", "wjpdf8", "wjpdf9", "wjpdf10", "wjpdf11", "wjpdf12", "wjpdf13", "wjpdf14", "wjpdf15", "wjpdf16", "wjpdf17", "wjpdf18", "wjpdf19", "wjpdf20", "wjpdf21", "wjpdf22", "wjpdf23", "wjpdf24", "wjpdf25", "wjpdf26", "wjpdf27", "wjpdf28", "wjpdf29", "wjpdf30", "wjpdf31", "wjpdf32", "wjpdf33", "wjpdf34", "wjpdf35", "wjpdf36", "wjpdf37", "wjpdf38", "wjpdf39", "wjpdf40", "wjpdf41", "wjpdf42", "wjpdf43", "wjpdf44", "wjpdf45", "wjpdf46", "wjpdf47", "wjpdf48", "wjpdf49", "wjpdf50", "wjpdf51", "wjpdf52", "wjpdf53", "wjpdf54", "wjpdf55", "wjpdf56", "wjpdf57", "wjpdf58", "wjpdf59", "wjpdf60", "wjpdf61", "wjpdf62", "wjpdf63", "wjpdf64", "wjpdf65", "wjpdf66", "wjpdf67", "wjpdf68", "wjpdf69", "wjpdf70", "wjpdf71", "wjpdf72", "wjpdf73", "wjpdf74", "wjpdf75", "wjpdf76", "wjpdf77", "wjpdf78", "wjpdf79", "wjpdf80", "wjpdf81", "wjpdf82", "wjpdf83", "wjpdf84", "wjpdf85", "wjpdf86", "wjpdf87", "wjpdf88", "wjpdf89", "wjpdf90", "wjpdf91", "wjpdf92", "wjpdf93", "wjpdf94", "wjpdf95", "wjpdf96", "wjpdf97", "wjpdf98", "wjpdf99", "wjpdf100", "ttpdf0", "ttpdf1", "ttpdf2", "ttpdf3", "ttpdf4", "ttpdf5", "ttpdf6", "ttpdf7", "ttpdf8", "ttpdf9", "ttpdf10", "ttpdf11", "ttpdf12", "ttpdf13", "ttpdf14", "ttpdf15", "ttpdf16", "ttpdf17", "ttpdf18", "ttpdf19", "ttpdf20", "ttpdf21", "ttpdf22", "ttpdf23", "ttpdf24", "ttpdf25", "ttpdf26", "ttpdf27", "ttpdf28", "ttpdf29", "ttpdf30"]
#systlist = []
#systlist += ['WtDRDS', 'akt10baseline', 'akt10jertau32', 'akt10jermass', 'akt10jerpt', 'akt10model', 'akt10track']
#systlist += ['akt4jer', 'akt4jes1', 'akt4jes2', 'akt4jesetamod', 'akt4jesetanc', 'akt4jesetastat', 'akt4jesfchf', 'akt4jesfclf', 'akt4jesfr', 'akt4jespuoffmu', 'akt4jespuoffnpv', 'akt4jespupt', 'akt4jespurho']
#systlist += ['btagb0', 'btagb1', 'btagc0pt1', 'btagc0pt2', 'btagc0pt3', 'btagc1', 'btagc2', 'btagc3', 'btagl0pt1', 'btagl0pt2', 'btagl0pt3', 'btagl2', 'btagl3', 'btagl4']
#systlist += ['lumi', 'metrespara', 'metresperp', 'metscale', 'pileupsf']
#systlist += ['qcde_boo12c', 'qcde_boo12f', 'qcde_boo3c', 'qcde_boo3f', 'qcde_res12c', 'qcde_res12f', 'qcde_res3c', 'qcde_res3f', 'qcdmu_boo12', 'qcdmu_boo3', 'qcdmu_res12', 'qcdmu_res3']
#systlist += ['singletop', 'ttgen_boo', 'ttisrfsr_boo', 'ttisrfsr_res', 'ttps_boo', 'ttps_res', 'ttxsec', 'wasym', 'wbb', 'wc', 'wl']
#systlist += ['wjpdf%d' % x for x in [12,16,19,20,3,33,34,35,37,4,42,43,49,5,53,56,57,61,62,63,71,75,77,78,8,83,89,93,94,95]]

def fixFile(template, final, sig, dirname, doBOnlyFit):
  fr = open(template, 'r')
  f = open(final, 'w')

  sigxsec = 1
  #for t in signalList:
  #  length = len(xs[t])
  #  for I in range(0,length):
  #    if sig == signalList[t][I]:
  #      extra_factor = 1
  #      if 'kkg' in sig and 'w' in sig:
  #        name = sig.split('w')[0]
  #        width = sig.split('w')[1]
  #        extra_factor = xs['kkgluon'][I]/xs['kkgluonw'+width][I]
  #      sigxsec = xs[t][I]*extra_factor
  #      break

  beginSysts = False
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
    if 'Ttres' in nline and not "TtresSmoothing" in nline:
      nline = nline.replace('Ttres', 'Ttres_'+dirname)
    if 'HistoPath' in line:
      nline = '  HistoPath: "/nfs/dust/atlas/user/danilo/plots2/TRExFitter/hists_15ifb/"\n'
    if 'LumiLabel' in line:
      nline = '  LumiLabel: "15 fb^{-1}"\n'
    if 'SystControlPlots' in nline: # and ((not doBOnlyFit) or 'cat' in dirname):
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
	fr.close()
	if not ('stat' in suf or 'binning' in suf or 'nnlo' in suf) and ('zprime2000' in suf or 'zprime3000' in suf):
		split_number = 5
		r_number = int(len(systlist)/split_number)
		for ri in range(0, split_number+1):
			runfile_r = 'submit_%s%s_rank%d.sh' % (suf, extra, ri)
			logfile_r = mydir+'/stdout_%s%s_rank%d.txt'%(suf, extra, ri)
			jobName_r = 'ttlim_%s%s_rank%d'%(suf, extra, ri)
			frr = open(runfile_r, 'w')
			frr.write('#!/bin/sh\n')
			#frr.write('#$ -cwd\n')
			frr.write('#$ -j y\n')
			frr.write('#$ -l cvmfs\n')
			#frr.write('#$ -l distro=sld6\n')
			frr.write('#$ -l distro=el7\n')
			frr.write('#$ -l arch=amd64\n')
			frr.write('#$ -l h_vmem=35G\n')
			frr.write('#$ -o '+logfile_r+'\n')
			frr.write('#$ -q '+queue+'\n')
			frr.write('#$ -m '+'eas'+'\n')
			frr.write('#$ -M '+email+'\n')
			frr.write('#$ -N '+jobName_r+'\n')
			frr.write('cd '+setdir+'\n')
			frr.write('export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase\n')
			frr.write('export DQ2_LOCAL_SITE_ID=DESY-HH_SCRATCHDISK \n')
			frr.write('source /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/user/atlasLocalSetup.sh\n')
			frr.write('lsetup rcsetup\n')
			frr.write('cd '+mydir+'\n')
			for r_item in range(ri*r_number, min(ri*r_number + r_number, len(systlist))):
				sitem = systlist[r_item]
				frr.write('./myFit.exe r ttres_%s.config Ranking=%s\n'%(suf, sitem))
			system('chmod a+x %s'%runfile_r)
	system('chmod a+x %s'%runfile)
	print("Running %s" % runfile)
	system('qsub %s'%runfile)
	#system('./%s > %s 2>&1 '% (runfile, logfile))
	#import time
	#time.sleep(40*60)


# B ONLY fit
#suf = "lowbins"
#suf = "s290"
#suf = "smoothsqrt"
#suf = "smoothjer"
suf = ""
import sys
if len(sys.argv) > 1:
  suf = sys.argv[1]

# fit tt norm in boosted

mydirin = "hists_15ifb"
#mydirin = "."

fixFile('ttres_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32_topptnnlo.config', 'ttres_bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32_topptnnlo%s.config' % suf, "bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32_topptnnlo%s" %suf, "bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32_topptnnlo%s" %suf, True)
system('cp -f hist_zprime1000.root %s/hist_bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32_topptnnlo%s.root' %(mydirin,suf)) ## use a dummy signal for the background only fit
jobSubmit('bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32_topptnnlo%s' %suf)

#fixFile('ttres_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32_lqcd.config', 'ttres_bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32_lqcd%s.config' % suf, "bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32_lqcd%s" %suf, "bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32_lqcd%s" %suf, True)
#system('cp -f hist_zprime1000.root %s/hist_bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32_lqcd%s.root' %(mydirin,suf)) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32_lqcd%s' %suf)

#fixFile('ttres_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32_freew.config', 'ttres_bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32_freew%s.config' % suf, "bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32_freew%s" %suf, "bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32_freew%s" %suf, True)
#system('cp -f hist_zprime1000.root %s/hist_bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32_freew%s.root' %(mydirin,suf)) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32_freew%s' %suf)

#fixFile('ttres_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32.config', 'ttres_bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32%s.config' % suf, "bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32%s" %suf, "bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32%s" %suf, True)
#system('cp -f hist_zprime1000.root %s/hist_bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32%s.root' %(mydirin,suf)) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32%s' %suf)

#fixFile('ttres_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero.config', 'ttres_bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero%s.config' % suf, "bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero%s" %suf, "bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero%s" %suf, True)
#system('cp -f hist_zprime1000.root %s/hist_bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero%s.root' %(mydirin,suf)) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero%s' %suf)

#fixFile('ttres_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32_asimov.config', 'ttres_bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32_asimov%s.config' % suf, "bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32_asimov%s" %suf, "bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32_asimov%s" %suf, True)
#system('cp -f hist_zprime1000.root %s/hist_bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32_asimov%s.root' %(mydirin,suf)) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_dectau32_asimov%s' %suf)

#fixFile('ttres_boottnorm_smooth3nnlottpspp8mbinsnottgen.config', 'ttres_bkg_boottnorm_smooth3nnlottpspp8mbinsnottgen%s.config' % (suf), "bkg_boottnorm_smooth3nnlottpspp8mbinsnottgen%s" % suf, "bkg_boottnorm_smooth3nnlottpspp8mbinsnottgen%s" % (suf), True)
#system('cp -f hist_zprime1000.root %s/hist_bkg_boottnorm_smooth3nnlottpspp8mbinsnottgen%s.root' %(mydirin,suf)) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_smooth3nnlottpspp8mbinsnottgen%s' % (suf))
#
#fixFile('ttres_boottnorm_smooth3nnlottpspp8mbins.config', 'ttres_bkg_boottnorm_smooth3nnlottpspp8mbins%s.config' % (suf), "bkg_boottnorm_smooth3nnlottpspp8mbins%s" % suf, "bkg_boottnorm_smooth3nnlottpspp8mbins%s" % (suf), True)
#system('cp -f hist_zprime1000.root %s/hist_bkg_boottnorm_smooth3nnlottpspp8mbins%s.root' %(mydirin,suf)) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_smooth3nnlottpspp8mbins%s' % (suf))

#fixFile('ttres_boottnorm_smooth3.config', 'ttres_bkg_boottnorm_smooth3%s.config' % suf, "bkg_boottnorm_smooth3%s" %suf, "bkg_boottnorm_smooth3%s" %suf, True)
#system('cp -f hist_zprime1000.root %s/hist_bkg_boottnorm_smooth3%s.root' %(mydirin,suf)) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_smooth3%s' %suf)

#fixFile('ttres_boottnorm_smooth2ttpspp8.config', 'ttres_bkg_boottnorm_smooth2ttpspp8%s.config' % suf, "bkg_boottnorm_smooth2ttpspp8%s"%suf, "bkg_boottnorm_smooth2ttpspp8%s" % suf, True)
#jobSubmit('bkg_boottnorm_smooth2ttpspp8%s' % suf)

#fixFile('ttres_boottnorm_partial.config', 'ttres_bkg_boottnorm_partial%s.config' % suf, "bkg_boottnorm_partial%s" %suf, "bkg_boottnorm_partial%s" %suf, True)
#system('cp -f hist_zprime1000.root %s/hist_bkg_boottnorm_partial%s.root' %(mydirin,suf)) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_partial%s' %suf)

#fixFile('ttres_boottnorm_smooth2ttpspp8mbins.config', 'ttres_bkg_boottnorm_smooth2ttpspp8mbins%s.config' % suf, "bkg_boottnorm_smooth2ttpspp8mbins%s" %suf, "bkg_boottnorm_smooth2ttpspp8mbins%s" %suf, True)
#system('cp -f hist_zprime1000.root %s/hist_bkg_boottnorm_smooth2ttpspp8mbins%s.root' %(mydirin,suf)) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_smooth2ttpspp8mbins%s' %suf)

#fixFile('ttres_boottnorm_smooth2.config', 'ttres_bkg_boottnorm_smooth2%s.config' % suf, "bkg_boottnorm_smooth2%s" %suf, "bkg_boottnorm_smooth2%s" %suf, True)
#system('cp -f hist_zprime1000.root %s/hist_bkg_boottnorm_smooth2%s.root' %(mydirin,suf)) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_smooth2%s' %suf)
#
#fixFile('ttres_boottnorm_smooth2_asimov.config', 'ttres_bkg_boottnorm_smooth2_asimov%s.config' % suf, "bkg_boottnorm_smooth2_asimov%s" %suf, "bkg_boottnorm_smooth2_asimov%s" %suf, True)
#system('cp -f hist_zprime1000.root %s/hist_bkg_boottnorm_smooth2_asimov%s.root' %(mydirin,suf)) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_smooth2_asimov%s' %suf)
#
#
#fixFile('ttres_boottnorm_smooth2nnlottpspp8mbins.config', 'ttres_bkg_boottnorm_smooth2nnlottpspp8mbins%s.config' % suf, "bkg_boottnorm_smooth2nnlottpspp8mbins%s" %suf, "bkg_boottnorm_smooth2nnlottpspp8mbins%s" %suf, True)
#system('cp -f hist_zprime1000.root %s/hist_bkg_boottnorm_smooth2nnlottpspp8mbins%s.root' %(mydirin,suf)) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_smooth2nnlottpspp8mbins%s' %suf)
#
#fixFile('ttres_boottnorm_smooth2nnlottpspp8mbins_asimov.config', 'ttres_bkg_boottnorm_smooth2nnlottpspp8mbins_asimov%s.config' % suf, "bkg_boottnorm_smooth2nnlottpspp8mbins_asimov%s" %suf, "bkg_boottnorm_smooth2nnlottpspp8mbins_asimov%s" %suf, True)
#system('cp -f hist_zprime1000.root %s/hist_bkg_boottnorm_smooth2nnlottpspp8mbins_asimov%s.root' %(mydirin,suf)) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_smooth2nnlottpspp8mbins_asimov%s' %suf)

#fixFile('ttres_boottnorm_smooth2nnlottpspp8mbinsqcdavg.config', 'ttres_bkg_boottnorm_smooth2nnlottpspp8mbinsqcdavg%s.config' % suf, "bkg_boottnorm_smooth2nnlottpspp8mbinsqcdavg%s" %suf, "bkg_boottnorm_smooth2nnlottpspp8mbinsqcdavg%s" %suf, True)
#system('cp -f hist_zprime1000.root %s/hist_bkg_boottnorm_smooth2nnlottpspp8mbinsqcdavg%s.root' %(mydirin,suf)) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_smooth2nnlottpspp8mbinsqcdavg%s' %suf)
#
#fixFile('ttres_boottnorm_smooth2nnlottpspp8mbinsqcdavg_asimov.config', 'ttres_bkg_boottnorm_smooth2nnlottpspp8mbinsqcdavg_asimov%s.config' % suf, "bkg_boottnorm_smooth2nnlottpspp8mbinsqcdavg_asimov%s" %suf, "bkg_boottnorm_smooth2nnlottpspp8mbinsqcdavg_asimov%s" %suf, True)
#system('cp -f hist_zprime1000.root %s/hist_bkg_boottnorm_smooth2nnlottpspp8mbinsqcdavg_asimov%s.root' %(mydirin,suf)) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_smooth2nnlottpspp8mbinsqcdavg_asimov%s' %suf)


#fixFile('ttres_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero.config', 'ttres_bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero%s.config' % suf, "bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero%s" %suf, "bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero%s" %suf, True)
#system('cp -f hist_zprime1000.root %s/hist_bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero%s.root' %(mydirin,suf)) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero%s' %suf)
#
#fixFile('ttres_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_asimov.config', 'ttres_bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_asimov%s.config' % suf, "bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_asimov%s" %suf, "bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_asimov%s" %suf, True)
#system('cp -f hist_zprime1000.root %s/hist_bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_asimov%s.root' %(mydirin,suf)) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero_asimov%s' %suf)


#######

#fixFile('ttres_boottnorm_smooth2qcdsmooth.config', 'ttres_bkg_boottnorm_smooth2qcdsmooth%s.config' % suf, "bkg_boottnorm_smooth2qcdsmooth%s" %suf, "bkg_boottnorm_smooth2qcdsmooth%s" %suf, True)
#system('cp -f hist_zprime1000.root %s/hist_bkg_boottnorm_smooth2qcdsmooth%s.root' %(mydirin,suf)) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_smooth2qcdsmooth%s' %suf)
#
#fixFile('ttres_boottnorm_smooth2qcdshape.config', 'ttres_bkg_boottnorm_smooth2qcdshape%s.config' % suf, "bkg_boottnorm_smooth2qcdshape%s" %suf, "bkg_boottnorm_smooth2qcdshape%s" %suf, True)
#system('cp -f hist_zprime1000.root %s/hist_bkg_boottnorm_smooth2qcdshape%s.root' %(mydirin,suf)) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_smooth2qcdshape%s' %suf)


#fixFile('ttres_boottnorm_smooth2psold.config', 'ttres_bkg_boottnorm_smooth2psold%s.config' % suf, "bkg_boottnorm_smooth2psold%s" %suf, "bkg_boottnorm_smooth2psold%s" %suf, True)
#system('cp -f hist_zprime1000.root hist_bkg_boottnorm_smooth2psold%s.root' %suf) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_smooth2psold%s' %suf)
#
#fixFile('ttres_boottnorm_smooth2psold_asimov.config', 'ttres_bkg_boottnorm_smooth2psold_asimov%s.config' % suf, "bkg_boottnorm_smooth2psold_asimov%s" %suf, "bkg_boottnorm_smooth2psold_asimov%s" %suf, True)
#system('cp -f hist_zprime1000.root hist_bkg_boottnorm_smooth2psold_asimov%s.root' %suf) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_smooth2psold_asimov%s' %suf)


#fixFile('ttres_boottnorm_smooth2mbins.config', 'ttres_bkg_boottnorm_smooth2mbins%s.config' % suf, "bkg_boottnorm_smooth2mbins%s" %suf, "bkg_boottnorm_smooth2mbins%s" %suf, True)
#system('cp -f hist_zprime1000.root hist_bkg_boottnorm_smooth2mbins%s.root' %suf) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_smooth2mbins%s' %suf)
#
#fixFile('ttres_boottnorm_smooth2mbins_asimov.config', 'ttres_bkg_boottnorm_smooth2mbins_asimov%s.config' % suf, "bkg_boottnorm_smooth2mbins_asimov%s" %suf, "bkg_boottnorm_smooth2mbins_asimov%s" %suf, True)
#system('cp -f hist_zprime1000.root hist_bkg_boottnorm_smooth2mbins_asimov%s.root' %suf) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_smooth2mbins_asimov%s' %suf)



#fixFile('ttres_boottnorm.config', 'ttres_bkg_boottnorm%s.config' % suf, "bkg_boottnorm%s" %suf, "bkg_boottnorm%s" %suf, True)
#system('cp -f hist_zprime1000.root hist_bkg_boottnorm%s.root' %suf) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm%s' %suf)

#fixFile('ttres_boottnorm_psold.config', 'ttres_bkg_boottnorm_psold%s.config' % suf, "bkg_boottnorm_psold%s" %suf, "bkg_boottnorm_psold%s" %suf, True)
#system('cp -f hist_zprime1000.root hist_bkg_boottnorm_psold%s.root' %suf) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_psold%s' %suf)

#fixFile('ttres_boottnorm_asimov.config', 'ttres_bkg_boottnorm_asimov%s.config' % suf, "bkg_boottnorm_asimov%s" %suf, "bkg_boottnorm_asimov%s" %suf, True)
#system('cp -f hist_zprime1000.root hist_bkg_boottnorm_asimov%s.root' %suf) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_asimov%s' %suf)
#
#fixFile('ttres_boottnorm_psold_asimov.config', 'ttres_bkg_boottnorm_psold_asimov%s.config' % suf, "bkg_boottnorm_psold_asimov%s" %suf, "bkg_boottnorm_psold_asimov%s" %suf, True)
#system('cp -f hist_zprime1000.root hist_bkg_boottnorm_psold_asimov%s.root' %suf) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_psold_asimov%s' %suf)


#fixFile('ttres_boottnorm_cat3.config', 'ttres_bkg_boottnorm_cat3%s.config' % suf, "bkg_boottnorm_cat3%s" %suf, "bkg_boottnorm_cat3%s" %suf, True)
#system('cp -f hist_zprime1000.root hist_bkg_boottnorm_cat3%s.root' %suf) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_cat3%s' %suf)
#
#fixFile('ttres_boottnorm_cat2.config', 'ttres_bkg_boottnorm_cat2%s.config' % suf, "bkg_boottnorm_cat2%s" %suf, "bkg_boottnorm_cat2%s" %suf, True)
#system('cp -f hist_zprime1000.root hist_bkg_boottnorm_cat2%s.root' %suf) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_cat2%s' %suf)
#
#fixFile('ttres_boottnorm_cat1.config', 'ttres_bkg_boottnorm_cat1%s.config' % suf, "bkg_boottnorm_cat1%s" %suf, "bkg_boottnorm_cat1%s" %suf, True)
#system('cp -f hist_zprime1000.root hist_bkg_boottnorm_cat1%s.root' %suf) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnorm_cat1%s' %suf)


#fixFile('ttres_boottnormlowbins.config', 'ttres_bkg_boottnormlowbins%s.config' % suf, "bkg_boottnormlowbins%s" %suf, "bkg_boottnormlowbins%s" %suf, True)
#system('cp -f hist_zprime1000.root hist_bkg_boottnormlowbins%s.root' %suf) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnormlowbins%s' %suf)

#fixFile('ttres_boottnormlowbins1.config', 'ttres_bkg_boottnormlowbins1%s.config' % suf, "bkg_boottnormlowbins1%s" %suf, "bkg_boottnormlowbins1%s" %suf, True)
#system('cp -f hist_zprime500.root hist_bkg_boottnormlowbins1%s.root' %suf) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnormlowbins1%s' %suf)

#fixFile('ttres_boottnormlowbins_isrfsrcorr.config', 'ttres_bkg_boottnormlowbins_isrfsrcorr%s.config' % suf, "bkg_boottnormlowbins_isrfsrcorr%s" %suf, "bkg_boottnormlowbins_isrfsrcorr%s" %suf, True)
#system('cp -f hist_zprime1000.root hist_bkg_boottnormlowbins_isrfsrcorr%s.root' %suf) ## use a dummy signal for the background only fit
#jobSubmit('bkg_boottnormlowbins_isrfsrcorr%s' %suf)


'''
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

# decorrelate generator and ISR/FSR between boosted and resolved
fixFile('ttres_decgenscale.config', 'ttres_bkg_decgenscale%s.config' % suf, "bkg_decgenscale%s" %suf, "bkg_decgenscale%s" %suf, True)
system('cp -f hist_zprime1000.root hist_bkg_decgenscale%s.root' %suf) ## use a dummy signal for the background only fit
jobSubmit('bkg_decgenscale%s' %suf)

# correlate generator and ISR/FSR between boosted and resolved
fixFile('ttres_corrgenscale.config', 'ttres_bkg_corrgenscale%s.config' % suf, "bkg_corrgenscale%s" %suf, "bkg_corrgenscale%s" %suf, True)
system('cp -f hist_zprime1000.root hist_bkg_corrgenscale%s.root' %suf) ## use a dummy signal for the background only fit
jobSubmit('bkg_corrgenscale%s' %suf)

# fine binning
fixFile('ttres_binning.config', 'ttres_bkg_binning%s.config' % suf, "bkg_binning%s" %suf, "bkg_binning%s" %suf, True)
system('cp -f hist_zprime1000.root hist_bkg_binning%s.root' %suf) ## use a dummy signal for the background only fit
jobSubmit('bkg_binning%s' %suf)

# nnlo rew.
fixFile('ttres_nnlo.config', 'ttres_bkg_nnlo%s.config' % suf, "bkg_nnlo%s" %suf, "bkg_nnlo%s" %suf, True)
system('cp -f hist_zprime1000.root hist_bkg_nnlo%s.root' %suf) ## use a dummy signal for the background only fit
jobSubmit('bkg_nnlo%s' %suf)

# boosted free norm + nnlo rew.
fixFile('ttres_nnlo_boottnorm.config', 'ttres_bkg_nnlo_boottnorm%s.config' % suf, "bkg_nnlo_boottnorm%s" %suf, "bkg_nnlo_boottnorm%s" %suf, True)
system('cp -f hist_zprime1000.root hist_bkg_nnlo_boottnorm%s.root' %suf) ## use a dummy signal for the background only fit
jobSubmit('bkg_nnlo_boottnorm%s' %suf)

# category only
fixFile('ttres_cat3.config', 'ttres_bkg_cat3%s.config' % suf, "bkg_cat3%s" %suf, "bkg_cat3%s" %suf, True)
system('cp -f hist_zprime1000.root hist_bkg_cat3%s.root' %suf) ## use a dummy signal for the background only fit
jobSubmit('bkg_cat3%s' %suf)

fixFile('ttres_cat2.config', 'ttres_bkg_cat2%s.config' % suf, "bkg_cat2%s" %suf, "bkg_cat2%s" %suf, True)
system('cp -f hist_zprime1000.root hist_bkg_cat2%s.root' %suf) ## use a dummy signal for the background only fit
jobSubmit('bkg_cat2%s' %suf)

fixFile('ttres_cat1.config', 'ttres_bkg_cat1%s.config' % suf, "bkg_cat1%s" %suf, "bkg_cat1%s" %suf, True)
system('cp -f hist_zprime1000.root hist_bkg_cat1%s.root' %suf) ## use a dummy signal for the background only fit
jobSubmit('bkg_cat1%s' %suf)

'''
# now go over to signal
for t in signalList:
  if "eft" in t:
    continue
  if not ('zprime' in t):
    continue
  # veto reweighted KKG for now
  if "kkg" in t and "w" in t:
    continue
  for i in []: #['zprime400', 'zprime1000']: #signalList[t]:
    fixFile('ttres_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero.config', 'ttres_%s%s_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero.config' % (i, suf), i, "%s%s_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero" % (i, suf), False)
    jobSubmit('%s%s_boottnorm_smooth2nnlottpspp8mbinsqcdfixzero' % (i, suf))

    #fixFile('ttres_boottnorm_smooth2nnlottpspp8mbins.config', 'ttres_%s%s_boottnorm_smooth2nnlottpspp8mbins.config' % (i, suf), i, "%s%s_boottnorm_smooth2nnlottpspp8mbins" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2nnlottpspp8mbins' % (i, suf))



    #fixFile('ttres_boottnorm_smooth2nnlottpspp8mbinsmerge_asimov.config', 'ttres_%s%s_boottnorm_smooth2nnlottpspp8mbinsmerge_asimov.config' % (i, suf), i, "%s%s_boottnorm_smooth2nnlottpspp8mbinsmergei_asimov" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2nnlottpspp8mbinsmerge_asimov' % (i, suf))

    #fixFile('ttres_boottnorm_smooth2ttpspp8mbinsmerge.config', 'ttres_%s%s_boottnorm_smooth2ttpspp8mbinsmerge.config' % (i, suf), i, "%s%s_boottnorm_smooth2ttpspp8mbinsmerge" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2ttpspp8mbinsmerge' % (i, suf))




    #fixFile('ttres_boottnorm_smooth2.config', 'ttres_%s%s_boottnorm_smooth2.config' % (i, suf), i, "%s%s_boottnorm_smooth2" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2' % (i, suf))

    #fixFile('ttres_boottnorm_smooth2qcdsmooth.config', 'ttres_%s%s_boottnorm_smooth2qcdsmooth.config' % (i, suf), i, "%s%s_boottnorm_smooth2qcdsmooth" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2qcdsmooth' % (i, suf))

    #fixFile('ttres_boottnorm_smooth2nnlottpspp8mbins.config', 'ttres_%s%s_boottnorm_smooth2nnlottpspp8mbins.config' % (i, suf), i, "%s%s_boottnorm_smooth2nnlottpspp8mbins" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2nnlottpspp8mbins' % (i, suf))


    #fixFile('ttres_boottnorm_smooth2nnlottpspp8mbinsmerge2.config', 'ttres_%s%s_boottnorm_smooth2nnlottpspp8mbinsmerge2.config' % (i, suf), i, "%s%s_boottnorm_smooth2nnlottpspp8mbinsmerge2" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2nnlottpspp8mbinsmerge2' % (i, suf))

    #fixFile('ttres_boottnorm_smooth2nnlottpspp8mbinsqcdavg.config', 'ttres_%s%s_boottnorm_smooth2nnlottpspp8mbinsqcdavg.config' % (i, suf), i, "%s%s_boottnorm_smooth2nnlottpspp8mbinsqcdavg" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2nnlottpspp8mbinsqcdavg' % (i, suf))

    #fixFile('ttres_boottnorm_smooth2nnlottpspp8mbinsqcdavglerr.config', 'ttres_%s%s_boottnorm_smooth2nnlottpspp8mbinsqcdavglerr.config' % (i, suf), i, "%s%s_boottnorm_smooth2nnlottpspp8mbinsqcdavglerr" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2nnlottpspp8mbinsqcdavglerr' % (i, suf))

    #fixFile('ttres_boottnorm_smooth2nnlombins.config', 'ttres_%s%s_boottnorm_smooth2nnlombins.config' % (i, suf), i, "%s%s_boottnorm_smooth2nnlombins" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2nnlombins' % (i, suf))

    #fixFile('ttres_boottnorm_smooth2nnlombins2.config', 'ttres_%s%s_boottnorm_smooth2nnlombins2.config' % (i, suf), i, "%s%s_boottnorm_smooth2nnlombins2" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2nnlombins2' % (i, suf))

    #fixFile('ttres_boottnorm_smooth2nnlottpspp8.config', 'ttres_%s%s_boottnorm_smooth2nnlottpspp8.config' % (i, suf), i, "%s%s_boottnorm_smooth2nnlottpspp8" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2nnlottpspp8' % (i, suf))

    #fixFile('ttres_boottnorm_smooth2qcdshape.config', 'ttres_%s%s_boottnorm_smooth2qcdshape.config' % (i, suf), i, "%s%s_boottnorm_smooth2qcdshape" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2qcdshape' % (i, suf))

    #fixFile('ttres_boottnorm_smooth2ttpspp8.config', 'ttres_%s%s_boottnorm_smooth2ttpspp8.config' % (i, suf), i, "%s%s_boottnorm_smooth2ttpspp8" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2ttpspp8' % (i, suf))


    #if i == 'zprime400':
    #  fixFile('ttres_boottnorm_smooth2_asimov.config', 'ttres_%s%s_boottnorm_smooth2_asimov_inj.config' %(i, suf), i, "%s%s_boottnorm_smooth2_asimov_inj" % (i, suf), False)
    #  jobSubmit("%s%s_boottnorm_smooth2_asimov_inj" % (i, suf))






    #fixFile('ttres_boottnorm_smooth2testNosmooth.config', 'ttres_%s%s_boottnorm_smooth2testNosmooth.config' % (i, suf), i, "%s%s_boottnorm_smooth2testNosmooth" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2testNosmooth' % (i, suf))

    #fixFile('ttres_boottnorm_smooth2test.config', 'ttres_%s%s_boottnorm_smooth2test.config' % (i, suf), i, "%s%s_boottnorm_smooth2test" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2test' % (i, suf))

    #fixFile('ttres_boottnorm_smooth2mbins.config', 'ttres_%s%s_boottnorm_smooth2mbins.config' % (i, suf), i, "%s%s_boottnorm_smooth2mbins" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2mbins' % (i, suf))

    #fixFile('ttres_boottnorm_smooth2qcdsmooth.config', 'ttres_%s%s_boottnorm_smooth2qcdsmooth.config' % (i, suf), i, "%s%s_boottnorm_smooth2qcdsmooth" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2qcdsmooth' % (i, suf))

    #fixFile('ttres_boottnorm_smooth2ttpspp8_cat3.config', 'ttres_%s%s_boottnorm_smooth2ttpspp8_cat3.config' % (i, suf), i, "%s%s_boottnorm_smooth2ttpspp8_cat3" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2ttpspp8_cat3' % (i, suf))

    #fixFile('ttres_boottnorm_smooth2ttpspp8_cat2.config', 'ttres_%s%s_boottnorm_smooth2ttpspp8_cat2.config' % (i, suf), i, "%s%s_boottnorm_smooth2ttpspp8_cat2" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2ttpspp8_cat2' % (i, suf))

    #fixFile('ttres_boottnorm_smooth2ttpspp8_cat1.config', 'ttres_%s%s_boottnorm_smooth2ttpspp8_cat1.config' % (i, suf), i, "%s%s_boottnorm_smooth2ttpspp8_cat1" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2ttpspp8_cat1' % (i, suf))

    #fixFile('ttres_boottnorm_smooth2ttpspp8_test.config', 'ttres_%s%s_boottnorm_smooth2ttpspp8_test.config' % (i, suf), i, "%s%s_boottnorm_smooth2ttpspp8_test" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2ttpspp8_test' % (i, suf))


    #fixFile('ttres_boottnorm_smooth2nnlo.config', 'ttres_%s%s_boottnorm_smooth2nnlo.config' % (i, suf), i, "%s%s_boottnorm_smooth2nnlo" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2nnlo' % (i, suf))


    #fixFile('ttres_boottnorm_smooth2qcdFrom1.config', 'ttres_%s%s_boottnorm_smooth2qcdFrom1.config' % (i, suf), i, "%s%s_boottnorm_smooth2qcdFrom1" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2qcdFrom1' % (i, suf))

    #fixFile('ttres_boottnorm_smooth2_cat1.config', 'ttres_%s%s_boottnorm_smooth2_cat1.config' % (i, suf), i, "%s%s_boottnorm_smooth2_cat1" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2_cat1' % (i, suf))
    #fixFile('ttres_boottnorm_smooth2_cat2.config', 'ttres_%s%s_boottnorm_smooth2_cat2.config' % (i, suf), i, "%s%s_boottnorm_smooth2_cat2" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2_cat2' % (i, suf))
    #fixFile('ttres_boottnorm_smooth2_cat3.config', 'ttres_%s%s_boottnorm_smooth2_cat3.config' % (i, suf), i, "%s%s_boottnorm_smooth2_cat3" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2_cat3' % (i, suf))

    #fixFile('ttres_boottnorm_smooth2.config', 'ttres_%s%s_boottnorm_smooth2.config' % (i, suf), i, "%s%s_boottnorm_smooth2" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2' % (i, suf))

    #fixFile('ttres_boottnorm_smooth2e.config', 'ttres_%s%s_boottnorm_smooth2e.config' % (i, suf), i, "%s%s_boottnorm_smooth2e" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2e' % (i, suf))

    #fixFile('ttres_boottnorm_smooth2mu.config', 'ttres_%s%s_boottnorm_smooth2mu.config' % (i, suf), i, "%s%s_boottnorm_smooth2mu" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2mu' % (i, suf))

    #fixFile('ttres_boottnorm_smooth2psold.config', 'ttres_%s%s_boottnorm_smooth2psold.config' % (i, suf), i, "%s%s_boottnorm_smooth2psold" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2psold' % (i, suf))





    #fixFile('ttres_boottnorm_psold.config', 'ttres_%s%s_boottnorm_psold.config' % (i, suf), i, "%s%s_boottnorm_psold" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_psold' % (i, suf))

    ## nominal
    #fixFile('ttres.config', 'ttres_%s%s.config' %(i, suf), i, "%s%s" % (i, suf), False)
    #jobSubmit("%s%s" % (i, suf))
    ## stat only
    #fixFile('ttres.config', 'ttres_%s%s_stat.config' %(i, suf), i, "%s%s_stat" % (i, suf), False)
    #jobSubmit("%s%s_stat" % (i, suf))
    ## ranking nominal
    #if 'zprime2000' in i or 'zprime3000' in i:
    #  fixFile('ttres.config', 'ttres_%s%s_inj.config' %(i, suf), i, "%s%s_inj" % (i, suf), False)
    #  jobSubmit("%s%s_inj" % (i, suf))

    ## boosted tt norm
    #fixFile('ttres_boottnorm.config', 'ttres_%s%s_boottnorm.config' % (i, suf), i, "%s%s_boottnorm" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm' % (i, suf))

    #fixFile('ttres_boottnorm_smooth2dectau32.config', 'ttres_%s%s_boottnorm_smooth2dectau32.config' % (i, suf), i, "%s%s_boottnorm_smooth2dectau32" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2dectau32' % (i, suf))

    #fixFile('ttres_boottnorm_smooth2lessbins.config', 'ttres_%s%s_boottnorm_smooth2lessbins.config' % (i, suf), i, "%s%s_boottnorm_smooth2lessbins" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2lessbins' % (i, suf))
    
    #fixFile('ttres_boottnorm_smooth2res.config', 'ttres_%s%s_boottnorm_smooth2res.config' % (i, suf), i, "%s%s_boottnorm_smooth2res" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2res' % (i, suf))

    #fixFile('ttres_boottnorm_smooth2boo.config', 'ttres_%s%s_boottnorm_smooth2boo.config' % (i, suf), i, "%s%s_boottnorm_smooth2boo" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2boo' % (i, suf))

    #fixFile('ttres_boottnorm_smooth2r1.config', 'ttres_%s%s_boottnorm_smooth2r1.config' % (i, suf), i, "%s%s_boottnorm_smooth2r1" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2r1' % (i, suf))
    #fixFile('ttres_boottnorm_smooth2r2.config', 'ttres_%s%s_boottnorm_smooth2r2.config' % (i, suf), i, "%s%s_boottnorm_smooth2r2" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2r2' % (i, suf))
    #fixFile('ttres_boottnorm_smooth2r3.config', 'ttres_%s%s_boottnorm_smooth2r3.config' % (i, suf), i, "%s%s_boottnorm_smooth2r3" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_smooth2r3' % (i, suf))

    #fixFile('ttres_boottnorm_asimov.config', 'ttres_%s%s_boottnorm_asimov.config' % (i, suf), i, "%s%s_boottnorm_asimov" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_asimov' % (i, suf))

    #fixFile('ttres_boottnorm_psold_asimov.config', 'ttres_%s%s_boottnorm_psold_asimov.config' % (i, suf), i, "%s%s_boottnorm_psold_asimov" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_psold_asimov' % (i, suf))

    # boosted tt norm -- stat only
    #fixFile('ttres_boottnorm.config', 'ttres_%s%s_boottnorm_stat.config' % (i, suf), i, "%s%s_boottnorm_stat" % (i, suf), False)
    #jobSubmit('%s%s_boottnorm_stat' % (i, suf))

    ## boosted tt norm -- ranking
    #if 'zprime2000' in i or 'zprime3000' in i:
    #  fixFile('ttres_boottnorm.config', 'ttres_%s%s_boottnorm_inj.config' %(i, suf), i, "%s%s_boottnorm_inj" % (i, suf), False)
    #  jobSubmit("%s%s_boottnorm_inj" % (i, suf))

    #if 'zprime400' in i or 'zprime1000' in i or 'zprime2000' in i or 'zprime3000' in i:
    #  fixFile('ttres_boottnorm_asimov.config', 'ttres_%s%s_boottnorm_asimov_inj.config' %(i, suf), i, "%s%s_boottnorm_asimov_inj" % (i, suf), False)
    #  jobSubmit("%s%s_boottnorm_asimov_inj" % (i, suf))

    #  fixFile('ttres_boottnorm_psold_asimov.config', 'ttres_%s%s_boottnorm_psold_asimov_inj.config' %(i, suf), i, "%s%s_boottnorm_psold_asimov_inj" % (i, suf), False)
    #  jobSubmit("%s%s_boottnorm_psold_asimov_inj" % (i, suf))

    ## NNLO rew.
    #fixFile('ttres_nnlo.config', 'ttres_%s%s_nnlo.config' % (i, suf), i, "%s%s_nnlo" % (i, suf), False)
    #jobSubmit('%s%s_nnlo' % (i, suf))

    ## fine binning
    #fixFile('ttres_binning.config', 'ttres_%s%s_binning.config' % (i, suf), i, "%s%s_binning" % (i, suf), False)
    #jobSubmit('%s%s_binning' % (i, suf))


# now KK gluon reweighted
#for t in signalList:
#  if "eft" in t:
#    continue
#  #if not ("kkg" in t and "w" in t):
#  if not ("kkg" in t and "w15" in t):
#    continue
#  for i in signalList[t]:
#    ## nominal
#    #fixFile('ttres.config', 'ttres_%s%s.config' %(i, suf), i, "%s%s" % (i, suf), False)
#    #jobSubmit("%s%s" % (i, suf))
#    ## stat only
#    #fixFile('ttres.config', 'ttres_%s%s_stat.config' %(i, suf), i, "%s%s_stat" % (i, suf), False)
#    #jobSubmit("%s%s_stat" % (i, suf))
#
#    # boosted tt norm
#    fixFile('ttres_boottnorm.config', 'ttres_%s%s_boottnorm.config' % (i, suf), i, "%s%s_boottnorm" % (i, suf), False)
#    jobSubmit('%s%s_boottnorm' % (i, suf))
#
#    # boosted tt norm -- stat only
#    fixFile('ttres_boottnorm.config', 'ttres_%s%s_boottnorm_stat.config' % (i, suf), i, "%s%s_boottnorm_stat" % (i, suf), False)
#    jobSubmit('%s%s_boottnorm_stat' % (i, suf))
