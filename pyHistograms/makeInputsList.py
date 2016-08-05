#!/usr/bin/env python

import HQTTtResonancesTools.DC15MC13TeV_25ns_mc15c_EXOT4
import HQTTtResonancesTools.DC15Data13TeV_25ns_207_EXOT4

def main():
	# input directory
	#ntuplesDir = '/nfs/dust/atlas/user/danilo/20062016v1'
	# for standard data and MC
	pattern = 'user.dferreir.*03082016v1_output.root'
	pattern_mtt = 'user.dferreir.*03082016v3_output.root'
	# for QCD e
	pattern_qcde = 'user.dferreir.*03082016QCDev1_output.root'
	pattern_qcdmu = 'user.dferreir.*03082016QCDmuv1_output.root'
	theScope = 'user.dferreir'
	
	# output directory
	#outputDir = '/afs/desy.de/user/d/danilo/xxl/af-atlas/Top2412/TopNtupleAnalysis/pyHistograms/hists_sr_nosyst'
	outputDir = '/afs/desy.de/user/d/danilo/xxl/af-atlas/Top2412/TopNtupleAnalysis/pyHistograms/hists_sr'
	outputDir = '/nfs/dust/atlas/user/danilo/hists_sr2416'
	#outputDir = '.'

	# 25 ns datasets
	names   = []

	names  += ['tt']
	names  += ['tthm']
	names  += ['wbbjets']
	names  += ['wccjets']
	names  += ['wcjets']
	names  += ['wljets']
	names  += ['zjets']
	names  += ["data"]
	names  += ['qcde', 'qcdmu']
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

	mapToSamples = {
					'wbbjets': 'MC15c_13TeV_25ns_FS_EXOT4_Wjets22',
					'wccjets': 'MC15c_13TeV_25ns_FS_EXOT4_Wjets22',
					'wcjets': 'MC15c_13TeV_25ns_FS_EXOT4_Wjets22',
					'wljets': 'MC15c_13TeV_25ns_FS_EXOT4_Wjets22',
					'data': 'Data15_13TeV_25ns_207_EXOT4,Data16_13TeV_25ns_207_EXOT4',
					'qcde': 'Data15_13TeV_25ns_207_EXOT4,Data16_13TeV_25ns_207_EXOT4',
					'qcdmu': 'Data15_13TeV_25ns_207_EXOT4,Data16_13TeV_25ns_207_EXOT4',
					'tt':'MC15c_13TeV_25ns_FS_EXOT4_ttbarPowhegPythia', #,MC15c_13TeV_25ns_FS_EXOT4_ttbarPowhegPythia_mttsliced',
					'tthm':'MC15c_13TeV_25ns_FS_EXOT4_ttbarPowhegPythia_mttsliced',
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
	response = rucio.list_dids(scope = theScope, filters = {'name' : pattern_qcde})
	datasets_qcde = []
	for l in response:
		datasets_qcde.append(l)
	response = rucio.list_dids(scope = theScope, filters = {'name' : pattern_qcdmu})
	datasets_qcdmu = []
	for l in response:
		datasets_qcdmu.append(l)
	response = rucio.list_dids(scope = theScope, filters = {'name' : pattern_mtt})
	datasets_mtt = []
	for l in response:
		datasets_mtt.append(l)
	
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

		# write list of files to be read when processing this sample
		f = open(outputDir+"/input_all.txt", 'a')
		
		# go over all directories in the ntuplesDir
		ds = datasets
		if sn == 'qcde':
			ds = datasets_qcde
		elif sn == 'qcdmu':
			ds = datasets_qcdmu
		elif sn == 'tthm' or sn == 'singletop':
			ds = datasets_mtt
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
					# go to the next directory in the same sample
					break
		f.close()
	
if __name__ == '__main__':
	main()

