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
    string prefix = "boosted";
    string channel = "mu";
    string h_input = "lepPt";
    string h_other = "";
    string h_titles = "";
    string h_syst = "";
    string h_systTitles = "";
    string _outfile = "";
    int underflow = 0;
    string _extraText = "";
    string yTitle = "";
    string xTitle = "";
    float xMax = -9999;
    float xMin = -9999;
    float lumi = 5;
    std::string config = "";

    static struct extendedOption extOpt[] = {
        {"help",            no_argument,       &help,   1, "Display help", &help, extendedOption::eOTInt},
        {"channel",         required_argument,     0, 'c', "Channel: one of e, mu, comb.", &channel, extendedOption::eOTString},
        {"prefix",          required_argument,     0, 'p', "Prefix.", &prefix, extendedOption::eOTString},
        {"histogram",       required_argument,     0, 'h', "Histogram.", &h_input, extendedOption::eOTString},
        {"other",           required_argument,     0, 'O', "Other file.", &h_other, extendedOption::eOTString},
        {"titles",          required_argument,     0, 'z', "Other titles.", &h_titles, extendedOption::eOTString},
        {"syst",            required_argument,     0, 's', "Systematics list.", &h_syst, extendedOption::eOTString},
        {"systTitles",      required_argument,     0, 'S', "Systematic list titles.", &h_systTitles, extendedOption::eOTString},
        {"outfile",         required_argument,     0, 'o', "Output file.", &_outfile, extendedOption::eOTString},
        {"underflow",       required_argument,     0, 'U', "Include underflow (0/1)", &underflow, extendedOption::eOTInt},
        {"extraText",       required_argument,     0, 'T', "Extra text to add in the plot.", &_extraText, extendedOption::eOTString},
        {"yTitle",          required_argument,     0, 'y', "Y title.", &yTitle, extendedOption::eOTString},
        {"xTitle",          required_argument,     0, 't', "X title.", &xTitle, extendedOption::eOTString},
        {"xMax",            required_argument,     0, 'X', "Limit X maximum value.", &xMax, extendedOption::eOTFloat},
        {"xMin",            required_argument,     0, 'x', "Limit X minimum value.", &xMin, extendedOption::eOTFloat},
        {"lumi",            required_argument,     0, 'l', "Luminosity value to show.", &lumi, extendedOption::eOTFloat},
        {"config",          required_argument,     0, 'C', "Configuration file.", &config, extendedOption::eOTString},

        {0, 0, 0, 0, 0, 0, extendedOption::eOTInt}
      };

    
    if (!parseArguments(argc, argv, extOpt) || help) {
      dumpHelp("plotCompareNominal", extOpt, "plot\nCalculate systematic uncertainties and make histograms with them.\n");
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

    std::string histogram = "";
    histogram = h_input;

    vector<string> other_items;
    split(h_other, ',', other_items);

    vector<string> other_titles;
    split(h_titles, ',', other_titles);

    vector<string> syst_items;
    split(h_syst, ',', syst_items);

    vector<string> syst_titles;
    split(h_systTitles, ',', syst_titles);

    cout.setf(ios::fixed, ios::floatfield);
    cout.precision(1);

    // for Data/MC comparison
    SampleSetConfiguration stackConfig = makeConfigurationPlotsCompare(prefix, channel, other_items, other_titles);
    SystematicCalculator systCalc(stackConfig);
    for (int z = 0; z < syst_items.size(); ++z) {
      systCalc.add(syst_items[z], new NotData(new HistDiff(syst_items[z].c_str(), "")));
    }
    //addAllSystematics(systCalc, channel, false);
    systCalc.calculate(histogram);

    if (underflow) stackConfig.showUnderflow();
    if (xMax > -998.0) stackConfig.limitMaxX(xMax);
    if (xMin > -998.0) stackConfig.limitMinX(xMin);

    cout << "Yields:" << endl << endl;
    systCalc.printYields(stackConfig);
  
    vector<string> extraText;
    string outfile = _outfile;
    if (outfile == "") {
      outfile = histogram+string("_");
      if (channel == "e.root") {
        outfile += "e.pdf";
      } else if (channel == "mu.root") {
        outfile += "mu.pdf";
      } else if (channel == "comb.root") {
        outfile += "comb.pdf";
      } else {
        outfile += "ukn.pdf";
      }
    }
    if (channel == "e.root") {
      extraText.push_back("e channel");
    } else if (channel == "mu.root") {
      extraText.push_back("#mu channel");
    } else if (channel == "comb.root") {
      extraText.push_back("e,#mu-channel");
    }
    vector<string> split_extraText;
    split(_extraText, ';', split_extraText);
    for (vector<string>::iterator i = split_extraText.begin(); i!=split_extraText.end();++i) extraText.push_back(*i);
    drawDataMCCompare(stackConfig, extraText, outfile, true, xTitle, syst_items, syst_titles, lumi);
  } catch (string s) {
    cout << "Crashed with exception: " << s << endl;
    dumpTrace();
  }

  return 0;
}
