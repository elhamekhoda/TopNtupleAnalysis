#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <cmath>
#include <memory>
#include <algorithm>
#include <iterator>

#include "TFile.h"
#include "TH1F.h"
#include "TH1.h"

#include <iomanip>
#include <sstream>

#include <signal.h>

#include "Hist.h"
#include "SystematicImplementation.h"
#include "utils.h"
#include "SampleSet.h"
#include "SystematicCalculation.h"

#include "ParseUtils.h"

#include "TCanvas.h"
#include "TH1D.h"
#include "TH1.h"
#include "TH1F.h"
#include "THStack.h"
#include "TGraphErrors.h"

using namespace std;

int main(int argc, char **argv) {
  signal(SIGSEGV, handler);

  try {

    int help = 0;
    string channel = "e";
    string prefix = "boosted";
    string h_input = "lepPt";
    int mcOnly = 0;
    string _outfile = "";
    int verbose = 0;
    int underflow = 0;
    string _extraText = "boosted";
    string yTitle = "";
    string xTitle = "";
    float xMax = -9999;
    float xMin = -9999;
    int mustBeBigger = 0;
    int posLegend = 0;
    int rebin = 1;
    float yMax = -1;
    int arrow = 0;
    int stamp = 0;
    float lumi = 5;
    std::string config = "";

    static struct extendedOption extOpt[] = {
        {"help",            no_argument,       &help,   1, "Display help", &help, extendedOption::eOTInt},
        {"channel",         required_argument,     0, 'c', "Channel: one of e, mu, comb", &channel, extendedOption::eOTString},
        {"prefix",          required_argument,     0, 'p', "Prefix.", &prefix, extendedOption::eOTString},
        {"histogram",       required_argument,     0, 'h', "Histogram name.", &h_input, extendedOption::eOTString},
        {"mcOnly",          required_argument,     0, 'm', "Only look for the ttbarMatched histograms? (0/1)", &mcOnly, extendedOption::eOTInt},
        {"outfile",         required_argument,     0, 'o', "Output file.", &_outfile, extendedOption::eOTString},
        {"verbose",         required_argument,     0, 'v', "Verbose. (0/1)", &verbose, extendedOption::eOTInt},
        {"underflow",       required_argument,     0, 'U', "Include underflow (0/1)", &underflow, extendedOption::eOTInt},
        {"extraText",       required_argument,     0, 'T', "Extra text to add in the plot.", &_extraText, extendedOption::eOTString},
        {"yTitle",          required_argument,     0, 'y', "Y title.", &yTitle, extendedOption::eOTString},
        {"xTitle",          required_argument,     0, 't', "X title.", &xTitle, extendedOption::eOTString},
        {"xMax",            required_argument,     0, 'X', "Limit X maximum value.", &xMax, extendedOption::eOTFloat},
        {"xMin",            required_argument,     0, 'x', "Limit X minimum value.", &xMin, extendedOption::eOTFloat},
        {"mustBeBigger",    required_argument,     0, 'M', "Widen range of the Y axis in the ratio plots.", &mustBeBigger, extendedOption::eOTInt},
        {"posLegend",       required_argument,     0, 'L', "Move legend to the left.", &posLegend, extendedOption::eOTInt},
        {"rebin",           required_argument,     0, 'r', "Rebin by this factor.", &rebin, extendedOption::eOTInt},
        {"yMax",            required_argument,     0, 'Y', "Maximum of the Y axis.", &yMax, extendedOption::eOTFloat},
        {"arrow",           required_argument,     0, 'a', "Draw arrow.", &arrow, extendedOption::eOTInt},
        {"stamp",           required_argument,     0, 's', "0 = ATLAS Internal, 1 = ATLAS Preliminary.", &stamp, extendedOption::eOTInt},
        {"lumi",            required_argument,     0, 'l', "Luminosity value to show", &lumi, extendedOption::eOTFloat},
        {"config",          required_argument,     0, 'C', "Configuration file for items.", &config, extendedOption::eOTString},

        {0, 0, 0, 0, 0, 0, extendedOption::eOTInt}
      };

    
    if (!parseArguments(argc, argv, extOpt) || help) {
      dumpHelp(std::string(argv[0]), extOpt, "plot\nCalculate systematic uncertainties and make histograms with them.\n");
      return 0;
    } else {
      std::cout << "Dumping options:" << std::endl;
      dumpOptions(extOpt);
    }

    lumi_scale = lumi;
    if (config != "")
      loadConfig(config.c_str());
    else
      loadConfig(std::string(argv[0]).substr(0, std::string(argv[0]).rfind('/'))+"/config.txt");

    _stamp = stamp;

    vector<string> h_items;
    split(h_input, '/', h_items);
    bool isRatio = false;
    std::string histogram = "";
    string histogram_num = "";
    string histogram_den = "";
    if (h_items.size() == 1) 
      histogram = h_items[0];
    else {
      histogram_num = h_items[0];
      histogram_den = h_items[1];
      isRatio = true;
    }

    cout.setf(ios::fixed, ios::floatfield);
    cout.precision(1);

    if (!isRatio) {
      // for Data/MC comparison
      SampleSetConfiguration stackConfig = makeConfigurationPlots(prefix, channel, mcOnly);
      SystematicCalculator systCalc(stackConfig);
      addAllSystematics(systCalc, channel);
      systCalc.calculate(histogram);

      if (underflow) stackConfig.showUnderflow();
      if (xMax > -998.0) stackConfig.limitMaxX(xMax, true);
      if (xMin > -998.0) stackConfig.limitMinX(xMin);
      if (rebin != 1) stackConfig.rebin(rebin);

      if (verbose) {
        systCalc.printBigTable(stackConfig);
      }
      cout << "Systematic uncertainties:" << endl << endl;
      systCalc.printSysts(stackConfig["MC"]);
      cout << "Yields:" << endl << endl;
      systCalc.printYields(stackConfig);
  
      vector<string> extraText;
      string outfile = _outfile;
      if (outfile == "") {
        outfile = prefix+"_"+histogram;
        outfile += string("_");
        if (channel == "e") {
          outfile += "e";
        } else if (channel == "mu") {
          outfile += "mu";
        } else if (channel == "comb") {
          outfile += "comb";
        } else {
          outfile += "ukn";
        }
        if (stamp == 1) outfile += "_ATLASPrelim";
        if (stamp == 2) outfile += "_ATLAS";
        outfile += ".pdf";
      }
      if (channel == "e") {
        extraText.push_back("e channel");
      } else if (channel == "mu") {
        extraText.push_back("#mu channel");
      } else if (channel == "comb") {
        //extraText.push_back("e,#mu-channel");
      }
      vector<string> split_extraText;
      split(_extraText, ';', split_extraText);
      for (vector<string>::iterator i = split_extraText.begin(); i!=split_extraText.end();++i) extraText.push_back(*i);
      drawDataMC(stackConfig, extraText, outfile, true, xTitle, yTitle, mustBeBigger, posLegend, yMax, arrow, lumi);

    } else { // if it is a ratio plot

      shared_ptr<SystematicRatioCalculator> systRatCalcD;
      shared_ptr<SystematicRatioCalculator> systRatCalc;
      shared_ptr<SystematicRatioCalculator> systRatCalcMCAtNLO;
      shared_ptr<SystematicRatioRatioCalculator> systRatRatCalc;
      shared_ptr<SystematicRatioRatioCalculator> systRatRatCalcMCAtNLO;

      if (!mcOnly) {
        // for data eff. numerator
        SampleSetConfiguration stackConfigNumD = makeConfigurationDataEff(prefix, channel);
        SystematicCalculator systCalcNumD(stackConfigNumD);
        addAllSystematics(systCalcNumD, channel);

        systCalcNumD.calculate(histogram_num);

        if (xMax > -998.0) stackConfigNumD.limitMaxX(xMax);
        if (xMin > -998.0) stackConfigNumD.limitMinX(xMin);

        if (verbose) {
          cout << "Data numerator systs.:" << endl << endl;
          systCalcNumD.printSysts(stackConfigNumD["MC"]);
          cout << "Data numerator yields:" << endl << endl;
          systCalcNumD.printYields(stackConfigNumD);
        }

        // for data eff. denominator
        SampleSetConfiguration stackConfigDenD = makeConfigurationDataEff(prefix, channel);
        SystematicCalculator systCalcDenD(stackConfigDenD);
        addAllSystematics(systCalcDenD, channel);
  
        systCalcDenD.calculate(histogram_den);

        if (xMax > -998.0) stackConfigDenD.limitMaxX(xMax);
        if (xMin > -998.0) stackConfigDenD.limitMinX(xMin);

        if (verbose) {
          cout << "Data denominator systs.:" << endl << endl;
          systCalcDenD.printSysts(stackConfigDenD["MC"]);
          cout << "Data denominator yields:" << endl << endl;
          systCalcDenD.printYields(stackConfigDenD);
        }

        // calculate ratio
        systRatCalcD.reset(new SystematicRatioCalculator(systCalcNumD, systCalcDenD));
        systRatCalcD->calculate(histogram_num, histogram_den, true);
  
        cout << "Systematic uncertainties for data eff.:" << endl << endl << endl;
        cout.precision(3);
        cout << "Ratio nominal in data:" << systRatCalcD->_sr["Ratio"]._item[0].nominal << endl;
        cout.precision(1);
        systRatCalcD->printAverageSysts(systRatCalcD->_sr["Ratio"]);

        systRatCalcD->printBinSysts(systRatCalcD->_sr["Ratio"]);
  
      }
  
      // for MC eff. numerator using PP
      SampleSetConfiguration stackConfigNum = makeConfigurationMCEff(prefix, channel);
      SystematicCalculator systCalcNum(stackConfigNum);
      addAllSystematics(systCalcNum, channel);

      systCalcNum.calculate(histogram_num);

      if (xMax > -998.0) stackConfigNum.limitMaxX(xMax);
      if (xMin > -998.0) stackConfigNum.limitMinX(xMin);

      if (verbose) {
        cout << "MC numerator systs. (standard):" << endl << endl;
        systCalcNum.printSysts(stackConfigNum["MC"]);
        cout << "MC numerator yields (standard):" << endl << endl;
        systCalcNum.printYields(stackConfigNum);
      }
  
      // for MC eff. denominator
      SampleSetConfiguration stackConfigDen = makeConfigurationMCEff(prefix, channel);
      SystematicCalculator systCalcDen(stackConfigDen);
      addAllSystematics(systCalcDen, channel);
  
      systCalcDen.calculate(histogram_den);

      if (xMax > -998.0) stackConfigDen.limitMaxX(xMax);
      if (xMin > -998.0) stackConfigDen.limitMinX(xMin);

      if (verbose) {
        cout << "MC denominator systs. (standard):" << endl << endl;
        systCalcDen.printSysts(stackConfigDen["MC"]);
        cout << "MC denominator yields (standard):" << endl << endl;
        systCalcDen.printYields(stackConfigDen);
      }

      // calculate ratio
      systRatCalc.reset(new SystematicRatioCalculator(systCalcNum, systCalcDen));
      systRatCalc->calculate(histogram_num, histogram_den, false);
      cout.precision(3);
      cout << "Ratio nominal in MC (Standard):" << systRatCalc->_sr["Ratio"]._item[0].nominal << endl;
      cout.precision(1);
      cout << "Systematic uncertainties for MC eff. (standard):" << endl << endl << endl;
      systRatCalc->printAverageSysts(systRatCalc->_sr["Ratio"]);

      systRatCalc->printBinSysts(systRatCalc->_sr["Ratio"]);

      systRatRatCalc.reset(new SystematicRatioRatioCalculator(*systRatCalcD.get(), *systRatCalc.get()));
      systRatRatCalc->calculate(histogram_num, histogram_den, false);

      std::cout << "Systematics on ratio of ratio: " << std::endl;
      systRatRatCalc->printBinSysts(systRatRatCalc->_sr["Ratio"]);

      vector<string> extraText;
      vector<string> split_extraText;
      split(_extraText, ';', split_extraText);
      for (vector<string>::iterator i = split_extraText.begin(); i!=split_extraText.end();++i) extraText.push_back(*i);
      string outfile = _outfile;
      if (outfile == "") {
        outfile = string("sf_")+prefix+"_"+histogram_num+string("_")+histogram_den+string("_");
        if (channel == "e") {
          outfile += "e";
        } else if (channel == "mu") {
          outfile += "mu";
        } else if (channel == "comb") {
          outfile += "comb";
        } else {
          outfile += "ukn";
        }
        if (stamp == 1) outfile += "_ATLASPrelim";
        if (stamp == 2) outfile += "_ATLAS";
        outfile += ".pdf";
      }
      if (channel == "e") {
        extraText.push_back("e channel");
      } else if (channel == "mu") {
        extraText.push_back("#mu channel");
      } else if (channel == "comb") {
        //extraText.push_back("e,#mu-channel");
      }
      if (!mcOnly) {
        drawEff(&(systRatCalc->_sr["Ratio"]), extraText, outfile, yTitle, &(systRatCalcD->_sr["Ratio"]), false, mustBeBigger, yMax, xTitle, &(systRatRatCalc->_sr["Ratio"]), lumi);
      } else {
        drawEff(&(systRatCalc->_sr["Ratio"]), extraText, outfile, yTitle, 0, false, mustBeBigger, yMax, xTitle, 0, lumi);
      }
    } // ratio?

  } catch (string s) {
    cout << "Crashed with exception: " << s << endl;
    dumpTrace();
  }

  return 0;
}
