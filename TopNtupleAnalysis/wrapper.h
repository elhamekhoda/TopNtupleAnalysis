#ifndef WRAPPER_H
#define WRAPPER_H

#include <cstdlib>
#include <sstream>
#include <vector>
#include "TLorentzVector.h"


void initWrapper(bool dt = true);
void getMtt(TLorentzVector lep, std::vector<TLorentzVector> jets, std::vector<bool> btag, TLorentzVector met);
double res_mtt();
double res_mtl();
double res_mth();
double res_mwh();
double res_chi2();
double getEWK(TLorentzVector top, TLorentzVector topbar, int initial_type, int var = 0);
TLorentzVector getNu(TLorentzVector l, double met, double met_phi);
double getQCDWeight(int btags, int boosted, TLorentzVector met, TLorentzVector lep, int isTight, std::vector<TLorentzVector> jet, float sd0, int isElectron, int muonTrigger, float topoetcone20, int runNumber);

void initPDF(const std::string &s = "NNPDF21_lo_as_0130_100");
double alphaS(double Q2);
void setEFT(float eftLambda, float eftCvv);
double getEFTSMWeight(int i1_pid, int i2_pid, std::vector<int> f_pid, TLorentzVector i1, TLorentzVector i2, TLorentzVector t, TLorentzVector tbar, std::vector<TLorentzVector> f, double Q2);

#endif