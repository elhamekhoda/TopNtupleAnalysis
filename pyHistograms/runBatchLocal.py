#!/usr/bin/env python

import HQTTtResonancesTools.DC15MC13TeV_25ns_mc15c_EXOT4
import HQTTtResonancesTools.DC15Data13TeV_25ns_207_EXOT4

def main():
	# for standard data and MC
	ntuplesDir = '/nfs/dust/atlas/user/danilo/ntuple_2429'

	# output directory
	# change this for your output directory
	outputDir = '/nfs/dust/atlas/user/danilo/hists2429_local'
	outputDir2 = '/nfs/dust/atlas/user/danilo/hists2429_local'

	# number of files per job
	#nFilesPerJob = 40
	nFilesPerJob = 8

	# use it to setup AnalysisTop
	# change this for the place where you setup RootCore
	rundir = '/nfs/dust/atlas/user/danilo/topana2429'

	# email to use to tell us when the job is done
	email = 'dferreir@cern.ch'

	# queue to submit to
	queue = 'long.q'
	#queue = 'short.q'

	# the default is AnaTtresSL, which produces many control pltos for tt res.
	# The Mtt version produces a TTree to do the limit setting
	# the QCD version aims at plots for QCD studies using the matrix method
	# look into read.cxx to see what is available
	# create yours, if you wish
	analysisType='AnaTtresSL'
	
	# leave it for nominal to run only the nominal
	#systematics = 'nominal'
	systematics = 'all,'
	#systematics = 'all1'
	#systematics = 'all2'
	#systematics = 'all3'
	#systematics = 'all4'
	
	# 25 ns datasets
	names   = []

	#names  += ["data"]
	#names  += ['qcde', 'qcdmu']

	#names  += ['tt']

	names  += ['tthm']
	names  += ['ttv']
	names  += ['singletop']
	names  += ['zjets']
	names  += ['vv']

	#names  += ['wbbjets']
	#names  += ['wccjets']
	#names  += ['wcjets']
	#names  += ['wljets']

	#names  += ['zprime400']
	#names  += ['zprime500']
	#names  += ['zprime750']
	#names  += ['zprime1000']
	#names  += ['zprime1250']
	#names  += ['zprime1500']
	#names  += ['zprime1750']
	#names  += ['zprime2000']
	#names  += ['zprime2250']
	#names  += ['zprime2500']
	#names  += ['zprime2750']
	#names  += ['zprime3000']
	#names  += ['zprime4000']
	#names  += ['zprime5000']
	#names  += ['kkgrav400']
	#names  += ['kkgrav500']
	#names  += ['kkgrav750']
	#names  += ['kkgrav1000']
	#names  += ['kkgrav2000']
	#names  += ['kkgrav3000']

	#names  += ['kkg500']
	#names  += ['kkg1000']
	#names  += ['kkg1500']
	#names  += ['kkg2000']
	#names  += ['kkg2500']
	#names  += ['kkg3000']
	#names  += ['kkg3500']
	#names  += ['kkg4000']
	#names  += ['kkg4500']
	#names  += ['kkg5000']

	#names  += ['ttsyst']
	#names  += ['ttpdf']
	#names  += ['ttpowhegherwig']
	######names  += ['ttmcatnloherwig']  # same as ttpdf nominal result, so why rerun it?
	#names  += ['ttradhi', 'ttradlo']

	#names  += ['ttsystaf2']
	#names  += ['ttpowhegherwigaf2']
	#names  += ['ttpowhegherwig7af2']

	#names  += ['eftl30c10']
	#names  += ['eftl35c10']
	#names  += ['eftl40c10']
	#names  += ['eftl45c10']
	#names  += ['eftl50c10']
	#names  += ['eftl55c10']
	#names  += ['eftl60c10']
	#names  += ['eftl100c10']
	
	#for k in ["10", "15", "20", "25", "30", "35", "40"]:
	#	names  += ['kkg500w%s'%k]
	#	names  += ['kkg1000w%s'%k]
	#	names  += ['kkg1500w%s'%k]
	#	names  += ['kkg2000w%s'%k]
	#	names  += ['kkg2500w%s'%k]
	#	names  += ['kkg3000w%s'%k]
	#	names  += ['kkg3500w%s'%k]
	#	names  += ['kkg4000w%s'%k]
	#	names  += ['kkg4500w%s'%k]
	#	names  += ['kkg5000w%s'%k]

	mapToSamples = {
					'wbbjets': 'MC15c_13TeV_25ns_FS_EXOT4_Wjets221',
					'wccjets': 'MC15c_13TeV_25ns_FS_EXOT4_Wjets221',
					'wcjets': 'MC15c_13TeV_25ns_FS_EXOT4_Wjets221',
					'wljets': 'MC15c_13TeV_25ns_FS_EXOT4_Wjets221',
					'data': 'Data15_13TeV_25ns_207_EXOT4,Data16_13TeV_25ns_207_EXOT4',
					'qcde': 'Data15_13TeV_25ns_207_EXOT4,Data16_13TeV_25ns_207_EXOT4',
					'qcdmu': 'Data15_13TeV_25ns_207_EXOT4,Data16_13TeV_25ns_207_EXOT4',
					'tt':'MC15c_13TeV_25ns_FS_EXOT4_ttbarPowhegPythia', #,MC15c_13TeV_25ns_FS_EXOT4_ttbarPowhegPythia_mttsliced',
					'tthm': 'MC15c_13TeV_25ns_FS_EXOT4_ttbarPowhegPythia_mttsliced',
					'ttv':'MC15c_13TeV_25ns_FS_EXOT4_ttbarV',
					'ttsyst':'MC15c_13TeV_25ns_FS_EXOT4_ttbarPowhegPythia',
					'ttpdf':'MC15c_13TeV_25ns_FS_EXOT4_ttbaraMcAtNlo_PDF',
					'ttpowhegherwig':'MC15c_13TeV_25ns_FS_EXOT4_ttbarPowhegHerwig',
					'ttmcatnloherwig':'MC15c_13TeV_25ns_FS_EXOT4_ttbarMCAtNLOHerwig',
                                        'ttpowhegherwig7af2':'MC15c_13TeV_25ns_AF2_EXOT4_ttbarPowhegHerwig7',
					'ttpowhegherwigaf2':'MC15c_13TeV_25ns_AF2_EXOT4_ttbarPowhegHerwig',
					'ttsystaf2':'MC15c_13TeV_25ns_AF2_EXOT4_ttbarPowhegPythia',
					'ttradhi':'MC15c_13TeV_25ns_FS_EXOT4_ttbarRadHi',
					'ttradlo':'MC15c_13TeV_25ns_FS_EXOT4_ttbarRadLo',
					'singletop':'MC15c_13TeV_25ns_FS_EXOT4_singletop',
					'zjets':'MC15c_13TeV_25ns_FS_EXOT4_Zjets221',
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
					'kkg500': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon500',
					'kkg1000': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon1000',
					'kkg1500': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon1500',
					'kkg2000': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon2000',
					'kkg2500': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon2500',
					'kkg3000': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon3000',
					'kkg3500': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon3500',
					'kkg4000': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon4000',
					'kkg4500': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon4500',
					'kkg5000': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon5000',

					'kkg500w10': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon500',
					'kkg1000w10': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon1000',
					'kkg1500w10': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon1500',
					'kkg2000w10': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon2000',
					'kkg2500w10': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon2500',
					'kkg3000w10': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon3000',
					'kkg3500w10': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon3500',
					'kkg4000w10': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon4000',
					'kkg4500w10': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon4500',
					'kkg5000w10': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon5000',

					'kkg500w15': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon500',
					'kkg1000w15': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon1000',
					'kkg1500w15': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon1500',
					'kkg2000w15': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon2000',
					'kkg2500w15': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon2500',
					'kkg3000w15': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon3000',
					'kkg3500w15': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon3500',
					'kkg4000w15': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon4000',
					'kkg4500w15': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon4500',
					'kkg5000w15': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon5000',

					'kkg500w20': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon500',
					'kkg1000w20': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon1000',
					'kkg1500w20': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon1500',
					'kkg2000w20': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon2000',
					'kkg2500w20': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon2500',
					'kkg3000w20': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon3000',
					'kkg3500w20': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon3500',
					'kkg4000w20': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon4000',
					'kkg4500w20': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon4500',
					'kkg5000w20': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon5000',

					'kkg500w25': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon500',
					'kkg1000w25': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon1000',
					'kkg1500w25': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon1500',
					'kkg2000w25': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon2000',
					'kkg2500w25': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon2500',
					'kkg3000w25': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon3000',
					'kkg3500w25': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon3500',
					'kkg4000w25': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon4000',
					'kkg4500w25': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon4500',
					'kkg5000w25': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon5000',

					'kkg500w30': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon500',
					'kkg1000w30': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon1000',
					'kkg1500w30': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon1500',
					'kkg2000w30': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon2000',
					'kkg2500w30': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon2500',
					'kkg3000w30': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon3000',
					'kkg3500w30': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon3500',
					'kkg4000w30': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon4000',
					'kkg4500w30': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon4500',
					'kkg5000w30': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon5000',

					'kkg500w35': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon500',
					'kkg1000w35': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon1000',
					'kkg1500w35': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon1500',
					'kkg2000w35': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon2000',
					'kkg2500w35': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon2500',
					'kkg3000w35': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon3000',
					'kkg3500w35': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon3500',
					'kkg4000w35': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon4000',
					'kkg4500w35': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon4500',
					'kkg5000w35': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon5000',

					'kkg500w40': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon500',
					'kkg1000w40': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon1000',
					'kkg1500w40': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon1500',
					'kkg2000w40': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon2000',
					'kkg2500w40': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon2500',
					'kkg3000w40': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon3000',
					'kkg3500w40': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon3500',
					'kkg4000w40': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon4000',
					'kkg4500w40': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon4500',
					'kkg5000w40': 'MC15c_13TeV_25ns_FS_EXOT4_KKgluon5000',

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
	import os
	import sys
	# get list of processed datasets

	dirs = glob.glob(ntuplesDir+'/user.dferreir.*15032017v*')
	dirs.extend(glob.glob(ntuplesDir+'/user.dferreir.*07042017v*'))

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
		if 'af2' in sn:
			nFilesPerJobEffective = 8
		elif 'tthm' in sn:
			nFilesPerJobEffective = 1
		elif 'tt' in sn:
			nFilesPerJobEffective = 1
		elif 'eft' in sn:
			nFilesPerJobEffective = 1
		elif 'singletop' in sn:
			nFilesPerJobEffective = 5
		elif 'kkgrav' in sn:
			nFilesPerJobEffective = 1
		elif 'zprime' in sn:
			nFilesPerJobEffective = 1
		elif 'kkg' in sn:
			nFilesPerJobEffective = 1
		elif 'data' in sn or 'qcd' in sn:
			nFilesPerJobEffective = 400

		# write list of files to be read when processing this sample
		f = open(outputDir+"/input_"+sn+'.txt', 'w')
		# output file after running read
		outfile = sn
		
		# go over all directories in the ntuplesDir
		ds = dirs
		if sn == 'qcde':
			ds = glob.glob(ntuplesDir+'/*QCDe*')
		elif sn == 'qcdmu':
			ds = glob.glob(ntuplesDir+'/*QCDmu*')
		elif sn == 'ttpdf':
			ds = glob.glob(ntuplesDir+'/*PDFv*')
		elif sn in ['ttpowhegherwig', 'ttmcatnloherwig', 'ttradhi', 'ttradlo']:
			ds = glob.glob(ntuplesDir+'/*Systv*')
		elif sn in ['ttsystaf2']:
			ds = glob.glob(ntuplesDir+'/*SystNewv3*')
		elif sn in ['ttpowhegherwig7af2']:
			ds = glob.glob(ntuplesDir+'/*SystNewv1*')
		elif sn in ['ttpowhegherwigaf2']:
			ds = glob.glob(ntuplesDir+'/*SystNewv3*')
		elif sn == 'data':
			ds = glob.glob(ntuplesDir+'/user.dferreir.00*15032017v*')

		for d in ds:
			# remove path and get only dir name in justfile
			justfile = d.split('/')[-1]
			dsid_dir = justfile.split('.')[2] # get the DSID of the directory
			# this will include all directories, so check if this director is in the sample
	
			# now go over the list of datasets in sample
			# and check if this DSID is there
			for s in sample.datasets:
				if len(s.split(':')) > 1:
					s = s.split(':')[1] # skip mc15_13TeV
				dsid_sample = s.split('.')[1] # get DSID
				if dsid_dir == dsid_sample: # this dataset belongs in the sample in the big for loop
					# get all files in the directory
					files = glob.glob(d+'/*.root*')

					# and write it in the list of input files to process
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
                elif "ttsystaf2" in sn or "ttpowhegherwig7af2" in sn:
			isData = ' --noMttSlices --af2 '
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
		if 'kkg' in sn and "0w" in sn:
			width = sn.split("w")
			extraKKgluon = {
					'10': ' --KKgluon 10',
					'15': ' --KKgluon 15',
					'20': ' --KKgluon 20',
					'25': ' --KKgluon 25',
					'30': ' --KKgluon 30',
					'35': ' --KKgluon 35',
					'40': ' --KKgluon 40',
					}
			extra = extraKKgluon[width]
	
		#extra += '  --applyMET 80 '

		for job in forJobs:
			jobName = sn+'_'+job
			infile = outputDir+"/input_"+jobName+'.txt'
			infullfile = outputDir+"/input_"+sn+'.txt'
			f = open(infile, 'w')
			for item in forJobs[job]:
				f.write(item)
			f.close()
			logfile = outputDir+"/stdout_"+jobName+'.txt'
			os.system('rm -f %s' % logfile)
			runfile = outputDir+"/run_"+jobName+'.sh'
			fr = open(runfile, 'w')
			fr.write('#!/bin/sh\n')
			fr.write('#$ -cwd\n')
			fr.write('#$ -j y\n')
			fr.write('#$ -l cvmfs\n')
			fr.write('#$ -l distro=sld6\n')
			fr.write('#$ -l arch=amd64\n')
			fr.write('#$ -l h_vmem=5G\n')
			fr.write('#$ -o '+logfile+'\n')
			fr.write('#$ -q '+queue+'\n')
			fr.write('#$ -m '+'as'+'\n')
			fr.write('#$ -M '+email+'\n')
			fr.write('#$ -N '+jobName+'\n')
			# bsub options
			#fr.write('#BSUB -C 0\n')
			#fr.write('#BSUB -e '+logfile+'\n')
			#fr.write('#BSUB -o '+logfile+'\n')
			#fr.write('#BSUB -q '+queue+'\n')
			##fr.write('#BSUB -M 5000000\n')
			##fr.write('#$ -N '+'tpy_'+jobName+'\n')
			#fr.write('#BSUB -u '+email+'\n')
			#fr.write('#BSUB -J tnapy_'+jobName+'\n')
			fr.write('export TMPDIR=%s\n' % outputDir2)
			fr.write("echo Temporary dir is $TMPDIR\n")
			fr.write('export EOS_MGM_URL=root://eosuser.cern.ch\n')
			fr.write('cd '+rundir+'\n')
			fr.write('export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase\n')
			fr.write('export DQ2_LOCAL_SITE_ID=DESY-HH_SCRATCHDISK \n')
			fr.write('source /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/user/atlasLocalSetup.sh\n')
			fr.write('export X509_USER_PROXY=$HOME/.globus/job_proxy.pem\n')
			#fr.write('export XrdSecDEBUG=2\n')
			fr.write('export DISPLAY=\n')
			fr.write('lsetup rcsetup\n')
			fr.write('cd TopNtupleAnalysis/pyHistograms\n')
			tmpDir = '$TMPDIR'
			out = 'be,'+tmpDir+'/be_'+jobName+'.root\;bmu,'+tmpDir+'/bmu_'+jobName+'.root\;re,'+tmpDir+'/re_'+jobName+'.root\;rmu,'+tmpDir+'/rmu_'+jobName+'.root'
			out += '\;be3,'+tmpDir+'/be3_'+jobName+'.root\;bmu3,'+tmpDir+'/bmu3_'+jobName+'.root\;re3,'+tmpDir+'/re3_'+jobName+'.root\;rmu3,'+tmpDir+'/rmu3_'+jobName+'.root'
			out += '\;be2,'+tmpDir+'/be2_'+jobName+'.root\;bmu2,'+tmpDir+'/bmu2_'+jobName+'.root\;re2,'+tmpDir+'/re2_'+jobName+'.root\;rmu2,'+tmpDir+'/rmu2_'+jobName+'.root'
			out += '\;be1,'+tmpDir+'/be1_'+jobName+'.root\;bmu1,'+tmpDir+'/bmu1_'+jobName+'.root\;re1,'+tmpDir+'/re1_'+jobName+'.root\;rmu1,'+tmpDir+'/rmu1_'+jobName+'.root'
			out += '\;be0,'+tmpDir+'/be0_'+jobName+'.root\;bmu0,'+tmpDir+'/bmu0_'+jobName+'.root\;re0,'+tmpDir+'/re0_'+jobName+'.root\;rmu0,'+tmpDir+'/rmu0_'+jobName+'.root'
			fr.write('./makeHistograms.py - '+isData+'   '+extra+'  --files '+infile+' --analysis '+analysisType+' --output '+out+'   --systs '+theSysts+'\n')
			fr.write('echo Status code $?\n')
			#fr.write('cp %s/*_%s.root %s/' % (tmpDir, jobName, outputDir2))
			fr.close()
			os.system('chmod a+x '+runfile)
			#subcmd = 'bsub <'+runfile + "|tee "+logfile
			subcmd = 'qsub '+runfile + "|tee "+logfile
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

