/**
 * @brief Analysis class for tt resonances.
 * @author of original analysis AnaTtresSL: Danilo Enoque Ferreira de Lima <dferreir@cern.ch>
 * @modified my Sabrina Groh <sgroh@cern.ch> to produce the input histograms for the W+jets estimation via heavy flavor scale factors
 * necessary histograms  HF_(pre)tag_el(/mu)_2015(/2016) and HF_(pre)tag_C(/cc/B/lf)_el(/mu)_2015(/2016)
 */

#include "TopNtupleAnalysis/Analysis.h"
#include "TopNtupleAnalysis/AnaMultijetAllIn1.h"
#include "TopNtupleAnalysis/Event.h"
#include "TLorentzVector.h"
#include <vector>
#include <string>
#include "TopNtupleAnalysis/HistogramService.h"

AnaMultijetAllIn1::AnaMultijetAllIn1(const std::string &filename, bool electron, bool boosted, std::vector<std::string> &systList)
  : Analysis(filename, systList), m_electron(electron), m_boosted(boosted),
    m_neutrinoBuilder("MeV"), m_chi2("MeV") {
  m_chi2.Init(TtresChi2::DATA2015_MC15C);

  m_hSvc.m_tree->Branch("truemtt",    &_tree_truemtt);
  m_hSvc.m_tree->Branch("mtt",    &_tree_mtt);
  m_hSvc.m_tree->Branch("weight", &_tree_weight);
  m_hSvc.m_tree->Branch("cat",    &_tree_cat);
  m_hSvc.m_tree->Branch("syst",   &_tree_syst);

  TH1::SetDefaultSumw2;

  double varBin1[] = {0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 220, 240, 260, 280, 300, 340, 380, 450, 500};
  int varBinN1 = sizeof(varBin1)/sizeof(double) - 1;
  double varBin2[] = {300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 540, 580, 620, 660, 700, 800};
  int varBinN2 = sizeof(varBin2)/sizeof(double) - 1;
  double varBin3[] = {0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 340, 380, 420, 460, 500};
  int varBinN3 = sizeof(varBin3)/sizeof(double) - 1;
  double varBin4[] = {80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 340, 380, 420, 460, 500};
  int varBinN4 = sizeof(varBin4)/sizeof(double) - 1;

  double varBin5[] = {0, 80, 160, 240, 320, 400, 480, 560,640,720,800,920,1040,1160,1280,1400,1550,1700,2000,2300,2600,2900,3200,3600,4100,4600,5100,6000};
  int varBinN5 = sizeof(varBin5)/sizeof(double) - 1;

  //m_hSvc.create1D("yields", "; One ; Events", 1, 0.5, 1.5);

  // Control plots to confirm that all events have been completely run through
  m_hSvc.create1D("Controlplot_initial_rejets_2015",  "; events pass rejets_2015; Events",  5, -1.5, 3.5);
  m_hSvc.create1D("Controlplot_initial_rejets_2016",  "; events pass rejets_2016; Events",  5, -1.5, 3.5);
  m_hSvc.create1D("Controlplot_initial_rmujets_2015", "; events pass rmujets_2015; Events", 5, -1.5, 3.5);
  m_hSvc.create1D("Controlplot_initial_rmujets_2016", "; events pass rmujets_2016; Events", 5, -1.5, 3.5);

  m_hSvc.create1D("Controlplot_initial_bejets_2015",  "; events pass bejets_2015; Events",  5, -1.5, 3.5);
  m_hSvc.create1D("Controlplot_initial_bejets_2016",  "; events pass bejets_2016; Events",  5, -1.5, 3.5);
  m_hSvc.create1D("Controlplot_initial_bmujets_2015", "; events pass bmujets_2015; Events", 5, -1.5, 3.5);
  m_hSvc.create1D("Controlplot_initial_bmujets_2016", "; events pass bmujets_2016; Events", 5, -1.5, 3.5);
  // |---- weighted
  m_hSvc.create1D("Controlplot_initial_rejets_2015_weight",  "; events pass rejets_2015; Events",  5, -1.5, 3.5);
  m_hSvc.create1D("Controlplot_initial_rejets_2016_weight",  "; events pass rejets_2016; Events",  5, -1.5, 3.5);
  m_hSvc.create1D("Controlplot_initial_rmujets_2015_weight", "; events pass rmujets_2015; Events", 5, -1.5, 3.5);
  m_hSvc.create1D("Controlplot_initial_rmujets_2016_weight", "; events pass rmujets_2016; Events", 5, -1.5, 3.5);

  m_hSvc.create1D("Controlplot_initial_bejets_2015_weight",  "; events pass bejets_2015; Events",  5, -1.5, 3.5);
  m_hSvc.create1D("Controlplot_initial_bejets_2016_weight",  "; events pass bejets_2016; Events",  5, -1.5, 3.5);
  m_hSvc.create1D("Controlplot_initial_bmujets_2015_weight", "; events pass bmujets_2015; Events", 5, -1.5, 3.5);
  m_hSvc.create1D("Controlplot_initial_bmujets_2016_weight", "; events pass bmujets_2016; Events", 5, -1.5, 3.5);
  //////// ---|
  m_hSvc.create1D("Controlplot_initial_rejetsWCR_2015",  "; events pass rejetsWCR_2015; Events",  5, -1.5, 3.5);
  m_hSvc.create1D("Controlplot_initial_rejetsWCR_2016",  "; events pass rejetsWCR_2016; Events",  5, -1.5, 3.5);
  m_hSvc.create1D("Controlplot_initial_rmujetsWCR_2015", "; events pass rmujetsWCR_2015; Events", 5, -1.5, 3.5);
  m_hSvc.create1D("Controlplot_initial_rmujetsWCR_2016", "; events pass rmujetsWCR_2016; Events", 5, -1.5, 3.5);

  m_hSvc.create1D("Controlplot_initial_rejetsWCRtag_2015",  "; events pass rejetsWCRtag_2015; Events",  5, -1.5, 3.5);
  m_hSvc.create1D("Controlplot_initial_rejetsWCRtag_2016",  "; events pass rejetsWCRtag_2016; Events",  5, -1.5, 3.5);
  m_hSvc.create1D("Controlplot_initial_rmujetsWCRtag_2015", "; events pass rmujetsWCRtag_2015; Events", 5, -1.5, 3.5);
  m_hSvc.create1D("Controlplot_initial_rmujetsWCRtag_2016", "; events pass rmujetsWCRtag_2016; Events", 5, -1.5, 3.5);



  // ### previous yields:
  // # boosted
  m_hSvc.create1D("yields_boost_el_2015",   "; one; Events (weighted)",5,-1.5,3.5);
  m_hSvc.create1D("yields_boost_el_nw_2015","; one; Events (weight=1)",5,-1.5,3.5);
  m_hSvc.create1D("yields_boost_mu_2015",   "; one; Events (weighted)",5,-1.5,3.5);
  m_hSvc.create1D("yields_boost_el_2016",   "; one; Events (weighted)",5,-1.5,3.5);
  m_hSvc.create1D("yields_boost_el_nw_2016","; one; Events (weight=1)",5,-1.5,3.5);
  m_hSvc.create1D("yields_boost_mu_2016",   "; one; Events (weighted)",5,-1.5,3.5);
  // for Wjets only: signal region (resolved or boosted)
  // # 2015 
  m_hSvc.create1D("yields_el_Wc_2015", "; one; Events (weighted)",5,-1.5,3.5);
  m_hSvc.create1D("yields_mu_Wc_2015", "; one; Events (weighted)",5,-1.5,3.5);
  m_hSvc.create1D("yields_el_Wcc_2015","; one; Events (weighted)",5,-1.5,3.5);
  m_hSvc.create1D("yields_mu_Wcc_2015","; one; Events (weighted)",5,-1.5,3.5);
  m_hSvc.create1D("yields_el_Wbb_2015","; one; Events (weighted)",5,-1.5,3.5);
  m_hSvc.create1D("yields_mu_Wbb_2015","; one; Events (weighted)",5,-1.5,3.5);
  m_hSvc.create1D("yields_el_Wlf_2015","; one; Events (weighted)",5,-1.5,3.5);
  m_hSvc.create1D("yields_mu_Wlf_2015","; one; Events (weighted)",5,-1.5,3.5);
 // # 2016
  m_hSvc.create1D("yields_el_Wc_2016", "; one; Events (weighted)",5,-1.5,3.5);
  m_hSvc.create1D("yields_mu_Wc_2016", "; one; Events (weighted)",5,-1.5,3.5);
  m_hSvc.create1D("yields_el_Wcc_2016","; one; Events (weighted)",5,-1.5,3.5);
  m_hSvc.create1D("yields_mu_Wcc_2016","; one; Events (weighted)",5,-1.5,3.5);
  m_hSvc.create1D("yields_el_Wbb_2016","; one; Events (weighted)",5,-1.5,3.5);
  m_hSvc.create1D("yields_mu_Wbb_2016","; one; Events (weighted)",5,-1.5,3.5);
  m_hSvc.create1D("yields_el_Wlf_2016","; one; Events (weighted)",5,-1.5,3.5);
  m_hSvc.create1D("yields_mu_Wlf_2016","; one; Events (weighted)",5,-1.5,3.5);

  // # resolved
  m_hSvc.create1D("yields_res_el_2015",     "; one; Events (weighted)",5,-1.5,3.5);
  m_hSvc.create1D("yields_res_el_nw_2015",  "; one; Events (weight=1)",5,-1.5,3.5);
  m_hSvc.create1D("yields_res_mu_2015",     "; one; Events (weighted)",5,-1.5,3.5);

  m_hSvc.create1D("yields_res_el_2016",     "; one; Events (weighted)",5,-1.5,3.5);
  m_hSvc.create1D("yields_res_el_nw_2016",  "; one; Events (weight=1)",5,-1.5,3.5);
  m_hSvc.create1D("yields_res_mu_2016",     "; one; Events (weighted)",5,-1.5,3.5);
 
  if (!m_boosted) {
    // ### PREtag ### 
    // 2in bin:
    // # 2015
    m_hSvc.create1D("lepPt_2in_pre_2015",     "; Pt of lept [GeV]; Events"  , 100, 25, 525);  // X
    m_hSvc.create1D("lepEta_2in_pre_2015",    "; lepton #eta ; Events"      , 20, -2.5, 2.5);  // X
    m_hSvc.create1D("lepPhi_2in_pre_2015",    "; lepton #phi [rd] ; Events" , 32, -3.2, 3.2);  // X
    m_hSvc.create1D("lepCharge_2in_pre_2015", "; lepton charge [e] ; Events", 5, -2.5, 2.5);  // X

    m_hSvc.create1DVar("leadJetPt_2in_pre_2015",     "; leading Jet p_{T} [GeV]; Events"       , varBinN1, varBin1);  // X
    m_hSvc.create1D("nJets_2in_pre_2015",            "; number of jets ; Events"               , 10, -0.5, 9.5);  // controll plot only
    m_hSvc.create1DVar("leadTrkbJetPt_2in_pre_2015", "; leading b-jet p_{T} [GeV]; Events"     , varBinN1, varBin1);// X
    m_hSvc.create1D("nTrkBtagJets_2in_pre_2015",     "; number of b-tagged track jets ; Events", 10, 0, 10);// X

    m_hSvc.create1DVar("MET_2in_pre_2015", " ; missing E_{T} [GeV]; Events"    , varBinN1, varBin1); // X
    m_hSvc.create1D("MWT_2in_pre_2015",    "; W transverse mass [GeV]; Events" , 20, 0, 200); //X
    m_hSvc.create1D("METpMWT_2in_pre_2015",";MET+MWT;events"                   ,100,0,1000); // X
    m_hSvc.create1D("npv_2in_pre_2015",    "; npv; Events"                     , 50, 0, 50); //X
    // #############
    // # 2016
    m_hSvc.create1D("lepPt_2in_pre_2016",     "; Pt of lept [GeV]; Events"  , 100, 25, 525);  // X
    m_hSvc.create1D("lepEta_2in_pre_2016",    "; lepton #eta ; Events"      , 20, -2.5, 2.5);  // X
    m_hSvc.create1D("lepPhi_2in_pre_2016",    "; lepton #phi [rd] ; Events" , 32, -3.2, 3.2);  // X
    m_hSvc.create1D("lepCharge_2in_pre_2016", "; lepton charge [e] ; Events", 5, -2.5, 2.5);  // X

    m_hSvc.create1DVar("leadJetPt_2in_pre_2016",     "; leading Jet p_{T} [GeV]; Events"       , varBinN1, varBin1);  // X
    m_hSvc.create1D("nJets_2in_pre_2016",            "; number of jets ; Events"               , 10, -0.5, 9.5);  // controll plot only
    m_hSvc.create1DVar("leadTrkbJetPt_2in_pre_2016", "; leading b-jet p_{T} [GeV]; Events"     , varBinN1, varBin1);// X
    m_hSvc.create1D("nTrkBtagJets_2in_pre_2016",     "; number of b-tagged track jets ; Events", 10, 0, 10);// X

    m_hSvc.create1DVar("MET_2in_pre_2016", " ; missing E_{T} [GeV]; Events"    , varBinN1, varBin1); // X
    m_hSvc.create1D("MWT_2in_pre_2016",    "; W transverse mass [GeV]; Events" , 20, 0, 200); //X
    m_hSvc.create1D("METpMWT_2in_pre_2016",";MET+MWT;events"                   ,100,0,1000); // X
    m_hSvc.create1D("npv_2in_pre_2016",    "; npv; Events"                     , 50, 0, 50); //X
    // ####################
    // ###################
    // ### TAG ###
    // 2in bin:
    // # 2015
    m_hSvc.create1D("lepPt_2in_tag_2015",     "; Pt of lept [GeV]; Events"  , 100, 25, 525);  // X
    m_hSvc.create1D("lepEta_2in_tag_2015",    "; lepton #eta ; Events"      , 20, -2.5, 2.5);  // X
    m_hSvc.create1D("lepPhi_2in_tag_2015",    "; lepton #phi [rd] ; Events" , 32, -3.2, 3.2);  // X
    m_hSvc.create1D("lepCharge_2in_tag_2015", "; lepton charge [e] ; Events", 5, -2.5, 2.5);  // X

    m_hSvc.create1DVar("leadJetPt_2in_tag_2015",     "; leading Jet p_{T} [GeV]; Events"       , varBinN1, varBin1);
    m_hSvc.create1D("nJets_2in_tag_2015",            "; number of jets ; Events"               , 10, -0.5, 9.5);
    m_hSvc.create1DVar("leadTrkbJetPt_2in_tag_2015", "; leading b-jet p_{T} [GeV]; Events"     , varBinN1, varBin1);
    m_hSvc.create1D("nTrkBtagJets_2in_tag_2015",     "; number of b-tagged track jets ; Events", 10, 0, 10);

    m_hSvc.create1DVar("MET_2in_tag_2015", "; missing E_{T} [GeV]; Events"     , varBinN1, varBin1);
    m_hSvc.create1D("MWT_2in_tag_2015",    "; W transverse mass [GeV]; Events" , 20, 0, 200);
    m_hSvc.create1D("METpMWT_2in_tag_2015",";MET+MWT;events"                   ,100,0,1000); // transform from keV to GeV !
    m_hSvc.create1D("npv_2in_tag_2015",    "; npv; Events"                     , 50, 0, 50);

    m_hSvc.create1DVar("mtlep_res_2in_tag_2015", "; leptonic top mass [GeV]; Events", varBinN4, varBin4);
    m_hSvc.create1DVar("mthad_res_2in_tag_2015", "; hadronic top mass [GeV]; Events", varBinN4, varBin4);

    // # 2016
    m_hSvc.create1D("lepPt_2in_tag_2016",     "; Pt of lept [GeV]; Events"  , 100, 25, 525);  // X
    m_hSvc.create1D("lepEta_2in_tag_2016",    "; lepton #eta ; Events"      , 20, -2.5, 2.5);  // X
    m_hSvc.create1D("lepPhi_2in_tag_2016",    "; lepton #phi [rd] ; Events" , 32, -3.2, 3.2);  // X
    m_hSvc.create1D("lepCharge_2in_tag_2016", "; lepton charge [e] ; Events", 5, -2.5, 2.5);  // X

    m_hSvc.create1DVar("leadJetPt_2in_tag_2016",     "; leading Jet p_{T} [GeV]; Events"       , varBinN1, varBin1);
    m_hSvc.create1D("nJets_2in_tag_2016",            "; number of jets ; Events"               , 10, -0.5, 9.5);
    m_hSvc.create1DVar("leadTrkbJetPt_2in_tag_2016", "; leading b-jet p_{T} [GeV]; Events"     , varBinN1, varBin1);
    m_hSvc.create1D("nTrkBtagJets_2in_tag_2016",     "; number of b-tagged track jets ; Events", 10, 0, 10);

    m_hSvc.create1DVar("MET_2in_tag_2016", "; missing E_{T} [GeV]; Events"     , varBinN1, varBin1);
    m_hSvc.create1D("MWT_2in_tag_2016",    "; W transverse mass [GeV]; Events" , 20, 0, 200);
    m_hSvc.create1D("METpMWT_2in_tag_2016",";MET+MWT;events"                   ,100,0,1000); // transform from keV to GeV !
    m_hSvc.create1D("npv_2in_tag_2016",    "; npv; Events"                     , 50, 0, 50);

    m_hSvc.create1DVar("mtlep_res_2in_tag_2016", "; leptonic top mass [GeV]; Events", varBinN4, varBin4);
    m_hSvc.create1DVar("mthad_res_2in_tag_2016", "; hadronic top mass [GeV]; Events", varBinN4, varBin4);

     // 2ex
    // # 2015
    m_hSvc.create1D("lepPt_2ex_tag_2015",     "; Pt of lept [GeV]; Events"  , 100, 25, 525);
    m_hSvc.create1D("lepEta_2ex_tag_2015",    "; lepton #eta ; Events"      , 20, -2.5, 2.5);
    m_hSvc.create1D("lepPhi_2ex_tag_2015",    "; lepton #phi [rd] ; Events" , 32, -3.2, 3.2);
    m_hSvc.create1D("lepCharge_2ex_tag_2015", "; lepton charge [e] ; Events", 5, -2.5, 2.5);

    m_hSvc.create1DVar("leadJetPt_2ex_tag_2015",     "; leading Jet p_{T} [GeV]; Events"       , varBinN1, varBin1);
    m_hSvc.create1D("nJets_2ex_tag_2015",            "; number of jets ; Events"               , 10, -0.5, 9.5);
    m_hSvc.create1DVar("leadTrkbJetPt_2ex_tag_2015", "; leading b-jet p_{T} [GeV]; Events"     , varBinN1, varBin1);
    m_hSvc.create1D("nTrkBtagJets_2ex_tag_2015",     "; number of b-tagged track jets ; Events", 10, 0, 10);

    m_hSvc.create1DVar("MET_2ex_tag_2015", "; missing E_{T} [GeV]; Events"     , varBinN1, varBin1);
    m_hSvc.create1D("MWT_2ex_tag_2015",    "; W transverse mass [GeV]; Events" , 20, 0, 200);
    m_hSvc.create1D("METpMWT_2ex_tag_2015",";MET+MWT;events"                   ,100,0,1000); // transform from keV to GeV !

    m_hSvc.create1D("npv_2ex_tag_2015",               "; npv; Events"                           , 50, 0, 50);
 
    // # 2016
    m_hSvc.create1D("lepPt_2ex_tag_2016",     "; Pt of lept [GeV]; Events"  , 100, 25, 525);
    m_hSvc.create1D("lepEta_2ex_tag_2016",    "; lepton #eta ; Events"      , 20, -2.5, 2.5);
    m_hSvc.create1D("lepPhi_2ex_tag_2016",    "; lepton #phi [rd] ; Events" , 32, -3.2, 3.2);
    m_hSvc.create1D("lepCharge_2ex_tag_2016", "; lepton charge [e] ; Events", 5, -2.5, 2.5);

    m_hSvc.create1DVar("leadJetPt_2ex_tag_2016",     "; leading Jet p_{T} [GeV]; Events"       , varBinN1, varBin1);
    m_hSvc.create1D("nJets_2ex_tag_2016",            "; number of jets ; Events"               , 10, -0.5, 9.5);
    m_hSvc.create1DVar("leadTrkbJetPt_2ex_tag_2016", "; leading b-jet p_{T} [GeV]; Events"     , varBinN1, varBin1);
    m_hSvc.create1D("nTrkBtagJets_2ex_tag_2016",     "; number of b-tagged track jets ; Events", 10, 0, 10);

    m_hSvc.create1DVar("MET_2ex_tag_2016", "; missing E_{T} [GeV]; Events"     , varBinN1, varBin1);
    m_hSvc.create1D("MWT_2ex_tag_2016",    "; W transverse mass [GeV]; Events" , 20, 0, 200);
    m_hSvc.create1D("METpMWT_2ex_tag_2016",";MET+MWT;events"                   ,100,0,1000); // transform from keV to GeV !

    m_hSvc.create1D("npv_2ex_tag_2016",               "; npv; Events"                           , 50, 0, 50);
 
    // 4in
    // # 2015
    m_hSvc.create1D("lepPt_4in_tag_2015",     "; Pt of lept [GeV]; Events"  , 100, 25, 525);
    m_hSvc.create1D("lepEta_4in_tag_2015",    "; lepton #eta ; Events"      , 20, -2.5, 2.5);
    m_hSvc.create1D("lepPhi_4in_tag_2015",    "; lepton #phi [rd] ; Events" , 32, -3.2, 3.2);
    m_hSvc.create1D("lepCharge_4in_tag_2015", "; lepton charge [e] ; Events", 5, -2.5, 2.5);

    m_hSvc.create1DVar("leadJetPt_4in_tag_2015",     "; leading Jet p_{T} [GeV]; Events"       , varBinN1, varBin1);
    m_hSvc.create1D("nJets_4in_tag_2015",            "; number of jets ; Events"               , 10, -0.5, 9.5);
    m_hSvc.create1DVar("leadTrkbJetPt_4in_tag_2015", "; leading b-jet p_{T} [GeV]; Events"     , varBinN1, varBin1);
    m_hSvc.create1D("nTrkBtagJets_4in_tag_2015g",     "; number of b-tagged track jets ; Events", 10, 0, 10);

    m_hSvc.create1DVar("MET_4in_tag_2015", "; missing E_{T} [GeV]; Events"     , varBinN1, varBin1);
    m_hSvc.create1D("MWT_4in_tag_2015",    "; W transverse mass [GeV]; Events" , 20, 0, 200);
    m_hSvc.create1D("METpMWT_4in_tag_2015",";MET+MWT;events"                   ,100,0,1000); // transform from keV to GeV !

    m_hSvc.create1D("npv_4in_tag_2015",               "; npv; Events"                           , 50, 0, 50);
    // # 2016
    m_hSvc.create1D("lepPt_4in_tag_2016",     "; Pt of lept [GeV]; Events"  , 100, 25, 525);
    m_hSvc.create1D("lepEta_4in_tag_2016",    "; lepton #eta ; Events"      , 20, -2.5, 2.5);
    m_hSvc.create1D("lepPhi_4in_tag_2016",    "; lepton #phi [rd] ; Events" , 32, -3.2, 3.2);
    m_hSvc.create1D("lepCharge_4in_tag_2016", "; lepton charge [e] ; Events", 5, -2.5, 2.5);

    m_hSvc.create1DVar("leadJetPt_4in_tag_2016",     "; leading Jet p_{T} [GeV]; Events"       , varBinN1, varBin1);
    m_hSvc.create1D("nJets_4in_tag_2016",            "; number of jets ; Events"               , 10, -0.5, 9.5);
    m_hSvc.create1DVar("leadTrkbJetPt_4in_tag_2016", "; leading b-jet p_{T} [GeV]; Events"     , varBinN1, varBin1);
    m_hSvc.create1D("nTrkBtagJets_4in_tag_2016g",     "; number of b-tagged track jets ; Events", 10, 0, 10);

    m_hSvc.create1DVar("MET_4in_tag_2016", "; missing E_{T} [GeV]; Events"     , varBinN1, varBin1);
    m_hSvc.create1D("MWT_4in_tag_2016",    "; W transverse mass [GeV]; Events" , 20, 0, 200);
    m_hSvc.create1D("METpMWT_4in_tag_2016",";MET+MWT;events"                   ,100,0,1000); // transform from keV to GeV !

    m_hSvc.create1D("npv_4in_tag_2016",               "; npv; Events"                           , 50, 0, 50);
    // ---------------------------
    // # W+/W- ratio
    m_hSvc.create1D("Wplus_jetmultiplicity_pretag_2015",  ";#jets;#events with l+",6,0.5,6.5); // 2ex,3ex,4ex,2in,3in,4in,5in
    m_hSvc.create1D("Wmin_jetmultiplicity_pretag_2015",   ";#jets;#events with l-",6,0.5,6.5);
    m_hSvc.create1D("Wplus_jetmultiplicity_pretag_2016",  ";#jets;#events with l+",6,0.5,6.5);
    m_hSvc.create1D("Wmin_jetmultiplicity_pretag_2016",   ";#jets;#events with l-",6,0.5,6.5);
    m_hSvc.create1D("Wplus_jetmultiplicity_tag_2015",  ";#jets;#events with l+",6,0.5,6.5); // 2ex,3ex,4ex,2in,3in,4in,5in
    m_hSvc.create1D("Wmin_jetmultiplicity_tag_2015",   ";#jets;#events with l-",6,0.5,6.5);
    m_hSvc.create1D("Wplus_jetmultiplicity_tag_2016",  ";#jets;#events with l+",6,0.5,6.5);
    m_hSvc.create1D("Wmin_jetmultiplicity_tag_2016",   ";#jets;#events with l-",6,0.5,6.5);
    //###
    m_hSvc.create1D("Wplus_jetmultiplicity_pretag_C_2015",  ";#jets;#events with l+",6,0.5,6.5); // 2ex,3ex,4ex,2in,3in,4in,5in
    m_hSvc.create1D("Wmin_jetmultiplicity_pretag_C_2015",   ";#jets;#events with l-",6,0.5,6.5);
    m_hSvc.create1D("Wplus_jetmultiplicity_pretag_C_2016",  ";#jets;#events with l+",6,0.5,6.5);
    m_hSvc.create1D("Wmin_jetmultiplicity_pretag_C_2016",   ";#jets;#events with l-",6,0.5,6.5);
    m_hSvc.create1D("Wplus_jetmultiplicity_tag_C_2015",  ";#jets;#events with l+",6,0.5,6.5); // 2ex,3ex,4ex,2in,3in,4in,5in
    m_hSvc.create1D("Wmin_jetmultiplicity_tag_C_2015",   ";#jets;#events with l-",6,0.5,6.5);
    m_hSvc.create1D("Wplus_jetmultiplicity_tag_C_2016",  ";#jets;#events with l+",6,0.5,6.5);
    m_hSvc.create1D("Wmin_jetmultiplicity_tag_C_2016",   ";#jets;#events with l-",6,0.5,6.5);
    //###
    m_hSvc.create1D("Wplus_jetmultiplicity_pretag_cc_2015",  ";#jets;#events with l+",6,0.5,6.5); // 2ex,3ex,4ex,2in,3in,4in,5in
    m_hSvc.create1D("Wmin_jetmultiplicity_pretag_cc_2015",   ";#jets;#events with l-",6,0.5,6.5);
    m_hSvc.create1D("Wplus_jetmultiplicity_pretag_cc_2016",  ";#jets;#events with l+",6,0.5,6.5);
    m_hSvc.create1D("Wmin_jetmultiplicity_pretag_cc_2016",   ";#jets;#events with l-",6,0.5,6.5);
    m_hSvc.create1D("Wplus_jetmultiplicity_tag_cc_2015",  ";#jets;#events with l+",6,0.5,6.5); // 2ex,3ex,4ex,2in,3in,4in,5in
    m_hSvc.create1D("Wmin_jetmultiplicity_tag_cc_2015",   ";#jets;#events with l-",6,0.5,6.5);
    m_hSvc.create1D("Wplus_jetmultiplicity_tag_cc_2016",  ";#jets;#events with l+",6,0.5,6.5);
    m_hSvc.create1D("Wmin_jetmultiplicity_tag_cc_2016",   ";#jets;#events with l-",6,0.5,6.5);
    //###
    m_hSvc.create1D("Wplus_jetmultiplicity_pretag_B_2015",  ";#jets;#events with l+",6,0.5,6.5); // 2ex,3ex,4ex,2in,3in,4in,5in
    m_hSvc.create1D("Wmin_jetmultiplicity_pretag_B_2015",   ";#jets;#events with l-",6,0.5,6.5);
    m_hSvc.create1D("Wplus_jetmultiplicity_pretag_B_2016",  ";#jets;#events with l+",6,0.5,6.5);
    m_hSvc.create1D("Wmin_jetmultiplicity_pretag_B_2016",   ";#jets;#events with l-",6,0.5,6.5);
    m_hSvc.create1D("Wplus_jetmultiplicity_tag_B_2015",  ";#jets;#events with l+",6,0.5,6.5); // 2ex,3ex,4ex,2in,3in,4in,5in
    m_hSvc.create1D("Wmin_jetmultiplicity_tag_B_2015",   ";#jets;#events with l-",6,0.5,6.5);
    m_hSvc.create1D("Wplus_jetmultiplicity_tag_B_2016",  ";#jets;#events with l+",6,0.5,6.5);
    m_hSvc.create1D("Wmin_jetmultiplicity_tag_B_2016",   ";#jets;#events with l-",6,0.5,6.5);
    //###
    m_hSvc.create1D("Wplus_jetmultiplicity_pretag_lf_2015",  ";#jets;#events with l+",6,0.5,6.5); // 2ex,3ex,4ex,2in,3in,4in,5in
    m_hSvc.create1D("Wmin_jetmultiplicity_pretag_lf_2015",   ";#jets;#events with l-",6,0.5,6.5);
    m_hSvc.create1D("Wplus_jetmultiplicity_pretag_lf_2016",  ";#jets;#events with l+",6,0.5,6.5);
    m_hSvc.create1D("Wmin_jetmultiplicity_pretag_lf_2016",   ";#jets;#events with l-",6,0.5,6.5);
    m_hSvc.create1D("Wplus_jetmultiplicity_tag_lf_2015",  ";#jets;#events with l+",6,0.5,6.5); // 2ex,3ex,4ex,2in,3in,4in,5in
    m_hSvc.create1D("Wmin_jetmultiplicity_tag_lf_2015",   ";#jets;#events with l-",6,0.5,6.5);
    m_hSvc.create1D("Wplus_jetmultiplicity_tag_lf_2016",  ";#jets;#events with l+",6,0.5,6.5);
    m_hSvc.create1D("Wmin_jetmultiplicity_tag_lf_2016",   ";#jets;#events with l-",6,0.5,6.5);

  }; // if !m_boosted

 

  // ####################################################################
  // # input for W+jets estimation for convert-script in Top_Charge_Asymmetry
  if (!m_boosted) {
    // # 2015
    m_hSvc.create2D("HF_pretag_el_2015","; jet multiplicity",7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_tag_el_2015","; jet multiplicity"   ,7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_pretag_C_el_2015","; jet multiplicity",7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_tag_C_el_2015","; jet multiplicity"   ,7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_pretag_cc_el_2015","; jet multiplicity",7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_tag_cc_el_2015","; jet multiplicity"   ,7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_pretag_B_el_2015","; jet multiplicity",7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_tag_B_el_2015","; jet multiplicity"   ,7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_pretag_lf_el_2015","; jet multiplicity",7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_tag_lf_el_2015","; jet multiplicity"   ,7,0.5,7.5,3,0.5,3.5);

    m_hSvc.create2D("HF_pretag_mu_2015","; jet multiplicity",7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_tag_mu_2015","; jet multiplicity"   ,7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_pretag_C_mu_2015","; jet multiplicity",7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_tag_C_mu_2015","; jet multiplicity"   ,7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_pretag_cc_mu_2015","; jet multiplicity",7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_tag_cc_mu_2015","; jet multiplicity"   ,7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_pretag_B_mu_2015","; jet multiplicity",7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_tag_B_mu_2015","; jet multiplicity"   ,7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_pretag_lf_mu_2015","; jet multiplicity",7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_tag_lf_mu_2015","; jet multiplicity"   ,7,0.5,7.5,3,0.5,3.5);
    // # 2016
    m_hSvc.create2D("HF_pretag_el_2016","; jet multiplicity",7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_tag_el_2016","; jet multiplicity"   ,7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_pretag_C_el_2016","; jet multiplicity",7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_tag_C_el_2016","; jet multiplicity"   ,7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_pretag_cc_el_2016","; jet multiplicity",7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_tag_cc_el_2016","; jet multiplicity"   ,7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_pretag_B_el_2016","; jet multiplicity",7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_tag_B_el_2016","; jet multiplicity"   ,7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_pretag_lf_el_2016","; jet multiplicity",7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_tag_lf_el_2016","; jet multiplicity"   ,7,0.5,7.5,3,0.5,3.5);

    m_hSvc.create2D("HF_pretag_mu_2016","; jet multiplicity",7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_tag_mu_2016","; jet multiplicity"   ,7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_pretag_C_mu_2016","; jet multiplicity",7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_tag_C_mu_2016","; jet multiplicity"   ,7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_pretag_cc_mu_2016","; jet multiplicity",7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_tag_cc_mu_2016","; jet multiplicity"   ,7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_pretag_B_mu_2016","; jet multiplicity",7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_tag_B_mu_2016","; jet multiplicity"   ,7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_pretag_lf_mu_2016","; jet multiplicity",7,0.5,7.5,3,0.5,3.5);
    m_hSvc.create2D("HF_tag_lf_mu_2016","; jet multiplicity"   ,7,0.5,7.5,3,0.5,3.5);
  }; // !m_boosted
  // #


  if (!m_boosted) {
    // only for resolved signal (resWCRtag + 4jets +chi2)
    // ttbar reconstruction resolved
    // 2015
    // matched objects - matched to truth?
    m_hSvc.create1D("W_Hadronic_2015", "; M_{j_{1}j_{2}} [GeV] ; Events"      , 1000, 0, 1000);
    m_hSvc.create1D("T_Hadronic_2015", "; M_{j_{1}j_{2}j_{bh}} [GeV] ; Events", 1000, 0, 1000);
    m_hSvc.create1D("T_Leptonic_2015", "; M_{j_{bl}l#nu} [GeV] ; Events"      , 1000, 0, 1000);
    m_hSvc.create1D("PT_Diff_2015",   "; #Delta p_{T} [GeV] ; Events"         , 1000, -500, 500);
    // Chi2 results
    m_hSvc.create1DVar("mtlep_chi2_2015", "; leptonic top mass [GeV]; Events"    , varBinN4, varBin4);
    m_hSvc.create1DVar("mthad_chi2_2015", "; hadronic top mass [GeV]; Events"    , varBinN4, varBin4);
    m_hSvc.create1DVar("mwhad_chi2_2015", "; hadronic W boson mass [GeV]; Events", 40, 0, 400);
    m_hSvc.create1D("chi2_2015",          "; log(#chi^{2}) ; Events"             , 50, -3, 7);
    // 2016
    // matched objects - matched to truth?
    m_hSvc.create1D("W_Hadronic_2016", "; M_{j_{1}j_{2}} [GeV] ; Events"      , 1000, 0, 1000);
    m_hSvc.create1D("T_Hadronic_2016", "; M_{j_{1}j_{2}j_{bh}} [GeV] ; Events", 1000, 0, 1000);
    m_hSvc.create1D("T_Leptonic_2016", "; M_{j_{bl}l#nu} [GeV] ; Events"      , 1000, 0, 1000);
    m_hSvc.create1D("PT_Diff_2016",   "; #Delta p_{T} [GeV] ; Events"         , 1000, -500, 500);
    // Chi2 results
    m_hSvc.create1DVar("mtlep_chi2_2016", "; leptonic top mass [GeV]; Events"    , varBinN4, varBin4);
    m_hSvc.create1DVar("mthad_chi2_2016", "; hadronic top mass [GeV]; Events"    , varBinN4, varBin4);
    m_hSvc.create1DVar("mwhad_chi2_2016", "; hadronic W boson mass [GeV]; Events", 40, 0, 400);
    m_hSvc.create1D("chi2_2016",          "; log(#chi^{2}) ; Events"             , 50, -3, 7);
  }; // !m_boosted
  // #

  // ####################################################################
  // signal region (boosted or resWCRtag + 4jets +chi2)
  // # 2015
  m_hSvc.create1DVar("leadTrkbJetPt_2015",   "; leading b-jet p_{T} [GeV]; Events"     , varBinN1, varBin1);
  m_hSvc.create1DVar("leadJetPt_2015",      "; leading b-jet p_{T} [GeV]; Events"     , varBinN1, varBin1);
  m_hSvc.create1D("nTrkBtagJets_2015",       "; number of b-tagged jets ; Events"      , 10, 0, 10);
  m_hSvc.create1D("nJets_2015",             "; number of b-tagged jets ; Events"      , 10, 0, 10);
  m_hSvc.create1D("closejl_minDeltaR_2015", "; min #Delta R(lep, jet); Events"        , 50, 0, 5); //1163
  m_hSvc.create1DVar("closejl_pt_2015",     "; Pt of closest jet to lep [GeV]; Events", varBinN1, varBin1); //1164

  m_hSvc.create1D("mu_2015",   "; <mu>; Events"                             , 100, 0, 100);
  m_hSvc.create1D("vtxz_2015", ";Z position of truth primary vertex; Events", 40, -400, 400);
  m_hSvc.create1D("npv_2015",  "; npv; Events"                              , 50, 0, 50);

  m_hSvc.create1D("weight_2015",        "; applied weights; Events"  , 2000, -10, 10);
  m_hSvc.create2D("weight_leptPt_2015", ";lept Pt (GeV); weight",100, 25, 525, 2000, -10, 10);

  m_hSvc.create1DVar("MET_2015",      "; missing E_{T} [GeV]; Events"     , varBinN1, varBin1);
  m_hSvc.create1D("MET_phi_2015","; missing E_{T} #phi [rd] ; Events", 32, -3.2, 3.2);  // X
  m_hSvc.create1D("MWT_2015",    "; W transverse mass [GeV]; Events" , 20, 0, 200); //X
  m_hSvc.create1D("METpMWT_2015",";MET+MWT;events"                   ,100,0,1000); // X

  m_hSvc.create1D("lepPt_2015",     "; Pt of lept [GeV]; Events"  , 100, 25, 525);  // X
  m_hSvc.create1D("lepEta_2015",    "; lepton #eta ; Events"      , 20, -2.5, 2.5);  // X
  m_hSvc.create1D("lepPhi_2015",    "; lepton #phi [rd] ; Events" , 32, -3.2, 3.2);  // X
  m_hSvc.create1D("lepCharge_2015", "; lepton charge [e] ; Events", 5, -2.5, 2.5);  // X

  m_hSvc.create1DVar("mtt_2015", "; mass of the top-antitop system [GeV]; Events", varBinN5, varBin5);
  m_hSvc.create1DVar("trueMtt_2015", "; mass of the top-antitop system [GeV]; Events", varBinN5, varBin5);
  // # 2016
  m_hSvc.create1DVar("leadTrkbJetPt_2016",   "; leading b-jet p_{T} [GeV]; Events"     , varBinN1, varBin1);
  m_hSvc.create1DVar("leadJetPt_2016",      "; leading b-jet p_{T} [GeV]; Events"     , varBinN1, varBin1);
  m_hSvc.create1D("nTrkBtagJets_2016",       "; number of b-tagged jets ; Events"      , 10, 0, 10);
  m_hSvc.create1D("nJets_2016",             "; number of b-tagged jets ; Events"      , 10, 0, 10);
  m_hSvc.create1D("closejl_minDeltaR_2016", "; min #Delta R(lep, jet); Events"        , 50, 0, 5); //1163
  m_hSvc.create1DVar("closejl_pt_2016",     "; Pt of closest jet to lep [GeV]; Events", varBinN1, varBin1); //1164

  m_hSvc.create1D("mu_2016",   "; <mu>; Events"                             , 100, 0, 100);
  m_hSvc.create1D("vtxz_2016", ";Z position of truth primary vertex; Events", 40, -400, 400);
  m_hSvc.create1D("npv_2016",  "; npv; Events"                              , 50, 0, 50);

  m_hSvc.create1D("weight_2016",        "; applied weights; Events"  , 2000, -10, 10);
  m_hSvc.create2D("weight_leptPt_2016", ";lept Pt (GeV);  weight",100, 25, 525, 2000, -10, 10);

  m_hSvc.create1DVar("MET_2016",      "; missing E_{T} [GeV]; Events"     , varBinN1, varBin1);
  m_hSvc.create1D("MET_phi_2016","; missing E_{T} #phi [rd] ; Events", 32, -3.2, 3.2);  // X
  m_hSvc.create1D("MWT_2016",    "; W transverse mass [GeV]; Events" , 20, 0, 200); //X
  m_hSvc.create1D("METpMWT_2016",";MET+MWT;events"                   ,100,0,1000); // X

  m_hSvc.create1D("lepPt_2016",     "; Pt of lept [GeV]; Events"  , 100, 25, 525);  // X
  m_hSvc.create1D("lepEta_2016",    "; lepton #eta ; Events"      , 20, -2.5, 2.5);  // X
  m_hSvc.create1D("lepPhi_2016",    "; lepton #phi [rd] ; Events" , 32, -3.2, 3.2);  // X
  m_hSvc.create1D("lepCharge_2016", "; lepton charge [e] ; Events", 5, -2.5, 2.5);  // X

  m_hSvc.create1DVar("mtt_2016", "; mass of the top-antitop system [GeV]; Events", varBinN5, varBin5);
  m_hSvc.create1DVar("trueMtt_2016", "; mass of the top-antitop system [GeV]; Events", varBinN5, varBin5);

  // ####################################################################
  if (m_boosted) {
    // signal region
    // 2015
    m_hSvc.create1DVar("largeJetPt_2015",      "; large jet p_{T} [GeV] ; Events"        , varBinN2, varBin2);
    m_hSvc.create1D("largeJetM_2015",          "; large jet mass [GeV] ; Events"         , 30, 0, 300);
    m_hSvc.create1D("largeJetEta_2015",        "; large jet #eta ; Events"               , 20, -2., 2.);
    m_hSvc.create1D("largeJetPhi_2015",        "; large jet #phi [rd] ; Events"          , 32, -3.2, 3.2);
    m_hSvc.create1D("largeJetSd12_2015",       "; large jet #sqrt{d_{12}} [GeV] ; Events", 20, 0, 200);
    m_hSvc.create1D("largeJet_tau32_2015",     "; #tau_{32}; Events"                     , 20, 0, 1);
    m_hSvc.create1D("largeJet_tau32_wta_2015", "; #tau_{32} wta; Events"                 , 20, 0, 1);
    m_hSvc.create1D("largeJet_tau21_2015",     "; #tau_{21}; Events"                     , 20, 0, 1);
    m_hSvc.create1D("largeJet_tau21_wta_2015", "; #tau_{21} wta; Events"                 , 20, 0, 1);

    m_hSvc.create1DVar("closeJetPt_boost_2015",     "; Pt of closest jet (sj) to lep [GeV]; Events", varBinN1, varBin1); //1164

    // TCA boosted
    m_hSvc.create1D("DeltaY_lep_hadTop_2015",                    ";Delta |Y|(lep, had top);Events"             ,50,-2.5,2.5); // boosted
    m_hSvc.create1D("DeltaEta_lep_hadTop_2015",                  ";Delta |Eta|(lep, had top);Events"           ,50,-2.5,2.5); // boosted
    m_hSvc.create1D("DeltaY_Top_antiTop_2015",           ";Delta |Y|(lep top, had top);Events"         ,50,-2.5,2.5);  // reconstructed top
    m_hSvc.create1D("DeltaY_Top_antiTop_range2_2015",    ";Delta |Y|(lep top, had top);Events"         ,100,-5,5);  // reconstructed top
    m_hSvc.create1D("DeltaEta_Top_antiTop_2015",         ";Delta |Eta|(lep top, had top);Events"       ,50,-2.5,2.5);  // reconstructed top
    m_hSvc.create1D("DeltaY_truth_Top_antiTop_2015",     ";Delta |y|(truth: lep top, had top);Events",50,-2.5,2.5);  // truth ttbar before FSR
    m_hSvc.create1D("DeltaDeltaY_truth_reco_Top_antiTop_2015",     ";Delta |Y|(truth:t-tbar)-Delta|y|(rec. t-tbar;Events",50,-2.5,2.5);  // truth ttbar before FSR

    // 2016
    m_hSvc.create1DVar("largeJetPt_2016",      "; large jet p_{T} [GeV] ; Events"        , varBinN2, varBin2);
    m_hSvc.create1D("largeJetM_2016",          "; large jet mass [GeV] ; Events"         , 30, 0, 300);
    m_hSvc.create1D("largeJetEta_2016",        "; large jet #eta ; Events"               , 20, -2., 2.);
    m_hSvc.create1D("largeJetPhi_2016",        "; large jet #phi [rd] ; Events"          , 32, -3.2, 3.2);
    m_hSvc.create1D("largeJetSd12_2016",       "; large jet #sqrt{d_{12}} [GeV] ; Events", 20, 0, 200);
    m_hSvc.create1D("largeJet_tau32_2016",     "; #tau_{32}; Events"                     , 20, 0, 1);
    m_hSvc.create1D("largeJet_tau32_wta_2016", "; #tau_{32} wta; Events"                 , 20, 0, 1);
    m_hSvc.create1D("largeJet_tau21_2016",     "; #tau_{21}; Events"                     , 20, 0, 1);
    m_hSvc.create1D("largeJet_tau21_wta_2016", "; #tau_{21} wta; Events"                 , 20, 0, 1);

    m_hSvc.create1DVar("closeJetPt_boost_2016",     "; Pt of closest jet (sj) to lep [GeV]; Events", varBinN1, varBin1); //1164

    // TCA boosted
    m_hSvc.create1D("DeltaY_lep_hadTop_2016",                    ";Delta |Y|(lep, had top);Events"             ,50,-2.5,2.5); // boosted
    m_hSvc.create1D("DeltaEta_lep_hadTop_2016",                  ";Delta |Eta|(lep, had top);Events"           ,50,-2.5,2.5); // boosted
    m_hSvc.create1D("DeltaY_Top_antiTop_2016",           ";Delta |Y|(lep top, had top);Events"         ,50,-2.5,2.5);  // reconstructed top
    m_hSvc.create1D("DeltaY_Top_antiTop_range2_2016",    ";Delta |Y|(lep top, had top);Events"         ,100,-5,5);  // reconstructed top
    m_hSvc.create1D("DeltaEta_Top_antiTop_2016",         ";Delta |Eta|(lep top, had top);Events"       ,50,-2.5,2.5);  // reconstructed top
    m_hSvc.create1D("DeltaY_truth_Top_antiTop_2016",     ";Delta |Eta|(truth: lep top, had top);Events",50,-2.5,2.5);  // truth ttbar before FSR
    m_hSvc.create1D("DeltaDeltaY_truth_reco_Top_antiTop_2016",     ";Delta |Y|(truth:t-tbar)-Delta|y|(rec. t-tbar;Events",50,-2.5,2.5);  // truth ttbar before FSR

    // NEW comparison purpose!
    m_hSvc.create1D("DeltaY_Top_antiTop_1516",           ";Delta |Y|(lep top, had top);Events"         ,100,-5,5);  // reconstructed top
   m_hSvc.create1D("DeltaY_Top_antiTop_1516_test",           ";Delta |Y|(lep top, had top);Events"         ,1000,-5,5);  // reconstructed top
    m_hSvc.create1D("DeltaY_truth_Top_antiTop_1516",           ";truth Delta |Y|(lep top, had top);Events"         ,100,-5,5);  // reconstructed top
    m_hSvc.create1D("DeltaDeltaY_truth_reco_Top_antiTop_1516",     ";Delta |Y|(truth:t-tbar)-Delta|y|(rec. t-tbar;Events",50,-2.5,2.5);  // truth ttbar before FSR
  }; // if (m_boosted)


}

AnaMultijetAllIn1::~AnaMultijetAllIn1() {
}

void AnaMultijetAllIn1::run(const Event &evt, double weight, const std::string &s){

  bool debug =false;
  if (debug ) std::cout<<" Inside RUN AnaMultijetAllIn1 with weight: "<<weight<<std::endl;


  // prepared to modify leptonSF weight here (in case of electron channel, but weights are ==1):
  if (m_electron && false) { // only for electrons
    if (evt.weight_indiv_leptonSF_EL_ChargeID()!=1 || evt.weight_indiv_leptonSF_EL_ChargeMisID()!=1 ||
	evt.weight_indiv_leptonSF_EL_ChargeID_up()!=1 || evt.weight_indiv_leptonSF_EL_ChargeMisID_STAT_up()!=1 ||  evt.weight_indiv_leptonSF_EL_ChargeMisID_SYST_up()!=1 ||
	evt.weight_indiv_leptonSF_EL_ChargeID_down()!=1 || evt.weight_indiv_leptonSF_EL_ChargeMisID_STAT_down()!=1  || evt.weight_indiv_leptonSF_EL_ChargeMisID_SYST_down()!=1
	){
      std::cout<<" ChargeID: "<<evt.weight_indiv_leptonSF_EL_ChargeID()<<std::endl;
      std::cout<<" ChargeID variation: (up) "<<evt.weight_indiv_leptonSF_EL_ChargeID_up()<<"     (down) "<<evt.weight_indiv_leptonSF_EL_ChargeID_down()<<std::endl;
      std::cout<<" ChargeMisID: "<<evt.weight_indiv_leptonSF_EL_ChargeMisID()<<std::endl;
      std::cout<<" ChargeMisID variation: STAT (up) "<<evt.weight_indiv_leptonSF_EL_ChargeMisID_STAT_up()<<"     (down) "<<evt.weight_indiv_leptonSF_EL_ChargeMisID_STAT_down()<<std::endl;
      std::cout<<" ChargeMisID variation: SYST (up) "<<evt.weight_indiv_leptonSF_EL_ChargeMisID_SYST_up()<<"     (down) "<<evt.weight_indiv_leptonSF_EL_ChargeMisID_SYST_down()<<std::endl;
    }
  };


  char name[200];

  std::string suffix = s;
 
  HistogramService *h = &m_hSvc;
  // controlplots, no cuts applied for storage of all events (no btag cat separattion) // is equal to yields e.g. yields_res_el_2015
  if (evt.passes("rejets_2015"))   h->h1D("Controlplot_initial_rejets_2015","",suffix)->Fill(-1); 
  if (evt.passes("rmujets_2015"))  h->h1D("Controlplot_initial_rmujets_2015","",suffix)->Fill(-1);  
  if (evt.passes("rejets_2016"))   h->h1D("Controlplot_initial_rejets_2016","",suffix)->Fill(-1);  
  if (evt.passes("rmujets_2016"))  h->h1D("Controlplot_initial_rmujets_2016","",suffix)->Fill(-1);
  
  if (evt.passes("bmujets_2015"))  h->h1D("Controlplot_initial_bmujets_2015","",suffix)->Fill(-1);
  if (evt.passes("bmujets_2015"))  h->h1D("Controlplot_initial_bmujets_2015","",suffix)->Fill(evt.Btagcat());
  if (evt.passes("bejets_2015"))   h->h1D("Controlplot_initial_bejets_2015","",suffix)->Fill(-1);
  if (evt.passes("bejets_2015"))   h->h1D("Controlplot_initial_bejets_2015","",suffix)->Fill(evt.Btagcat());
  if (evt.passes("bmujets_2016"))  h->h1D("Controlplot_initial_bmujets_2016","",suffix)->Fill(-1);
  if (evt.passes("bmujets_2016"))  h->h1D("Controlplot_initial_bmujets_2016","",suffix)->Fill(evt.Btagcat());
  if (evt.passes("bejets_2016"))   h->h1D("Controlplot_initial_bejets_2016","",suffix)->Fill(-1);
  if (evt.passes("bejets_2016"))   h->h1D("Controlplot_initial_bejets_2016","",suffix)->Fill(evt.Btagcat());
  // same Controlplot_initial values, weighted:
  if (evt.passes("rejets_2015"))   h->h1D("Controlplot_initial_rejets_2015_weight","",suffix)->Fill(-1, weight); 
  if (evt.passes("rmujets_2015"))  h->h1D("Controlplot_initial_rmujets_2015_weight","",suffix)->Fill(-1, weight);  
  if (evt.passes("rejets_2016"))   h->h1D("Controlplot_initial_rejets_2016_weight","",suffix)->Fill(-1, weight);  
  if (evt.passes("rmujets_2016"))  h->h1D("Controlplot_initial_rmujets_2016_weight","",suffix)->Fill(-1, weight);
  
  if (evt.passes("bmujets_2015"))  h->h1D("Controlplot_initial_bmujets_2015_weight","",suffix)->Fill(-1, weight);
  if (evt.passes("bmujets_2015"))  h->h1D("Controlplot_initial_bmujets_2015_weight","",suffix)->Fill(evt.Btagcat(), weight);
  if (evt.passes("bejets_2015"))   h->h1D("Controlplot_initial_bejets_2015_weight","",suffix)->Fill(-1, weight);
  if (evt.passes("bejets_2015"))   h->h1D("Controlplot_initial_bejets_2015_weight","",suffix)->Fill(evt.Btagcat(), weight);
  if (evt.passes("bmujets_2016"))  h->h1D("Controlplot_initial_bmujets_2016_weight","",suffix)->Fill(-1, weight);
  if (evt.passes("bmujets_2016"))  h->h1D("Controlplot_initial_bmujets_2016_weight","",suffix)->Fill(evt.Btagcat(), weight);
  if (evt.passes("bejets_2016"))   h->h1D("Controlplot_initial_bejets_2016_weight","",suffix)->Fill(-1, weight);
  if (evt.passes("bejets_2016"))   h->h1D("Controlplot_initial_bejets_2016_weight","",suffix)->Fill(evt.Btagcat(), weight);
  // --|


  if (evt.passes("rejetsWCR_2015"))   h->h1D("Controlplot_initial_rejetsWCR_2015","",suffix)->Fill(-1);   
  if (evt.passes("rejetsWCR_2015"))   h->h1D("Controlplot_initial_rejetsWCR_2015","",suffix)->Fill(evt.Btagcat());   
  if (evt.passes("rmujetsWCR_2015"))  h->h1D("Controlplot_initial_rmujetsWCR_2015","",suffix)->Fill(-1); 
  if (evt.passes("rmujetsWCR_2015"))  h->h1D("Controlplot_initial_rmujetsWCR_2015","",suffix)->Fill(evt.Btagcat());    
  if (evt.passes("rejetsWCR_2016"))   h->h1D("Controlplot_initial_rejetsWCR_2016","",suffix)->Fill(-1); 
  if (evt.passes("rejetsWCR_2016"))   h->h1D("Controlplot_initial_rejetsWCR_2016","",suffix)->Fill(evt.Btagcat()); 
  if (evt.passes("rmujetsWCR_2016"))  h->h1D("Controlplot_initial_rmujetsWCR_2016","",suffix)->Fill(-1);
  if (evt.passes("rmujetsWCR_2016"))  h->h1D("Controlplot_initial_rmujetsWCR_2016","",suffix)->Fill(evt.Btagcat());

  if (evt.passes("rejetsWCRtag_2015"))   h->h1D("Controlplot_initial_rejetsWCRtag_2015","",suffix)->Fill(-1);
  if (evt.passes("rejetsWCRtag_2015"))   h->h1D("Controlplot_initial_rejetsWCRtag_2015","",suffix)->Fill(evt.Btagcat());  
  if (evt.passes("rmujetsWCRtag_2015"))  h->h1D("Controlplot_initial_rmujetsWCRtag_2015","",suffix)->Fill(-1);
  if (evt.passes("rmujetsWCRtag_2015"))  h->h1D("Controlplot_initial_rmujetsWCRtag_2015","",suffix)->Fill(evt.Btagcat());   
  if (evt.passes("rejetsWCRtag_2016"))   h->h1D("Controlplot_initial_rejetsWCRtag_2016","",suffix)->Fill(-1);  
  if (evt.passes("rejetsWCRtag_2016"))   h->h1D("Controlplot_initial_rejetsWCRtag_2016","",suffix)->Fill(evt.Btagcat());  
  if (evt.passes("rmujetsWCRtag_2016"))  h->h1D("Controlplot_initial_rmujetsWCRtag_2016","",suffix)->Fill(-1);
  if (evt.passes("rmujetsWCRtag_2016"))  h->h1D("Controlplot_initial_rmujetsWCRtag_2016","",suffix)->Fill(evt.Btagcat());


 
 

  // ######################################################
  // ##
  // ## check lepton channel
  // ##
  if (m_electron && (evt.electron().size() != 1 || evt.muon().size() != 0))
    return;
  if (!m_electron && (evt.electron().size() != 0 || evt.muon().size() != 1))
    return;
  if (debug ) std::cout<<" Check channel passed"<<std::endl;
  // ##
  // ######################################################


  // print cutselection:
  if (debug ){
    // #2015
    if (evt.passes("rmujetsWCR_2015"))     std::cout<<" Event passes rmujetsWCR_2015"<<std::endl;
    if (evt.passes("rmujetsWCRtag_2015"))  std::cout<<" Event passes rmujetsWCRtag_2015"<<std::endl;
    if (evt.passes("rejetsWCR_2015"))      std::cout<<" Event passes rejetsWCR_2015"<<std::endl;
    if (evt.passes("rejetsWCRtag_2015"))   std::cout<<" Event passes rejetsWCRtag_2015"<<std::endl;
    if (evt.passes("bmujets_2015")) std::cout<<" Event passes bmujets_2015"<<std::endl;
    if (evt.passes("bejets_2015"))  std::cout<<" Event passes bejets_2015"<<std::endl;

    // #2016
    if (evt.passes("rmujetsWCR_2016"))     std::cout<<" Event passes rmujetsWCR_2016"<<std::endl;
    if (evt.passes("rmujetsWCRtag_2016"))  std::cout<<" Event passes rmujetsWCRtag_2016"<<std::endl;
    if (evt.passes("rejetsWCR_2016"))      std::cout<<" Event passes rejetsWCR_2016"<<std::endl;
    if (evt.passes("rejetsWCRtag_2016"))   std::cout<<" Event passes rejetsWCRtag_2016"<<std::endl;
    if (evt.passes("bmujets_2016")) std::cout<<" Event passes bmujets_2016"<<std::endl;
    if (evt.passes("bejets_2016"))  std::cout<<" Event passes bejets_2016"<<std::endl;
  };
  
  // ######################################################
  // ##
  // ## topology check: boosted or resolved requested
  // ##
  if (m_boosted){
    if (!(evt.passes("bmujets_2015") || evt.passes("bejets_2015") || evt.passes("bmujets_2016") || evt.passes("bejets_2016"))){
      if (debug ) std::cout<<" RETURN: boost, but no boost selection "<<std::endl;
      return;
    };
  };
  if (!m_boosted){
    // selection with lowest critera : rxjetsWCR:
    if (!(evt.passes("rmujetsWCR_2015") || evt.passes("rmujetsWCR_2016") || evt.passes("rejetsWCR_2015") || evt.passes("rejetsWCR_2016"))) {
      if (debug) std::cout<<" RETURN, resolved, but no resolved selection "<<std::endl;
      return;
    };
  };
  // // // boosted veto for resolved channel:
  // if (!m_boosted && (evt.passes("bmujets_2015") || evt.passes("bejets_2015") || evt.passes("bmujets_2016") || evt.passes("bejets_2016"))) {
  //   if (debug) std::cout<<" boosted veto for resolved event"<<std::endl;
  //   return;
  // };

  if (debug ) std::cout<<" Check selected topology passed"<<std::endl;
  // ##
  // ######################################################

  // ######################################################
  // ##
  // apply MET Cut
  bool do_METcut = false;
  double MET_GeV =  evt.met().Perp()*1e-3;
  if (debug) std::cout<<" MET: "<<MET_GeV<<std::endl;
  if (MET_GeV<40 && do_METcut)     {
    if (debug) std::cout<<" Return because of METcut set to >= 40 GeV"<<std::endl;
    return;
  }
  // ##
  // ######################################################

  // ######################################################
  // ##
  // ## implement cut from TopAnalysis 2.4.21:  LOG10_CHI2 < 0.9
  // ## in TA2.4.21 calo b-tag jets are used instead of track b-tag jets
  // ##
  bool is_4j_signal = false;
  bool is_btag_signal = false;
  bool is_chi2_signal = false;
  float chi2Value_global = 1000000; // log10(1000000) = 6
  // ##
  // ##
  // ######################################################


  // ######################################################
  // ##
  // ##  set weight of QCD to 0 in case it is nan // Problem with ~10 events in LooseData 2016 (->Sanmay), inf is problem of electron channel
  if(std::isnan(weight) ) {
    std::cout<<"Weight is Nan, making it  0"<<std::endl;
    weight = 0;
  }
  if(std::isinf(weight) ) {
    std::cout<<"Weight is inf, making it  0"<<std::endl;
    weight = 0;
  }
  // ##
  // ##
  // ######################################################



  // ######################################################
  // ##
  // ##
  // FIll "initial" histograms with btag cat

  if (!m_boosted && !( evt.passes("bmujets_2015") || evt.passes("bejets_2015") || evt.passes("bmujets_2016") || evt.passes("bejets_2016"))) {
    if (evt.passes("rejets_2015"))   h->h1D("Controlplot_initial_rejets_2015","",suffix)->Fill(evt.Btagcat()); 
    if (evt.passes("rmujets_2015"))  h->h1D("Controlplot_initial_rmujets_2015","",suffix)->Fill(evt.Btagcat());
    if (evt.passes("rejets_2016"))   h->h1D("Controlplot_initial_rejets_2016","",suffix)->Fill(evt.Btagcat());
    if (evt.passes("rmujets_2016"))  h->h1D("Controlplot_initial_rmujets_2016","",suffix)->Fill(evt.Btagcat());
    // weighted:
    if (evt.passes("rejets_2015"))   h->h1D("Controlplot_initial_rejets_2015_weight","",suffix)->Fill(evt.Btagcat(),weight); 
    if (evt.passes("rmujets_2015"))  h->h1D("Controlplot_initial_rmujets_2015_weight","",suffix)->Fill(evt.Btagcat(),weight);
    if (evt.passes("rejets_2016"))   h->h1D("Controlplot_initial_rejets_2016_weight","",suffix)->Fill(evt.Btagcat(),weight);
    if (evt.passes("rmujets_2016"))  h->h1D("Controlplot_initial_rmujets_2016_weight","",suffix)->Fill(evt.Btagcat(),weight);

  };
  if (evt.passes("rejetsWCR_2015"))   h->h1D("Controlplot_initial_rejetsWCR_2015","",suffix)->Fill(-1);   
  if (evt.passes("rejetsWCR_2015"))   h->h1D("Controlplot_initial_rejetsWCR_2015","",suffix)->Fill(evt.Btagcat());   
  if (evt.passes("rmujetsWCR_2015"))  h->h1D("Controlplot_initial_rmujetsWCR_2015","",suffix)->Fill(-1); 
  if (evt.passes("rmujetsWCR_2015"))  h->h1D("Controlplot_initial_rmujetsWCR_2015","",suffix)->Fill(evt.Btagcat());    
  if (evt.passes("rejetsWCR_2016"))   h->h1D("Controlplot_initial_rejetsWCR_2016","",suffix)->Fill(-1); 
  if (evt.passes("rejetsWCR_2016"))   h->h1D("Controlplot_initial_rejetsWCR_2016","",suffix)->Fill(evt.Btagcat()); 
  if (evt.passes("rmujetsWCR_2016"))  h->h1D("Controlplot_initial_rmujetsWCR_2016","",suffix)->Fill(-1);
  if (evt.passes("rmujetsWCR_2016"))  h->h1D("Controlplot_initial_rmujetsWCR_2016","",suffix)->Fill(evt.Btagcat());

  if (evt.passes("rejetsWCRtag_2015"))   h->h1D("Controlplot_initial_rejetsWCRtag_2015","",suffix)->Fill(-1);
  if (evt.passes("rejetsWCRtag_2015"))   h->h1D("Controlplot_initial_rejetsWCRtag_2015","",suffix)->Fill(evt.Btagcat());  
  if (evt.passes("rmujetsWCRtag_2015"))  h->h1D("Controlplot_initial_rmujetsWCRtag_2015","",suffix)->Fill(-1);
  if (evt.passes("rmujetsWCRtag_2015"))  h->h1D("Controlplot_initial_rmujetsWCRtag_2015","",suffix)->Fill(evt.Btagcat());   
  if (evt.passes("rejetsWCRtag_2016"))   h->h1D("Controlplot_initial_rejetsWCRtag_2016","",suffix)->Fill(-1);  
  if (evt.passes("rejetsWCRtag_2016"))   h->h1D("Controlplot_initial_rejetsWCRtag_2016","",suffix)->Fill(evt.Btagcat());  
  if (evt.passes("rmujetsWCRtag_2016"))  h->h1D("Controlplot_initial_rmujetsWCRtag_2016","",suffix)->Fill(-1);
  if (evt.passes("rmujetsWCRtag_2016"))  h->h1D("Controlplot_initial_rmujetsWCRtag_2016","",suffix)->Fill(evt.Btagcat());


  if (evt.passes("bmujets_2015"))  h->h1D("Controlplot_initial_bmujets_2015","",suffix)->Fill(-1);
  if (evt.passes("bmujets_2015"))  h->h1D("Controlplot_initial_bmujets_2015","",suffix)->Fill(evt.Btagcat());
  if (evt.passes("bejets_2015"))   h->h1D("Controlplot_initial_bejets_2015","",suffix)->Fill(-1);
  if (evt.passes("bejets_2015"))   h->h1D("Controlplot_initial_bejets_2015","",suffix)->Fill(evt.Btagcat());
  if (evt.passes("bmujets_2016"))  h->h1D("Controlplot_initial_bmujets_2016","",suffix)->Fill(-1);
  if (evt.passes("bmujets_2016"))  h->h1D("Controlplot_initial_bmujets_2016","",suffix)->Fill(evt.Btagcat());
  if (evt.passes("bejets_2016"))   h->h1D("Controlplot_initial_bejets_2016","",suffix)->Fill(-1);
  if (evt.passes("bejets_2016"))   h->h1D("Controlplot_initial_bejets_2016","",suffix)->Fill(evt.Btagcat()); 
 

  bool trig1(0);
  bool trig2(0);
  bool trig3(0);
  bool trig4(0);
  bool trig5(0);

  bool isTight = false;
  int lep_charge = 0;
  bool lep_charge_pos = false;
  float lep_ETA = 42;
  float lep_Y = 42;

  int Njets=evt.jet().size();
  if (Njets>3) is_4j_signal=true;

  TLorentzVector l;
  if (m_electron) {
    l = evt.electron()[0].mom();

    isTight = evt.electron()[0].isTightPP();
    lep_charge = evt.electron()[0].charge();
    lep_ETA = l.Eta();
    lep_Y = l.Rapidity();

    // //Electron trigers
    // trig1 = evt.electron()[0].HLT_e24_lhmedium_L1EM20VH();
    // trig2 = evt.electron()[0].HLT_e60_lhmedium();
    // trig3 = evt.electron()[0].HLT_e120_lhloose();
 
    // bool trig_MC = trig1 || trig2 || trig3;
    // bool trig_DT = trig1 || trig2 || trig3;

    // if (evt.channelNumber()!=0){
    //	 if (!trig_MC)return;
    // }else{
    //     if (!trig_DT)return;
    // }

  } else {
    l = evt.muon()[0].mom();

    isTight = evt.muon()[0].isTight();
    lep_charge = evt.muon()[0].charge();
    lep_ETA = l.Eta();
    lep_Y = l.Rapidity();

    ////Muon trigers
    // trig1 = evt.muon()[0].HLT_mu20_L1MU15(); //prescaled
    // trig2 = evt.muon()[0].HLT_mu50();
    // //// assumption:  HLT_mu24_ivarmedium unprescaled???
    // trig3 = evt.muon()[0].HLT_mu24_ivarmedium();
    //bool trig_prescaled   = trig1;
    //bool trig_unprescaled = trig2 || trig3;
    //if(!trig_prescaled && !trig_unprescaled) return;
     ////if (s!="_Loose")
    //if (isTight)
    //   if (trig_prescaled && !trig_unprescaled)	return;

  }//m_electron

  // ###########################
  // #
  // # Not compatible with systematics: Rerunning on same events leads to skipping all events:
  // # Duplicated event removal after the selection  
  // if (isDuplicateEvent(evt.runNumber(), evt.eventNumber(), l.Perp())){
  //   std::cout << "DUPLICATE EVENT! SKIPPING " << std::endl;
  //   m_Nduplicate++;
  //   return;
  // }
  // #
  // ###########################

  const TLorentzVector &j = evt.jet()[0].mom();

  int nTrkBtagged = 0; //nB-tagged jets
  float lead_bjet_pt=0.;

  for (size_t bidx = 0; bidx < evt.tjet().size(); ++bidx)
    if (evt.tjet()[bidx].btag_mv2c10_70_trk() && evt.tjet()[bidx].pass_trk()){
      if(nTrkBtagged==0) lead_bjet_pt=evt.tjet()[bidx].mom().Perp()*1e-3;
      nTrkBtagged += 1;
    };

  if (nTrkBtagged>=1) is_btag_signal=true;


  if (debug )  std::cout<<" Lepton Charge: "<<lep_charge<<std::endl;
  if (lep_charge>0) lep_charge_pos = true;
  if (lep_charge<0) lep_charge_pos = false;

  // Don't care about (calo) b-tagged jets
  // int nBtagged = 0; //nB-tagged jets
  // for (size_t bidx = 0; bidx < evt.jet().size(); ++bidx){
  //   if (evt.jet()[bidx].btag_mv2c20_70()){
  //     if(nBtagged==0) h->h1D("leadbJetPt", "", suffix)->Fill(evt.jet()[bidx].mom().Perp()*1e-3, weight);
  //     nBtagged += 1;
  //   }
  // };
  // h->h1D("nBtagJets", "", suffix)->Fill(nBtagged, weight);

  // ###############################################
  // # new version
  //define histogram labels:
  //--> HFSF multijet yields:
  // Bin Labels
  TString labels[8];
  labels[0] = "empty";
  labels[1] = "1ex";
  labels[2] = "2ex";
  labels[3] = "3ex";
  labels[4] = "4ex";
  labels[5] = "5in";
  labels[6] = "3in";
  labels[7] = "4in";

  TString labelsY[4];
  labelsY[0] = "empty";
  labelsY[1] = "pos";
  labelsY[2] = "neg";
  labelsY[3] = "all";
  if (!m_boosted ) {
    // error with Loose Data, histogram not set or whatever, bin number is 1, and labeling results in many error messages
    if (h->h2D("HF_pretag_el_2015","",suffix)->GetNbinsX() >1 && h->h2D("HF_pretag_el_2015","",suffix)->GetNbinsY()>1){ 
      
      for (unsigned int i_bin = 1; i_bin < 8; i_bin++) {
      	// # 2015
	if (debug) std::cout<<" i_bin: "<<i_bin<<" labels[i_bin]: "<<labels[i_bin]<<std::endl;
	h->h2D("HF_pretag_el_2015","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_pretag_C_el_2015","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_pretag_cc_el_2015","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_pretag_B_el_2015","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_pretag_lf_el_2015","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_tag_el_2015","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_tag_C_el_2015","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_tag_cc_el_2015","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_tag_B_el_2015","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_tag_lf_el_2015","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);

	h->h2D("HF_pretag_mu_2015","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_pretag_C_mu_2015","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_pretag_cc_mu_2015","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_pretag_B_mu_2015","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_pretag_lf_mu_2015","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_tag_mu_2015","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_tag_C_mu_2015","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_tag_cc_mu_2015","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_tag_B_mu_2015","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_tag_lf_mu_2015","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	// ### might be unnecessary soon
	// #
	if (i_bin>1 ){
	  unsigned int ni_bin=i_bin;
	  unsigned int ni2_bin=i_bin-1;
	  h->h1D("Wplus_jetmultiplicity_pretag_2015","",suffix)->GetXaxis()->SetBinLabel(ni2_bin,labels[ni_bin]);
	  h->h1D("Wmin_jetmultiplicity_pretag_2015","",suffix)->GetXaxis()->SetBinLabel(ni2_bin,labels[ni_bin]);
	  h->h1D("Wplus_jetmultiplicity_tag_2015","",suffix)->GetXaxis()->SetBinLabel(ni2_bin,labels[ni_bin]);
	  h->h1D("Wmin_jetmultiplicity_tag_2015","",suffix)->GetXaxis()->SetBinLabel(ni2_bin,labels[ni_bin]);

	  h->h1D("Wplus_jetmultiplicity_pretag_C_2015","",suffix)->GetXaxis()->SetBinLabel(ni2_bin,labels[ni_bin]);
	  h->h1D("Wmin_jetmultiplicity_pretag_C_2015","",suffix)->GetXaxis()->SetBinLabel(ni2_bin,labels[ni_bin]);
	  h->h1D("Wplus_jetmultiplicity_tag_C_2015","",suffix)->GetXaxis()->SetBinLabel(ni2_bin,labels[ni_bin]);
	  h->h1D("Wmin_jetmultiplicity_tag_C_2015","",suffix)->GetXaxis()->SetBinLabel(ni2_bin,labels[ni_bin]);

	  h->h1D("Wplus_jetmultiplicity_pretag_cc_2015","",suffix)->GetXaxis()->SetBinLabel(ni2_bin,labels[ni_bin]);
	  h->h1D("Wmin_jetmultiplicity_pretag_cc_2015","",suffix)->GetXaxis()->SetBinLabel(ni2_bin,labels[ni_bin]);
	  h->h1D("Wplus_jetmultiplicity_tag_cc_2015","",suffix)->GetXaxis()->SetBinLabel(ni2_bin,labels[ni_bin]);
	  h->h1D("Wmin_jetmultiplicity_tag_cc_2015","",suffix)->GetXaxis()->SetBinLabel(ni2_bin,labels[ni_bin]);

	  h->h1D("Wplus_jetmultiplicity_pretag_B_2015","",suffix)->GetXaxis()->SetBinLabel(ni2_bin,labels[ni_bin]);
	  h->h1D("Wmin_jetmultiplicity_pretag_B_2015","",suffix)->GetXaxis()->SetBinLabel(ni2_bin,labels[ni_bin]);
	  h->h1D("Wplus_jetmultiplicity_tag_B_2015","",suffix)->GetXaxis()->SetBinLabel(ni2_bin,labels[ni_bin]);
	  h->h1D("Wmin_jetmultiplicity_tag_B_2015","",suffix)->GetXaxis()->SetBinLabel(ni2_bin,labels[ni_bin]);

	  h->h1D("Wplus_jetmultiplicity_pretag_lf_2015","",suffix)->GetXaxis()->SetBinLabel(ni2_bin,labels[ni_bin]);
	  h->h1D("Wmin_jetmultiplicity_pretag_lf_2015","",suffix)->GetXaxis()->SetBinLabel(ni2_bin,labels[ni_bin]);
	  h->h1D("Wplus_jetmultiplicity_tag_lf_2015","",suffix)->GetXaxis()->SetBinLabel(ni2_bin,labels[ni_bin]);
	  h->h1D("Wmin_jetmultiplicity_tag_lf_2015","",suffix)->GetXaxis()->SetBinLabel(ni2_bin,labels[ni_bin]);
	};
	// #
	// ######
	// # 2016
	h->h2D("HF_pretag_el_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_pretag_C_el_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_pretag_cc_el_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_pretag_B_el_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_pretag_lf_el_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_tag_el_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_tag_C_el_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_tag_cc_el_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_tag_B_el_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_tag_lf_el_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);

	h->h2D("HF_pretag_mu_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_pretag_C_mu_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_pretag_cc_mu_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_pretag_B_mu_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_pretag_lf_mu_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_tag_mu_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_tag_C_mu_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_tag_cc_mu_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_tag_B_mu_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	h->h2D("HF_tag_lf_mu_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[i_bin]);
	// ### migh be unnecessary soon
	// #
	if (i_bin<7 ){
		int unsigned ni_bin=i_bin+1;
		h->h1D("Wplus_jetmultiplicity_pretag_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[ni_bin]);
		h->h1D("Wmin_jetmultiplicity_pretag_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[ni_bin]);
		h->h1D("Wplus_jetmultiplicity_tag_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[ni_bin]);
		h->h1D("Wmin_jetmultiplicity_tag_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[ni_bin]);

		h->h1D("Wplus_jetmultiplicity_pretag_C_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[ni_bin]);
		h->h1D("Wmin_jetmultiplicity_pretag_C_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[ni_bin]);
		h->h1D("Wplus_jetmultiplicity_tag_C_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[ni_bin]);
		h->h1D("Wmin_jetmultiplicity_tag_C_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[ni_bin]);

		h->h1D("Wplus_jetmultiplicity_pretag_cc_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[ni_bin]);
		h->h1D("Wmin_jetmultiplicity_pretag_cc_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[ni_bin]);
		h->h1D("Wplus_jetmultiplicity_tag_cc_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[ni_bin]);
		h->h1D("Wmin_jetmultiplicity_tag_cc_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[ni_bin]);

		h->h1D("Wplus_jetmultiplicity_pretag_B_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[ni_bin]);
		h->h1D("Wmin_jetmultiplicity_pretag_B_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[ni_bin]);
		h->h1D("Wplus_jetmultiplicity_tag_B_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[ni_bin]);
		h->h1D("Wmin_jetmultiplicity_tag_B_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[ni_bin]);

		h->h1D("Wplus_jetmultiplicity_pretag_lf_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[ni_bin]);
		h->h1D("Wmin_jetmultiplicity_pretag_lf_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[ni_bin]);
		h->h1D("Wplus_jetmultiplicity_tag_lf_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[ni_bin]);
		h->h1D("Wmin_jetmultiplicity_tag_lf_2016","",suffix)->GetXaxis()->SetBinLabel(i_bin,labels[ni_bin]);
	};
	// #
	// ######
      }; // for binX
      
      for (unsigned int binY = 1; binY < 4; binY++) {
        // # 2015
        h->h2D("HF_pretag_el_2015","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
        h->h2D("HF_pretag_C_el_2015","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
        h->h2D("HF_pretag_cc_el_2015","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
        h->h2D("HF_pretag_B_el_2015","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
        h->h2D("HF_pretag_lf_el_2015","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
        h->h2D("HF_tag_el_2015","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
        h->h2D("HF_tag_C_el_2015","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
        h->h2D("HF_tag_cc_el_2015","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
        h->h2D("HF_tag_B_el_2015","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
        h->h2D("HF_tag_lf_el_2015","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);

        h->h2D("HF_pretag_mu_2015","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
        h->h2D("HF_pretag_C_mu_2015","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
        h->h2D("HF_pretag_cc_mu_2015","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
        h->h2D("HF_pretag_B_mu_2015","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
        h->h2D("HF_pretag_lf_mu_2015","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
        h->h2D("HF_tag_mu_2015","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
        h->h2D("HF_tag_C_mu_2015","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
        h->h2D("HF_tag_cc_mu_2015","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
        h->h2D("HF_tag_B_mu_2015","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
        h->h2D("HF_tag_lf_mu_2015","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
        // # 2016
        h->h2D("HF_pretag_el_2016","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
        h->h2D("HF_pretag_C_el_2016","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
        h->h2D("HF_pretag_cc_el_2016","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
        h->h2D("HF_pretag_B_el_2016","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
        h->h2D("HF_pretag_lf_el_2016","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
        h->h2D("HF_tag_el_2016","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
        h->h2D("HF_tag_C_el_2016","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
	h->h2D("HF_tag_cc_el_2016","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
	h->h2D("HF_tag_B_el_2016","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
	h->h2D("HF_tag_lf_el_2016","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);

	h->h2D("HF_pretag_mu_2016","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
	h->h2D("HF_pretag_C_mu_2016","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
	h->h2D("HF_pretag_cc_mu_2016","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
	h->h2D("HF_pretag_B_mu_2016","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
	h->h2D("HF_pretag_lf_mu_2016","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
	h->h2D("HF_tag_mu_2016","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
	h->h2D("HF_tag_C_mu_2016","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
	h->h2D("HF_tag_cc_mu_2016","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
	h->h2D("HF_tag_B_mu_2016","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
	h->h2D("HF_tag_lf_mu_2016","",suffix)->GetYaxis()->SetBinLabel(binY,labelsY[binY]);
      }; // for binY
    }; // if NbinsX and NbinsY >1 

 

    // filling
    int jet_multi = evt.jet().size();
  
    std::vector<int> filled_bins;
    filled_bins.clear();
    if (jet_multi == 1)
      filled_bins.push_back(1);
    if (jet_multi == 2)
      filled_bins.push_back(2);
    if (jet_multi == 3) {
      filled_bins.push_back(3);
      filled_bins.push_back(6);
    };
    if (jet_multi == 4) {
      filled_bins.push_back(4);
      filled_bins.push_back(6);
      filled_bins.push_back(7);
    };
    if (jet_multi >= 5) {
      filled_bins.push_back(5);
      filled_bins.push_back(6);
      filled_bins.push_back(7);
    };
    
    // (still) resolved all = !boosted
    // loop over bins to fill

    //  Sherpa 1: truth jet matching for c-hadron
    //  Sherpa 2: no truth jet matching
    //if (debug|| true)  
    //std::cout<<"Event Sherpa W-filter (Sherpa 2.2: NO truth jet matching: "<<evt.Wfilter_Sherpa_nT()<<")"<<std::endl;
    int Wfilter=evt.Wfilter_Sherpa_nT();

    for (unsigned int i_jet = 0; i_jet < filled_bins.size();i_jet++) {
      // fill W+ and W- (total bin)
      // pretag 2015 (el)
      if (evt.passes("rejetsWCR_2015") )  {
	h->h2D("HF_pretag_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==1) h->h2D("HF_pretag_C_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==2) h->h2D("HF_pretag_cc_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==3 || Wfilter==4) h->h2D("HF_pretag_B_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==5) h->h2D("HF_pretag_lf_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
      };
      // pretag 2016 (el)
      if (evt.passes("rejetsWCR_2016") )  {
	h->h2D("HF_pretag_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==1) h->h2D("HF_pretag_C_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==2) h->h2D("HF_pretag_cc_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==3 || Wfilter==4) h->h2D("HF_pretag_B_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==5) h->h2D("HF_pretag_lf_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
      };
      // tag 2015 (el)
      if (evt.passes("rejetsWCRtag_2015") ){ 
	h->h2D("HF_tag_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==1) h->h2D("HF_tag_C_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==2) h->h2D("HF_tag_cc_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==3 || Wfilter==4) h->h2D("HF_tag_B_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==5) h->h2D("HF_tag_lf_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
      };
      // tag 2016 (el)
      if (evt.passes("rejetsWCRtag_2016") ){ 
	h->h2D("HF_tag_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==1) h->h2D("HF_tag_C_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==2) h->h2D("HF_tag_cc_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==3 || Wfilter==4) h->h2D("HF_tag_B_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==5) h->h2D("HF_tag_lf_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
      };
      // pretag 2015 (mu)
      if (evt.passes("rmujetsWCR_2015") ) {
	h->h2D("HF_pretag_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==1) h->h2D("HF_pretag_C_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==2) h->h2D("HF_pretag_cc_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==3 || Wfilter==4) h->h2D("HF_pretag_B_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==5) h->h2D("HF_pretag_lf_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
      };
      // pretag 2016 (mu)
      if (evt.passes("rmujetsWCR_2016") ) {
	h->h2D("HF_pretag_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==1) h->h2D("HF_pretag_C_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==2) h->h2D("HF_pretag_cc_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==3 || Wfilter==4) h->h2D("HF_pretag_B_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==5) h->h2D("HF_pretag_lf_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
      };
      // tag 2015 (mu)
      if (evt.passes("rmujetsWCRtag_2015") )  {
	h->h2D("HF_tag_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==1) h->h2D("HF_tag_C_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==2) h->h2D("HF_tag_cc_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==3 || Wfilter==4) h->h2D("HF_tag_B_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==5) h->h2D("HF_tag_lf_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
      };
      // tag 2016 (mu)
      if (evt.passes("rmujetsWCRtag_2016") )  {
	h->h2D("HF_tag_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==1) h->h2D("HF_tag_C_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==2) h->h2D("HF_tag_cc_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==3 || Wfilter==4) h->h2D("HF_tag_B_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
	if (Wfilter==5) h->h2D("HF_tag_lf_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 3,weight);
      };
      //###############################
      // # fill positive charged lepton row
      // #
      if (lep_charge_pos)  {

	// # pretag 2015 (el)
	if (evt.passes("rejetsWCR_2015"))  {
	  h->h2D("HF_pretag_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==1)    h->h2D("HF_pretag_C_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==2)    h->h2D("HF_pretag_cc_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==3 || Wfilter==4)    h->h2D("HF_pretag_B_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==5)    h->h2D("HF_pretag_lf_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	};
	// # pretag 2016 (el)
	if (evt.passes("rejetsWCR_2016"))  {
	  h->h2D("HF_pretag_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==1)   h->h2D("HF_pretag_C_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==2)   h->h2D("HF_pretag_cc_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==3 || Wfilter==4)    h->h2D("HF_pretag_B_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==5)   h->h2D("HF_pretag_lf_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	 };
	// # tag 2015 (el)
	if (evt.passes("rejetsWCRtag_2015")) {
	  h->h2D("HF_tag_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==1)    h->h2D("HF_tag_C_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if(Wfilter==2)     h->h2D("HF_tag_cc_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==3 || Wfilter==4)    h->h2D("HF_tag_B_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==5)    h->h2D("HF_tag_lf_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	};
	// # tag 2016 (el)
	if (evt.passes("rejetsWCRtag_2016")) {
	  h->h2D("HF_tag_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==1)   h->h2D("HF_tag_C_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if(Wfilter==2)    h->h2D("HF_tag_cc_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==3 || Wfilter==4)   h->h2D("HF_tag_B_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==5)   h->h2D("HF_tag_lf_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	};
	// # pretag 2015 (mu)
	if (evt.passes("rmujetsWCR_2015") ) {
	  h->h2D("HF_pretag_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==1)   h->h2D("HF_pretag_C_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==2)   h->h2D("HF_pretag_cc_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==3 || Wfilter==4)  h->h2D("HF_pretag_B_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==5)    h->h2D("HF_pretag_lf_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	};
	// # pretag 2016 (mu)
	if (evt.passes("rmujetsWCR_2016") ) {
	  h->h2D("HF_pretag_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==1) h->h2D("HF_pretag_C_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==2) h->h2D("HF_pretag_cc_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==3 || Wfilter==4) h->h2D("HF_pretag_B_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==5) h->h2D("HF_pretag_lf_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	};
	// # tag 2015 (mu)
	if (evt.passes("rmujetsWCRtag_2015") ){
	  h->h2D("HF_tag_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==1) h->h2D("HF_tag_C_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==2) h->h2D("HF_tag_cc_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==3 || Wfilter==4) h->h2D("HF_tag_B_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==5) h->h2D("HF_tag_lf_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	};
 
	// # tag 2016 (mu)
	if (evt.passes("rmujetsWCRtag_2016") ){
	  h->h2D("HF_tag_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==1) h->h2D("HF_tag_C_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==2) h->h2D("HF_tag_cc_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==3 || Wfilter==4) h->h2D("HF_tag_B_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	  if (Wfilter==5) h->h2D("HF_tag_lf_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 1,weight);
	};
      };
      // #
      //###############################

      //###############################
      // # fill negative charged lepton row
      // #
      if (!lep_charge_pos)  {
	// # pretag 2015 (el)
	if (evt.passes("rejetsWCR_2015")){
	  h->h2D("HF_pretag_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==1) h->h2D("HF_pretag_C_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==2) h->h2D("HF_pretag_cc_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==3 || Wfilter==4) h->h2D("HF_pretag_B_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==5) h->h2D("HF_pretag_lf_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	};
	// # pretag 2016 (el)
	if (evt.passes("rejetsWCR_2016")){
	  h->h2D("HF_pretag_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==1) h->h2D("HF_pretag_C_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==2) h->h2D("HF_pretag_cc_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==3 || Wfilter==4) h->h2D("HF_pretag_B_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==5) h->h2D("HF_pretag_lf_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	};
	// # tag 2015 (el)
	if (evt.passes("rejetsWCRtag_2015") ) {
	  h->h2D("HF_tag_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==1) h->h2D("HF_tag_C_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==2) h->h2D("HF_tag_cc_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==3 || Wfilter==4) h->h2D("HF_tag_B_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==5) h->h2D("HF_tag_lf_el_2015","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	};
	// # tag 2016 (el)
	if (evt.passes("rejetsWCRtag_2016") ) {
	  h->h2D("HF_tag_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==1) h->h2D("HF_tag_C_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==2) h->h2D("HF_tag_cc_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==3 || Wfilter==4) h->h2D("HF_tag_B_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==5) h->h2D("HF_tag_lf_el_2016","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	};
	// # pretag 2015 (mu)
	if (evt.passes("rmujetsWCR_2015") ){
	  h->h2D("HF_pretag_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==1) h->h2D("HF_pretag_C_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==2) h->h2D("HF_pretag_cc_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==3 || Wfilter==4) h->h2D("HF_pretag_B_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==5) h->h2D("HF_pretag_lf_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	};
	// # pretag 2016 (mu)
	if (evt.passes("rmujetsWCR_2016") ){
	  h->h2D("HF_pretag_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==1) h->h2D("HF_pretag_C_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==2) h->h2D("HF_pretag_cc_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==3 || Wfilter==4) h->h2D("HF_pretag_B_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==5) h->h2D("HF_pretag_lf_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	};
	// # tag 2015 (mu)
	if (evt.passes("rmujetsWCRtag_2015")){
	  h->h2D("HF_tag_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==1) h->h2D("HF_tag_C_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==2) h->h2D("HF_tag_cc_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==3 || Wfilter==4) h->h2D("HF_tag_B_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==5) h->h2D("HF_tag_lf_mu_2015","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	};
	// # tag 2016 (mu)
	if (evt.passes("rmujetsWCRtag_2016")){
	  h->h2D("HF_tag_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==1) h->h2D("HF_tag_C_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==2) h->h2D("HF_tag_cc_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==3 || Wfilter==4) h->h2D("HF_tag_B_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	  if (Wfilter==5) h->h2D("HF_tag_lf_mu_2016","",suffix)->Fill(filled_bins.at(i_jet), 2,weight);
	};
      }; // lep charge neg

      // ##########################
      // ## Ratio only in separate histograms:
      // inside loop over jetbins
      // => pretag 2015
      if (evt.passes("rejetsWCR_2015") || evt.passes("rmujetsWCR_2015") ){
	if (lep_charge_pos){
	  h->h1D("Wplus_jetmultiplicity_pretag_2015","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==1) h->h1D("Wplus_jetmultiplicity_pretag_C_2015","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==2) h->h1D("Wplus_jetmultiplicity_pretag_cc_2015","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==3 || Wfilter==4) h->h1D("Wplus_jetmultiplicity_pretag_B_2015","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==5) h->h1D("Wplus_jetmultiplicity_pretag_lf_2015","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	};
	if (!lep_charge_pos){
	  h->h1D("Wmin_jetmultiplicity_pretag_2015","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==1) h->h1D("Wmin_jetmultiplicity_pretag_C_2015","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==2) h->h1D("Wmin_jetmultiplicity_pretag_cc_2015","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==3 || Wfilter==4) h->h1D("Wmin_jetmultiplicity_pretag_B_2015","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==5) h->h1D("Wmin_jetmultiplicity_pretag_lf_2015","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	};
      }; // if pretag 2015
      // => pretag 2016
      if (evt.passes("rejetsWCR_2016") || evt.passes("rmujetsWCR_2016") ){
	if (lep_charge_pos){
	  h->h1D("Wplus_jetmultiplicity_pretag_2016","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==1) h->h1D("Wplus_jetmultiplicity_pretag_C_2016","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==2) h->h1D("Wplus_jetmultiplicity_pretag_cc_2016","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==3 || Wfilter==4) h->h1D("Wplus_jetmultiplicity_pretag_B_2016","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==5) h->h1D("Wplus_jetmultiplicity_pretag_lf_2016","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	};
	if (!lep_charge_pos){
	  h->h1D("Wmin_jetmultiplicity_pretag_2016","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==1) h->h1D("Wmin_jetmultiplicity_pretag_C_2016","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==2) h->h1D("Wmin_jetmultiplicity_pretag_cc_2016","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==3 || Wfilter==4) h->h1D("Wmin_jetmultiplicity_pretag_B_2016","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==5) h->h1D("Wmin_jetmultiplicity_pretag_lf_2016","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	};
      }; // if pretag 2016
      // => tag 2015
      if (evt.passes("rejetsWCRtag_2015") || evt.passes("rmujetsWCRtag_2015") ){
	if (lep_charge_pos){
	  h->h1D("Wplus_jetmultiplicity_tag_2015","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==1) h->h1D("Wplus_jetmultiplicity_tag_C_2015","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==2) h->h1D("Wplus_jetmultiplicity_tag_cc_2015","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==3 || Wfilter==4) h->h1D("Wplus_jetmultiplicity_tag_B_2015","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==5) h->h1D("Wplus_jetmultiplicity_tag_lf_2015","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	};
	if (!lep_charge_pos){
	  h->h1D("Wmin_jetmultiplicity_tag_2015","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==1) h->h1D("Wmin_jetmultiplicity_tag_C_2015","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==2) h->h1D("Wmin_jetmultiplicity_tag_cc_2015","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==3 || Wfilter==4) h->h1D("Wmin_jetmultiplicity_tag_B_2015","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==5) h->h1D("Wmin_jetmultiplicity_tag_lf_2015","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	};
      }; // if tag 2015
      // => tag 2016
      if (evt.passes("rejetsWCRtag_2016") || evt.passes("rmujetsWCRtag_2016") ){
	if (lep_charge_pos){
	  h->h1D("Wplus_jetmultiplicity_tag_2016","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==1) h->h1D("Wplus_jetmultiplicity_tag_C_2016","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==2) h->h1D("Wplus_jetmultiplicity_tag_cc_2016","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==3 || Wfilter==4) h->h1D("Wplus_jetmultiplicity_tag_B_2016","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==5) h->h1D("Wplus_jetmultiplicity_tag_lf_2016","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	};
	if (!lep_charge_pos){
	  h->h1D("Wmin_jetmultiplicity_tag_2016","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==1) h->h1D("Wmin_jetmultiplicity_tag_C_2016","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==2) h->h1D("Wmin_jetmultiplicity_tag_cc_2016","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==3 || Wfilter==4) h->h1D("Wmin_jetmultiplicity_tag_B_2016","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	  if (Wfilter==5) h->h1D("Wmin_jetmultiplicity_tag_lf_2016","",suffix)->Fill(filled_bins.at(i_jet)-1,weight);
	};
      }; // if tag 2016




      // ##
      // ##########################
    }; // for loop
  }; // !boosted (rxWCR= all resolved)
  
  // #######################
  // # Define globally needed variables:
  float MET_var=evt.met().Perp()*1e-3;
  float MWT_var = sqrt(2. * l.Perp() * evt.met().Perp() * (1. - cos(l.Phi() - evt.met().Phi())))*1e-3;

  if (!m_boosted){
    // in all resolved
    // #######################
    // # fill pretag /tag histograms depending on jet multiplicity here
    if (debug) std::cout<<" Fill jet multiplicity dependent histograms"<<std::endl;
    if (Njets>1) {
      // 2in pretag 2015 (el)
      if ( evt.passes("rejetsWCR_2015") || evt.passes("rmujetsWCR_2015") ){
	h->h1D("lepPt_2in_pre_2015", "", suffix)->Fill(l.Perp()*1e-3, weight);
	h->h1D("lepEta_2in_pre_2015", "", suffix)->Fill(l.Eta(), weight);
	h->h1D("lepPhi_2in_pre_2015", "", suffix)->Fill(l.Phi(), weight);
	h->h1D("lepCharge_2in_pre_2015", "", suffix)->Fill(lep_charge, weight);
	h->h1D("leadJetPt_2in_pre_2015", "", suffix)->Fill(j.Perp()*1e-3, weight);
	h->h1D("nJets_2in_pre_2015", "", suffix)->Fill(Njets, weight);
	h->h1D("leadTrkbJetPt_2in_pre_2015", "", suffix)->Fill(lead_bjet_pt, weight);
	h->h1D("nTrkBtagJets_2in_pre_2015", "", suffix)->Fill(nTrkBtagged, weight);
	h->h1D("npv_2in_pre_2015", "", suffix)->Fill(evt.npv(), weight);
	h->h1D("MET_2in_pre_2015", "", suffix)->Fill(MET_var, weight);
	h->h1D("MWT_2in_pre_2015", "", suffix)->Fill(MWT_var,weight);
	h->h1D("METpMWT_2in_pre_2015", "", suffix)->Fill(MWT_var+MET_var,weight);
      };
      // 2in pretag 2016 (el)
      if (evt.passes("rejetsWCR_2016") || evt.passes("rmujetsWCR_2016")){
	h->h1D("lepPt_2in_pre_2016", "", suffix)->Fill(l.Perp()*1e-3, weight);
	h->h1D("lepEta_2in_pre_2016", "", suffix)->Fill(l.Eta(), weight);
	h->h1D("lepPhi_2in_pre_2016", "", suffix)->Fill(l.Phi(), weight);
	h->h1D("lepCharge_2in_pre_2016", "", suffix)->Fill(lep_charge, weight);
	h->h1D("leadJetPt_2in_pre_2016", "", suffix)->Fill(j.Perp()*1e-3, weight);
	h->h1D("nJets_2in_pre_2016", "", suffix)->Fill(Njets, weight);
	h->h1D("leadTrkbJetPt_2in_pre_2016", "", suffix)->Fill(lead_bjet_pt, weight);
	h->h1D("nTrkBtagJets_2in_pre_2016", "", suffix)->Fill(nTrkBtagged, weight);
	h->h1D("npv_2in_pre_2016", "", suffix)->Fill(evt.npv(), weight);
	h->h1D("MET_2in_pre_2016", "", suffix)->Fill(MET_var, weight);
	h->h1D("MWT_2in_pre_2016", "", suffix)->Fill(MWT_var,weight);
	h->h1D("METpMWT_2in_pre_2016", "", suffix)->Fill(MWT_var+MET_var,weight);
      };
      // 2in tag 2015 (el)
      if (evt.passes("rejetsWCRtag_2015") || evt.passes("rmujetsWCRtag_2015")){
	h->h1D("lepPt_2in_tag_2015", "", suffix)->Fill(l.Perp()*1e-3, weight);
	h->h1D("lepEta_2in_tag_2015", "", suffix)->Fill(l.Eta(), weight);
	h->h1D("lepPhi_2in_tag_2015", "", suffix)->Fill(l.Phi(), weight);
	h->h1D("lepCharge_2in_tag_2015", "", suffix)->Fill(lep_charge, weight);
	h->h1D("leadJetPt_2in_tag_2015", "", suffix)->Fill(j.Perp()*1e-3, weight);
	h->h1D("nJets_2in_tag_2015", "", suffix)->Fill(Njets, weight);
	h->h1D("leadTrkbJetPt_2in_tag_2015", "", suffix)->Fill(lead_bjet_pt, weight);
	h->h1D("nTrkBtagJets_2in_tag_2015", "", suffix)->Fill(nTrkBtagged, weight);
	h->h1D("npv_2in_tag_2015", "", suffix)->Fill(evt.npv(), weight);
	h->h1D("MET_2in_tag_2015", "", suffix)->Fill(MET_var, weight);
	h->h1D("MWT_2in_tag_2015", "", suffix)->Fill(MWT_var,weight);
	h->h1D("METpMWT_2in_tag_2015", "", suffix)->Fill(MWT_var+MET_var,weight);
      };
      // 2in tag 2016 (el)
      if (evt.passes("rejetsWCRtag_2016") || evt.passes("rmujetsWCRtag_2016") ){
	h->h1D("lepPt_2in_tag_2016", "", suffix)->Fill(l.Perp()*1e-3, weight);
	h->h1D("lepEta_2in_tag_2016", "", suffix)->Fill(l.Eta(), weight);
	h->h1D("lepPhi_2in_tag_2016", "", suffix)->Fill(l.Phi(), weight);
	h->h1D("lepCharge_2in_tag_2016", "", suffix)->Fill(lep_charge, weight);
	h->h1D("leadJetPt_2in_tag_2016", "", suffix)->Fill(j.Perp()*1e-3, weight);
	h->h1D("nJets_2in_tag_2016", "", suffix)->Fill(Njets, weight);
	h->h1D("leadTrkbJetPt_2in_tag_2016", "", suffix)->Fill(lead_bjet_pt, weight);
	h->h1D("nTrkBtagJets_2in_tag_2016", "", suffix)->Fill(nTrkBtagged, weight);
	h->h1D("npv_2in_tag_2016", "", suffix)->Fill(evt.npv(), weight);
	h->h1D("MET_2in_tag_2016", "", suffix)->Fill(MET_var, weight);
	h->h1D("MWT_2in_tag_2016", "", suffix)->Fill(MWT_var,weight);
	h->h1D("METpMWT_2in_tag_2016", "", suffix)->Fill(MWT_var+MET_var,weight);
      };
    }; //Njets>1
    if (Njets==2) {
      // 2ex tag 2015 (el)
      if (evt.passes("rejetsWCRtag_2015") || evt.passes("rmujetsWCRtag_2015")){
	h->h1D("lepPt_2ex_tag_2015", "", suffix)->Fill(l.Perp()*1e-3, weight);
	h->h1D("lepEta_2ex_tag_2015", "", suffix)->Fill(l.Eta(), weight);
	h->h1D("lepPhi_2ex_tag_2015", "", suffix)->Fill(l.Phi(), weight);
	h->h1D("lepCharge_2ex_tag_2015", "", suffix)->Fill(lep_charge, weight);
	h->h1D("leadJetPt_2ex_tag_2015", "", suffix)->Fill(j.Perp()*1e-3, weight);
	h->h1D("nJets_2ex_tag_2015", "", suffix)->Fill(Njets, weight);
	h->h1D("leadTrkbJetPt_2ex_tag_2015", "", suffix)->Fill(lead_bjet_pt, weight);
	h->h1D("nTrkBtagJets_2ex_tag_2015", "", suffix)->Fill(nTrkBtagged, weight);
	h->h1D("npv_2ex_tag_2015", "", suffix)->Fill(evt.npv(), weight);
	h->h1D("MET_2ex_tag_2015", "", suffix)->Fill(MET_var, weight);
	h->h1D("MWT_2ex_tag_2015", "", suffix)->Fill(MWT_var,weight);
	h->h1D("METpMWT_2ex_tag_2015", "", suffix)->Fill(MWT_var+MET_var,weight);
      };
      // 2ex tag 2016 (el)
      if (evt.passes("rejetsWCRtag_2016") || evt.passes("rmujetsWCRtag_2016")){
	h->h1D("lepPt_2ex_tag_2016", "", suffix)->Fill(l.Perp()*1e-3, weight);
	h->h1D("lepEta_2ex_tag_2016", "", suffix)->Fill(l.Eta(), weight);
	h->h1D("lepPhi_2ex_tag_2016", "", suffix)->Fill(l.Phi(), weight);
	h->h1D("lepCharge_2ex_tag_2016", "", suffix)->Fill(lep_charge, weight);
	h->h1D("leadJetPt_2ex_tag_2016", "", suffix)->Fill(j.Perp()*1e-3, weight);
	h->h1D("nJets_2ex_tag_2016", "", suffix)->Fill(Njets, weight);
	h->h1D("leadTrkbJetPt_2ex_tag_2016", "", suffix)->Fill(lead_bjet_pt, weight);
	h->h1D("nTrkBtagJets_2ex_tag_2016", "", suffix)->Fill(nTrkBtagged, weight);
	h->h1D("npv_2ex_tag_2016", "", suffix)->Fill(evt.npv(), weight);
	h->h1D("MET_2ex_tag_2016", "", suffix)->Fill(MET_var, weight);
	h->h1D("MWT_2ex_tag_2016", "", suffix)->Fill(MWT_var,weight);
	h->h1D("METpMWT_2ex_tag_2016", "", suffix)->Fill(MWT_var+MET_var,weight);
      };
    }; //Njets==2
    if (Njets>3) {
      // 4in tag 2015 (el)
      if (evt.passes("rejetsWCRtag_2015") || evt.passes("rmujetsWCRtag_2015")){
	h->h1D("lepPt_4in_tag_2015", "", suffix)->Fill(l.Perp()*1e-3, weight);
	h->h1D("lepEta_4in_tag_2015", "", suffix)->Fill(l.Eta(), weight);
	h->h1D("lepPhi_4in_tag_2015", "", suffix)->Fill(l.Phi(), weight);
	h->h1D("lepCharge_4in_tag_2015", "", suffix)->Fill(lep_charge, weight);
	h->h1D("leadJetPt_4in_tag_2015", "", suffix)->Fill(j.Perp()*1e-3, weight);
	h->h1D("nJets_4in_tag_2015", "", suffix)->Fill(Njets, weight);
	h->h1D("leadTrkbJetPt_4in_tag_2015", "", suffix)->Fill(lead_bjet_pt, weight);
	h->h1D("nTrkBtagJets_4in_tag_2015", "", suffix)->Fill(nTrkBtagged, weight);
	h->h1D("npv_4in_tag_2015", "", suffix)->Fill(evt.npv(), weight);
	h->h1D("MET_4in_tag_2015", "", suffix)->Fill(MET_var, weight);
	h->h1D("MWT_4in_tag_2015", "", suffix)->Fill(MWT_var,weight);
	h->h1D("METpMWT_4in_tag_2015", "", suffix)->Fill(MWT_var+MET_var,weight);
      };
      // 4in tag 2016 (el)
      if (evt.passes("rejetsWCRtag_2016") || evt.passes("rmujetsWCRtag_2016")){
	h->h1D("lepPt_4in_tag_2016", "", suffix)->Fill(l.Perp()*1e-3, weight);
	h->h1D("lepEta_4in_tag_2016", "", suffix)->Fill(l.Eta(), weight);
	h->h1D("lepPhi_4in_tag_2016", "", suffix)->Fill(l.Phi(), weight);
	h->h1D("lepCharge_4in_tag_2016", "", suffix)->Fill(lep_charge, weight);
	h->h1D("leadJetPt_4in_tag_2016", "", suffix)->Fill(j.Perp()*1e-3, weight);
	h->h1D("nJets_4in_tag_2016", "", suffix)->Fill(Njets, weight);
	h->h1D("leadTrkbJetPt_4in_tag_2016", "", suffix)->Fill(lead_bjet_pt, weight);
	h->h1D("nTrkBtagJets_4in_tag_2016", "", suffix)->Fill(nTrkBtagged, weight);
	h->h1D("npv_4in_tag_2016", "", suffix)->Fill(evt.npv(), weight);
	h->h1D("MET_4in_tag_2016", "", suffix)->Fill(MET_var, weight);
	h->h1D("MWT_4in_tag_2016", "", suffix)->Fill(MWT_var,weight);
	h->h1D("METpMWT_4in_tag_2016", "", suffix)->Fill(MWT_var+MET_var,weight);
      };
    }; //Njets>3
    // # 
    // #######################
  }; // !boosted (rxWCR= all resolved)

  // here: All (resolved+boosted)

  float mtt = -1;

  if (!m_boosted && is_4j_signal && is_btag_signal){
    // resolved signal without chi2:


    // #######################
    // # matching
    // outputs, they will be filled by the TTBarLeptonJetsBuilder_chi2
    int  igj3, igj4; // index for the Whad
    int igb3, igb4; // index for the b's
    int  ign1;  // index for the neutrino (because chi2 can test both pz solution)
    double chi2ming1, chi2ming1H, chi2ming1L;
    for(double idr=20.0; idr<=50.0; idr++)
      {
	TLorentzVector bl = evt.MC_bl();
	TLorentzVector bh = evt.MC_bh();
	double N_BMatch(0.), N_BMatch_BTag(0.), N_nBMatch(0.), N_nBMatch_BTag(0.);
	for (size_t z = 0; z < evt.jet().size(); ++z)
	  {
	    TLorentzVector tmpAk4Jet = evt.jet()[z].mom();
	    bool is_bmatch = tmpAk4Jet.DeltaR(bl) < 0.4 || tmpAk4Jet.DeltaR(bh) < 0.4;
	    bool is_btag(false);

	    for (size_t bidx = 0; bidx < evt.tjet().size(); ++bidx)
	      {
		TLorentzVector tmpTJet = evt.tjet()[bidx].mom();
		if(tmpAk4Jet.DeltaR(tmpTJet) < idr/100.) {
		  if(evt.tjet()[bidx].btag_mv2c10_70_trk() && evt.tjet()[bidx].pass_trk())
		    is_btag = true;
		} // if(tmpAk4Jet.DeltaR(tmpTJet) < idr/100.)
	      } // for (size_t bidx = 0; bidx < evt.tjet().size(); ++bidx)

	    //if(is_bmatch && is_btag) std::cout<<"btag found"<<std::endl;
	    if(is_bmatch) N_BMatch++;
	    if(!is_bmatch) N_nBMatch++;
	    if(is_bmatch && is_btag) N_BMatch_BTag++;
	    if(!is_bmatch && is_btag) N_nBMatch_BTag++;
	  } // for (size_t z = 0; z < evt.jet().size(); ++z)
	if(N_BMatch == 0 || N_nBMatch == 0) continue;
	double e_b = N_BMatch_BTag/N_BMatch;
	double e_bbar = N_nBMatch_BTag/N_nBMatch;

	//h->p1D("Profile_DelR", "", suffix)->Fill(idr/100., e_b*(1-e_bbar));
      } // or(double idr=20.0; idr<=50.0; idr++)

    // ###
    // #########################

    // #########################
    // ### calculate chi2 
    // prepare inputs
    // LEPTON --> TLorentzVector for your lepton
    // vjets -->  std::vector<TLorentzVector*> for the jets
    // vjets_btagged --> std::vector<bool> to say if the jets are btagged or not
    // met --> TLorentzVector for your MET

    std::vector<TLorentzVector *> vjets;
    std::vector<bool> vjets_btagged;
    for (size_t z = 0; z < evt.jet().size(); ++z) {
      vjets.push_back(new TLorentzVector(0,0,0,0));
      vjets[z]->SetPtEtaPhiE(evt.jet()[z].mom().Perp(), evt.jet()[z].mom().Eta(), evt.jet()[z].mom().Phi(), evt.jet()[z].mom().E());
      // https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/BTagingxAODEDM
      // https://twiki.cern.ch/twiki/bin/view/AtlasProtected/BTaggingBenchmarks
      //vjets_btagged.push_back(evt.jet()[z].btag_mv2c20_60());

      TLorentzVector tmpAk4Jet = evt.jet()[z].mom();
      bool is_btagged(false), is_bmatched(false);
      std::vector<bool> is_btagged_delR(31, false);

      TLorentzVector bl = evt.MC_bl();
      TLorentzVector bh = evt.MC_bh();

      if(tmpAk4Jet.DeltaR(bl) < 0.4 || tmpAk4Jet.DeltaR(bh) < 0.4)
	is_bmatched = true;

      for (size_t bidx = 0; bidx < evt.tjet().size(); ++bidx)
	{
	  TLorentzVector tmpTJet = evt.tjet()[bidx].mom();
	  // if(z==0 && bidx==0)
	  //   h->h1D("DeltaR_Leading", "", suffix)->Fill(tmpAk4Jet.DeltaR(tmpTJet));
	  //h->h1D("DeltaR_Inclusive", "", suffix)->Fill(tmpAk4Jet.DeltaR(tmpTJet));
	  if(tmpAk4Jet.DeltaR(tmpTJet) <= 0.4){
	    if (evt.tjet()[bidx].btag_mv2c10_70_trk() && evt.tjet()[bidx].pass_trk())
	      is_btagged = true;
	    //break;
	  }
	} // for (size_t bidx = 0; bidx < evt.tjet().size(); ++bidx)

	vjets_btagged.push_back(is_btagged);
      } // for size_t z

    if (debug)	std::cout<<" before calling findMinChiSquate : crash here"<<std::endl;
    TLorentzVector met = evt.met();
    bool status = m_chi2.findMinChiSquare(&l, &vjets, &vjets_btagged, &met, igj3, igj4, igb3, igb4, ign1, chi2ming1, chi2ming1H, chi2ming1L);
    // if (chi2ming1 <2){
    // 	std::cout<<" InputCheck:"<<std::endl;
    // 	std::cout<<" l pt: "<<l.Pt()<<", lead vjets pt: "<<vjets[0]->Perp()<<" lead btag tagged?: "<<vjets_btagged[0]<<",met: "<<met.Pt()<<std::endl;
    // 	for (int i=0; i<vjets.size();i++){
    // 	  std::cout<<" <jet "<<i<<" of "<<vjets.size()<<">  pt: "<<vjets[i]->Perp()<<"   btag?: "<<vjets_btagged[i]<<std::endl;
    // 	};
    // };
    //bool status=false;

    if (debug) std::cout<<" after findMinChiSquare"<<std::endl;
    float chi2Value = 1000000; // log10(1000000) = 6
    float mwh = -1;
    float mtl = -1;
    float mth = -1;

    if (status){
      chi2Value = chi2ming1;
      //if (chi2Value <2) std::cout<<" if status: Chi² value: "<<chi2Value<<std::endl;
      mwh = m_chi2.getResult_Mwh();
      mtl = m_chi2.getResult_Mtl();
      mth = m_chi2.getResult_Mth();
      mtt = m_chi2.getResult_Mtt();
    }
    chi2Value_global = chi2Value; 
    if (log10(chi2Value_global) < 0.9) is_chi2_signal=true;

    // reset inputs:
    for (size_t z = 0; z < vjets.size(); ++z) {
      delete vjets[z];
    }
    vjets.clear();
    vjets_btagged.clear();

    // Fill histograms
    if ((evt.passes("rejetsWCRtag_2015")||evt.passes("rmujetsWCRtag_2015")) && is_chi2_signal) {
      h->h1D("mtt_chi2_2015", "", suffix)->Fill(mtt*1e-3, weight);
      h->h1D("mtlep_chi2_2015", "", suffix)->Fill(mtl*1e-3, weight);
      h->h1D("mthad_chi2_2015", "", suffix)->Fill(mth*1e-3, weight);
      h->h1D("mwhad_chi2_2015", "", suffix)->Fill(mwh*1e-3, weight);
      h->h1D("chi2_2015", "", suffix)->Fill(log10(chi2Value), weight);
    };
    if ( (evt.passes("rejetsWCRtag_2016")||evt.passes("rmujetsWCRtag_2016"))  && is_chi2_signal) {
      h->h1D("mtt_chi2_2016", "", suffix)->Fill(mtt*1e-3, weight);
      h->h1D("mtlep_chi2_2016", "", suffix)->Fill(mtl*1e-3, weight);
      h->h1D("mthad_chi2_2016", "", suffix)->Fill(mth*1e-3, weight);
      h->h1D("mwhad_chi2_2016", "", suffix)->Fill(mwh*1e-3, weight);
      h->h1D("chi2_2016", "", suffix)->Fill(log10(chi2Value), weight);
    };

    // # end chi2
    // ########################


    // #########################
    // # using matched objects - only filled with ttbar, I suspect
    // #
    TLorentzVector a_w1h( evt.MA_w1h() ), a_w2h( evt.MA_w2h() ), a_bh( evt.MA_bh() );
    TLorentzVector a_w1l( evt.MA_w1l() ), a_w2l( evt.MA_w2l() ), a_bl( evt.MA_bl() );
    if ( (evt.passes("rmujetsWCRtag_2015") || evt.passes("rejetsWCRtag_2015")) && is_chi2_signal) {
      h->h1D("W_Hadronic_2015", "", suffix)->Fill((a_w1h + a_w2h).M()*1e-3);
      h->h1D("T_Hadronic_2015", "", suffix)->Fill((a_w1h + a_w2h + a_bh).M()*1e-3 - (a_w1h + a_w2h).M()*1e-3);
      h->h1D("T_Leptonic_2015", "", suffix)->Fill((a_w1l + a_w2l + a_bl).M()*1e-3);
      h->h1D("PT_Diff_2015", "", suffix)->Fill(((a_w1h+a_w2h+a_bh).Pt() - (a_w1l+a_w2l+a_bl).Pt() )*1e-3);
    };
    if ( (evt.passes("rmujetsWCRtag_2016") || evt.passes("rejetsWCRtag_2016")) && is_chi2_signal) {
      h->h1D("W_Hadronic_2016", "", suffix)->Fill((a_w1h + a_w2h).M()*1e-3);
      h->h1D("T_Hadronic_2016", "", suffix)->Fill((a_w1h + a_w2h + a_bh).M()*1e-3 - (a_w1h + a_w2h).M()*1e-3);
      h->h1D("T_Leptonic_2016", "", suffix)->Fill((a_w1l + a_w2l + a_bl).M()*1e-3);
      h->h1D("PT_Diff_2016", "", suffix)->Fill(((a_w1h+a_w2h+a_bh).Pt() - (a_w1l+a_w2l+a_bl).Pt() )*1e-3);
    };
    // # 
    // #######################
 
  }; // if resolved && is_4jets_signal && is_btag_signal

  // ###################
  // # deltaR between lepton and the closest narrow jet
  float closejl_deltaR  = 99;
  float deltaR_tmp      = 99;
  int closejl_idx       = -1;

  size_t jet_idx = 0;
  for (; jet_idx < evt.jet().size(); ++jet_idx){
    deltaR_tmp = 99;
    float dphi = l.DeltaPhi(evt.jet()[jet_idx].mom());
    float dy = l.Rapidity() - evt.jet()[jet_idx].mom().Rapidity();
    deltaR_tmp = std::sqrt(dy*dy + dphi*dphi);
    if (deltaR_tmp < closejl_deltaR){
      closejl_deltaR = deltaR_tmp;
      closejl_idx = jet_idx;
    }
  }//for
  if (debug) std::cout<<" deltaR between lepton and closes jet done"<<std::endl;

  float closejl_pt = -1;
  if (closejl_idx>0)    closejl_pt = evt.jet()[closejl_idx].mom().Perp();
  // ###
 // ###################


  // ###########################################################
  // #####                                                 #####
  // #####          SIGNAL resolved and boosted            #####
  // #####                                                 #####
  // ###########################################################

  // SIGNAL region boosted or resolved:
  if ((m_boosted && is_btag_signal) || (!m_boosted && (evt.passes("rmujetsWCRtag_2015") || evt.passes("rmujetsWCRtag_2016") || evt.passes("rejetsWCRtag_2015") || evt.passes("rejetsWCRtag_2016")) && is_4j_signal && is_btag_signal && is_chi2_signal)){
    // SIGNAL region boosted or resolved (WCRtag + 4jets + btag + chi2)

    bool is_2015 =false;
    bool is_2016 = false;
    if ( (m_boosted && (evt.passes("bejets_2015") || evt.passes("bmujets_2015"))) || (!m_boosted && ( evt.passes("rejetsWCRtag_2015") || evt.passes("rmujetsWCRtag_2015"))) ) is_2015 = true;
    if ( (m_boosted && (evt.passes("bejets_2016") || evt.passes("bmujets_2016"))) || (!m_boosted && ( evt.passes("rejetsWCRtag_2016") || evt.passes("rmujetsWCRtag_2016"))) ) is_2016 = true;

    float weight_input=weight;
    if (weight>10) weight_input = 9.9;
    if (weight<-10) weight_input = -9.9;

    // ### Jet kinematics
    std::vector<float> jetMass_vector;
    std::vector<float> jetPt_vector;
    std::vector<float> jetEta_vector;
    std::vector<float> jetPhi_vector;

    jetMass_vector.resize(evt.jet().size());
    jetPt_vector.resize(evt.jet().size());
    jetEta_vector.resize(evt.jet().size());
    jetPhi_vector.resize(evt.jet().size());

    size_t iJet = 0;
    for (; iJet < evt.jet().size(); ++iJet){
      const TLorentzVector &jet_p4 = evt.jet()[iJet].mom();
      jetMass_vector[iJet] =  evt.jet()[iJet].mom().M();
      jetPt_vector[iJet]   =  evt.jet()[iJet].mom().Pt();
      jetEta_vector[iJet]  =  evt.jet()[iJet].mom().Eta();
      jetPhi_vector[iJet]  =  evt.jet()[iJet].mom().Phi();
    }//for


    if (is_2015){
      h->h1D("leadTrkbJetPt_2015", "", suffix)->Fill(lead_bjet_pt, weight);
      h->h1D("leadJetPt_2015", "", suffix)->Fill(j.Perp()*1e-3, weight);
      h->h1D("nTrkBtagJets_2015", "", suffix)->Fill(nTrkBtagged, weight);
      h->h1D("nJets_2015", "", suffix)->Fill(Njets, weight);
      h->h1D("closejl_minDeltaR_2015", "", suffix)->Fill(closejl_deltaR, weight);
      h->h1D("closejl_pt_2015", "", suffix)->Fill(closejl_pt*1e-3, weight);

      h->h1D("mu_2015","", suffix)->Fill(evt.mu() , weight);
      //z prosition of primary vertex
      h->h1D("vtxz_2015", "", suffix)->Fill(evt.vtxz(), weight);
      h->h1D("npv_2015", "", suffix)->Fill(evt.npv(), weight);

      h->h1D("weight_2015", "", suffix)->Fill(weight_input); 
      h->h2D("weight_leptPt_2015", "", suffix)->Fill(l.Perp()*1e-3, weight_input); 

      h->h1D("MET_2015", "", suffix)->Fill(MET_var, weight);
      h->h1D("MET_phi_2015", "", suffix)->Fill(evt.met().Phi(), weight);
      h->h1D("MWT_2015", "", suffix)->Fill(MWT_var,weight);
      h->h1D("METpMWT_2015", "", suffix)->Fill(MWT_var+MET_var,weight);

      h->h1D("lepPt_2015", "", suffix)->Fill(l.Perp()*1e-3, weight);
      h->h1D("lepEta_2015", "", suffix)->Fill(l.Eta(), weight);
      h->h1D("lepPhi_2015", "", suffix)->Fill(l.Phi(), weight);
      h->h1D("lepCharge_2015", "", suffix)->Fill(lep_charge, weight);

      int maxNjet = (evt.jet().size()<6) ? evt.jet().size() : 6;
      for (int i = 0; i < maxNjet; ++i){

	std::string nameJet_m = "jet" + std::to_string(i)+"_m_2015";
	h->h1D(nameJet_m, "", suffix)->Fill(jetMass_vector[i]*1e-3, weight);

	std::string nameJet_pt = "jet" + std::to_string(i)+"_pt_2015";
	h->h1D(nameJet_pt, "", suffix)->Fill(jetPt_vector[i]*1e-3, weight);

	std::string nameJet_eta = "jet" + std::to_string(i)+"_eta_2015";
	h->h1D(nameJet_eta, "", suffix)->Fill(jetEta_vector[i], weight);

	std::string nameJet_phi = "jet" + std::to_string(i)+"_phi_2015";
	h->h1D(nameJet_phi, "", suffix)->Fill(jetPhi_vector[i], weight);
      }//for
      if (m_electron){
	if (evt.Wfilter_Sherpa_nT()==1)   {
	  h->h1D("yields_el_Wc_2015", "", suffix)->Fill(-1, weight);
	  h->h1D("yields_el_Wc_2015", "", suffix)->Fill(evt.Btagcat(), weight);
	};
	if (evt.Wfilter_Sherpa_nT()==2)  {
	  h->h1D("yields_el_Wcc_2015", "", suffix)->Fill(-1, weight);
	  h->h1D("yields_el_Wcc_2015", "", suffix)->Fill(evt.Btagcat(), weight);
	};
	if (evt.Wfilter_Sherpa_nT()==3 || evt.Wfilter_Sherpa_nT()==4 )   {
	  h->h1D("yields_el_Wbb_2015", "", suffix)->Fill(-1, weight);
	  h->h1D("yields_el_Wbb_2015", "", suffix)->Fill(evt.Btagcat(), weight);
	};
	if (evt.Wfilter_Sherpa_nT()==5)   {
	  h->h1D("yields_el_Wlf_2015", "", suffix)->Fill(-1, weight);
	  h->h1D("yields_el_Wlf_2015", "", suffix)->Fill(evt.Btagcat(), weight);
	};
      };
      if (!m_electron){
	if (evt.Wfilter_Sherpa_nT()==1)  {
	  h->h1D("yields_mu_Wc_2015", "", suffix)->Fill(-1, weight);
	  h->h1D("yields_mu_Wc_2015", "", suffix)->Fill(evt.Btagcat(), weight);
	};
	if (evt.Wfilter_Sherpa_nT()==2)   {
	  h->h1D("yields_mu_Wcc_2015", "", suffix)->Fill(-1, weight);
	  h->h1D("yields_mu_Wcc_2015", "", suffix)->Fill(evt.Btagcat(), weight);
	};	
	if (evt.Wfilter_Sherpa_nT()==3 || evt.Wfilter_Sherpa_nT()==4 )  {
	  h->h1D("yields_mu_Wbb_2015", "", suffix)->Fill(-1, weight);
	  h->h1D("yields_mu_Wbb_2015", "", suffix)->Fill(evt.Btagcat(), weight);
	};
	if (evt.Wfilter_Sherpa_nT()==5)   {
	  h->h1D("yields_mu_Wlf_2015", "", suffix)->Fill(-1, weight);
	  h->h1D("yields_mu_Wlf_2015", "", suffix)->Fill(evt.Btagcat(), weight);
	};
      };

      h->h1D("trueMtt_2015", "", suffix)->Fill(evt.MC_ttbar_beforeFSR().M()*1e-3, weight);
    }; // is 2015
    if (is_2016){
      h->h1D("leadTrkbJetPt_2016", "", suffix)->Fill(lead_bjet_pt, weight);
      h->h1D("leadJetPt_2016", "", suffix)->Fill(j.Perp()*1e-3, weight);
      h->h1D("nTrkBtagJets_2016", "", suffix)->Fill(nTrkBtagged, weight);
      h->h1D("nJets_2016", "", suffix)->Fill(Njets, weight);
      h->h1D("closejl_minDeltaR_2016", "", suffix)->Fill(closejl_deltaR, weight);
      h->h1D("closejl_pt_2016", "", suffix)->Fill(closejl_pt*1e-3, weight);

      h->h1D("mu_2016","", suffix)->Fill(evt.mu() , weight);
      //z prosition of primary vertex
      h->h1D("vtxz_2016", "", suffix)->Fill(evt.vtxz(), weight);
      h->h1D("npv_2016", "", suffix)->Fill(evt.npv(), weight);

      h->h1D("weight_2016", "", suffix)->Fill(weight_input); 
      h->h2D("weight_leptPt_2016", "", suffix)->Fill(l.Perp()*1e-3, weight_input); 

      h->h1D("MET_2016", "", suffix)->Fill(MET_var, weight);
      h->h1D("MET_phi_2016", "", suffix)->Fill(evt.met().Phi(), weight);
      h->h1D("MWT_2016", "", suffix)->Fill(MWT_var,weight);
      h->h1D("METpMWT_2016", "", suffix)->Fill(MWT_var+MET_var,weight);

      h->h1D("lepPt_2016", "", suffix)->Fill(l.Perp()*1e-3, weight);
      h->h1D("lepEta_2016", "", suffix)->Fill(l.Eta(), weight);
      h->h1D("lepPhi_2016", "", suffix)->Fill(l.Phi(), weight);
      h->h1D("lepCharge_2016", "", suffix)->Fill(lep_charge, weight);

      int maxNjet = (evt.jet().size()<6) ? evt.jet().size() : 6;
      for (int i = 0; i < maxNjet; ++i){

	std::string nameJet_m = "jet" + std::to_string(i)+"_m_2016";
	h->h1D(nameJet_m, "", suffix)->Fill(jetMass_vector[i]*1e-3, weight);

	std::string nameJet_pt = "jet" + std::to_string(i)+"_pt_2016";
	h->h1D(nameJet_pt, "", suffix)->Fill(jetPt_vector[i]*1e-3, weight);

	std::string nameJet_eta = "jet" + std::to_string(i)+"_eta_2016";
	h->h1D(nameJet_eta, "", suffix)->Fill(jetEta_vector[i], weight);

	std::string nameJet_phi = "jet" + std::to_string(i)+"_phi_2016";
	h->h1D(nameJet_phi, "", suffix)->Fill(jetPhi_vector[i], weight);
      }//for
      if (m_electron){
	if (evt.Wfilter_Sherpa_nT()==1)   {
	  h->h1D("yields_el_Wc_2016", "", suffix)->Fill(-1, weight);
	  h->h1D("yields_el_Wc_2016", "", suffix)->Fill(evt.Btagcat(), weight);
	};
	if (evt.Wfilter_Sherpa_nT()==2)  {
	  h->h1D("yields_el_Wcc_2016", "", suffix)->Fill(-1, weight);
	  h->h1D("yields_el_Wcc_2016", "", suffix)->Fill(evt.Btagcat(), weight);
	};
	if (evt.Wfilter_Sherpa_nT()==3 || evt.Wfilter_Sherpa_nT()==4 )   {
	  h->h1D("yields_el_Wbb_2016", "", suffix)->Fill(-1, weight);
	  h->h1D("yields_el_Wbb_2016", "", suffix)->Fill(evt.Btagcat(), weight);
	};
	if (evt.Wfilter_Sherpa_nT()==5)   {
	  h->h1D("yields_el_Wlf_2016", "", suffix)->Fill(-1, weight);
	  h->h1D("yields_el_Wlf_2016", "", suffix)->Fill(evt.Btagcat(), weight);
	};
      };
      if (!m_electron){
	if (evt.Wfilter_Sherpa_nT()==1)   {
	  h->h1D("yields_mu_Wc_2016", "", suffix)->Fill(-1, weight);
	  h->h1D("yields_mu_Wc_2016", "", suffix)->Fill(evt.Btagcat(), weight);
	};
	if (evt.Wfilter_Sherpa_nT()==2)   {
	  h->h1D("yields_mu_Wcc_2016", "", suffix)->Fill(-1, weight);
	  h->h1D("yields_mu_Wcc_2016", "", suffix)->Fill(evt.Btagcat(), weight);
	};
	if (evt.Wfilter_Sherpa_nT()==3 || evt.Wfilter_Sherpa_nT()==4 )   {
	  h->h1D("yields_mu_Wbb_2016", "", suffix)->Fill(-1, weight);
	  h->h1D("yields_mu_Wbb_2016", "", suffix)->Fill(evt.Btagcat(), weight);
	};
	if (evt.Wfilter_Sherpa_nT()==5)  {
	  h->h1D("yields_mu_Wlf_2016", "", suffix)->Fill(-1, weight);
	  h->h1D("yields_mu_Wlf_2016", "", suffix)->Fill(evt.Btagcat(), weight);
	};
      }; // if m_electron
      h->h1D("trueMtt_2016", "", suffix)->Fill(evt.MC_ttbar_beforeFSR().M()*1e-3, weight);
    }; // is 2016


    _tree_truemtt = evt.MC_ttbar_beforeFSR().M()*1e-3;

    if (m_boosted && is_btag_signal){
      // boosted signal

      // ################
      // # reconstruct ttbar system:
      size_t close_idx = 0;
      for (; close_idx < evt.jet().size(); ++close_idx)
	if (evt.jet()[close_idx].closeToLepton())
	  break;
      const TLorentzVector &sj = evt.jet()[close_idx].mom();
     

      // recheck angular cuts:
      size_t goodljet_idx = 0;
      int pos0=-1;
      int pos_angular=-1;
      for (; goodljet_idx < evt.largeJet().size(); ++goodljet_idx) {
      	TLorentzVector ljet_help=evt.largeJet()[goodljet_idx].mom();
      	//std::cout << "jet " << goodljet_idx << " pt = " << evt.largeJet()[goodljet_idx].mom().Perp() << ", good = " << evt.largeJet()[goodljet_idx].good() << std::endl;
      	if (evt.largeJet()[goodljet_idx].good()){
      	  if (pos0<0) pos0=goodljet_idx;
      	  // NEW: check angular cuts:
      	  if ( ljet_help.DeltaR(sj)>1.5 && fabs( ljet_help.DeltaPhi(l))>2.3){
      	    //std::cout<<" NEW: really good large jet found at index "<<goodljet_idx<<std::endl;
      	    pos_angular=goodljet_idx;
      	    break;
      	  };// if passed angular cuts
      	}; // if good = top tagged
      }; // loop large Jets
      if (pos_angular!=pos0 ) std::cout<<" new large jet found: here "<<pos_angular<<" instead of here "<<pos0<<std::endl;
      //// |------------
      // TEST: don't use recheck for angular cut:
      //if (pos_angular!=pos0 ) std::cout<<" new large jet would have been found: here "<<pos_angular<<" instead of here "<<pos0<<std::endl;
      // reset goodljet_idx to pos0: 
      //goodljet_idx= pos0; // with additional checK. goodljet_idx=pos_angular
      // ----|
      const TLorentzVector &lj = evt.largeJet()[goodljet_idx].mom();


      if (debug) 	std::cout<<" recalc mtt"<<std::endl;
      // recalc. mtt
      // lepton = l
      // large-R jet = hadronic top = lj
      // selected jet = leptonic top's b-jet = sj
      // neutrino px, py = met
      std::vector<TLorentzVector*> vec_nu = m_neutrinoBuilder.candidatesFromWMass_Rotation(&l, evt.met().Perp(), evt.met().Phi(), true);
      TLorentzVector nu(0,0,0,0);
      if (vec_nu.size() > 0) {
	nu = *(vec_nu[0]);
	for (size_t z = 0; z < vec_nu.size(); ++z) delete vec_nu[z];
	vec_nu.clear();
      }
      if (evt.largeJet().size()!=0)    mtt = (lj+sj+nu+l).M();
      // #
      // ################

      // ###############
      // # top charge asymmetry calculations

      if (debug) std::cout<<" Calculate Delta Eta lepton <-> fat jet"<<std::endl;
      float DeltaEta_boost  = 42;
      if (lep_charge_pos)  DeltaEta_boost  = fabs(lep_ETA)- fabs(lj.Eta());
      if (!lep_charge_pos) DeltaEta_boost  = fabs(lj.Eta())-fabs(lep_ETA);
      if (debug) std::cout<<" Result Delta Eta lepton <-> fat jet: "<<DeltaEta_boost<<std::endl;

      if (debug) std::cout<<" Calculate Delta Y lepton <-> fat jet"<<std::endl;
      float DeltaY_boost = 42;
      if (lep_charge_pos)  DeltaY_boost = fabs(lep_Y)-fabs(lj.Rapidity());
      if (!lep_charge_pos) DeltaY_boost = fabs(lj.Rapidity())-fabs(lep_Y);
      if (debug) std::cout<<" Result Delta Y lepton <-> fat jet: "<<DeltaY_boost<<std::endl;

      float lepTop_Eta = (sj+nu+l).Eta();
      float lepTop_Y = (sj+nu+l).Rapidity();
      float hadTop_Y = lj.Rapidity();
      float hadTop_Eta = lj.Eta();
      if (debug) std::cout<<" Calculated Eta of leptonic top: "<<lepTop_Eta<<"   and Y: "<<lepTop_Y<<std::endl;

      float DeltaEta_boost_rec = 42;
      if (lep_charge_pos)  DeltaEta_boost_rec = fabs(lepTop_Eta)- fabs(hadTop_Eta);
      if (!lep_charge_pos) DeltaEta_boost_rec = fabs(hadTop_Eta)-fabs(lepTop_Eta);

      if (debug) std::cout<<" Calculated Delta |Eta| of reconstructed lep top and had top (fatjet) :"<<DeltaEta_boost_rec<<std::endl;
 
      float DeltaY_boost_rec = 42;
      if (lep_charge_pos)  DeltaY_boost_rec =fabs(lepTop_Y)-fabs(hadTop_Y);
      if (!lep_charge_pos) DeltaY_boost_rec =fabs(hadTop_Y)-fabs(lepTop_Y);
      if (debug) std::cout<<" Calculated Delta |Y| of reconstructed lep top and had top (fatjet) :"<<DeltaY_boost_rec<<std::endl;

      // ==> comment out: Use Data , too => might crash!
      // // use truth top and anti-top
      TLorentzVector truth_top= evt.MC_t();
      TLorentzVector truth_tbar = evt.MC_tbar();
      if (debug){
	std::cout<<" Phi of true top: "<<truth_top.Phi()<<std::endl;
	std::cout<<" Y of true top: "<<truth_top.Rapidity()<<std::endl;
	std::cout<<" Eta of true top: "<<truth_top.Eta()<<std::endl;
	std::cout<<" m of true top: "<<truth_top.M()<<std::endl;
      };
      float DeltaY_boost_truth = 0;
      DeltaY_boost_truth = fabs(truth_top.Rapidity())-fabs(truth_tbar.Rapidity());
      // #
      // ######################

      // ######################
      // # histograms:
      if (is_2015){
	if (m_electron){
	  h->h1D("yields_boost_el_2015","",suffix)->Fill(-1,weight);
	  h->h1D("yields_boost_el_2015","",suffix)->Fill(evt.Btagcat(),weight);
	  h->h1D("yields_boost_el_nw_2015","",suffix)->Fill(-1);
	  h->h1D("yields_boost_el_nw_2015","",suffix)->Fill(evt.Btagcat());
	};
	if (!m_electron){
	  h->h1D("yields_boost_mu_2015","",suffix)->Fill(-1,weight);
	  h->h1D("yields_boost_mu_2015","",suffix)->Fill(evt.Btagcat(),weight);
	  h->h1D("yields_boost_mu_nw_2015","",suffix)->Fill(-1);
	  h->h1D("yields_boost_mu_nw_2015","",suffix)->Fill(evt.Btagcat());
	};

	h->h1D("mtt_2015", "", suffix)->Fill(mtt*1e-3, weight);

	h->h1D("largeJetPt_2015", "", suffix)->Fill(lj.Perp()*1e-3, weight);
	h->h1D("largeJetM_2015", "", suffix)->Fill(lj.M()*1e-3, weight);
	h->h1D("largeJetEta_2015", "", suffix)->Fill(lj.Eta(), weight);
	h->h1D("largeJetPhi_2015", "", suffix)->Fill(lj.Phi(), weight);
	h->h1D("largeJetSd12_2015", "", suffix)->Fill(evt.largeJet()[goodljet_idx].split12()*1e-3, weight); // necessary *1e-3 ??? in MeV?
	h->h1D("largeJet_tau32_2015", "", suffix)->Fill(evt.largeJet()[goodljet_idx].subs("tau32"), weight);
	h->h1D("largeJet_tau32_wta_2015", "", suffix)->Fill(evt.largeJet()[goodljet_idx].subs("tau32_wta"), weight);
	h->h1D("largeJet_tau21_2015", "", suffix)->Fill(evt.largeJet()[goodljet_idx].subs("tau21"), weight);
	h->h1D("largeJet_tau21_wta_2015", "", suffix)->Fill(evt.largeJet()[goodljet_idx].subs("tau21_wta"), weight);

	h->h1D("closeJetPt_boost_2015", "", suffix)->Fill(sj.Perp()*1e-3, weight);

	h->h1D("DeltaY_lep_hadTop_2015","",suffix)->Fill(DeltaY_boost,weight);
	h->h1D("DeltaEta_lep_hadTop_2015","",suffix)->Fill(DeltaEta_boost,weight);

	h->h1D("DeltaY_Top_antiTop_2015","",suffix)->Fill(DeltaY_boost_rec,weight);
	h->h1D("DeltaY_Top_antiTop_range2_2015","",suffix)->Fill(DeltaY_boost_rec,weight);
	h->h1D("DeltaEta_Top_antiTop_2015","",suffix)->Fill(DeltaEta_boost_rec,weight);
	h->h1D("DeltaY_truth_Top_antiTop_2015","",suffix)->Fill(DeltaY_boost_truth, weight);
	h->h1D("DeltaDeltaY_truth_reco_Top_antiTop_2015","",suffix)->Fill(DeltaY_boost_truth-DeltaY_boost_rec,weight);
	// 1516 combined -> testing purpose
	h->h1D("DeltaY_truth_Top_antiTop_1516","",suffix)->Fill(DeltaY_boost_truth, weight);
 	h->h1D("DeltaY_Top_antiTop_1516","",suffix)->Fill(DeltaY_boost_rec, weight);
	h->h1D("DeltaY_Top_antiTop_1516_test","",suffix)->Fill(DeltaY_boost_rec, weight);
	h->h1D("DeltaDeltaY_truth_reco_Top_antiTop_1516","",suffix)->Fill(DeltaY_boost_truth-DeltaY_boost_rec,weight);


 
     }; //is_2015
      if (is_2016){
	if (m_electron){
	  h->h1D("yields_boost_el_2016","",suffix)->Fill(-1,weight);
	  h->h1D("yields_boost_el_2016","",suffix)->Fill(evt.Btagcat(),weight);
	  h->h1D("yields_boost_el_nw_2016","",suffix)->Fill(-1);
	  h->h1D("yields_boost_el_nw_2016","",suffix)->Fill(evt.Btagcat());
	};
	if (!m_electron){
	  h->h1D("yields_boost_mu_2016","",suffix)->Fill(-1,weight);
	  h->h1D("yields_boost_mu_2016","",suffix)->Fill(evt.Btagcat(),weight);
	  h->h1D("yields_boost_mu_nw_2016","",suffix)->Fill(-1);
	  h->h1D("yields_boost_mu_nw_2016","",suffix)->Fill(evt.Btagcat());
	};

	h->h1D("mtt_2016", "", suffix)->Fill(mtt*1e-3, weight);

	h->h1D("largeJetPt_2016", "", suffix)->Fill(lj.Perp()*1e-3, weight);
	h->h1D("largeJetM_2016", "", suffix)->Fill(lj.M()*1e-3, weight);
	h->h1D("largeJetEta_2016", "", suffix)->Fill(lj.Eta(), weight);
	h->h1D("largeJetPhi_2016", "", suffix)->Fill(lj.Phi(), weight);
	h->h1D("largeJetSd12_2016", "", suffix)->Fill(evt.largeJet()[goodljet_idx].split12()*1e-3, weight); // necessary *1e-3 ??? in MeV?
	h->h1D("largeJet_tau32_2016", "", suffix)->Fill(evt.largeJet()[goodljet_idx].subs("tau32"), weight);
	h->h1D("largeJet_tau32_wta_2016", "", suffix)->Fill(evt.largeJet()[goodljet_idx].subs("tau32_wta"), weight);
	h->h1D("largeJet_tau21_2016", "", suffix)->Fill(evt.largeJet()[goodljet_idx].subs("tau21"), weight);
	h->h1D("largeJet_tau21_wta_2016", "", suffix)->Fill(evt.largeJet()[goodljet_idx].subs("tau21_wta"), weight);

	h->h1D("closeJetPt_boost_2016", "", suffix)->Fill(sj.Perp()*1e-3, weight);

	h->h1D("DeltaY_lep_hadTop_2016","",suffix)->Fill(DeltaY_boost,weight);
	h->h1D("DeltaEta_lep_hadTop_2016","",suffix)->Fill(DeltaEta_boost,weight);
	h->h1D("DeltaY_Top_antiTop_2016","",suffix)->Fill(DeltaY_boost_rec,weight);
	h->h1D("DeltaY_Top_antiTop_range2_2016","",suffix)->Fill(DeltaY_boost_rec,weight);
	h->h1D("DeltaEta_Top_antiTop_2016","",suffix)->Fill(DeltaEta_boost_rec,weight);
	h->h1D("DeltaY_truth_Top_antiTop_2016","",suffix)->Fill(DeltaY_boost_truth, weight);
	h->h1D("DeltaDeltaY_truth_reco_Top_antiTop_2016","",suffix)->Fill(DeltaY_boost_truth-DeltaY_boost_rec,weight);
	// 1516 combined -> testing purpose
   	h->h1D("DeltaY_truth_Top_antiTop_1516","",suffix)->Fill(DeltaY_boost_truth, weight);
  	h->h1D("DeltaY_Top_antiTop_1516","",suffix)->Fill(DeltaY_boost_rec, weight);
  	h->h1D("DeltaY_Top_antiTop_1516_test","",suffix)->Fill(DeltaY_boost_rec, weight);
	h->h1D("DeltaDeltaY_truth_reco_Top_antiTop_1516","",suffix)->Fill(DeltaY_boost_truth-DeltaY_boost_rec,weight);
      }; //is_2016

      _tree_mtt = mtt*1e-3;
      _tree_weight = weight;
      _tree_cat = -1;

      if ( (evt.passes("bejets_2015")  ||  evt.passes("bejets_2016"))  && m_boosted && m_electron) 	_tree_cat = 0;
      if ( (evt.passes("bmujets_2015") || evt.passes("bmujets_2016")) && m_boosted && !m_electron)        _tree_cat =  1;
      h->m_tree->Fill();

    }; // if boosted

    if (!m_boosted){
      //resolved signal = WCRtag + 4j +btag +chi2
      _tree_mtt = mtt*1e-3;
      _tree_weight = weight;
      _tree_cat = -1;

      if ((evt.passes("rejetsWCR_2015")   ||  evt.passes("rejetsWCR_2016")) && !m_boosted && m_electron   ) _tree_cat = 2;
      if ((evt.passes("rmujetsWCR_2015")  || evt.passes("rmujetsWCR_2016")) && !m_boosted && !m_electron  ) _tree_cat = 3;

      // #####################
      // ### fill yields 
      // --- resolved signal (= WCRTag + 4j + btag + chi2
      if (m_electron){
	if (is_2015) {
	  h->h1D("yields_res_el_2015", "", suffix)->Fill(-1, weight);
	  h->h1D("yields_res_el_2015", "", suffix)->Fill(evt.Btagcat(), weight);
	  h->h1D("yields_res_el_nw_2015", "", suffix)->Fill(-1);
	  h->h1D("yields_res_el_nw_2015", "", suffix)->Fill(evt.Btagcat());

	};
	if (is_2016) {
	  h->h1D("yields_res_el_2016", "", suffix)->Fill(-1, weight);
	  h->h1D("yields_res_el_2016", "", suffix)->Fill(evt.Btagcat(), weight);
	  h->h1D("yields_res_el_nw_2016", "", suffix)->Fill(-1);
	  h->h1D("yields_res_el_nw_2016", "", suffix)->Fill(evt.Btagcat());
	};
      };
      if (!m_electron){
	if (is_2015) h->h1D("yields_res_mu_2015", "", suffix)->Fill(-1, weight);
	if (is_2015) h->h1D("yields_res_mu_2015", "", suffix)->Fill(evt.Btagcat(), weight);
	if (is_2016) h->h1D("yields_res_mu_2016", "", suffix)->Fill(-1, weight);
	if (is_2016) h->h1D("yields_res_mu_2016", "", suffix)->Fill(evt.Btagcat(), weight);
      };
   
  
      h->m_tree->Fill();
      // #
      // #####################
      

    }; //resolved signal = WCRtag + 4j +btag +chi2

  }; // END signal region boost or resolved
 
  if (debug) std::cout<<" Run AnaMultijetAllIn1 is done for this Event"<<std::endl;
}
