#ifndef SIGNALMODEL_H
#define SIGNALMODEL_H
#include <string>
#include <fstream>
#include "BaseSignalModel.h"
#include "RooAbsPdf.h"
#include "RooRealVar.h"
#include "RooFormulaVar.h"
#include "RooWorkspace.h"
#include "RooDataSet.h"
#include <fstream>


class SignalModel : public BaseSignalModel {
  public:
    SignalModel(const std::string &name, double xsec, double param, const std::string &channel, const std::string &syst,
                RooWorkspace *work);
    virtual ~SignalModel();

    void fit(RooDataSet *data, const std::string &);
    RooAbsPdf *getPdfWithSystematics();

};

#endif

