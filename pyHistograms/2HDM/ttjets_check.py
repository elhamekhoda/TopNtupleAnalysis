#!/usr/bin/env python
import os
import sys
import subprocess
import os.path
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
channels = ["re","rmu"]

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

         ### check log file
         flogname = logdir+jobconf+".log"
         if(not os.path.isfile(flogname)):
            print "missing log file:",flogname
         else:
            flog = open(flogname)
            lines = flog.readlines()
            nlastlines = 10
            for line in lines[::-1]:
               if(nlastlines==0): break
               if("(tree =  nominal , syst =   ) Entry" in line): break
               if("host = "                             in line): break
               nlastlines -= 1
            if(nlastlines==0):
               print "log file missing patterns:",flogname

            ### check root file
            for channel in channels:
               ffigname = figdir+channel+"."+jobconf+".root"
               if(not os.path.isfile(ffigname)):
                  print "missing root file:",ffigname
               else:
                  if(os.path.getsize(ffigname)/1000<25):
                     print "too small root file:",ffigname
