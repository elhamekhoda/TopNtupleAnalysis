#include <stdio.h>
#include <execinfo.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>

#include <iostream>
#include <sstream>

#include "SampleSet.h"
#include "SystematicCalculation.h"

#include "utils.h"

#include "TLine.h"
#include "TCanvas.h"
#include "TH1D.h"
#include "TGraphAsymmErrors.h"
#include "THStack.h"
#include "TLegend.h"
#include "TLatex.h"
#include "TROOT.h"

#include <memory>

int _stamp = 0;

using namespace std;

shared_ptr<TGraphAsymmErrors> normaliseBand(shared_ptr<TGraphAsymmErrors> band, TH1D *MC_sum) {
  shared_ptr<TGraphAsymmErrors> rat((TGraphAsymmErrors *) band->Clone("ratio_band"));
  for (int k = 1; k < MC_sum->GetNbinsX()+1; ++k) {
    double mx, my;
    band->GetPoint(k-1, mx, my);
    if (MC_sum->GetBinContent(k) != 0) {
      rat->SetPoint(k-1, MC_sum->GetBinCenter(k), my/MC_sum->GetBinContent(k));
      rat->SetPointEXhigh(k-1, band->GetErrorXhigh(k-1));
      rat->SetPointEXlow(k-1, band->GetErrorXlow(k-1));
      rat->SetPointEYhigh(k-1, band->GetErrorYhigh(k-1)/MC_sum->GetBinContent(k));
      double ll = band->GetErrorYlow(k-1)/MC_sum->GetBinContent(k);
      if (ll > 1) ll = 1;
      rat->SetPointEYlow(k-1, ll);
    } else {
      rat->SetPoint(k-1, MC_sum->GetBinCenter(k), 1);
      rat->SetPointEXhigh(k-1, band->GetErrorXhigh(k-1));
      rat->SetPointEXlow(k-1, band->GetErrorXlow(k-1));
      rat->SetPointEYhigh(k-1, 0);
      rat->SetPointEYlow(k-1, 0);
    }
  }

  return rat;
}

shared_ptr<TGraphErrors> TH1toGraph(TH1D *Data) {
  shared_ptr<TGraphErrors> rat(new TGraphErrors(Data->GetNbinsX()));
  for (int k = 1; k < Data->GetNbinsX()+1; ++k) {
    double mx, my;
    rat->SetPoint(k-1, Data->GetBinCenter(k), Data->GetBinContent(k));
    rat->SetPointError(k-1, Data->GetBinWidth(k)*0.5,  Data->GetBinError(k));
    //rat->SetPointEXhigh(k-1, Data->GetBinWidth(k)*0.5);
    //rat->SetPointEXlow(k-1, Data->GetBinWidth(k)*0.5);
    //rat->SetPointEYhigh(k-1, Data->GetBinError(k));
    //rat->SetPointEYlow(k-1, Data->GetBinError(k));
  }
  rat->SetMarkerStyle(Data->GetMarkerStyle());
  rat->SetMarkerSize(Data->GetMarkerSize());
  rat->SetMarkerColor(Data->GetMarkerColor());
  rat->SetLineStyle(Data->GetLineStyle());
  rat->SetLineColor(Data->GetLineColor());
  rat->SetLineWidth(Data->GetLineWidth());

  return rat;
}

void addSystToStat(shared_ptr<TH1D> Data, shared_ptr<TGraphAsymmErrors> band) {
  for (int k = 1; k < Data->GetNbinsX()+1; ++k) {
    double mx, my;
    band->GetPoint(k-1, mx, my);
    double emy = band->GetErrorYlow(k-1);
    double sy = Data->GetBinError(k);
    double ty = sqrt(sy*sy + emy*emy);
    Data->SetBinError(k, ty);
  }
}

shared_ptr<TH1D> normaliseBandLine(shared_ptr<TH1D> band, TH1D *MC_sum) {
  shared_ptr<TH1D> rat((TH1D *) band->Clone(Form("ratio_band%s", band->GetName())));
  rat->Divide(band.get(), MC_sum);
  for (int k = 1; k < MC_sum->GetNbinsX()+1; ++k) {
    if (MC_sum->GetBinContent(k) == 0) rat->SetBinContent(k, 1);
  }
  return rat;
}

void drawCompare(SampleSetConfiguration &stackConfig, const vector<std::string> &extraText, const std::string &outfile, bool ratio, double lumi) {
  TStyle *atlasStyle = AtlasStyle();
  gROOT->SetStyle("ATLAS");
  gROOT->ForceStyle();

  shared_ptr<TCanvas> c(new TCanvas("c", "", 800, 600));

  // do ratio?
  TPad *pad_ratio = 0;
  if (ratio) {
    c->Divide(1, 2, 0.015, 0.01);
    pad_ratio = (TPad *) c->cd(2);
    pad_ratio->SetPad(0,0,1,0.30);
    pad_ratio->SetTopMargin(0.01);
    pad_ratio->SetBottomMargin(0.45);
    c->cd(1)->SetPad(0,0.2,1,1);
    c->cd(1)->SetBottomMargin(0.13);
  }

  c->cd(1);

  // make legend
  shared_ptr<TLegend> leg(new TLegend(0.55, 0.6, 0.85, 0.92));
  //if (stackConfig._stack.size() > 2)
  //  leg->SetNColumns(2);
  leg->SetFillStyle(0);
  leg->SetBorderSize(0);

  // make MC stack and add entries in legend
  vector<shared_ptr<TH1D> > hists;
  string name_first = "";
  double maximum = 0;
  for (map<string, SampleSet>::iterator i = stackConfig._stack.begin(); i != stackConfig._stack.end(); ++i) {
    hists.push_back(i->second.makeTH1(i->first.c_str()));
    hists.back()->SetStats(0);
    leg->AddEntry(hists.back().get(), i->second._item[0].name_plot.c_str(), i->second._item[0].legendstyle.c_str());
    if (i == stackConfig._stack.begin()) {
      name_first = i->second._item[0].name_plot.c_str();
    }
    maximum = std::max(hists.back()->GetBinContent(hists.back()->GetMaximumBin()), maximum);
  }

  for (size_t z = 0; z < hists.size(); ++z) {
    hists[z]->SetMaximum(1.7*maximum);
  }

  hists[0]->Draw("e");
  for (size_t z = 1; z < hists.size(); ++z) {
    hists[z]->Draw("e same");
  }
  
  leg->Draw();

  vector<shared_ptr<TH1D> > rat;
  shared_ptr<TLine> lin;
  if (ratio && hists.size() > 0) {
    for (int k = 1; k < hists.size(); ++k) {
      rat.push_back(shared_ptr<TH1D>());
      rat[k-1].reset((TH1D *) hists[k]->Clone(Form("ratio%d", k)));
      rat[k-1]->Divide(hists[k].get(), hists[0].get(), 1, 1, "B");
      rat[k-1]->SetStats(0);
      rat[k-1]->GetYaxis()->SetRangeUser(0.3, 1.7);
      rat[k-1]->SetTitle("");
      //rat[k-1]->GetYaxis()->SetTitle(Form("H/%s", name_first.c_str()));
      rat[k-1]->GetYaxis()->SetTitle("#frac{Sample}{Black}");
      rat[k-1]->GetYaxis()->SetNdivisions(3, 0, 5);
      rat[k-1]->GetXaxis()->SetLabelFont(42);
      rat[k-1]->GetXaxis()->SetTitleFont(42);
      rat[k-1]->GetYaxis()->SetLabelFont(42);
      rat[k-1]->GetYaxis()->SetTitleFont(42);
      rat[k-1]->GetYaxis()->SetLabelSize(0.18);
      rat[k-1]->GetYaxis()->SetTitleOffset(0.40);
      rat[k-1]->GetYaxis()->SetLabelOffset(0.02);
      rat[k-1]->GetYaxis()->SetTitleSize(0.18);
      rat[k-1]->GetXaxis()->SetTitleSize(0.2);
      rat[k-1]->GetXaxis()->SetLabelSize(0.18);
      rat[k-1]->GetXaxis()->SetTitleSize(0.18);
      rat[k-1]->GetXaxis()->SetTitleOffset(1.1);
      rat[k-1]->SetTitle("");
    }

    c->cd(2);
    rat[0]->Draw("e");
    for (int k = 1; k < rat.size(); ++k) {
      rat[k]->Draw("e same");
    }
    lin.reset(new TLine(rat[0]->GetXaxis()->GetBinLowEdge(1), 1, rat[0]->GetXaxis()->GetBinUpEdge(rat[0]->GetNbinsX()), 1));
    lin->SetLineColor(kBlack);
    lin->SetLineWidth(3);
    lin->SetLineStyle(2);
    lin->Draw();
  }

  // major hack to remove the zero label in the main plot, which is cut in half by the ratio pad
  if (ratio) {
    TPad *pe = new TPad("pe", "pe", 0, 0, 0.99*c->cd(1)->GetLeftMargin(), 0.18);
    pe->SetFillColor(c->cd(1)->GetFillColor());
    pe->SetBorderMode(0);
    //pe->Draw();
  }

  string _stampText = "Internal";
  if (_stamp == 1)
    _stampText = "Preliminary";
  else if (_stamp == 2)
    _stampText = "";
  stampATLAS(_stampText, 0.20, 0.89);
  stampLumi(lumi, 0.20, 0.81);
  for (vector<string>::const_iterator i = extraText.begin(); i != extraText.end(); ++i) {
    double pos = (double) ((int) (i - extraText.begin()));
    stampText(*i, 0.20, 0.74-0.05*pos, 0.06*0.9);
  }

  c->SaveAs(outfile.c_str());
}

void drawDataMC(SampleSetConfiguration &stackConfig, const vector<std::string> &extraText, const std::string &outfile, bool ratio, const std::string &xTitle, const std::string &yTitle, bool mustBeBigger, int posLegend, float yMax, int useArrow, double lumi) {
  TStyle *atlasStyle = AtlasStyle();
  gROOT->SetStyle("ATLAS");
  gROOT->ForceStyle();

  shared_ptr<TCanvas> c(new TCanvas("c", "", 800, 600));

  // do ratio?
  TPad *pad_ratio = 0;
  if (ratio && stackConfig._stack.find("Data") != stackConfig._stack.end()) {
    c->Divide(1, 2, 0.015, 0.01);
    pad_ratio = (TPad *) c->cd(2);
    pad_ratio->SetPad(0,0,1,0.30);
    pad_ratio->SetTopMargin(0.01);
    pad_ratio->SetBottomMargin(0.45);
    c->cd(1)->SetPad(0,0.2,1,1);
    c->cd(1)->SetBottomMargin(0.13);
  }

  c->cd(1);

  // make syst. band
  shared_ptr<TGraphAsymmErrors> band = stackConfig["MC"].makeBand();
  //band->SetFillStyle(3354);
  band->SetFillStyle(1001);
  band->SetFillColorAlpha(kGreen-8, 0.5);

  // make legend
  //shared_ptr<TLegend> leg(new TLegend(0.55, 0.6, 0.85, 0.92));
  shared_ptr<TLegend> leg;
  if (posLegend == 0)
    leg.reset(new TLegend(0.62, 0.5, 0.88, 0.92));
  else if (posLegend == 1)
    leg.reset(new TLegend(0.18, 0.25, 0.45, 0.65));
  else if (posLegend == 2 || posLegend == 5)
    leg.reset(new TLegend(0.62, 0.3, 0.88, 0.72));
  else if (posLegend == 3)
    leg.reset(new TLegend(0.18, 0.32, 0.45, 0.74));
  else if (posLegend == 6)
    leg.reset(new TLegend(0.62, 0.5, 0.88, 0.92));
  else if (posLegend == 7)
    leg.reset(new TLegend(0.62, 0.5, 0.88, 0.92));
  else if (posLegend == 8)
    leg.reset(new TLegend(0.62, 0.3, 0.88, 0.72));
  //leg->SetNColumns(2);
  leg->SetFillStyle(0);
  leg->SetBorderSize(0);

  shared_ptr<TH1D> Data;
  if (stackConfig._stack.find("Data") != stackConfig._stack.end())
    Data = stackConfig["Data"].makeTH1("Data");
  if (Data) {
    Data->SetStats(0);
    leg->AddEntry(Data.get(), "Data", "LP");
  }

  // make MC stack and add entries in legend
  vector<shared_ptr<TH1D> > vechist;
  shared_ptr<THStack> MC = stackConfig["MC"].makeStack("MC", leg, vechist);

  if (band) {
    leg->AddEntry(band.get(), "Syst. uncertainty", "F");
  }

  double maximum = MC->GetMaximum();
  if (Data) maximum = std::max(Data->GetBinContent(Data->GetMaximumBin()), MC->GetMaximum());
  maximum *= 1.8;
  if (yMax > 0)
    maximum = yMax;

  MC->SetMaximum(maximum);
  if (Data) {
    Data->SetMaximum(maximum);
    if (yTitle != "") Data->GetYaxis()->SetTitle(yTitle.c_str());
  }
  MC->SetMinimum(0.001);
  Data->SetMinimum(0.001);

  MC->Draw();
  if (yTitle != "") MC->GetYaxis()->SetTitle(yTitle.c_str());
  if (!ratio) {
    if (xTitle == "")
      MC->GetXaxis()->SetTitle(vechist[0]->GetXaxis()->GetTitle());
    else
      MC->GetXaxis()->SetTitle(xTitle.c_str());
    if (yTitle != "")
      MC->GetYaxis()->SetTitle(yTitle.c_str());
    else
      MC->GetYaxis()->SetTitle(vechist[0]->GetYaxis()->GetTitle());
  }
  c->Update();
  MC->Draw("same");
  band->Draw("2 ][ same");
  if (Data)
    Data->Draw("e same");
  leg->Draw();
  gPad->RedrawAxis();

  shared_ptr<TGraph> arrow;
  shared_ptr<TGraph> arrowdw;
  shared_ptr<TH1D> rat;
  shared_ptr<TGraphAsymmErrors> rat_band;
  shared_ptr<TLine> lin;
  if (ratio && Data) {
    TH1D *MC_sum = (TH1D *) MC->GetStack()->At(MC->GetStack()->LastIndex());
    rat.reset((TH1D *) Data->Clone("ratio"));
    arrow.reset(new TGraph(Data->GetNbinsX()+1));
    arrowdw.reset(new TGraph(Data->GetNbinsX()+1));

    rat->Divide(Data.get(), MC_sum, 1, 1, "B");
    rat_band = normaliseBand(band, MC_sum);

    double theMax = 1.6;
    double theMin = 0.4;
    c->cd(2);
    rat->SetStats(0);
    if (!mustBeBigger) {
      rat->GetYaxis()->SetRangeUser(0.3, 1.7);
      theMax = 1.7;
      theMin = 0.3;
    } else {
      rat->GetYaxis()->SetRangeUser(0.0, 2.3);
      theMax = 2.3;
      theMin = 0.0;
    }
    rat->SetTitle("");
    if (xTitle == "")
      rat->GetXaxis()->SetTitle(MC_sum->GetXaxis()->GetTitle());
    else
      rat->GetXaxis()->SetTitle(xTitle.c_str());
    rat->GetYaxis()->SetTitle("Data/Sim.");
    rat->GetYaxis()->SetNdivisions(3, 0, 5);
    rat->GetXaxis()->SetLabelFont(42);
    rat->GetXaxis()->SetTitleFont(42);
    rat->GetYaxis()->SetLabelFont(42);
    rat->GetYaxis()->SetTitleFont(42);
    rat->GetYaxis()->SetLabelSize(0.18);
    rat->GetYaxis()->SetTitleOffset(0.45);
    rat->GetYaxis()->SetLabelOffset(0.02);
    rat->GetYaxis()->SetTitleSize(0.18);
    rat->GetXaxis()->SetTitleSize(0.2);
    rat->GetXaxis()->SetLabelSize(0.18);
    rat->GetXaxis()->SetTitleSize(0.18);
    rat->GetXaxis()->SetTitleOffset(1.1);
    rat->SetTitle("");

    arrow->SetMarkerSize(2.0);
    arrow->SetMarkerStyle(26);
    arrow->SetMarkerColor(kBlack);
    arrowdw->SetMarkerSize(2.0);
    arrowdw->SetMarkerStyle(32);
    arrowdw->SetMarkerColor(kBlack);
    for (int z = 0; z < rat->GetNbinsX()+1; ++z) {
      //if (rat->GetBinContent(z) > theMax || (rat->GetBinContent(z) == 0 && MC_sum->GetBinContent(z) != 0)) {
      if (rat->GetBinContent(z) > theMax) {
        arrow->SetPoint(z, rat->GetBinCenter(z), theMax-0.15);
      } else {
        arrow->SetPoint(z, rat->GetBinCenter(z), -1);
      }
      if (rat->GetBinContent(z) < theMin) {
        arrowdw->SetPoint(z, rat->GetBinCenter(z), theMin+0.15);
      } else {
        arrowdw->SetPoint(z, rat->GetBinCenter(z), theMax+10);
      }
      //if (rat->GetBinContent(z) == 0 && MC_sum->GetBinContent(z) != 0) {
      //  float myx = rat->GetBinCenter(z);
      //  rat->Fill(myx, 0.001);
      //}
    }
    rat->Draw("e");
    rat_band->Draw("2 ][ same");
    rat->Draw("e same");
    if (useArrow) {
      arrow->Draw("p same");
      arrowdw->Draw("p same");
    }
    gPad->RedrawAxis();
    lin.reset(new TLine(rat->GetXaxis()->GetBinLowEdge(1), 1, rat->GetXaxis()->GetBinUpEdge(rat->GetNbinsX()), 1));
    lin->SetLineColor(kBlack);
    lin->SetLineWidth(3);
    lin->SetLineStyle(2);
    lin->Draw();
  }

  // major hack to remove the zero label in the main plot, which is cut in half by the ratio pad
  if (ratio) {
    TPad *pe = new TPad("pe", "pe", 0, 0, 0.99*c->cd(1)->GetLeftMargin(), 0.18);
    pe->SetFillColor(c->cd(1)->GetFillColor());
    pe->SetBorderMode(0);
    //pe->Draw();
  }

  string _stampText = "Internal";
  if (_stamp == 1)
    _stampText = "Preliminary";
  else if (_stamp == 2)
    _stampText = "";
  if (posLegend != 2 && posLegend != 5 && posLegend != 6) {
    stampATLAS(_stampText, 0.20, 0.88);
    stampLumiText(lumi, 0.20, 0.78, "#sqrt{s} = 13 TeV", 0.05);
  } else if (posLegend == 5) {
    stampATLAS(_stampText, 0.20, 0.88);
    stampLumiText(lumi, 0.20, 0.75, "#sqrt{s} = 13 TeV", 0.05);
  } else if (posLegend == 6 || posLegend == 7) {
    stampATLAS(_stampText, 0.20, 0.88);
    stampLumiText(lumi, 0.20, 0.78, "#sqrt{s} = 13 TeV", 0.05);
  } else if (posLegend == 8) {
    stampATLAS(_stampText, 0.30, 0.88);
    stampLumiText(lumi, 0.30, 0.78, "#sqrt{s} = 13 TeV", 0.05);
  } else {
    stampATLAS(_stampText, 0.25, 0.88);
    stampLumiText(lumi, 0.25, 0.78, "#sqrt{s} = 13 TeV", 0.05);
  }
  if (posLegend < 2 || posLegend == 6) {
    for (vector<string>::const_iterator i = extraText.begin(); i != extraText.end(); ++i) {
      double pos = (double) ((int) (i - extraText.begin()));
      stampText(*i, 0.20, 0.66-0.06*pos, 0.06*0.9);
    }
  } else if (posLegend == 7) {
    for (vector<string>::const_iterator i = extraText.begin(); i != extraText.end(); ++i) {
      double pos = (double) ((int) (i - extraText.begin()));
      stampText(*i, 0.60, 0.40-0.06*pos, 0.06*0.9);
    }
  } else if (posLegend == 8) {
    for (vector<string>::const_iterator i = extraText.begin(); i != extraText.end(); ++i) {
      double pos = (double) ((int) (i - extraText.begin()));
      stampText(*i, 0.55, 0.88-0.06*pos, 0.06*0.9);
    }
  } else {
    for (vector<string>::const_iterator i = extraText.begin(); i != extraText.end(); ++i) {
      double pos = (double) ((int) (i - extraText.begin()));
      stampText(*i, 0.55, 0.88-0.06*pos, 0.06*0.9);
    }
  }

  c->SaveAs(outfile.c_str());
}

void drawDataMCCompare(SampleSetConfiguration &stackConfig, const vector<std::string> &extraText, const std::string &outfile, bool ratio, const std::string &xTitle, const vector<string> &syst_items, const vector<string> &syst_titles, double lumi) {
  TStyle *atlasStyle = AtlasStyle();
  gROOT->SetStyle("ATLAS");
  gROOT->ForceStyle();

  shared_ptr<TCanvas> c(new TCanvas("c", "", 800, 600));

  // do ratio?
  TPad *pad_ratio = 0;
  if (ratio && stackConfig._stack.find("Data") != stackConfig._stack.end()) {
    c->Divide(1, 2, 0.015, 0.01);
    pad_ratio = (TPad *) c->cd(2);
    pad_ratio->SetPad(0,0,1,0.30);
    pad_ratio->SetTopMargin(0.01);
    pad_ratio->SetBottomMargin(0.45);
    c->cd(1)->SetPad(0,0.2,1,1);
    c->cd(1)->SetBottomMargin(0.13);
  }

  c->cd(1);

  // make syst. band
  shared_ptr<TGraphAsymmErrors> band = stackConfig["MC"].makeBand();
  band->SetFillStyle(1001);
  band->SetFillColorAlpha(kGreen-8, 0.5);

  // make legend
  shared_ptr<TLegend> leg(new TLegend(0.65, 0.5, 0.95, 0.92));
  //leg->SetNColumns(2);
  leg->SetFillStyle(0);
  leg->SetBorderSize(0);

  // make MC stack and add entries in legend
  vector<shared_ptr<TH1D> > vechist;
  vector<vector<shared_ptr<TH1D> >  > vechisto;
  shared_ptr<THStack> MC = stackConfig["MC"].makeStack("MC", leg, vechist);
  vector<shared_ptr<THStack> > MCO;
  int no = stackConfig.n()-2;
  for (int z = 0; z < no; ++z) {
    vechisto.push_back(vector<shared_ptr<TH1D> >());
    MCO.push_back(stackConfig[Form("MC%d", z)].makeStack(Form("MC%d", z), leg, vechisto[z]));
  }

  shared_ptr<TH1D> Data;
  if (stackConfig._stack.find("Data") != stackConfig._stack.end())
    Data = stackConfig["Data"].makeTH1("Data");
  if (Data) {
    Data->SetStats(0);
    leg->AddEntry(Data.get(), "Data", "LP");
  }

  vector<shared_ptr<TH1D> > ExtraSyst;
  int myColours[] = {kRed, kBlue, kGreen, kMagenta, kPink};
  for (int z = 0; z < syst_items.size(); ++z) {
    ExtraSyst.push_back(stackConfig["MC"].makeTH1(Form("ExtraSyst%d", z), syst_items[z]));
    ExtraSyst[z]->SetStats(0);
    ExtraSyst[z]->SetLineColor(myColours[z]);
    leg->AddEntry(ExtraSyst[z].get(), syst_titles[z].c_str(), "F");
  }

  double maximum = MC->GetMaximum();
  if (Data) maximum = std::max(Data->GetBinContent(Data->GetMaximumBin()), MC->GetMaximum());
  MC->SetMaximum(1.7*maximum);
  if (Data)
    Data->SetMaximum(1.7*maximum);

  MC->Draw();
  for (int z = 0; z < no; ++z) {
    MCO[z]->Draw("same");
  }
  for (int z = 0; z < syst_items.size(); ++z) {
    ExtraSyst[z]->Draw("hist same");
  }
  if (!ratio)
    if (xTitle == "")
      MC->GetXaxis()->SetTitle(vechist[0]->GetXaxis()->GetTitle());
    else
      MC->GetXaxis()->SetTitle(xTitle.c_str());
  MC->GetYaxis()->SetTitle(vechist[0]->GetYaxis()->GetTitle());
  if (Data)
    Data->Draw("e same");
  //band->Draw("2 ][ same");
  leg->Draw();

  shared_ptr<TH1D> rat;
  vector<shared_ptr<TH1D> > rato;
  vector<shared_ptr<TH1D> > ratExtra;
  shared_ptr<TGraphAsymmErrors> rat_band;
  shared_ptr<TLine> lin;
  if (ratio && Data) {
    TH1D *MC_sum = (TH1D *) MC->GetStack()->At(MC->GetStack()->LastIndex());
    vector<TH1D *> MCO_sum;
    for (int z = 0; z < no; ++z) MCO_sum.push_back((TH1D *) MCO[z]->GetStack()->At(MCO[z]->GetStack()->LastIndex()));

    rat.reset((TH1D *) Data->Clone("ratio"));
    for (int z = 0; z < no; ++z) {
      rato.push_back(shared_ptr<TH1D>());
      //rato[z].reset((TH1D *) Data->Clone(Form("ratio_o_%d", z)));
      rato[z].reset((TH1D *) MC_sum->Clone(Form("ratio_o_%d", z)));
    }
    for (int z = 0; z < ExtraSyst.size(); ++z) {
      ratExtra.push_back(shared_ptr<TH1D>());
      ratExtra[z].reset((TH1D *) MC_sum->Clone(Form("ratioExtra_%d", z)));
      ratExtra[z]->SetLineColor(ExtraSyst[z]->GetLineColor());
    }
    rat->Divide(Data.get(), MC_sum, 1, 1, "B");
    for (int z = 0; z < no; ++z) {
      rato[z]->Divide(MCO_sum[z], MC_sum, 1, 1, "B");
      rato[z]->SetStats(0);
      rato[z]->GetYaxis()->SetRangeUser(0.3, 1.7);
      rato[z]->SetTitle("");
    }
    for (int z = 0; z < ExtraSyst.size(); ++z) {
      ratExtra[z]->Divide(ExtraSyst[z].get(), MC_sum, 1, 1, "B");
      ratExtra[z]->SetStats(0);
      ratExtra[z]->GetYaxis()->SetRangeUser(0.3, 1.7);
      ratExtra[z]->SetTitle("");
    }
    rat_band = normaliseBand(band, MC_sum);

    c->cd(2);
    rat->SetStats(0);
    rat->GetYaxis()->SetRangeUser(0.4, 1.6);
    rat->SetTitle("");
    if (xTitle == "")
      rat->GetXaxis()->SetTitle(MC_sum->GetXaxis()->GetTitle());
    else
      rat->GetXaxis()->SetTitle(xTitle.c_str());
    rat->GetYaxis()->SetTitle("#frac{Any}{Nominal}");
    rat->GetYaxis()->SetNdivisions(3, 0, 5);
    rat->GetXaxis()->SetLabelFont(42);
    rat->GetXaxis()->SetTitleFont(42);
    rat->GetYaxis()->SetLabelFont(42);
    rat->GetYaxis()->SetTitleFont(42);
    rat->GetYaxis()->SetLabelSize(0.18);
    rat->GetYaxis()->SetTitleOffset(0.45);
    rat->GetYaxis()->SetLabelOffset(0.02);
    rat->GetYaxis()->SetTitleSize(0.18);
    rat->GetXaxis()->SetTitleSize(0.2);
    rat->GetXaxis()->SetLabelSize(0.18);
    rat->GetXaxis()->SetTitleSize(0.18);
    rat->GetXaxis()->SetTitleOffset(1.1);
    rat->SetTitle("");

    for (int z = 0; z < no; ++z) {
      rato[z]->GetYaxis()->SetTitle("Data/Sim.");
      rato[z]->GetYaxis()->SetNdivisions(3, 0, 5);
      rato[z]->GetXaxis()->SetLabelFont(42);
      rato[z]->GetXaxis()->SetTitleFont(42);
      rato[z]->GetYaxis()->SetLabelFont(42);
      rato[z]->GetYaxis()->SetTitleFont(42);
      rato[z]->GetYaxis()->SetLabelSize(0.18);
      rato[z]->GetYaxis()->SetTitleOffset(0.45);
      rato[z]->GetYaxis()->SetLabelOffset(0.02);
      rato[z]->GetYaxis()->SetTitleSize(0.18);
      rato[z]->GetXaxis()->SetTitleSize(0.2);
      rato[z]->GetXaxis()->SetLabelSize(0.18);
      rato[z]->GetXaxis()->SetTitleSize(0.18);
      rato[z]->GetXaxis()->SetTitleOffset(1.1);
      rato[z]->SetTitle("");
      rato[z]->SetLineColor(MCO_sum[z]->GetLineColor());
    }
    rat->Draw("e");
    for (int z = 0; z < no; ++z) {
      rato[z]->Draw("hist same");
    }
    for (int z = 0; z < ratExtra.size(); ++z) {
      ratExtra[z]->Draw("hist same");
    }
    //rat_band->Draw("2 ][ same");
    lin.reset(new TLine(rat->GetXaxis()->GetBinLowEdge(1), 1, rat->GetXaxis()->GetBinUpEdge(rat->GetNbinsX()), 1));
    lin->SetLineColor(kBlack);
    lin->SetLineWidth(3);
    lin->SetLineStyle(2);
    lin->Draw();
  }

  // major hack to remove the zero label in the main plot, which is cut in half by the ratio pad
  if (ratio) {
    TPad *pe = new TPad("pe", "pe", 0, 0, 0.99*c->cd(1)->GetLeftMargin(), 0.18);
    pe->SetFillColor(c->cd(1)->GetFillColor());
    pe->SetBorderMode(0);
    //pe->Draw();
  }

  string _stampText = "Internal";
  if (_stamp == 1)
    _stampText = "Preliminary";
  else if (_stamp == 2)
    _stampText = "";
  stampATLAS(_stampText, 0.20, 0.89);
  stampLumi(lumi, 0.20, 0.81);
  for (vector<string>::const_iterator i = extraText.begin(); i != extraText.end(); ++i) {
    double pos = (double) ((int) (i - extraText.begin()));
    stampText(*i, 0.20, 0.74-0.05*pos, 0.06*0.9);
  }

  c->SaveAs(outfile.c_str());
}

void drawEff(SampleSet *ssMC, const vector<std::string> &extraText, const std::string &outfile, const std::string &yTitle, SampleSet *ssData, bool mcError, int mustBeBigger, float yMax, const std::string &xTitle, SampleSet *ssRat, double lumi) {
  TStyle *atlasStyle = AtlasStyle();
  gROOT->SetStyle("ATLAS");
  gROOT->ForceStyle();
  gStyle->SetOptStat(0);
  gStyle->SetLabelSize(0.1);

  shared_ptr<TCanvas> c(new TCanvas("c", "", 800, 600));

  // do ratio?
  TPad *pad_ratio = 0;
  TPad *pad_ratio2 = 0;
  c->Divide(1, 2, 0.015, 0.01);
  pad_ratio = (TPad *) c->cd(2);
  pad_ratio->SetPad(0.01,0,1,0.30);
  pad_ratio->SetTopMargin(0.01);
  pad_ratio->SetBottomMargin(0.45);
  pad_ratio->SetLeftMargin(0.16);
  c->cd(1)->SetPad(0.01,0.2,1,0.99);
  c->cd(1)->SetBottomMargin(0.13);

  c->cd(1);

  // make syst. band
  shared_ptr<TGraphAsymmErrors> band;
  if (ssData)
    band = ssData->makeBand(true);
  if (band) {
    band->SetFillStyle(3354);
    band->SetLineStyle(1);
    band->SetLineColor(kBlack);
    band->SetFillColor(kBlack);
  }

  shared_ptr<TGraphAsymmErrors> bandMC = ssMC->makeBand(true);
  bandMC->SetFillStyle(3354);
  bandMC->SetLineStyle(1);
  bandMC->SetLineColor(kRed);
  bandMC->SetFillColor(kRed);

  // make legend
  shared_ptr<TLegend> leg;
  leg.reset(new TLegend(0.40,0.15,0.65,0.35));
  //leg->SetNColumns(1);
  leg->SetFillStyle(0);
  leg->SetBorderSize(0);
  leg->SetTextSize(0.045);

  // make MC stack and add entries in legend
  shared_ptr<TH1D> MC = ssMC->makeTH1("MC");
  MC->SetStats(0);
  MC->SetMarkerStyle(22);
  MC->SetMarkerColor(kRed);
  MC->SetMarkerSize(1.0);
  MC->SetLineColor(kRed);

  shared_ptr<TH1D> Data;
  if (ssData)
    Data = ssData->makeTH1("Data");
  if (Data) {
    Data->SetStats(0);
    Data->SetMarkerStyle(20);
    Data->SetMarkerSize(1.0);
    Data->SetMarkerColor(kBlack);
    Data->SetLineColor(kBlack);
    leg->AddEntry(Data.get(), "Data - BG", "LP");
  }
  leg->AddEntry(MC.get(), "MC", "LP");

  TLegend *leg2;
  leg2 = new TLegend(0.65,0.18,0.85,0.26);
  //leg2->SetNColumns(1);
  leg2->SetFillStyle(0);
  leg2->SetBorderSize(0);
  leg2->SetTextSize(0.045);
  if (mcError) leg2->AddEntry(bandMC.get(), "Syst. uncertainty", "F");
  // data error
  else leg2->AddEntry(band.get(), "Syst. uncertainty", "F");

  double maximum = MC->GetBinContent(MC->GetMaximumBin());
  if (Data) maximum = std::max(Data->GetBinContent(Data->GetMaximumBin()), MC->GetBinContent(MC->GetMaximumBin()));
  maximum *= 1.7;
  if (yMax > 0) maximum = yMax;
  MC->SetMaximum(maximum);
  if (Data) {
    Data->SetMaximum(maximum);
    if (yTitle != "") Data->GetYaxis()->SetTitle(yTitle.c_str());
  }

  MC->SetMinimum(0.0001);
  if (Data)
    Data->SetMinimum(0.0001);

  MC->GetXaxis()->SetTitleOffset(2.0);
  MC->GetYaxis()->SetTitleOffset(1.0); //1.7
  int ndiv = (int) floor((MC->GetXaxis()->GetBinUpEdge(MC->GetNbinsX())-MC->GetXaxis()->GetBinLowEdge(1))/MC->GetBinWidth(1));
  MC->GetXaxis()->SetNdivisions(ndiv+500, false);

  if (Data) {
    Data->GetXaxis()->SetTitleOffset(2.0);
    Data->GetYaxis()->SetTitleOffset(1.0);
  }
  if (yTitle != "") MC->GetYaxis()->SetTitle(yTitle.c_str());

  MC->Draw("e");
  Data->Draw("e same");

  if (mcError) {
    bandMC->Draw("2 ][ same");
  } else if (!mcError && band) band->Draw("2 ][ same");
  leg->Draw();
  leg2->Draw();

  shared_ptr<TH1D> rat;
  shared_ptr<TGraphAsymmErrors> rat_band;
  if (Data && MC) {
    if (ssRat) {
      rat = ssRat->makeTH1("ratrat");
      rat->SetStats(0);
      rat->SetMarkerStyle(20);
      rat->SetMarkerSize(1.0);
      rat->SetMarkerColor(kBlack);
      rat->SetLineColor(kBlack);
      rat_band = ssRat->makeBand(false);
    } else {
      rat.reset((TH1D *) Data->Clone("ratio_std"));
      rat->Divide(Data.get(), MC.get(), 1, 1, "B");
      if (band) {
        rat_band = normaliseBand(band, MC.get());
      }
    }
  }

  c->cd(2);
  shared_ptr<TLegend> legSFerr;
  shared_ptr<TLine> lin;
  if (rat) {
    rat->SetStats(0);
    if (mustBeBigger == 0)
      rat->GetYaxis()->SetRangeUser(0.3, 1.7);
    else if (mustBeBigger == 1)
      rat->GetYaxis()->SetRangeUser(0.1, 1.9);
    else if (mustBeBigger == 2)
      rat->GetYaxis()->SetRangeUser(0.8, 1.2);
    rat->SetTitle("");
    rat->GetXaxis()->SetTitle(MC->GetXaxis()->GetTitle());
    if (xTitle != "") {
      rat->GetXaxis()->SetTitle(xTitle.c_str());
    }
    rat->GetYaxis()->SetTitle("Data/Sim.");
    rat->GetYaxis()->SetNdivisions(405, true);
    rat->GetXaxis()->SetNdivisions(ndiv+500, false);
    rat->GetXaxis()->SetLabelFont(42);
    rat->GetXaxis()->SetTitleFont(42);
    rat->GetYaxis()->SetLabelFont(42);
    rat->GetYaxis()->SetTitleFont(42);
    rat->GetYaxis()->SetLabelOffset(0.02);
    //rat->GetXaxis()->SetTitleSize(0.14);
    //rat->GetXaxis()->SetLabelSize(0.14);
    //rat->GetXaxis()->SetTitleOffset(1.0);
    rat->GetXaxis()->SetTitleSize(0.18);
    rat->GetXaxis()->SetLabelSize(0.18);
    rat->GetXaxis()->SetTitleOffset(1.1);

    //rat->GetYaxis()->SetLabelSize(0.14);
    //rat->GetYaxis()->SetTitleSize(0.14);
    //rat->GetYaxis()->SetTitleOffset(0.5);
    rat->GetYaxis()->SetLabelSize(0.18);
    rat->GetYaxis()->SetTitleSize(0.18);
    rat->GetYaxis()->SetTitleOffset(0.45);
    rat->SetTitle("");

    rat->Draw("e");
    if (rat_band) rat_band->Draw("2 ][ same");
    if (!mcError && rat_band)
      rat_band->SetFillColor(kBlue);
    else if (rat_band)
      rat_band->SetFillColor(kRed);
    if (rat_band)
      rat_band->SetFillStyle(3345);

    lin.reset(new TLine(rat->GetXaxis()->GetBinLowEdge(1), 1, rat->GetXaxis()->GetBinUpEdge(rat->GetNbinsX()), 1));
    lin->SetLineColor(kBlack);
    lin->SetLineWidth(3);
    lin->SetLineStyle(2);
    lin->Draw();

    c->cd(2)->SetGridy();
    c->cd(1);

    legSFerr.reset(new TLegend(0.18,0.68,0.48,0.75));
    if (!mcError && rat_band) {
      legSFerr->AddEntry(rat_band.get(),"correlated data-MC systematic uncertainty","f");
    } else {
      //legSFerr->AddEntry(rat_band.get(),"MC systematic error","f");
    }
    legSFerr->SetTextSize(0.04);
    if (!mcError) legSFerr->Draw();

  }

  c->cd(1);
  double xstart = 0.2;
  double ystart = 0.88;

  string _stampText = "Internal";
  if (_stamp == 1)
    _stampText = "Preliminary";
  else if (_stamp == 2)
    _stampText = "";
  stampATLAS(_stampText, xstart, ystart);
  stampLumiText(lumi, xstart, ystart-0.10, "#sqrt{s} = 13 TeV", 0.05);

  vector<double> xx;
  vector<double> yy;
  xx.push_back(xstart+0.42);
  yy.push_back(ystart);
  xx.push_back(xstart+0.42);
  yy.push_back(ystart-0.06*1);
  xx.push_back(xstart);
  yy.push_back(ystart-0.25 - 0.06*0);
  xx.push_back(xstart);
  yy.push_back(ystart-0.25 - 0.06*1);
  for (vector<string>::const_iterator i = extraText.begin(); i != extraText.end(); ++i) {
    size_t pos = ((size_t) (i - extraText.begin()));
    stampText(*i, xx[pos], yy[pos], 0.05);
  }

  c->SaveAs(outfile.c_str());
}

void stampATLAS(const std::string &text, float x, float y) {
  TLatex l;
  l.SetNDC();
  l.SetTextFont(72);
  l.SetTextColor(1);
  double delx = 0.115*696*gPad->GetWh()/(472*gPad->GetWw());

  l.SetTextSize(0.06);
  l.DrawLatex(x, y, "ATLAS");

  TLatex p;
  p.SetNDC();
  p.SetTextFont(42);
  p.SetTextColor(1);

  p.SetTextSize(0.06);
  p.DrawLatex(x+delx, y, text.c_str());

}
void stampLumi(float lumi, float x, float y) {
  std::stringstream ss;
  ss << "#int L dt = " << lumi << " fb^{-1}";
  TLatex l;
  l.SetNDC();
  l.SetTextFont(42);
  l.SetTextColor(1);
  l.SetTextSize(0.06*0.7);
  l.DrawLatex(x, y, ss.str().c_str());
}
void stampText(const std::string &text, float x, float y, float size) {
  TLatex l;
  l.SetNDC();
  l.SetTextFont(42);
  l.SetTextColor(1);
  l.SetTextSize(size);
  l.DrawLatex(x, y, text.c_str());
}

void stampLumiText(float lumi, float x, float y, const std::string &text, float size) {
  std::stringstream ss;
  ss << "#int L dt = " << lumi << " fb^{-1}, " << text;
  TLatex l;
  l.SetNDC();
  l.SetTextFont(42);
  l.SetTextColor(1);
  l.SetTextSize(size);
  l.DrawLatex(x, y, ss.str().c_str());
}


TStyle *AtlasStyle()  {
  TStyle *atlasStyle = new TStyle("ATLAS","Atlas style");

  // use plain black on white colors
  Int_t icol=0; // WHITE
  atlasStyle->SetFrameBorderMode(icol);
  atlasStyle->SetFrameFillColor(icol);
  atlasStyle->SetCanvasBorderMode(icol);
  atlasStyle->SetCanvasColor(icol);
  atlasStyle->SetPadBorderMode(icol);
  atlasStyle->SetPadColor(icol);
  atlasStyle->SetStatColor(icol);
  atlasStyle->SetStatW(0.15);
  atlasStyle->SetStatH(0.11);
  atlasStyle->SetLegendBorderSize(icol);
  //atlasStyle->SetFillColor(icol); // don't use: white fill color for *all* objects

  // set the paper & margin sizes
  atlasStyle->SetPaperSize(20,26);

  // set margin sizes
  atlasStyle->SetPadTopMargin(0.06);
  atlasStyle->SetPadRightMargin(0.08);
  atlasStyle->SetPadBottomMargin(0.15);
  atlasStyle->SetPadLeftMargin(0.16);

  // Set Canvas sizes
  atlasStyle->SetCanvasDefH(500);
  atlasStyle->SetCanvasDefW(800);
  atlasStyle->SetCanvasDefH(600);
  atlasStyle->SetCanvasDefW(600);

  // set title offsets (for axis label)
  atlasStyle->SetTitleXOffset(0.9); //1.2
  atlasStyle->SetTitleYOffset(1.0); // 1.4

  // use large fonts
  //Int_t font=72; // Helvetica italics
  Int_t font=42; // Helvetica
  Double_t tsize=0.05;
  atlasStyle->SetTextFont(font);

  atlasStyle->SetTextSize(tsize);
  atlasStyle->SetLabelFont(font,"x");
  atlasStyle->SetTitleFont(font,"x");
  atlasStyle->SetLabelFont(font,"y");
  atlasStyle->SetTitleFont(font,"y");
  atlasStyle->SetLabelFont(font,"z");
  atlasStyle->SetTitleFont(font,"z");

  atlasStyle->SetLabelSize(0.07,"x");
  atlasStyle->SetTitleSize(0.07,"x");
  atlasStyle->SetLabelSize(0.06,"y");
  atlasStyle->SetTitleSize(0.07,"y");
  atlasStyle->SetLabelSize(tsize,"z");
  atlasStyle->SetTitleSize(tsize,"z");

  // use bold lines and markers
  atlasStyle->SetMarkerStyle(20);
  atlasStyle->SetMarkerSize(1.2);
  atlasStyle->SetHistLineWidth(2);
  atlasStyle->SetHatchesLineWidth(1);
  atlasStyle->SetLineStyleString(2,"[12 12]"); // postscript dashes

  // get rid of X error bars 
  //atlasStyle->SetErrorX(0.001);
  atlasStyle->SetEndErrorSize(4.0);

  // do not display any of the standard histogram decorations
  atlasStyle->SetOptTitle(0);
  atlasStyle->SetOptStat(1111);
  //atlasStyle->SetOptStat(0);
  atlasStyle->SetOptFit(1111);
  //atlasStyle->SetOptFit(0);

  // put tick marks on top and RHS of plots
  atlasStyle->SetPadTickX(1);
  atlasStyle->SetPadTickY(1);

  // PALETTE
  atlasStyle->SetPalette(1,0);

  return atlasStyle;
}

SampleSetConfiguration makeConfigurationPlots(const string &prefix, const string &channel, bool isMcOnly) {
  SampleSetConfiguration stackConfig;

  stackConfig.addType("MC");
  if (!isMcOnly)
    stackConfig.addType("Data");
  if (channel == "e" && !isMcOnly)
    stackConfig.add("Data", Form("%s_e_DTE.root", prefix.c_str()), "data", "Data", "Data",
                        "PL", 1, kBlack, 1, 0, 20, 1, "e");
  else if (channel == "mu" && !isMcOnly)
    stackConfig.add("Data", Form("%s_mu_DTE.root", prefix.c_str()), "data", "Data", "Data",
                        "PL", 1, kBlack, 1, 0, 20, 1, "e");
  else if (channel == "comb" && !isMcOnly)
    stackConfig.add("Data", Form("%s_comb_DTE.root", prefix.c_str()), "data", "Data", "Data",
                        "PL", 1, kBlack, 1, 0, 20, 1, "e");

  stackConfig.add("MC", Form("%s_%s_ttbar.root", prefix.c_str(), channel.c_str()), "ttbar matched", "$t\\bar{t}$", "t#bar{t} (matched)",
                          "F", 1, kBlack, 1001,      0, 1, 0, "hist");
  stackConfig.add("MC", Form("%s_%s_singletop.root", prefix.c_str(), channel.c_str()), "Single Top", "single top", "Single top",
                        "F", 1, kBlack, 1001,     62, 1, 0, "hist");
  stackConfig.add("MC", Form("%s_%s_Wjets.root", prefix.c_str(), channel.c_str()), "W+jets", "$W+$ jets", "W+jets",
                        "F", 1, kBlack, 1001,     92, 1, 0, "hist");
  stackConfig.add("MC", Form("%s_%s_Zjets.root", prefix.c_str(), channel.c_str()), "Z+jets", "$Z+$ jets", "Z+jets",
                        "", 1, kBlack, 1001,    807, 1, 0, "hist");
  stackConfig.add("MC", Form("%s_%s_VV.root", prefix.c_str(), channel.c_str()), "diboson", "diboson", "diboson",
                        "", 1, kBlack, 1001,       5, 1, 0, "hist");

  return stackConfig;
}

SampleSetConfiguration makeConfigurationPlotsCompare(const string &prefix, const string &channel, const vector<string> &other, const vector<string> &title) {
  SampleSetConfiguration stackConfig;

  stackConfig.addType("MC");
  stackConfig.addType("Data");
  for (int z = 0; z < other.size(); z++) {
    stackConfig.addType(Form("MC%d", z));
  }

  stackConfig.add("MC", Form("%s_%s_ttbar.root", prefix.c_str(), channel.c_str()), "ttbar matched", "$t\\bar{t}$", "t#bar{t} (matched)",
                          "F", 1, kBlack, 1001,      0, 1, 0, "hist");
  stackConfig.add("MC", Form("%s_%s_singletop.root", prefix.c_str(), channel.c_str()), "Single Top", "single top", "Single top",
                        "F", 1, kBlack, 1001,     62, 1, 0, "hist");
  stackConfig.add("MC", Form("%s_%s_Wjets.root", prefix.c_str(), channel.c_str()), "W+jets", "$W+$ jets", "W+jets",
                        "F", 1, kBlack, 1001,     92, 1, 0, "hist");
  stackConfig.add("MC", Form("%s_%s_Zjets.root", prefix.c_str(), channel.c_str()), "Z+jets", "$Z+$ jets", "Z+jets",
                        "", 1, kBlack, 1001,    807, 1, 0, "hist");
  stackConfig.add("MC", Form("%s_%s_VV.root", prefix.c_str(), channel.c_str()), "diboson", "diboson", "diboson",
                        "", 1, kBlack, 1001,       5, 1, 0, "hist");

  int col[] = {kRed, kBlue, kGreen};
  for (int z = 0; z < other.size(); ++z) {
    stackConfig.add(Form("MC%d", z), other[z], title[z], title[z], title[z],
                          "F", 1, col[z], 1001,      0, 1, 0, "hist");
    stackConfig.add(Form("MC%d", z), Form("%s_%s_singletop.root", prefix.c_str(), channel.c_str()), Form("single top %d", z), "single top", "single top",
                          "", 1, kBlack, 1001,     62, 1, 0, "hist");
    stackConfig.add(Form("MC%d", z), Form("%s_%s_Wjets.root", prefix.c_str(), channel.c_str()), Form("W+jets %d", z), "$W+$ jets", "W + jets",
                          "", 1, kBlack, 1001,     92, 1, 0, "hist");
    stackConfig.add(Form("MC%d", z), Form("%s_%s_Zjets.root", prefix.c_str(), channel.c_str()), Form("Z+jets %d", z), "$Z+$ jets", "Z + jets",
                          "", 1, kBlack, 1001,    807, 1, 0, "hist");
    stackConfig.add(Form("MC%d", z), Form("%s_%s_VV.root", prefix.c_str(), channel.c_str()), Form("diboson %d", z), "diboson", "diboson",
                          "", 1, kBlack, 1001,       5, 1, 0, "hist");
  }
  if (channel == "e.root")
    stackConfig.add("Data", Form("%s_e_data.root", prefix.c_str()), "data", "data", "data",
                        "PL", 1, kBlack, 1, 0, 20, 1, "e");
  else if (channel == "mu.root")
    stackConfig.add("Data", Form("%s_mu_data.root", prefix.c_str()), "data", "data", "data",
                        "PL", 1, kBlack, 1, 0, 20, 1, "e");
  else if (channel == "comb.root")
    stackConfig.add("Data", Form("%s_comb_DTE.root", prefix.c_str()), "data", "data", "data",
                        "PL", 1, kBlack, 1, 0, 20, 1, "e");

  return stackConfig;
}

SampleSetConfiguration makeConfigurationMCEff(const string &prefix, const string &channel) {
  SampleSetConfiguration stackConfig;

  stackConfig.addType("MCAtNLO");
  stackConfig.add("MCAtNLO", Form("%s_%s_ttbar.root", prefix.c_str(), channel.c_str()), "ttbar", "$t\\bar{t}", "t#bar{t}",
                        "F", 1, kBlack, 1001, 0, 1, 0, "hist");

  return stackConfig;
}


SampleSetConfiguration makeConfigurationDataEff(const string &prefix, const string &channel) {
  SampleSetConfiguration stackConfig;

  stackConfig.addType("MC");
  stackConfig.addType("Data");
  if (channel == "e")
    stackConfig.add("Data", Form("%s_e_DTE.root", prefix.c_str()), "data", "data", "data",
                            "PL", 1, kBlack, 1, 0, 20, 1, "e");
  else if (channel == "mu")
    stackConfig.add("Data", Form("%s_mu_DTE.root", prefix.c_str()), "data", "data", "data",
                            "PL", 1, kBlack, 1, 0, 20, 1, "e");
  else if (channel == "comb.root")
    stackConfig.add("Data", Form("%s_comb_DTE.root", prefix.c_str()), "data", "data", "data",
                            "PL", 1, kBlack, 1, 0, 20, 1, "e");

  stackConfig.add("MC", Form("%s_%s_ttbar.root", prefix.c_str(), channel.c_str()), "ttbar not matched", "$t\\bar{t}$ not matched", "t#bar{t} (not matched)",
                        "F", 1, kBlack, 1001,  kGray, 1, 0, "hist");
  stackConfig.add("MC", Form("%s_%s_singletop.root", prefix.c_str(), channel.c_str()), "single top", "single top", "single top",
                        "F", 1, kBlack, 1001,     62, 1, 0, "hist");
  stackConfig.add("MC", Form("%s_%s_Wjets.root", prefix.c_str(), channel.c_str()), "W+jets", "$W+$ jets", "W + jets",
                        "F", 1, kBlack, 1001,     92, 1, 0, "hist");
  stackConfig.add("MC", Form("%s_%s_Zjets.root", prefix.c_str(), channel.c_str()), "Z+jets", "$Z+$ jets", "Z + jets",
                        "", 1, kBlack, 1001,     95, 1, 0, "hist");
  stackConfig.add("MC", Form("%s_%s_VV.root", prefix.c_str(), channel.c_str()), "diboson", "diboson", "diboson",
                        "", 1, kBlack, 1001,       5, 1, 0, "hist");

  return stackConfig;
}

void addAllSystematics(SystematicCalculator &systCalc, const std::string &channel) {
  vector<string> only_ttbar;
  only_ttbar.push_back("ttbar_");

  systCalc.add("(00) Luminosity", new NotData(new HistNorm(0.03)));

  systCalc.add("(01) \\akt $R=0.4$ jet energy resolution", new NotData(new Symm(new HistDiff("JET_JER_SINGLE_NP__1up", ""))));
  systCalc.add("(02) \\akt $R=0.4$ jet energy scale 1", new NotData(new Symm(new HistDiff("JET_NPScenario1_JET_GroupedNP_1__1up", ""), new HistDiff("JET_NPScenario1_JET_GroupedNP_1__1down", ""))));
  systCalc.add("(03) \\akt $R=0.4$ jet energy scale 2", new NotData(new Symm(new HistDiff("JET_NPScenario1_JET_GroupedNP_2__1up", ""), new HistDiff("JET_NPScenario1_JET_GroupedNP_2__1down", ""))));
  systCalc.add("(04) \\akt $R=0.4$ jet energy scale 3", new NotData(new Symm(new HistDiff("JET_NPScenario1_JET_GroupedNP_3__1up", ""), new HistDiff("JET_NPScenario1_JET_GroupedNP_3__1down", ""))));
  //systCalc.add("(05) \\akt $R=1.0$ jet energy resolution", new NotData(new HistDiff("", "")));
  //systCalc.add("(06) \\akt $R=1.0$ jet energy scale", new NotData(new Symm(new HistDiff("", ""), new HistDiff("", ""))));

  systCalc.add("(07) Muon res. (MS)", new NotData(new Symm(new HistDiff("MUONS_MS__1up", ""), new HistDiff("MUONS_MS__1down", ""))));
  systCalc.add("(08) Muon res. (ID)", new NotData(new Symm(new HistDiff("MUONS_ID__1up", ""), new HistDiff("MUONS_ID__1down", ""))));
  systCalc.add("(09) Muon scale", new NotData(new Symm(new HistDiff("MUONS_SCALE__1up", ""), new HistDiff("MUONS_SCALE__1down", ""))));
  systCalc.add("(10) Electron res.", new NotData(new Symm(new HistDiff("EG_RESOLUTION_ALL__1up", ""), new HistDiff("EG_RESOLUTION_ALL__1down", ""))));
  systCalc.add("(11) Electron scale", new NotData(new Symm(new HistDiff("EG_SCALE_ALL__1up", ""), new HistDiff("EG_SCALE_ALL__1down", ""))));

  systCalc.add("(12) MET Soft Trk res. para.", new NotData(new Symm(new HistDiff("MET_SoftTrk_ResoPara", ""))));
  systCalc.add("(13) MET Soft Trk res. perp.", new NotData(new Symm(new HistDiff("MET_SoftTrk_ResoPerp", ""))));
  systCalc.add("(14) MET Soft Trk scale", new NotData(new Symm(new HistDiff("MET_SoftTrk_ScaleUp", ""), new HistDiff("MET_SoftTrk_ScaleDown", ""))));

  systCalc.add("(15) b-tagging efficiency E0", new NotData(new Symm(new HistDiff("btagbSF_0__1up", ""), new HistDiff("btagbSF_0__1down", ""))));
  systCalc.add("(16) b-tagging efficiency E1", new NotData(new Symm(new HistDiff("btagbSF_1__1up", ""), new HistDiff("btagbSF_1__1down", ""))));
  systCalc.add("(17) b-tagging efficiency E2", new NotData(new Symm(new HistDiff("btagbSF_2__1up", ""), new HistDiff("btagbSF_2__1down", ""))));
  systCalc.add("(18) b-tagging efficiency E3", new NotData(new Symm(new HistDiff("btagbSF_3__1up", ""), new HistDiff("btagbSF_3__1down", ""))));
  systCalc.add("(19) b-tagging efficiency E4", new NotData(new Symm(new HistDiff("btagbSF_4__1up", ""), new HistDiff("btagbSF_4__1down", ""))));
  systCalc.add("(20) b-tagging efficiency E5", new NotData(new Symm(new HistDiff("btagbSF_5__1up", ""), new HistDiff("btagbSF_5__1down", ""))));

  systCalc.add("(21) c-jet mistag E0", new NotData(new Symm(new HistDiff("btagcSF_0__1up", ""), new HistDiff("btagcSF_0__1down", ""))));
  systCalc.add("(22) c-jet mistag E1", new NotData(new Symm(new HistDiff("btagcSF_1__1up", ""), new HistDiff("btagcSF_1__1down", ""))));
  systCalc.add("(23) c-jet mistag E2", new NotData(new Symm(new HistDiff("btagcSF_2__1up", ""), new HistDiff("btagcSF_2__1down", ""))));
  systCalc.add("(24) c-jet mistag E3", new NotData(new Symm(new HistDiff("btagcSF_3__1up", ""), new HistDiff("btagcSF_3__1down", ""))));

  systCalc.add("(25) l-jet mistag E0", new NotData(new Symm(new HistDiff("btaglSF_0__1up", ""), new HistDiff("btaglSF_0__1down", ""))));
  systCalc.add("(26) l-jet mistag E1", new NotData(new Symm(new HistDiff("btaglSF_1__1up", ""), new HistDiff("btaglSF_1__1down", ""))));
  systCalc.add("(27) l-jet mistag E2", new NotData(new Symm(new HistDiff("btaglSF_2__1up", ""), new HistDiff("btaglSF_2__1down", ""))));
  systCalc.add("(28) l-jet mistag E3", new NotData(new Symm(new HistDiff("btaglSF_3__1up", ""), new HistDiff("btaglSF_3__1down", ""))));

  systCalc.add("(29) Lepton SF", new NotData(new Symm(new HistDiff("lepSF__1up", ""), new HistDiff("lepSF__1down", ""))));

  systCalc.add("(30) ttbar cross section", new NotData(new Symm(new HistNorm(0.10, only_ttbar), new HistNorm(-0.10, only_ttbar))));

  //systCalc.add("(31) PDF", new Relative(Form("out_pdf1_%s", channel.c_str()), Form("out_pdf2_%s", channel.c_str()), only_allttbar));
  //systCalc.add("(32) Parton shower", new Relative(Form("out_pshower4_%s", channel.c_str()), Form("out_pshower1_%s", channel.c_str()), only_allttbar));
  //systCalc.add("(33) ISR/FSR", new RelativeISRFSR(Form("out_isr2_%s", channel.c_str()), Form("out_isr1_%s", channel.c_str()), only_allttbar));
  //systCalc.add("(34) MC generator", new Relative(Form("out_mcgen1_%s", channel.c_str()), Form("out_mcgen4_%s", channel.c_str()), only_allttbar));
  //systCalc.add("(35) Renormalisation scale", new NotData(new Symm(new HistDiff("_scaleUp", ""), new HistDiff("_scaleDown", ""))));
}


void dumpTrace() {
  void *trace[16];
  char **messages = (char **)NULL;
  int i, trace_size = 0;

  // get void*'s for all entries on the stack
  trace_size = backtrace(trace, 16);
  messages = backtrace_symbols(trace, trace_size);
  cout << "Back trace:" << endl;
  for (i=1; i<trace_size; ++i) {
    cout << "[bt] #" << i << " " << messages[i] << endl;
   /* find first occurence of '(' or ' ' in message[i] and assume
    * everything before that is the file name. (Don't go beyond 0 though
    * (string terminator)*/
    size_t p = 0;
    while(messages[i][p] != '(' && messages[i][p] != ' ' && messages[i][p] != 0)
      ++p;

    stringstream syscom;
    string filename = string(messages[i]).substr(0, p);
    syscom << "addr2line " << trace[i] << " -e " << filename;
    //last parameter is the file name of the symbol
    system(syscom.str().c_str());
  }
}

void handler(int sig) {
  cout << "Error signal " << sig << endl;
  dumpTrace();
  exit(1);
}

void split(const std::string &s, char delim, std::vector<std::string> &elems) {
  std::stringstream ss(s);
  std::string item;
  while (std::getline(ss, item, delim)) {
    elems.push_back(item);
  }
}

