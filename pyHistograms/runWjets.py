#!/usr/bin/env python

import HQTTtResonancesTools.DC15MC13TeV_25ns_mc15c_EXOT4
import HQTTtResonancesTools.DC15Data13TeV_25ns_207_EXOT4

def main():
    # input directory
    ntuplesDir = '/nfs/dust/atlas/user/danilo/02062016v1'
    
    # output directory
    outputDir = 'hists_WjetsHF'
    
    # the default is AnaTtresSL, which produces many control pltos for tt res.
    # The Mtt version produces a TTree to do the limit setting
    # the QCD version aims at plots for QCD studies using the matrix method
    # look into read.cxx to see what is available
    # create yours, if you wish
    analysisType='AnaWjetsCR'
    
    # leave it for nominal to run only the nominal
    systematics = 'nominal'
    
    # 25 ns datasets
    names   = []
    names  += ['wbbjets']
    names  += ['wccjets']
    names  += ['wcjets']
    names  += ['wljets']

    names  += ["data"]
    names  += ['tt']
    names  += ['singletop']
    names  += ['zjets']
    names  += ['vv']

    mapToSamples = {
                    'wbbjets': 'MC15c_13TeV_25ns_FS_EXOT4_Wjets22',
                    'wccjets': 'MC15c_13TeV_25ns_FS_EXOT4_Wjets22',
                    'wcjets': 'MC15c_13TeV_25ns_FS_EXOT4_Wjets22',
                    'wljets': 'MC15c_13TeV_25ns_FS_EXOT4_Wjets22',
                    'data': 'Data15_13TeV_25ns_207_EXOT4',
		    'tt':'MC15c_13TeV_25ns_FS_EXOT4_ttbarPowhegPythia',
		    'singletop':'MC15c_13TeV_25ns_FS_EXOT4_singletop',
		    'zjets':'MC15c_13TeV_25ns_FS_EXOT4_Zjets22',
		    'vv': 'MC15c_13TeV_25ns_FS_EXOT4_VV',
		   }
    
    import TopExamples.grid
    
    
    import glob
    import os
    # get list of processed datasets
    dirs = glob.glob(ntuplesDir+'/*')
    
    # each "sample" below means an item in the list names above
    # there may contain multiple datasets
    # for each sample we want to read
    for sn in names:
        sname = mapToSamples[sn]
        samples = TopExamples.grid.Samples([sname])
        sample = samples[0]

        # write list of files to be read when processing this sample
        f = open(outputDir+"/input_"+s+'.txt', 'w')
        # output file after running read
        outfile = sn
        
        # go over all directories in the ntuplesDir
        for d in dirs:
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
              # and write it in ht elist of input files to process
              for item in files:
                  if not '.part' in item:
                      f.write(item+'\n')
              # go to the next directory in the same sample
              break
        f.close()
        theSysts = systematics
        isData = ''
	extra = ''
        if "data" in sn:
            theSysts = "nominal"
            isData = ' -d '
        if "wbb" in sn:
	    extra = ' --WjetsHF bb '
	elif 'wccj' in sn:
	    extra = ' --WjetsHF cc'
	elif 'wcj' in sn:
	    extra = ' --WjetsHF c'
	elif 'wl' in sn:
	    extra = ' --WjetsHF l'
        os.system('./makeHistograms.py - '+isData+'  '+extra+' --files '+outputDir+"/input_"+sample.name+'.txt --analysis '+analysisType+' --output Wpre_resjets_el:'+outputDir+'/Wpre_resjets_el_'+outfile+'.root,Wpre_resjets_mu:'+outputDir+'/Wpre_resjets_mu_'+outfile+'.root,Wtag_resjets_el:'+outputDir+'/Wtag_resjets_el_'+outfile+'.root,Wtag_resjets_mu:'+outputDir+'/Wtag_resjets_mu_'+outfile+'.root --systs '+theSysts)
    
if __name__ == '__main__':
    main()

