#include "TMath.h"

Double_t wfunction(Int_t E, Double_t x) {
  Double_t parfit[6]={0,1,0,0,0,0};
  Double_t invw=1.,w=-1.;

  if (E == 500){
  
    parfit[0] = 499.457;
    parfit[1] = 8.60731;
    parfit[2] = 16.3864;
    parfit[3] = -0.00742983;
    parfit[4] = 6.00826;
    parfit[5] = 0.365257;
    
  } else if (E == 1000){
    
    parfit[0] = 997.131;
    parfit[1] = -20.2489;
    parfit[2] = -35.5745;
    parfit[3] = -7.06233e-05;
    parfit[4] = 3.18654;
    parfit[5] = -2.4417;
    
  } else if (E == 2000){
 
    parfit[0] = 1995.73;
    parfit[1] = 39.7748;
    parfit[2] = 68.5862;
    parfit[3] = -0.0029858;
    parfit[4] = 0.702608;
    parfit[5] = 0.565776;

  } else if (E == 3000){
    
    parfit[0] = 2996.66;
    parfit[1] = 58.0755;
    parfit[2] = 108.767;
    parfit[3] = -0.00286079;
    parfit[4] = 1.17198;
    parfit[5] = 0.579856;
    
  } else if (E == 4000){
    
    parfit[0] = 3995.15;
    parfit[1] = 73.8778;
    parfit[2] = 150.954;
    parfit[3] = -0.00291672;
    parfit[4] = 1.32313;
    parfit[5] = 0.641975;
    
  } else if (E == 5000){
    
    parfit[0] = 4991.61;
    parfit[1] = -85.3154;
    parfit[2] = -194.41;
    parfit[3] = -0.0042171;
    parfit[4] = 2.69907;
    parfit[5] = 0.753666;
    
  } else return w;
  
 
  invw = ( 2 * parfit[2] / (TMath::Pi() * parfit[1]) )  /  TMath::Max(1.e-10, (1 + (x-parfit[0])*(x-parfit[0])/(parfit[1]*parfit[1]) ) ) + parfit[4]*exp(parfit[3]*x)+parfit[5]  ; // Lorentz par2 = hauteur par1 = largeur, par0 = position pic + pol1
  w = 1.0/invw;
  return w;}
