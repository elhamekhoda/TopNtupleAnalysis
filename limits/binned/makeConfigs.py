from os import system

from ttres.inputs import *

def fixFile(template, final, i, doBOnlyFit):
  fr = open(template, 'r')
  f = open(final, 'w')

  for line in fr:
    if '% SIGNAL' in line:
      f.write('''
Sample: "Signal"
  Type: SIGNAL
  Title: "Signal"
  LineColor: 632
  NormFactor: "SigXsecOverSM",0,0,100
  HistoFile: "%s"
''' % ('hist_'+i))
      continue
    
    nline = line
    if 'FitTtres' in nline:
      nline = nline.replace('FitTtres', 'FitTtres_'+i)
    if 'JobTtres' in nline:
      nline = nline.replace('JobTtres', 'JobTtres_'+i)
    if 'FitType' in nline and doBOnlyFit:
      nline = nline.replace('SPLUSB', 'BONLY')
    f.write(nline)

  f.close()
  fr.close()


# B ONLY fit
fixFile('ttres/ttres_template.config', 'ttres/ttres_bkg.config', "tmp", True)
system('./myFit.exe h ttres/ttres_bkg.config')
system('./myFit.exe d ttres/ttres_bkg.config')
system('./myFit.exe w ttres/ttres_bkg.config')
system('./myFit.exe f ttres/ttres_bkg.config')
system('./myFit.exe p ttres/ttres_bkg.config')

# now go over to signal
for i in signalList:
  fixFile('ttres/ttres_template.config', 'ttres/ttres_'+i+'.config', i, False)

  system('./myFit.exe h ttres/ttres_'+i+'.config')
  system('./myFit.exe d ttres/ttres_'+i+'.config')
  system('./myFit.exe w ttres/ttres_'+i+'.config')
  system('./myFit.exe p ttres/ttres_'+i+'.config')
  system('./myFit.exe f ttres/ttres_'+i+'.config')
  system('./myFit.exe l ttres/ttres_'+i+'.config')


