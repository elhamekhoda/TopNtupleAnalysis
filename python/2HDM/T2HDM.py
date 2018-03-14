#!/usr/bin/python

import numpy as NUMPY
import subprocess
from contextlib import contextmanager
import os
import sys
import pwd
import string
import random
from pipes import quote
from pprint import pprint
import imp
import ROOT
from ROOT import *


username   = pwd.getpwuid(os.getuid()).pw_name #os.getlogin()
mgpath     = "/afs/cern.ch/user/h/hod/MadGraph/MG5_aMC_v2_4_3/"
libpath    = "/afs/cern.ch/user/h/hod/data/lib2HDM/"
libpathtmp = "/tmp/"+username+"/"


class fermions:
   """fermion definitions"""
   def __init__(self):
      self.u = 1
      self.d = 2
      self.s = 3
      self.c = 4
      self.b = 5
      self.t = 6
      self.e = 11
      self.mu = 13
      self.tau = 15

class t2HDM:
   """The 2HDM definitions"""
   def __init__(self, nameX="A", mX=500, typeX=2, sba=1, tanb=0.4):
      ### the model parameters
      self.nameX   = nameX
      self.mX      = mX
      self.typeX   = typeX
      self.sba     = sba
      self.tanb    = tanb
      self.cuts  = "m"+nameX+"=="+str(mX)+" && sba=="+str(sba)+" && tanb=="+str(tanb)
      self.cuts += " && TMath::ATan(tanb)>0. && TMath::ATan(tanb)<TMath::Pi()/2."
      self.cuts += " && TMath::Abs(cba)<=1."
      self.cuts += " && type=="+str(typeX)
      # self.cuts += " && (status&7)==0" 
      self.cuts += " && (status&3)==0"
      self.MC   = 1.42
      self.MB   = 4.7
      self.MT   = 172.5
      self.MM   = 0.10566
      self.MTAU = 1.777
      self.parameters = []
      self.modules    = {}
      self.rndstr = ''.join(random.SystemRandom().choice(string.ascii_letters + string.ascii_uppercase + string.digits) for _ in range(10))
      ########################
      self.setParameters() ###
      ########################

   def couplings(self,fermion,cba):
      Fermions = fermions()
      g = 0.
      if(self.typeX==1):
         if(self.nameX=="h"):
            if(fermion==Fermions.u or fermion==Fermions.c  or fermion==Fermions.t):   g = self.sba+cba/self.tanb
            if(fermion==Fermions.d or fermion==Fermions.s  or fermion==Fermions.b):   g = self.sba+cba/self.tanb
            if(fermion==Fermions.e or fermion==Fermions.mu or fermion==Fermions.tau): g = self.sba+cba/self.tanb
         if(self.nameX=="H"):
            if(fermion==Fermions.u or fermion==Fermions.c  or fermion==Fermions.t):   g = cba-self.sba/self.tanb
            if(fermion==Fermions.d or fermion==Fermions.s  or fermion==Fermions.b):   g = cba-self.sba/self.tanb
            if(fermion==Fermions.e or fermion==Fermions.mu or fermion==Fermions.tau): g = cba-self.sba/self.tanb
         if(self.nameX=="A"):
            if(fermion==Fermions.u or fermion==Fermions.c  or fermion==Fermions.t):   g = +1./self.tanb
            if(fermion==Fermions.d or fermion==Fermions.s  or fermion==Fermions.b):   g = -1./self.tanb
            if(fermion==Fermions.e or fermion==Fermions.mu or fermion==Fermions.tau): g = -1./self.tanb
      if(self.typeX==2):
         if(self.nameX=="h"):
            if(fermion==Fermions.u or fermion==Fermions.c  or fermion==Fermions.t):   g = self.sba+cba/self.tanb
            if(fermion==Fermions.d or fermion==Fermions.s  or fermion==Fermions.b):   g = self.sba-cba*self.tanb
            if(fermion==Fermions.e or fermion==Fermions.mu or fermion==Fermions.tau): g = self.sba-cba*self.tanb
         if(self.nameX=="H"):
            if(fermion==Fermions.u or fermion==Fermions.c  or fermion==Fermions.t):   g = cba-self.sba/self.tanb
            if(fermion==Fermions.d or fermion==Fermions.s  or fermion==Fermions.b):   g = cba+self.sba*self.tanb
            if(fermion==Fermions.e or fermion==Fermions.mu or fermion==Fermions.tau): g = cba+self.sba*self.tanb
         if(self.nameX=="A"):
            if(fermion==Fermions.u or fermion==Fermions.c  or fermion==Fermions.t):   g = +1./self.tanb
            if(fermion==Fermions.d or fermion==Fermions.s  or fermion==Fermions.b):   g = self.tanb
            if(fermion==Fermions.e or fermion==Fermions.mu or fermion==Fermions.tau): g = self.tanb
      return g

   def setParameters(self):
      f = TFile("/afs/cern.ch/user/h/hod/data/thdm_grid_v166.root","READ")
      t = f.Get("thdm")
      b_tb  = NUMPY.zeros(1, dtype=float)
      b_sba = NUMPY.zeros(1, dtype=float)
      b_cba = NUMPY.zeros(1, dtype=float)
      b_wA  = NUMPY.zeros(1, dtype=float)
      b_wH  = NUMPY.zeros(1, dtype=float)
      b_mA  = NUMPY.zeros(1, dtype=float)
      b_mH  = NUMPY.zeros(1, dtype=float)
      t.SetBranchAddress("tanb",b_tb);
      t.SetBranchAddress("sba",b_sba);
      t.SetBranchAddress("cba",b_cba);
      t.SetBranchAddress("width_A",b_wA);
      t.SetBranchAddress("width_H",b_wH);
      t.SetBranchAddress("mA",b_mA);
      t.SetBranchAddress("mH",b_mH);
      
      print "Before cuts = "+str(t.GetEntries())
      print "cuts: "+self.cuts
      t.Draw(">>elist",self.cuts,"entrylist");
      elist = gDirectory.Get("elist");
      t.SetEntryList(elist);
      Nlist = elist.GetN()
      print "After self.cuts = "+str(Nlist)
      
      Fermions = fermions()
      for i in range(0,Nlist):
         n = elist.Next()
         t.GetEntry(n)
         tanb = b_tb[0]
         sba  = b_sba[0]
         cba  = b_cba[0]
         wA   = b_wA[0]
         wH   = b_wH[0]
         mA   = b_mA[0]
         mH   = b_mH[0]
         YMT   = self.couplings(Fermions.t  ,cba)*self.MT
         YMB   = self.couplings(Fermions.b  ,cba)*self.MB
         YMC   = self.couplings(Fermions.c  ,cba)*self.MC
         YMM   = self.couplings(Fermions.mu ,cba)*self.MM
         YMTAU = self.couplings(Fermions.tau,cba)*self.MTAU
         print "["+str(i)+"] tanb="+'%.6f' % tanb+" sba="+'%.6f' % sba+" cba="+'%.6f' % cba+" wA="+'%.6f' % wA+" wH="+'%.6f' % wH+" YMT="+'%.6f' % YMT+" YMB="+'%.6f' % YMB+" YMC="+'%.6f' % YMC+" YMM="+'%.6f' % YMM+" YMTAU="+'%.6f' % YMTAU
         adict = {}
         adict = {'tanb':tanb, 'sba':sba, 'cba':cba, 'mA':mA, 'wA':wA, 'mH':mH, 'wH':wH, 'YMT':YMT, 'YMB':YMB, 'YMC':YMC, 'YMM':YMM, 'YMTAU':YMTAU}
         self.parameters.append(adict.copy())
      print "N="+str(len(self.parameters))+" parameters set !"


diagramsSM = [ "P0_gg_ttx",
               "P0_uux_ttx",
               "P1_uux_ttxg",
               "P1_gux_ttxux",
               "P1_gu_ttxu",
               "P1_gg_ttxg",
               "P2_gu_ttxgu",
               "P2_uxux_ttxuxux",
               "P2_uxcx_ttxuxcx",
               "P2_uux_ttxuux",
               "P2_uux_ttxgg",
               "P2_uux_ttxccx",
               "P2_uu_ttxuu",
               "P2_ucx_ttxucx",
               "P2_uc_ttxuc",
               "P2_gux_ttxgux",
               "P2_gg_ttxgg",
               "P2_gg_ttxuux"
             ]
diagramsXX = diagramsSM +  [ "P0_bbx_ttx",
                             "P1_bbx_ttxg",
                             "P1_gbx_ttxbx",
                             "P1_gb_ttxb",
                             "P2_gb_ttxgb",
                             "P2_bxbx_ttxbxbx",
                             "P2_uxbx_ttxuxbx",
                             "P2_bbx_ttxbbx",
                             "P2_bbx_ttxgg",
                             "P2_uux_ttxbbx",
                             "P2_bbx_ttxuux",
                             "P2_bb_ttxbb",
                             "P2_ubx_ttxubx",
                             "P2_ub_ttxub",
                             "P2_gbx_ttxgbx",
                             "P2_gg_ttxbbx",
                             #"P2_uxb_ttxuxb"
                            ]
ptest4 = [[148.7495, 0.0, 0.0, 148.7495],
          [346.258375, 0.0, 0.0, -346.258375],
          [285.4675, -99.5479765625, 60.29248046875, -197.2335625],
          [209.539609375, 99.5479765625, -60.29248046875, -0.2753184814453125]]
ptest5 = [[264.3046875, 0.0, 0.0, 264.3046875],
          [328.02553125, 0.0, 0.0, -328.02553125],
          [242.8330625, 18.229767578125, 58.28096484375, 157.198890625],
          [199.76946875, -59.23303515625, -29.940345703125, -79.73228125],
          [149.727625, 41.00326953125, -28.34062109375, -141.18746875]]
ptest6 = [[596.8451875, 0.0, 0.0, 596.8451875],
          [245.78221875, 0.0, 0.0, -245.78221875],
          [433.40378125, -140.238125, -88.751625, 361.48684375],
          [238.4015625, 154.838421875, 24.286923828125, 54.7362890625],
          [56.67294140625, -6.11514990234375, 34.39092578125, 44.62837109375],
          [114.1488359375, -8.485150390625, 30.0737734375, -109.7885546875]]

def getProcName(proc):
   procname = proc
   procname = procname.replace("P0_","")
   procname = procname.replace("P1_","")
   procname = procname.replace("P2_","")
   procname = procname.replace("_","")
   return procname

@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)

def invert_momenta(p):
   """ fortran/C-python do not order table in the same order"""
   new_p = []
   for i in range(len(p[0])):  new_p.append([0]*len(p))
   for i, onep in enumerate(p):
      for j, x in enumerate(onep):
         new_p[j][i] = x
   return new_p


def getXlibpath(changelibpath,firsttime=False):
   libmatrix = ""
   if(changelibpath):
      if(firsttime):
         p = subprocess.Popen("rm -rf "+libpathtmp+model.rndstr, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
         out, err = p.communicate()
         p = subprocess.Popen("mkdir -p "+libpathtmp+model.rndstr, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
         out, err = p.communicate()
         p = subprocess.Popen("/bin/cp -rf "+libpath+"matrix "+libpathtmp+model.rndstr+"/", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
         out, err = p.communicate()
      libmatrix = libpathtmp+model.rndstr+"/matrix/"
   else:
      libmatrix = libpath+"matrix/"
   return libmatrix






####################################################
####################################################
####################################################
### load the default model
print "\n$$$$$$$$$$$$$$$$$$$$ Initial model setup (loaded by default) $$$$$$$$$$$$$$$$$$$$"
model = t2HDM()
print "\n"
### reset the model
def resetModel(nameX,mX,typeX,sba,tanb):
   global model
   print "\n$$$$$$$$$$$$$$$$$$$$ Alternative model setup (loaded by the user choice) $$$$$$$$$$$$$$$$$$$$"
   model = t2HDM(nameX,mX,typeX,sba,tanb)
   print "\n"
####################################################
####################################################
####################################################



def compileSM():	
   X       = "matrix/"
   command = "./bin/mg5_aMC run/proc.SM.dat"
   procdirbase = "pp-SM-ttjets/SubProcesses/"
   procdirs = []
   for proc in diagramsSM:
      procdirs.append(procdirbase+proc+"/")
   matxdir = libpath+X
   libdir  = matxdir+"SM/"

   p = subprocess.Popen("rm -rf "+libdir, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   out, err = p.communicate()
   p = subprocess.Popen("mkdir -p "+libdir, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   out, err = p.communicate()
   for proc in diagramsSM:
      p = subprocess.Popen("mkdir -p "+libdir+"/"+proc, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      out, err = p.communicate()

   # enter the directory like this:
   with cd(mgpath):
      # make sure the old directory is removed
      p = subprocess.Popen("rm -rf "+procdirbase, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      out, err = p.communicate()

      # execute the generation of the process
      p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      out, err = p.communicate()

      p = subprocess.Popen("/bin/cp -f "+procdirbase+"makefile "+procdirbase+"makefile_ORIG", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      out, err = p.communicate()

      notMade = True
      for procdir in procdirs:
         # go to make the library
         with cd(procdir):
            proc = procdir
            proc = proc.replace(procdirbase,"")
            proc = proc.replace("/","")
            procname = getProcName(proc)
            if(notMade):
               p = subprocess.Popen("make", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
               out, err = p.communicate()
               notMade = False
         
            ### cahnge the makefile, make and copy
            p = subprocess.Popen("/bin/cp -f ../makefile_ORIG ../makefile", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            p = subprocess.Popen('sed -i -e "s/MENUM)py/MENUM)SM'+procname+'py/g" '+mgpath+procdir+'makefile', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            p = subprocess.Popen("make matrix2SM"+procname+"py.so", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            p = subprocess.Popen("cp matrix2SM"+procname+"py.so "+libdir+proc+"/", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            p = subprocess.Popen("cp ../../Cards/*.dat "+libdir+proc+"/", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            p = subprocess.Popen("mv "+libdir+proc+"/param_card_default.dat "+libdir+proc+"/param_card.dat_ORIG", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            p = subprocess.Popen("rm -f "+libdir+proc+"/*_default.dat", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()


def compileX():
   X       = "matrix/2HDM/"
   command = "./bin/mg5_aMC run/proc."+model.nameX+".dat"
   procdirbase = "pp-"+model.nameX+"-ttjets/SubProcesses/"
   S = ""
   if(model.nameX=="A"): S = "h"
   if(model.nameX=="H"): S = "h1"
   procdirs = []
   for proc in diagramsXX:
      procdirs.append(procdirbase+proc+"_no_"+S+"/")
   matxdir = libpath+X+model.nameX+"/"
   libdir  = matxdir

   p = subprocess.Popen("rm -rf "+libdir, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   out, err = p.communicate()
   p = subprocess.Popen("mkdir -p "+libdir, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   out, err = p.communicate()
   for proc in diagramsXX:
      p = subprocess.Popen("mkdir -p "+libdir+"/"+proc+"_no_"+S, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      out, err = p.communicate()

   # enter the directory like this:
   with cd(mgpath):
      # make sure the old directory is removed
      p = subprocess.Popen("rm -rf "+procdirbase, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      out, err = p.communicate()

      # modify the main parameters card
      ifname = "models/HEFTff/parameters.py_ORIG"
      ofname = ifname.replace("_ORIG","")
      p = subprocess.Popen("/bin/cp -f "+ifname+" "+ofname, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
      out, err = p.communicate()

      #############
      index = 0 ###
      #############

      replacements = {}
      if(model.nameX=="H"):
         replacements.update({' = 111.,':          ' = 100000000000.,'})
         replacements.update({' = 0.11111,':       ' = 100000000000.,'})
         replacements.update({' = 120.,':          ' = '+str(model.parameters[index].get("mH"))+','})
         replacements.update({' = 0.00575308848,': ' = '+str(model.parameters[index].get("wH"))+','})
      if(model.nameX=="A"):
         replacements.update({' = 111.,':          ' = '+str(model.parameters[index].get("mA"))+','})
         replacements.update({' = 0.11111,':       ' = '+str(model.parameters[index].get("wA"))+','})
         replacements.update({' = 120.,':          ' = 100000000000.,'})
         replacements.update({' = 0.00575308848,': ' = 100000000000.,'})
      replacements.update({' = 1.27,':          ' = '+str(model.parameters[index].get("YMC"))+','})
      replacements.update({' = 4.2,':           ' = '+str(model.parameters[index].get("YMB"))+','})
      replacements.update({' = 164.5,':         ' = '+str(model.parameters[index].get("YMT"))+','})
      replacements.update({' = 0.10567,':       ' = '+str(model.parameters[index].get("YMM"))+','})
      replacements.update({' = 1.778,':         ' = '+str(model.parameters[index].get("YMTAU"))+','})
      replacements.update({' = 172.,':          ' = 172.5,'})
      for sold in replacements.keys():
         snew = replacements[sold]
         # p = subprocess.Popen('sed -i -- "s/'+sold+'/'+snew+'/g" '+ofname, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)     
         p = subprocess.Popen('sed -i -e "s/'+sold+'/'+snew+'/g" '+ofname, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)     
         out, err = p.communicate()

      # execute the generation of the process
      p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      out, err = p.communicate()

      p = subprocess.Popen("/bin/cp -f "+procdirbase+"makefile "+procdirbase+"makefile_ORIG", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      out, err = p.communicate()

      notMade = True
      for procdir in procdirs:
         # go to make the library
         with cd(procdir):
            proc = procdir
            proc = proc.replace(procdirbase,"")
            proc = proc.replace("/","")
            procname = getProcName(proc)
            if(notMade):
               p = subprocess.Popen("make", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
               out, err = p.communicate()
               notMade = False
	
            ### cahnge the makefile, make and copy
            p = subprocess.Popen("/bin/cp -f ../makefile_ORIG ../makefile", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            p = subprocess.Popen('sed -i -e "s/MENUM)py/MENUM)'+model.nameX+procname+'py/g" '+mgpath+procdir+'makefile', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            p = subprocess.Popen("make matrix2"+model.nameX+procname+"py.so", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            p = subprocess.Popen("cp matrix2"+model.nameX+procname+"py.so "+libdir+proc+"/", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            p = subprocess.Popen("cp ../../Cards/*.dat "+libdir+proc+"/", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            p = subprocess.Popen("mv "+libdir+proc+"/param_card_default.dat "+libdir+proc+"/param_card.dat_ORIG", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            p = subprocess.Popen("rm -f "+libdir+proc+"/*_default.dat", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
   

def resetX(changelibpath):
   libmatrix = getXlibpath(changelibpath,True)
   nX = len(model.parameters)
   S = ""
   if(model.nameX=="A"): S = "h"
   if(model.nameX=="H"): S = "h1"
   libmatrixx = libmatrix+"2HDM/"+model.nameX+"/"
   for proc in diagramsXX:
      proc += "_no_"+S
      procdir = proc
      proc = getProcName(proc)
      fname = libmatrixx+procdir+"/param_card.dat"
      ### copy the ORIG param_card.dat to the curent one
      p = subprocess.Popen("/bin/cp -f "+fname+"_ORIG "+fname, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      out, err = p.communicate()
      
      #print "in -->",fname      
      #p = subprocess.Popen("touch "+fname+"_TEST", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      #out, err = p.communicate()
      
      #############
      index = 0 ###
      #############
      
      ### now change it
      replacements = {}
      if(model.nameX=="A"):
         replacements.update({'   25 1.000000e+11 # MH'          : '   25 %.6e # MH'          % model.parameters[index].get("mH")})
         replacements.update({'  9000006 5.000000e+02 # MP'      : '  9000006 %.6e # MP'      % model.parameters[index].get("mA")})
         replacements.update({'    4 3.550000e+00 # ymc'         : '    4 %.6e # ymc'         % model.parameters[index].get("YMC")})
         replacements.update({'    5 1.880000e+00 # ymb'         : '    5 %.6e # ymb'         % model.parameters[index].get("YMB")})
         replacements.update({'    6 4.312500e+02 # ymt'         : '    6 %.6e # ymt'         % model.parameters[index].get("YMT")})
         replacements.update({'   13 4.226400e-02 # ymm'         : '   13 %.6e # ymm'         % model.parameters[index].get("YMM")})
         replacements.update({'   15 7.108000e-01 # ymtau'       : '   15 %.6e # ymtau'       % model.parameters[index].get("YMTAU")})
         replacements.update({'DECAY  25 1.000000e+11 # WH'      : 'DECAY  25 %.6e # WH'      % model.parameters[index].get("wH")})
         replacements.update({'DECAY 9000006 1.439074e+02 # WH1' : 'DECAY 9000006 %.6e # WH1' % model.parameters[index].get("wA")})
      elif(model.nameX=="H"):
         replacements.update({'   25 5.000000e+02 # MH'          : '   25 %.6e # MH'          % model.parameters[index].get("mH")})
         replacements.update({'  9000006 1.000000e+11 # MP'      : '  9000006 %.6e # MP'      % model.parameters[index].get("mA")})
         replacements.update({'    4 -3.550000e+00 # ymc'        : '    4 %.6e # ymc'         % model.parameters[index].get("YMC")})
         replacements.update({'    5 1.880000e+00 # ymb'         : '    5 %.6e # ymb'         % model.parameters[index].get("YMB")})
         replacements.update({'    6 -4.312500e+02 # ymt'        : '    6 %.6e # ymt'         % model.parameters[index].get("YMT")})
         replacements.update({'   13 4.226400e-02 # ymm'         : '   13 %.6e # ymm'         % model.parameters[index].get("YMM")})
         replacements.update({'   15 7.108000e-01 # ymtau'       : '   15 %.6e # ymtau'       % model.parameters[index].get("YMTAU")})
         replacements.update({'DECAY  25 8.040533e+01 # WH'      : 'DECAY  25 %.6e # WH'      % model.parameters[index].get("wH")})
         replacements.update({'DECAY 9000006 1.000000e+11 # WH1' : 'DECAY 9000006 %.6e # WH1' % model.parameters[index].get("wA")})
      else:
         print "unsuported model %s - quitting" % model.nameX
         quit()
      for sold in replacements.keys():
         snew = replacements[sold]
         # p = subprocess.Popen('sed -i -- "s/'+sold+'/'+snew+'/g" '+fname, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)     
         p = subprocess.Popen('sed -i -e "s/'+sold+'/'+snew+'/g" '+fname, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)     
         out, err = p.communicate()
      
         #p = subprocess.Popen(snew+" >> "+fname+"_TEST", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)     
         #out, err = p.communicate()
         #print "   change: %s  --> %s" % (sold,snew)
      print "Changed parameters card in ",fname


#################################################################
#################################################################
#################################################################


def setModules(changelibpath):
   nX = len(model.parameters)
   S = ""
   if(model.nameX=="A"): S = "h"
   if(model.nameX=="H"): S = "h1"
   libmatrixx = getXlibpath(changelibpath)+"2HDM/"+model.nameX+"/"
   for proc in diagramsXX:
      proc += "_no_"+S
      procdir = proc
      proc = getProcName(proc)
      name = 'matrix2'+model.nameX+proc+'py'
      print "changing dir to: "+libmatrixx+procdir+"/"
      with cd(libmatrixx+procdir+"/"):
         print "in "+os.getcwd()+", trying to import ",name
         module_info = imp.find_module(name,[libmatrixx+procdir+"/"])
         model.modules.update({name:imp.load_module(name, *module_info)})
         model.modules[name].initialise(libmatrixx+procdir+"/param_card.dat")
         p = subprocess.Popen("rm -f "+libmatrixx+procdir+"/core.*", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
         out, err = p.communicate()
         print "Successfully initialised ",name
   libmatrixsm = getXlibpath(changelibpath)+"SM/"
   for proc in diagramsSM:
      procdir = proc
      proc = getProcName(proc)
      name = 'matrix2SM'+proc+'py'
      with cd(libmatrixsm+procdir+"/"):
         print "in "+os.getcwd()+", trying to import "+name
         module_info = imp.find_module(name,[libmatrixsm+procdir+"/"])
         model.modules.update({name:imp.load_module(name, *module_info)})
         model.modules[name].initialise(libmatrixsm+procdir+"/param_card.dat")
         p = subprocess.Popen("rm -f "+libmatrixsm+procdir+"/core.*", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
         out, err = p.communicate()
         print "Successfully initialised ",name


def testModules(changelibpath):
   setModules(changelibpath)
   S = ""
   if(model.nameX=="A"): S = "h"
   if(model.nameX=="H"): S = "h1"
   alphaS = 0.1 # just a random value
   nhel = 0     # sum over all helicity
   me2 = {}
   for proc in diagramsSM:
      p = ptest4
      if("P0" in proc):   p = ptest4
      elif("P1" in proc): p = ptest5
      elif("P2" in proc): p = ptest6
      else:
         print "ERROR - unknown SM process:", proc
         quit()
      procname = getProcName(proc)
      P=invert_momenta(p)
      me2.update({proc:model.modules['matrix2SM'+procname+'py'].get_me(P,alphaS,nhel)}) ### calculate the SM ME^2
      print "Done testing library SM %s" % (procname)
   for proc in diagramsXX:
      p = ptest4
      if("P0" in proc):   p = ptest4
      elif("P1" in proc): p = ptest5
      elif("P2" in proc): p = ptest6
      else:
         print "ERROR - unknown SM process:", proc
         quit()
      procname = getProcName(proc)+"no"+S
      P=invert_momenta(p)
      me2.update({proc+"_no_"+S:model.modules['matrix2'+model.nameX+procname+'py'].get_me(P,alphaS,nhel)}) ### calculate the X ME^2
      print "Done testing library 2HDM %s" % (procname)
   print me2

### for making all the libs SM/A/H
def make(test=True):
   compileSM()
   compileX()
   if(test): testModules(False)
   else:     setModules(False)
   nameX = "H" if(model.nameX=="A") else "A" ### compile the same setup with the other X...
   resetModel(nameX,model.mX,model.typeX,model.sba,model.tanb)
   compileX()
   if(test): testModules(False)
   else:     setModules(False)

### for resetting the A/H libs if these are already compiled with "make()"
def reset(nameX,mX,typeX,sba,tanb,test=True):
   resetModel(nameX,mX,typeX,sba,tanb)
   print "model nameX=%s,mX=%g,typeX=%g,sba=%g,tanb=%g" % (model.nameX,model.mX,model.typeX,model.sba,model.tanb)
   resetX(True)
   if(test): testModules(True)
   else:     setModules(True)
