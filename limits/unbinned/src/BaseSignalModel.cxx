#include <string>
#include "BaseSignalModel.h"
#include <fstream>
#include <iostream>
#include <map>
#include "Models.h"
#include "RooExtendPdf.h"
#include "RooWorkspace.h"
#include "RooRealVar.h"
#include <vector>
#include "RooAbsPdf.h"
#include "RooRealVar.h"
#include "RooFormulaVar.h"
#include "RooConstVar.h"

#include <sstream>


using namespace std;
using namespace RooFit;

BaseSignalModel::BaseSignalModel(const std::string &name, double xsec, double param, const std::string &channel, const std::string &syst,
                                RooWorkspace *work)
  : m_name(name), m_xsec(xsec), m_param(param), m_channel(channel), m_syst(syst), m_work(work) {

  m_p["norm"] = new RooRealVar(Form("norm_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "norm", 20, 0, 1000);     // signal expected number of events
  m_nsig_mu = new RooFormulaVar(Form("nsig_mu_%s_%s_%s", name.c_str(), channel.c_str(), syst.c_str()), "@0*@1", RooArgList(*m_p["norm"], *work->var("mu")));
}

BaseSignalModel::~BaseSignalModel() {
}

void BaseSignalModel::saveParameters(const std::string &file) {
  ofstream o(file.c_str());
  o << m_name << "  " << m_xsec << "  " << m_param << "  " << m_channel << "  " << m_syst << std::endl;
  for (std::map<std::string, RooRealVar *>::iterator it = m_p.begin(); it != m_p.end(); ++it) {
    o << it->first << "  " << it->second->getVal() << std::endl;
  }
  o.close();
}

void BaseSignalModel::readParameters(const std::string &file) {
  ifstream o(file.c_str());
  std::string line;
  std::getline(o, line, '\n');
  std::stringstream ssf(line);
  ssf >> m_name;
  ssf >> m_xsec;
  ssf >> m_param;
  ssf >> m_channel;
  ssf >> m_syst;
  while (std::getline(o, line, '\n')) {
    std::stringstream ss(line);
    std::string n;
    double x;
    if (!(ss >> n >> x)) { break; }
    m_p[n]->setVal(x);
  }
}

RooAbsPdf *BaseSignalModel::getPdf(){
  return m_pdf;
}

RooRealVar *BaseSignalModel::param(const std::string &n) {
  return m_p[n];
}

RooFormulaVar *BaseSignalModel::systParam(const std::string &n) {
  return m_syst_param[n];
}

void BaseSignalModel::getParamWithSystematics(std::vector<RooRealVar *> &alpha, std::vector<std::string> &systs, std::map<std::string, BaseSignalModel *> &models, std::map<std::string, std::map<std::string, double> > &delta_p) {
  m_syst_param.clear();
  for (std::map<std::string, RooRealVar *>::iterator it = m_p.begin(); it != m_p.end(); ++it) {
    std::string n = it->first;

    delta_p[n] = std::map<std::string, double>();

    std::stringstream listForFormula;
    int count = 0;
    std::vector<double> widths;
    std::vector<double> list_mu;
    std::vector<double> list_sigma;
    listForFormula << "(1";
    for (size_t z = 1; z < systs.size(); ++z) {
      double delta = (models[Form("%s_%s_%s", m_name.c_str(), m_channel.c_str(), systs[z].c_str())]->param(n)->getVal() - param(n)->getVal());
      std::cout << "delta_p(" << n << ", " << systs[z] << ") = " << delta << std::endl;
      if (models.find(Form("%s_%s_%sdw", m_name.c_str(), m_channel.c_str(), systs[z].c_str())) != models.end()) {
        double deltadw = (models[Form("%s_%s_%sdw", m_name.c_str(), m_channel.c_str(), systs[z].c_str())]->param(n)->getVal() - param(n)->getVal());
        if (std::fabs(deltadw) > std::fabs(delta)) {
          delta = deltadw;
        }
      }
      if (param(n)->getVal() != 0) delta /= param(n)->getVal();
      delta_p[n][systs[z]] = delta;

      //double m = 1; // mean of log-normal
      //double v = std::fabs(delta); // std. dev. of log normal;
      //double mu = std::log(m/std::sqrt(1+v/(m*m)));
      //double sigma = std::sqrt(std::log(1+v/(m*m)));
      // alpha is Gaussian with mean 0 and sigma = 1
      // exp(mu + sigma*alpha) is log-normal with mean 1 and variance delta^2
      //listForFormula << "*exp(@" << count << " + @" << count+1 << "*@" << count+2 << ")";
      //count = count + 3;
      //list_mu.push_back(mu);
      //list_sigma.push_back(sigma);

      // for a Gaussian
      listForFormula << " + @" << count << "*@" << count+1;
      widths.push_back(delta);
      count = count + 2;
    }
    listForFormula << ")*@" << count;
    RooArgList list_m;
    for (size_t z = 1; z < systs.size(); ++z) {
      list_m.add(RooConst(widths[z-1]));
      //list_m.add(RooConst(list_mu[z-1]));
      //list_m.add(RooConst(list_sigma[z-1]));

      double mymax = alpha[z-1]->getMax();
      double mymin = alpha[z-1]->getMin();
      double current_max = alpha[z-1]->getMax();
      double current_min = alpha[z-1]->getMin();
      if (widths[z-1] != 0 && m_p[n]->getVal() != 0) {
        alpha[z-1]->setMax("",  1000);
        alpha[z-1]->setMin("", -1000);

        mymax = (m_p[n]->getMax() - m_p[n]->getVal())/(m_p[n]->getVal()*widths[z-1]);
        if (mymax > 1.0) mymax = 1.0;
        if (mymax < 0) mymax = 0.1;
        alpha[z-1]->setMax("", mymax);
        mymin = (m_p[n]->getMin() - m_p[n]->getVal())/(m_p[n]->getVal()*widths[z-1]);
        if (mymin < -1.0) mymin = -1.0;
        if (mymin > 0) mymin = -0.1;
        alpha[z-1]->setMin("", mymin);
      }
      list_m.add(*alpha[z-1]);
    }
    list_m.add(RooConst(m_p[n]->getVal()));
    m_syst_param[n] = new RooFormulaVar(Form("f%s_%s", n.c_str(), m_channel.c_str()), listForFormula.str().c_str(), list_m);
  }
}

