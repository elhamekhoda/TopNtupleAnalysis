#!/usr/bin/env python
from os import path

from ROOT import *
import math
import array

Internal = True
#Internal = False

files = "/nfs/dust/atlas/user/danilo/res_2429/"

binning = [260, 300, 340, 380, 420, 500, 600, 700, 800, 900, 1000]

gStyle.SetOptStat(0)
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)

def stampATLAS(text, x, y):
  t = TLatex()
  t.SetNDC()
  t.SetTextFont(72)
  t.SetTextColor(1)
  delx = 0.115*696*gPad.GetWh()/(472*gPad.GetWw()) #+ 0.05
  t.SetTextSize(0.04)
  t.DrawLatex(x,y,"ATLAS")
  t.SetTextFont(42)
  t.SetTextSize(0.04)
  t.DrawLatex(x+delx, y, text)

def stampLumiText(lumi, x, y, text, size):
  t = TLatex()
  t.SetNDC()
  t.SetTextFont(42)
  t.SetTextColor(1)
  t.SetTextSize(size)
  #t.DrawLatex(x,y,"#int L dt = "+str(lumi)+" fb^{-1}, "+text)
  if lumi > 0:
    t.DrawLatex(x,y, text+", "+str(lumi)+" fb^{-1}")
  else:
    t.DrawLatex(x,y, text)

def stampText(x, y, text, size):
  t = TLatex()
  t.SetNDC()
  t.SetTextFont(42)
  t.SetTextColor(1)
  t.SetTextSize(size)
  t.DrawLatex(x,y, text)


def setStyle(h, col, sty, ylabel = "Events", xlabel = "#frac{p_{T,reco} - p_{T,truth}}{p_{T,truth}}", ylim = -1):
    h.GetYaxis().SetTitle(ylabel);
    h.GetXaxis().SetTitle(xlabel)
    h.GetXaxis().SetTitleOffset(1.5);
    h.GetYaxis().SetTitleOffset(1.5);
    h.GetXaxis().SetLabelSize(0.05);
    h.GetXaxis().SetTitleSize(0.05);
    h.GetYaxis().SetLabelSize(0.05);
    h.GetYaxis().SetTitleSize(0.05);
    h.SetLineWidth(2);
    h.SetLineStyle(sty);
    h.SetLineColor(col);
    if ylim > 0 and isinstance(h, TH1F):
      h.GetYaxis().SetRangeUser(0, ylim);
      h.SetMaximum(ylim);

def cutChannel(cn):

  nb = 0
  for l in xrange(len(cn.tjet_pt)):
    if cn.tjet_mv2c10[l] > 0.6455:
      nb += 1
  if nb < 1:
    return False

  n = 0
  for i in range(0, len(cn.ljet_pt)):
    if cn.ljet_pt[i] < 260e3:
      continue
    if cn.ljet_m[i] < 50e3:
      continue
    n += 1

  if n < 1:
    return False

  if cn.met_met < 20e3:
    return False

  if len(cn.jet_pt) < 1:
    return False

  lep_pt = -1
  lep_phi = 99
  lep_eta = 99
  if len(cn.el_pt) == 1 and len(cn.mu_pt) == 0:
    lep_pt = cn.el_pt[0]
    lep_eta = cn.el_eta[0]
    lep_phi = cn.el_phi[0]
  elif len(cn.mu_pt) == 1 and len(cn.el_pt) == 0:
    lep_pt = cn.mu_pt[0]
    lep_eta = cn.mu_eta[0]
    lep_phi = cn.mu_phi[0]
  else:
    return False

  mtw = math.sqrt(2*lep_pt*cn.met_met*(1-math.cos(lep_phi - cn.met_phi)))
  if cn.met_met + mtw < 60e3:
    return False

  n = 0
  for i in range(0, len(cn.ljet_pt)):
    if cn.ljet_pt[i] < 260e3:
      continue
    if cn.ljet_m[i] < 50e3:
      continue
    dp = math.fabs(lep_phi - cn.ljet_phi[i])
    if dp > 2*math.pi:
      dp -= 2*math.pi
    if dp < 2.3:
      continue
    n += 1
  if n < 1:
    return False

  found = False
  mindR = 1.5
  highPt = 0
  jetIdx = -1
  for k in range(0, len(cn.jet_pt)):
    dPhi = math.fabs(cn.jet_phi[k] - lep_phi)
    if dPhi > 2*math.pi:
      dPhi -= 2*math.pi
    dEta = math.fabs(cn.jet_eta[k] - lep_eta)
    dR = (dEta**2 + dPhi**2)**0.5
    if dR < mindR and cn.jet_pt[k] > highPt:
      mindR = dR
      highPt = cn.jet_pt[k]
      jetIdx = k
      found = True
  return found

def drawIt(hr, channels, label, suf = "", ylabel = ""):
  cacc = TCanvas("c", "", 800, 600);
  cacc.SetBottomMargin(0.2)
  cacc.SetLeftMargin(0.14)
  l = TLegend(0.65,0.65,0.90,0.89)
  l.SetBorderSize(0)

  first = True
  for i in sorted(channels.keys()):
    op = "hist"
    if not isinstance(hr[i], TH1F):
      op = ""
    if ylabel != "":
      hr[i].GetYaxis().SetTitle(ylabel)
    if first:
      hr[i].Draw(op);
    else:
      hr[i].Draw("%s same" % op);
    first = False
    l.AddEntry(hr[i], channels[i], "L")
  
  l.Draw()
  gPad.RedrawAxis()

  if Internal:
    stampATLAS("Simulation Internal", 0.18, 0.83)
  else:
    stampATLAS("Simulation", 0.18, 0.83)
  stampLumiText(-1, 0.18, 0.75, "#sqrt{s} = 13 TeV", 0.04)
  stampText(0.18, 0.70, label, 0.05)

  suf += ""
  if not Internal:
    suf += "_ATLASSimul"
  for i in [".eps", ".png", ".pdf"]:
    cacc.SaveAs("res"+suf+i)

def doIt():
  cn = TChain("nominal")

  hpt = {}
  htau32 = {}
  hm = {}
  fout = TFile("res.root", "recreate")
  for i in binning:
    hpt[i] = TH1F("pt_%s"%i, "", 20, -0.5, 0.5)
    htau32[i] = TH1F("tau32_%s"%i, "", 20, -0.5, 0.5)
    hm[i] = TH1F("m_%s"%i, "", 20, -0.5, 0.5)

  import glob
  for d in glob.glob(files+"/*"):
    for f in glob.glob(d+"/*"):
      cn.Add(f)

  for i in xrange(cn.GetEntries()):
    cn.GetEntry(i)
    if i % 10000 == 0:
      print "Entry %d/%d" % (i, cn.GetEntries())
    if not cutChannel(cn):
      continue

    lep_pt = -1
    lep_phi = 99
    lep_eta = 99
    if len(cn.el_pt) == 1 and len(cn.mu_pt) == 0:
      lep_pt = cn.el_pt[0]
      lep_eta = cn.el_eta[0]
      lep_phi = cn.el_phi[0]
    elif len(cn.mu_pt) == 1 and len(cn.el_pt) == 0:
      lep_pt = cn.mu_pt[0]
      lep_eta = cn.mu_eta[0]
      lep_phi = cn.mu_phi[0]

    mindR = 1.5
    highPt = 0
    jetIdx = -1
    for k in range(0, len(cn.jet_pt)):
      dPhi = math.fabs(cn.jet_phi[k] - lep_phi)
      if dPhi > 2*math.pi:
        dPhi -= 2*math.pi
      dEta = math.fabs(cn.jet_eta[k] - lep_eta)
      dR = (dEta**2 + dPhi**2)**0.5
      if dR < mindR and cn.jet_pt[k] > highPt:
        mindR = dR
        highPt = cn.jet_pt[k]
        jetIdx = k

    sjet_eta = cn.jet_eta[jetIdx]
    sjet_phi = cn.jet_phi[jetIdx]

    for j in range(0, len(cn.ljet_pt)):
      if cn.ljet_pt[j] < binning[0]*1e3:
        continue
      if cn.ljet_m[j] < 50e3:
        continue
      dp = math.fabs(lep_phi - cn.ljet_phi[j])
      if dp > 2*math.pi:
        dp -= 2*math.pi
      if dp < 2.3:
        continue

      dPhi = math.fabs(sjet_phi - cn.ljet_phi[j])
      if dPhi > 2*math.pi:
        dPhi -= 2*math.pi
      dEta = math.fabs(sjet_eta - cn.ljet_phi[j])
      dR = (dEta**2 + dPhi**2)**0.5
      if dR < 1.5:
        continue

      binPos = len(binning)-1
      for k in range(0, len(binning)-1):
        if cn.ljet_pt[j] < binning[k+1]*1e3:
          binPos = k
          break
      #print "Jet pT", cn.ljet_pt[j], "bin", binning[binPos]
      binVal = binning[binPos]
      res_pt = -99
      res_m = -99
      res_tau32 = -99
      mindR = 0.7
      truthPos = -1
      for k in range(0, len(cn.akt10truthjet_pt)):
        dPhi = math.fabs(cn.akt10truthjet_phi[k] - cn.ljet_phi[j])
	if dPhi > 2*math.pi:
	  dPhi -= 2*math.pi
	dEta = math.fabs(cn.akt10truthjet_eta[k] - cn.ljet_phi[j])
	dR = (dEta**2 + dPhi**2)**0.5
	if dR < mindR:
	  mindR = dR
	  truthPos = k
      if truthPos >= 0:
        res_pt = (cn.ljet_pt[j] - cn.akt10truthjet_pt[truthPos])/cn.akt10truthjet_pt[truthPos]
	if cn.akt10truthjet_m[truthPos] != 0:
          res_m = (cn.ljet_m[j] - cn.akt10truthjet_m[truthPos])/cn.akt10truthjet_m[truthPos]
	else:
	  res_m = 99
	if cn.akt10truthjet_tau32_wta[truthPos] != 0:
          res_tau32 = (cn.ljet_tau32_wta[j] - cn.akt10truthjet_tau32_wta[truthPos])/cn.akt10truthjet_tau32_wta[truthPos]
	else:
	  res_tau32 = 99
        hpt[binVal].Fill(res_pt, cn.weight_mc*cn.weight_leptonSF*cn.weight_trackjet_bTagSF_70)
        hm[binVal].Fill(res_m, cn.weight_mc*cn.weight_leptonSF*cn.weight_trackjet_bTagSF_70)
        htau32[binVal].Fill(res_tau32, cn.weight_mc*cn.weight_leptonSF*cn.weight_trackjet_bTagSF_70)

  lt_color = [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 15, 30, 40, 38, 49]
  #lt_line = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
  c = 0
  hpt_max = 0
  hm_max = 0
  htau32_max = 0
  for i in binning:
    m = hpt[i].GetBinContent(hpt[i].GetMaximumBin())
    if m > hpt_max: hpt_max = m
    m = hm[i].GetBinContent(hm[i].GetMaximumBin())
    if m > hm_max: hm_max = m
    m = htau32[i].GetBinContent(htau32[i].GetMaximumBin())
    if m > htau32_max: htau32_max = m
  for i in binning:
    st_color = lt_color[c]
    st_line = 1 #lt_line[c]
    setStyle(hpt[i], st_color,  st_line, "Events", "#frac{p_{T,reco} - p_{T,truth}}{p_{T,truth}}", hpt_max*1.6)
    setStyle(hm[i], st_color,  st_line, "Events", "#frac{m_{reco} - m_{truth}}{m_{truth}}", hm_max*1.6)
    setStyle(htau32[i], st_color,  st_line, "Events", "#frac{#tau_{32,reco} - #tau_{32,truth}}{#tau_{32,truth}}", htau32_max*1.6)
    hpt[i].Scale(1.0/hpt[i].Integral())
    hm[i].Scale(1.0/hm[i].Integral())
    htau32[i].Scale(1.0/htau32[i].Integral())
    c += 1


  leg = {}
  for i in range(0, len(binning)):
    if i < len(binning)-1:
      leg[binning[i]] = "p_{T} #in [%d GeV, %d GeV]" % (binning[i], binning[i+1])
    else:
      leg[binning[i]] = "p_{T} > %d GeV" % binning[i]

  drawIt(hpt, leg, "p_{T}", suf = "pt")
  drawIt(hm, leg, "mass", suf = "m")
  drawIt(htau32, leg, "#tau_{32}", suf = "tau32")
  fout.Write()
  fout.Close()

def plotSummary():

  hsum_pt = TH1F("sum_pt", "", len(binning)-1, array.array('d',binning))
  hsum_m = TH1F("sum_m", "", len(binning)-1, array.array('d',binning))
  hsum_tau32 = TH1F("sum_tau32", "", len(binning)-1, array.array('d',binning))

  hsum_pt_fit = TF1("sum_pt_fit", "TMath::Sqrt([0]^2 + ([1]/x)^2)", binning[0], binning[-1])
  hsum_m_fit = TF1("sum_m_fit", "TMath::Sqrt([0]^2 + ([1]/x)^2)", binning[0], binning[-1])
  hsum_tau32_fit = TF1("sum_tau32_fit", "[0]*(1 - TMath::Exp(-[1]*x))", binning[0], binning[-1])
  hsum_tau32_fit.SetParameter(0, 0.2)
  hsum_tau32_fit.SetParameter(1, 1.0/100.0)

  hpt = {}
  htau32 = {}
  hm = {}
  fout = TFile("res.root", "read")
  for i in binning:
    hpt[i] = fout.Get("pt_%s"%i)
    htau32[i] = fout.Get("tau32_%s"%i)
    hm[i] = fout.Get("m_%s"%i)

  result = {}
  result['pt'] = []
  result['m'] = []
  result['tau32'] = []
  for i in range(0, len(binning)):
    ib = binning[i]
    for h,v,r,name in [[hpt, hsum_pt, result['pt'], 'pT'], [htau32, hsum_tau32, result['tau32'], 'tau32'], [hm, hsum_m, result['m'], 'm']]:
      s = 1
      m = 0.0
      se = 0
      ff = TF1("%s_fit" % h[ib], "gaus", -0.5, 0.5)
      h[ib].Fit(ff, "RSN0", "", m-s, m+s)
      m = ff.GetParameter(1)
      s = ff.GetParameter(2)
      se = ff.GetParError(2)
      h[ib].Fit(ff, "RSN0", "", m-2*s, m+2*s)
      m = ff.GetParameter(1)
      s = ff.GetParameter(2)
      se = ff.GetParError(2)
      v.SetBinContent(i+1, s)
      v.SetBinError(i+1, se)
      r.append(s)
      ff.SetRange(m-2*s, m+2*s)
      drawIt({'0':h[ib], '1':ff}, {'0':'%s in bin %d GeV' % (name, ib), '1': 'Fit'}, name, suf = "fit%s%d" % (name, ib))
  print "Results:"
  print binning
  print "pT: ", result['pt']
  print "m: ", result['m']
  print "tau32: ", result['tau32']

  for h,f,name in [[hsum_pt, hsum_pt_fit, "pT"], [hsum_tau32, hsum_tau32_fit, "tau32"], [hsum_m, hsum_m_fit, "mass"]]:
    h.Fit(f, "RSN0", "", binning[0], binning[-1])
    print "Fit for %s for sigma = %s, with [0] = %f +/- %f and [1] = %f +/- %f" % (name, f.GetTitle(), f.GetParameter(0), f.GetParError(0), f.GetParameter(1), f.GetParError(1))

  setStyle(hsum_pt, kBlue, 1, "#frac{p_{T,reco} - p_{T,truth}}{p_{T,truth}}", "p_{T,reco} [GeV]", 0.5)
  setStyle(hsum_m, kRed, 1, "#frac{m_{reco} - m_{truth}}{m_{truth}}", "p_{T,reco} [GeV]", 0.5)
  setStyle(hsum_tau32, kMagenta, 1, "#frac{#tau_{32,reco} - #tau_{32,truth}}{#tau_{32,truth}}", "p_{T,reco} [GeV]", 0.5)

  setStyle(hsum_pt_fit, kBlue, 2, "#frac{p_{T,reco} - p_{T,truth}}{p_{T,truth}}", "p_{T,reco} [GeV]", 0.5)
  setStyle(hsum_m_fit, kRed, 2, "#frac{m_{reco} - m_{truth}}{m_{truth}}", "p_{T,reco} [GeV]", 0.5)
  setStyle(hsum_tau32_fit, kMagenta, 2, "#frac{#tau_{32,reco} - #tau_{32,truth}}{#tau_{32,truth}}", "p_{T,reco} [GeV]", 0.5)

  drawIt({'pt':hsum_pt, 'ptfit': hsum_pt_fit, 'tau32':hsum_tau32, 'tau32fit': hsum_tau32_fit, 'm': hsum_m, 'mfit': hsum_m_fit}, {'pt':'p_{T}', 'ptfit':'p_{T} fit', 'tau32':'#tau_{32}', 'tau32fit': '#tau_{32} fit', 'm':'mass', 'mfit': 'mass fit'}, "Summary", suf = "summary", ylabel = "Resolution")
  fout.Close()

# call it
doIt()
plotSummary()

