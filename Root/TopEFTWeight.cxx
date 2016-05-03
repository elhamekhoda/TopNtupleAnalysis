#include <iostream>

#include "TopNtupleAnalysis/TopEFTWeight.h"
#include "TLorentzVector.h"
#include "TMath.h"

#include <map>

#include <cmath>
using namespace std;

TopEFTWeight::TopEFTWeight(double cvv, double lambda) :
    m_cvv(cvv),
    m_caa(0),
    m_cvvp(0),
    m_caap(0),
    m_lambda(lambda)
{
}

TopEFTWeight::~TopEFTWeight() {
}

double TopEFTWeight::m2(TLorentzVector a, TLorentzVector b) {
  return pow(a.E()+b.E(), 2) - pow(a.Px()+b.Px(), 2) - pow(a.Py()+b.Py(), 2) - pow(a.Pz()+b.Pz(), 2);
}

double TopEFTWeight::m2diff(TLorentzVector a, TLorentzVector b) {
  return pow(a.E()-b.E(), 2) - pow(a.Px()-b.Px(), 2) - pow(a.Py()-b.Py(), 2) - pow(a.Pz()-b.Pz(), 2);
}

double TopEFTWeight::alphas(const double scale2) {
  const double mZ2 = std::pow(91.1876, 2);
  const double alphasMZ = 0.118;
  const double nf = 5;
  const double b0 = (33.0 - 2.0*nf)/12.0/TMath::Pi();
  double als = alphasMZ/(1.0 + alphasMZ*b0*std::log(scale2/mZ2));
  return als;
}


std::pair<double, double> TopEFTWeight::getScaleFactor(
        float MC_t_pt,
        float MC_t_eta,
        float MC_t_phi,
        float MC_t_m,
        float MC_tbar_pt,
        float MC_tbar_eta,
        float MC_tbar_phi,
        float MC_tbar_m,
        float MC_i1_px,
        float MC_i1_py,
        float MC_i1_pz,
        float MC_i1_m,
        float MC_i2_px,
        float MC_i2_py,
        float MC_i2_pz,
        float MC_i2_m,
	int   MC_i1_pid,
	int   MC_i2_pid) {
    double w = 1.0;
    double werr = 0.0;

    TLorentzVector top;
    TLorentzVector topbar;
    TLorentzVector i1;
    TLorentzVector i2;
    top.SetPtEtaPhiM(MC_t_pt*1e-3, MC_t_eta, MC_t_phi, MC_t_m*1e-3);
    topbar.SetPtEtaPhiM(MC_tbar_pt*1e-3, MC_tbar_eta, MC_tbar_phi, MC_tbar_m*1e-3);
    double MC_i1_e = sqrt(pow(MC_i1_m, 2) + pow(MC_i1_px, 2) + pow(MC_i1_py, 2) + pow(MC_i1_pz, 2));
    double MC_i2_e = sqrt(pow(MC_i2_m, 2) + pow(MC_i2_px, 2) + pow(MC_i2_py, 2) + pow(MC_i2_pz, 2));
    i1.SetPxPyPzE(MC_i1_px*1e-3, MC_i1_py*1e-3, MC_i1_pz*1e-3, MC_i1_e*1e-3);
    i2.SetPxPyPzE(MC_i2_px*1e-3, MC_i2_py*1e-3, MC_i2_pz*1e-3, MC_i2_e*1e-3);
    bool isGG = false;
    bool isUp = false;
    if (MC_i1_pid == 22 || MC_i1_pid == -22) {
      isGG = true;
    }
    if (MC_i1_pid == 1 || MC_i1_pid == 3 || MC_i1_pid == -1 || MC_i1_pid == -3) {
      isUp = true;
    }
    double pi = TMath::Pi();
    double s = m2(top, topbar);
    double t = m2diff(i1, top);
    double u = m2diff(i1, topbar);
    if (s <= 0 || s != s) {
        std::cout << "getWeight: s < 0 for top pt = " << top.Perp() << ", tbar pt = " << topbar.Perp() << std::endl;
    }
    double alpha_s = alphas(s);
    if (alpha_s <= 0 || alpha_s != alpha_s) {
        std::cout << "getWeight: alpha_s < 0 for top pt = " << top.Perp() << ", tbar pt = " << topbar.Perp() << ", s = " << s << std::endl;
    }
    double gs = std::sqrt(4*pi*alpha_s);
    double m_t = 175.0;
    double v = 246.0;
    double cvV  = m_cvv;
    double cvVp = m_cvvp;
    double caA  = m_caa;
    double caAp = m_caap;
    double tau1 = (pow(m_t, 2) - t)/s;
    double tau2 = (pow(m_t, 2) - u)/s;
    double rho  = 4*pow(m_t, 2)/s;
    double chg = 0;//2*ctg; // for gluon-gluon-t-t vertex

    // using dsigma/dt
    double sigma_qq_tt_SM = 4*pi*pow(alpha_s, 2)/(9*pow(s, 2))*(pow(tau1, 2)+pow(tau2, 2)+rho*0.5);
    double sigma_gg_tt_SM = pi*pow(alpha_s, 2)/pow(s, 2)*(1.0/(6*tau1*tau2) - 3.0/8.0)*(rho + pow(tau1, 2) + pow(tau2, 2) - pow(rho, 2)/(4*tau1*tau2));

    double sign = -1;
    if (isUp) sign = 1;

    double sigma_qq_tt_NP = sigma_qq_tt_SM*(1 + (cvV + sign*cvVp*0.5)/pow(gs, 2)*s/pow(m_lambda, 2)) + alpha_s/(9*pow(s*m_lambda, 2))*((caA+sign*caAp*0.5)*s*(tau2-tau1)+ 4*gs*chg*sqrt(2)*v*m_t);
    double sigma_qq_tt_NP_lambda4 = pow(std::sqrt(sigma_qq_tt_SM), 2)*0.25*pow(cvV + sign*cvVp*0.5, 2)/pow(gs, 4)*pow(s, 2)/pow(m_lambda, 4);
    sigma_qq_tt_NP += sigma_qq_tt_NP_lambda4;

    double sigma_gg_tt_NP = sigma_gg_tt_SM + sqrt(2)*alpha_s*gs*v*m_t/pow(s, 2)*chg/pow(m_lambda, 2)*(1.0/(6*tau1*tau2) - 3.0/8.0);

    if (isGG) {
        w = sigma_gg_tt_NP/sigma_gg_tt_SM;
        werr = 0.05*w; // arbitrary
    } else {
        w = sigma_qq_tt_NP/sigma_qq_tt_SM;
        werr = sigma_qq_tt_NP_lambda4;
    }

    return std::pair<double, double>(w, werr);
}

