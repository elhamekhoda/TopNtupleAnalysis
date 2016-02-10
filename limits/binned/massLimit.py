
from inputs import *

from ROOT import *

gStyle.SetOptStat(0)

clim = TCanvas("clim", "", 800, 600);
l = TLegend(0.5,0.5,0.89,0.89)
l.SetBorderSize(0)

h = TH1F("h", "", 50, 0, 5.0);
h.GetYaxis().SetRangeUser(1e-2, 60);
h.GetYaxis().SetTitle("95% CL upper limit on #sigma #times BR [pb]");
h.GetXaxis().SetTitle("m_{Z'} [TeV]");
h.Draw("hist");
xsec = TGraph(len(xs));
nom = TGraph(len(xs));
obs = TGraph(len(xs));
sigma1 = TGraphAsymmErrors(len(xs));
sigma2 = TGraphAsymmErrors(len(xs));
for i in range(0, len(xs)):
  f = TFile("JobTtres_"+signalList[i]+"/Limits/JobTtres_"+signalList[i]+".root")
  hi = f.Get("limit")
  muobs = hi.GetBinContent(1)
  muexp = hi.GetBinContent(2)
  muexp_p2 = abs(-muexp + hi.GetBinContent(3))
  muexp_p1 = abs(-muexp + hi.GetBinContent(4))
  muexp_m1 = abs(-muexp + hi.GetBinContent(5))
  muexp_m2 = abs(-muexp + hi.GetBinContent(6))
  ftxt = open('lim_'+signalList[i]+'.txt', 'w')
  ftxt.write('muobs     '+str(muobs)+'\n')
  ftxt.write('muexp     '+str(muexp)+'\n')
  ftxt.write('muexp_p2  '+str(muexp_p2)+'\n')
  ftxt.write('muexp_p1  '+str(muexp_p1)+'\n')
  ftxt.write('muexp_m1  '+str(muexp_m1)+'\n')
  ftxt.write('muexp_m2  '+str(muexp_m2)+'\n')
  ftxt.write('xsec      '+str(xs[i])+'\n')
  ftxt.close()

  sigma1.SetPoint(i, mass[i], muexp*xs[i])
  sigma1.SetPointError(i, 0, 0, muexp_m1*xs[i], muexp_p1*xs[i])
  sigma2.SetPoint(i, mass[i], muexp*xs[i])
  sigma2.SetPointError(i, 0, 0, muexp_m2*xs[i], muexp_p2*xs[i])
  xsec.SetPoint(i, mass[i], xs[i])
  nom.SetPoint(i, mass[i], muexp*xs[i])
  obs.SetPoint(i, mass[i], muobs*xs[i])
nom.SetLineWidth(2);
nom.SetLineStyle(kDashed);
obs.SetLineWidth(2);
nom.SetMarkerStyle(20);
obs.SetMarkerStyle(20);
nom.SetMarkerSize(1.0);
obs.SetMarkerSize(1.0);
obs.SetMarkerColor(kRed);
xsec.SetLineWidth(3);
xsec.SetLineColor(kRed);
sigma2.SetFillStyle(1001);
sigma2.SetFillColor(5);
sigma2.SetLineColor(5);
sigma2.SetMarkerColor(5);
sigma1.SetFillStyle(1001);
sigma1.SetFillColor(3);
sigma1.SetMarkerColor(3);

l.AddEntry(nom, "Expected", "L")
l.AddEntry(obs, "Observed", "LP")
l.AddEntry(sigma1, "#pm 1 #sigma", "F")
l.AddEntry(sigma2, "#pm 2 #sigma", "F")
l.AddEntry(xsec, "LO Z prime TC2 cross section #times 1.3", "L")

sigma2.Draw("3");
sigma1.Draw("3");
nom.Draw("L")
obs.Draw("LP")
xsec.Draw("L")
l.Draw()
clim.SetLogy(1)

def stampATLAS(text, x, y):
  t = TLatex()
  t.SetNDC()
  t.SetTextFont(72)
  t.SetTextColor(1)
  delx = 0.115*696*gPad.GetWh()/(472*gPad.GetWw()) + 0.05
  t.SetTextSize(0.06)
  t.DrawLatex(x,y,"ATLAS")
  t.SetTextFont(42)
  t.SetTextSize(0.06)
  t.DrawLatex(x+delx, y, text)

def stampLumiText(lumi, x, y, text, size):
  t = TLatex()
  t.SetNDC()
  t.SetTextFont(42)
  t.SetTextColor(1)
  t.SetTextSize(size)
  t.DrawLatex(x,y,"#int L dt = "+str(lumi)+" fb^{-1}, "+text)

stampATLAS("Internal", 0.15, 0.80)
stampLumiText(3.3, 0.15, 0.70, "#sqrt{s} = 13 TeV", 0.03)

clim.SaveAs("mass_limit.eps")

  
