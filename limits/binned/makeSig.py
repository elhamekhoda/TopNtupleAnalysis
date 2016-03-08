#!/usr/bin/env python
from os import system,getcwd
from time import time
from inputs import *
import socket, random, re

# now go over to signal
for i in signalList:
     system('./myFit.exe s ttres_'+i+'.config')

