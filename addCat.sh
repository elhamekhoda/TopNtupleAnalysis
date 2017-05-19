
for i in data kkg1000 kkg1500 kkg2000 kkg2500 kkg3000 kkg3500 kkg4000 kkg4500  kkg5000 kkg500 kkgrav1000 kkgrav2000 kkgrav3000 kkgrav400 kkgrav500 kkgrav750 qcde qcdmu singletop ttall tthm ttpdf ttpowhegherwig ttradhi ttradlo tt ttsyst ttv vv wbbjets wccjets wcjets wljets zjets zprime1000 zprime1250 zprime1500 zprime1750 zprime2000 zprime2250 zprime2500 zprime2750 zprime3000 zprime4000 zprime400 zprime5000 zprime500 zprime750 ; do
  hadd -f beX_${i}.root be3_${i}.root be2_${i} be1_${i}.root
  hadd -f bmuX_${i}.root bmu3_${i}.root bmu2_${i} bmu1_${i}.root
  hadd -f reX_${i}.root re3_${i}.root re2_${i} re1_${i}.root
  hadd -f rmuX_${i}.root rmu3_${i}.root rmu2_${i} rmu1_${i}.root
done

