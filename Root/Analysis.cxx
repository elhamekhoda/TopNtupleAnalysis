/**
 * @brief Analysis base class
 * @author Danilo Enoque Ferreira de Lima <dferreir@cern.ch>
 */

#include "TopNtupleAnalysis/Analysis.h"
#include "TopNtupleAnalysis/Event.h"

Analysis::Analysis(const std::string &filename, std::vector<std::string> &systematicList)
  : m_filename(filename), m_hSvc(filename) {
  for (size_t i = 0; i < systematicList.size(); ++i) {
    m_hSvc.addSystematics(systematicList[i]);
  }
  m_hSvc.addTrigger("");
}

Analysis::Analysis(const std::string &filename)
  : m_filename(filename), m_hSvc(filename) {
  m_hSvc.addSystematics("");
  m_hSvc.addTrigger("");
}

Analysis::~Analysis() {
}

