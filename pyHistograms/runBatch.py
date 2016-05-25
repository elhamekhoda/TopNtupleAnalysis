
import HQTTtResonancesTools.DC15MC13TeV_25ns_mc15c_EXOT4
import HQTTtResonancesTools.DC15Data13TeV_25ns_207_EXOT4
from subprocess import Popen,PIPE

# lxbatch queue to submit to
queue = '1nd'

# email to use to tell us when the job is done
email = 'dferreir@cern.ch'

# directory with the base of the RootCore stuff
rundir = '/afs/desy.de/user/d/danilo/private/topana/Top246'

# number of files per job
nFilesPerJob = 2

# input directory
ntuplesDir = '/nfs/dust/atlas/user/danilo/12052016v1'

# output directory
outputDir = rundir+'/TopNtupleAnalysis/pyHistograms/hists'

# the default is AnaTtresSL, which produces many control pltos for tt res.
# The Mtt version produces a TTree to do the limit setting
# the QCD version aims at plots for QCD studies using the matrix method
# look into read.cxx to see what is available
# create yours, if you wish
analysisType='AnaTtresSL'

# leave it for nominal to run only the nominal
#systematics = 'nominal'
systematics = 'all'

names   = []
# 25 ns datasets
names  += ['MC15c_13TeV_25ns_FS_EXOT4_ttbarPowhegPythia']
#names  += ['MC15c_13TeV_25ns_FS_EXOT4_ttbarPowhegPythia_mttsliced']
names  += ['MC15c_13TeV_25ns_FS_EXOT4_singletop']
names  += ['MC15c_13TeV_25ns_FS_EXOT4_Wjets22']
names  += ['MC15c_13TeV_25ns_FS_EXOT4_Zjets22']
names  += ['MC15c_13TeV_25ns_FS_EXOT4_VV']
#names += ['MC15_13TeV_25ns_FS_EXOT4_Zprime400']
#names += ['MC15_13TeV_25ns_FS_EXOT4_Zprime500']
#names += ['MC15_13TeV_25ns_FS_EXOT4_Zprime750']
#names += ['MC15_13TeV_25ns_FS_EXOT4_Zprime1000']
#names += ['MC15_13TeV_25ns_FS_EXOT4_Zprime1250']
#names += ['MC15_13TeV_25ns_FS_EXOT4_Zprime1500']
#names += ['MC15_13TeV_25ns_FS_EXOT4_Zprime1750']
#names += ['MC15_13TeV_25ns_FS_EXOT4_Zprime2000']
#names += ['MC15_13TeV_25ns_FS_EXOT4_Zprime2250']
#names += ['MC15_13TeV_25ns_FS_EXOT4_Zprime2500']
#names += ['MC15_13TeV_25ns_FS_EXOT4_Zprime2750']
#names += ['MC15_13TeV_25ns_FS_EXOT4_Zprime3000']
#names += ['MC15_13TeV_25ns_FS_EXOT4_Zprime4000']
#names += ['MC15_13TeV_25ns_FS_EXOT4_Zprime5000']

import TopExamples.grid

import glob
#files = glob.glob(ntuplesDir+'/*.root')
samples = TopExamples.grid.Samples(names)

import glob
import os
# get list of processed datasets
dirs = glob.glob(ntuplesDir+'/*')
#dirs = Popen([eosrun, "ls", ntuplesDir], stdout=PIPE).communicate()[0].split('\n')

# each "sample" below means an item in the list names above
# there may contain multiple datasets
# for each sample we want to read
for sample in samples:
    # write list of files to be read when processing this sample
    f = open(outputDir+"/input_"+sample.name+'.txt', 'w')
    # output file after running read
    #outfile = outputDir+"/"+sample.name
    outfile = sample.name

    forJobs = {}
    nJob = 0
    nFile = 0
    
    # go over all directories in the ntuplesDir
    for d in dirs:
      if d == '':
         continue

      # remove path and get only dir name in justfile
      #justfile = d.split('/')[-1]
      #dsid_dir = justfile.split('.')[2] # get the DSID of the directory
      dsid_dir = d.split('.')[2] # get the DSID of the directory
      # this will include all directories, so check if this director is in the sample

      # now go over the list of datasets in sample
      # and check if this DSID is there
      for s in sample.datasets:
        if len(s.split(':')) > 1:
          s = s.split(':')[1] # skip mc15_13TeV
        dsid_sample = s.split('.')[1] # get DSID
        if dsid_dir == dsid_sample: # this dataset belongs in the sample in the big for loop
          # get all files in the directory
          files = glob.glob(d+'/*.root*')
          #files = Popen([eosrun, "ls", ntuplesDir+"/"+d], stdout=PIPE).communicate()[0].split('\n')
          # and write it in ht elist of input files to process
          for item in files:
              if not '.part' in item and item != '':
                  fullname = item
                  #fullname = entry+ntuplesDir+"/"+d+'/'+item
                  f.write(fullname+'\n')

                  if nFile == nFilesPerJob:
                     nFile = 0
                     nJob = nJob + 1
                  if nFile == 0:
                     forJobs[str(nJob)] = []
                  forJobs[str(nJob)].append(fullname+'\n')
                  nFile = nFile + 1
          # go to the next directory in the same sample
          break
    f.close()
    theSysts = systematics
    isData = ''
    if "Data" in sample.name:
      theSysts = "nominal"
      isData = ' -d '

    for job in forJobs:
        jobName = sample.name+'_'+job
        infile = outputDir+"/input_"+jobName+'.txt'
        infullfile = outputDir+"/input_"+sample.name+'.txt'
        f = open(infile, 'w')
        for item in forJobs[job]:
            f.write(item)
        f.close()
        errfile = outputDir+"/stderr_"+jobName+'.txt'
        logfile = outputDir+"/stdout_"+jobName+'.txt'
        runfile = outputDir+"/run_"+jobName+'.sh'
        fr = open(runfile, 'w')
        fr.write('#!/bin/sh\n')
        fr.write('cd '+rundir+'\n')
        fr.write('source /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/user/atlasLocalSetup.sh\n')
        fr.write('lsetup rcsetup\n')
        fr.write('cd TopNtupleAnalysis/pyHistograms\n')
        fr.write('./makeHistograms.py - '+isData+' --files '+infile+' --fullFiles '+infullfile+' --analysis '+analysisType+' --output re:'+outputDir+'/resolved_e_'+outfile+'_'+job+'.root,rmu:'+outputDir+'/resolved_mu_'+outfile+'_'+job+'.root,be:'+outputDir+'/boosted_e_'+outfile+'_'+job+'.root,bmu:'+outputDir+'/boosted_mu_'+outfile+'_'+job+'.root --systs '+theSysts+'\n')
        fr.close()
        os.system('chmod a+x '+runfile)
        subcmd = 'bsub -e '+errfile+' -o '+logfile+' -q '+queue+' -N -u '+email+' -J tna_'+jobName+' '+runfile
        os.system(subcmd)
        #print(subcmd)
        #import sys
        #sys.exit(0)

