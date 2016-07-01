#!/usr/bin/env python

import HQTTtResonancesTools.DC15MC13TeV_25ns_mc15c_EXOT4
import HQTTtResonancesTools.DC15Data13TeV_25ns_207_EXOT4

def main():
	# input directory
	#ntuplesDir = '/nfs/dust/atlas/user/danilo/20062016v1'
	pattern = 'user.dferreir.*24062016v1_output.root'
	theScope = 'user.dferreir'
	
	# output directory
	#outputDir = '/afs/desy.de/user/d/danilo/xxl/af-atlas/Top2412/TopNtupleAnalysis/pyHistograms/hists_sr_nosyst'
	outputDir = '/afs/desy.de/user/d/danilo/xxl/af-atlas/Top2412/TopNtupleAnalysis/pyHistograms/hists_sr'

	# number of files per job
	nFilesPerJob = 40
	#nFilesPerJob = 8

	# use it to setup AnalysisTop
	rundir = '/afs/desy.de/user/d/danilo/xxl/af-atlas/Top2412'

	# email to use to tell us when the job is done
	email = 'dferreir@cern.ch'

	# queue to submit to
	#queue = '1nd'
	queue = 'short.q'
	#queue = 'default.q'

	# the default is AnaTtresSL, which produces many control pltos for tt res.
	# The Mtt version produces a TTree to do the limit setting
	# the QCD version aims at plots for QCD studies using the matrix method
	# look into read.cxx to see what is available
	# create yours, if you wish
	#analysisType='AnaWjetsCR'
	analysisType='AnaTtresSL'
	
	# leave it for nominal to run only the nominal
	#systematics = 'nominal'
	systematics = 'all'
	
	# 25 ns datasets
	names   = []
	names  += ['tt']
	names  += ['wbbjets']
	names  += ['wccjets']
	names  += ['wcjets']
	names  += ['wljets']
	names  += ['zjets']

	names  += ["data"]
	names  += ['singletop']
	names  += ['vv']

	names  += ["data"]

	names  += ['zprime400']
	names  += ['zprime500']
	names  += ['zprime750']
	names  += ['zprime1000']
	names  += ['zprime1250']
	names  += ['zprime1500']
	names  += ['zprime1750']
	names  += ['zprime2000']
	names  += ['zprime2250']
	names  += ['zprime2500']
	names  += ['zprime2750']
	names  += ['zprime3000']
	names  += ['zprime4000']
	names  += ['zprime5000']

	names  += ['kkgrav400']
	names  += ['kkgrav500']
	names  += ['kkgrav750']
	names  += ['kkgrav1000']
	names  += ['kkgrav2000']
	names  += ['kkgrav3000']

	mapToSamples = {
					'wbbjets': 'MC15c_13TeV_25ns_FS_EXOT4_Wjets22',
					'wccjets': 'MC15c_13TeV_25ns_FS_EXOT4_Wjets22',
					'wcjets': 'MC15c_13TeV_25ns_FS_EXOT4_Wjets22',
					'wljets': 'MC15c_13TeV_25ns_FS_EXOT4_Wjets22',
					'data': 'Data15_13TeV_25ns_207_EXOT4,Data16_13TeV_25ns_207_EXOT4',
					'tt':'MC15c_13TeV_25ns_FS_EXOT4_ttbarPowhegPythia,MC15c_13TeV_25ns_FS_EXOT4_ttbarPowhegPythia_mttsliced',
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
		   }
	
	import TopExamples.grid
	
	
	import glob
	import os
	import sys
	# get list of processed datasets
	#dirs = glob.glob(ntuplesDir+'/*')

	import rucio.client
	rucio = rucio.client.Client()
	response = rucio.list_dids(scope = theScope, filters = {'name' : pattern})
	datasets = []
	for l in response:
		datasets.append(l)
	
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
		if 'tt' in sn:
			nFilesPerJobEffective = 10
			#nFilesPerJobEffective = 2

		# write list of files to be read when processing this sample
		f = open(outputDir+"/input_"+sn+'.txt', 'w')
		# output file after running read
		outfile = sn
		
		# go over all directories in the ntuplesDir
		for d in datasets:
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
					#files = glob.glob(d+'/*.root*')

					from subprocess import Popen, PIPE
					process = Popen(["rucio", "list-file-replicas", "--protocols", "root", d], stdout=PIPE)
					(output, err) = process.communicate()
					#exit_code = process.wait()
					pfns = {}
					for line in output.split('\n'):
						outline = line.split()
						if not 'root://' in line:
							continue
						fname = outline[3]
						site = outline[10][0:-1]
						pfno = outline[11]
						idx = pfno.find('/', len("root://")+2)
						pfn = pfno[:idx] + "/" + pfno[idx:]
						if not fname in pfns:
							pfns[fname] = {}
						pfns[fname][site] = pfn
					files = []
					for fname in pfns:
						if 'DESY-HH_LOCALGROUPDISK' in pfns[fname]:
							files.append(pfns[fname]['DESY-HH_LOCALGROUPDISK'])
						else:
							#print "File %s is not available in DESY! It is available on " % fname, pfns[fname]
							k = pfns[fname].keys()[0]
							files.append(pfns[fname][k])
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
					# go to the next directory in the same sample
					break
		f.close()
		theSysts = systematics
		isData = ''
		extra = ''
		if "data" in sn:
			theSysts = "nominal"
			isData = ' -d '
		if "wbbjets" in sn:
			extra = ' --WjetsHF bb '
		elif 'wccjets' in sn:
			extra = ' --WjetsHF cc'
		elif 'wcjets' in sn:
			extra = ' --WjetsHF c'
		elif 'wljets' in sn:
			extra = ' --WjetsHF l'
	
		for job in forJobs:
			jobName = sn+'_'+job
			infile = outputDir+"/input_"+jobName+'.txt'
			infullfile = outputDir+"/input_"+sn+'.txt'
			f = open(infile, 'w')
			for item in forJobs[job]:
				f.write(item)
			f.close()
			logfile = outputDir+"/stdout_"+jobName+'.txt'
			runfile = outputDir+"/run_"+jobName+'.sh'
			fr = open(runfile, 'w')
			fr.write('#!/bin/sh\n')
			fr.write('#$ -cwd\n')
			fr.write('#$ -j y\n')
			fr.write('#$ -l cvmfs\n')
			fr.write('#$ -l distro=sld6\n')
			fr.write('#$ -l arch=amd64\n')
			fr.write('#$ -l h_vmem=3G\n')
			fr.write('#$ -o '+logfile+'\n')
			fr.write('#$ -q '+queue+'\n')
			fr.write('#$ -m '+'eas'+'\n')
			fr.write('#$ -M '+email+'\n')
			fr.write('#$ -N tnapy_'+jobName+'\n')
			# bsub options
			#fr.write('#$ -e '+logfile+'\n')
			#fr.write('#$ -o '+logfile+'\n')
			#fr.write('#$ -q '+queue+'\n')
			#fr.write('#$ -N '+''+'\n')
			#fr.write('#$ -u '+email+'\n')
			#fr.write('#$ -J tnapy_'+jobName+'\n')
			fr.write('cd '+rundir+'\n')
			fr.write('export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase\n')
			fr.write('export DQ2_LOCAL_SITE_ID=DESY-HH_SCRATCHDISK \n')
			fr.write('source /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/user/atlasLocalSetup.sh\n')
			fr.write('export X509_USER_PROXY=$HOME/.globus/job_proxy.pem\n')
			fr.write('lsetup rcsetup\n')
			fr.write('cd TopNtupleAnalysis/pyHistograms\n')
			out = 'be:'+outputDir+'/be_'+jobName+'.root,bmu:'+outputDir+'/bmu_'+jobName+'.root,re:'+outputDir+'/re_'+jobName+'.root,rmu:'+outputDir+'/rmu_'+jobName+'.root,be2015:'+outputDir+'/be2015_'+jobName+'.root,bmu2015:'+outputDir+'/bmu2015_'+jobName+'.root,re2015:'+outputDir+'/re2015_'+jobName+'.root,rmu2015:'+outputDir+'/rmu2015_'+jobName+'.root,be2016:'+outputDir+'/be2016_'+jobName+'.root,bmu2016:'+outputDir+'/bmu2016_'+jobName+'.root,re2016:'+outputDir+'/re2016_'+jobName+'.root,rmu2016:'+outputDir+'/rmu2016_'+jobName+'.root'
			fr.write('./makeHistograms.py - '+isData+'   '+extra+'  --files '+infile+' --fullFiles '+infullfile+' --analysis '+analysisType+' --output '+out+'   --systs '+theSysts+'\n')
			fr.close()
			os.system('chmod a+x '+runfile)
			subcmd = 'qsub '+runfile
			os.system(subcmd)
			#sys.exit(0)
	
if __name__ == '__main__':
	import os
	fr = open("get_proxy.sh", "w")
	fr.write("export X509_USER_PROXY=$HOME/.globus/job_proxy.pem\n")
	fr.write("voms-proxy-init --voms atlas --vomslife 96:00 --valid 96:00\n")
	fr.close()
	os.system("chmod a+x get_proxy.sh")
	os.system("./get_proxy.sh")
	main()

