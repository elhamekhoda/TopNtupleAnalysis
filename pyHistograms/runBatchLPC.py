#!/usr/bin/env python

import HQTTtResonancesTools.DC15MC13TeV_25ns_mc15c_EXOT4
import HQTTtResonancesTools.DC15Data13TeV_25ns_207_EXOT4

import socket, random, re, time, os


# use it to setup AnalysisTop
# change this for the place where you setup RootCore
rundir = '/AtlasDisk/users/scalvet/Zprime/AnalysisTop-2.4.25_analysis/'

useTrkJet = 0

# output directory
# change this for your output directory
outputDir = '/AtlasDisk/users/scalvet/Zprime/AnalysisTop-2.4.25_analysis_output_nom_calo/'
if useTrkJet:
   outputDir = '/AtlasDisk/users/scalvet/Zprime/AnalysisTop-2.4.25_analysis_output_nom_trk/'
os.system("mkdir -p "+outputDir)

plateform = socket.gethostname()
WORKDIR    = "temp"
tarfile    = outputDir+"/analysis.tar.gz"
'''
Functions to write down the initialisation
'''
def WriteScript_Init(scriptName):
	f = open(scriptName,'w')
	if plateform.find("clratl") != -1:
		WriteScript_Init_clr(f)
	#if plateform.find("ccage") != -1:
	#	WriteScript_Init_ccin2p3(f)
	return f
		
def WriteScript_Init_clr(f):
	f.write('#!/bin/bash\n')
	workDir = re.sub('\.','',str(time.time())+`random.randint(0, 1000000)`)
	WORKDIR = "/users_local1/$LOGNAME/"+workDir
	f.write('echo running on $HOSTNAME\n')
	f.write('\n')
	f.write('mkdir -p /users_local1/$LOGNAME/\n')
	f.write('cd /users_local1/$LOGNAME/\n')
	f.write('pwd\n')
	f.write('df -h .\n')	
	f.write('\n' + 'mkdir -p '+WORKDIR)
	f.write('\n' + 'cd '+WORKDIR)
	f.write('\n')
	f.write('pwd')
	f.write('\n')			
	f.write('\n ls \n')
	f.write('export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase\n')
	f.write('source /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/user/atlasLocalSetup.sh\n')
	f.write('\n')
	f.write('cp -f '+tarfile+' .\n')
	f.write('\n ls \n')
	f.write('\n echo untaring the tarball \n')
	f.write('tar -xzf '+tarfile.split("/")[-1]+'\n')
	f.write('rm -f *.tar.gz \n')
	f.write('\n echo ...untaring done \n')
	f.write('\n ls \n')
	f.write('\n')
	f.write('setupATLAS\n') 
	f.write('lsetup rcsetup\n')
	f.write('\n')

'''
Functions to write down the exe, and copy of the output files
'''
def WriteScript_End(f):
	if plateform.find("clratl") != -1:
		f.write('\n' + 'pwd | awk -F  \'/\' \'{print "rm -rf /"$2"/"$3"/"$4}\' |sh '  )
	if plateform.find("ccage") != -1:
		aaaaa=1 #nothing to do
	f.write('\n')

def main():
	# for standard data and MC

	# change this for your samples
	ntuplesDir = '/AtlasDisk/group/Zprime/AT-2.4.25v2/SR/' #calo
	pattern = 'user.scalvet.*AT2425.v2.0SR_output.root'
	pattern_data = 'user.scalvet.00*AT2425.v1.0SR_output.root'
	pattern_syst = 'user.scalvet.*04122016Systv*_output.root'
	pattern_pdf = 'user.scalvet.*04122016PDFv*_output.root'
	# for QCD e
	pattern_qcde = 'user.scalvet.*04122016QCDev*_output.root'
	pattern_qcdmu = 'user.scalvet.*04122016QCDmuv*_output.root'
	if useTrkJet:
		ntuplesDir = '/AtlasDisk/group/Zprime/AT-2.4.25v1/SR/' #trk
		pattern = 'user.scalvet.*AT2425.v1.0SR_output.root'
		pattern_data = 'user.scalvet.00*AT2425.v1.0SR_output.root'
		pattern_syst = 'user.scalvet.*04122016Systv*_output.root'
		pattern_pdf = 'user.scalvet.*04122016PDFv*_output.root'
		# for QCD e
		pattern_qcde = 'user.scalvet.*04122016QCDev*_output.root'
		pattern_qcdmu = 'user.scalvet.*04122016QCDmuv*_output.root'
	theScope = 'user.scalvet'
	

	# number of files per job
	#nFilesPerJob = 40
	nFilesPerJob = 8

	
	if os.path.exists(tarfile)==0:
		com = "cd ../../; tar -czvf "+tarfile+" . --exclude=output*.root --exclude=LPCTools  --exclude=.svn "
		print com
		os.system(com)

	
	# email to use to tell us when the job is done
	email = 'scalvet@cern.ch'

	# queue to submit to
	queue = 'long64sl6@clratlserv03'
	#queue = '1nd'
	#queue = '1nw'
	#queue = '8nh'
	#queue = 'short.q'

	# the default is AnaTtresSL, which produces many control plots for tt res.
	# The Mtt version produces a TTree to do the limit setting
	# the QCD version aims at plots for QCD studies using the matrix method
	# look into read.cxx to see what is available
	# create yours, if you wish
	analysisType='AnaTtresSL'
	
	# leave it for nominal to run only the nominal
	systematics = 'nominal'
	#systematics = 'all'
	#systematics = 'all1'
	#systematics = 'all2'
	#systematics = 'all3'
	#systematics = 'all4'
	
	# 25 ns datasets
	names   = []

	#names  += ['tt']
	#names  += ['tthm']
	#names  += ['ttv']
	names  += ['wbbjets']
	names  += ['wccjets']
	names  += ['wcjets']
	names  += ['wljets']
	#names  += ['singletop']

	#names  += ['zjets']
	#names  += ['vv']

	#names  += ["data"]
	#names  += ['qcde', 'qcdmu']

#	names  += ['zprime400']
#	names  += ['zprime500']
#	names  += ['zprime750']
#	names  += ['zprime1000']
#	names  += ['zprime1250']
#	names  += ['zprime1500']
#	names  += ['zprime1750']
#	names  += ['zprime2000']
#	names  += ['zprime2250']
#	names  += ['zprime2500']
#	names  += ['zprime2750']
#	names  += ['zprime3000']
#	names  += ['zprime4000']
#	names  += ['zprime5000']
	#names  += ['kkgrav400']
	#names  += ['kkgrav500']
	#names  += ['kkgrav750']
	#names  += ['kkgrav1000']
	#names  += ['kkgrav2000']
	#names  += ['kkgrav3000']

	#names  += ['ttsyst']
	#names  += ['ttpdf']
	#names  += ['ttpowhegherwig']
	#names  += ['ttmcatnloherwig']
	#names  += ['ttradhi', 'ttradlo']

	#names  += ['eftl30c10']
	#names  += ['eftl35c10']
	#names  += ['eftl40c10']
	#names  += ['eftl45c10']
	#names  += ['eftl50c10']
	#names  += ['eftl55c10']
	#names  += ['eftl60c10']
	#names  += ['eftl100c10']

	mapToSamples = {
					'wbbjets': 'MC15c_13TeV_25ns_FS_EXOT4_Wjets22',
					'wccjets': 'MC15c_13TeV_25ns_FS_EXOT4_Wjets22',
					'wcjets': 'MC15c_13TeV_25ns_FS_EXOT4_Wjets22',
					'wljets': 'MC15c_13TeV_25ns_FS_EXOT4_Wjets22',
					'data': 'Data15_13TeV_25ns_207_EXOT4,Data16_13TeV_25ns_33257ipb_EXOT4',
					'qcde': 'Data15_13TeV_25ns_207_EXOT4,Data16_13TeV_25ns_33257ipb_EXOT4',
					'qcdmu': 'Data15_13TeV_25ns_207_EXOT4,Data16_13TeV_25ns_33257ipb_EXOT4',
					'tt':'MC15c_13TeV_25ns_FS_EXOT4_ttbarPowhegPythia', #,MC15c_13TeV_25ns_FS_EXOT4_ttbarPowhegPythia_mttsliced',
					'tthm': 'MC15c_13TeV_25ns_FS_EXOT4_ttbarPowhegPythia_mttsliced',
					'ttv':'MC15c_13TeV_25ns_FS_EXOT4_ttbarV',
					'ttsyst':'MC15c_13TeV_25ns_FS_EXOT4_ttbarPowhegPythia',
					'ttpdf':'MC15c_13TeV_25ns_FS_EXOT4_ttbaraMcAtNlo_PDF',
					'ttpowhegherwig':'MC15c_13TeV_25ns_FS_EXOT4_ttbarPowhegHerwig',
					'ttmcatnloherwig':'MC15c_13TeV_25ns_FS_EXOT4_ttbarMCAtNLOHerwig',
					'ttradhi':'MC15c_13TeV_25ns_FS_EXOT4_ttbarRadHi',
					'ttradlo':'MC15c_13TeV_25ns_FS_EXOT4_ttbarRadLo',
					'singletop':'MC15c_13TeV_25ns_FS_EXOT4_singletop',
					'zjets':'MC15c_13TeV_25ns_FS_EXOT4_Zjets22',
					'vv': 'MC15c_13TeV_25ns_FS_EXOT4_VV',
					'zprime400': 'MC15c_13TeV_25ns_FS_EXOT4_Zprime400',
					'zprime500': 'MC15c_13TeV_25ns_FS_EXOT4_Zprime500',
					'zprime750': 'MC15c_13TeV_25ns_FS_EXOT4_Zprime750',
					'zprime1000': 'MC15c_13TeV_25ns_FS_EXOT4_Zprime1000',
					'zprime1250': 'MC15c_13TeV_25ns_FS_EXOT4_Zprime1250',
					'zprime1500': 'MC15c_13TeV_25ns_FS_EXOT4_Zprime1500',
					'zprime1750': 'MC15c_13TeV_25ns_FS_EXOT4_Zprime1750',
					'zprime2000': 'MC15c_13TeV_25ns_FS_EXOT4_Zprime2000',
					'zprime2250': 'MC15c_13TeV_25ns_FS_EXOT4_Zprime2250',
					'zprime2500': 'MC15c_13TeV_25ns_FS_EXOT4_Zprime2500',
					'zprime2750': 'MC15c_13TeV_25ns_FS_EXOT4_Zprime2750',
					'zprime3000': 'MC15c_13TeV_25ns_FS_EXOT4_Zprime3000',
					'zprime4000': 'MC15c_13TeV_25ns_FS_EXOT4_Zprime4000',
					'zprime5000': 'MC15c_13TeV_25ns_FS_EXOT4_Zprime5000',
					'kkgrav400': 'MC15c_13TeV_25ns_FS_EXOT4_Gtt400',
					'kkgrav500': 'MC15c_13TeV_25ns_FS_EXOT4_Gtt500',
					'kkgrav750': 'MC15c_13TeV_25ns_FS_EXOT4_Gtt750',
					'kkgrav1000': 'MC15c_13TeV_25ns_FS_EXOT4_Gtt1000',
					'kkgrav2000': 'MC15c_13TeV_25ns_FS_EXOT4_Gtt2000',
					'kkgrav3000': 'MC15c_13TeV_25ns_FS_EXOT4_Gtt3000',
					'eftl30c1': 'MC15c_13TeV_25ns_FS_EXOT4_ttbarLO',
					'eftl35c1': 'MC15c_13TeV_25ns_FS_EXOT4_ttbarLO',
					'eftl40c1': 'MC15c_13TeV_25ns_FS_EXOT4_ttbarLO',
					'eftl45c1': 'MC15c_13TeV_25ns_FS_EXOT4_ttbarLO',
					'eftl50c1': 'MC15c_13TeV_25ns_FS_EXOT4_ttbarLO',
					'eftl55c1': 'MC15c_13TeV_25ns_FS_EXOT4_ttbarLO',
					'eftl60c1': 'MC15c_13TeV_25ns_FS_EXOT4_ttbarLO',
					'eftl100c1': 'MC15c_13TeV_25ns_FS_EXOT4_ttbarLO',
					'eftl30c10': 'MC15c_13TeV_25ns_FS_EXOT4_ttbarLO',
					'eftl35c10': 'MC15c_13TeV_25ns_FS_EXOT4_ttbarLO',
					'eftl40c10': 'MC15c_13TeV_25ns_FS_EXOT4_ttbarLO',
					'eftl45c10': 'MC15c_13TeV_25ns_FS_EXOT4_ttbarLO',
					'eftl50c10': 'MC15c_13TeV_25ns_FS_EXOT4_ttbarLO',
					'eftl55c10': 'MC15c_13TeV_25ns_FS_EXOT4_ttbarLO',
					'eftl60c10': 'MC15c_13TeV_25ns_FS_EXOT4_ttbarLO',
					'eftl100c10': 'MC15c_13TeV_25ns_FS_EXOT4_ttbarLO',
		   }
	import TopExamples.grid
	
	
	import glob
	import sys
	
	# get list of processed datasets
	dirs = glob.glob(ntuplesDir+'/*')
	import rucio.client
	rucio = rucio.client.Client()
	response = rucio.list_dids(scope = theScope, filters = {'name' : pattern})
	datasets = []
	for l in response:
		datasets.append(l)
	response = rucio.list_dids(scope = theScope, filters = {'name' : pattern_qcde})
	datasets_qcde = []
	for l in response:
		datasets_qcde.append(l)
	response = rucio.list_dids(scope = theScope, filters = {'name' : pattern_qcdmu})
	datasets_qcdmu = []
	for l in response:
		datasets_qcdmu.append(l)

	#response = rucio.list_dids(scope = theScope, filters = {'name' : pattern_mtt})
	#datasets_mtt = []
	#for l in response:
	#	datasets_mtt.append(l)

	response = rucio.list_dids(scope = theScope, filters = {'name' : pattern_data})
	datasets_data = []
	for l in response:
		datasets_data.append(l)

	response = rucio.list_dids(scope = theScope, filters = {'name' : pattern_syst})
	datasets_syst = []
	for l in response:
		datasets_syst.append(l)

	response = rucio.list_dids(scope = theScope, filters = {'name' : pattern_pdf})
	datasets_pdf = []
	for l in response:
		datasets_pdf.append(l)

	# each "sample" below means an item in the list names above
	# there may contain multiple datasets
	# for each sample we want to read
	for sn in names:
		sname = mapToSamples[sn]
		sample = None
		for it in sname.split(','):
			samples = TopExamples.grid.Samples([it])
			if sample == None:
				sample = samples[0]
			else:
				sample.datasets.extend(samples[0].datasets)

		forJobs = {}
		nJob = 0
		nFile = 0

		nFilesPerJobEffective = nFilesPerJob
		if 'tthm' in sn:
			nFilesPerJobEffective = 1
		elif 'tt' in sn:
			nFilesPerJobEffective = 10
		elif 'eft' in sn:
			nFilesPerJobEffective = 1
		elif 'singletop' in sn:
			nFilesPerJobEffective = 5
		elif 'kkgrav' in sn:
			nFilesPerJobEffective = 1
		elif 'zprime' in sn:
			nFilesPerJobEffective = 10
		elif 'data' in sn or 'qcd' in sn:
			nFilesPerJobEffective = 300

		# write list of files to be read when processing this sample
		f = open(outputDir+"/input_"+sn+'.txt', 'w')
		# output file after running read
		outfile = sn
		
		# go over all directories in the ntuplesDir
		ds = datasets
		if sn == 'qcde':
			ds = datasets_qcde
		elif sn == 'qcdmu':
			ds = datasets_qcdmu
		#elif sn == 'tthm' or sn == 'singletop':
		#	ds = datasets_mtt
		elif sn == 'ttpdf':
			ds = datasets_pdf
		elif sn in ['ttpowhegherwig', 'ttmcatnloherwig', 'ttradhi', 'ttradlo']:
			ds = datasets_syst
		elif sn == 'data':
			ds = datasets_data
		for d in ds:
			# remove path and get only dir name in justfile
			#justfile = d.split('/')[-1]
			dsid_dir = d.split('.')[2] # get the DSID of the directory
			# this will include all directories, so check if this director is in the sample
	
			# now go over the list of datasets in sample
			# and check if this DSID is there
			for s in sample.datasets:
				if len(s.split(':')) > 1:
					s = s.split(':')[1] # skip mc15_13TeV
				dsid_sample = s.split('.')[1] # get DSID
				if dsid_dir == dsid_sample: # this dataset belongs in the sample in the big for loop
					# get all files in the directory
					#print ntuplesDir+'/'+d
					# get all files in the directory
					files = glob.glob(ntuplesDir+'/'+d+'/*.root*')
					
					# and write it in ht elist of input files to process
					for item in files:
						if not '.part' in item:
							f.write(item+'\n')
							if nFile == nFilesPerJobEffective:
								nFile = 0
								nJob = nJob + 1
							if nFile == 0:
								forJobs[str(nJob)] = []
							forJobs[str(nJob)].append(item+'\n')
							nFile = nFile + 1
		f.close()
		theSysts = systematics
		isData = ''
		extra = ''
		if "data" in sn:
			theSysts = "nominal"
			isData = ' -d '
		elif "qcde" in sn:
			theSysts = "nominal"
			isData = ' -d -Q e '
		elif "qcdmu" in sn:
			theSysts = "nominal"
			isData = ' -d -Q mu '
		elif "pdf" in sn:
			isData = ' --pdf PDF4LHC15_nlo_30 --noMttSlices '
			theSysts = "pdf"
		elif "ttsyst" in sn:
			isData = ' --noMttSlices '
			theSysts = "nominal"
		elif sn in ['ttpowhegherwig', 'ttmcatnloherwig', 'ttradhi', 'ttradlo']:
			theSysts = "nominal"
			isData = ' --noMttSlices '
		
		if "wbbjets" in sn:
			extra = ' --WjetsHF bb '
		elif 'wccjets' in sn:
			extra = ' --WjetsHF cc'
		elif 'wcjets' in sn:
			extra = ' --WjetsHF c'
		elif 'wljets' in sn:
			extra = ' --WjetsHF l'
		if 'eft' in sn:
			extraEFT = {
					'eftl30c1': ' --EFT 3000,1',
					'eftl35c1': ' --EFT 3500,1',
					'eftl40c1': ' --EFT 4000,1',
					'eftl45c1': ' --EFT 4500,1',
					'eftl50c1': ' --EFT 5000,1',
					'eftl55c1': ' --EFT 5500,1',
					'eftl60c1': ' --EFT 6000,1',
					'eftl100c1': ' --EFT 10000,1',
					'eftl30c10': ' --EFT 3000,10',
					'eftl35c10': ' --EFT 3500,10',
					'eftl40c10': ' --EFT 4000,10',
					'eftl45c10': ' --EFT 4500,10',
					'eftl50c10': ' --EFT 5000,10',
					'eftl55c10': ' --EFT 5500,10',
					'eftl60c10': ' --EFT 6000,10',
					'eftl100c10': ' --EFT 10000,10',
					}
			extra = extraEFT[sn]
	
		#extra += '  --applyMET 80 '

		for job in forJobs:
			jobName = sn+'_'+job
			print jobName
			infile = outputDir+"/input_"+jobName+'.txt'
			infullfile = outputDir+"/input_"+sn+'.txt'
			f = open(infile, 'w')
			for item in forJobs[job]:
				f.write(item)
			f.close()
			logfile = outputDir+"/stdout_"+jobName+'.txt'
			os.system('rm -f %s' % logfile)
			runfile = outputDir+"/run_"+jobName+'.sh'
			fr =  WriteScript_Init(runfile)
			fr.write('cd TopNtupleAnalysis/pyHistograms\n')
			tmpDir = '.'

			#out = 'be,'+outputDir+'/be_'+jobName+'.root\;bmu,'+outputDir+'/bmu_'+jobName+'.root\;re,'+outputDir+'/re_'+jobName+'.root\;rmu,'+outputDir+'/rmu_'+jobName+'.root\;be2015,'+outputDir+'/be2015_'+jobName+'.root\;bmu2015,'+outputDir+'/bmu2015_'+jobName+'.root\;re2015,'+outputDir+'/re2015_'+jobName+'.root\;rmu2015,'+outputDir+'/rmu2015_'+jobName+'.root\;be2016,'+outputDir+'/be2016_'+jobName+'.root\;bmu2016,'+outputDir+'/bmu2016_'+jobName+'.root\;re2016,'+outputDir+'/re2016_'+jobName+'.root\;rmu2016,'+outputDir+'/rmu2016_'+jobName+'.root'
			out = 'be,'+tmpDir+'/be_'+jobName+'.root\;bmu,'+tmpDir+'/bmu_'+jobName+'.root\;re,'+tmpDir+'/re_'+jobName+'.root\;rmu,'+tmpDir+'/rmu_'+jobName+'.root'
			out += '\;be3,'+tmpDir+'/be3_'+jobName+'.root\;bmu3,'+tmpDir+'/bmu3_'+jobName+'.root\;re3,'+tmpDir+'/re3_'+jobName+'.root\;rmu3,'+tmpDir+'/rmu3_'+jobName+'.root'
			out += '\;be2,'+tmpDir+'/be2_'+jobName+'.root\;bmu2,'+tmpDir+'/bmu2_'+jobName+'.root\;re2,'+tmpDir+'/re2_'+jobName+'.root\;rmu2,'+tmpDir+'/rmu2_'+jobName+'.root'
			out += '\;be1,'+tmpDir+'/be1_'+jobName+'.root\;bmu1,'+tmpDir+'/bmu1_'+jobName+'.root\;re1,'+tmpDir+'/re1_'+jobName+'.root\;rmu1,'+tmpDir+'/rmu1_'+jobName+'.root'
			out += '\;be0,'+tmpDir+'/be0_'+jobName+'.root\;bmu0,'+tmpDir+'/bmu0_'+jobName+'.root\;re0,'+tmpDir+'/re0_'+jobName+'.root\;rmu0,'+tmpDir+'/rmu0_'+jobName+'.root'
			sumOfWeights = "sumOfWeights_calo.txt"
			if useTrkJet: sumOfWeights = "sumOfWeights_trk.txt"
			fr.write('cp -f '+sumOfWeights+' sumOfWeights_new.txt\n')
			
			useTrk = ""
			#if useTrkJet: useTrk=" --useTrkJetForChi2 "
			
			fr.write('./makeHistograms.py - '+isData+'   '+extra+' --noMttSlices --files '+infile+' --analysis '+analysisType+' --output '+out+'   --systs '+theSysts+' '+useTrk+'\n')
			fr.write('cp %s/*_%s.root %s/' % (tmpDir, jobName, outputDir))
			WriteScript_End(fr)
			fr.close()
			os.system('chmod a+x '+runfile)
			subcmd = 'qsub -N '+jobName+' -q '+queue+'  -e '+outputDir+' -o '+outputDir+' ' + runfile
			print subcmd
			os.system(subcmd)

if __name__ == '__main__':
	import os
	main()

