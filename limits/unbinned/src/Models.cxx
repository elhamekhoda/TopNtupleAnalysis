#include "Models.h"

#include "TMath.h"
#include "RooAbsPdf.h"
#include "RooRealProxy.h"
#include <iostream>

ClassImp(BkgFallPdf)
ClassImp(BkgDijetsPdf)
ClassImp(BkgWtbPdf)
ClassImp(SignalPdf)
ClassImp(SimpleSignalPdf)
ClassImp(SkewNormalPdf)

BkgWtbPdf::BkgWtbPdf() {
}

BkgWtbPdf::BkgWtbPdf(const char *name, const char *title, RooAbsReal &_x,
                       RooAbsReal &_p1, RooAbsReal &_p2)
   : RooAbsPdf(name, title),
     m_x("x", "x", this, _x),
     m_p1("p1", "p1", this, _p1),
     m_p2("p2", "p2", this, _p2)
  {
}

BkgWtbPdf::BkgWtbPdf(const BkgWtbPdf &other, const char *name)
   : RooAbsPdf(other, name),
     m_x("x", this, other.m_x),
     m_p1("p1",this, other.m_p1),
     m_p2("p2",this, other.m_p2)
{
}

TObject *BkgWtbPdf::clone(const char *newname) const {
  return new BkgWtbPdf(*this, newname);
}

BkgWtbPdf::~BkgWtbPdf() {
}
double BkgWtbPdf::evaluate() const {
  double x = m_x;
  double _p1 = m_p1;
  double _p2 = m_p2;

  return TMath::Exp(_p1*x + _p2*x*x);
}

BkgFallPdf::BkgFallPdf() {
}

BkgFallPdf::BkgFallPdf(const char *name, const char *title, RooAbsReal &_x,
                       RooAbsReal &_p1, RooAbsReal &_p2)//,
                       //RooAbsReal &_p3)
   : RooAbsPdf(name, title),
     m_x("x", "x", this, _x),
     m_p1("p1", "p1", this, _p1),
     m_p2("p2", "p2", this, _p2)//,
     //m_p3("p3", "p3", this, _p3)
  {
}

BkgFallPdf::BkgFallPdf(const BkgFallPdf &other, const char *name)
   : RooAbsPdf(other, name),
     m_x("x", this, other.m_x),
     m_p1("p1",this, other.m_p1),
     m_p2("p2",this, other.m_p2)//,
     //m_p3("p3",this, other.m_p3)
{
}

TObject *BkgFallPdf::clone(const char *newname) const {
  return new BkgFallPdf(*this, newname);
}

BkgFallPdf::~BkgFallPdf() {
}
double BkgFallPdf::evaluate() const {
  double x = m_x/13.0e3;
  double _p1 = m_p1;
  double _p2 = m_p2;
  //double _p3 = m_p3;

  double f  = TMath::Power(x, _p1+_p2*TMath::Log(x));

  return f;
}

BkgDijetsPdf::BkgDijetsPdf() {
}

BkgDijetsPdf::BkgDijetsPdf(const char *name, const char *title, RooAbsReal &_x,
                           RooAbsReal &_p1, RooAbsReal &_p2,
                           RooAbsReal &_p3)
   : RooAbsPdf(name, title),
     m_x("x", "x", this, _x),
     m_p1("p1", "p1", this, _p1),
     m_p2("p2", "p2", this, _p2),
     m_p3("p3", "p3", this, _p3)
  {
}

BkgDijetsPdf::BkgDijetsPdf(const BkgDijetsPdf &other, const char *name)
   : RooAbsPdf(other, name),
     m_x("x", this, other.m_x),
     m_p1("p1",this, other.m_p1),
     m_p2("p2",this, other.m_p2),
     m_p3("p3",this, other.m_p3)
{
}

TObject *BkgDijetsPdf::clone(const char *newname) const {
  return new BkgDijetsPdf(*this, newname);
}

BkgDijetsPdf::~BkgDijetsPdf() {
}
double BkgDijetsPdf::evaluate() const {
  double x = m_x/13.0e3;
  double _p1 = m_p1;
  double _p2 = m_p2;
  double _p3 = m_p3;

  double f = 0;

  f  = TMath::Power(1-x, _p1)/TMath::Power(x, _p2+_p3*TMath::Log(x));

  if (f < 0) f = 0; // it can result in -0 sometimes
  return f;
}

SignalPdf::SignalPdf() {
}

SignalPdf::SignalPdf(const char *name, const char *title, RooAbsReal &_x,
                     RooAbsReal &_m, RooAbsReal &_s, RooAbsReal &_xi, RooAbsReal &_omega, RooAbsReal &_alpha, RooAbsReal &_xnorm,
                     RooAbsReal &_m2, RooAbsReal &_s2, RooAbsReal &_norm2,
                     RooAbsReal &_m3, RooAbsReal &_s3, RooAbsReal &_norm3)
 : RooAbsPdf(name, title),
    m_x("x", "x", this, _x),
    m_m("m", "m", this, _m),
    m_s("s", "s", this, _s),
    m_xi("xi", "xi", this, _xi),
    m_omega("omega", "omega", this, _omega),
    m_alpha("alpha", "alpha", this, _alpha),
    m_norm("norm", "norm", this, _xnorm),
    m_m2("m2", "m2", this, _m2),
    m_s2("s2", "s2", this, _s2),
    m_norm2("norm2", "norm2", this, _norm2),
    m_m3("m3", "m3", this, _m3),
    m_s3("s3", "s3", this, _s3),
    m_norm3("norm3", "norm3", this, _norm3) {
}

SignalPdf::SignalPdf(const SignalPdf &other, const char *name)
  : RooAbsPdf(other, name),
    m_x("x",this, other.m_x),
    m_m("m",this, other.m_m),
    m_s("s",this, other.m_s),
    m_xi("xi",this, other.m_xi),
    m_omega("omega",this, other.m_omega),
    m_alpha("alpha",this, other.m_alpha),
    m_norm("norm",this, other.m_norm),
    m_m2("m2",this, other.m_m2),
    m_s2("s2",this, other.m_s2),
    m_norm2("norm2",this, other.m_norm2),
    m_m3("m3",this, other.m_m3),
    m_s3("s3",this, other.m_s3),
    m_norm3("norm3",this, other.m_norm3) {
}

TObject *SignalPdf::clone(const char *newname) const {
  return new SignalPdf(*this, newname);
}
SignalPdf::~SignalPdf() {
}

double SignalPdf::evaluate() const {
  double x = m_x;
  double m = m_m;
  double s = m_s;
  double xi = m_xi;
  double omega = m_omega;
  double alpha = m_alpha;
  double xnorm = m_norm;
  double m2 = m_m2;
  double s2 = m_s2;
  double xnorm2 = m_norm2;
  double m3 = m_m3;
  double s3 = m_s3;
  double xnorm3 = m_norm3;

  if (omega <= 0) return 1e99;
  if (xnorm <= 0) return 1e99;
  if (s2 <= 0) return 1e99;
  if (s3 <= 0) return 1e99;
  if (s <= 0) return 1e99;

  double f = xnorm/(omega*TMath::Pi())*TMath::Exp(-TMath::Power(x-xi,2)/(2.0*omega*omega))*(0.5*(1+TMath::Erf(alpha*(x-xi)/omega)));
  f += (1.0-xnorm)/(TMath::Sqrt(2*TMath::Pi())*s)*TMath::Exp(-TMath::Power(x-m,2)/(2.0*s*s));
  f += xnorm2/(TMath::Sqrt(2*TMath::Pi())*s2)*TMath::Exp(-TMath::Power(x-m2,2)/(2.0*s2*s2));
  f += xnorm3/(TMath::Sqrt(2*TMath::Pi())*s3)*TMath::Exp(-TMath::Power(x-m3,2)/(2.0*s3*s3));
  if (f < 0) f = 0;

  return f;
}

SimpleSignalPdf::SimpleSignalPdf() {
}

SimpleSignalPdf::SimpleSignalPdf(const char *name, const char *title, RooAbsReal &_x,
                     RooAbsReal &_m, RooAbsReal &_s, RooAbsReal &_xi, RooAbsReal &_omega, RooAbsReal &_alpha, RooAbsReal &_xnorm//,
//                     RooAbsReal &_m2, RooAbsReal &_s2, RooAbsReal &_norm2, RooAbsReal &_norms
                     )
 : RooAbsPdf(name, title),
    m_x("x", "x", this, _x),
    m_m("m", "m", this, _m),
    m_s("s", "s", this, _s),
    m_xi("xi", "xi", this, _xi),
    m_omega("omega", "omega", this, _omega),
    m_alpha("alpha", "alpha", this, _alpha),
    m_xnorm("xnorm", "xnorm", this, _xnorm)//,
    //m_xnorms("xnorms", "xnorms", this, _norms),
    //m_m2("m2", "m2", this, _m2),
    //m_s2("s2", "s2", this, _s2),
    //m_norm2("norm2", "norm2", this, _norm2)
  {
}

SimpleSignalPdf::SimpleSignalPdf(const SimpleSignalPdf &other, const char *name)
  : RooAbsPdf(other, name),
    m_x("x",this, other.m_x),
    m_m("m",this, other.m_m),
    m_s("s",this, other.m_s),
    m_xi("xi",this, other.m_xi),
    m_omega("omega",this, other.m_omega),
    m_alpha("alpha",this, other.m_alpha),
    m_xnorm("xnorm",this, other.m_xnorm)//,
    //m_xnorms("xnorms",this, other.m_xnorms),
    //m_m2("m2",this, other.m_m2),
    //m_s2("s2",this, other.m_s2),
    //m_norm2("norm2",this, other.m_norm2)
  {
}

TObject *SimpleSignalPdf::clone(const char *newname) const {
  return new SimpleSignalPdf(*this, newname);
}
SimpleSignalPdf::~SimpleSignalPdf() {
}

double SimpleSignalPdf::evaluate() const {
  double x = m_x;
  double m = m_m;
  double s = m_s;
  double xnorm = m_xnorm;
  double xi = m_xi;
  double omega = m_omega;
  double alpha = m_alpha;
  //double xnorms = m_xnorms;
  //double m2 = m_m2;
  //double s2 = m_s2;
  //double xnorm2 = m_norm2;

  if (omega <= 0) return 1e99;
  if (s <= 0) return 1e99;
  //if (s2 <= 0) return 1e99;

  double f = xnorm/(omega*TMath::Pi())*TMath::Exp(-TMath::Power(x-xi,2)/(2.0*omega*omega))*(0.5*(1+TMath::Erf(alpha*(x-xi)/omega)));
  f += (1-xnorm)/(TMath::Sqrt(2*TMath::Pi())*s)*TMath::Exp(-TMath::Power(x-m,2)/(2.0*s*s));
  //f += xnorm2/(TMath::Sqrt(2*TMath::Pi())*s2)*TMath::Exp(-TMath::Power(x-m2,2)/(2.0*s2*s2));

  return f;
}

SkewNormalPdf::SkewNormalPdf() {
}

SkewNormalPdf::SkewNormalPdf(const char *name, const char *title, RooAbsReal &_x,
                            RooAbsReal &_xi, RooAbsReal &_omega, RooAbsReal &_alpha)
 : RooAbsPdf(name, title),
    m_x("x", "x", this, _x),
    m_xi("xi", "xi", this, _xi),
    m_omega("omega", "omega", this, _omega),
    m_alpha("alpha", "alpha", this, _alpha)
  {
}

SkewNormalPdf::SkewNormalPdf(const SkewNormalPdf &other, const char *name)
  : RooAbsPdf(other, name),
    m_x("x",this, other.m_x),
    m_xi("xi",this, other.m_xi),
    m_omega("omega",this, other.m_omega),
    m_alpha("alpha",this, other.m_alpha)
  {
}

TObject *SkewNormalPdf::clone(const char *newname) const {
  return new SkewNormalPdf(*this, newname);
}

SkewNormalPdf::~SkewNormalPdf() {
}

double SkewNormalPdf::evaluate() const {
  double x = m_x;
  double xi = m_xi;
  double omega = m_omega;
  double alpha = m_alpha;

  double f = 2.0/(omega*std::sqrt(2*TMath::Pi()));
  f *= TMath::Exp(-TMath::Power(x-xi,2)/(2.0*omega*omega));
  f *= 0.5 * (1 + TMath::Erf( alpha*(x-xi)/(omega*TMath::Sqrt(2)) ) );

  return f;
}

