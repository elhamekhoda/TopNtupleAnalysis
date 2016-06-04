#!/usr/bin/env python

import HQTTtResonancesTools.DC15MC13TeV_25ns_mc15c_EXOT4
import HQTTtResonancesTools.DC15Data13TeV_25ns_207_EXOT4

def main():
    # input directory
    ntuplesDir = '/nfs/dust/atlas/user/danilo/02062016WjetsCRv1'
    
    # output directory
    outputDir = 'hists'
    outputDir = 'tmp'#hists_Wweight'
    
    # the default is AnaTtresSL, which produces many control pltos for tt res.
    # The Mtt version produces a TTree to do the limit setting
    # the QCD version aims at plots for QCD studies using the matrix method
    # look into read.cxx to see what is available
    # create yours, if you wish
    analysisType='AnaTtresSL'
    analysisType='AnaWjetsCR'
    
    # leave it for nominal to run only the nominal
    systematics = 'nominal'
    #systematics = 'all'
    
    names   = []
    #names  += ["Data15_13TeV_25ns_207_EXOT4"]
    # 25 ns datasets

    names  += ['MC15c_13TeV_25ns_FS_EXOT4_ttbarPowhegPythia']
    ##names  += ['MC15c_13TeV_25ns_FS_EXOT4_ttbarPowhegPythia_mttsliced']
    #names  += ['MC15c_13TeV_25ns_FS_EXOT4_singletop']
    #names  += ['MC15c_13TeV_25ns_FS_EXOT4_Wjets22']
    #names  += ['MC15c_13TeV_25ns_FS_EXOT4_Zjets22']
    #names  += ['MC15c_13TeV_25ns_FS_EXOT4_VV']

    #names += ['MC15c_13TeV_25ns_FS_EXOT4_Zprime400']
    #names += ['MC15c_13TeV_25ns_FS_EXOT4_Zprime500']
    #names += ['MC15c_13TeV_25ns_FS_EXOT4_Zprime750']
    #names += ['MC15c_13TeV_25ns_FS_EXOT4_Zprime1000']
    #names += ['MC15c_13TeV_25ns_FS_EXOT4_Zprime1250']
    #names += ['MC15c_13TeV_25ns_FS_EXOT4_Zprime1500']
    #names += ['MC15c_13TeV_25ns_FS_EXOT4_Zprime1750']
    #names += ['MC15c_13TeV_25ns_FS_EXOT4_Zprime2000']
    #names += ['MC15c_13TeV_25ns_FS_EXOT4_Zprime2250']
    #names += ['MC15c_13TeV_25ns_FS_EXOT4_Zprime2500']
    #names += ['MC15c_13TeV_25ns_FS_EXOT4_Zprime2750']
    #names += ['MC15c_13TeV_25ns_FS_EXOT4_Zprime3000']
    #names += ['MC15c_13TeV_25ns_FS_EXOT4_Zprime4000']
    #names += ['MC15c_13TeV_25ns_FS_EXOT4_Zprime5000']
    #names += ['MC15_13TeV_25ns_FS_EXOT4_ttbarPowhegHerwigAF2', 'MC15_13TeV_25ns_FS_EXOT4_ttbarMCAtNLOHerwigAF2', 'MC15_13TeV_25ns_FS_EXOT4_ttbarPowhegPythiaAF2', 'MC15_13TeV_25ns_FS_EXOT4_ttbarRadLo', 'MC15_13TeV_25ns_FS_EXOT4_ttbarRadHi']
    
    import TopExamples.grid
    
    import glob
    files = glob.glob(ntuplesDir+'/*.root')
    samples = TopExamples.grid.Samples(names)
    
    import glob
    import os
    # get list of processed datasets
    dirs = glob.glob(ntuplesDir+'/*')
    
    # each "sample" below means an item in the list names above
    # there may contain multiple datasets
    # for each sample we want to read
    for sample in samples:
        # write list of files to be read when processing this sample
        f = open(outputDir+"/input_"+sample.name+'.txt', 'w')
        # output file after running read
        #outfile = outputDir+"/"+sample.name
        outfile = sample.name
        
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
        if "Data" in sample.name:
            theSysts = "nominal"
            isData = ' -d '
        jobName = outfile
        out = 'Wpre_resjets_el:'+outputDir+'/Wpre_resjets_el_'+jobName+'.root,Wpre_resjets_mu:'+outputDir+'/Wpre_resjets_mu_'+jobName+'.root,Wtag_resjets_el:'+outputDir+'/Wtag_resjets_el_'+jobName+'.root,Wtag_resjets_mu:'+outputDir+'/Wtag_resjets_mu_'+jobName+'.root'
        #out = ' re:'+outputDir+'/resolved_e_'+outfile+'.root,rmu:'+outputDir+'/resolved_mu_'+outfile+'.root,be:'+outputDir+'/boosted_e_'+outfile+'.root,bmu:'+outputDir+'/boosted_mu_'+outfile+'.root'
        os.system('./makeHistograms.py - '+isData+' --files '+outputDir+"/input_"+sample.name+'.txt --analysis '+analysisType+' --output '+out+' --systs '+theSysts)
    
if __name__ == '__main__':
    main()

