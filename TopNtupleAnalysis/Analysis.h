/**
 * @brief Analysis base class
 * @author Danilo Enoque Ferreira de Lima <dferreir@cern.ch>
 */

#ifndef ANALYSIS_H
#define ANALYSIS_H

#include <string>
#include "TH1F.h"
#include "TFile.h"
#include "TopNtupleAnalysis/Event.h"
#include "TopNtupleAnalysis/HistogramService.h"

class Analysis {
  public:
    Analysis(const std::string &filename);
    virtual ~Analysis();

    virtual void run(const Event &e, double weight) = 0;

  protected:
    std::string m_filename;
    HistogramService m_hSvc;

};

#endif

