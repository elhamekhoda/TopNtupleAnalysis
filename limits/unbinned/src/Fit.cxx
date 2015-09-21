#include "FitUtils.h"
#include "ParseUtils.h"

#include "TLatex.h"
#include "TLine.h"
#include "TLegend.h"
#include "TStyle.h"
#include "TGraphErrors.h"
#include "TGraphAsymmErrors.h"
#include "TH1F.h"

#include "TCanvas.h"
#include "TGraph.h"

using namespace std;

int main(int argc, char **argv) {
  gStyle->SetOptStat(0);

  int help = 0;
  float _injMu = 0;
  float _sigSyst = 0;
  float _sigShapeSyst = 0;
  string _outdir = "results";
  int fitSignal = 0;
  int fitBkg = 0;
  int makeWorkspace = 0;
  int doLimit = 0;

  static struct extendedOption extOpt[] = {
      {"help",            no_argument,       &help,   1, "Display help", &help, extendedOption::eOTInt},
      {"injMu",           required_argument,     0, 'i', "Inject signal with this mu.", &_injMu, extendedOption::eOTFloat},
      {"sigSyst",         required_argument,     0, 's', "Add this signal normalisation systematic unc.", &_sigSyst, extendedOption::eOTFloat},
      {"sigShapeSyst",    required_argument,     0, 'y', "Add this signal shape systematic unc.", &_sigShapeSyst, extendedOption::eOTFloat},
      {"outdir",          required_argument,     0, 'd', "Output plot directory", &_outdir, extendedOption::eOTString},
      {"fitSignal",       required_argument,     0, 'S', "Fit signal.", &fitSignal, extendedOption::eOTInt},
      {"fitBkg",          required_argument,     0, 'B', "Fit background.", &fitBkg, extendedOption::eOTInt},
      {"makeWorkspace",   required_argument,     0, 'w', "Make joint workspace.", &makeWorkspace, extendedOption::eOTInt},
      {"doLimit",         required_argument,     0, 'L', "Do limit setting.", &doLimit, extendedOption::eOTInt},
      {0, 0, 0, 0, 0, 0, extendedOption::eOTInt}
  };

  if (!parseArguments(argc, argv, extOpt) || help) {
    dumpHelp("Fit", extOpt, "Fit\nFit background to data and calculate limits.\n");
    return 0;
  } else {
    std::cout << "Dumping options:" << std::endl;
    dumpOptions(extOpt);
  }

  outputDir = _outdir;
  vector<float> points_xsec;
  points_xsec.push_back(1.3*3.69900238076);//1.7);
  points_xsec.push_back(1.3*1.50806798183);
  points_xsec.push_back(1.3*0.684451508485);
  points_xsec.push_back(1.3*0.334388285018);
  points_xsec.push_back(1.3*0.172299333764);//3.6e-2);
  points_xsec.push_back(1.3*0.0923739492669);
  points_xsec.push_back(1.3*0.0510543839336);
  points_xsec.push_back(1.3*0.0166807659717);//1.5e-3);
  vector<float> points_n;
  points_n.push_back(1.0);
  points_n.push_back(1.25);
  points_n.push_back(1.5);
  points_n.push_back(1.75);
  points_n.push_back(2.0);
  points_n.push_back(2.25);
  points_n.push_back(2.5);
  points_n.push_back(3.0);
  vector<string> points;
  points.push_back("zp1tev");
  points.push_back("zp125tev");
  points.push_back("zp15tev");
  points.push_back("zp175tev");
  points.push_back("zp2tev");
  points.push_back("zp225tev");
  points.push_back("zp25tev");
  points.push_back("zp3tev");

  if (fitSignal) {
    for (size_t z = 0; z < points.size(); ++z) {
      string pre = points[z];
      float xs = points_xsec[z];
      MakeSignalModel(Form("data8tev/%s_bmu.txt", pre.c_str()), "bmu", pre.c_str(), xs);
      MakeSignalModel(Form("data8tev/%s_be.txt", pre.c_str()), "be", pre.c_str(), xs);
      MakeSignalModel(Form("data8tev/%s_rmu.txt", pre.c_str()), "rmu", pre.c_str(), xs);
      MakeSignalModel(Form("data8tev/%s_re.txt", pre.c_str()), "re", pre.c_str(), xs);
    }
  }

  if (fitBkg) {
    MakeBkgModel("data/ttbar_bmu.root", "bmu", 20e3);
    MakeBkgModel("data/ttbar_be.root", "be", 20e3);
    MakeBkgModel("data/ttbar_rmu.root", "rmu", 20e3);
    MakeBkgModel("data/ttbar_re.root", "re", 20e3);
  }

  vector<Results> res;
  if (makeWorkspace) {
    for (size_t z = 0; z < points.size(); ++z) {
      vector<string> vws;
      vector<string> vwb;
      vector<string> vchannel;
      vector<string> vfs;
      vector<string> vfb;

      vws.push_back(Form("%s/workspace_sig_bmu_%s.root", outputDir.c_str(), points[z].c_str()));
      vwb.push_back(Form("%s/workspace_bkg_bmu.root", outputDir.c_str()));
      vchannel.push_back("bmu");

      vws.push_back(Form("%s/workspace_sig_be_%s.root", outputDir.c_str(), points[z].c_str()));
      vwb.push_back(Form("%s/workspace_bkg_be.root", outputDir.c_str()));
      vchannel.push_back("be");
  
      vws.push_back(Form("%s/workspace_sig_rmu_%s.root", outputDir.c_str(), points[z].c_str()));
      vwb.push_back(Form("%s/workspace_bkg_rmu.root", outputDir.c_str()));
      vchannel.push_back("rmu");

      vws.push_back(Form("%s/workspace_sig_re_%s.root", outputDir.c_str(), points[z].c_str()));
      vwb.push_back(Form("%s/workspace_bkg_re.root", outputDir.c_str()));
      vchannel.push_back("re");

 
      for (size_t y = 0; y < vchannel.size(); ++y) {
        vfs.push_back(Form("data8tev/%s_%s.txt", points[z].c_str(), vchannel[y].c_str()));
        vfb.push_back(Form("data/ttbar_%s.root",                       vchannel[y].c_str()));
      }
      float xs = points_xsec[z];
      if (_injMu == 0) xs = 0;
      MakeSBModel(vws, vwb, vchannel, points[z], vfs, vfb, 20e3, xs, _sigSyst, _sigShapeSyst);
      if (doLimit) {
        res.push_back(Limits(Form("%s/jointModel_%s.root", outputDir.c_str(), points[z].c_str()), points[z], vfb, vfs, vchannel, _injMu*xs));
      }
    }
  }


  if (doLimit) {
    ofstream limit(Form("%s/limit.txt", outputDir.c_str()));
    for (size_t z = 0; z < points.size(); ++z) {
      limit << points[z] << "   " << points_n[z] << "    " << points_xsec[z] << "    " << res[z].mumax << "    " << std::fabs(res[z].mumax - res[z].mumax_up) << "    " << std::fabs(res[z].mumax - res[z].mumax_dw) << "    " << std::fabs(res[z].mumax - res[z].mumax2_up) << "    " << std::fabs(res[z].mumax - res[z].mumax2_dw) << "     " << res[z].mumax_obs << "    " << res[z].p << "    " << res[z].expP << endl;
    }
    limit.close();

    TCanvas *clim = new TCanvas("clim", "", 800, 600);
    TH1F *h = new TH1F("h", "", 50, 0, 5.0);
    h->GetYaxis()->SetRangeUser(1e-3, 60);
    h->GetYaxis()->SetTitle("95\% CL upper limit on #sigma #times BR [pb]");
    h->GetXaxis()->SetTitle("m_{Z'} [TeV]");
    h->Draw("hist");
    TGraph *xsec = new TGraph(points.size());
    TGraph *nom = new TGraph(points.size());
    TGraph *obs = new TGraph(points.size());
    TGraphAsymmErrors *sigma1 = new TGraphAsymmErrors(points.size());
    for (size_t z = 0; z < points.size(); ++z) {
      sigma1->SetPoint(z, points_n[z], res[z].mumax*points_xsec[z]);
      nom->SetPoint(z, points_n[z], res[z].mumax*points_xsec[z]);
      obs->SetPoint(z, points_n[z], res[z].mumax_obs*points_xsec[z]);
      xsec->SetPoint(z, points_n[z], points_xsec[z]);
      sigma1->SetPointError(z, 0, 0, res[z].mumax_dw*points_xsec[z], res[z].mumax_up*points_xsec[z]);
    }
    TGraphAsymmErrors *sigma2 = new TGraphAsymmErrors(points.size());
    for (size_t z = 0; z < points.size(); ++z) {
      sigma2->SetPoint(z, points_n[z], res[z].mumax*points_xsec[z]);
      sigma2->SetPointError(z, 0, 0, res[z].mumax2_dw*points_xsec[z], res[z].mumax2_up*points_xsec[z]);
    }
  
    nom->SetLineWidth(2);
    nom->SetLineStyle(kDashed);
    obs->SetLineWidth(2);
    nom->SetMarkerStyle(20);
    obs->SetMarkerStyle(20);
    nom->SetMarkerSize(1.0);
    obs->SetMarkerSize(1.0);
    obs->SetMarkerColor(kRed);
    xsec->SetLineWidth(3);
    xsec->SetLineColor(kRed);
    sigma2->SetFillStyle(1001);
    sigma2->SetFillColor(5);
    sigma2->SetLineColor(5);
    sigma2->SetMarkerColor(5);
    sigma1->SetFillStyle(1001);
    sigma1->SetFillColor(3);
    sigma1->SetLineColor(kBlack);
    sigma2->Draw("E3");
    sigma1->Draw("E3");
    nom->Draw("LP");
    obs->Draw("LP");
    xsec->Draw("LP");
    TLegend *l = new TLegend(0.52,0.6,0.9,0.9);
    l->AddEntry(obs, "Observed CLs", "L");
    l->AddEntry(nom, "Expected CLs", "L");
    l->AddEntry(sigma1, "Expected CLs #pm 1 #sigma", "F");
    l->AddEntry(sigma2, "Expected CLs #pm 2 #sigma", "F");
    l->AddEntry(xsec, "Z' cross section", "L");
    l->SetFillColor(0);
    l->SetFillStyle(0);
    l->SetBorderSize(0);
    l->Draw();
    clim->SetLogy();

    clim->SaveAs(Form("%s/lim_zp.eps", outputDir.c_str()));
    clim->SaveAs(Form("%s/lim_zp.C", outputDir.c_str()));

    for (size_t z = 0; z < points.size(); ++z) {
      std::cout << "Signal point: " << points[z] << ", mumax_obs = " << res[z].mumax_obs << ", mumax = " << res[z].mumax << " + " << res[z].mumax_up << " - " << res[z].mumax_dw << " + " << res[z].mumax2_up << " - " << res[z].mumax2_dw  << ", p = " << res[z].p << ", expP = " << res[z].expP << std::endl;
    }

    TCanvas *cp = new TCanvas("cp", "", 800, 600);
    TH1F *hp = new TH1F("hp", "", 60, 0, 3.0);
    hp->GetYaxis()->SetRangeUser(1e-7, 1);
    hp->GetYaxis()->SetTitle("p_{0}");
    hp->GetXaxis()->SetTitle("m_{Z'} [TeV]");
    hp->GetXaxis()->SetTitleSize(0.05);
    hp->GetYaxis()->SetTitleSize(0.05);
    hp->GetXaxis()->SetTitleFont(42);
    hp->GetYaxis()->SetTitleFont(42);
    hp->GetXaxis()->SetTitleOffset(0.7);
    hp->GetYaxis()->SetTitleOffset(0.7);
    hp->Draw("hist");
    TGraph *gp = new TGraph(points.size());
    TGraph *gpe = new TGraph(points.size());
    for (size_t z = 0; z < points.size(); ++z) {
      gp->SetPoint(z, points_n[z], res[z].p);
      gpe->SetPoint(z, points_n[z], res[z].expP);
    }
    gp->SetLineColor(kBlack);
    gp->SetLineWidth(2);
    gp->SetMarkerStyle(20);
    gp->Draw("PL");
    gpe->SetLineColor(kRed);
    gpe->SetLineWidth(2);
    gpe->SetLineStyle(kDashed);
    gpe->SetMarkerStyle(20);
    gpe->Draw("L");
    cp->SetLogy();
    cp->SetGridy();
    TLegend leg(0.5,0.2,0.9,0.3);
    leg.SetFillStyle(0);
    leg.SetBorderSize(0);
    leg.AddEntry(gp, "Observed p-value", "LP");
    leg.AddEntry(gpe, "Expected p-value", "L");
    leg.Draw();
    TLine *ls[5];
    TLatex latex;
    latex.SetTextSize(0.05);
    for (size_t z = 0; z < 5 ; ++z) {
      ls[z] = new TLine(0, 1-TMath::Erf((z+1.0)/TMath::Sqrt(2)), hp->GetXaxis()->GetBinUpEdge(hp->GetNbinsX()), 1-TMath::Erf((z+1.0)/TMath::Sqrt(2)));
      ls[z]->SetLineStyle(kDashed);
      ls[z]->SetLineWidth(2);
      ls[z]->Draw();
      latex.SetNDC(0);
      latex.DrawLatex(hp->GetXaxis()->GetBinUpEdge(hp->GetNbinsX())*1.01, (1-TMath::Erf((z+1.0)/TMath::Sqrt(2)))*0.98, Form("%d #sigma", (int) z+1));
    }
    cp->SaveAs(Form("%s/hypo_zp.eps", outputDir.c_str()));
    cp->SaveAs(Form("%s/hypo_zp.C", outputDir.c_str()));
  }

  return 0;
}

