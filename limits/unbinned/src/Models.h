#ifndef _MODELS_H
#define _MODELS_H

#include "TMath.h"
#include "RooAbsPdf.h"
#include "RooRealProxy.h"

class BkgFallPdf : public RooAbsPdf {
  public:
  RooRealProxy m_x;
  RooRealProxy m_p1;
  RooRealProxy m_p2;
  //RooRealProxy m_p3;

  BkgFallPdf();
  BkgFallPdf(const char *name, const char *title, RooAbsReal &_x,
             RooAbsReal &_p1, RooAbsReal &_p2);//,
             //RooAbsReal &_p3);
  BkgFallPdf(const BkgFallPdf &other, const char *name = 0);
  virtual TObject *clone(const char *newname) const;
  virtual ~BkgFallPdf();
  double evaluate() const;

  ClassDef(BkgFallPdf, 1)
};

class BkgDijetsPdf : public RooAbsPdf {
  public:
  RooRealProxy m_x;
  RooRealProxy m_p1;
  RooRealProxy m_p2;
  RooRealProxy m_p3;

  BkgDijetsPdf();
  BkgDijetsPdf(const char *name, const char *title, RooAbsReal &_x,
             RooAbsReal &_p1, RooAbsReal &_p2,
             RooAbsReal &_p3);
  BkgDijetsPdf(const BkgDijetsPdf &other, const char *name = 0);
  virtual TObject *clone(const char *newname) const;
  virtual ~BkgDijetsPdf();
  double evaluate() const;

  ClassDef(BkgDijetsPdf, 1)
};

class BkgWtbPdf : public RooAbsPdf {
  public:
  RooRealProxy m_x;
  RooRealProxy m_p1;
  RooRealProxy m_p2;

  BkgWtbPdf();
  BkgWtbPdf(const char *name, const char *title, RooAbsReal &_x,
             RooAbsReal &_p1, RooAbsReal &_p2);
  BkgWtbPdf(const BkgWtbPdf &other, const char *name = 0);
  virtual TObject *clone(const char *newname) const;
  virtual ~BkgWtbPdf();
  double evaluate() const;

  ClassDef(BkgWtbPdf, 1)
};


class SignalPdf : public RooAbsPdf {
  public:
  RooRealProxy m_x;
  RooRealProxy m_m;
  RooRealProxy m_s;
  RooRealProxy m_xi;
  RooRealProxy m_omega;
  RooRealProxy m_alpha;
  RooRealProxy m_norm;

  RooRealProxy m_m2;
  RooRealProxy m_s2;
  RooRealProxy m_norm2;

  RooRealProxy m_m3;
  RooRealProxy m_s3;
  RooRealProxy m_norm3;

  SignalPdf();
  SignalPdf(const char *name, const char *title, RooAbsReal &_x,
            RooAbsReal &_m, RooAbsReal &_s, RooAbsReal &_xi, RooAbsReal &_omega, RooAbsReal &_alpha, RooAbsReal &_xnorm,
            RooAbsReal &_m2, RooAbsReal &_s2, RooAbsReal &_norm2,
            RooAbsReal &_m3, RooAbsReal &_s3, RooAbsReal &_norm3);

  SignalPdf(const SignalPdf &other, const char *name = 0);
  virtual TObject *clone(const char *newname) const;
  virtual ~SignalPdf();
  double evaluate() const;

  ClassDef(SignalPdf, 1)
};

class SimpleSignalPdf : public RooAbsPdf {
  public:
  RooRealProxy m_x;
  RooRealProxy m_m;
  RooRealProxy m_s;
  RooRealProxy m_xi;
  RooRealProxy m_omega;
  RooRealProxy m_alpha;
  RooRealProxy m_xnorm;
  //RooRealProxy m_xnorms;
  //RooRealProxy m_m2;
  //RooRealProxy m_s2;
  //RooRealProxy m_norm2;

  SimpleSignalPdf();
  SimpleSignalPdf(const char *name, const char *title, RooAbsReal &_x,
            RooAbsReal &_m, RooAbsReal &_s, RooAbsReal &_xi, RooAbsReal &_omega, RooAbsReal &_alpha, RooAbsReal &_xnorm);//,
//            RooAbsReal &_m2, RooAbsReal &_s2, RooAbsReal &_norm2, RooAbsReal &_norms);

  SimpleSignalPdf(const SimpleSignalPdf &other, const char *name = 0);
  virtual TObject *clone(const char *newname) const;
  virtual ~SimpleSignalPdf();
  double evaluate() const;

  ClassDef(SimpleSignalPdf, 1)
};

class SkewNormalPdf : public RooAbsPdf {
  public:
  RooRealProxy m_x;
  RooRealProxy m_xi;
  RooRealProxy m_omega;
  RooRealProxy m_alpha;

  SkewNormalPdf();
  SkewNormalPdf(const char *name, const char *title, RooAbsReal &_x,
                RooAbsReal &_xi, RooAbsReal &_omega, RooAbsReal &_alpha);

  SkewNormalPdf(const SkewNormalPdf &other, const char *name = 0);
  virtual TObject *clone(const char *newname) const;
  virtual ~SkewNormalPdf();
  double evaluate() const;

  ClassDef(SkewNormalPdf, 1)
};

#endif

