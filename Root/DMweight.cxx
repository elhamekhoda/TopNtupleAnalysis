#include "TMath.h"

//Double_t get_wfunction(Int_t E, Double_t x) {
Double_t get_wfunction(Int_t E, Int_t DM, Double_t x) {
  Double_t parfit[6]={0,1,0,0,0,0};
  Double_t invw=1.,w=-1.;
 

  //Vector official weight
  if (DM == 10){
    if (E == 400){
      parfit[0] = 400.124;
      parfit[1] = 6.14889;
      parfit[2] = 11.9118;
      parfit[3] = -0.0118351;
      parfit[4] = -40.1824;
      parfit[5] = 0.85065;
 
    } else  if (E == 500){
      parfit[0] = 499.737;
      parfit[1] = 9.68792;
      parfit[2] = 19.9502;
      parfit[3] = 0.000138141;
      parfit[4] = 7.91514;
      parfit[5] = -8.04166;
      
    } else  if (E == 600){
      parfit[0] = 599.459;
      parfit[1] = 10.2396;
      parfit[2] = 20.3767;
      parfit[3] = -0.00591912;
      parfit[4] = -4.38154;
      parfit[5] = 0.6424;
      
    } else  if (E == 750){
      parfit[0] = 749.381;
      parfit[1] = 13.086;
      parfit[2] = 25.067;
      parfit[3] = -0.00497272;
      parfit[4] = -2.95206;
      parfit[5] = 0.602543;
      
    } else  if (E == 850){
      parfit[0] = 849.344;
      parfit[1] = 16.2285;
      parfit[2] = 31.4054;
      parfit[3] = -0.00628461;
      parfit[4] = -3.67837;
      parfit[5] = 0.521856;
      
    } else if (E == 1000){
      parfit[0] = 999.073;
      parfit[1] = 18.0137;
      parfit[2] = 34.5754;
      parfit[3] = -0.0053398;
      parfit[4] = -2.88164;
      parfit[5] = 0.541665;
      
    } else if (E == 1250){
      parfit[0] = 1247.95;
      parfit[1] = 21.5733;
      parfit[2] = 41.7084;
      parfit[3] = -0.00456064;
      parfit[4] = -2.35614;
      parfit[5] = 0.550313;
      
    } else if (E == 1500){
      parfit[0] = 1499.01;
      parfit[1] = 25.6216;
      parfit[2] = 48.7057;
      parfit[3] = -0.00338051;
      parfit[4] = -1.40886;
      parfit[5] = 0.56835;
      
    } else if (E == 1750){
      parfit[0] = 1746.7;
      parfit[1] = 31.0178;
      parfit[2] = 60.2606;
      parfit[3] = -0.00387178;
      parfit[4] = -1.79854;
      parfit[5] = 0.552492;
      
    } else if (E == 2000){
      parfit[0] = 1998.61;
      parfit[1] = 35.4226;
      parfit[2] = 65.9738;
      parfit[3] = -0.00449366;
      parfit[4] = -2.58214;
      parfit[5] = 0.57883;
      
    } else if (E == 2250){    
      parfit[0] = 2247.18;
      parfit[1] = 40.1224;
      parfit[2] = 79.5558;
      parfit[3] = -0.00384645;
      parfit[4] = -1.72075;
      parfit[5] = 0.561076;
      
    } else if (E == 2500){
      parfit[0] = 2497.64;
      parfit[1] = 42.8198;
      parfit[2] = 86.0359;
      parfit[3] = -0.00396805;
      parfit[4] = -1.99716;
      parfit[5] = 0.581335;
      
    } else if (E == 2750){
      parfit[0] = 2747.14;
      parfit[1] = 47.5433;
      parfit[2] = 94.6818;
      parfit[3] = -0.00560427;
      parfit[4] = -4.09972;
      parfit[5] = 0.597447;
      
    } else if (E == 3000){
      parfit[0] = 2997.1;
      parfit[1] = 53.5402;
      parfit[2] = 110.478;
      parfit[3] = -0.00529422;
      parfit[4] = -3.04968;
      parfit[5] = 0.594732;
      
    } else if (E == 4000){
      parfit[0] = 3996.32;
      parfit[1] = 73.8613;
      parfit[2] = 165.746;
      parfit[3] = -0.00350419;
      parfit[4] = -1.84407;
      parfit[5] = 0.695899;
      
    } else if (E == 5000){
      parfit[0] = 4997.64;
      parfit[1] = 89.5965;
      parfit[2] = 241.192;
      parfit[3] = -0.00435407;
      parfit[4] = -2.91892;
      parfit[5] = 0.830158;
    } else return w;

    //==========> DM 100
    
  } else if (DM == 100) {
    if (E == 500){
      parfit[0] = 499.998;
      parfit[1] = 8.28714;
      parfit[2] = 17.0132;
      parfit[3] = -0.0175705;
      parfit[4] = -254.45;
      parfit[5] = 0.546174;
      
    } else if (E == 1000){
      parfit[0] = 998.718;
      parfit[1] = 18.4224;
      parfit[2] = 34.9387;
      parfit[3] = -0.00536071;
      parfit[4] = -2.84222;
      parfit[5] = 0.539503;
      
    } else if (E == 1250){
      parfit[0] = 1247.97;
      parfit[1] = 21.6464;
      parfit[2] = 42.1831;
      parfit[3] = -0.00417624;
      parfit[4] = -2.22236;
      parfit[5] = 0.554857;
      
    } else if (E == 1500){
      parfit[0] = 1499;
      parfit[1] = 25.2305;
      parfit[2] = 49.2915;
      parfit[3] = -0.00294422;
      parfit[4] = -1.12987;
      parfit[5] = 0.568716;
      
    } else if (E == 2000){
      parfit[0] = 1998.58;
      parfit[1] = 34.4549;
      parfit[2] = 65.1713;
      parfit[3] = -0.00388905;
      parfit[4] = -2.03507;
      parfit[5] = 0.576855;

    } else if (E == 2500){
      parfit[0] = 2496.91;
      parfit[1] = 44.0698;
      parfit[2] = 87.4671;
      parfit[3] = -0.00328159;
      parfit[4] = -1.426;
      parfit[5] = 0.580002;
      
    } else if (E == 2750){
      parfit[0] = 2747.92;
      parfit[1] = 48.4514;
      parfit[2] = 95.0448;
      parfit[3] = -0.00529111;
      parfit[4] = -3.73356;
      parfit[5] = 0.600105;
      
    } else if (E == 3000){
      parfit[0] = 2998.76;
      parfit[1] = 54.8438;
      parfit[2] = 113.713;
      parfit[3] = -0.0141772;
      parfit[4] = -64.6014;
      parfit[5] = 0.573053;
      
    } else if (E == 4000){
      parfit[0] = 3999.09;
      parfit[1] = 68.8166;
      parfit[2] = 162.39;
      parfit[3] = -0.00391027;
      parfit[4] = -2.18293;
      parfit[5] = 0.693692;
      
    } else if (E == 5000){
      parfit[0] = 4995;
      parfit[1] = 85.9746;
      parfit[2] = 240.127;
      parfit[3] = -0.00474744;
      parfit[4] = -3.3157;
      parfit[5] = 0.819507;  
    } else return w;

    //==========> DM 150
  } else if (DM == 150) {
    if (E == 500){
      parfit[0] = 499.961;
      parfit[1] = 8.58006;
      parfit[2] = 17.0161;
      parfit[3] = -0.0166036;
      parfit[4] = -191.09;
      parfit[5] = 0.557444;
      
    } else if (E == 1000){
      parfit[0] = 998.738;
      parfit[1] = 18.5059;
      parfit[2] = 35.2311;
      parfit[3] = -0.00538887;
      parfit[4] = -2.78157;
      parfit[5] = 0.535937;
      
    } else if (E == 1250){
      parfit[0] = 1248.12;
      parfit[1] = 21.6565;
      parfit[2] = 42.0514;
      parfit[3] = -0.00406496;
      parfit[4] = -2.11794;
      parfit[5] = 0.556926;
      
    } else if (E == 1500){
      parfit[0] = 1499.04;
      parfit[1] = 25.2529;
      parfit[2] = 49.3827;
      parfit[3] = -0.00289831;
      parfit[4] = -1.08681;
      parfit[5] = 0.568048;
      
    } else if (E == 2000){
      parfit[0] = 1998.58;
      parfit[1] = 34.4696;
      parfit[2] = 65.1568;
      parfit[3] = -0.00388844;
      parfit[4] = -2.0332;
      parfit[5] = 0.576872;

    } else if (E == 2500){
      parfit[0] = 2496.92;
      parfit[1] = 44.0553;
      parfit[2] = 87.4382;
      parfit[3] = -0.00327901;
      parfit[4] = -1.42475;
      parfit[5] = 0.580052;

    } else if (E == 2750){
      parfit[0] = 2747.92;
      parfit[1] = 48.4683;
      parfit[2] = 95.0364;
      parfit[3] = -0.00529117;
      parfit[4] = -3.73242;
      parfit[5] = 0.600084;
      
    } else if (E == 3000){
      parfit[0] = 2998.73;
      parfit[1] = 54.8509;
      parfit[2] = 113.734;
      parfit[3] = -0.0143569;
      parfit[4] = -69.3236;
      parfit[5] = 0.572978;
      
    } else if (E == 4000){
      parfit[0] = 3999.08;
      parfit[1] = 68.8205;
      parfit[2] = 162.404;
      parfit[3] = -0.00391147;
      parfit[4] = -2.18446;
      parfit[5] = 0.693673;
      
    } else if (E == 5000){
      parfit[0] = 4995;
      parfit[1] = 86.1525;
      parfit[2] = 240.06;
      parfit[3] = -0.00474802;
      parfit[4] = -3.31711;
      parfit[5] = 0.819574;
      
    } else return w;

    //==========> DM 200
   
  } else if (DM == 200) {
    if (E == 500){
      parfit[0] = 499.826;
      parfit[1] = 8.30698;
      parfit[2] = 14.8278;
      parfit[3] = -0.0135507;
      parfit[4] = -63.6207;
      parfit[5] = 0.624834;
      
    } else if (E == 1000){
      parfit[0] = 999.078;
      parfit[1] = 18.4415;
      parfit[2] = 35.0445;
      parfit[3] = -0.00544015;
      parfit[4] = -2.86037;
      parfit[5] = 0.537805;
      
    } else if (E == 1250){
      parfit[0] = 1248.06;
      parfit[1] = 21.5927;
      parfit[2] = 41.7832;
      parfit[3] = -0.00411116;
      parfit[4] = -2.15578;
      parfit[5] = 0.55732;
      
    } else if (E == 1500){
      parfit[0] = 1499;
      parfit[1] = 25;
      parfit[2] = 49.0476;
      parfit[3] = -0.00365759;
      parfit[4] = -1.58095;
      parfit[5] = 0.562246;
      
    } else if (E == 2000){
      parfit[0] = 1998.58;
      parfit[1] = 34.4626;
      parfit[2] = 65.1048;
      parfit[3] = -0.00387092;
      parfit[4] = -2.01948;
      parfit[5] = 0.577192;

    } else if (E == 2500){
      parfit[0] = 2497.02;
      parfit[1] = 43.9494;
      parfit[2] = 86.9593;
      parfit[3] = -0.00326836;
      parfit[4] = -1.41218;
      parfit[5] = 0.581874;

    } else if (E == 2750){
      parfit[0] = 2747.93;
      parfit[1] = 48.5937;
      parfit[2] = 95.9582;
      parfit[3] = -0.0055454;
      parfit[4] = -4.08553;
      parfit[5] = 0.596344;

    } else if (E == 3000){
      parfit[0] = 2998.76;
      parfit[1] = 54.9019;
      parfit[2] = 113.779;
      parfit[3] = -0.0143535;
      parfit[4] = -68.9475;
      parfit[5] = 0.572905;
      
    } else if (E == 4000){
      parfit[0] = 3998.49;
      parfit[1] = 68.6585;
      parfit[2] = 162.414;
      parfit[3] = -0.00391677;
      parfit[4] = -2.18454;
      parfit[5] = 0.693275;
      
    } else if (E == 5000){
      parfit[0] = 4995;
      parfit[1] = 85.4465;
      parfit[2] = 239.643;
      parfit[3] = -0.0045793;
      parfit[4] = -3.10818;
      parfit[5] = 0.822058;
      
    } else return w;

    //==========> DM 250
   
  } else if (DM == 250) {
    if (E == 500){
      parfit[0] = 484.402;
      parfit[1] = 20;
      parfit[2] = 3.4937;
      parfit[3] = -0.00729537;
      parfit[4] = -12.0111;
      parfit[5] = 1.24932;
      
    } else if (E == 1000){
      parfit[0] = 999.075;
      parfit[1] = 18.4126;
      parfit[2] = 34.3883;
      parfit[3] = -0.00570072;
      parfit[4] = -3.21687;
      parfit[5] = 0.54183;
      
    } else if (E == 1250){
      parfit[0] = 1247.59;
      parfit[1] = 20.9823;
      parfit[2] = 41.0963;
      parfit[3] = -0.00428151;
      parfit[4] = -2.35196;
      parfit[5] = 0.558917;
      
    } else if (E == 1500){
      parfit[0] = 1499.19;
      parfit[1] = 24.9724;
      parfit[2] = 48.3673;
      parfit[3] = -0.00293768;
      parfit[4] = -1.1166;
      parfit[5] = 0.574622;
      
    } else if (E == 2000){
      parfit[0] = 1999.21;
      parfit[1] = 33.7378;
      parfit[2] = 64.5886;
      parfit[3] = -0.00401426;
      parfit[4] = -2.14027;
      parfit[5] = 0.577273;

    } else if (E == 2500){
      parfit[0] = 2496.89;
      parfit[1] = 44.1419;
      parfit[2] = 87.4926;
      parfit[3] = -0.00325021;
      parfit[4] = -1.40747;
      parfit[5] = 0.580059;

    } else if (E == 2750){
      parfit[0] = 2747.76;
      parfit[1] = 48.9839;
      parfit[2] = 96.1852;
      parfit[3] = -0.00557551;
      parfit[4] = -4.11743;
      parfit[5] = 0.596051;
      
    } else if (E == 3000){
      parfit[0] = 2998.63;
      parfit[1] = 55.0235;
      parfit[2] = 114.017;
      parfit[3] = -0.0146575;
      parfit[4] = -76.9946;
      parfit[5] = 0.572456;
      
    } else if (E == 4000){
      parfit[0] = 3998.49;
      parfit[1] = 68.6538;
      parfit[2] = 162.31;
      parfit[3] = -0.00391199;
      parfit[4] = -2.18064;
      parfit[5] = 0.693387;
      
    } else if (E == 5000){
      parfit[0] = 4995;
      parfit[1] = 85.3655;
      parfit[2] = 239.45;
      parfit[3] = -0.00458952;
      parfit[4] = -3.11912;
      parfit[5] = 0.821846;
      
    } else return w;

    //==========> DM 350
   
  } else if (DM == 350) {
    if (E == 500){
      parfit[0] = 484.389;
      parfit[1] = 20;
      parfit[2] = 3.4883;
      parfit[3] = -0.00729776;
      parfit[4] = -12.0243;
      parfit[5] = 1.24942;
 
    } else if (E == 1000){
      parfit[0] = 998.812;
      parfit[1] = 18.2598;
      parfit[2] = 31.7672;
      parfit[3] = -0.00451147;
      parfit[4] = -2;
      parfit[5] = 0.579003;
      
    } else if (E == 1250){
      parfit[0] = 1247.49;
      parfit[1] = 21.6759;
      parfit[2] = 40.7607;
      parfit[3] = -0.00416126;
      parfit[4] = -2.17485;
      parfit[5] = 0.563956;
      
    } else if (E == 1500){
      parfit[0] = 1498.88;
      parfit[1] = 25.1789;
      parfit[2] = 46.709;
      parfit[3] = -0.00286227;
      parfit[4] = -1.22944;
      parfit[5] = 0.589739;
      
    } else if (E == 2000){
      parfit[0] = 1999.24;
      parfit[1] = 33.7515;
      parfit[2] = 64.3117;
      parfit[3] = -0.00404773;
      parfit[4] = -2.17885;
      parfit[5] = 0.578349;

    } else if (E == 2500){
      parfit[0] = 2496.94;
      parfit[1] = 44.1604;
      parfit[2] = 87.3302;
      parfit[3] = -0.00324962;
      parfit[4] = -1.41399;
      parfit[5] = 0.58073;

    } else if (E == 2750){
      parfit[0] = 2747.28;
      parfit[1] = 48.7998;
      parfit[2] = 97.2093;
      parfit[3] = -0.00560021;
      parfit[4] = -4.16796;
      parfit[5] = 0.593056;

    } else if (E == 3000){
      parfit[0] = 2998.55;
      parfit[1] = 55.2315;
      parfit[2] = 114.539;
      parfit[3] = -0.0149336;
      parfit[4] = -84.395;
      parfit[5] = 0.570796;
      
    } else if (E == 4000){
      parfit[0] = 3995.77;
      parfit[1] = 66.2714;
      parfit[2] = 152.931;
      parfit[3] = -0.00353256;
      parfit[4] = -1.9113;
      parfit[5] = 0.706866;
      
    } else if (E == 5000){
      parfit[0] = 4995.44;
      parfit[1] = 86.2824;
      parfit[2] = 240.372;
      parfit[3] = -0.00470012;
      parfit[4] = -3.26219;
      parfit[5] = 0.820514;
      
    } else return w;

    //==========> DM 500
   
  } else if (DM == 500) {
    if (E == 500){
      parfit[0] = 484.381;
      parfit[1] = 20;
      parfit[2] = 3.49847;
      parfit[3] = -0.00729177;
      parfit[4] = -11.9978;
      parfit[5] = 1.24949;

    } else if (E == 1000){
      parfit[0] = 1008.82;
      parfit[1] = 5.04099;
      parfit[2] = -0.5;
      parfit[3] = -0.00747501;
      parfit[4] = -14.4992;
      parfit[5] = 1.02109;
      
    } else if (E == 1250){
      parfit[0] = 1246.99;
      parfit[1] = 20.8851;
      parfit[2] = 34.0263;
      parfit[3] = -0.00231057;
      parfit[4] = -1.06322;
      parfit[5] = 0.663066;
      
    } else if (E == 1500){
      parfit[0] = 1498.68;
      parfit[1] = 25.6699;
      parfit[2] = 45.7462;
      parfit[3] = -0.00338026;
      parfit[4] = -1.50939;
      parfit[5] = 0.58763;
      
    } else if (E == 2000){
      parfit[0] = 1998.68;
      parfit[1] = 34.2846;
      parfit[2] = 63.2968;
      parfit[3] = -0.00384706;
      parfit[4] = -2.07889;
      parfit[5] = 0.585403;

    } else if (E == 2500){
      parfit[0] = 2496.45;
      parfit[1] = 43.032;
      parfit[2] = 83.8406;
      parfit[3] = -0.00333365;
      parfit[4] = -1.47465;
      parfit[5] = 0.590692;

    } else if (E == 2750){
      parfit[0] = 2746.77;
      parfit[1] = 49.901;
      parfit[2] = 96.5765;
      parfit[3] = -0.00555723;
      parfit[4] = -4.05705;
      parfit[5] = 0.594844;      

    } else if (E == 3000){
      parfit[0] = 2998.56;
      parfit[1] = 55.138;
      parfit[2] = 114.063;
      parfit[3] = -0.0157225;
      parfit[4] = -112.785;
      parfit[5] = 0.571634;
      
    } else if (E == 4000){
      parfit[0] = 3995;
      parfit[1] = 66.676;
      parfit[2] = 152.61;
      parfit[3] = -0.00349828;
      parfit[4] = -1.87346;
      parfit[5] = 0.706785;
      
    } else if (E == 5000){
      parfit[0] = 4995;
      parfit[1] = 88.6412;
      parfit[2] = 233.937;
      parfit[3] = -0.00408459;
      parfit[4] = -2.62276;
      parfit[5] = 0.834685;     
    } else return w;


    //==========> DM 750
   
  } else if (DM == 750) {
    if (E == 500){
      parfit[0] = 484.389;
      parfit[1] = 20;
      parfit[2] = 3.4883;
      parfit[3] = -0.00729776;
      parfit[4] = -12.0243;
      parfit[5] = 1.24942;
 

    } else if (E == 1000){
      parfit[0] = 1010.83;
      parfit[1] = 4.38171;
      parfit[2] = -0.5;
      parfit[3] = -0.00573801;
      parfit[4] = -7.03038;
      parfit[5] = 1.03944;
      
    } else if (E == 1250){
      parfit[0] = 1261.97;
      parfit[1] = 20;
      parfit[2] = -3.14851;
      parfit[3] = -0.0041857;
      parfit[4] = -4.24715;
      parfit[5] = 1.07144;
      
    } else if (E == 1500){
      parfit[0] = 1505.54;
      parfit[1] = 6.07638;
      parfit[2] = -0.5;
      parfit[3] = -0.00348029;
      parfit[4] = -2.70613;
      parfit[5] = 1.02705;
      
    } else if (E == 2000){
      parfit[0] = 1997.98;
      parfit[1] = 34.0873;
      parfit[2] = 57.9405;
      parfit[3] = -0.00474275;
      parfit[4] = -3.10621;
      parfit[5] = 0.605455;

    } else if (E == 2500){
      parfit[0] = 2496.85;
      parfit[1] = 42.1293;
      parfit[2] = 82.5006;
      parfit[3] = -0.00362703;
      parfit[4] = -1.67273;
      parfit[5] = 0.592294;

    } else if (E == 2750){
      parfit[0] = 2746.9;
      parfit[1] = 47.7077;
      parfit[2] = 93.0044;
      parfit[3] = -0.00586957;
      parfit[4] = -4.63601;
      parfit[5] = 0.601598;      

    } else if (E == 3000){
      parfit[0] = 2997.82;
      parfit[1] = 60.0468;
      parfit[2] = 117.287;
      parfit[3] = -0.017074;
      parfit[4] = -176.59;
      parfit[5] = 0.56938;
      
    } else if (E == 4000){
      parfit[0] = 3996.84;
      parfit[1] = 69.7022;
      parfit[2] = 161.085;
      parfit[3] = -0.00358969;
      parfit[4] = -1.94589;
      parfit[5] = 0.698152;
      
    } else if (E == 5000){
      parfit[0] = 4995;
      parfit[1] = 89.4674;
      parfit[2] = 240.287;
      parfit[3] = -0.00421784;
      parfit[4] = -2.72609;
      parfit[5] = 0.827526;
      
    } else return w;


    //==========> DM 1000
   
  } else if (DM == 1000) {
    if (E == 500){
      parfit[0] = 484.375;
      parfit[1] = 20;
      parfit[2] = 3.49924;
      parfit[3] = -0.00728727;
      parfit[4] = -11.9821;
      parfit[5] = 1.24977;
      
    } else if (E == 1000){
      parfit[0] = 1010.81;
      parfit[1] = 4.38569;
      parfit[2] = -0.5;
      parfit[3] = -0.00573806;
      parfit[4] = -6.99558;
      parfit[5] = 1.03923;
      
    } else if (E == 1250){
      parfit[0] = 1261.98;
      parfit[1] = 20;
      parfit[2] = -3.14187;
      parfit[3] = -0.00418904;
      parfit[4] = -4.25206;
      parfit[5] = 1.07124;
      
    } else if (E == 1500){
      parfit[0] = 1505.53;
      parfit[1] = 6.08824;
      parfit[2] = -0.5;
      parfit[3] = -0.00348093;
      parfit[4] = -2.70688;
      parfit[5] = 1.02703;
      
    } else if (E == 2000){
      parfit[0] = 2011.17;
      parfit[1] = 45.5893;
      parfit[2] = -7.90874;
      parfit[3] = -0.00453799;
      parfit[4] = -4.94582;
      parfit[5] = 1.06346;

    } else if (E == 2500){
      parfit[0] = 2496.54;
      parfit[1] = 44.0797;
      parfit[2] = 72.1588;
      parfit[3] = -0.00340733;
      parfit[4] = -1.59159;
      parfit[5] = 0.628734;

    } else if (E == 2750){
      parfit[0] = 2749.47;
      parfit[1] = 47.7251;
      parfit[2] = 83.9242;
      parfit[3] = -0.00688587;
      parfit[4] = -6.98199;
      parfit[5] = 0.62482;

    } else if (E == 3000){
      parfit[0] = 2998.21;
      parfit[1] = 58.7827;
      parfit[2] = 109.338;
      parfit[3] = -0.0149719;
      parfit[4] = -81.2999;
      parfit[5] = 0.584706;
      
    } else if (E == 4000){
      parfit[0] = 3995.64;
      parfit[1] = 68.6861;
      parfit[2] = 156.699;
      parfit[3] = -0.00382973;
      parfit[4] = -2.05315;
      parfit[5] = 0.694198;
      
    } else if (E == 5000){
      parfit[0] = 4995;
      parfit[1] = 83.4848;
      parfit[2] = 227.043;
      parfit[3] = -0.00432033;
      parfit[4] = -2.81062;
      parfit[5] = 0.829903;
      
    } else return w;


    //==========> DM 10000
   
  } else if (DM == 10000) {
    if (E == 500){
      parfit[0] = 484.412;
      parfit[1] = 20;
      parfit[2] = 3.50587;
      parfit[3] = -0.00728501;
      parfit[4] = -11.967;
      parfit[5] = 1.24953;
      
    } else if (E == 1000){
      parfit[0] = 1010.82;
      parfit[1] = 4.39068;
      parfit[2] = -0.5;
      parfit[3] = -0.00574832;
      parfit[4] = -7.05486;
      parfit[5] = 1.03923;
      
    } else if (E == 1250){
      parfit[0] = 1261.94;
      parfit[1] = 20;
      parfit[2] = -3.14529;
      parfit[3] = -0.00418941;
      parfit[4] = -4.25319;
      parfit[5] = 1.07131;
      
    } else if (E == 1500){
      parfit[0] = 1508.95;
      parfit[1] = 25.8098;
      parfit[2] = -4.10133;
      parfit[3] = -0.00306721;
      parfit[4] = -2.4801;
      parfit[5] = 1.07962;
      
    } else if (E == 2000){
      parfit[0] = 2011.32;
      parfit[1] = 45.7432;
      parfit[2] = -7.95452;
      parfit[3] = -0.0045378;
      parfit[4] = -4.94703;
      parfit[5] = 1.0637;

    } else if (E == 2500){
      parfit[0] = 2514.64;
      parfit[1] = 34.8682;
      parfit[2] = -4.29425;
      parfit[3] = -0.00490092;
      parfit[4] = -4.43461;
      parfit[5] = 1.03212;

    } else if (E == 2750){
      parfit[0] = 2761.94;
      parfit[1] = 41.1018;
      parfit[2] = -8.9863;
      parfit[3] = -0.00465328;
      parfit[4] = -5.09432;
      parfit[5] = 1.0659;      

    } else if (E == 3000){
      parfit[0] = 3004.06;
      parfit[1] = 20;
      parfit[2] = -3.92594;
      parfit[3] = -0.0173018;
      parfit[4] = -371.486;
      parfit[5] = 1.02604;
      
    } else if (E == 4000){
      parfit[0] = 4014.46;
      parfit[1] = 34.0788;
      parfit[2] = -7.72417;
      parfit[3] = -0.00241551;
      parfit[4] = -1.20264;
      parfit[5] = 1.04953;
      
    } else if (E == 5000){
      parfit[0] = 5013.57;
      parfit[1] = 36.8953;
      parfit[2] = -9.58699;
      parfit[3] = -0.00318056;
      parfit[4] = -1.30532;
      parfit[5] = 1.00174;
      
    } else return w;

    /*

    //==========> DM 100
   
    } else if (DM == 100) {
    if (E == 500){

    } else if (E == 1000){

    } else if (E == 1250){

    } else if (E == 1500){

    } else if (E == 2000){

    } else if (E == 3000){

    } else if (E == 4000){

    } else if (E == 5000){

    } else return w;
    */
 
    
  } else return w; // ==============+> END DM loop


  
  invw = ( 2 * parfit[2] / (TMath::Pi() * parfit[1]) )  /  TMath::Max(1.e-10, (1 + (x-parfit[0])*(x-parfit[0])/(parfit[1]*parfit[1]) ) ) + parfit[4]*exp(parfit[3]*x) + parfit[5]  ; // Lorentz par2 = hauteur par1 = largeur, par0 = position pic + pol1
  
  w = 1/invw;
  return w;
}