/**
 * @brief Analysis base class
 * @author Danilo Enoque Ferreira de Lima <dferreir@cern.ch>
 */

#include "TopNtupleAnalysis/Analysis.h"
#include "TopNtupleAnalysis/Event.h"

Analysis::Analysis(const std::string &filename)
  : m_filename(filename), m_hSvc(filename) {
  m_hSvc.addSystematics(""); // add other systematics to create copies of histograms per systs.
  m_hSvc.addTrigger("");
}

Analysis::~Analysis() {
}

