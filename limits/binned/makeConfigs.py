#!/usr/bin/env python
from os import system,getcwd
from time import time
from inputs import *
import socket, random, re



dobatch = 1
site=""
#outputName="resolved"
outputName="boosted"
#outputName="boosted_resolved"
if socket.gethostname().find("clratl") != -1:
	site="LPC"

listOfJobs=[]

def createAndSubmitJob(configName):
	system('mkdir -p '+outputName)
	
	here = getcwd()
	
	f = open("script_"+configName.split('.')[0]+".sh",'w')	
	f.write('#!/bin/bash\n')
	f.write('echo running on $HOSTNAME\n')
	f.write('\n')
	WORKDIR=""
	if site=="LPC":
		workDir = re.sub('\.','',str(time())+`random.randint(0, 1000000)`)
		WORKDIR = "/users_local1/$LOGNAME/"+workDir
	else :
		print "ERROR : site is not defiend!"
		return
		
	f.write('\n' + 'mkdir -p '+WORKDIR+'\n')
	f.write('\n' + 'cd '+WORKDIR+'\n')
	f.write('export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase\n')
	f.write('source /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/user/atlasLocalSetup.sh\n')
	f.write('localSetupROOT\n')
	f.write('\n')
	f.write('cp -f '+here+'/t.tar.gz .\n')
	f.write('tar -xzvf t.tar.gz\n')
	f.write('echo "untaring done!" \n\n')
	
	f.write('./myFit.exe h '+configName+' > log_'+configName.split('.')[0]+'_h\n')
	f.write('./myFit.exe d '+configName+' > log_'+configName.split('.')[0]+'_d\n')
	f.write('./myFit.exe w '+configName+' > log_'+configName.split('.')[0]+'_w\n')
	f.write('./myFit.exe f '+configName+' > log_'+configName.split('.')[0]+'_f\n')
	f.write('./myFit.exe p '+configName+' > log_'+configName.split('.')[0]+'_p\n')
	if configName.find("bkg")!=-1:
		#do nothing
		a=1
	else:
		f.write('./myFit.exe l '+configName+' > log_'+configName.split('.')[0]+'_l\n')
		#f.write('./myFit.exe r '+configName+' > log_'+configName.split('.')[0]+'_r\n')
	
	
	
	outDir = './JobTtres_'+configName.split('.')[0].replace('ttres_','')
	
	f.write('cp -rf '+outDir+' '+here+'/'+outputName+'\n')
	f.write('cp -f log_'+configName.split('.')[0]+'_*  '+here+'/'+outputName+'/'+outDir+'/\n')
	f.write('rm -rf '+WORKDIR+'\n')
	f.close()
	
	com=""
	if site=="LPC":
		com = 'qsub -N '+outDir.split('_')[1]+' -q multi64sl6@clratlserv05  -e '+here+'/'+outputName+' -o '+here+'/'+outputName+' script_'+configName.split('.')[0]+'.sh'
		
	#print com
	global listOfJobs
	listOfJobs+=[com,]
	
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
      continue
    
    nline = line
    if 'FitTtres' in nline:
      nline = nline.replace('FitTtres', 'FitTtres_'+i)
    if 'JobTtres' in nline:
      nline = nline.replace('JobTtres', 'JobTtres_'+i)
    if 'FitType' in nline and doBOnlyFit:
      nline = nline.replace('SPLUSB', 'BONLY')
    f.write(nline)

  f.close()
  fr.close()




# B ONLY fit
fixFile('ttres_template.config', 'ttres_bkg.config', "bkg", True)
system('cp -f hist_Zprime2000.root hist_bkg.root') ## use a dummy signal for the background only fit
if dobatch:
	createAndSubmitJob('ttres_bkg.config')
else:
	system('./myFit.exe h ttres_bkg.config')
	system('./myFit.exe d ttres_bkg.config')
	system('./myFit.exe w ttres_bkg.config')
	system('./myFit.exe f ttres_bkg.config')
	system('./myFit.exe p ttres_bkg.config')



# now go over to signal
for i in signalList:
  fixFile('ttres_template.config', 'ttres_'+i+'.config', i, False)

  if dobatch:
     createAndSubmitJob('ttres_'+i+'.config')
  else:
     system('./myFit.exe h ttres_'+i+'.config')
     system('./myFit.exe d ttres_'+i+'.config')
     system('./myFit.exe w ttres_'+i+'.config')
     system('./myFit.exe f ttres_'+i+'.config')
     system('./myFit.exe p ttres_'+i+'.config')
     system('./myFit.exe l ttres_'+i+'.config')




if dobatch :
	system("tar -czvf t.tar.gz . --exclude=JobTtres_* --exclude=old* --exclude=*.tar.gz" )
	for j in listOfJobs:
		print j
		system(j)
	
