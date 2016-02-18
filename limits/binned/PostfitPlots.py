
# run as 

from ROOT import *
import numpy
#from numpy import *

class FitRes:

    name = []
    pull = []
    errup = []
    errdw = []
    corr = numpy.matrix([])

    def __init__(self):
        name = []
        pull = []
        errup = []
        errdw = []
        corr = numpy.matrix([])

def loadSpectrum(sampleName, histName, syst):
    if sampleName != "bkg":
        print "hist_{:}.root".format(sampleName)
        f = TFile("hist_{:}.root".format(sampleName))
        print f
        print "{:}{:}".format(histName, syst)
        h = f.Get("{:}{:}".format(histName, syst))
        print h
        if h:
            h.SetDirectory(0)
        return h
    # it is == bkg, so sum all backgrounds
    h = None
    for i in ["ttbar", "Zjets", "Wjets", "VV", "singletop", "QCDe", "QCDmu"]:
        if h == None:
            h1 = loadSpectrum(i, histName, syst)
            if not h1:
               return h1
            h = h1.Clone("bkg{:}{:}".format(histName, syst))
            continue
        h.Add(loadSpectrum(i, histName, syst))
    return h

def copySpectrum(sampleName, histName, syst, newname):
    h = loadSpectrum(sampleName, histName, syst)
    if h == None:
        if 'dw' in syst:
            h = loadSpectrum(sampleName, histName, syst.replace('dw', 'up', 1))
    hc = h.Clone(newname)
    return hc

def loadStatsSq(h):
    for i in xrange(h.GetNbinsX()+1):
        h.SetBinContent(i, h.GetBinError(i)*h.GetBinError(i))

def loadZero(h):
    for i in xrange(h.GetNbinsX()+1):
        h.SetBinContent(i, 0)
        h.SetBinError(i, 0)
    h.Sumw2()

def histSqrt(h):
    for i in xrange(h.GetNbinsX()+1):
        if h.GetBinContent(i) < 0:
            print "Bin ",i," has negative content: ", h.GetBinContent(i)
            h.SetBinContent(i,0)
        h.SetBinContent(i, (h.GetBinContent(i))**0.5)

def MakePostfitPlot(fr, sampleName, histName, outputFile, outputFilePF, shortName):
    # TODO: escape code for data

    # nominal
    nom  = loadSpectrum(sampleName, histName, "")

    # nominal post fit
    nom_PF = copySpectrum(sampleName, histName, "", "{:}PF".format(histName))

    # prefit variation up: load it initially with square of stat error
    all_up  = copySpectrum(sampleName, histName, "", "{:}up".format(histName))
    loadStatsSq(all_up)
    # prefit variation dw: load it initially with square of stat error
    all_dw  = copySpectrum(sampleName, histName, "", "{:}dw".format(histName))
    loadStatsSq(all_dw)

    # post fit variation up: load it with zeroes
    all_up_PF  = copySpectrum(sampleName, histName, "", "{:}PFup".format(histName))
    loadZero(all_up_PF)
    # post fit variation up: load it with zeroes
    all_dw_PF  = copySpectrum(sampleName, histName, "", "{:}PFdw".format(histName))
    loadZero(all_dw_PF)

    # post fit variation up without correlations: load it with zeroes
    all_up_PF_uncorr  = copySpectrum(sampleName, histName, "", "{:}PFuncorrup".format(histName))
    loadZero(all_up_PF_uncorr)
    # post fit variation up without correlations: load it with zeroes
    all_dw_PF_uncorr  = copySpectrum(sampleName, histName, "", "{:}PFuncorrdw".format(histName))
    loadZero(all_dw_PF_uncorr)

    h_list_up_PF = []
    h_list_dw_PF = []

    for idx in xrange(len(fr.name)):
        systLabel = fr.name[idx]
        pull = fr.pull[idx]
        pull_error = fr.errup[idx]

        # first the gamma
        if "gamma_stat_"+shortName in systLabel:
            theBin = int(systLabel.split('_')[-1])
            nom_PF.SetBinContent(theBin, nom_PF.GetBinContent(theBin)*pull)
            # calculate all_up = stat^2 + \sum_{syst = i} \Delta_i^2 + ((1 - gamma)*v0)^2
            v0 = nom.GetBinContent(theBin)
            all_up_PF_uncorr.SetBinContent(theBin, all_up_PF_uncorr.GetBinContent(theBin)+(v0*(pull+pull_error))**2)
            all_dw_PF_uncorr.SetBinContent(theBin, all_dw_PF_uncorr.GetBinContent(theBin)+(v0*(pull+pull_error))**2)

            h_up_PF = nom_PF.Clone("{:}{:}PFup".format(histName, systLabel))
            h_dw_PF = nom_PF.Clone("{:}{:}PFdw".format(histName, systLabel))

            for b in xrange(0, h_up_PF.GetNbinsX()+1):
                if b != theBin:
                    h_up_PF.SetBinContent(b, 0)
                    h_dw_PF.SetBinContent(b, 0)
                else:
                    h_up_PF.SetBinContent(theBin, h_up_PF.GetBinContent(theBin)*(pull_error))
                    h_dw_PF.SetBinContent(theBin, h_up_PF.GetBinContent(theBin)*(pull_error))

            h_list_up_PF.append(h_up_PF)
            h_list_dw_PF.append(h_dw_PF)
        elif "gamma_stat_" in systLabel:
            h_up_PF = nom_PF.Clone("{:}{:}PFup".format(histName, systLabel))
            h_dw_PF = nom_PF.Clone("{:}{:}PFdw".format(histName, systLabel))
            for b in xrange(0, h_up_PF.GetNbinsX()+1):
                h_up_PF.SetBinContent(b, 0)
                h_dw_PF.SetBinContent(b, 0)
            h_list_up_PF.append(h_up_PF)
            h_list_dw_PF.append(h_dw_PF)
        # now normal uncertainties
        else:
            h_var = loadSpectrum(sampleName, histName, systLabel)
            if h_var:
                h_up = h_var
                h_dw = h_var
            else:
                h_up = loadSpectrum(sampleName, histName, systLabel+"up")
                h_dw = loadSpectrum(sampleName, histName, systLabel+"dw")
                if h_dw == None:
                    h_dw = loadSpectrum(sampleName, histName, systLabel+"up")

            h_var_PF = loadSpectrum(sampleName, histName, systLabel)
            if h_var_PF:
                h_up_PF = h_var_PF.Clone("{:}{:}PFup".format(histName, systLabel))
                h_dw_PF = h_var_PF.Clone("{:}{:}PFdw".format(histName, systLabel))
            else:
                h_up_PF = copySpectrum(sampleName, histName, systLabel+"up", "{:}{:}PFup".format(histName, systLabel))
                h_dw_PF = copySpectrum(sampleName, histName, systLabel+"dw", "{:}{:}PFdw".format(histName, systLabel))

            h_correction = nom_PF.Clone("{:}corr{:}".format(histName, systLabel))
            if pull > 0:
                h_correction.Add(h_up, nom, 1 , -1) # up - nom
            else:
                h_correction.Add(h_dw, nom, -1 , 1) # nom - dw

            nom_PF.Add(h_correction, pull) # nominal PF = nom(bin)*gamma(bin) + \sum_{i=syst} pull_i \times \Delta_i
                                           # where \Delta_i = (up - nom) if pull > 0 or (nom - dw) if pull <= 0

            # calculate all_up = stat^2 + \sum_{syst = i} \Delta_i^2 + ((1 - gamma)*v0)^2
            # for now it is already stat^2
            for oneBin in xrange(nom.GetNbinsX()+1):
                v0 = nom.GetBinContent(oneBin)
                e0 = nom.GetBinError(oneBin)
                vUp = h_up.GetBinContent(oneBin)-v0
                vDw = h_dw.GetBinContent(oneBin)-v0
                if vUp < vDw:
                    v0 = vUp
                    vUp = vDw
                    vDw = v0
                all_up.SetBinContent(oneBin, all_up.GetBinContent(oneBin)+vUp**2)
                all_dw.SetBinContent(oneBin, all_dw.GetBinContent(oneBin)+vDw**2)

            # do the same for the post fit histogram without correlations
            # but rescale up/dw amount by pull error
            for oneBin in xrange(nom.GetNbinsX()+1):
                v0 = nom.GetBinContent(oneBin)
                e0 = nom.GetBinError(oneBin)
                vUp = h_up.GetBinContent(oneBin)-v0
                vDw = h_dw.GetBinContent(oneBin)-v0
                vUp = vUp * pull_error
                vDw = vDw * pull_error
                if vUp < vDw:
                    v0 = vUp
                    vUp = vDw
                    vDw = v0
                all_up_PF_uncorr.SetBinContent(oneBin, all_up_PF_uncorr.GetBinContent(oneBin)+vUp**2)
                all_dw_PF_uncorr.SetBinContent(oneBin, all_dw_PF_uncorr.GetBinContent(oneBin)+vDw**2)

            # calculate all_up = stat^2 + \sum_{syst = i} \Delta_i^2
            # for now it is already stat^2
            for oneBin in xrange(nom.GetNbinsX()+1):
                v0 = nom.GetBinContent(oneBin)
                e0 = nom.GetBinError(oneBin)
                vUp = h_up.GetBinContent(oneBin)-v0
                vDw = h_dw.GetBinContent(oneBin)-v0
                vUp = vUp * pull_error
                vDw = vDw * pull_error
                if vUp < vDw:
                    v0 = vUp
                    vUp = vDw
                    vDw = v0
                h_up_PF.SetBinContent(oneBin, vUp)
                h_dw_PF.SetBinContent(oneBin, vDw)

            h_list_up_PF.append(h_up_PF)
            h_list_dw_PF.append(h_dw_PF)
        # end of if about gamma
    # end of systs loop

    # add stat errors in post fit quadrature sum and nominal
    for oneBin in xrange(nom.GetNbinsX()+1):
        e0 = nom.GetBinError(oneBin)
        nom_PF.SetBinError(oneBin, e0)
        all_up_PF_uncorr.AddBinContent(oneBin, e0**2)
        all_dw_PF_uncorr.AddBinContent(oneBin, e0**2)
        all_up_PF.AddBinContent(oneBin, e0**2)
        all_dw_PF.AddBinContent(oneBin, e0**2)

    # all_up_PF = all_up_PF (now includes sum in quadrature of systs and stat) +
    #            + \sum_{i,j} corr(i, j) \times up_PF(i) \times up_PF(j)
    tmp_up = nom_PF.Clone("tmp_up")
    tmp_dw = nom_PF.Clone("tmp_dw")
    for i in xrange(len(fr.name)):
        for j in xrange(len(fr.name)):
            loadZero(tmp_up)
            loadZero(tmp_dw)
            tmp_up.Multiply(h_list_up_PF[i], h_list_up_PF[j], fr.corr[i, j], 1)
            tmp_dw.Multiply(h_list_dw_PF[i], h_list_dw_PF[j], fr.corr[i, j], 1)
            all_up_PF.Add(tmp_up)
            all_dw_PF.Add(tmp_dw)

    # take sqrt of the sum in quadrature of the prefit up/dw variations
    histSqrt(all_up)
    histSqrt(all_dw)

    histSqrt(all_up_PF_uncorr)
    histSqrt(all_dw_PF_uncorr)

    histSqrt(all_up_PF)
    histSqrt(all_dw_PF)

    # just add variations to nominal ... but make a copy first
    all_rel_up = all_up.Clone("{:}_rel".format(all_up.GetName()))
    all_rel_dw = all_dw.Clone("{:}_rel".format(all_dw.GetName()))

    all_rel_up_PF = all_up_PF.Clone("{:}_rel".format(all_up_PF.GetName()))
    all_rel_dw_PF = all_dw_PF.Clone("{:}_rel".format(all_dw_PF.GetName()))

    # all_up = nom + up
    # all_dw = nom - dw
    all_up.Add(nom, all_up, 1, 1)
    all_dw.Add(nom, all_dw, 1, -1)
    
    all_up_PF.Add(nom_PF, all_up_PF, 1, 1)
    all_dw_PF.Add(nom_PF, all_dw_PF, 1, -1)

    # and write it in the output
    # prefit first
    outputFile.cd()
    nom.Write("{:}{:}".format(sampleName, histName))
    all_up.Write("{:}{:}up".format(sampleName, histName))
    all_dw.Write("{:}{:}dw".format(sampleName, histName))
    all_rel_up.Write("{:}{:}up_rel".format(sampleName, histName))
    all_rel_dw.Write("{:}{:}dw_rel".format(sampleName, histName))

    outputFilePF.cd()
    nom_PF.Write("{:}{:}".format(sampleName, histName))
    all_up_PF.Write("{:}{:}up".format(sampleName, histName))
    all_dw_PF.Write("{:}{:}dw".format(sampleName, histName))
    all_rel_up_PF.Write("{:}{:}up_rel".format(sampleName, histName))
    all_rel_dw_PF.Write("{:}{:}dw_rel".format(sampleName, histName))

def readParams(inputFile):
    fr = FitRes()
    inp = open(inputFile)
    nuipNext = False
    corrNext = False
    linesIn = 0
    for line in inp:
        line = line[0:-1]
        if "NUISANCE" in line:
            nuipNext = True
            corrNext = False
            linesIn = 0
            continue
        if "CORRELATION" in line:
            nuipNext = False
            corrNext = True
            linesIn = 0
            continue
        lsplit = line.split()
        if len(lsplit) < 2:
            continue
        if nuipNext:
            fr.name.append(lsplit[0])
            fr.pull.append(float(lsplit[1]))
            fr.errup.append(float(lsplit[2]))
            fr.errdw.append(float(lsplit[3]))
        if corrNext:
            if linesIn == 0:
                size = int(lsplit[0])
                fr.corr = numpy.matrix(numpy.zeros([size, size]))
            else:
                idx = linesIn - 1
                for col in xrange(len(lsplit)):
                    fr.corr[idx, col] = float(lsplit[col])
        linesIn = linesIn + 1
    return fr

def MakeAllPostfitPlots(inputFile, sampleList, output, outputPF):
    fr = readParams(inputFile)
    outputFile = TFile(output, "RECREATE")
    outputFilePF = TFile(outputPF, "RECREATE")
    shortNameForGamma = {'xboostede':'be', 'xboostedmu':'bmu'}
    for sampleName in sampleList:
        for histName in ["xboostede", "xboostedmu"]:
            print "Sample", sampleName," hist",histName
            MakePostfitPlot(fr, sampleName, histName, outputFile, outputFilePF, shortNameForGamma[histName])
    outputFile.Close()
    outputFilePF.Close()

if __name__ == "__main__":
    MakeAllPostfitPlots("params_bonly.txt", ["ttbar", "Wjets", "Zjets", "singletop", "VV", "QCDe", "QCDmu", "Zprime400", "Zprime500", "Zprime750", "Zprime1000", "Zprime1250", "Zprime1500", "Zprime1750", "Zprime2000", "Zprime2250", "Zprime2500", "Zprime2750", "Zprime3000", "Zprime4000", "Zprime5000", "bkg"], "spectrum_prefit.root", "spectrum_postfit.root")
