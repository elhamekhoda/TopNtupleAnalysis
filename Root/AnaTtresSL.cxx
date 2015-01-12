/**
 * @brief Analysis class for tt resonances.
 * @author Danilo Enoque Ferreira de Lima <dferreir@cern.ch>
 */

#include "TopNtupleAnalysis/Analysis.h"
#include "TopNtupleAnalysis/AnaTtresSL.h"
#include "TopNtupleAnalysis/Event.h"
#include "TLorentzVector.h"
#include <vector>
#include <string>
#include "TopNtupleAnalysis/HistogramService.h"

AnaTtresSL::AnaTtresSL(const std::string &filename, bool electron, bool boosted)
  : Analysis(filename), m_electron(electron), m_boosted(boosted),
    m_neutrinoBuilder("MeV"), m_chi2("MeV") {

  m_chi2.Init(TtresChi2::DATA2012SUMMER2013);

  m_hSvc.create1D("lepPt", "; Lepton p_{T} ; Events", 30, 0, 300);
  m_hSvc.create1D("lepEta", "; Lepton #eta ; Events", 50, -2.5, 2.5);
  m_hSvc.create1D("lepPhi", "; Lepton #phi ; Events", 64, -3.2, 3.2);

  m_hSvc.create1D("leadJetPt", "; Leading Jet p_{T} ; Events", 50, 0, 500);
  m_hSvc.create1D("leadbJetPt", "; Leading b-jet p_{T} ; Events", 50, 0, 500);

  m_hSvc.create1D("met", "; Missing E_{T} ; Events", 50, 0, 500);
  m_hSvc.create1D("met_phi", "; Missing E_{T} #phi; Events", 64, -3.2, 3.2);

  if (m_boosted) {
    m_hSvc.create1D("closeJetPt", "; Selected Jet p_{T} ; Events", 25, 0, 500);

    m_hSvc.create1D("largeJetPt", "; Large jet p_{T} ; Events", 20, 300, 700);
    m_hSvc.create1D("largeJetM", "; Large jet M ; Events", 15, 0, 300);
    m_hSvc.create1D("largeJetSd12", "; Large jet #sqrt{d_{12}} ; Events", 30, 0, 300);

    m_hSvc.create1D("mtlep_boo", "; m_{t,lep} ; Events", 40, 0, 400);
  } else {
    m_hSvc.create1D("mtlep_res", "; m_{t,lep} ; Events", 40, 0, 400);
    m_hSvc.create1D("mthad_res", "; m_{t,had} ; Events", 40, 0, 400);
    m_hSvc.create1D("mwhad_res", "; m_{W,had} ; Events", 40, 0, 400);
    m_hSvc.create1D("chi2", "; #chi^{2} ; Events", 50, 0, 10);
  }

  m_hSvc.create1D("mtt", "; m_{t#bar{t}} ; Events", 60, 0, 6000);
}

AnaTtresSL::~AnaTtresSL() {
}

void AnaTtresSL::run(const Event &e, double weight) {
  std::string s = ""; // this would be the systematics ... could be sent as an argument in the future

  // check channel
  if (m_electron && (e.electron().size() != 1 || e.muon().size() != 0))
    return;

  if (!m_electron && (e.electron().size() != 0 || e.muon().size() != 1))
    return;

  if (m_boosted)
    if (!(e.passes("bejets") || e.passes("bmujets")))
      return;

  if (!m_boosted)
    if (!(e.passes("rejets") || e.passes("rmujets")))
      return;

  HistogramService *h = &m_hSvc;
  TLorentzVector l;
  if (m_electron) {
    l = e.electron()[0].mom();
  } else {
    l = e.muon()[0].mom();
  }
  h->h1D("lepPt", "", s)->Fill(l.Perp()*1e-3, weight);
  h->h1D("lepEta", "", s)->Fill(l.Eta(), weight);
  h->h1D("lepPhi", "", s)->Fill(l.Phi(), weight);

  h->h1D("met_phi", "", s)->Fill(e.met().Phi(), weight);

  const TLorentzVector &j = e.jet()[0].mom();
  h->h1D("leadJetPt", "", s)->Fill(j.Perp()*1e-3, weight);
  size_t bidx = 0;
  for (; bidx < e.jet().size(); ++bidx)
    if (e.jet()[bidx].btag())
      break;
  h->h1D("leadbJetPt", "", s)->Fill(e.jet()[bidx].mom().Perp()*1e-3, weight);

  float mtt = 0;

  h->h1D("met", "", s)->Fill(e.met().Perp()*1e-3, weight);

  if (m_boosted && (e.passes("bejets") || e.passes("bmujets"))) {

    size_t close_idx = 0;
    for (; close_idx < e.jet().size(); ++close_idx)
      if (e.jet()[close_idx].closeToLepton())
        break;
    const TLorentzVector &sj = e.jet()[close_idx].mom();
    h->h1D("closeJetPt", "", s)->Fill(sj.Perp()*1e-3, weight);

    size_t goodljet_idx = 0;
    for (; goodljet_idx < e.largeJet().size(); ++goodljet_idx)
      if (e.largeJet()[goodljet_idx].good())
        break;
    const TLorentzVector &lj = e.largeJet()[goodljet_idx].mom();
    h->h1D("largeJetPt", "", s)->Fill(lj.Perp()*1e-3, weight);
    h->h1D("largeJetM", "", s)->Fill(lj.M()*1e-3, weight);
    h->h1D("largeJetSd12", "", s)->Fill(e.largeJet()[goodljet_idx].split12()*1e-3, weight);

    // recalc. mtt
    // lepton = l
    // large-R jet = hadronic top = lj
    // selected jet = leptonic top's b-jet = sj
    // neutrino px, py = met
    std::vector<TLorentzVector*> vec_nu = m_neutrinoBuilder.candidatesFromWMass_Rotation(&l, e.met().Perp(), e.met().Phi(), true);   
    TLorentzVector nu(0,0,0,0);
    if (vec_nu.size() > 0) {
      nu = *(vec_nu[0]);
      for (size_t z = 0; z < vec_nu.size(); ++z) delete vec_nu[z];
      vec_nu.clear();
    }
    mtt = (lj+sj+nu+l).M();
    h->h1D("mtt", "", s)->Fill(mtt*1e-3, weight);
    h->h1D("mtlep_boo", "", s)->Fill((sj+nu+l).M()*1e-3, weight);
  }

  if (!m_boosted && (e.passes("rejets") || e.passes("rmujets"))) {

    // inputs 
    // LEPTON --> TLorentzVector for your lepton
    // vjets -->  std::vector<TLorentzVector*> for the jets
    // vjets_btagged --> std::vector<bool> to say if the jets are btagged or not
    // met --> TLorentzVector for your MET

    // outputs, they will be filled by the TTBarLeptonJetsBuilder_chi2
    int  igj3, igj4; // index for the Whad
    int igb3, igb4; // index for the b's
    int  ign1;  // index for the neutrino (because chi2 can test both pz solution)
    double chi2ming1, chi2ming1H, chi2ming1L;

    std::vector<TLorentzVector *> vjets;
    std::vector<bool> vjets_btagged;
    for (size_t z = 0; z < e.jet().size(); ++z) {
      vjets.push_back(new TLorentzVector(0,0,0,0));
      vjets[z]->SetPtEtaPhiE(e.jet()[z].mom().Perp(), e.jet()[z].mom().Eta(), e.jet()[z].mom().Phi(), e.jet()[z].mom().E());
      // https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/BTagingxAODEDM
      // https://twiki.cern.ch/twiki/bin/view/AtlasProtected/BTaggingBenchmarks
      vjets_btagged.push_back(e.jet()[z].btag());
    }
    TLorentzVector met = e.met();
    bool status = m_chi2.findMinChiSquare(&l, &vjets, &vjets_btagged, &met, igj3, igj4, igb3, igb4, ign1, chi2ming1, chi2ming1H, chi2ming1L); 
    // status has to be true

    if (status) mtt = m_chi2.getResult_Mtt();
    for (size_t z = 0; z < vjets.size(); ++z) {
      delete vjets[z];
    }
    vjets.clear();
    vjets_btagged.clear();
    h->h1D("mtt", "", s)->Fill(mtt*1e-3, weight);
    h->h1D("mtlep_res", "", s)->Fill(m_chi2.getResult_Mtl()*1e-3, weight);
    h->h1D("mthad_res", "", s)->Fill(m_chi2.getResult_Mth()*1e-3, weight);
    h->h1D("mwhad_res", "", s)->Fill(m_chi2.getResult_Mwh()*1e-3, weight);
    h->h1D("chi2", "", s)->Fill(chi2ming1, weight);
  }


}

