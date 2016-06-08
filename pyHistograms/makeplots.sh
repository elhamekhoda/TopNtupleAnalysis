
LUMI=1.79617

for ch in be bmu re rmu ; do
    ../../plotting/plot -c $ch -h yields -l $LUMI -C config.txt >yields_${ch}.txt
    ../../plotting/plot -c $ch -h lepPt --normBinWidth 20 -l $LUMI --rebin 4 --xTitle "Lepton p_{T} [GeV]" --yTitle "Events / 20 GeV" --stamp 0 -C config.txt
    ../../plotting/plot -c $ch -h lepEta  -l $LUMI  --xTitle "Lepton #eta" --yTitle "Events / 0.25" --stamp 0 -C config.txt
    ../../plotting/plot -c $ch -h nJets -l $LUMI --xTitle "Number of jets" --yTitle "Events" --stamp 0 -C config.txt
    ../../plotting/plot -c $ch -h nTrkBtagJets -l $LUMI --xTitle "Number of b-tagged track jets" --yTitle "Events" --stamp 0 -C config.txt
    ../../plotting/plot -c $ch -h MET --normBinWidth 20 -l $LUMI --yTitle "Events / 20 GeV" --xTitle "E_{T}^{miss} [GeV]" --stamp 0 -C config.txt
    ../../plotting/plot -c $ch -h MET_phi -l $LUMI --yTitle "Events / 0.2" --xTitle "E_{T}^{miss} #phi [rd]" --stamp 0 -C config.txt
    ../../plotting/plot -c $ch -h mwt -l $LUMI --yTitle "Events / 10 GeV" --xTitle "m_{WT} [GeV]" --stamp 0 -C config.txt
    ../../plotting/plot -c $ch -h closeJetPt -l $LUMI --normBinWidth 10 --yTitle "Events / 10 GeV" --xTitle "Selected jet p_{T} [GeV]" --stamp 0 -C config.txt
    ../../plotting/plot -c $ch -h largeJetPt -l $LUMI --normBinWidth 20 --yTitle "Events / 20 GeV" --xTitle "Large-R jet p_{T} [GeV]" --stamp 0 -C config.txt
    ../../plotting/plot -c $ch -h largeJetM -l $LUMI  --yTitle "Events / 10 GeV" --xTitle "Large-R jet mass [GeV]" --stamp 0 -C config.txt
    ../../plotting/plot -c $ch -h largeJetPtMtt -l $LUMI  --yTitle "Events / 0.02" --xTitle "Large-R jet p_{T} / m_{t#bar{t}} " --stamp 0 -C config.txt
    ../../plotting/plot -c $ch -h largeJetEta -l $LUMI  --yTitle "Events / 0.1" --xTitle "Large-R jet #eta" --stamp 0 -C config.txt
    ../../plotting/plot -c $ch -h largeJetPhi -l $LUMI  --yTitle "Events / 0.2" --xTitle "Large-R jet #phi [rd]" --stamp 0 -C config.txt
    ../../plotting/plot -c $ch -h mtlep_boo -l $LUMI --normBinWidth 20  --yTitle "Events / 20 GeV" --xTitle "Mass of the leptonic top [GeV]" --stamp 0 -C config.txt
    ../../plotting/plot -c $ch -h mtlep_res -l $LUMI --normBinWidth 20  --yTitle "Events / 20 GeV" --xTitle "Mass of the leptonic top [GeV]" --stamp 0 -C config.txt
    ../../plotting/plot -c $ch -h mthad_res -l $LUMI --normBinWidth 20  --yTitle "Events / 20 GeV" --xTitle "Mass of the hadronic top [GeV]" --stamp 0 -C config.txt
    ../../plotting/plot -c $ch -h mwhad_res -l $LUMI --normBinWidth 20  --yTitle "Events / 20 GeV" --xTitle "Mass of the hadronic W [GeV]" --stamp 0 -C config.txt
    ../../plotting/plot -c $ch -h chi2 -l $LUMI  --yTitle "Events / 0.2" --xTitle "log(#chi^{2})" --stamp 0 -C config.txt
    ../../plotting/plot -c $ch -h largeJet_tau32_wta -l $LUMI  --yTitle "Events / 0.05" --xTitle "Large-R jet #tau_{32} wta" --stamp 0 -C config.txt
    ../../plotting/plot -c $ch -h largeJet_tau21_wta -l $LUMI  --yTitle "Events / 0.05" --xTitle "Large-R jet #tau_{21} wta" --stamp 0 -C config.txt
    ../../plotting/plot -c $ch -h mtt -l $LUMI --xTitle "m_{t#bar{t}}" --yTitle "Events" --stamp 0 -C config.txt
done
