#include "SystematicImplementation.h"

#include "Hist.h"
#include <string>
#include <iostream>

using namespace std;

Syst::Syst() {
}

HistDiff::HistDiff(const string &a, const string &b) {
  _a = a;
  _b = b;
}

Hist HistDiff::get(const string &name, const string &fname) {
  Hist ha(name, _a, fname);
  Hist hb(name, _b, fname);
  return (ha - hb);
}

HistNorm::HistNorm(double n) {
  _n = n;
}

HistNorm::HistNorm(double n, const vector<string> &only) {
  _n = n;
  _only = only;
}

Hist HistNorm::get(const string &name, const string &fname) {
  bool good = false;
  for (int i = 0; i < _only.size(); ++i) {
    if (fname.find(_only[i]) != string::npos) good = true;
  }
  if (!good && _only.size() != 0) return Hist();
  Hist ha(name, "", fname);
  ha *= _n;
  return ha;
}

Symm::Symm(Syst *a, Syst *b) {
  _a.reset(a);
  if (b) _b.reset(b);
}

Hist Symm::get(const string &name, const string &fname) {
  Hist ha = _a->get(name, fname);
  if (!_b) {
    return ha;
  }
  Hist hb = _b->get(name, fname);
  Hist hc;
  hc.max(ha, hb);
  return hc;
}

NotData::NotData(Syst *a) {
  _a.reset(a);
}

Hist NotData::get(const string &name, const string &fname) {
  if (fname.find("Data") != string::npos) return Hist();
  Hist ha = _a->get(name, fname);
  return ha;
}

SystCorr::SystCorr(Syst *a, Syst *b) {
  _a.reset(a);
  _b.reset(b);
}

Hist SystCorr::get(const string &name, const string &fname) {
  Hist ha = _a->get(name, fname);
  Hist hb = _b->get(name, fname);
  Hist hc = ha + hb;
  return hc;
}

Relative::Relative(const string &a, const string &b, const vector<string> &only, double scale) {
  _a = a;
  _b = b;
  _only = only;
  _scale = scale;
}

Hist Relative::get(const string &name, const string &fname) {
  bool good = false;
  for (int i = 0; i < _only.size(); ++i) {
    if (fname.find(_only[i]) != string::npos) good = true;
  }
  if (!good && _only.size() != 0) return Hist();

  Hist ha(name, "", _a);
  Hist hb(name, "", _b);
  Hist hnom(name, "", fname);
  return hnom - hnom*hb*_scale/ha;
  //return (ha-hb)*0.5;
}

RelativeISRFSR::RelativeISRFSR(const string &a, const string &b, const vector<string> &only) {
  _a = a;
  _b = b;
  _only = only;
}

Hist RelativeISRFSR::get(const string &name, const string &fname) {
  bool good = false;
  for (int i = 0; i < _only.size(); ++i) {
    if (fname.find(_only[i]) != string::npos) good = true;
  }
  if (!good) return Hist();

  Hist ha(name, "", _a);
  Hist hb(name, "", _b);
  Hist hnom(name, "", fname);
  Hist hc = ha + hb;
  Hist hd = ha - hb;
  //return (hnom*hd/hc).abs();
  return (hnom*hd/hc);
}

