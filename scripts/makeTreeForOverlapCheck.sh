#!/bin/bash

export dir=/AtlasDisk/user/scalvet/Zprime/ExotComb/Tuples/AnalysisTop-21.2.57_HVTcomb_v1/

ls $dir | awk -v dir="$dir" -F '.' '{print "ls "dir"/user.*"$3"*_output.root/* > "$3".txt"}' |sh


for SAMPLE in `ls $dir | awk  -F '.' '{print $3}'`
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
