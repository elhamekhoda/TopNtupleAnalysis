/**
 * @brief Jet representation to be read off the input file.
 * @author Danilo Enoque Ferreira de Lima <dferreir@cern.ch>
 */
#include "TopNtupleAnalysis/MObject.h"
#include "TopNtupleAnalysis/Jet.h"
#include <cmath>

Jet::Jet()
  : MObject() {
  m_type = MObject::jet;
  m_trueflavour = 1;
  m_mv1 = 0;
  m_ip3dsv1 = 0;
  m_jvf = 1;
  m_closeToLepton = 0;
}

Jet::Jet(const TLorentzVector &v)
  : MObject(v, MObject::jet) {
  m_trueflavour = 1;
  m_mv1 = 0;
  m_ip3dsv1 = 0;
  m_jvf = 1;
  m_closeToLepton = 0;
}

Jet::~Jet() {
}

int &Jet::trueFlavour() {
  return m_trueflavour;
}
const int Jet::trueFlavour() const {
  return m_trueflavour;
}

bool Jet::pass() const {
  if (std::fabs(mom().Eta()) > 2.5) return false;
  if (mom().Perp() < 25e3) return false;
  if ( (mom().Perp() <= 50e3) && (std::fabs(mom().Eta()) < 2.4) && \
       (std::fabs(jvf()) <= 0.5) )
    return false;
  return true;
}

bool Jet::btag() const {
  if (ip3dsv1() < 1.85) return false;
  return true;
}

const float Jet::mv1() const {
  return m_mv1;
}
float &Jet::mv1() {
  return m_mv1;
}


const float Jet::ip3dsv1() const {
  return m_ip3dsv1;
}
float &Jet::ip3dsv1() {
  return m_ip3dsv1;
}

const int Jet::closeToLepton() const {
  return m_closeToLepton;
}
int &Jet::closeToLepton() {
  return m_closeToLepton;
}

const float Jet::jvf() const {
  return m_jvf;
}
float &Jet::jvf() {
  return m_jvf;
}


