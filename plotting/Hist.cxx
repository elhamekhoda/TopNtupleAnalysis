#include "Hist.h"
#include <cmath>
#include <iostream>
#include "utils.h"

using namespace std;

Hist::Hist(int nbins, double value) {
  _size = nbins;
  for (int i = 0; i < _size; ++i) {
    _x.push_back(value);
    _y.push_back(value);
    _ye.push_back(value);
  }
  _e = 0;
  yTitle = "Entries";
  xTitle = "x";
}

Hist::Hist(const string &name, const string &syst, const string &file) {
  TFile *f = new TFile(file.c_str());
  if (!f || !f->IsOpen()) {
    throw string("Failed to open file ")+file+string(", trying to get ")+name+string(" for syst ")+syst;
  }
  string n = name;
  n += syst;
  TH1 *h = (TH1 *) f->Get(n.c_str());
  if (!h) {
    throw string("Failed to get histogram in file ")+file+string(", trying to get ")+name+string("for syst ")+syst;
  }
  if (file.find("data") == std::string::npos && file.find("Data") == std::string::npos) h->Scale(lumi_scale*1000);
  _size = 0;
  for (int i = 0; i <= h->GetNbinsX()+1; ++i) {
    _size++;
    _x.push_back(h->GetXaxis()->GetBinLowEdge(i));
    _y.push_back(h->GetBinContent(i));
    _ye.push_back(h->GetBinError(i));
  }
  h->IntegralAndError(0,h->GetNbinsX()+1, _e);
  xTitle = h->GetXaxis()->GetTitle();
  yTitle = h->GetYaxis()->GetTitle();
  delete f;
}

Hist::Hist(const Hist &other)
  : _size(other._size), _x(other._x), _y(other._y), _ye(other._ye), _e(other._e),
    xTitle(other.xTitle),yTitle(other.yTitle) {
}

double &Hist::operator[](int i) { return _y.at(i); }
double Hist::operator[](int i) const { return _y.at(i); }
double &Hist::x(int i) { return _x.at(i); }
double Hist::x(int i) const { return _x.at(i); }
double &Hist::e(int i) { return _ye[i]; }
double Hist::e(int i) const { return _ye[i]; }

Hist &Hist::operator =(const Hist &other) {
  _x = other._x;
  _y = other._y;
  _size = other._size;
  _ye = other._ye;
  _e = other._e;
  yTitle = other.yTitle;
  xTitle = other.xTitle;
  return *this;
}

Hist Hist::operator +(Hist a) const {
  if (_size == 0) return a;
  if (a._size == 0) return *this;
  if (a._size != _size) throw string("Trying to add histograms with different sizes.");
  Hist me(*this);
  for (int i = 0; i < _size; ++i) {
    me[i] += a[i];
    me.e(i) = sqrt(me.e(i)*me.e(i) + a.e(i)*a.e(i));
  }
  return me;
}
Hist Hist::operator -(Hist a) const {
  if (_size == 0) return a;
  if (a._size == 0) return *this;
  if (a._size != _size) throw string("Trying to add histograms with different sizes.");
  Hist me(*this);
  for (int i = 0; i < _size; ++i) {
    me[i] -= a[i];
    me.e(i) = sqrt(me.e(i)*me.e(i) + a.e(i)*a.e(i));
  }
  return me;
}

Hist Hist::smooth(int nbins) {
  Hist me(*this);

  double pre_yield = me.yield();

  Double_t *xx = new Double_t[_size];
  for (unsigned int i = 0; i < _size; ++i)
    xx[i] = 100 + me[i];

  TH1::SmoothArray(_size, xx, nbins);

  for (int i = 0; i < _size; ++i) {
    me[i] = xx[i] - 100;
  }

  // keep the normalisation fixed before and after smoothing
  if (me.yield() != 0)
    me *= pre_yield/me.yield();

  return me;
}


Hist Hist::operator *(Hist a) const {
  if (_size == 0) return a;
  if (a._size == 0) return *this;
  if (a._size != _size) throw string("Trying to add histograms with different sizes.");
  Hist me(*this);
  for (int i = 0; i < _size; ++i) {
    me.e(i) = sqrt(pow(me[i]*a.e(i), 2) + pow(a[i]*me.e(i), 2));
    me[i] *= a[i];
  }
  return me;
}
Hist Hist::operator /(Hist a) const {
  if (_size == 0) return a;
  if (a._size == 0) return *this;
  if (a._size != _size) throw string("Trying to add histograms with different sizes.");
  Hist me(*this);
  for (int i = 0; i < _size; ++i) {
    if (a[i] != 0) {
      me[i] /= a[i];
      me.e(i) = sqrt(fabs(((1.-2.*me[i])*me.e(i)*me.e(i) + me[i]*me[i]*a.e(i)*a.e(i) )/(a[i]*a[i]) ));
      //me.e(i) = sqrt(pow((me[i]/pow(a[i], 2))*a.e(i), 2) + pow(me.e(i)/a[i], 2));
    } else if (a[i] == 0 && me[i] == 0) {
      me.e(i) = 1;
      me[i] = 1;
    } else {
      me.e(i) = 0;
      me[i] = 0;
    }
  }
  return me;
}

Hist &Hist::operator +=(Hist a) {
  if (_size == 0) {
    (*this) = a;
    return *this;
  }
  if (a._size == 0) {
    return *this;
  }
  if (a._size != _size) throw string("Trying to add histograms with different sizes.");
  for (int i = 0; i < _size; ++i) {
    (*this).e(i) = sqrt((*this).e(i)*(*this).e(i) + a.e(i)*a.e(i));
    (*this)[i] += a[i];
  }
  return *this;
}


Hist &Hist::operator -=(Hist a) {
  if (_size == 0) {
    (*this) = a;
    return *this;
  }
  if (a._size == 0) {
    return *this;
  }
  if (a._size != _size) throw string("Trying to add histograms with different sizes.");
  for (int i = 0; i < _size; ++i) {
    (*this).e(i) = sqrt((*this).e(i)*(*this).e(i) + a.e(i)*a.e(i));
    (*this)[i] -= a[i];
  }
  return *this;
}

Hist &Hist::operator *=(Hist a) {
  if (_size == 0) {
    (*this) = a;
    return *this;
  }
  if (a._size == 0) {
    return *this;
  }
  
  if (a._size != _size) throw string("Trying to add histograms with different sizes.");
  for (int i = 0; i < _size; ++i) {
    (*this).e(i) = sqrt((*this).e(i)*(*this).e(i) + a.e(i)*a.e(i));
    (*this)[i] *= a[i];
  }
  return *this;
}

Hist Hist::operator *(double a) const {
  Hist me(*this);
  for (int i = 0; i < _size; ++i) {
    me[i] *= a;
    me.e(i) *= a;
  }
  return me;
}
Hist &Hist::operator *=(double f) {
  for (int i = 0; i < _size; ++i) (*this)[i] *= f;
  for (int i = 0; i < _size; ++i) (*this).e(i) *= f;
}


void Hist::max(Hist a, Hist b) {
  *this = a;
  for (int i = 0; i < _size; ++i) {
    if (std::fabs(b[i]) > std::fabs(a[i])) (*this)[i] = b[i];
    else (*this)[i] = a[i];
  }
}

double Hist::yield() const {
  double y = 0;
  for (int i = 0; i < _size; ++i) {
    y += (*this)[i];
  }
  return y;
}

double Hist::meanY() const {
  double y = 0;
  for (int i = 1; i < _size-1; ++i) {
    y += (*this)[i]*((*this).x(i+1) - (*this).x(i));
  }
  y /= ((*this).x(_size-1) - (*this).x(1));
  return y;
}

double Hist::yieldstat() const {
  return _e;
}

void Hist::squareRoot() {
  for (int i = 0; i < _size; ++i) {
    (*this).e(i) = sqrt((*this).e(i));
    (*this)[i] = sqrt((*this)[i]);
  }
}

Hist Hist::power(double e) {
  Hist ret(*this);
  for (int i = 0; i < _size; ++i) {
    ret.e(i) = pow(ret.e(i), e);
    ret[i] = pow(ret[i], e);
  }
}

void Hist::showUnderflow() {
  if (_size == 0) return;
  _x.insert(_x.begin(), _x[0]-1);

  _y.insert(_y.begin(), 0);
  _size++;
  _ye.insert(_ye.begin(), 0);
}

void Hist::limitMaxX(double xMax, bool addOverflow) {
  if (_size <= 2) return;
  size_t iMax = 0;
  while (_x[iMax] < xMax) {
    if (iMax >= _x.size()-1) {
      break;
    } else {
      ++iMax;
    }
  }
  if (iMax >= _x.size()-1) return;

  double cumInt = 0;
  double cumIntError = 0;
  xMax = _x[iMax];
  for (size_t i = iMax; i < _x.size(); ++i) {
    cumInt += _y[i];
    cumIntError += pow(_y[i], 2);
    if (!addOverflow) break;
  }
  cumIntError = sqrt(cumIntError);
  _x.erase(_x.begin()+iMax, _x.end());
  _y.erase(_y.begin()+iMax, _y.end());
  _ye.erase(_ye.begin()+iMax, _ye.end());

  _x.push_back(xMax);
  _y.push_back(cumInt);
  _ye.push_back(cumIntError);

  _size = _x.size();
}

void Hist::limitMinX(double xMin) {
  if (_size <= 2) return;
  size_t iMin = _x.size()-1;
  while (_x[iMin] > xMin) {
    if (iMin == 0) {
      break;
    } else {
      --iMin;
    }
  }
  if (iMin <= 0) return;

  double cumInt = 0;
  double cumIntError = 0;
  xMin = _x[iMin];
  for (size_t i = 0; i < iMin; ++i) {
    cumInt += _y[i];
    cumIntError += pow(_y[i], 2);
  }
  cumIntError = sqrt(cumIntError);
  _x.erase(_x.begin(), _x.begin()+iMin);
  _y.erase(_y.begin(), _y.begin()+iMin);
  _ye.erase(_ye.begin(), _ye.begin()+iMin);

  _x.insert(_x.begin(), xMin-1);
  _y.insert(_y.begin(), cumInt);
  _ye.insert(_ye.begin(), cumIntError);

  _size = _x.size();
}

void Hist::rebin(int r) {
  if (_size <= 2) return;

  vector<double> nx;
  vector<double> ny;
  vector<double> nye;
  nx.push_back(_x[0]);
  ny.push_back(_y[0]);
  nye.push_back(_ye[0]);
  int count = 0;
  double addX = _x[1];
  double oldX = _x[1];
  double addY = 0;
  double addYE = 0;
  for (size_t i = 1; i < _size-1; ++i) {
    addX = _x[i];
    if (count < r) {
      addY += _y[i];
      addYE += pow(_ye[i], 2);
    } else {
      nx.push_back(oldX);
      ny.push_back(addY);
      nye.push_back(sqrt(addYE));

      oldX  = _x[i];
      addY  = _y[i];
      addYE = pow(_ye[i], 2);
      count = 0;
    }
    count++;
  }
  if (count != 0) {
    nx.push_back(oldX);
    ny.push_back(addY);
    nye.push_back(sqrt(addYE));
  }
  nx.push_back(_x[_size-1]);
  ny.push_back(_y[_size-1]);
  nye.push_back(_ye[_size-1]);
  _x = nx;
  _y = ny;
  _ye = nye;

  _size = _x.size();
}

void Hist::showOverflow() {
  _x.insert(_x.end(), _x[_size]+1);

  _y.insert(_y.end(), 0);
  _size++;
  _ye.insert(_ye.end(), 0);
}

shared_ptr<TH1D> Hist::makeTH1(const string name) {
  shared_ptr<TH1D> h;
  int mySize = _size-2; // skip underflow
  double *myX = new double[mySize+1];
  for (int p = 0; p <= mySize; ++p) {
    myX[p] = (*this).x(p+1);
  }
  h.reset(new TH1D(name.c_str(), name.c_str(), mySize, myX));
  delete [] myX;
  h->Sumw2();
  for (int p = 0; p < _size; ++p) {
    h->SetBinContent(p, (*this)[p]);
    h->SetBinError(p, (*this).e(p));
  }
  h->GetXaxis()->SetTitle(xTitle.c_str());
  h->GetYaxis()->SetTitle(yTitle.c_str());
  return h;
}

Hist Hist::abs() {
  Hist h(*this);
  for (size_t i = 0; i < _size; ++i) h[i] = fabs(h[i]);
  return h;
}

ostream &operator<<(ostream &o, Hist &h) {
  o << "Histogram with x title '" << h.xTitle << "', size = " << h._size << ", yield = " << h.yield() << ": ";
  for (int k = 0; k < h._size; ++k) o << "(" << h.x(k) << ", " << h[k] << ", " << h.e(k) << ") ";
  return o;
}
ostream &operator<<(ostream &o, TH1D &h) {
  o << "TH1D with x title " << h.GetXaxis()->GetTitle() << ", size = " << h.GetNbinsX() << ": ";
  for (int k = 0; k <= h.GetNbinsX()+1; ++k) o << "(" << h.GetXaxis()->GetBinLowEdge(k) << ", " << h.GetBinContent(k) <<") ";
  return o;
}

void Hist::clipErrorForEfficiency() {
  for (int i = 0; i < _size; ++i) {
    if ((*this).e(i) + (*this)[i] > 1) {
      (*this).e(i) = 1 - (*this)[i];
    }
  }
}
