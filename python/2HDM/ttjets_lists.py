#!/usr/bin/env python
import os
import glob
basedir  = "/afs/cern.ch/user/h/hod/data/mc15_13TeV/"
sampledir = "MGPy8EG_A14N30NLO_ttbarNp012p/"
srcdir = "../"
path = basedir+sampledir
files = glob.glob(path+"*/*")
print files

fall = open(srcdir+"fileslist.txt",'w')
fsingle = {}

os.system("rm -f "+srcdir+"input_EXOT4_*.txt")

for f in sorted(files):
   fall.write(f+"\n")

   p = f.replace(path,"").split("/")[0] ## strip off just the dataset name
   dsid = p.split(".")[2]               ## strip off just the datast id

   if(dsid in ["407200","407201","407202","407203","407204"]): dsid = "40720X"

   if(dsid not in fsingle.keys()): fsingle.update({dsid:open(srcdir+"input_EXOT4_"+str(dsid)+".txt",'a')})
   fsingle[dsid].write(f+"\n")
   
for dsid,f in fsingle.iteritems():
   f.close()

fall.close()
