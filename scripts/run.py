
ntuplesDir = 'test2'
outputDir = 'test2_hist'

import glob
files = glob.glob(ntuplesDir+'/*.root')

import os
for item in files:
    outfile = outputDir+"/"+item.split('/')[-1].split('.')[0]
    os.system('./read --files '+item+' --analysis AnaTtresSL --output '+outfile+'_re.root,'+outfile+'_rmu.root,'+outfile+'_be.root,'+outfile+'_bmu.root')

