#!/usr/bin/env python
from itertools import izip_longest
import subprocess

def grouper(n, iterable, fillvalue=None):
   "Collect data into fixed-length chunks or blocks"
   # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
   args = [iter(iterable)] * n
   return izip_longest(fillvalue=fillvalue, *args)

def splitinput(fin,nfilesperjob):
   with open(fin) as f:
      for i, g in enumerate(grouper(nfilesperjob,f,fillvalue=''), 1):
         si = str(i)
         if(i<10): si = "0"+si
         foutname = fin.replace(".txt","_j"+si+".txt")
         with open(foutname,'w') as fout:
            fout.writelines(g)

## global data structures
#splits = {"410000":{"njobs":26,"nfilesperjob":1}, "407200":{"njobs":5,"nfilesperjob":1}, "407201":{"njobs":2,"nfilesperjob":1}, "407202":{"njobs":3,"nfilesperjob":1}, "407203":{"njobs":2,"nfilesperjob":1}, "407204":{"njobs":3,"nfilesperjob":1}}
splits = {"410000":{"njobs":26,"nfilesperjob":1}, "40720X":{"njobs":15,"nfilesperjob":1}}
