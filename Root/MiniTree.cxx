/**
 * @brief Class that reads information from the input file and puts it in a object-oriented format in Event.
 * @author Danilo Enoque Ferreira de Lima <dferreir@cern.ch>
 */
#include "TopNtupleAnalysis/MiniTree.h"
#include "TopNtupleAnalysis/Event.h"
#include "TLorentzVector.h"
#include "TFile.h"
#include <vector>
#include <string>
#include <iostream>
#include "TChain.h"

MiniTree::MiniTree(bool toWrite, const std::string &file, const std::string &name)
  : m_toWrite(toWrite), m_fileToWrite(0), m_chain(0), m_name(name) {
  if (toWrite) {
    m_fileToWrite = new TFile(file.c_str(), "RECREATE");
    m_chain = new TTree(name.c_str(), "");
  } else {
    m_fileToWrite = new TFile(file.c_str());
    m_chain = new TChain(name.c_str());
    ((TChain *) m_chain)->Add(file.c_str());
  }
  m_sumWeights = 0;

  prepareBranches();
}

MiniTree::~MiniTree() {
  if (m_toWrite) {
    m_fileToWrite->cd();
    m_chain->Write();
  }
  if (m_chain) delete m_chain;
  if (m_fileToWrite) delete m_fileToWrite;
}

void MiniTree::read(int event, Event &e) {
  e.clear();
  m_chain->GetEntry(event);
  e.channelNumber() = mcChannelNumber;

  e.npv() = npv; 
  e.vtxz() = vtxz;
  e.mu() = mu;
  e.mu_original() = mu_original;
  e.weight_mc() = weight_mc;
  e.weight_pileup() = weight_pileup;
  e.weight_bTagSF() = weight_bTagSF;
  e.weight_leptonSF() = weight_leptonSF;
  
  // adding the truth information into the event  
     
  e.MC_w1h().SetPtEtaPhiM(MC_w1h_pt, MC_w1h_eta, MC_w1h_phi, MC_w1h_m);
  e.MC_w1h_pdgId() = MC_w1h_pdgId;
  e.MC_w2h().SetPtEtaPhiM(MC_w2h_pt, MC_w2h_eta, MC_w2h_phi, MC_w2h_m);
  e.MC_w2h_pdgId() = MC_w2h_pdgId;
  e.MC_bh().SetPtEtaPhiM( MC_bh_pt, MC_bh_eta, MC_bh_phi, MC_bh_m);
  
  e.MC_w1l().SetPtEtaPhiM(MC_w1l_pt, MC_w1l_eta, MC_w1l_phi, MC_w1l_m);
  e.MC_w1l_pdgId() = MC_w1l_pdgId;
  e.MC_w2l().SetPtEtaPhiM(MC_w2l_pt, MC_w2l_eta, MC_w2l_phi, MC_w2l_m);
  e.MC_w2l_pdgId() = MC_w2l_pdgId;
  e.MC_bl().SetPtEtaPhiM( MC_bl_pt, MC_bl_eta, MC_bl_phi, MC_bl_m);
  
  e.MC_ttbar_beforeFSR().SetPtEtaPhiM(MC_ttbar_beforeFSR_pt, MC_ttbar_beforeFSR_eta, MC_ttbar_beforeFSR_phi, MC_ttbar_beforeFSR_m);
  
  for (int k = 0; k < el_pt->size(); ++k) {
    e.electron().push_back(Electron());
    e.electron()[k].mom().SetPtEtaPhiE(el_pt->at(k), el_eta->at(k), el_phi->at(k), el_e->at(k));
    //e.electron()[k].setMI(el_miniiso->at(k));
    e.electron()[k].setTightPP(true);
    e.electron()[k].caloMom() = e.electron()[k].mom();
    e.electron()[k].trkMom() = e.electron()[k].mom();
    e.electron()[k].z0() = 0;
    e.electron()[k].author() = 1;
  }
  for (int k = 0; k < mu_pt->size(); ++k) {
    e.muon().push_back(Muon());
    e.muon()[k].mom().SetPtEtaPhiE(mu_pt->at(k), mu_eta->at(k), mu_phi->at(k), mu_e->at(k));
    e.muon()[k].setMI(0);
    e.muon()[k].setTight(true);
    e.muon()[k].z0() = 0;
    e.muon()[k].d0() = 0;
    e.muon()[k].sd0() = 0;
    e.muon()[k].author() = 0;
    e.muon()[k].passTrkCuts() = true;
  }

  for (int k = 0; k < jet_pt->size(); ++k) {
    e.jet().push_back(Jet());
    e.jet()[k].mom().SetPtEtaPhiE(jet_pt->at(k), jet_eta->at(k), jet_phi->at(k), jet_e->at(k));
    e.jet()[k].trueFlavour() = 0; // TODO jet_trueflav==0?-99:jet_trueflav->at(k);
    e.jet()[k].mv1() = jet_mv1==0?-99:jet_mv1->at(k);
    e.jet()[k].ip3dsv1() = jet_ip3dsv1==0?-99:jet_ip3dsv1->at(k);
    e.jet()[k].mv2c20() = jet_mv2c20==0?-99:jet_mv2c20->at(k);
    e.jet()[k].jvt() = jet_jvt==0?-99:jet_jvt->at(k);
    e.jet()[k].closeToLepton() = jet_closeToLepton==0?-99:jet_closeToLepton->at(k);
  }
   
  for (int k = 0; k < ljet_pt->size(); ++k) {
    e.largeJet().push_back(LargeJet());
    e.largeJet()[k].mom().SetPtEtaPhiE(ljet_pt->at(k), ljet_eta->at(k), ljet_phi->at(k), ljet_e->at(k));
    e.largeJet()[k].split12() = ljet_sd12->at(k);
    e.largeJet()[k].good() = ljet_good->at(k);
    e.largeJet()[k].trueFlavour() = 0; //TODO ljet_trueflav==0?-99:ljet_trueflav->at(k);
  }
  
  e.met(met_met*std::cos(met_phi), met_met*std::sin(met_phi));

  e.passes().clear();

  if (bejets) e.passes().push_back("bejets");
  if (bmujets) e.passes().push_back("bmujets");
  if (rejets) e.passes().push_back("rejets");
  if (rmujets) e.passes().push_back("rmujets");
  if (ejets) e.passes().push_back("ejets");
  if (mujets) e.passes().push_back("mujets");
  if (ee) e.passes().push_back("ee");
  if (emu) e.passes().push_back("emu");
  if (mumu) e.passes().push_back("mumu");
}

double &MiniTree::sumWeights() {
  return m_sumWeights;
}

void MiniTree::write(const Event &e) {
  mcChannelNumber = e.channelNumber();
  npv = e.npv();
  vtxz= e.vtxz();
  mu  = e.mu();
  mu_original = e.mu_original();

  weight_mc 	  = e.weight_mc();
  weight_pileup   = e.weight_pileup();
  weight_bTagSF   = e.weight_bTagSF();
  weight_leptonSF = e.weight_leptonSF();

  el_pt->clear();
  el_eta->clear();
  el_phi->clear();
  el_e->clear();
  for (int k = 0; k < e.electron().size(); ++k) {
    el_pt->push_back(e.electron()[k].mom().Perp());
    el_eta->push_back(e.electron()[k].mom().Eta());
    el_phi->push_back(e.electron()[k].mom().Phi());
    el_e->push_back(e.electron()[k].mom().E());
  }

  mu_pt->clear();
  mu_eta->clear();
  mu_phi->clear();
  mu_e->clear();
  for (int k = 0; k < e.muon().size(); ++k) {
    mu_pt->push_back(e.muon()[k].mom().Perp());
    mu_eta->push_back(e.muon()[k].mom().Eta());
    mu_phi->push_back(e.muon()[k].mom().Phi());
    mu_e->push_back(e.muon()[k].mom().E());
  }

  jet_pt->clear();
  jet_eta->clear();
  jet_phi->clear();
  jet_e->clear();
  jet_mv1->clear();
  jet_mv2c20->clear();
  jet_ip3dsv1->clear();
  jet_closeToLepton->clear();
  for (int k = 0; k < e.jet().size(); ++k) {
    jet_pt->push_back(e.jet()[k].mom().Perp());
    jet_eta->push_back(e.jet()[k].mom().Eta());
    jet_phi->push_back(e.jet()[k].mom().Phi());
    jet_e->push_back(e.jet()[k].mom().E());
    jet_mv1->push_back(e.jet()[k].mv1());
    jet_mv2c20->push_back(e.jet()[k].mv2c20());
    jet_ip3dsv1->push_back(e.jet()[k].ip3dsv1());
    jet_closeToLepton->push_back(e.jet()[k].closeToLepton());
  }

  ljet_pt->clear();
  ljet_eta->clear();
  ljet_phi->clear();
  ljet_e->clear();
  ljet_sd12->clear();
  ljet_good->clear();
  for (int k = 0; k < e.largeJet().size(); ++k) {
    ljet_pt->push_back(e.largeJet()[k].mom().Perp());
    ljet_eta->push_back(e.largeJet()[k].mom().Eta());
    ljet_phi->push_back(e.largeJet()[k].mom().Phi());
    ljet_e->push_back(e.largeJet()[k].mom().E());
    ljet_good->push_back(e.largeJet()[k].good());
  }
  met_met = e.met().Perp();
  met_phi = e.met().Phi();

  bejets = 0;
  bmujets = 0;
  rejets = 0;
  rmujets = 0;
  ejets = 0;
  mujets = 0;
  ee = 0;
  mumu = 0;
  emu = 0;
  if (e.passes("bejets"))   bejets = 1;
  if (e.passes("bmujets"))  bmujets = 1;
  if (e.passes("rejets"))   rejets = 1;
  if (e.passes("rmujets"))  rmujets = 1;
  if (e.passes("ejets"))    ejets = 1;
  if (e.passes("mujets"))   mujets = 1;

  if (e.passes("ee"))       ee = 1;
  if (e.passes("emu"))      emu = 1;
  if (e.passes("mumu"))     mumu = 1;

  m_chain->Fill();
}

void MiniTree::addFileToRead(const std::string &fname) {
  ((TChain *) m_chain)->Add(fname.c_str());
}

double MiniTree::getSumWeights() {
  return m_sumWeights;
}

int MiniTree::GetEntries() {
  return m_chain->GetEntries();
}

void MiniTree::prepareBranches() {

  el_pt = 0;
  el_eta = 0;
  el_phi = 0;
  el_miniiso = 0;
  el_e = 0;

  mu_pt = 0;
  mu_eta = 0;
  mu_phi = 0;
  mu_miniiso = 0;
  mu_e = 0;

  jet_pt = 0;
  jet_eta = 0;
  jet_phi = 0;
  jet_e = 0;
  jet_mv1 = 0;
  jet_mv2c20 = 0;
  jet_ip3dsv1 = 0;
  jet_jvt = 0;
  jet_closeToLepton = 0;

  ljet_pt = 0;
  ljet_eta = 0;
  ljet_phi = 0;
  ljet_e = 0;
  ljet_sd12 = 0;
  ljet_good = 0;

  MC_w1h_pt 	= -5000;
  MC_w1h_eta 	= -5000;
  MC_w1h_phi 	= -5000;
  MC_w1h_m 	= -5000;  
  MC_w1h_pdgId 	= 0;
  
  MC_w2h_pt 	= -5000;
  MC_w2h_eta 	= -5000;
  MC_w2h_phi 	= -5000;
  MC_w2h_m 	= -5000;
  MC_w2h_pdgId 	= 0;
  
  MC_bh_pt 	= -5000;
  MC_bh_eta 	= -5000;
  MC_bh_phi 	= -5000;
  MC_bh_m 	= -5000;
  
  MC_w1l_pt 	= -5000;
  MC_w1l_eta 	= -5000;
  MC_w1l_phi 	= -5000;
  MC_w1l_m 	= -5000;
  MC_w1l_pdgId 	= 0;
  
  MC_w2l_pt 	= -5000;
  MC_w2l_eta 	= -5000;
  MC_w2l_phi 	= -5000;
  MC_w2l_m 	= -5000;
  MC_w2l_pdgId 	= 0;
  
  MC_bl_pt 	= -5000;
  MC_bl_eta 	= -5000;
  MC_bl_phi 	= -5000;
  MC_bl_m 	= -5000;
  
  MC_ttbar_beforeFSR_pt = 0;
  MC_ttbar_beforeFSR_eta = 0;
  MC_ttbar_beforeFSR_phi = 0;
  MC_ttbar_beforeFSR_m = 0;

  if (m_toWrite) {
    m_chain->Branch("mcChannelNumber", &mcChannelNumber);
    m_chain->Branch("weight_mc", &weight_mc);
    m_chain->Branch("weight_pileup", &weight_pileup);
    m_chain->Branch("weight_bTagSF", &weight_bTagSF);
    m_chain->Branch("weight_leptonSF", &weight_leptonSF);    

    m_chain->Branch("MC_w1h_pt",  	&MC_w1h_pt);
    m_chain->Branch("MC_w1h_eta", 	&MC_w1h_eta);
    m_chain->Branch("MC_w1h_phi", 	&MC_w1h_phi);
    m_chain->Branch("MC_w1h_m",		&MC_w1h_m);
    m_chain->Branch("MC_w1h_pdgId",	&MC_w1h_pdgId);
    
    m_chain->Branch("MC_w2h_pt",  	&MC_w2h_pt);
    m_chain->Branch("MC_w2h_eta", 	&MC_w2h_eta);
    m_chain->Branch("MC_w2h_phi", 	&MC_w2h_phi);
    m_chain->Branch("MC_w2h_m",		&MC_w2h_m);
    m_chain->Branch("MC_w2h_pdgId",	&MC_w2h_pdgId);
    
    m_chain->Branch("MC_bh_pt",  	&MC_bh_pt);
    m_chain->Branch("MC_bh_eta", 	&MC_bh_eta);
    m_chain->Branch("MC_bh_phi", 	&MC_bh_phi);
    m_chain->Branch("MC_bh_m",		&MC_bh_m);
    
    m_chain->Branch("MC_w1l_pt",  	&MC_w1l_pt);
    m_chain->Branch("MC_w1l_eta", 	&MC_w1l_eta);
    m_chain->Branch("MC_w1l_phi", 	&MC_w1l_phi);
    m_chain->Branch("MC_w1l_m",		&MC_w1l_m);
    m_chain->Branch("MC_w1l_pdgId",	&MC_w1l_pdgId);
    
    m_chain->Branch("MC_w2l_pt",  	&MC_w2l_pt);
    m_chain->Branch("MC_w2l_eta", 	&MC_w2l_eta);
    m_chain->Branch("MC_w2l_phi", 	&MC_w2l_phi);
    m_chain->Branch("MC_w2l_m",		&MC_w2l_m);
    m_chain->Branch("MC_w2l_pdgId",	&MC_w2l_pdgId);
    
    m_chain->Branch("MC_bl_pt",  	&MC_bl_pt);
    m_chain->Branch("MC_bl_eta", 	&MC_bl_eta);
    m_chain->Branch("MC_bl_phi", 	&MC_bl_phi);
    m_chain->Branch("MC_bl_m",		&MC_bl_m);    
    
    m_chain->Branch("MC_ttbar_beforeFSR_pt", &MC_ttbar_beforeFSR_pt);
    m_chain->Branch("MC_ttbar_beforeFSR_eta", &MC_ttbar_beforeFSR_eta);
    m_chain->Branch("MC_ttbar_beforeFSR_phi", &MC_ttbar_beforeFSR_phi);
    m_chain->Branch("MC_ttbar_beforeFSR_m", &MC_ttbar_beforeFSR_m);

    m_chain->Branch("el_pt", &el_pt);
    m_chain->Branch("el_eta", &el_eta);
    m_chain->Branch("el_phi", &el_phi);
    m_chain->Branch("el_e", &el_e);
    //m_chain->Branch("el_miniiso", &el_miniiso);

    m_chain->Branch("mu_pt", &mu_pt);
    m_chain->Branch("mu_eta", &mu_eta);
    m_chain->Branch("mu_phi", &mu_phi);
    m_chain->Branch("mu_e", &mu_e);
    //m_chain->Branch("mu_miniiso", &mu_miniiso);

    m_chain->Branch("jet_pt", &jet_pt);
    m_chain->Branch("jet_eta", &jet_eta);
    m_chain->Branch("jet_phi", &jet_phi);
    m_chain->Branch("jet_e", &jet_e);
    m_chain->Branch("jet_mv1", &jet_mv1);
    m_chain->Branch("jet_mv2c20", &jet_mv2c20);
    m_chain->Branch("jet_ip3dsv1", &jet_ip3dsv1);
    m_chain->Branch("jet_jvt", &jet_jvt);
    m_chain->Branch("jet_closeToLepton", &jet_closeToLepton);

    m_chain->Branch("ljet_pt", &ljet_pt);
    m_chain->Branch("ljet_eta", &ljet_eta);
    m_chain->Branch("ljet_phi", &ljet_phi);
    m_chain->Branch("ljet_e", &ljet_e);
    m_chain->Branch("ljet_sd12", &ljet_sd12);
    m_chain->Branch("ljet_good", &ljet_good);

    m_chain->Branch("met_met", &met_met);
    m_chain->Branch("met_phi", &met_phi);
    
    m_chain->Branch("npv", &npv);
    m_chain->Branch("vtxz", &vtxz);
    m_chain->Branch("mu", &mu);
    m_chain->Branch("mu_original", &mu_original);

    m_chain->Branch("bejets", &bejets);
    m_chain->Branch("bmujets", &bmujets);
    m_chain->Branch("rejets", &rejets);
    m_chain->Branch("rmujets", &rmujets);
    m_chain->Branch("ejets", &ejets);
    m_chain->Branch("mujets", &mujets);

    m_chain->Branch("ee", &ee);
    m_chain->Branch("mumu", &mumu);
    m_chain->Branch("emu", &emu);
    
    m_chain->Branch("binning01", &binning01);
    m_chain->Branch("binning02", &binning02);
    m_chain->Branch("binning03", &binning03);
    m_chain->Branch("binning04", &binning04);
    m_chain->Branch("binning05", &binning05);
    
  } else {
    m_chain->SetBranchAddress("mcChannelNumber",  &mcChannelNumber);
    m_chain->SetBranchAddress("weight_mc", 	  &weight_mc);
    m_chain->SetBranchAddress("weight_pileup", 	  &weight_pileup);
    m_chain->SetBranchAddress("weight_bTagSF_70", 	  &weight_bTagSF);
    m_chain->SetBranchAddress("weight_leptonSF",  &weight_leptonSF);
    
    m_chain->SetBranchAddress("MC_w1h_pt",  	&MC_w1h_pt);
    m_chain->SetBranchAddress("MC_w1h_eta", 	&MC_w1h_eta);
    m_chain->SetBranchAddress("MC_w1h_phi", 	&MC_w1h_phi);
    m_chain->SetBranchAddress("MC_w1h_m",	&MC_w1h_m);
    m_chain->SetBranchAddress("MC_w1h_pdgId",	&MC_w1h_pdgId);
        
    m_chain->SetBranchAddress("MC_w2h_pt",  	&MC_w2h_pt);
    m_chain->SetBranchAddress("MC_w2h_eta", 	&MC_w2h_eta);
    m_chain->SetBranchAddress("MC_w2h_phi", 	&MC_w2h_phi);
    m_chain->SetBranchAddress("MC_w2h_m",	&MC_w2h_m);
    m_chain->SetBranchAddress("MC_w2h_pdgId",	&MC_w2h_pdgId);
    
    m_chain->SetBranchAddress("MC_bh_pt",  	&MC_bh_pt);
    m_chain->SetBranchAddress("MC_bh_eta", 	&MC_bh_eta);
    m_chain->SetBranchAddress("MC_bh_phi", 	&MC_bh_phi);
    m_chain->SetBranchAddress("MC_bh_m",	&MC_bh_m);
    
    m_chain->SetBranchAddress("MC_w1l_pt",  	&MC_w1l_pt);
    m_chain->SetBranchAddress("MC_w1l_eta", 	&MC_w1l_eta);
    m_chain->SetBranchAddress("MC_w1l_phi", 	&MC_w1l_phi);
    m_chain->SetBranchAddress("MC_w1l_m",	&MC_w1l_m);
    m_chain->SetBranchAddress("MC_w1l_pdgId",	&MC_w1l_pdgId);
    
    m_chain->SetBranchAddress("MC_w2l_pt",  	&MC_w2l_pt);
    m_chain->SetBranchAddress("MC_w2l_eta", 	&MC_w2l_eta);
    m_chain->SetBranchAddress("MC_w2l_phi", 	&MC_w2l_phi);
    m_chain->SetBranchAddress("MC_w2l_m",	&MC_w2l_m);
    m_chain->SetBranchAddress("MC_w2l_pdgId",	&MC_w2l_pdgId);
    
    m_chain->SetBranchAddress("MC_bl_pt",  	&MC_bl_pt);
    m_chain->SetBranchAddress("MC_bl_eta", 	&MC_bl_eta);
    m_chain->SetBranchAddress("MC_bl_phi", 	&MC_bl_phi);
    m_chain->SetBranchAddress("MC_bl_m",	&MC_bl_m);  
    
    m_chain->SetBranchAddress("MC_ttbar_beforeFSR_pt", &MC_ttbar_beforeFSR_pt);
    m_chain->SetBranchAddress("MC_ttbar_beforeFSR_eta", &MC_ttbar_beforeFSR_eta);
    m_chain->SetBranchAddress("MC_ttbar_beforeFSR_phi", &MC_ttbar_beforeFSR_phi);
    m_chain->SetBranchAddress("MC_ttbar_beforeFSR_m", &MC_ttbar_beforeFSR_m);

    m_chain->SetBranchAddress("el_pt", &el_pt);
    m_chain->SetBranchAddress("el_eta", &el_eta);
    m_chain->SetBranchAddress("el_phi", &el_phi);
    m_chain->SetBranchAddress("el_e", &el_e);
    //m_chain->SetBranchAddress("el_miniiso", &el_miniiso);

    m_chain->SetBranchAddress("mu_pt", &mu_pt);
    m_chain->SetBranchAddress("mu_eta", &mu_eta);
    m_chain->SetBranchAddress("mu_phi", &mu_phi);
    m_chain->SetBranchAddress("mu_e", &mu_e);
    //m_chain->SetBranchAddress("mu_miniiso", &mu_miniiso);

    m_chain->SetBranchAddress("jet_pt", &jet_pt);
    m_chain->SetBranchAddress("jet_eta", &jet_eta);
    m_chain->SetBranchAddress("jet_phi", &jet_phi);
    m_chain->SetBranchAddress("jet_e", &jet_e);
    m_chain->SetBranchAddress("jet_mv1", &jet_mv1);
    m_chain->SetBranchAddress("jet_mv2c20", &jet_mv2c20);
    m_chain->SetBranchAddress("jet_ip3dsv1", &jet_ip3dsv1);
    m_chain->SetBranchAddress("jet_jvt", &jet_jvt);
    m_chain->SetBranchAddress("jet_closeToLepton", &jet_closeToLepton);

    m_chain->SetBranchAddress("ljet_pt", &ljet_pt);
    m_chain->SetBranchAddress("ljet_eta", &ljet_eta);
    m_chain->SetBranchAddress("ljet_phi", &ljet_phi);
    m_chain->SetBranchAddress("ljet_e", &ljet_e);
    m_chain->SetBranchAddress("ljet_sd12", &ljet_sd12);
    m_chain->SetBranchAddress("ljet_good", &ljet_good);

    m_chain->SetBranchAddress("met_met", &met_met);
    m_chain->SetBranchAddress("met_phi", &met_phi);
  
    m_chain->SetBranchAddress("npv", &npv);
    m_chain->SetBranchAddress("vtxz", &vtxz);
    m_chain->SetBranchAddress("mu", &mu);
    m_chain->SetBranchAddress("mu_original_xAOD", &mu_original);

    m_chain->SetBranchAddress("bejets", &bejets);
    m_chain->SetBranchAddress("bmujets", &bmujets);
    m_chain->SetBranchAddress("rejets", &rejets);
    m_chain->SetBranchAddress("rmujets", &rmujets);
    m_chain->SetBranchAddress("ejets", &ejets);
    m_chain->SetBranchAddress("mujets", &mujets);

    m_chain->SetBranchAddress("ee", &ee);
    m_chain->SetBranchAddress("mumu", &mumu);
    m_chain->SetBranchAddress("emu", &emu);
    
    //m_chain->SetBranchAddress("binning01", &binning01);
    //m_chain->SetBranchAddress("binning02", &binning02);
    //m_chain->SetBranchAddress("binning03", &binning03);
    //m_chain->SetBranchAddress("binning04", &binning04);
    //m_chain->SetBranchAddress("binning05", &binning05);
  }
}

