/**
 * @brief Code to parse input parameters without BOOST to avoid the unnecessary overload of libraries needed.
 * @author Danilo Enoque Ferreira de Lima <dferreir@cern.ch> 
 */
#include "TopNtupleAnalysis/MMUtils.h"

#include <getopt.h>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>

#include <vector>
#include <algorithm>
#include "TFile.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TH1D.h"
#include "TH2D.h"
#include "TLorentzVector.h"


MMUtils::MMUtils(const std::string &eff_filename, const std::string &fake_filename) {

  if (eff_filename!="" && fake_filename!=""){
      
    TFile m_eff_rootfile(eff_filename.c_str(), "r");
    
    eff_map_resolved_e = (TH2F*)m_eff_rootfile.Get("eff_pTdr_resolved_e")->Clone();
    eff_map_resolved_e->SetDirectory(0);
    
    eff_map_resolved_mu = (TH2F*)m_eff_rootfile.Get("eff_pTdr_resolved_mu")->Clone();
    eff_map_resolved_mu->SetDirectory(0);
    
    eff_map_boosted_e = (TH2F*)m_eff_rootfile.Get("eff_pTdr_boosted_e")->Clone();
    eff_map_boosted_e->SetDirectory(0);
    
    eff_map_boosted_mu = (TH2F*)m_eff_rootfile.Get("eff_pTdr_boosted_mu")->Clone();    
    eff_map_boosted_mu->SetDirectory(0);
      
    TFile m_fake_rootfile(fake_filename.c_str(), "r");
        
    fake_pt_resolved_e = (TH1F*)m_fake_rootfile.Get("fakeRate_pt_resolved_e")->Clone();
    fake_pt_resolved_e->SetDirectory(0);
    
    //fake_pt_resolved_mu = (TH1F*)m_fake_rootfile.Get("fakeRate_pt_resolved_mu")->Clone();
    //fake_pt_resolved_mu->SetDirectory(0);
    
    fake_pt_boosted_e = (TH1F*)m_fake_rootfile.Get("fakeRate_pt_boosted_e")->Clone();
    fake_pt_boosted_e->SetDirectory(0);
    
    //fake_pt_boosted_mu = (TH1F*)m_fake_rootfile.Get("fakeRate_pt_boosted_mu")->Clone();    
    //fake_pt_boosted_mu->SetDirectory(0); 

    //fake_dr_resolved_e  = (TH1F*)m_fake_rootfile.Get("fakeRate_dr_resolved_e")->Clone();
    //fake_dr_resolved_e->SetDirectory(0); 
    
    fake_dr_resolved_mu = (TH1F*)m_fake_rootfile.Get("fakeRate_dr_resolved_mu")->Clone();
    fake_dr_resolved_mu->SetDirectory(0); 
    
    //fake_dr_boosted_e   = (TH1F*)m_fake_rootfile.Get("fakeRate_dr_boosted_e")->Clone();
    //fake_dr_boosted_e->SetDirectory(0); 
    
    fake_dr_boosted_mu  = (TH1F*)m_fake_rootfile.Get("fakeRate_dr_boosted_mu")->Clone();
    fake_dr_boosted_mu->SetDirectory(0); 

  }
  
}
  
MMUtils::~MMUtils(){
  
  delete eff_map_resolved_e  ;
  delete eff_map_resolved_mu  ;
  delete eff_map_boosted_e ;
  delete eff_map_boosted_mu ;
  
  delete fake_pt_resolved_e ;
  //delete fake_pt_resolved_mu ;
  delete fake_pt_boosted_e;
  //delete fake_pt_boosted_mu;
  
  //delete fake_dr_resolved_e ;
  delete fake_dr_resolved_mu ;
  //delete fake_dr_boosted_e;
  delete fake_dr_boosted_mu;
  
  delete eff_map;
  delete fake_pt;
  delete fake_dr;
} 

float MMUtils::getMMweights(const Event &evt, int runMM_StatErr) {
   
   float lepPt(0);
   float closejl_pT(0); 
   float closejl_DR(99); 
   
   bool isTight;

   bool isBoosted(0);
   if (evt.passes("bejets") || evt.passes("bmujets"))      isBoosted = true;    
   
   TLorentzVector lepP4; 
   bool isElectron(0);   
   if (evt.electron().size() == 1 && evt.muon().size() == 0)    {
       isElectron = true;
       lepP4 = evt.electron()[0].mom();
       isTight = evt.electron()[0].isTightPP();
       
   }else if (evt.electron().size() == 0 && evt.muon().size() == 1){	       
       lepP4 = evt.muon()[0].mom();
       
       bool trig_unprescaled = evt.muon()[0].HLT_mu20_iloose_L1MU15() || evt.muon()[0].HLT_mu50();
       
       isTight = evt.muon()[0].isTight();
       if( !trig_unprescaled )	isTight = false;
   }
   
   lepPt = lepP4.Perp()*1e-3; 
   
   float deltaRapidity2 = 99;
   float deltaPhi2	= 99;
   float deltaR_tmp     = 99;

   size_t jet_idx = 0;
   for (; jet_idx < evt.jet().size(); ++jet_idx){  

       deltaRapidity2 = pow(evt.jet()[jet_idx].mom().Rapidity() - lepP4.Rapidity(), 2);    
       deltaPhi2 = pow(evt.jet()[jet_idx].mom().DeltaPhi(lepP4), 2);	     
       deltaR_tmp = sqrt(deltaPhi2 + deltaRapidity2);

       if (deltaR_tmp < closejl_DR){
   	  closejl_DR = deltaR_tmp;
          closejl_pT = evt.jet()[jet_idx].mom().Perp()*1e-3;
       }  
   }//for 

   if (isBoosted){
   	if (isElectron)	{
	   eff_map  = eff_map_boosted_e;
	   fake_pt = fake_pt_boosted_e;
	   //fake_dr = fake_dr_resolved_e;
	}
	else{
	   eff_map = eff_map_boosted_mu;
	   //fake_pt = fake_pt_resolved_mu;
	   fake_dr = fake_dr_boosted_mu;
	}
   }
   else{
   	if (isElectron){
	   eff_map = eff_map_resolved_e;
	   //fake_dr = fake_dr_resolved_e;
	   fake_pt = fake_pt_resolved_e; 
	}	
	else{
	   eff_map = eff_map_resolved_mu;
	   fake_dr = fake_dr_resolved_mu; 
	   //fake_pt = fake_pt_resolved_mu;
	}
   }//isBoosted	
   
   
   float fakeRate(0.); 
   float fakeRate_err(0.);
 
   // --> Getting eff rate  

   int binx(0);
   int biny(0);
   
   if(lepPt>eff_map->GetXaxis()->GetXmax()){
          binx = eff_map->GetXaxis()->FindBin(0.95*eff_map->GetXaxis()->GetXmax());
   }else{
          binx = eff_map->GetXaxis()->FindBin(lepPt);
   }
   if(closejl_DR>eff_map->GetYaxis()->GetXmax()){
	  biny = eff_map->GetYaxis()->FindBin(0.95*eff_map->GetYaxis()->GetXmax());
   }else{
	  biny = eff_map->GetYaxis()->FindBin(closejl_DR);
   }
   
   int bin            = eff_map->GetBin(binx, biny, 0);
   float realRate     = eff_map->GetBinContent(bin);
   float realRate_err = eff_map->GetBinError(bin); 
	     
   binx = 0;
   
   if(!isElectron){
     
     if(closejl_DR>fake_dr->GetXaxis()->GetXmax())	binx = fake_dr->GetXaxis()->FindBin(0.95*fake_dr->GetXaxis()->GetXmax());
     else						binx = fake_dr->GetXaxis()->FindBin(closejl_DR);

     fakeRate     = fake_dr->GetBinContent(binx);
     fakeRate_err = fake_dr->GetBinError(binx);
     
   } else {
     
     if(lepPt>fake_pt->GetXaxis()->GetXmax())	binx = fake_pt->GetXaxis()->FindBin(0.95*fake_pt->GetXaxis()->GetXmax());
     else					binx = fake_pt->GetXaxis()->FindBin(lepPt);
     
     fakeRate     = fake_pt->GetBinContent(binx);
     fakeRate_err = fake_pt->GetBinError(binx);
     
   }//isElectron
      
   //--> Implementing weights
   float Weight = 1;

   //Maximazing the stat error for runMM_StatErr==1 || runMM_StatErr==2
   if (runMM_StatErr==1){
     realRate += realRate_err;
     fakeRate -= fakeRate_err;
   } else if (runMM_StatErr==2){
     realRate -= realRate_err;
     fakeRate += fakeRate_err;
   }
   	
   if (isTight){
     if(realRate>0 && fakeRate>0)  Weight = fakeRate*(realRate - 1)/(realRate - fakeRate); 
     else{
     	     std::cerr << "Error: realRate or fakeRate equal to 0 " << std::endl;	     
	     Weight = 0;
     }
   }
   else {	
     if(realRate>0 && fakeRate>0)  Weight = fakeRate*realRate/(realRate - fakeRate);
     else{
     	     std::cerr << "Error: realRate or fakeRate equal to 0 " << std::endl;
     	     Weight = 0;
     }       
   
   }//isTight
   
   //if(!isTight)	std::cout << "is tight? " << isTight << " - QCD weight" << Weight << std::endl;
   
   return Weight;  

}//getMMweights

