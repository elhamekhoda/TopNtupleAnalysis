
LUMI=14.76518

PLOTTING=/afs/desy.de/user/d/danilo/xxl/af-atlas/Top2416/TopNtupleAnalysis/plotting/plot

for ch in be bmu re rmu be2015 bmu2015 re2015 rmu2015 be2016 bmu2016 re2016 rmu2016 ; do
    $PLOTTING -c $ch -h yields -l $LUMI -C config.txt >yields_${ch}.txt
#    $PLOTTING -c $ch -h yields_bveto -l $LUMI -C config.txt >yields_bveto_${ch}.txt
    $PLOTTING -c $ch -h yieldsPos -l $LUMI -C config.txt >yieldsPos_${ch}.txt
#    $PLOTTING -c $ch -h yields_bvetoPos -l $LUMI -C config.txt >yields_bvetoPos_${ch}.txt
    $PLOTTING -c $ch -h yieldsNeg -l $LUMI -C config.txt >yieldsNeg_${ch}.txt
#    $PLOTTING -c $ch -h yields_bvetoNeg -l $LUMI -C config.txt >yields_bvetoNeg_${ch}.txt
done

for ch in be bmu re rmu be2015 bmu2015 re2015 rmu2015 be2016 bmu2016 re2016 rmu2016 ; do
    $PLOTTING -c $ch -h lepPt --normBinWidth 20 -l $LUMI --rebin 4 --xTitle "Lepton p_{T} [GeV]" --yTitle "Events / 20 GeV" --stamp 0 -C config.txt
    $PLOTTING -c $ch -h lepEta  -l $LUMI  --xTitle "Lepton #eta" --yTitle "Events / 0.25" --stamp 0 -C config.txt
    $PLOTTING -c $ch -h nJets -l $LUMI --xTitle "Number of jets" --yTitle "Events" --stamp 0 -C config.txt
    $PLOTTING -c $ch -h nTrkBtagJets -l $LUMI --xTitle "Number of b-tagged track jets" --yTitle "Events" --stamp 0 -C config.txt
    $PLOTTING -c $ch -h MET --normBinWidth 20 -l $LUMI --yTitle "Events / 20 GeV" --xTitle "E_{T}^{miss} [GeV]" --stamp 0 -C config.txt
    $PLOTTING -c $ch -h MET_phi -l $LUMI --yTitle "Events / 0.2" --xTitle "E_{T}^{miss} #phi [rd]" --stamp 0 -C config.txt
    $PLOTTING -c $ch -h mwt -l $LUMI --yTitle "Events / 10 GeV" --xTitle "m_{WT} [GeV]" --stamp 0 -C config.txt
    $PLOTTING -c $ch -h closeJetPt -l $LUMI --normBinWidth 10 --yTitle "Events / 10 GeV" --xTitle "Selected jet p_{T} [GeV]" --stamp 0 -C config.txt
    $PLOTTING -c $ch -h largeJetPt -l $LUMI --normBinWidth 20 --yTitle "Events / 20 GeV" --xTitle "Large-R jet p_{T} [GeV]" --stamp 0 -C config.txt
    $PLOTTING -c $ch -h largeJetM -l $LUMI  --yTitle "Events / 10 GeV" --xTitle "Large-R jet mass [GeV]" --stamp 0 -C config.txt
    $PLOTTING -c $ch -h largeJetPtMtt -l $LUMI  --yTitle "Events / 0.02" --xTitle "Large-R jet p_{T} / m_{t#bar{t}} " --stamp 0 -C config.txt
    $PLOTTING -c $ch -h largeJetEta -l $LUMI  --yTitle "Events / 0.1" --xTitle "Large-R jet #eta" --stamp 0 -C config.txt
    $PLOTTING -c $ch -h largeJetPhi -l $LUMI  --yTitle "Events / 0.2" --xTitle "Large-R jet #phi [rd]" --stamp 0 -C config.txt
    $PLOTTING -c $ch -h mtlep_boo -l $LUMI --normBinWidth 20  --yTitle "Events / 20 GeV" --xTitle "Mass of the leptonic top [GeV]" --stamp 0 -C config.txt
    $PLOTTING -c $ch -h mtlep_res -l $LUMI --normBinWidth 20  --yTitle "Events / 20 GeV" --xTitle "Mass of the leptonic top [GeV]" --stamp 0 -C config.txt
    $PLOTTING -c $ch -h mthad_res -l $LUMI --normBinWidth 20  --yTitle "Events / 20 GeV" --xTitle "Mass of the hadronic top [GeV]" --stamp 0 -C config.txt
    $PLOTTING -c $ch -h mwhad_res -l $LUMI --normBinWidth 20  --yTitle "Events / 20 GeV" --xTitle "Mass of the hadronic W [GeV]" --stamp 0 -C config.txt
    $PLOTTING -c $ch -h chi2 -l $LUMI  --yTitle "Events / 0.2" --xTitle "log(#chi^{2})" --stamp 0 -C config.txt
    $PLOTTING -c $ch -h largeJet_tau32_wta -l $LUMI  --yTitle "Events / 0.05" --xTitle "Large-R jet #tau_{32} wta" --stamp 0 -C config.txt
    $PLOTTING -c $ch -h largeJet_tau21_wta -l $LUMI  --yTitle "Events / 0.05" --xTitle "Large-R jet #tau_{21} wta" --stamp 0 -C config.txt
    $PLOTTING -c $ch -h trueMtt --mcOnly 1 --normBinWidth 100 --logY 1 -l $LUMI --xTitle "true m_{t#bar{t}}" --yTitle "Events / 100 GeV" --stamp 0 -C config.txt
done

for ch in be bmu re rmu re2015 rmu2015 be2016 bmu2016 re2016 rmu2016 ; do
    $PLOTTING -c $ch -h mtt --mcOnly 1 --normBinWidth 100 --logY 1 -l $LUMI --xTitle "m_{t#bar{t}}" --yTitle "Events / 100 GeV" --stamp 0 -C config.txt
done

for ch in bmu2015 be2015 ; do
    $PLOTTING -c $ch -h mtt --mcOnly 0 --normBinWidth 100 --logY 1 -l $LUMI --xTitle "m_{t#bar{t}}" --yTitle "Events / 100 GeV" --stamp 0 -C config.txt
done
