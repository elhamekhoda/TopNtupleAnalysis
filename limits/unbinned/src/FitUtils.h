#ifndef _FITUTILS_H
#define _FITUTILS_H

#include <fstream>
#include <sstream>
#include <iomanip>
#include <string>
#include <map>
#include <vector>

#include "RooCategory.h"
#include "RooWorkspace.h"
#include "RooRealVar.h"
#include "RooDataSet.h"

#include "RooStats/ModelConfig.h"
#include "RooNLLVar.h"
#include "RooFitResult.h"

#include "Models.h"

extern std::string outputDir;

class Results {
  public:
    double mumax;
    double mumax_dw;
    double mumax_up;
    double mumax2_dw;
    double mumax2_up;
    double p;
    double expP;
    double mumax_obs;
    Results ();
    Results(double a, double b, double c, double d, double e, double f, double g, double h);
};

RooDataSet *readData(const std::string &file, int channels_hist, const std::string &syst, RooWorkspace *work, double extraWeight = 1.0, bool useCat = false);
void readData(RooDataSet *data, const std::string &file, int channels_hist, const std::string &syst, RooWorkspace *work, double extraWeight = 1.0, bool useCat = false);

int minimizeFancy(RooAbsReal* fcn, RooFitResult **fr);
int minimizeFancy(RooNLLVar* nll, RooFitResult **fr);

double load(const char *file, RooDataSet *data, \
            RooRealVar &x, RooRealVar &w, \
            double extraWeight = 1.0, RooCategory *idx = 0);
void MakeBkgModel(const char *bkgfile, const char *channel, double extraWeight = 1.0);
void MakeSignalModel(const char *sigfile, const char *channel, const char *sigpoint, double extraW = 1);
RooDataSet * fitSignal(RooAbsPdf *sig, const std::string &sigfile, RooRealVar &x, RooRealVar &w, double &yield, double extraW = 1, const std::string &mode = "zp1tev", const std::string &channel = "bmu");
double lnmuLogNormal(double mean, double sigma);
double lnkLogNormal(double mean, double sigma);
void MakeSBModel(std::vector<std::string> &vws, std::vector<std::string> &vwb, std::vector<std::string> &vchannel, const std::string &mode, \
                 std::vector<std::string> &vfs, std::vector<std::string> &vfb, double bkgW, double sigW, double sigSyst, double sigShapeSyst);

int minimize(RooNLLVar* nll, RooFitResult *&res);
void getSignificance(RooDataSet *data, RooStats::ModelConfig *sbModel, RooWorkspace *w, double &pnull, double &palt, double &pnullA, bool discovery = true, double mu = 0);

double getTransition(double y, std::vector<double> &ylist, std::vector<double> &xlist);

Results Limits(const char *mfile, const std::string &mode,
               std::vector<std::string> &vfb, std::vector<std::string> &vfs, std::vector<std::string> &vchannel, double injMu = 0);

#endif

