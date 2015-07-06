/**
 * @brief Event class, with information read off the input file read using MiniTree.
 * @author Danilo Enoque Ferreira de Lima <dferreir@cern.ch>
 */
#include "TopNtupleAnalysis/Event.h"
#include <vector>
#include <cmath>
#include <algorithm>

Event::Event() {
}

Event::~Event() {
}

std::vector<std::string> &Event::passes() {
  return m_passes;
}

const bool Event::passes(const std::string &selection) const {
  return std::find(m_passes.begin(), m_passes.end(), selection) != m_passes.end();
}

const int Event::hfor() const {
  return m_hfor;
}

int &Event::hfor() {
  return m_hfor;
}

void Event::clear() {
  m_electron.clear();
  m_muon.clear();
  m_jet.clear();
  m_largeJet.clear();
  m_met.SetPxPyPzE(0,0,0,0);
  m_passes.clear();
}

float &Event::pileupWeight() {
  return m_pileupWeight;
}
const float Event::pileupWeight() const {
  return m_pileupWeight;
}

float &Event::weight_mc() {
  return m_weight_mc;
}

const float Event::weight_mc() const {
  return m_weight_mc;
}

std::vector<Electron> &Event::electron() {
  return m_electron;
}

std::vector<Muon> &Event::muon() {
  return m_muon;
}

std::vector<Jet> &Event::jet() {
  return m_jet;
}

std::vector<LargeJet> &Event::largeJet() {
  return m_largeJet;
}

void Event::met(float met_x, float met_y) {
  m_met.SetPxPyPzE(met_x, met_y, 0, std::sqrt(std::pow(met_x, 2) + std::pow(met_y, 2)));
}

TLorentzVector Event::met() const {
  return m_met;
}

const std::vector<Electron> &Event::electron() const {
  return m_electron;
}

const std::vector<Muon> &Event::muon() const {
  return m_muon;
}

const std::vector<Jet> &Event::jet() const {
  return m_jet;
}

const std::vector<LargeJet> &Event::largeJet() const {
  return m_largeJet;
}


int &Event::runNumber() {
  return m_runNumber;
}

const int Event::runNumber() const {
  return m_runNumber;
}

int &Event::eventNumber() {
  return m_eventNumber;
}

const int Event::eventNumber() const {
  return m_eventNumber;
}

bool &Event::isData() {
  return m_isData;
}
const bool Event::isData() const {
  return m_isData;
}

int &Event::channelNumber() {
  return m_channelNumber;
}
const int Event::channelNumber() const {
  return m_channelNumber;
}

float &Event::mu() {
  return m_mu;
}
const float Event::mu() const {
  return m_mu;
}


int &Event::npv() {
  return m_npv;
}
const int Event::npv() const {
  return m_npv;
}


unsigned int &Event::lbn() {
  return m_lbn;
}

const unsigned int Event::lbn() const {
  return m_lbn;
}

