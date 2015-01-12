
import ami

inputDirectory = '/afs/phas.gla.ac.uk/user/d/dferreira/atlas_data/dferreira02/topxaod_ttres13e4_01'

yieldmap = {}

import glob
import os
samples = glob.glob(inputDirectory+'/*')
for dir in samples:
    sample = dir.split('/')[-1]
    if len(sample.split('.')) < 4:
        continue
    dsid = sample.split('.')[2] # user.BLABLABLA.123456.MOREBLABLABLA
    inds = 'mc14_13TeV.'+dsid+'.*merge.AOD*r5787_r5853'
    yields = ami.askAmi(inds)
    key, value = yields.popitem()
    yieldmap[int(dsid)] = value

from ROOT import TFile, TTree
f = TFile('EventCount.root', "recreate")
t = TTree("count", "")
import array
dsid = array.array( 'i', [ 0 ] )
value = array.array( 'f', [ 0. ] )
t.Branch("type", dsid, "type/I")
t.Branch("value", value, "value/F")

for i in yieldmap:
  dsid[0] = i
  value[0] = yieldmap[i]
  t.Fill()

f.Write()
f.Close()

