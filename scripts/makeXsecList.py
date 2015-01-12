import os
import sys
from xml.dom.minidom import parse, parseString


import pyAMI.client

def askAmi(query):
  amiclient = pyAMI.client.Client('atlas')

  #swap * for % - databases
  query = query.replace('*', '%%')

  data = "'"+query+"'"

  argument = 'SearchQuery -glite="SELECT dataset.logicalDatasetName, dataset.totalEvents, dataset.crossSection WHERE dataset.logicalDatasetName LIKE %s"' % data

  if data.find('data') > -1:
        if data.find('data12') > -1:
            argument += ' -processingStep=real_data'
            argument += ' -project=data12_001'
        elif data.find('data11') > -1:
            argument += ' -processingStep=real_data'
            argument += ' -project=data11_001'
        else:
            argument += ' -processingStep=real_data'
            argument += ' -project=data10_001'
  else:
        argument += ' -processingStep=production'
        if data.find('mc09') > -1:
          argument += ' -project=mc09'
        if data.find('mc10') > -1:
          argument += ' -project=mc10'
        if data.find('mc11') > -1:
          argument += ' -project=mc11_001'
        if data.find('mc12') > -1:
          argument += ' -project=mc12_001'
        if data.find('mc14') > -1:
          argument += ' -project=mc14_001'

  maxTries = 3

  #print argument
  failures = 0
  for i in range(maxTries):
      try:
          results = amiclient.execute(argument, format='xml')
      except:
          failures += 1

  if failures == maxTries:
      print ''
      print 'is your voms proxy okay?'
      print 'Try voms-proxy-init -voms atlas'
      sys.exit(1)

  # print result
  dom = parseString(results)
  rows = dom.getElementsByTagName('row')

  final = {}
  for row in rows:
      fields = row.getElementsByTagName('field')
      retName = ''
      retNEv = 0
      retXSe = 0
      for field in fields:
        if field.attributes['name'].value == 'logicalDatasetName':
          retName=field.firstChild.nodeValue

        if field.attributes['name'].value == 'totalEvents':
          retNEv = field.firstChild.nodeValue

        if field.attributes['name'].value == 'crossSection':
          retXSe = field.firstChild.nodeValue

      final[retName] = [retNEv, retXSe]

  #unicode -> normalcode
  results = {}
  for k in final.keys():
    results[str(k)] = [int(final[k][0]), float(final[k][1])]

  return results

simple = {
'mc14_13TeV.110401.PowhegPythia_P2012_ttbar_nonallhad.merge.AOD.e2928_s1982_s2008_r5787_r5853/' : 'ttbar SL+DL (110401)',
'mc14_13TeV.110070.PowhegPythia_P2012_singletop_tchan_lept_top.merge.AOD.e3049_s1982_s2008_r5787_r5853/' : 'single top t-channel, top (110070)',
'mc14_13TeV.110071.PowhegPythia_P2012_singletop_tchan_lept_antitop.merge.AOD.e3049_s1982_s2008_r5787_r5853/' : 'single top t-channel antitop (110071)',
'mc14_13TeV.110302.PowhegPythia_P2012_st_schan_lep.merge.AOD.e3049_s1982_s2008_r5787_r5853/' : 'single top s-channel (110302)',
'mc14_13TeV.110305.PowhegPythia_P2012_st_Wtchan_incl_DR.merge.AOD.e3049_s1982_s2008_r5787_r5853/' : 'single top Wt-channel (110305)',
'mc14_13TeV.167740.Sherpa_CT10_WenuMassiveCBPt0_BFilter.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets e nu pt < 70, bfilter (167740)',
'mc14_13TeV.167741.Sherpa_CT10_WenuMassiveCBPt0_CJetFilterBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets e nu pt < 70, cfilter (167741)',
'mc14_13TeV.167742.Sherpa_CT10_WenuMassiveCBPt0_CJetVetoBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets e nu pt < 70, lfilter (167742)',
'mc14_13TeV.167743.Sherpa_CT10_WmunuMassiveCBPt0_BFilter.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets mu nu pt < 70, bfilter (167743)',
'mc14_13TeV.167744.Sherpa_CT10_WmunuMassiveCBPt0_CJetFilterBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets mu nu pt < 70, cfilter (167744)',
'mc14_13TeV.167745.Sherpa_CT10_WmunuMassiveCBPt0_CJetVetoBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/': 'W+jets mu nu pt < 70, lfilter (167745)',
'mc14_13TeV.167746.Sherpa_CT10_WtaunuMassiveCBPt0_BFilter.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets tau nu pt < 70, bfilter (167746)',
'mc14_13TeV.167747.Sherpa_CT10_WtaunuMassiveCBPt0_CJetFilterBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets tau nu pt < 70, cfilter (167747)',
'mc14_13TeV.167748.Sherpa_CT10_WtaunuMassiveCBPt0_CJetVetoBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets tau nu pt < 70, lfilter (167748)',
'mc14_13TeV.167761.Sherpa_CT10_WenuMassiveCBPt70_140_BFilter.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets e nu 70 < pt < 140, bfilter (167761)',
'mc14_13TeV.167762.Sherpa_CT10_WenuMassiveCBPt70_140_CJetFilterBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets e nu 70 < pt < 140, cfilter (167762)',
'mc14_13TeV.167763.Sherpa_CT10_WenuMassiveCBPt70_140_CJetVetoBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets e nu 70 < pt < 140, lfilter (167763)',
'mc14_13TeV.167764.Sherpa_CT10_WmunuMassiveCBPt70_140_BFilter.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets mu nu 70 < pt < 140, bfilter (167764)',
'mc14_13TeV.167765.Sherpa_CT10_WmunuMassiveCBPt70_140_CJetFilterBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets mu nu 70 < pt < 140, cfilter (167765)',
'mc14_13TeV.167766.Sherpa_CT10_WmunuMassiveCBPt70_140_CJetVetoBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets mu nu 70 < pt < 140, lfilter (167766)',
'mc14_13TeV.167767.Sherpa_CT10_WtaunuMassiveCBPt70_140_BFilter.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets tau nu 70 < pt < 140, bfilter (167767)',
'mc14_13TeV.167768.Sherpa_CT10_WtaunuMassiveCBPt70_140_CJetFilterBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets tau nu 70 < pt < 140, cfilter (167768)',
'mc14_13TeV.167769.Sherpa_CT10_WtaunuMassiveCBPt70_140_CJetVetoBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets tau nu 70 < pt < 140, lfilter (167769)',
'mc14_13TeV.167770.Sherpa_CT10_WenuMassiveCBPt140_280_BFilter.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets e nu 140 < pt < 280, bfilter (167770)',
'mc14_13TeV.167771.Sherpa_CT10_WenuMassiveCBPt140_280_CJetFilterBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets e nu 140 < pt < 280, cfilter (167771)',
'mc14_13TeV.167772.Sherpa_CT10_WenuMassiveCBPt140_280_CJetVetoBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets e nu 140 < pt < 280, lfilter (167772)',
'mc14_13TeV.167773.Sherpa_CT10_WmunuMassiveCBPt140_280_BFilter.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets mu nu 140 < pt < 280, bfilter (167773)',
'mc14_13TeV.167774.Sherpa_CT10_WmunuMassiveCBPt140_280_CJetFilterBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets mu nu 140 < pt < 280, cfilter (167774)',
'mc14_13TeV.167775.Sherpa_CT10_WmunuMassiveCBPt140_280_CJetVetoBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets mu nu 140 < pt < 280, lfilter (167775)',
'mc14_13TeV.167776.Sherpa_CT10_WtaunuMassiveCBPt140_280_BFilter.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets tau nu 140 < pt < 280, bfilter (167776)',
'mc14_13TeV.167777.Sherpa_CT10_WtaunuMassiveCBPt140_280_CJetFilterBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets tau nu 140 < pt < 280, cfilter (167777)',
'mc14_13TeV.167778.Sherpa_CT10_WtaunuMassiveCBPt140_280_CJetVetoBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets tau nu 140 < pt < 280, lfilter (167778)',
'mc14_13TeV.167779.Sherpa_CT10_WenuMassiveCBPt280_500_BFilter.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets e nu 280 < pt < 500, bfilter (167779)',
'mc14_13TeV.167780.Sherpa_CT10_WenuMassiveCBPt280_500_CJetFilterBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets e nu 280 < pt < 500, cfilter (167780)',
'mc14_13TeV.167781.Sherpa_CT10_WenuMassiveCBPt280_500_CJetVetoBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets e nu 280 < pt < 500, lfilter (167781)',
'mc14_13TeV.167782.Sherpa_CT10_WmunuMassiveCBPt280_500_BFilter.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : 'W+jets mu nu 280 < pt < 500, bfilter (167782)',
'mc14_13TeV.167783.Sherpa_CT10_WmunuMassiveCBPt280_500_CJetFilterBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/': '',
'mc14_13TeV.167784.Sherpa_CT10_WmunuMassiveCBPt280_500_CJetVetoBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167785.Sherpa_CT10_WtaunuMassiveCBPt280_500_BFilter.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167786.Sherpa_CT10_WtaunuMassiveCBPt280_500_CJetFilterBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167787.Sherpa_CT10_WtaunuMassiveCBPt280_500_CJetVetoBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167788.Sherpa_CT10_WenuMassiveCBPt500_BFilter.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167789.Sherpa_CT10_WenuMassiveCBPt500_CJetFilterBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167790.Sherpa_CT10_WenuMassiveCBPt500_CJetVetoBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167791.Sherpa_CT10_WmunuMassiveCBPt500_BFilter.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167792.Sherpa_CT10_WmunuMassiveCBPt500_CJetFilterBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167793.Sherpa_CT10_WmunuMassiveCBPt500_CJetVetoBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167794.Sherpa_CT10_WtaunuMassiveCBPt500_BFilter.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167795.Sherpa_CT10_WtaunuMassiveCBPt500_CJetFilterBVeto.merge.AOD.e2822_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167749.Sherpa_CT10_ZeeMassiveCBPt0_BFilter.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167750.Sherpa_CT10_ZeeMassiveCBPt0_CFilterBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167751.Sherpa_CT10_ZeeMassiveCBPt0_CVetoBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167752.Sherpa_CT10_ZmumuMassiveCBPt0_BFilter.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167753.Sherpa_CT10_ZmumuMassiveCBPt0_CFilterBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167754.Sherpa_CT10_ZmumuMassiveCBPt0_CVetoBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167755.Sherpa_CT10_ZtautauMassiveCBPt0_BFilter.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167756.Sherpa_CT10_ZtautauMassiveCBPt0_CFilterBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167757.Sherpa_CT10_ZtautauMassiveCBPt0_CVetoBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167797.Sherpa_CT10_ZeeMassiveCBPt70_140_BFilter.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167798.Sherpa_CT10_ZeeMassiveCBPt70_140_CFilterBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167799.Sherpa_CT10_ZeeMassiveCBPt70_140_CVetoBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167800.Sherpa_CT10_ZmumuMassiveCBPt70_140_BFilter.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167801.Sherpa_CT10_ZmumuMassiveCBPt70_140_CFilterBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167802.Sherpa_CT10_ZmumuMassiveCBPt70_140_CVetoBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167803.Sherpa_CT10_ZtautauMassiveCBPt70_140_BFilter.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167804.Sherpa_CT10_ZtautauMassiveCBPt70_140_CFilterBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167805.Sherpa_CT10_ZtautauMassiveCBPt70_140_CVetoBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167809.Sherpa_CT10_ZeeMassiveCBPt140_280_BFilter.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167810.Sherpa_CT10_ZeeMassiveCBPt140_280_CFilterBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167811.Sherpa_CT10_ZeeMassiveCBPt140_280_CVetoBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167812.Sherpa_CT10_ZmumuMassiveCBPt140_280_BFilter.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167813.Sherpa_CT10_ZmumuMassiveCBPt140_280_CFilterBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167814.Sherpa_CT10_ZmumuMassiveCBPt140_280_CVetoBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167815.Sherpa_CT10_ZtautauMassiveCBPt140_280_BFilter.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167816.Sherpa_CT10_ZtautauMassiveCBPt140_280_CFilterBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167817.Sherpa_CT10_ZtautauMassiveCBPt140_280_CVetoBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167821.Sherpa_CT10_ZeeMassiveCBPt280_500_BFilter.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167822.Sherpa_CT10_ZeeMassiveCBPt280_500_CFilterBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167823.Sherpa_CT10_ZeeMassiveCBPt280_500_CVetoBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167824.Sherpa_CT10_ZmumuMassiveCBPt280_500_BFilter.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167825.Sherpa_CT10_ZmumuMassiveCBPt280_500_CFilterBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167826.Sherpa_CT10_ZmumuMassiveCBPt280_500_CVetoBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167827.Sherpa_CT10_ZtautauMassiveCBPt280_500_BFilter.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167828.Sherpa_CT10_ZtautauMassiveCBPt280_500_CFilterBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167829.Sherpa_CT10_ZtautauMassiveCBPt280_500_CVetoBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167833.Sherpa_CT10_ZeeMassiveCBPt500_BFilter.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167834.Sherpa_CT10_ZeeMassiveCBPt500_CFilterBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167835.Sherpa_CT10_ZeeMassiveCBPt500_CVetoBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167836.Sherpa_CT10_ZmumuMassiveCBPt500_BFilter.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167837.Sherpa_CT10_ZmumuMassiveCBPt500_CFilterBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167838.Sherpa_CT10_ZmumuMassiveCBPt500_CVetoBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167839.Sherpa_CT10_ZtautauMassiveCBPt500_BFilter.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167840.Sherpa_CT10_ZtautauMassiveCBPt500_CFilterBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.167841.Sherpa_CT10_ZtautauMassiveCBPt500_CVetoBVeto.merge.AOD.e2798_s1982_s2008_r5787_r5853/' : '',
'mc14_13TeV.147910.Pythia8_AU2CT10_jetjet_JZ0W.merge.AOD.e2743_s1982_s2008_r5720_r5853/':'',
'mc14_13TeV.147911.Pythia8_AU2CT10_jetjet_JZ1W.merge.AOD.e2743_s1982_s2008_r5720_r5853/':'',
'mc14_13TeV.147912.Pythia8_AU2CT10_jetjet_JZ2W.merge.AOD.e2743_s1982_s2008_r5720_r5853/':'',
'mc14_13TeV.147913.Pythia8_AU2CT10_jetjet_JZ3W.merge.AOD.e2743_s1982_s2008_r5720_r5853/':'',
'mc14_13TeV.147914.Pythia8_AU2CT10_jetjet_JZ4W.merge.AOD.e2743_s1982_s2008_r5720_r5853/':'',
'mc14_13TeV.147915.Pythia8_AU2CT10_jetjet_JZ5W.merge.AOD.e2743_s1982_s2008_r5720_r5853/':'',
'mc14_13TeV.147916.Pythia8_AU2CT10_jetjet_JZ6W.merge.AOD.e2743_s1982_s2008_r5720_r5853/':'',
'mc14_13TeV.147917.Pythia8_AU2CT10_jetjet_JZ7W.merge.AOD.e2743_s1982_s2008_r5720_r5853/':''
}

_list = simple.keys()

full_list = {}
for i in _list:
    r = askAmi(i[0:len(i)-1])
    for k in r:
       full_list[k] = [r[k][0], r[k][1]*1e6] # and convert to fb

print '# dsid xsec kfac'
for k in full_list:
    name = k[0:k.find('.merge')]
    gen='none'
    if 'Sherpa' in name:
      gen='sherpa'
    elif 'Pythia8' in name:
      gen='pythia8'
    else:
      gen='pythia'
    print name.split('.')[1]+'    '+str(full_list[k][1]) +'    1    '+gen

