
from ttres_config.inputs import *

from ROOT import *

gStyle.SetOptStat(0)

clim = TCanvas("clim", "", 800, 600);
l = TLegend(0.5,0.5,0.89,0.89)
l.SetBorderSize(0)

h = TH1F("h", "", 40, 0, 4.0);
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
  f = TFile("FitTtres_"+signalList[i]+"/Limits/FitTtres_"+signalList[i]+".root")
  hi = f.Get("limit")
  muobs = hi.GetBinContent(1)
  muexp = hi.GetBinContent(2)
  muexp_p2 = abs(-muexp + hi.GetBinContent(3))
  muexp_p1 = abs(-muexp + hi.GetBinContent(4))
  muexp_m1 = abs(-muexp + hi.GetBinContent(5))
  muexp_m2 = abs(-muexp + hi.GetBinContent(6))

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

t = TLatex()
t.SetNDC()
t.DrawLatex(0.15,0.8, "#int L dt = 10 fb^{-1}")

clim.SaveAs("ttres_config/mass_limit.eps")

  
