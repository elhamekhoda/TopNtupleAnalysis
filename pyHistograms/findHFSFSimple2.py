#!/usr/bin/env python

import ROOT
import uncertainties as unc
import uncertainties.unumpy as unp
import numpy as np
import nemmen

odir = 'hists_WjetsHF2'
files = {}
channels = ['Wpre_resjets_el', 'Wpre_resjets_mu', 'Wtag_resjets_el', 'Wtag_resjets_mu', 'Wtag2_resjets_el', 'Wtag2_resjets_mu']
samples = ['data', 'tt', 'zjets', 'vv', 'wbbjets', 'wccjets', 'wcjets', 'wljets', 'singletop']
for ch in channels:
  files[ch] = {
         'data' : '%s/%s_%s.root' % (odir, ch, 'data'),
         'wbbjets' : '%s/%s_%s.root' % (odir, ch, 'wbbjets'),
         'wccjets' : '%s/%s_%s.root' % (odir, ch, 'wccjets'),
         'wcjets' : '%s/%s_%s.root' % (odir, ch, 'wcjets'),
         'wljets' : '%s/%s_%s.root' % (odir, ch, 'wljets'),
         'singletop' : '%s/%s_%s.root' % (odir, ch, 'singletop'),
         'tt' : '%s/%s_%s.root' % (odir, ch, 'tt'),
         'zjets' : '%s/%s_%s.root' % (odir, ch, 'zjets'),
         'vv' : '%s/%s_%s.root' % (odir, ch, 'vv'),
	}

def toHist(name, inp, ch, sample, q):
	h = ROOT.TH1F(name, "", 5, 0.5, 5.5)
	for njets in range(1,6):
		h.SetBinContent(njets, inp[ch][sample][njets][q].n)
		h.SetBinError(njets, inp[ch][sample][njets][q].s)
	h.SetDirectory(0)
	return h


def plotConfig(name, inp, ch, sample, q):
	h = toHist("tmp", inp, ch, sample, q)
	ROOT.gStyle.SetOptStat(0)
	ROOT.gStyle.SetPadTickX(1)
	ROOT.gStyle.SetPadTickY(1)

	c = ROOT.TCanvas("c", "", 800, 600);

	m = h.GetBinContent(h.GetMaximumBin())*1.3
	h.GetYaxis().SetRangeUser(0, m);
	h.GetYaxis().SetTitle("Events");
	h.GetXaxis().SetTitle("Number of jets");
	h.GetXaxis().SetTitleOffset(0.9);
	h.GetXaxis().SetLabelSize(0.05);
	h.GetXaxis().SetTitleSize(0.05);
	h.SetLineWidth(2)
	h.Draw("hist");
	c.SaveAs(name)

def plotStack(name, inp, ch, samples, q):
	ROOT.gStyle.SetOptStat(0)
	ROOT.gStyle.SetPadTickX(1)
	ROOT.gStyle.SetPadTickY(1)

	c = ROOT.TCanvas("c", "", 800, 600);
	l = ROOT.TLegend(0.5,0.67,0.87,0.89)
	l.SetBorderSize(0)
	l.SetNColumns(2)
	st = ROOT.THStack("stack", "")
	count = len(samples)-1
	col = [0, ROOT.kGreen, ROOT.kCyan, ROOT.kRed, ROOT.kAzure+3, 62, 95, 5]
	for s in reversed(samples):
		h = toHist("%s_%s_%d" % (ch, s, q), inp, ch, s, q)
		h.SetFillColor(col[count])
		h.SetLineColor(1)
		h.SetLineWidth(2)
		st.Add(h)
		l.AddEntry(h, s, "F")
		count -= 1

	hdata = toHist("%s_%s_%d" % (ch, "data", q), inp, ch, "data", q)
	l.AddEntry(hdata, "data", "LP")
	m = hdata.GetBinContent(hdata.GetMaximumBin())*1.4
	st.SetMaximum(m)
	st.SetMinimum(0)
	st.Draw()
	st.GetYaxis().SetTitle("Events");
	st.GetXaxis().SetTitle("Number of jets");
	st.GetXaxis().SetTitleOffset(0.9);
	st.GetXaxis().SetLabelSize(0.05);
	st.GetXaxis().SetTitleSize(0.05);
	st.GetYaxis().SetRangeUser(0, m);
	st.Draw("hist")
	c.Update()
	hdata.GetYaxis().SetRangeUser(0, m)
	hdata.SetMarkerStyle(20)
	hdata.SetMarkerSize(1.0)
	hdata.SetLineWidth(2)
	hdata.SetLineColor(1)
	hdata.Draw("e1 same")
	l.Draw()
	c.SaveAs(name)

def main():
	# in[channel][sample][njet][charge]
	inp = {}
	for ch in channels:
		inp[ch] = {}
		for s in samples:
			inp[ch][s] = {}
			L = 1.0
			if not 'data' in s:
				L = 1.79617e3
			oneFile = ROOT.TFile(files[ch][s])
			histPos = oneFile.Get('nJetsPos')
			histNeg = oneFile.Get('nJetsNeg')
			histAll = oneFile.Get('nJets')
			for njets in range(1,6):
				inp[ch][s][njets] = {}
				inp[ch][s][njets][1] = unc.ufloat(L*histPos.GetBinContent(njets), L*histPos.GetBinError(njets))
				inp[ch][s][njets][-1] = unc.ufloat(L*histNeg.GetBinContent(njets), L*histNeg.GetBinError(njets))
				inp[ch][s][njets][0] = unc.ufloat(L*histAll.GetBinContent(njets), L*histAll.GetBinError(njets))
	
	for ch in channels:
		for q in [0,1,-1]:
			bkgSamples = ['tt', 'wbbjets', 'wccjets', 'wcjets', 'wljets', 'singletop', 'zjets', 'vv']
			plotStack("stack_%s_q%d.pdf" % (ch, q), inp, ch, bkgSamples, q)

	toSubtract = ['singletop']
	#toSubtract = ['singletop', 'tt', 'vv', 'zjets']
	for ch in channels:
		inp[ch]['datasub'] = {}
		inp[ch]['wjets'] = {}
		for njets in range(1, 6):
			inp[ch]['datasub'][njets] = {}
			inp[ch]['datasub'][njets][1] = inp[ch]['data'][njets][1]
			inp[ch]['datasub'][njets][-1] = inp[ch]['data'][njets][-1]
			inp[ch]['datasub'][njets][0] = inp[ch]['data'][njets][0]
			for s in toSubtract:
				inp[ch]['datasub'][njets][0] -= inp[ch][s][njets][0]
				inp[ch]['datasub'][njets][1] -= inp[ch][s][njets][1]
				inp[ch]['datasub'][njets][-1] -= inp[ch][s][njets][-1]
			inp[ch]['wjets'][njets] = {}
			inp[ch]['wjets'][njets][1] = inp[ch]['wbbjets'][njets][1]
			inp[ch]['wjets'][njets][-1] = inp[ch]['wbbjets'][njets][-1]
			inp[ch]['wjets'][njets][0] = inp[ch]['wbbjets'][njets][0]
			for s in ['wccjets', 'wcjets', 'wljets']:
				inp[ch]['wjets'][njets][0] += inp[ch][s][njets][0]
				inp[ch]['wjets'][njets][1] += inp[ch][s][njets][1]
				inp[ch]['wjets'][njets][-1] += inp[ch][s][njets][-1]
		plotConfig(ch+"_datasub_q0.pdf", inp, ch, "datasub", 0)
		plotConfig(ch+"_datasub_q1.pdf", inp, ch, "datasub", 1)
		plotConfig(ch+"_datasub_q-1.pdf", inp, ch, "datasub", -1)
		plotConfig(ch+"_wjets_q0.pdf", inp, ch, "wjets", 0)
		plotConfig(ch+"_wjets_q1.pdf", inp, ch, "wjets", 1)
		plotConfig(ch+"_wjets_q-1.pdf", inp, ch, "wjets", -1)

	kcc = {'el':unc.ufloat(0,0), 'mu':unc.ufloat(0,0)}
	kcc['el'] = inp['Wpre_resjets_el']['wccjets'][2][0]/inp['Wpre_resjets_el']['wbbjets'][2][0]
	kcc['mu'] = inp['Wpre_resjets_mu']['wccjets'][2][0]/inp['Wpre_resjets_mu']['wbbjets'][2][0]

	rmc = {'el':unc.ufloat(0,0), 'mu':unc.ufloat(0,0)}
	rmcp1 = {'el':unc.ufloat(0,0), 'mu':unc.ufloat(0,0)}
	rmcm1 = {'el':unc.ufloat(0,0), 'mu':unc.ufloat(0,0)}
	rmc_rat = {'el':unc.ufloat(0,0), 'mu':unc.ufloat(0,0)}
	ca_data = {'el':unc.ufloat(0,0), 'mu':unc.ufloat(0,0)}
	ca_mc = {'el':unc.ufloat(0,0), 'mu':unc.ufloat(0,0)}
	N_mc = {'el':unc.ufloat(0,0), 'mu':unc.ufloat(0,0)}
	N_data = {'el':unc.ufloat(0,0), 'mu':unc.ufloat(0,0)}
	f_ca = {'el':unc.ufloat(0,0), 'mu':unc.ufloat(0,0)}

	pbb = {}
	pcc = {}
	pc = {}
	pl = {}

	pbbp = {}
	pccp = {}
	pcp = {}
	plp = {}

	sfbb = {}
	sfcc = {}
	sfc = {}
	sfl = {}

	fbb_data = {'el':unc.ufloat(0,0), 'mu':unc.ufloat(0,0)}
	fbb_mc = {'el':unc.ufloat(0,0), 'mu':unc.ufloat(0,0)}
	fc_data = {'el':unc.ufloat(0,0), 'mu':unc.ufloat(0,0)}
	fc_mc = {'el':unc.ufloat(0,0), 'mu':unc.ufloat(0,0)}
	fl_data = {'el':unc.ufloat(0,0), 'mu':unc.ufloat(0,0)}
	fl_mc = {'el':unc.ufloat(0,0), 'mu':unc.ufloat(0,0)}

	nj = 2
	for lep in ['el', 'mu']:
		pbb[lep] = inp['Wtag_resjets_el']['wbbjets'][nj][0]/inp['Wpre_resjets_el']['wbbjets'][nj][0]
		pcc[lep] = inp['Wtag_resjets_el']['wccjets'][nj][0]/inp['Wpre_resjets_el']['wccjets'][nj][0]
		pc[lep] = inp['Wtag_resjets_el']['wcjets'][nj][0]/inp['Wpre_resjets_el']['wcjets'][nj][0]
		pl[lep] = inp['Wtag_resjets_el']['wljets'][nj][0]/inp['Wpre_resjets_el']['wljets'][nj][0]

		pbbp[lep] = inp['Wtag2_resjets_el']['wbbjets'][nj][0]/inp['Wtag_resjets_el']['wbbjets'][nj][0]
		pccp[lep] = inp['Wtag2_resjets_el']['wccjets'][nj][0]/inp['Wtag_resjets_el']['wccjets'][nj][0]
		pcp[lep] = inp['Wtag2_resjets_el']['wcjets'][nj][0]/inp['Wtag_resjets_el']['wcjets'][nj][0]
		plp[lep] = inp['Wtag2_resjets_el']['wljets'][nj][0]/inp['Wtag_resjets_el']['wljets'][nj][0]

		N0p_data = inp['Wpre_resjets_%s' % lep]['datasub'][nj][1]
		N0n_data = inp['Wpre_resjets_%s' % lep]['datasub'][nj][-1]
		N1p_data = inp['Wtag_resjets_%s' % lep]['datasub'][nj][1]
		N1n_data = inp['Wtag_resjets_%s' % lep]['datasub'][nj][-1]
		N2p_data = inp['Wtag2_resjets_%s' % lep]['datasub'][nj][1]
		N2n_data = inp['Wtag2_resjets_%s' % lep]['datasub'][nj][-1]
		N0p_mc = inp['Wpre_resjets_%s' % lep]['wjets'][nj][1]
		N0n_mc = inp['Wpre_resjets_%s' % lep]['wjets'][nj][-1]
		N1p_mc = inp['Wtag_resjets_%s' % lep]['wjets'][nj][1]
		N1n_mc = inp['Wtag_resjets_%s' % lep]['wjets'][nj][-1]
		N2p_mc = inp['Wtag2_resjets_%s' % lep]['wjets'][nj][1]
		N2n_mc = inp['Wtag2_resjets_%s' % lep]['wjets'][nj][-1]
		print "Lepton %s" % lep
		print "%10s %10s %10s %10s %10s" % ("data/mc", "N0p", "N0n", "N1p", "N1n", "N2p", "N2n")
		print "%10s %10f %10f %10f %10f" % ("mc", N0p_mc, N0n_mc, N1p_mc, N1n_mc, N2p_mc, N2n_mc)
		print "%10s %10f %10f %10f %10f" % ("data", N0p_data, N0n_data, N1p_data, N1n_data, N2p_data, N2n_data)

		# Charge asymmetry
		rmc[lep] = N0p_mc/N0n_mc
		rmcp1[lep] = N0p_mc+N0n_mc
		rmcm1[lep] = N0p_mc-N0n_mc
		rmc_rat[lep] = rmcp1[lep]/rmcm1[lep]

		ca_data[lep] = N0p_data - N0n_data
		ca_mc[lep] = N0p_mc - N0n_mc

		N_data[lep] = inp['Wpre_resjets_%s' % lep]['datasub'][nj][0]
		N_mc[lep] = inp['Wpre_resjets_%s' % lep]['wjets'][nj][0]

		f_ca[lep] = rmc_rat[lep]*ca_data[lep]/N_mc[lep]

		# Now the HF SFs

		A = unp.matrix([[pbb[lep] + kcc[lep]*pc[lep], pc[lep], pl[lep]],
						[pbbp[lep]+kcc[lep]*pcp[lep], pc[lep], plp[lep]],
						[unc.ufloat(1,0)+kcc[lep], unc.ufloat(1, 0), unc.ufloat(1, 0)]])
		B_d = unp.matrix([[(N1p_data - N1n_data)/(N0p_data - N0n_data)], [(N2p_data - N2n_data)/(N1p_data + N2n_data)], [unc.ufloat(1,0)]])
		B_m = unp.matrix([[(N1p_mc - N1n_mc)/(N0p_mc - N0n_mc)], [(N2p_mc - N2n_mc)/(N1p_mc + N2n_mc)], [unc.ufloat(1,0)]])
		
		f_d = A.I*B_d
		f_m = A.I*B_m
		fbb_data[lep] = f_d[0]
		fcc_data[lep] = f_d[0]
		fc_data[lep] = f_d[1]
		fl_data[lep] = f_d[2]

		fbb_mc[lep] = f_m[0]
		fcc_mc[lep] = f_m[0]
		fc_mc[lep] = f_m[1]
		fl_mc[lep] = f_m[2]

		sfbb[lep] = fbb_data[lep]/fbb_mc[lep]
		sfcc[lep] = fcc_data[lep]/fcc_mc[lep]
		sfc[lep] = fc_data[lep]/fc_mc[lep]
		sfl[lep] = fl_data[lep]/fl_mc[lep]

		#norm_change = Frac_bb[lep]['2p']*sfbb[lep] + Frac_cc[lep]['2p']*sfcc[lep] + Frac_c[lep]['2p']*sfc[lep] + Frac_l[lep]['2p']*sfl[lep]
		#wbb[lep]['2p'] = sfbb[lep]/norm_change
		#wcc[lep]['2p'] = sfcc[lep]/norm_change
		#wc[lep]['2p'] = sfc[lep]/norm_change
		#wl[lep]['2p'] = sfl[lep]/norm_change

	print "\\begin{tabular}{|c|c|}"
	print "\\hline"
	print "\\multicolumn{2}{|c|}{Using information from $n_{jets}=%d$} \\\\" % nj
	print "\\hline"
	print "%10s & %10s \\\\" % ('Variable', 'Channel')
	print "\\hline"
	for lep in ['el', 'mu']:
		print "\\hline"
		print "\\multicolumn{2}{|c|}{%s lepton} \\\\" % lep
		print "\\hline"
		for var in ["pbb", "pcc", "pc", "pl", "pbbp", "pccp", "pcp", "plp", "rmc", "rmc_rat", "kcc", "fbb_data", "fbb_mc", "fcc_data", "fcc_mc", "fc_data", "fc_mc", "fl_data", "fl_mc", "ca_data", "ca_mc", "N_mc", "N_data", "f_ca", "sfbb", "sfcc", "sfc", "sfl"]:
			g = eval(var)
			print "%20s   &   $%10.3f$" % (var, g[lep])
	print "\\hline"
	print "\\end{tabular}"

main()

