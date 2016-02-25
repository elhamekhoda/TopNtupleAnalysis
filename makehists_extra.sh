
S=1
LUMI=3.20905

rm -f hist_*.root
for histogram in mtt largeJetPt largeJetM ; do

    for ch in boosted ; do
      for lep in e mu ; do
        ../plotting/plot  -c $lep -p $ch -h $histogram -l $LUMI --saveTH1 ${histogram}${ch}${lep}  --smoothen $S -C ../plotting/config_limit.txt
      done
    done

done

rm spectrum_all.tar.gz
tar cvfz spectrum_all.tar.gz hist*.root

