#!/bin/bash

export dir=/AtlasDisk/group/Zprime/AT-21.2.46_HVTcomb_v3/
ls $dir/user.*.301323.*_output_root/* > Zprime500.txt
ls $dir/user.*.301325.*_output_root/* > Zprime1000.txt
ls $dir/user.*.301329.*_output_root/* > Zprime2000.txt
ls $dir/user.*.302715.*_output_root/* > Wprime1000lep.txt
ls $dir/user.*.302719.*_output_root/* > Wprime2000lep.txt
ls $dir/user.*.302723.*_output_root/* > Wprime3000lep.txt
ls $dir/user.*.306136.*_output_root/* > Wprime2000had.txt
ls $dir/user.*.302736.*_output_root/* > Wprime3500had.txt
	  
for SAMPLE in Zprime500 Zprime1000 Zprime2000
do
	echo "Doing "$SAMPLE
	cd ../python
	rm -f hist_*.root
	python makeHistograms.py --do-tree --files=../scripts/$SAMPLE.txt  AnaTtresSL \
	-o "(re1,good,MV2c10_70):hist_re1.root" \
	-o "(re2,good,MV2c10_70):hist_re2.root" \
	-o "(re3,good,MV2c10_70):hist_re3.root" \
	-o "(rmu1,good,MV2c10_70):hist_rmu1.root" \
	-o "(rmu2,good,MV2c10_70):hist_rmu2.root" \
	-o "(rmu3,good,MV2c10_70):hist_rmu3.root" \
	-o "(be1,good,MV2c10_70):hist_be1.root" \
	-o "(be2,good,MV2c10_70):hist_be2.root" \
	-o "(be3,good,MV2c10_70):hist_be3.root" \
	-o "(bmu1,good,MV2c10_70):hist_bmu1.root" \
	-o "(bmu2,good,MV2c10_70):hist_bmu2.root" \
	-o "(bmu3,good,MV2c10_70):hist_bmu3.root" \
	#--nevents=10 \
	
	root -l -b -q '../scripts/makeTreeForOverlapCheck_tool.C("'$SAMPLE'")'
	cd ../scripts
done 
