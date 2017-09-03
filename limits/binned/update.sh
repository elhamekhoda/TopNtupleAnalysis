rm -rf tmp
mkdir tmp
rm limit_pack.tar.gz

cp mass_limit_zprime.* tmp
cp mass_limit_kkgluon.* tmp
cp mass_limit_kkG.* tmp
cp mass_limit_zprime_stat.* tmp
cp mass_limit_kkgluon_stat.* tmp
cp mass_limit_kkG_stat.* tmp

mkdir tmp/Ttres_bkg
mkdir tmp/Ttres_bkg/Plots
mkdir tmp/Ttres_bkg/Fits
cp Ttres_bkg/*.pdf tmp/Ttres_bkg/
cp Ttres_bkg/Plots/*.pdf tmp/Ttres_bkg/Plots/
cp Ttres_bkg/Fits/* tmp/Ttres_bkg/Fits/

mkdir tmp/Ttres_bkg_cat1
mkdir tmp/Ttres_bkg_cat2
mkdir tmp/Ttres_bkg_cat3
cp Ttres_bkg_cat1/*.pdf tmp/Ttres_bkg_cat1/
cp Ttres_bkg_cat2/*.pdf tmp/Ttres_bkg_cat2/
cp Ttres_bkg_cat3/*.pdf tmp/Ttres_bkg_cat3/

for i in zprime2000 zprime3000 zprime2000_inj zprime3000_inj ; do
  mkdir tmp/Ttres_$i
  cp Ttres_$i/*.pdf tmp/Ttres_$i/
done

mkdir tmp/fine_binning
mkdir tmp/fine_binning/std
mkdir tmp/fine_binning/std/Plots
mkdir tmp/fine_binning/fine
mkdir tmp/fine_binning/fine/Plots
mkdir tmp/fine_binning/fine/Plots_zprime3000
mkdir tmp/fine_binning/fine/Plots_zprime5000

cp tmp/mass_limit_* tmp/fine_binning/std/
cp tmp/Ttres_bkg/Plots/*.pdf tmp/fine_binning/std/Plots/
cp tmp/Ttres_bkg/*.pdf tmp/fine_binning/std/
cp mass_limit_zprime_binning.* tmp/fine_binning/fine/
cp mass_limit_kkgluon_binning.* tmp/fine_binning/fine/
cp mass_limit_kkG_binning.* tmp/fine_binning/fine/
cp limit_ratio_zprime__binning.* tmp/fine_binning/fine/
cp limit_ratio_kkgluon__binning.* tmp/fine_binning/fine/
cp limit_ratio_kkG__binning.* tmp/fine_binning/fine/
cp Ttres_bkg_binning/*.pdf tmp/fine_binning/fine/
cp Ttres_bkg_binning/Plots/*.pdf tmp/fine_binning/fine/Plots/
cp Ttres_zprime3000_binning/Plots/*.pdf tmp/fine_binning/fine/Plots_zprime3000/
cp Ttres_zprime5000_binning/Plots/*.pdf tmp/fine_binning/fine/Plots_zprime5000/

mkdir tmp/nnlo
mkdir tmp/nnlo/nnlo
mkdir tmp/nnlo/std

cp mass_limit_zprime_nnlo.* tmp/nnlo/nnlo
cp mass_limit_kkgluon_nnlo.* tmp/nnlo/nnlo
cp mass_limit_kkG_nnlo.* tmp/nnlo/nnlo
cp limit_ratio_zprime__nnlo.* tmp/nnlo/nnlo
cp limit_ratio_kkgluon__nnlo.* tmp/nnlo/nnlo
cp limit_ratio_kkG__nnlo.* tmp/nnlo/nnlo
cp tmp/mass_limit_* tmp/nnlo/std/
cp tmp/Ttres_bkg/Plots/* tmp/nnlo/std/
cp tmp/Ttres_bkg/*.pdf tmp/nnlo/std/

cp Ttres_bkg_nnlo/Plots/*.pdf tmp/nnlo/nnlo/
cp Ttres_bkg_nnlo/*.pdf tmp/nnlo/nnlo/


mkdir tmp/boottnorm
mkdir tmp/boottnorm/std
mkdir tmp/boottnorm/boottnorm

cp mass_limit_zprime_boottnorm.* tmp/boottnorm/boottnorm
cp mass_limit_kkgluon_boottnorm.* tmp/boottnorm/boottnorm
cp mass_limit_kkG_boottnorm.* tmp/boottnorm/boottnorm
cp limit_ratio_zprime__boottnorm.* tmp/boottnorm/boottnorm
cp limit_ratio_kkgluon__boottnorm.* tmp/boottnorm/boottnorm
cp limit_ratio_kkG__boottnorm.* tmp/boottnorm/boottnorm

cp tmp/mass_limit_*.pdf tmp/boottnorm/std/
cp tmp/Ttres_bkg/Plots/*.pdf tmp/boottnorm/std/
cp tmp/Ttres_bkg/*.pdf tmp/boottnorm/std/

cp Ttres_bkg_boottnorm/Plots/*.pdf tmp/boottnorm/boottnorm/
cp Ttres_bkg_boottnorm/*.pdf tmp/boottnorm/boottnorm/

mkdir tmp/mttSlope
mkdir tmp/mttSlope/std
mkdir tmp/mttSlope/mttSlope
mkdir tmp/mttSlope/mttSlope/effect

cp tmp/Ttres_bkg/Plots/*.pdf tmp/mttSlope/std/
cp tmp/Ttres_bkg/*.pdf tmp/mttSlope/std/

cp Ttres_bkg_slope/Plots/*.pdf tmp/mttSlope/mttSlope/
cp Ttres_bkg_slope/*.pdf tmp/mttSlope/mttSlope/
cp Ttres_bkg_slope/Systematics/mttSlope/*.pdf tmp/mttSlope/mttSlope/effect

cd tmp
tar cvfz ../limit_pack.tar.gz .
cd ..


