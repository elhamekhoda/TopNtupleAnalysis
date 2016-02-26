#!/usr/bin/env python
from os import system,getcwd
from time import time
import socket, random, re

site=""
#outputName="resolved"
outputName="boosted"
#outputName="boosted_resolved"
if socket.gethostname().find("clratl") != -1:
	site="LPC"

listOfJobs=[]


def createAndSubmitSubJobForRanking(configName, Nsyst):
	system('mkdir -p '+outputName)
	
	here = getcwd()
	for i in range(Nsyst):
		scriptName = "script_"+configName.split('.')[0]+"_"+`i`+".sh"
		f = open(scriptName,'w')	
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
		f.write('cp -f '+here+'/RankingPlot.tar.gz .\n')
		f.write('tar -xzvf RankingPlot.tar.gz\n')
		f.write('echo "untaring done!" \n\n')
		
		f.write("./myFit.exe r "+configName+"   'Ranking="+`i`+"' > log_"+configName.split('.')[0]+"_r"+`i`+"\n")	
	
		outDir = './JobTtres_'+configName.split('.')[0].replace('ttres_','')
	
		f.write('cp -rf '+outDir+'/* '+here+'/'+outputName+'/'+outDir+'/\n')
		f.write('cp -f log_'+configName.split('.')[0]+'_*  '+here+'/'+outputName+'/\n')
		f.write('rm -rf '+WORKDIR+'\n')
		f.close()
	
		com=""
		if site=="LPC":
			#com = 'qsub -N '+outDir.split('_')[1]+'_'+`i`+' -q long64sl6@clratlserv03  -e '+here+'/'+outputName+' -o '+here+'/'+outputName+' '+scriptName
			com = 'qsub -N '+outDir.split('_')[1]+'_'+`i`+' -q multi64sl6@clratlserv05  -e '+here+'/'+outputName+' -o '+here+'/'+outputName+' '+scriptName
		
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




# S+B fit
sig = "Zprime2000"

fixFile('ttres_template.config', 'ttres_'+sig+'.config', sig, False)
createAndSubmitSubJobForRanking('ttres_'+sig+'.config', 88)

system("cp -r "+outputName+"/JobTtres_"+sig+" .")
system("tar -czvf RankingPlot.tar.gz .  --exclude=boosted* --exclude=resolved* --exclude=old* --exclude=*.tar.gz" )
system("rm -rf JobTtres_"+sig)
for j in listOfJobs:
	#continue
	print j
	system(j)

print "When all the jobs are then do:"
print "   ./myFit.exe  r  ttres_"+sig+".config  'Ranking=plot' "
