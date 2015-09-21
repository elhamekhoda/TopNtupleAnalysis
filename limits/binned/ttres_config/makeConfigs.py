from os import system

from ttres_config.inputs import *

for i in signalList:
  fr = open('ttres_config/ttres_template.config', 'r')
  f = open('ttres_config/ttres_'+i+'.config', 'w')
  for line in fr:
    if '% SIGNAL' in line:
      f.write('''
Sample: "Signal"
  Type: SIGNAL
  Title: "Signal"
  FillColor: 632
  LineColor: 632
  NormFactor: "SigXsecOverSM",1,0,100
  HistoFile: "%s"
''' % ('hist_'+i))
      continue
    
    nline = line
    if 'FitTtres' in nline:
      nline = nline.replace('FitTtres', 'FitTtres_'+i)
    f.write(nline)

  f.close()
  fr.close()

  system('./myFit.exe h ttres_config/ttres_'+i+'.config')
  system('./myFit.exe d ttres_config/ttres_'+i+'.config')
  system('./myFit.exe w ttres_config/ttres_'+i+'.config')
  system('./myFit.exe f ttres_config/ttres_'+i+'.config')
  system('./myFit.exe l ttres_config/ttres_'+i+'.config')

