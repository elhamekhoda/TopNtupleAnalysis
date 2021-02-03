#ifndef WRAPPER_H
#define WRAPPER_H

#include <cstdlib>
#include <sstream>
#include <vector>
#include "Math/Vector4D.h"
#include "TLorentzVector.h"
#include "TMath.h"

class TopNtupleAnalysisUtils {
public:
TopNtupleAnalysisUtils();
virtual ~TopNtupleAnalysisUtils();
void initWrapper(bool dt = true);
void getMtt(TLorentzVector lep, const std::vector<TLorentzVector> jets, const std::vector<bool> btag, TLorentzVector met);
void getMtt(ROOT::Math::PtEtaPhiEVector lep, const std::vector<ROOT::Math::PtEtaPhiEVector> jets, const std::vector<bool> btag, ROOT::Math::PtEtaPhiEVector met);
double res_mtt();
double res_mtl();
double res_mth();
double res_mwh();
double res_chi2();
int res_bcat();
TLorentzVector res_tv(std::string target);
double getEWK(TLorentzVector top, TLorentzVector topbar, int initial_type, int var = 0);
TLorentzVector getNu(TLorentzVector l, double met, double met_phi);
double getQCDWeight(int btags, int boosted, TLorentzVector met, TLorentzVector lep, int isTight, std::vector<TLorentzVector> jet, float sd0, int isElectron,  float topoetcone20, int runNumber);
Double_t wfunction(Int_t E, Int_t DM, Double_t x);
// #ifdef NNLOReweighter_NNLOReweighter
void InitNNLO(int mcChannelNumber);
double getNNLOWeight(double ttbarPt, double topPt, int mode);
// #endif
#ifndef NOEFT
void initPDF(const std::string &s = "NNPDF21_lo_as_0130_100");
double alphaS(double Q2);
void setEFT(float eftLambda, float eftCvv);
double getEFTSMWeight(int i1_pid, int i2_pid, std::vector<int> f_pid, TLorentzVector i1, TLorentzVector i2, TLorentzVector t, TLorentzVector tbar, std::vector<TLorentzVector> f, double Q2);
#endif
ClassDef(TopNtupleAnalysisUtils, 0)
};
#endif

