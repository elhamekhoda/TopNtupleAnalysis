#!/usr/bin/python

import os
import subprocess
import argparse
## usage: python ttjets_sends.py -M batch/check/merge/plots/dry
parser = argparse.ArgumentParser(description='ttjets sends')
parser.add_argument('-M', metavar='<run mode>', required=True, help='The run mode [batch/check/merge/plots/dry]')
parser.add_argument('-F', metavar='<run mode>', required=True, help='Force signal only ? [0/1]')
args = parser.parse_args()
mode=str(args.M)
ForceSignalOnly=int(args.F)
print "M=%s, F=%g" % (mode,ForceSignalOnly)

decision = raw_input("do you want to run "+mode+"? [yes/Yes/YES/no]...")
if(decision==("yes") or decision==("Yes") or decision==("Yes")):
   print "running!"
else:
   print "quitting!"
   quit()

nameX = ["A","H"]
mX    = [500,800]
tanbX = [0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.2,1.4,1.6,1.8,2.0]
sba   = 1
typeX = 2

jobdir  = "/afs/cern.ch/user/h/hod/data/jobs/"
os.system("rm -f "+jobdir+"failed_jobs.sh")
for m in mX:
   sm = str(m)
   for s in nameX:
      for tanb in tanbX:
         stanb = '%.1f' % tanb
         command = "python ttjets_"+mode+".py -S "+s+" -M "+sm+" -SBA "+str(sba)+" -TANB "+stanb+" -TYPE "+str(typeX)
         if(mode=="batch"): command += " -R 0 -F 1"
         if(mode=="check"): command += " -R 0 -F 1"
         if(mode=="merge"): command += " -F 1"
         if(mode=="plots"): command += ""
         if(not ForceSignalOnly and (m==mX[0] and s==nameX[0] and tanb==tanbX[0])): 
            command = command.replace("-R 0","-R 1")
            command = command.replace("-F 1","-F 0")
         ### execute
         if(mode!="dry"):   os.system(command)
         else:
            command.replace("dry","batch")
            command += " -R 0 -F 1"
            print command

### summary
if(mode=="check"):
   print "\nplease check faild jobs:\n"+jobdir+"failed_jobs.sh"
