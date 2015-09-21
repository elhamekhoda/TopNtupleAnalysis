
#./FitSignal -L 10000.0
./FitBkg -L 10000.0
for i in zp125tev zp15tev zp175tev
do
    ./MakeWorkspace -n ${i} -L 10000.0 --data ttres_new/bkg.root --nosyst 0

    ./FitCombined --workspace results/workspace_${i}.root --suffix ${i} -L 10000.0
    ./SetLimit --workspace results/workspace_${i}.root  --suffix ${i} --poiscan 0.0:50:2.0 -L 10000.0 --external 0
done

for i in zp2tev zp225tev zp25tev zp275tev
do
    ./MakeWorkspace -n ${i} -L 10000.0 --data ttres_new/bkg.root --nosyst 0

    ./FitCombined --workspace results/workspace_${i}.root --suffix ${i} -L 10000.0
    ./SetLimit --workspace results/workspace_${i}.root  --suffix ${i} --poiscan 0.0:100:5.0 -L 10000.0 --external 0

done

for i in zp4tev
do
    ./MakeWorkspace -n ${i} -L 10000.0 --data ttres_new/bkg.root --nosyst 0

    ./FitCombined --workspace results/workspace_${i}.root --suffix ${i} -L 10000.0
    ./SetLimit --workspace results/workspace_${i}.root  --suffix ${i} --poiscan 0.0:100:100.0 -L 10000.0 --external 0

done

