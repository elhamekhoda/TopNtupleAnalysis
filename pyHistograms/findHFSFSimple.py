#!/usr/bin/env python

import ROOT

odir = 'hists_WjetsHF'
files = {}
channels = ['Wpre_resjets_el', 'Wpre_resjets_mu', 'Wtag_resjets_el', 'Wtag_resjets_mu']
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
	h = ROOT.TH1F(name, "", 4, 0.5, 4.5)
	for njets in range(2,5):
		h.SetBinContent(njets, inp[ch][sample][njets][q][0])
		h.SetBinError(njets, inp[ch][sample][njets][q][1])
	h.SetDirectory(0)
	return h


def plotConfig(name, inp, ch, sample, q):
	h = toHist("tmp", inp, ch, sample, q)
	ROOT.gStyle.SetOptStat(0)
	ROOT.gStyle.SetPadTickX(1)
	ROOT.gStyle.SetPadTickY(1)

	c = ROOT.TCanvas("c", "", 800, 600);

	#h.GetYaxis().SetRangeUser(0, 3000);
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
	l = ROOT.TLegend(0.5,0.45,0.87,0.89)
	l.SetBorderSize(0)
	st = ROOT.THStack("stack", "")
	count = len(samples)-1
	col = [0, kGreen, kCyan, kRed, 62, 95, 5]
	for s in reverded(samples):
		h = toHist("%s_%s_%d" % (ch, s, q), inp, ch, s, q)
		h.SetFillColor(col[count])
		h.SetLineColor(1)
		h.SetLineWidth(2)
		st.Add(h)
		l.AddEntry(h, s, "F")
		count -= 1

	hdata = toHist("%s_%s_%d" % (ch, "data", q), inp, ch, "data", q)
	l.AddEntry(hdata, "data", "L")
	st.Draw();
	m = hdata.GetBinContent(1)*1.2
	st.GetYaxis().SetRangeUser(0, m);
	st.GetYaxis().SetTitle("Events");
	st.GetXaxis().SetTitle("Number of jets");
	st.GetXaxis().SetTitleOffset(0.9);
	st.GetXaxis().SetLabelSize(0.05);
	st.GetXaxis().SetTitleSize(0.05);
	st.Draw("hist")
	hdata.SetMarkerStyle(21)
	hdata.SetMarkerSize(1.2)
	hdata.SetLineWidth(2)
	hdata.SetLineColor(1)
	hdata.Draw("e1 same")
	l.Draw()
	c.SaveAs(name)

def ratio(a, b):
	c = [0,0]
	c[0] = a[0]/b[0]
	c[1] = c[0]*ROOT.TMath.Sqrt(a[1]**2/a[0]**2 + b[1]**2/b[0]**2)
	return c

def ratioPlusMinus(a, b):
	c = [0,0]
	c[0] = (a[0] + b[0])/(a[0] - b[0])
	# error^2 is (-(2 b)/(a-b)^2)^2 da^2 + ((2 a)/(a-b)^2)^2 db^2
	c[1] = ROOT.TMath.Sqrt((2*b[0]/(a[0]-b[0])**2)**2*a[1]**2 + (2*a[0]/(a[0]-b[0])**2)**2*b[1]**2)
	return c

def ratioBin(a, b):
	c = [0,0]
	c[0] = a[0]/b[0]
	#c[1] = c[0]*ROOT.TMath.Sqrt(a[1]**2/a[0]**2 + b[1]**2/b[0]**2)
	if a[0] < b[0]:
		c[1] = ROOT.TMath.Abs(((1 - 2*a[0]**2/b[0]**2)*a[1]**2 + a[0]**2*b[1]**2/b[0]**2) / b[0]**2)
	else:
		c[1] = 0
	return c

def add(a, b):
	c = [0,0]
	c[0] = a[0]+b[0]
	c[1] = ROOT.TMath.Sqrt(a[1]**2 + b[1]**2)
	return c

def diff(a, b):
	c = [0,0]
	c[0] = a[0]-b[0]
	c[1] = ROOT.TMath.Sqrt(a[1]**2 + b[1]**2)
	return c

def mult(a, b):
	c = [0,0]
	c[0] = a[0]*b[0]
	c[1] = ROOT.TMath.Sqrt(b[0]**2*a[1]**2 + a[0]**2*b[1]**2)
	return c

def scale(a, k):
	c = [0,0]
	c[0] = a[0]*k
	c[1] = a[1]*k
	return c

def main():
	# in[##channel][sample][njet][charge]
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
			for njets in range(2,5):
				inp[ch][s][njets] = {}
				inp[ch][s][njets][1] = [L*histPos.GetBinContent(njets), L*histPos.GetBinError(njets)]
				inp[ch][s][njets][-1] = [L*histNeg.GetBinContent(njets), L*histNeg.GetBinError(njets)]
				inp[ch][s][njets][0] = [L*histAll.GetBinContent(njets), L*histAll.GetBinError(njets)]
	
	for ch in channels:
		for q in [0,1,-1]:
			bkgSamples = ['tt', 'wbbjets', 'wccjets', 'wcjets', 'singletop', 'zjets', 'vv']
			plotStack("stack_%s_q%d.eps" % (ch, q), inp, ch, bkgSamples, q)

	toSubtract = ['singletop']
	#toSubtract = ['singletop', 'tt', 'vv', 'zjets']
	for ch in channels:
		inp[ch]['datasub'] = {}
		inp[ch]['wjets'] = {}
		for njets in range(2, 5):
			inp[ch]['datasub'][njets] = {}
			inp[ch]['datasub'][njets][1] = inp[ch]['data'][njets][1][:]
			inp[ch]['datasub'][njets][-1] = inp[ch]['data'][njets][-1][:]
			inp[ch]['datasub'][njets][0] = inp[ch]['data'][njets][0][:]
			for s in toSubtract:
				inp[ch]['datasub'][njets][0][0] -= inp[ch][s][njets][0][0]
				inp[ch]['datasub'][njets][1][0] -= inp[ch][s][njets][1][0]
				inp[ch]['datasub'][njets][-1][0] -= inp[ch][s][njets][-1][0]
				inp[ch]['datasub'][njets][0][1] = ROOT.TMath.Sqrt(inp[ch]['datasub'][njets][0][1]**2 + inp[ch][s][njets][0][1]**2)
				inp[ch]['datasub'][njets][1][1] = ROOT.TMath.Sqrt(inp[ch]['datasub'][njets][1][1]**2 + inp[ch][s][njets][1][1]**2)
				inp[ch]['datasub'][njets][-1][1] = ROOT.TMath.Sqrt(inp[ch]['datasub'][njets][-1][1]**2 + inp[ch][s][njets][-1][1]**2)
			inp[ch]['wjets'][njets] = {}
			inp[ch]['wjets'][njets][1] = inp[ch]['wbbjets'][njets][1][:]
			inp[ch]['wjets'][njets][-1] = inp[ch]['wbbjets'][njets][-1][:]
			inp[ch]['wjets'][njets][0] = inp[ch]['wbbjets'][njets][0][:]
			for s in ['wccjets', 'wcjets', 'wljets']:
				inp[ch]['wjets'][njets][0][0] += inp[ch][s][njets][0][0]
				inp[ch]['wjets'][njets][1][0] += inp[ch][s][njets][1][0]
				inp[ch]['wjets'][njets][-1][0] += inp[ch][s][njets][-1][0]
				inp[ch]['wjets'][njets][0][1] = ROOT.TMath.Sqrt(inp[ch]['wjets'][njets][0][1]**2 + inp[ch][s][njets][0][1]**2)
				inp[ch]['wjets'][njets][1][1] = ROOT.TMath.Sqrt(inp[ch]['wjets'][njets][1][1]**2 + inp[ch][s][njets][1][1]**2)
				inp[ch]['wjets'][njets][-1][1] = ROOT.TMath.Sqrt(inp[ch]['wjets'][njets][-1][1]**2 + inp[ch][s][njets][-1][1]**2)
		plotConfig(ch+"_datasub_q0.eps", inp, ch, "datasub", 0)
		plotConfig(ch+"_datasub_q1.eps", inp, ch, "datasub", 1)
		plotConfig(ch+"_datasub_q-1.eps", inp, ch, "datasub", -1)
		plotConfig(ch+"_wjets_q0.eps", inp, ch, "wjets", 0)
		plotConfig(ch+"_wjets_q1.eps", inp, ch, "wjets", 1)
		plotConfig(ch+"_wjets_q-1.eps", inp, ch, "wjets", -1)

	kcc = {'el':[0,0], 'mu':[0,0]}
	kc = {'el':[0,0], 'mu':[0,0]}
	kcc['el'] = ratio(inp['Wpre_resjets_el']['wccjets'][2][0], inp['Wpre_resjets_el']['wbbjets'][2][0])
	kcc['mu'] = ratio(inp['Wpre_resjets_mu']['wccjets'][2][0], inp['Wpre_resjets_mu']['wbbjets'][2][0])
	kc['el'] = ratio(inp['Wpre_resjets_el']['wcjets'][2][0],inp['Wpre_resjets_el']['wbbjets'][2][0])
	kc['mu'] = ratio(inp['Wpre_resjets_mu']['wcjets'][2][0],inp['Wpre_resjets_mu']['wbbjets'][2][0])
	#effb = 0.7
	#effc = 1.0/7.09
	#effl = 1.0/119.69
	#pbb = effb**2 + 2*effb*(1-effb)
	#pcc = effc**2 + 2*effc*(1-effc)
	#pc = effc*effl + effl*(1-effc) + effc*(1-effl)
	#pl = effl**2 + 2*effl*(1-effl)

	sfbb = {}
	sfcc = {}
	sfc = {}
	sfl = {}

	pbb = {}
	pcc = {}
	pc = {}
	pl = {}

	fbb_data = {'el':[0,0], 'mu':[0,0]}
	fbb_mc = {'el':[0,0], 'mu':[0,0]}
	fl_data = {'el':[0,0], 'mu':[0,0]}
	fl_mc = {'el':[0,0], 'mu':[0,0]}

	rmc = {'el':[0,0], 'mu':[0,0]}
	rmcp1 = {'el':[0,0], 'mu':[0,0]}
	rmcm1 = {'el':[0,0], 'mu':[0,0]}
	rmc_rat = {'el':[0,0], 'mu':[0,0]}
	ca_data = {'el':[0,0], 'mu':[0,0]}
	ca_mc = {'el':[0,0], 'mu':[0,0]}
	N_mc = {'el':[0,0], 'mu':[0,0]}
	N_data = {'el':[0,0], 'mu':[0,0]}

	f_ca = {'el':[0,0], 'mu':[0,0]}

	nj = 2
	for lep in ['el', 'mu']:
		pbb[lep] = ratioBin(inp['Wtag_resjets_el']['wbbjets'][nj][0], inp['Wpre_resjets_el']['wbbjets'][nj][0])
		pcc[lep] = ratioBin(inp['Wtag_resjets_el']['wccjets'][nj][0], inp['Wpre_resjets_el']['wccjets'][nj][0])
		pc[lep] = ratioBin(inp['Wtag_resjets_el']['wcjets'][nj][0], inp['Wpre_resjets_el']['wcjets'][nj][0])
		pl[lep] = ratioBin(inp['Wtag_resjets_el']['wljets'][nj][0], inp['Wpre_resjets_el']['wljets'][nj][0])

		Npp_data = inp['Wpre_resjets_%s' % lep]['datasub'][nj][1]
		Npn_data = inp['Wpre_resjets_%s' % lep]['datasub'][nj][-1]
		Ntp_data = inp['Wtag_resjets_%s' % lep]['datasub'][nj][1]
		Ntn_data = inp['Wtag_resjets_%s' % lep]['datasub'][nj][-1]
		Npp_mc = inp['Wpre_resjets_%s' % lep]['wjets'][nj][1]
		Npn_mc = inp['Wpre_resjets_%s' % lep]['wjets'][nj][-1]
		Ntp_mc = inp['Wtag_resjets_%s' % lep]['wjets'][nj][1]
		Ntn_mc = inp['Wtag_resjets_%s' % lep]['wjets'][nj][-1]
		print "Lepton %s" % lep
		print "%10s %10s %10s %10s %10s" % ("data/mc", "Npp", "Npn", "Ntp", "Ntn")
		print "%10s %10d %10d %10d %10d" % ("mc", Npp_mc[0], Npn_mc[0], Ntp_mc[0], Ntn_mc[0])
		print "%10s %10d %10d %10d %10d" % ("data", Npp_data[0], Npn_data[0], Ntp_data[0], Ntn_data[0])

		# Charge asymmetry
		rmc[lep] = ratio(Npp_mc, Npn_mc)
		#rmcp1[lep] = add(rmc[lep], [1, 0])
		#rmcm1[lep] = diff(rmc[lep], [1, 0])
		rmcp1[lep] = add(Npp_mc, Npn_mc)
		rmcm1[lep] = diff(Npp_mc, Npn_mc)
		rmc_rat[lep] = ratioPlusMinus(Npp_mc, Npn_mc)

		ca_data[lep] = diff(Npp_data, Npn_data)
		ca_mc[lep] = diff(Npp_mc, Npn_mc)

		N_data[lep] = add(Npp_data, Npn_data)
		N_mc[lep] = add(Npp_mc, Npn_mc)

		f_ca[lep] = ratio(mult(rmc_rat[lep], ca_data[lep]), N_mc[lep])

		# Now the HF SFs

		den = diff(pbb[lep], pl[lep])
		den = add(den, mult(kcc[lep], diff(pcc[lep],pl[lep])))
		den = add(den, mult(kc[lep], diff(pc[lep],pl[lep])))

		data_num = ratioBin(diff(Ntp_data, Ntn_data), diff(Npp_data, Npn_data))
		data_num = diff(data_num, pl[lep])
		fbb_data[lep] = ratio(data_num, den)

		fbb_mc[lep] = ratioBin(inp['Wpre_resjets_%s' % lep]['wbbjets'][nj][0], inp['Wpre_resjets_%s' % lep]['wjets'][nj][0])

		sfbb[lep] = ratio(fbb_data[lep], fbb_mc[lep])
		sfcc[lep] = ratio(fbb_data[lep], fbb_mc[lep])
		sfc[lep] = ratio(fbb_data[lep], fbb_mc[lep])

		fl_data[lep] = diff([1,0], mult(add(add([1,0], kcc[lep]), kc[lep]), fbb_data[lep]))
		fl_mc[lep] = diff([1,0], mult(add(add([1,0], kcc[lep]), kc[lep]), fbb_mc[lep]))
		sfl[lep] = ratio(fl_data[lep], fl_mc[lep])

		#fbb_data[lep] = ((Ntp_data - Ntn_data)/(Npp_data - Npn_data) - pl)*1.0/(pbb + kcc[lep]*(pcc-pl) + kc[lep]*(pc-pl) - pl)
		#fbb_mc[lep] = ((Ntp_mc - Ntn_mc)/(Npp_mc - Npn_mc) - pl)*1.0/(pbb + kcc[lep]*(pcc-pl) + kc[lep]*(pc-pl) - pl)
	print "\\begin{tabular}{|c|c|}"
	print "\\hline"
	print "\\multicolumn{2}{|c|}{Using information from $n_{jets}=%d$} \\\\" % nj
	print "\\hline"
	print "%10s & %10s \\\\" % ('Variable', 'Channel')
	print "\\hline"
	for var in []:
		g = eval(var)
		print "%10s   &   %5f " % (var, g[0], g[1])
	for lep in ['el', 'mu']:
		print "\\hline"
		print "\\multicolumn{2}{|c|}{%s lepton} \\\\" % lep
		print "\\hline"
		for var in ["pbb", "pcc", "pc", "pl", "rmc", "rmc_rat", "kcc", "kc", "fbb_data", "fbb_mc", "ca_data", "ca_mc", "N_mc", "N_data", "f_ca", "sfbb", "sfcc", "sfc", "sfl"]:
			g = eval(var)
			print "%20s   &   $%10.3f \\pm %10.3f$" % (var+" ("+lep+")", g[lep][0], g[lep][1])
	print "\\hline"
	print "\\end{tabular}"
	
main()

