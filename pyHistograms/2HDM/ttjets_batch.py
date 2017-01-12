#!/usr/bin/env python
import os
import sys
import subprocess
import ttjets_split
import argparse
## usage:
## python ttjets_batch.py -S A -M 500 -SBA 1 -TANB 0.4 -TYPE 2 -R 1 -F 0
parser = argparse.ArgumentParser(description='ttjets plot')
parser.add_argument('-S', metavar='<resonance name>', required=True, help='The resonance name [A/H]')
parser.add_argument('-M', metavar='<resonance mass>', required=True, help='The resonance mass [500,...]')
parser.add_argument('-SBA', metavar='<sin(beta-alpha)>', required=True, help='Sin(beta-alpha) [1,...]')
parser.add_argument('-TANB', metavar='<tan(beta)>', required=True, help='Tan(beta) [0.3,...]')
parser.add_argument('-TYPE', metavar='<type>', required=True, help='Type [1/2]')
parser.add_argument('-R', metavar='<resplit inputs?>', required=True, help='Resplit the inputs? [0/1]')
parser.add_argument('-F', metavar='<force signal only??>', required=True, help='Force signal only? [0/1]')
args = parser.parse_args()
S=str(args.S)
M=int(args.M)
SBA=float(args.SBA)
TANB=float(args.TANB)
TYPE=int(args.TYPE)
RESPLIT=int(args.R)
ForceSignalOnly=int(args.F)
print "S=%s, M=%s, SBA=%s, TANB=%s, TYPE=%s, RESPLIT=%s, ForceSignalOnly=%s" % (S,M,SBA,TANB,TYPE,RESPLIT,ForceSignalOnly)

basedir = "/afs/cern.ch/user/h/hod/AnalysisTop/AnalysisTop-2.4.21/"
srcdir  = basedir+"TopNtupleAnalysis/pyHistograms/"
jobdir  = "/afs/cern.ch/user/h/hod/data/jobs/"
logdir  = "/afs/cern.ch/user/h/hod/data/logs/"
figdir  = "/afs/cern.ch/user/h/hod/data/figs/"

runnums = ["410000", "407200", "407201", "407202", "407203", "407204"]
#runnums = ["407200", "407201", "407202", "407203", "407204"]
#runnums = ["410000"]

MH=-1
MA=-1
if(S=="H"):
   MH=M
   MA=-1
else:
   MH=-1
   MA=M


for runnum in runnums:
   isTTjets = (int(runnum)>=407200 and int(runnum)<=407204)
   if(ForceSignalOnly and not isTTjets): continue
   niterations = 2 if(isTTjets and not ForceSignalOnly) else 1
   for iteration in xrange(niterations):
      isSignal = 1 if(ForceSignalOnly) else iteration
      if(RESPLIT): ttjets_split.splitinput(srcdir+"input_EXOT4_"+runnum+".txt",ttjets_split.splits[runnum]["nfilesperjob"])
      for subjob in xrange(1,ttjets_split.splits[runnum]["njobs"]+1):
         sjob = str(subjob) if(subjob>9) else "0"+str(subjob)
         jobconf  = ""
         jobopt   = ""
         if(isTTjets and isSignal):
            sSBA    = str(SBA).replace(".","")
            sTANB   = str(TANB).replace(".","")
            jobconf = str(runnum)+".s"+str(S)+"_m"+str(M)+"_sba"+sSBA+"_tanb"+sTANB+"_t"+str(TYPE)+".j"+sjob
            jobopt  = str(MH)+","+str(MA)+","+str(SBA)+","+str(TANB)+","+str(TYPE)
         else:
            jobconf = str(runnum)+".j"+sjob
            jobopt  = ""

         fjobname = jobdir+jobconf+".sh"
         flogname = logdir+jobconf+".log"
         ffigpattern = figdir+"*."+jobconf+".root"

         ### delete files from previous submission
         p = subprocess.Popen("rm -f "+fjobname, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
         out, err = p.communicate()
         p = subprocess.Popen("rm -f "+flogname, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
         out, err = p.communicate()
         p = subprocess.Popen("rm -f "+ffigpattern, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
         out, err = p.communicate()

         ### make the job file
         fjob = open(fjobname,'w')
         fjob.write('#!/bin/bash\n')
         fjob.write('echo "host = $HOSTNAME"\n')
         fjob.write('cd '+basedir+'\n')
         fjob.write('export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase\n')
         fjob.write('source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh\n')
         fjob.write('source rcSetup.sh\n')
         fjob.write('cd '+srcdir+'2HDM/local/\n')
         fjob.write('source setup.sh\n')
         fjob.write('cd '+srcdir+'\n')
         if(isTTjets and isSignal):
            #fjob.write("./makeHistograms.py  --files input_EXOT4_"+runnum+"_j"+sjob+".txt  --analysis AnaTtresSL  --output re,////tmp/hod/re."+jobconf+".root\;rmu,////tmp/hod/rmu."+jobconf+".root,be:////tmp/hod/be."+jobconf+".root\;bmu,////tmp/hod/bmu."+jobconf+".root  --systs nominal  --SCALAR "+jobopt+"\n")
            fjob.write("./makeHistograms.py  --files input_EXOT4_"+runnum+"_j"+sjob+".txt  --analysis AnaTtresSL  --output re,////tmp/hod/re."+jobconf+".root\;rmu,////tmp/hod/rmu."+jobconf+".root  --systs nominal  --SCALAR "+jobopt+"\n")
         else:
            #fjob.write("./makeHistograms.py  --files input_EXOT4_"+runnum+"_j"+sjob+".txt  --analysis AnaTtresSL  --output re,////tmp/hod/re."+jobconf+".root\;rmu,////tmp/hod/rmu."+jobconf+".root,be:////tmp/hod/be."+jobconf+".root\;bmu,////tmp/hod/bmu."+jobconf+".root  --systs nominal\n")
            fjob.write("./makeHistograms.py  --files input_EXOT4_"+runnum+"_j"+sjob+".txt  --analysis AnaTtresSL  --output re,////tmp/hod/re."+jobconf+".root\;rmu,////tmp/hod/rmu."+jobconf+".root  --systs nominal\n")
         fjob.write('/bin/cp -f /tmp/hod/*.root '+figdir+'\n')
         fjob.write('echo "host = $HOSTNAME"\n')

         ### submit the job
         p = subprocess.Popen("chmod 755 "+fjobname, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
         out, err = p.communicate() 
         p = subprocess.Popen("bsub -q 1nd -o "+flogname+" "+fjobname, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
         out, err = p.communicate()
         print "bsub output: ",out

print "run: `bjobs -w` to list the jobs"
print "run: `bkill -u hod 0` to kill the jobs"
