#ifndef BASESIGNALMODEL_H
#define BASESIGNALMODEL_H
#include <string>
#include <fstream>
#include "RooAbsPdf.h"
#include "RooRealVar.h"
#include "RooFormulaVar.h"
#include "RooWorkspace.h"
#include "RooDataSet.h"
#include <fstream>
#include <map>
#include <vector>

class BaseSignalModel {
  public:
    BaseSignalModel(const std::string &name, double xsec, double param, const std::string &channel, const std::string &syst,
                    RooWorkspace *work);
    virtual ~BaseSignalModel();

    virtual void fit(RooDataSet *data, const std::string &outdir) = 0;
    void saveParameters(const std::string &file);
    void readParameters(const std::string &file);
    RooAbsPdf *getPdf();
    RooRealVar *param(const std::string &n);
    RooFormulaVar *systParam(const std::string &n);
    void getParamWithSystematics(std::vector<RooRealVar *> &alpha, std::vector<std::string> &systs, std::map<std::string, BaseSignalModel *> &models, std::map<std::string, std::map<std::string, double> > &delta_p);
    virtual RooAbsPdf *getPdfWithSystematics() = 0;
    const std::map<std::string, RooRealVar *> &p() const { return m_p; }

    RooFitResult *m_fr;
    double m_param;


  protected:
    std::string m_name;
    double m_xsec;
    std::string m_channel;
    std::string m_syst;
    RooWorkspace *m_work;

    std::map<std::string, RooRealVar *> m_p;

    RooFormulaVar *m_nsig_mu;
    RooAbsPdf *m_pdf;

    std::map<std::string, RooFormulaVar *> m_syst_param;

};

#endif

