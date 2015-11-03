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
    
    fake_map_resolved_e = (TH2F*)m_fake_rootfile.Get("2Dfake_resolved_e")->Clone();
    fake_map_resolved_e->SetDirectory(0);
    
    fake_map_resolved_mu = (TH2F*)m_fake_rootfile.Get("2Dfake_resolved_mu")->Clone();
    fake_map_resolved_mu->SetDirectory(0);
    
    fake_map_boosted_e = (TH2F*)m_fake_rootfile.Get("2Dfake_boosted_e")->Clone();
    fake_map_boosted_e->SetDirectory(0);
    
    fake_map_boosted_mu = (TH2F*)m_fake_rootfile.Get("2Dfake_boosted_mu")->Clone();    
    fake_map_boosted_mu->SetDirectory(0);  
       
  }
  
}
  
MMUtils::~MMUtils(){
  
  delete eff_map_resolved_e  ;
  delete eff_map_resolved_e  ;
  delete eff_map_resolved_mu ;
  delete eff_map_resolved_mu ;
  
  delete fake_map_resolved_e ;
  delete fake_map_resolved_e ;
  delete fake_map_resolved_mu;
  delete fake_map_resolved_mu;
  
  delete eff_map;
  delete fake_map;
} 

float MMUtils::getMMweights(const Event &evt, const std::string &s) {
   
   float lepPt(0);
   float closejl_pT(0); 
   float closejl_DR(99); 
   
   bool isTight;

   bool isBoosted(0);
   if (!(evt.passes("rejets")) || !(evt.passes("rmujets")))      isBoosted = true;	    
   
   TLorentzVector lepP4; 
   bool isElectron(0);   
   if (evt.electron().size() == 1)    {
       isElectron = true;
       lepP4 = evt.electron()[0].mom();
       isTight = evt.electron()[0].isTightPP();
       
   }else if (evt.muon().size() == 1){	       
       lepP4 = evt.muon()[0].mom();
       isTight = evt.muon()[0].isTight();
   }
   
   lepPt = lepP4.Perp()*1e-3; 
   
   float deltaRapidity2 = 99;
   float deltaPhi2	= 99;
   float deltaR_tmp     = 99;

   size_t jet_idx = 0;
   for (; jet_idx < evt.jet().size(); ++jet_idx){  

       deltaRapidity2 = pow(evt.jet()[jet_idx].mom().Rapidity() - lepP4.Eta(), 2);    
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
	   fake_map = fake_map_boosted_e;
	}
	else{
	   eff_map = eff_map_boosted_mu;
	   fake_map = fake_map_boosted_mu;
	}
   }
   else{
   	if (isElectron){
	   eff_map = eff_map_resolved_e;
	   fake_map = fake_map_resolved_e;
	}	
	else{
	   eff_map = eff_map_resolved_mu;
	   fake_map = fake_map_resolved_mu;
	}
   }//isBoosted	
   	
   
   if(lepPt>eff_map->GetXaxis()->GetXmax() || lepPt>fake_map->GetXaxis()->GetXmax())  	    
   	lepPt = 0.95*eff_map->GetXaxis()->GetXmax(); 
   
   if(closejl_DR>eff_map->GetYaxis()->GetXmax() || closejl_pT>fake_map->GetYaxis()->GetXmax())    
   	closejl_DR = 0.95*eff_map->GetYaxis()->GetXmax(); 
   
   // --> Getting eff rate  
   float effRate = eff_map->GetBinContent(eff_map->FindBin(lepPt, closejl_DR));

   //--> Getting fake rate
   float fakeRate = fake_map->GetBinContent(fake_map->FindBin(lepPt, closejl_pT));
      
   //--> Implementing weights
   float Weight = 1;
     
   if (isTight){
     	if((effRate - fakeRate) !=0.)	Weight = fakeRate*(effRate - 1)/(effRate - fakeRate); 
	else				std::cerr << "Error: effRate - fakeRate == 0";
   }
   else {	   
   	if((effRate - fakeRate) !=0.)	Weight = fakeRate*effRate/(effRate - fakeRate);
   	else				std::cerr << "Error: effRate - fakeRate == 0";
   
   }//isTight

   return Weight;  

}//getMMweights

