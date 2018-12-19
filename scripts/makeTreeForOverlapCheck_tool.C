#include <iostream>
#include "TFile.h"
#include "TTree.h"

void makeTreeForOverlapCheck_tool(std::string f_out_name){
	
  TFile f_out((f_out_name+"_tt_ljets.root").c_str(), "RECREATE");
  TTree* m_tree = new TTree("overlap", "overlap");
  	
  int run_number(0);
  unsigned long long int event_number(0);
  std::vector<int> *region=0;
  double m_tt(0);
  

  m_tree->Branch("run_number", &run_number);
  m_tree->Branch("event_number", &event_number);
  m_tree->Branch("region", &region);
  m_tree->Branch("m_tt", &m_tt);
 
  
  std::vector<std::pair<string,int>> todo;
  todo.push_back(std::make_pair(std::string("hist_re1.root"),850));
  todo.push_back(std::make_pair(std::string("hist_re2.root"),851));
  todo.push_back(std::make_pair(std::string("hist_re3.root"),852));
  todo.push_back(std::make_pair(std::string("hist_rmu1.root"),860));
  todo.push_back(std::make_pair(std::string("hist_rmu2.root"),861));
  todo.push_back(std::make_pair(std::string("hist_rmu3.root"),862));
  todo.push_back(std::make_pair(std::string("hist_be1.root"),870));
  todo.push_back(std::make_pair(std::string("hist_be2.root"),871));
  todo.push_back(std::make_pair(std::string("hist_be3.root"),872));
  todo.push_back(std::make_pair(std::string("hist_bmu1.root"),880));
  todo.push_back(std::make_pair(std::string("hist_bmu2.root"),881));
  todo.push_back(std::make_pair(std::string("hist_bmu3.root"),882));
   

  for (std::vector<std::pair<string,int>>::iterator it = todo.begin() ; it != todo.end(); ++it){

  	std::cout << it->first << "  " << it->second << std::endl;
	TFile f_in(it->first.c_str(), "READ");
  	TTree* tree_in = (TTree*)f_in.Get("mini");
	
	std::vector<long>* runNumber=0;
	std::vector<long>* eventNumber=0;
	std::vector<float>* mttReco=0;
	
	
  	tree_in->SetBranchAddress("runNumber", &runNumber);
  	tree_in->SetBranchAddress("eventNumber", &eventNumber);
  	tree_in->SetBranchAddress("mttReco", &mttReco);
  	region->clear();
	region->push_back(it->second);
	
	
	for (long long i=0; i<tree_in->GetEntries();i++){
	  tree_in->GetEvent(i);
	  	  
	  if(mttReco->size()!=1) std::cerr << "Error: wrong length!! size= " << mttReco->size() << std::endl;
	  
	  //run_number=std::atoi(f_out_name);
	  run_number = runNumber->at(0);

	  event_number = eventNumber->at(0);
	  m_tt = mttReco->at(0);
	  
	  m_tree->Fill();
	}
  	f_in.Close();
	
  }
  f_out.cd();
  m_tree->Write();
  
  f_out.Close();

}
