#!/usr/bin/env python

# Only to be used by sumWeights.py to get sum of weights for normalisation

import HQTTtResonancesTools.DC15MC13TeV_25ns_mc15c_EXOT4
import HQTTtResonancesTools.DC15Data13TeV_25ns_207_EXOT4

def main():
	ntuples_dir = '/nfs/dust/atlas/user/danilo/ntuple_2429'
	
	# output directory
	outputDir = '.'

	# 25 ns datasets
	names   = []

	names  += ['tt']
	names  += ['tthm']
	names  += ['ttv']
	names  += ['wbbjets']
	names  += ['zjets']
	##names  += ["data"]
	##names  += ['qcde', 'qcdmu']
	names  += ['singletop']
	names  += ['vv']
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
	names  += ['ttpdf']
	names  += ['ttpowhegherwig']
	names  += ['ttmcatnloherwig']
	names  += ['ttradhi', 'ttradlo']
	#names  += ['eftl30c1']

	names  += ['kkg500']
	names  += ['kkg1000']
	names  += ['kkg1500']
	names  += ['kkg2000']
	names  += ['kkg2500']
	names  += ['kkg3000']
	names  += ['kkg3500']
	names  += ['kkg4000']
	names  += ['kkg4500']
	names  += ['kkg5000']

	names  += ['ttsystaf2']
	names  += ['ttpowhegherwigaf2']
	names  += ['ttpowhegherwig7af2']


	mapToSamples = {
					'wbbjets': 'MC15c_13TeV_25ns_FS_EXOT4_Wjets221',
					'wccjets': 'MC15c_13TeV_25ns_FS_EXOT4_Wjets221',
					'wcjets': 'MC15c_13TeV_25ns_FS_EXOT4_Wjets221',
					'wljets': 'MC15c_13TeV_25ns_FS_EXOT4_Wjets221',
					'data': 'Data15_13TeV_25ns_207_EXOT4,Data16_13TeV_25ns_207_EXOT4',
					'qcde': 'Data15_13TeV_25ns_207_EXOT4,Data16_13TeV_25ns_207_EXOT4',
					'qcdmu': 'Data15_13TeV_25ns_207_EXOT4,Data16_13TeV_25ns_207_EXOT4',
					'tt':'MC15c_13TeV_25ns_FS_EXOT4_ttbarPowhegPythia', #,MC15c_13TeV_25ns_FS_EXOT4_ttbarPowhegPythia_mttsliced',
					'tthm':'MC15c_13TeV_25ns_FS_EXOT4_ttbarPowhegPythia_mttsliced',
					'ttv':'MC15c_13TeV_25ns_FS_EXOT4_ttbarV',
					'ttsystaf2':'MC15c_13TeV_25ns_AF2_EXOT4_ttbarPowhegPythia',
					'ttpowhegherwig7af2':'MC15c_13TeV_25ns_AF2_EXOT4_ttbarPowhegHerwig7',
					'ttpowhegherwigaf2':'MC15c_13TeV_25ns_AF2_EXOT4_ttbarPowhegHerwig',
					'ttpdf':'MC15c_13TeV_25ns_FS_EXOT4_ttbaraMcAtNlo_PDF',
					'ttpowhegherwig':'MC15c_13TeV_25ns_FS_EXOT4_ttbarPowhegHerwig',
					'ttmcatnloherwig':'MC15c_13TeV_25ns_FS_EXOT4_ttbarMCAtNLOHerwig',
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
					'eftl30c1': 'MC15c_13TeV_25ns_FS_EXOT4_ttbarLO',
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
		# go over all directories in the ntuplesDir
		ds = dirs
		suf = 'all'
		if sn == 'qcde':
			ds = glob.glob(ntuplesDir+'/*QCDe*')
			suf = 'qcde'
		elif sn == 'qcdmu':
			ds = glob.glob(ntuplesDir+'/*QCDmu*')
			suf = 'qcdmu'
		#elif sn == 'tthm' or sn == 'singletop':
		#	ds = datasets_mtt
		elif sn == 'ttpdf':
			ds = glob.glob(ntuplesDir+'/*PDFv*')
			suf = 'pdf'
		elif sn in ['ttpowhegherwig', 'ttmcatnloherwig', 'ttradhi', 'ttradlo']:
			ds = glob.glob(ntuplesDir+'/*Systv*')
			suf = 'syst'
		elif sn in ['ttsystaf2']:
			ds = glob.glob(ntuplesDir+'/*SystNewv3*')
			suf = 'systaf2'
		elif sn in ['ttpowhegherwig7af2']:
			ds = glob.glob(ntuplesDir+'/*SystNewv1*')
			suf = 'systaf2'
		elif sn in ['ttpowhegherwigaf2']:
			ds = glob.glob(ntuplesDir+'/*SystNewv3*')
			suf = 'systaf2'
		elif sn == 'data':
			ds = glob.glob(ntuplesDir+'/user.dferreir.00*15032017v*')
			suf = 'data'
		# write list of files to be read when processing this sample
		f = open(outputDir+"/inputSW_%s.txt" % suf, 'a')
		
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
					files = glob.glob(d+'/*.root*')
					# and write it in the list of input files to process
					for item in files:
						if not '.part' in item:
							f.write(item+'\n')
					
					if useFileOnGrid:
						# go to the next directory in the same sample
						break
		f.close()
	
if __name__ == '__main__':
	main()

