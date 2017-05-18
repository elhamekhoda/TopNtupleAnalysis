
LUMI=36.1

PLOTTING=/afs/cern.ch/work/d/dferreir/private/topana/Top2429/TopNtupleAnalysis/plotting/plot

rm -f hist_*.root
#for histogram in mtt mttPos mttNeg ; do
for histogram in mtt ; do
    for ch in be3 bmu3 re3 rmu3 be2 bmu2 re2 rmu2 be1 bmu1 re1 rmu1 be0 bmu0 re0 rmu0 be bmu re rmu ; do
        #$PLOTTING  -c $ch -h $histogram -l $LUMI --saveTH1 ${histogram}${ch}  --smoothen 1 -C config_limit.txt
        $PLOTTING  -c $ch -h $histogram -l $LUMI --saveTH1 ${histogram}${ch}  --smoothen 0 -C config_limit_nosmooth.txt
    done
done

#rm spectrum_all.tar.gz
#tar cvfz spectrum_all.tar.gz hist*.root

