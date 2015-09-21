#ifndef BKGMODEL_H
#define BKGMODEL_H

#include <string>
#include <fstream>
#include "BaseSignalModel.h"
#include "RooAbsPdf.h"
#include "RooRealVar.h"
#include "RooFormulaVar.h"
#include "RooWorkspace.h"
#include "RooDataSet.h"
#include <fstream>


class BkgModel : public BaseSignalModel {
  public:
    BkgModel(const std::string &name, double xsec, double param, const std::string &channel, const std::string &syst,
                RooWorkspace *work);
    virtual ~BkgModel();

    void fit(RooDataSet *data, const std::string &outdir);
    RooAbsPdf *getPdfWithSystematics();

};

#endif

