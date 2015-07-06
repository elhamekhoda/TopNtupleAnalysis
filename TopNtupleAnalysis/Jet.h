/**
 * @brief Jet representation to be read off the input file.
 * @author Danilo Enoque Ferreira de Lima <dferreir@cern.ch>
 */
#ifndef JET_H
#define JET_H

#include "TopNtupleAnalysis/MObject.h"
#include "TLorentzVector.h"

class Jet : public MObject {
  public:
    Jet();
    Jet(const TLorentzVector &v);
    virtual ~Jet();

    int &trueFlavour();
    const int trueFlavour() const;

    const float mv1() const;
    float &mv1();

    const float ip3dsv1() const;
    float &ip3dsv1();

    const float jvt() const;
    float &jvt();

    bool pass() const;
    bool btag() const;

    int &closeToLepton();
    const int closeToLepton() const;

  protected:
    int m_trueflavour;
    float m_mv1;
    float m_ip3dsv1;
    float m_jvt;
    int m_closeToLepton;

};

#endif
