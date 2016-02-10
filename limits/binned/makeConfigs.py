from os import system

from inputs import *

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
fixFile('ttres_template.config', 'ttres_bkg.config', "tmp", True)
system('cp -f hist_Zprime2000.root hist_tmp.root') ## use a dummy signal for the background only fit
system('./myFit.exe h ttres_bkg.config')
system('./myFit.exe d ttres_bkg.config')
system('./myFit.exe w ttres_bkg.config')
system('./myFit.exe f ttres_bkg.config')
system('./myFit.exe p ttres_bkg.config')

# now go over to signal
for i in signalList:
  fixFile('ttres_template.config', 'ttres_'+i+'.config', i, False)

  system('./myFit.exe h ttres_'+i+'.config')
  system('./myFit.exe d ttres_'+i+'.config')
  system('./myFit.exe w ttres_'+i+'.config')
  system('./myFit.exe p ttres_'+i+'.config')
  system('./myFit.exe f ttres_'+i+'.config')
  system('./myFit.exe l ttres_'+i+'.config')


