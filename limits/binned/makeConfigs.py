#!/usr/bin/env python
from os import system,getcwd,path
from time import time
from inputs import *
import socket, random, re

site="DESY"
if socket.gethostname().find("clratl") != -1:
	site="LPC"
print "@"+site+"! "

# change those:
if site=="DESY":
   setdir = '/afs/desy.de/user/d/danilo/xxl/af-atlas/Top2418'
   mydir = '/nfs/dust/atlas/user/danilo/hists_sr2418_jes/TRexFitter_trs'
elif site=="LPC":
   mydir = '/AtlasDisk/users/scalvet/Zprime/LimitSetting/TopNtupleAnalysis/limits/binned/Jamboree/test1/TRExFitter'
   version="firstTest"
   version="secondTest"



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
  Smoothing: 40
''')
      continue
    
    nline = line
    if 'FitTtres' in nline:
      nline = nline.replace('FitTtres', 'FitTtres_'+i)
    if 'JobTtres' in nline:
      nline = nline.replace('JobTtres', 'JobTtres_'+i)
    if 'FitType' in nline and doBOnlyFit:
      nline = nline.replace('SPLUSB', 'BONLY')
    if 'eft' in i and 'Binning: ' in nline:
      nline = "  Binning: 2000,6000\n"
    f.write(nline)

  f.close()
  fr.close()


def jobSubmit(suf):
	if site=="DESY":
		jobSubmitDESY(suf)
	elif site=="LPC":
		jobSubmitLPC(suf)


def jobSubmitLPC(stuf):
        print stuf
	
        here = getcwd()
        configName = 'ttres_'+stuf+'.config'
	
	system('mkdir -p '+version)
	if path.exists(version+"/t.tar.gz")==False:
		print "Making tarball..."
		com = "tar -czf "+version+"/t.tar.gz --exclude="+version+"/*root --exclude=inputFiles/ --exclude=JobTtres *"
		system(com)
	
	system('cp '+configName+' '+version)
	
        scriptName=version+"/script_"+stuf+".sh"
        f = open(scriptName,'w')       
        f.write('#!/bin/bash\n')
        f.write('echo running on $HOSTNAME\n')
        f.write('\n')
	
        workDir = re.sub('\.','',str(time())+`random.randint(0, 1000000)`)
        WORKDIR = "/users_local1/$LOGNAME/"+workDir
               
        f.write('\n' + 'mkdir -p '+WORKDIR+'\n')
        f.write('\n' + 'cd '+WORKDIR+'\n')
        f.write('export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase\n')
        f.write('source /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/user/atlasLocalSetup.sh\n')
        f.write('localSetupROOT\n')
        f.write('\n')
        f.write('cp -f '+here+"/"+version+'/t.tar.gz .\n')
        f.write('tar -xzvf t.tar.gz\n')
        f.write('echo "untaring done!" \n\n')
        f.write('cp -f '+here+"/"+version+'/'+configName+' .\n')
        f.write('./myFit.exe h '+configName+' > log_'+stuf+'_h\n')
        f.write('./myFit.exe d '+configName+' > log_'+stuf+'_d\n')
        f.write('./myFit.exe w '+configName+' > log_'+stuf+'_w\n')
        f.write('./myFit.exe f '+configName+' > log_'+stuf+'_f\n')
        f.write('./myFit.exe p '+configName+' > log_'+stuf+'_p\n')
        if configName.find("bkg")!=-1:
                #do nothing
                a=1
        else:
                f.write('./myFit.exe l '+configName+' > log_'+stuf+'_l\n')
                f.write('./myFit.exe s '+configName+' > log_'+stuf+'_s\n')
                #f.write('./myFit.exe r '+configName+' > log_'+stuf+'_r\n')
       
       
       
        outDir = './JobTtres_'+stuf
       
        f.write('cp -rf '+outDir+' '+here+'/'+version+'\n')
        f.write('cp -f log_'+stuf+'_*  '+here+'/'+version+'/'+outDir+'/\n')
        f.write('rm -rf '+WORKDIR+'\n')
        f.close()
       
        com= 'qsub -N '+stuf+' -q multi64sl6@clratlserv05  -e '+here+'/'+version+' -o '+here+'/'+version+' '+scriptName
        #com= 'qsub -N '+stuf+' -q fast64sl6@clratlserv03  -e '+here+'/'+version+' -o '+here+'/'+version+' '+scriptName
               
        print com


def jobSubmitDESY(suf):
	runfile = 'submit_%s.sh' % suf
	logfile = mydir+'/stdout_%s.txt'%suf
	queue = 'long.q'
	if 'bkg' in suf:
		queue = 'short.q'
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
fixFile('ttres_template.config', 'ttres_bkg.config', "bkg", True)
system('cp -f hist_zprime2000.root hist_bkg.root') ## use a dummy signal for the background only fit
jobSubmit('bkg')

# now go over to signal
for t in signalList:
  for i in signalList[t]:
    fixFile('ttres_template.config', 'ttres_'+i+'.config', i, False)
    jobSubmit(i)

