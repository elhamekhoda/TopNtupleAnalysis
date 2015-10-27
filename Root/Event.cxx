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
  m_tjet.clear();
  m_largeJet.clear();
  m_met.SetPxPyPzE(0,0,0,0);
  m_passes.clear();
}

float &Event::weight_pileup() {
  return m_weight_pileup;
}
const float Event::weight_pileup() const {
  return m_weight_pileup;
}

float &Event::weight_mc() {
  return m_weight_mc;
}

const float Event::weight_mc() const {
  return m_weight_mc;
}

float &Event::weight_bTagSF() {
  return m_weight_bTagSF;
}

const float Event::weight_bTagSF() const {
  return m_weight_bTagSF;
}

float &Event::weight_leptonSF() {
  return m_weight_leptonSF;
}

const float Event::weight_leptonSF() const {
  return m_weight_leptonSF;
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

std::vector<Jet> &Event::tjet() {
  return m_tjet;
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

const std::vector<Jet> &Event::tjet() const {
  return m_tjet;
}

const std::vector<LargeJet> &Event::largeJet() const {
  return m_largeJet;
}

unsigned int &Event::runNumber() {
  return m_runNumber;
}

const unsigned int Event::runNumber() const {
  return m_runNumber;
}

unsigned int &Event::eventNumber() {
  return m_eventNumber;
}

const unsigned int Event::eventNumber() const {
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

float &Event::mu_original() {
  return m_mu_original;
}
const float Event::mu_original() const {
  return m_mu_original;
}

int &Event::npv() {
  return m_npv;
}
const int Event::npv() const {
  return m_npv;
}

float &Event::vtxz(){
  return m_vtxz;
}

const float Event::vtxz() const{
  return m_vtxz;
}

unsigned int &Event::lbn() {
  return m_lbn;
}

const unsigned int Event::lbn() const {
  return m_lbn;
}

//Variables from the truth: lepton+jet channel

//hadronic top decay
TLorentzVector &Event::MC_w1h() {
  return m_MC_w1h;
}
const TLorentzVector &Event::MC_w1h() const {
  return m_MC_w1h;
}

int &Event::MC_w1h_pdgId() {
  return m_MC_w1h_pdgId;
}
const int Event::MC_w1h_pdgId() const {
  return m_MC_w1h_pdgId;
}

TLorentzVector &Event::MC_w2h() {
  return m_MC_w2h;
}
const TLorentzVector &Event::MC_w2h() const {
  return m_MC_w2h;
}

int &Event::MC_w2h_pdgId() {
  return m_MC_w2h_pdgId;
}
const int Event::MC_w2h_pdgId() const {
  return m_MC_w2h_pdgId;
}

TLorentzVector &Event::MC_bh() {
  return m_MC_bh;
}
const TLorentzVector &Event::MC_bh() const {
  return m_MC_bh;
}

//leptonic top decay
TLorentzVector &Event::MC_w1l() {
  return m_MC_w1l;
}
const TLorentzVector &Event::MC_w1l() const {
  return m_MC_w1l;
}

signed int &Event::MC_w1l_pdgId() {
  return m_MC_w1l_pdgId;
}
const signed int Event::MC_w1l_pdgId() const {
  return m_MC_w1l_pdgId;
}

TLorentzVector &Event::MC_w2l() {
  return m_MC_w2l;
}
const TLorentzVector &Event::MC_w2l() const {
  return m_MC_w2l;
}

int &Event::MC_w2l_pdgId() {
  return m_MC_w2l_pdgId;
}
const int Event::MC_w2l_pdgId() const {
  return m_MC_w2l_pdgId;
}

TLorentzVector &Event::MC_bl() {
  return m_MC_bl;
}
const TLorentzVector &Event::MC_bl() const {
  return m_MC_bl;
}

TLorentzVector &Event::MC_ttbar_beforeFSR() {
  return m_MC_ttbar_beforeFSR;
}
const TLorentzVector &Event::MC_ttbar_beforeFSR() const {
  return m_MC_ttbar_beforeFSR;
}

//MA
//hadronic top decay

TLorentzVector &Event::MA_w1h() {
  return m_MA_w1h;
}
const TLorentzVector &Event::MA_w1h() const {
  return m_MA_w1h;
}

int &Event::MA_w1h_pdgId() {
  return m_MA_w1h_pdgId;
}
const int Event::MA_w1h_pdgId() const {
  return m_MA_w1h_pdgId;
}

TLorentzVector &Event::MA_w2h() {
  return m_MA_w2h;
}
const TLorentzVector &Event::MA_w2h() const {
  return m_MA_w2h;
}

int &Event::MA_w2h_pdgId() {
  return m_MA_w2h_pdgId;
}
const int Event::MA_w2h_pdgId() const {
  return m_MA_w2h_pdgId;
}

TLorentzVector &Event::MA_bh() {
  return m_MA_bh;
}
const TLorentzVector &Event::MA_bh() const {
  return m_MA_bh;
}

//leptonic top decay
TLorentzVector &Event::MA_w1l() {
  return m_MA_w1l;
}
const TLorentzVector &Event::MA_w1l() const {
  return m_MA_w1l;
}

signed int &Event::MA_w1l_pdgId() {
  return m_MA_w1l_pdgId;
}
const signed int Event::MA_w1l_pdgId() const {
  return m_MA_w1l_pdgId;
}

TLorentzVector &Event::MA_w2l() {
  return m_MA_w2l;
}
const TLorentzVector &Event::MA_w2l() const {
  return m_MA_w2l;
}

int &Event::MA_w2l_pdgId() {
  return m_MA_w2l_pdgId;
}
const int Event::MA_w2l_pdgId() const {
  return m_MA_w2l_pdgId;
}

TLorentzVector &Event::MA_bl() {
  return m_MA_bl;
}
const TLorentzVector &Event::MA_bl() const {
  return m_MA_bl;
}

