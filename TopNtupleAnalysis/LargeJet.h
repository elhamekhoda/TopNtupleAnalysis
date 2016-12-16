/**
 * @brief Large-R jet representation to be read off the input file.
 * @author Danilo Enoque Ferreira de Lima <dferreir@cern.ch>
 */
#ifndef LARGEJET_H
#define LARGEJET_H

#include "TopNtupleAnalysis/MObject.h"
#include "TLorentzVector.h"

class LargeJet : public MObject {
  public:
    LargeJet();
    LargeJet(const TLorentzVector &v);
    LargeJet(const LargeJet &l);
    virtual ~LargeJet();

    int &trueFlavour();
    const int trueFlavour() const;

    bool pass() const;
    bool passLoose() const;
    bool passFakeSelection(const TLorentzVector &lept, const TLorentzVector &selJet) const;
    
    double &split12();
    const double split12() const;

    bool notgood() const;
    bool &notgood();
    void setnotGood(bool);

    bool good() const;
    bool &good();
    void setGood(bool);

    bool good_sb() const;
    bool &good_sb();
    void setGood_sb(bool);

    float &subs(const std::string &s);
    const float subs(const std::string &s) const;

  protected:
    double m_split12;

    int m_trueFlavour;
    bool m_good;
    bool m_good_sb;
    bool m_notgood;

    std::map<std::string, float> m_subs;
};

#endif
