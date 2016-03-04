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

    int &isWTaggedMed();
    const int isWTaggedMed() const;

    int &isWTaggedTight();
    const int isWTaggedTight() const;


    int &isZTaggedMed();
    const int isZTaggedMed() const;

    int &isZTaggedTight();
    const int isZTaggedTight() const;

    
    bool pass() const;
    bool passLoose() const;
    bool passFakeSelection(const TLorentzVector &lept, const TLorentzVector &selJet) const;
    
    double &split12();
    const double split12() const;

    bool good() const;
    bool &good();
    void setGood(bool);
    
    bool isSmoothTopTagged_50() const;
    bool &isSmoothTopTagged_50();
    void setIsSmoothTopTagged_50(bool);

    bool isSmoothTopTagged_80() const;
    bool &isSmoothTopTagged_80();
    void setIsSmoothTopTagged_80(bool);

    bool isGhAssTrackJetBtagged() const;
    bool &isGhAssTrackJetBtagged();
    void setIsGhAssTrackJetBtagged(bool);
    
    float &subs(const std::string &s);
    const float subs(const std::string &s) const;

  protected:
    double m_split12;

    int m_trueFlavour;
    bool m_good;
    bool m_isSmoothTopTagged_50;
    bool m_isSmoothTopTagged_80;
    bool m_isGhAssTrackJetBtagged;
    int m_isWTaggedMed;
    int m_isWTaggedTight;
    int m_isZTaggedMed;
    int m_isZTaggedTight;


    std::map<std::string, float> m_subs;
};

#endif
