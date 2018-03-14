#!/usr/bin/env python
import os
import sys
import subprocess
import argparse
## usage:
## python ttjets_merge.py -S A -M 500 -SBA 1 -TANB 0.4 -TYPE 2 -F 0
parser = argparse.ArgumentParser(description='ttjets plot')
parser.add_argument('-S', metavar='<resonance name>', required=True, help='The resonance name [A/H]')
parser.add_argument('-M', metavar='<resonance mass>', required=True, help='The resonance mass [500,...]')
parser.add_argument('-SBA', metavar='<sin(beta-alpha)>', required=True, help='Sin(beta-alpha) [1,...]')
parser.add_argument('-TANB', metavar='<tan(beta)>', required=True, help='Tan(beta) [0.3,...]')
parser.add_argument('-TYPE', metavar='<type>', required=True, help='Type [1/2]')
parser.add_argument('-F', metavar='<force signal only??>', required=True, help='Force signal only? [0/1]')
args = parser.parse_args()
S=str(args.S)
M=int(args.M)
SBA=float(args.SBA)
TANB=float(args.TANB)
TYPE=int(args.TYPE)
ForceSignalOnly=int(args.F)
print "S=%s, M=%s, SBA=%s, TANB=%s, TYPE=%s, ForceSignalOnly=%s" % (S,M,SBA,TANB,TYPE,ForceSignalOnly)

MH=-1
MA=-1
if(S=="H"):
   MH=M
   MA=-1
else:
   MH=-1
   MA=M
sSBA  = str(SBA).replace(".","")
sTANB = str(TANB).replace(".","")
model  = ".s"+str(S)+"_m"+str(M)+"_sba"+sSBA+"_tanb"+sTANB+"_t"+str(TYPE)

'''
decision = raw_input("do you want to run "+mode+"? [yes/Yes/YES/no]...")
if(decision==("yes") or decision==("Yes") or decision==("Yes")):
   print "running!"
else:
   print "quitting!"
   quit()
'''

def mergeoutput(path,pattern):
   mergedname = path+pattern.replace("j*","merged")
   p = subprocess.Popen("rm -f "+mergedname, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   out, err = p.communicate()
   p = subprocess.Popen("hadd -f "+mergedname+" "+path+pattern, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   out, err = p.communicate()
   print out

figdir  = "/afs/cern.ch/user/h/hod/data/figs/"

runnums = ["410000", "40720X"]
#runnums = ["410000", "407200", "407201", "407202", "407203", "407204"]
#runnums = ["407200", "407201", "407202", "407203", "407204"]
channels = ["re","rmu"]
#channels = ["re","rmu","be","bmu"]

for runnum in runnums:
   isTTjets = (runnum=="40720X") #(int(runnum)>=407200 and int(runnum)<=407204)
   for channel in channels:
      if(not ForceSignalOnly):
         ## e.g. re.40720X.j01.root
         pattern = channel+"."+runnum+".j*.root"
         mergeoutput(figdir,pattern)
      if(isTTjets):
         ## e.g. re.40720X.sA_m500_sba1_tanb03_t2.j01.root
         pattern = channel+"."+runnum+model+".j*.root"
         mergeoutput(figdir,pattern)
