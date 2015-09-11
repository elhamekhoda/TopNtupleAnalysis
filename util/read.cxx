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
#include "TopNtupleAnalysis/AnaTtresSLMtt.h"
#include "TopNtupleAnalysis/AnaTtresQCD.h"

#include "TopDataPreparation/SampleXsection.h"

#include "TopNtupleAnalysis/ParseUtils.h"

#include <fstream>

#include "TROOT.h"
#include "TInterpreter.h"

#include <sstream>

int main(int argc, char **argv) {

  //ROOT::Cintex::Cintex::Enable();

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
  std::string systs = "nominal";
  int loose = 0;

  static struct extendedOption extOpt[] = {
        {"help",          no_argument,       &help,   1, "Display help", &help, extendedOption::eOTInt},
        {"data",         required_argument,     0, 'd', "Is this data?", &isData, extendedOption::eOTInt},
        {"atlFastII",         required_argument,     0, 'a', "Is this AtlFastII? (0/1)", &isAtlFastII, extendedOption::eOTInt},
        {"files",         required_argument,     0, 'f', "Input list of comma-separated D3PD files to apply the selection on", &files, extendedOption::eOTString},
        {"analysis",   required_argument,     0, 'A', "Analysis to run. Choices: AnaTtresSL", &analysis, extendedOption::eOTString},
        {"output",   required_argument,     0, 'o', "Comma-separated list of output files.", &outFile, extendedOption::eOTString},
        {"systs",   required_argument,     0, 's', "Comma-separated list of systematics.", &systs, extendedOption::eOTString},
        {"loose",   required_argument,     0, 'l', "Should I run over the loose TTree too?", &loose, extendedOption::eOTInt},

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
    ifstream f(files.c_str());
    if (!f) {
      std::cout << "Cannot open " << files << std::endl;
      std::exit(-2);
    }
    std::string thePathStr;
    while (std::getline(f, thePathStr)) {
      if (thePathStr != "") {
        size_t idx = std::string::npos;
        idx = thePathStr.find("\n");
        std::string aFile = thePathStr.substr(0, idx);
        fileList.push_back(aFile);
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
    std::exit(-1);
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

  // split systs by comma
  std::vector<std::string> systsList;
  std::vector<std::string> systsListWithBlankNominal;
  for (size_t i = 0,n; i <= systs.length(); i=n+1) {
    n = systs.find_first_of(',',i);
    if (n == std::string::npos)
      n = systs.length();
    std::string tmp = systs.substr(i,n-i);
    std::string tmpWithBlankNominal = tmp;
    if (tmpWithBlankNominal == "nominal") tmpWithBlankNominal = "";
    systsList.push_back(tmp);
    systsListWithBlankNominal.push_back(tmpWithBlankNominal);
    if (loose) {
      systsListWithBlankNominal.push_back(tmpWithBlankNominal+std::string("_Loose"));
    }
  }

  if (systs != "nominal") { // if there are other systematics, include SF systs. too
    systsListWithBlankNominal.push_back("lepSF__1up");
    systsListWithBlankNominal.push_back("lepSF__1down");
    systsListWithBlankNominal.push_back("btagbSF__1up");
    systsListWithBlankNominal.push_back("btagbSF__1down");
    systsListWithBlankNominal.push_back("btagcSF__1up");
    systsListWithBlankNominal.push_back("btagcSF__1down");
    systsListWithBlankNominal.push_back("btaglSF__1up");
    systsListWithBlankNominal.push_back("btaglSF__1down");
    if (loose) {
      systsListWithBlankNominal.push_back("lepSF__1up_Loose");
      systsListWithBlankNominal.push_back("lepSF__1down_Loose");
      systsListWithBlankNominal.push_back("btagbSF__1up_Loose");
      systsListWithBlankNominal.push_back("btagbSF__1down_Loose");
      systsListWithBlankNominal.push_back("btagcSF__1up_Loose");
      systsListWithBlankNominal.push_back("btagcSF__1down_Loose");
      systsListWithBlankNominal.push_back("btaglSF__1up_Loose");
      systsListWithBlankNominal.push_back("btaglSF__1down_Loose");
    }
  }

  std::vector<Analysis *> vec_analysis;
  
  if (analysis == "AnaTtresSL") {
    vec_analysis.push_back(new AnaTtresSL(outList[0], true,  false, systsListWithBlankNominal)); // resolved electron
    vec_analysis.push_back(new AnaTtresSL(outList[1], false, false, systsListWithBlankNominal)); // resolved muon    
    vec_analysis.push_back(new AnaTtresSL(outList[2], true,  true,  systsListWithBlankNominal)); // boosted  electron
    vec_analysis.push_back(new AnaTtresSL(outList[3], false, true,  systsListWithBlankNominal)); // boosted  muon
  } else if(analysis == "AnaTtresQCD"){
    vec_analysis.push_back(new AnaTtresQCD(outList[0], true,  false, systsListWithBlankNominal) ); //resolved electron
    vec_analysis.push_back(new AnaTtresQCD(outList[1], false, false, systsListWithBlankNominal) ); // resolved muon
    vec_analysis.push_back(new AnaTtresQCD(outList[2], true,  true,  systsListWithBlankNominal) ); // boosted  electron
    vec_analysis.push_back(new AnaTtresQCD(outList[3], false, true,  systsListWithBlankNominal) ); // boosted  muon
  } else if (analysis == "AnaTtresSLMtt") {
    vec_analysis.push_back(new AnaTtresSLMtt(outList[0], true,  false, systsListWithBlankNominal)); // resolved electron
    vec_analysis.push_back(new AnaTtresSLMtt(outList[1], false, false, systsListWithBlankNominal)); // resolved muon    
    vec_analysis.push_back(new AnaTtresSLMtt(outList[2], true,  true,  systsListWithBlankNominal)); // boosted  electron
    vec_analysis.push_back(new AnaTtresSLMtt(outList[3], false, true,  systsListWithBlankNominal)); // boosted  muon
  }

  SampleXsection sampleXsection;
  //sampleXsection.readFromFile("scripts/XSectionFromAmi-13TeV.txt");
  sampleXsection.readFromFile("scripts/XSection-MC15-13TeV.data");

  // retrieve, list of sum of weights
  std::map<int, float> sumOfWeights;
  TChain t_sumWeights("sumWeights");
  if(!isData) {
    for (int k = 0; k < fileList.size(); ++k) {
      t_sumWeights.Add(fileList[k].c_str());
    }
    int dsid;
    float value;
    t_sumWeights.SetBranchAddress("dsid", &dsid);
    t_sumWeights.SetBranchAddress("totalEventsWeighted", &value);
    for (int k = 0; k < t_sumWeights.GetEntries(); ++k) {
      t_sumWeights.GetEntry(k);
      if (sumOfWeights.find(dsid) == sumOfWeights.end()) sumOfWeights[dsid] = 0;
        sumOfWeights[dsid] += value;
    }
  }

  // systsList contains the list of TTrees representing systematics
  // given by the user
  for (size_t systIdx = 0; systIdx < systsList.size(); ++systIdx) {

    // it does not have the xxx_Loose TTrees, so we add it ourselves and run over it too
    std::vector<std::string> lepton_modes;
    lepton_modes.push_back(systsList[systIdx]);
    if (loose) {
      lepton_modes.push_back(systsList[systIdx]+std::string("_Loose"));
    }
    for (size_t lmodeIdx = 0; lmodeIdx < lepton_modes.size(); ++lmodeIdx) {

      // now we are looping over all possible TTrees with all systematic uncertainties
      // Call MiniTree to open the files and read that TTree
      std::string tname = lepton_modes[lmodeIdx];
      MiniTree mt(false, fileList[0].c_str(), tname.c_str());
      for (int k = 1; k < fileList.size(); ++k) {
        mt.addFileToRead(fileList[k]);
      }

      // for the nominal "systematic unc.", use an empty string as suffix to be backward compatible
      // also, it would be horrible to plot histograms with the nominal suffix all the time ...
      std::string systSuffixForHistograms = tname;
      if (systSuffixForHistograms == "nominal")
        systSuffixForHistograms = "";
      else if (systSuffixForHistograms == "nominal_Loose")
        systSuffixForHistograms = "_Loose";

      Event sel; // selected objects

      // now loop over all entries for this systematic uncertainty
      for (int k = 0; k < mt.GetEntries(); ++k) {
        if (k % 1000 == 0)
          std::cout << "("<< tname << ") Entry " << k << "/" << mt.GetEntries() << std::endl;
    
        // read the event into an Event object to be sent to the Analysis code later
        mt.read(k, sel);
        int channel = sel.channelNumber();
    
        // this is list just contains systSuffixForHistograms for all systematics
        // except for the nominal and nominal_Loose, on which it contains
        // the electron SF, muon SF and b-tagging SF systematics
        // these systematics do not show up as separate TTrees, so they need special treatment
        std::vector<std::string> weightSystematics;
        if (systSuffixForHistograms != "" && systSuffixForHistograms != "_Loose") {
          weightSystematics.push_back(systSuffixForHistograms);
        } else { // apply variations on the nominal
          weightSystematics.push_back(systSuffixForHistograms);
          weightSystematics.push_back(std::string("lepSF__1up")+systSuffixForHistograms);
          weightSystematics.push_back(std::string("lepSF__1down")+systSuffixForHistograms);
          weightSystematics.push_back(std::string("btagbSF__1up")+systSuffixForHistograms);
          weightSystematics.push_back(std::string("btagbSF__1down")+systSuffixForHistograms);
          weightSystematics.push_back(std::string("btagcSF__1up")+systSuffixForHistograms);
          weightSystematics.push_back(std::string("btagcSF__1down")+systSuffixForHistograms);
          weightSystematics.push_back(std::string("btaglSF__1up")+systSuffixForHistograms);
          weightSystematics.push_back(std::string("btaglSF__1down")+systSuffixForHistograms);
        }
        // loop over weight systematics
        for (size_t wIdx = 0; wIdx < weightSystematics.size(); ++wIdx) {
          std::string &suffix = weightSystematics[wIdx];

          double weight = 1;
          if (!isData) {
            weight *= sel.weight_mc()*sel.weight_pileup();
            weight *= sampleXsection.getXsection(channel);
            // TODO (Danilo) -> Change the next lines to use the SF syst. var. information
            // when suffix is one of the above
            //
            weight *= sel.weight_bTagSF();

            if (suffix == "lepSF__1up" || suffix == "lepSF__1up_Loose") {
              weight *= mt.weight_indiv_SF_EL_Trigger_UP*mt.weight_indiv_SF_EL_Reco_UP*mt.weight_indiv_SF_EL_ID_UP*mt.weight_indiv_SF_EL_Isol_UP;
              weight *= mt.weight_indiv_SF_MU_Trigger_SYST_UP*mt.weight_indiv_SF_MU_Trigger_SYST_UP*mt.weight_indiv_SF_MU_ID_SYST_UP*mt.weight_indiv_SF_MU_Isol_SYST_UP;
            } else if (suffix == "lepSF__1down" || suffix == "lepSF__1down_Loose") {
              weight *= mt.weight_indiv_SF_EL_Trigger_DOWN*mt.weight_indiv_SF_EL_Reco_DOWN*mt.weight_indiv_SF_EL_ID_DOWN*mt.weight_indiv_SF_EL_Isol_DOWN;
              weight *= mt.weight_indiv_SF_MU_Trigger_SYST_DOWN*mt.weight_indiv_SF_MU_Trigger_SYST_DOWN*mt.weight_indiv_SF_MU_ID_SYST_DOWN*mt.weight_indiv_SF_MU_Isol_SYST_DOWN;
            } else {
              weight *= sel.weight_leptonSF();
            }
          
            if (sumOfWeights[channel] != 0)
              weight /= sumOfWeights[channel];
            // std::cout << "weight: " << weight << "\t"<< sel.weight_mc() << "\t" << sampleXsection.getXsection(channel) << "\t" <<  sel.weight_bTagSF() << "\t" << sel.weight_leptonSF() << "\t" << sel.weight_pileup() << "\t" << sumOfWeights[channel]  << std::endl;          
          }
      
          // this applies b-tagging early
          // if you don't want it change the if below
          int nBtagged = 0;    
          for (size_t bidx = 0; bidx < sel.jet().size(); ++bidx) {
            if (sel.jet()[bidx].btag_mv2c20_70()) {
              nBtagged += 1;	
            }
          }
      
          if (analysis=="AnaTtresSL") {
            for (size_t iAna = 0; iAna < vec_analysis.size(); ++iAna) 
              if(nBtagged>=1) vec_analysis[iAna]->run(sel, weight, suffix);
          } else if (analysis=="AnaTtresQCD") {
            for (size_t iAna = 0; iAna < vec_analysis.size(); ++iAna) 
              if(nBtagged>=1) vec_analysis[iAna]->run(sel, weight, suffix);
          } else if (analysis=="AnaTtresSLMtt") {
            for (size_t iAna = 0; iAna < vec_analysis.size(); ++iAna) 
              if(nBtagged>=1) vec_analysis[iAna]->run(sel, weight, suffix);
          } //if  
        } // end of loop over weight systematics
      } // end of loop over entries
    } // end of loop over lepton modes (tight and loose)
  } // end of loop over systematics

  for (size_t iAna = 0; iAna < vec_analysis.size(); ++iAna) {
    vec_analysis[iAna]->terminate();
    delete vec_analysis[iAna];
  }

  vec_analysis.clear();

  return 0;
}

