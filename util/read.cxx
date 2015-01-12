/**
 * @brief Main executable to run over input mini flat ntuples,
 * read events in an object-oriented way and
 * run the event analysis class that derives from Analysis.
 * The main objective is to be minimal and to allow users to run this part
 * of the code in their laptops.
 *
 * @author Danilo Enoque Ferreira de Lima <dferreir@mail.cern.ch>
 */

#include "TopNtupleAnalysis/Event.h"
#include "TChain.h"
#include "TopNtupleAnalysis/MiniTree.h"

#include <iostream>

#include "TopNtupleAnalysis/EventCount.h"

#include "TopNtupleAnalysis/Analysis.h"
#include "TopNtupleAnalysis/AnaTtresSL.h"

#include "TopDataPreparation/SampleXsection.h"
#include "Cintex/Cintex.h"

#include "TopNtupleAnalysis/ParseUtils.h"

#include <fstream>

#include "TROOT.h"
#include "TInterpreter.h"

#include <sstream>

int main(int argc, char **argv) {

  ROOT::Cintex::Cintex::Enable();

  gROOT->ProcessLine("#include <vector>");
  gInterpreter->GenerateDictionary("vector<vector<float> >", "vector");

  initEventCount();

  // input files
  int help = 0;
  int isData = 0;
  int isAtlFastII = 0;
  std::string outFile = "histogram_e.root,histogram_mu.root";
  std::string files = "output.root";
  std::string analysis = "AnaTtresSL";

  static struct extendedOption extOpt[] = {
        {"help",          no_argument,       &help,   1, "Display help", &help, extendedOption::eOTInt},
        {"data",         required_argument,     0, 'd', "Is this data?", &isData, extendedOption::eOTInt},
        {"atlFastII",         required_argument,     0, 'a', "Is this AtlFastII? (0/1)", &isAtlFastII, extendedOption::eOTInt},
        {"files",         required_argument,     0, 'f', "Input list of comma-separated D3PD files to apply the selection on", &files, extendedOption::eOTString},
        {"analysis",   required_argument,     0, 'A', "Analysis to run. Choices: AnaTtresSL", &analysis, extendedOption::eOTString},
        {"output",   required_argument,     0, 'o', "Comma-separated list of output files.", &outFile, extendedOption::eOTString},

        {0, 0, 0, 0, 0, 0, extendedOption::eOTInt}
      };

  if (!parseArguments(argc, argv, extOpt) || help) {
    dumpHelp("read", extOpt, "read\nRead selected events after preselection and generate histograms.\n");
    return 0;
  } else {
    std::cout << "Dumping options:" << std::endl;
    dumpOptions(extOpt);
  }

  // parse file list
  std::vector<std::string> fileList;
  if ( ((files.find("input") != std::string::npos) && (files.find(".txt") != std::string::npos)) ) {
    std::cout << "Using file given as text list." << std::endl;
    std::vector<std::string> inputList;
    // split by ','
    std::string argStr = files;
    for (size_t i = 0,n; i <= argStr.length(); i=n+1) {
      n = argStr.find_first_of(',',i);
      if (n == std::string::npos)
        n = argStr.length();
      std::string tmp = argStr.substr(i,n-i);
      if (tmp != "")
        inputList.push_back(tmp);
    }

    for (int k = 0; k < inputList.size(); ++k) {

      ifstream f(inputList[k].c_str());
      std::string thePathStr;
      while (f.good()) {
        std::stringstream ss;
        f.get(*ss.rdbuf(), '\n');
        if (f.get() == EOF)
          break;

       thePathStr = ss.str();
         if (thePathStr != "") {
          // bug in Ganga/Grid nodes: \\n is substituted instead of a newline
          size_t idx = std::string::npos;
          do {
            idx = thePathStr.find("\\n");
            std::string aFile = thePathStr.substr(0, idx);
            if (aFile.find(".root") != std::string::npos)
              fileList.push_back(aFile);
            if (idx != std::string::npos) {
              thePathStr = thePathStr.substr(idx+2);
            }
          } while (idx != std::string::npos);
        }
      }
    }
    for (std::vector<std::string>::const_iterator it = fileList.begin(); it != fileList.end(); ++it) {
      std::cout << "Input file \""<<*it<<"\""<< std::endl;
    }
  } else {
    // split by ','
    std::string argStr = files;
    for (size_t i = 0,n; i <= argStr.length(); i=n+1) {
      n = argStr.find_first_of(',',i);
      if (n == std::string::npos)
        n = argStr.length();
      std::string tmp = argStr.substr(i,n-i);
      fileList.push_back(tmp);
    }
  }
  if (fileList.size() == 0) {
    std::cout << "ERROR: You must input at least one file." << std::endl;
  }

  MiniTree mt(false, fileList[0].c_str(), "nominal");
  for (int k = 1; k < fileList.size(); ++k) {
    mt.addFileToRead(fileList[k]);
  }

  // get output files
  std::string outStr = outFile;
  std::vector<std::string> outList;
  for (size_t i = 0,n; i <= outStr.length(); i=n+1) {
    n = outStr.find_first_of(',',i);
    if (n == std::string::npos)
      n = outStr.length();
    std::string tmp = outStr.substr(i,n-i);
    outList.push_back(tmp);
  }


  std::vector<Analysis *> vec_analysis;
  if (analysis == "AnaTtresSL") {
    vec_analysis.push_back(new AnaTtresSL(outList[0], true,  false )); // resolved electron
    vec_analysis.push_back(new AnaTtresSL(outList[1], false, false )); // resolved muon
    vec_analysis.push_back(new AnaTtresSL(outList[2], true,  true  )); // boosted  electron
    vec_analysis.push_back(new AnaTtresSL(outList[3], false, true  )); // boosted  muon
  }

  Event sel; // selected objects

  SampleXsection sampleXsection;
  sampleXsection.readFromFile("scripts/XSectionFromAmi-13TeV.txt");

  for (int k = 0; k < mt.GetEntries(); ++k) {
    if (k % 100 == 0)
      std::cout << "Entry " << k << "/" << mt.GetEntries() << std::endl;

    mt.read(k, sel);

    int channel = sel.channelNumber();
    
    double weight = 1;
    if (!isData) {
      weight *= sel.mcWeight();// *sel.pileupWeight();
      weight *= sampleXsection.getXsection(channel);
      weight /= getEventCountBeforeSkimming(channel);
    }
    for (size_t iAna = 0; iAna < vec_analysis.size(); ++iAna) {
      vec_analysis[iAna]->run(sel, weight);
    }
  }

  for (size_t iAna = 0; iAna < vec_analysis.size(); ++iAna) delete vec_analysis[iAna];
  vec_analysis.clear();

  return 0;
}

