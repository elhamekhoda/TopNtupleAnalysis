#ifndef UTILS_H
#define UTILS_H

#include "SampleSet.h"
#include "SystematicCalculation.h"

#include "TStyle.h"
#include "TGraphErrors.h"
#include <memory>

void dumpTrace();
void handler(int sig);

extern int _stamp;
extern std::map<std::string, std::string> name;
extern std::map<std::string, std::pair<std::string, std::string> > syst;
extern float lumi_scale;

void loadConfig(const std::string &file = "config.txt");

shared_ptr<TGraphErrors> TH1toGraph(TH1D *Data);
SampleSetConfiguration makeConfigurationPlots(const string &prefix, const string &channel, bool isMcOnly = false);
SampleSetConfiguration makeConfigurationPlotsCompare(const string &prefix, const string &channel, const vector<string> &other, const vector<string> &title);
SampleSetConfiguration makeConfigurationMCEff(const string &prefix, const string &channel);
SampleSetConfiguration makeConfigurationDataEff(const string &prefix, const string &channel);
void addAllSystematics(SystematicCalculator &systCalc, const std::string &channel);

void split(const std::string &s, char delim, std::vector<std::string> &elems);

void addSystToStat(shared_ptr<TH1D> Data, shared_ptr<TGraphAsymmErrors> band);

void drawDataMC(SampleSetConfiguration &stackConfig, const vector<std::string> &extraText, const std::string &outfile = "plot.eps", bool ratio = true, const std::string &xTitle = "", const std::string &yTitle = "", bool mustBeBigger = false, int posLegend = 0, float yMax = -1, int arrow = 0, double lumi = 5);
void drawDataMCCompare(SampleSetConfiguration &stackConfig, const vector<std::string> &extraText, const std::string &outfile, bool ratio, const std::string &xTitle, const vector<string> &syst_items, const vector<string> &syst_titles, double lumi = 5);
void drawEff(SampleSet *ssMC, const vector<std::string> &extraText, const std::string &outfile = "eff.eps", const std::string &yTitle = "", SampleSet *ssData = 0, bool mcError = false, int mustBeBigger = 0, float yMax = -1, const std::string &xTitle = "", SampleSet *ssRatRat = 0, double lumi = 5);

TStyle *AtlasStyle();
void stampText(const std::string &text, float x, float y, float size = 0.06);
void stampLumi(float lumi, float x, float y);
void stampATLAS(const std::string &text, float x, float y, bool hasRatio = true);
void stampLumiText(float lumi, float x, float y, const std::string &text, float size = 0.06);

shared_ptr<TGraphErrors> normaliseBand(shared_ptr<TGraphErrors> band, TH1D *MC_sum);
shared_ptr<TGraphErrors> normaliseBandFkr(shared_ptr<TGraphErrors> band, TH1D *MC_sum, TH1D *Data);
shared_ptr<TH1D> normaliseBand(shared_ptr<TH1D> band, TH1D *MC_sum);

void drawCompare(SampleSetConfiguration &stackConfig, const vector<std::string> &extraText, const std::string &outfile, bool ratio, double lumi);

#endif

