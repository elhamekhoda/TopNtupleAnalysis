This is a framework for reading flat ntuples generated from AnalysisTop, running an analysis over them and producing final plots. It is recommended to use the Python code in `pyHistograms`, which will also link to the C++ code, but it should be easier to adapt to your needs. To do so, you can compile the code using either __Atlas CMake__ or simply __CMake__.


Prerequisites
-------------
#### Optional
* NNLO Reweighting: NNLOReweighter (Only works with __Altas CMake__)

    ```bash
    acm clone_project MultiBJets/NNLOReweighter
    ```
* Grid Access: HQTTtResonancesTools (Only works with __Altas CMake__)

    ```bash
    acm clone_project elham/BoostedJetTaggers
    acm clone_project atlas-phys/exot/hqt/R21-ttbar-1lep/TtResonancesTools
    acm clone_project atlas-phys/exot/hqt/R21-ttbar-1lep/HQTTtResonancesTools
    ```
* EFTLib: LHAPDF

General Instruction
-------------------
#### Installation
1. Use __Atlas CMake__ ({+ Recommended +})

    ```bash
    acm clone_project atlas-phys/exot/hqt/R21-ttbar-1lep/TopNtupleAnalysis
    acm find_packages
    acm compile
    ```
2. Use __vanilla CMake__ ({- Alternative -})  
   A portable version that can be installed in your laptop without git-atlas or athena environment. You only need __TopDataPreparation__. Fast (but quite tedious) way to do so is:
   ```bash
   # Sparse checkout TopDataPreparation from athena
   git init athena
   git -C athena config core.sparseCheckout true
   git -C athena remote add upstream https://:@gitlab.cern.ch:8443/atlas/athena.git
   echo PhysicsAnalysis/TopPhys/TopPhysUtils/TopDataPreparation >> athena/.git/info/sparse-checkout
   git -C athena fetch --depth 1 upstream 21.2
   git -C athena checkout 21.2
   # Symbolic link TopDataPreparation side by side with TopNtupleAnalysis
   ln -s athena/PhysicsAnalysis/TopPhys/TopPhysUtils/TopDataPreparation
   # Checkout TopNtupleAnalysis
   git clone https://:@gitlab.cern.ch:8443/atlas-phys/exot/hqt/R21-ttbar-1lep/TopNtupleAnalysis.git
   cd TopNtupleAnalysis && cmake . && cmake --build . -- -j 4
   ```
   Note that there are some restrictions for this stand-alone version without __Atlas CMake__.
   
#### Usage
The main UI is `pyHistograms/makeHistograms.py`.
```
usage: makeHistograms.py [-h] [-d] [-f FILE] [-A ANALYSIS] [-o [FILES]]
                         [-s SYSTEMATICS] [-W FLAVOURS] [-P PDFS] [-Q CHANNEL]
                         [-N] [-M CUT] [-S MH,MA,SBA,TANB,TYPE]
                         [-E LAMBDA,CVV] [-K WIDTH] [-D] [-p PDF] [-F] [-w]
                         [-u FLOAT] [-t TOP_TAGGER]

optional arguments:
  -h, --help            show this help message and exit
  -d, --data            Is this data? (default: False)
  -f FILE, --files FILE
                        Text file with list of input files. (default:
                        input.txt)
  -A ANALYSIS, --analysis ANALYSIS
                        Analysis code to run. (default: AnaTtresSL)
  -o [FILES], --output [FILES]
                        You can run more than 1 channels in the same time. The
                        syntax is "-o (<topo><lep>[<b-cat>],[<top-
                        tagger>]):<output_fname> [-o ... [-o ...]]". See Also:
                        `--top-tagger` (default:
                        ['(re,good_smooth_ts80):hist_re.root',
                        '(rmu,good_smooth_ts80):hist_rmu.root',
                        '(be,good_smooth_ts80):hist_be.root',
                        '(bmu,good_smooth_ts80):hist_bmu.root'])
  -s SYSTEMATICS, --systs SYSTEMATICS
                        Comma-separated list of systematic uncertainties in
                        TTrees in the input file. Use 'all' to run over all
                        the default ones. (default: nominal)
  -W FLAVOURS, --WjetsHF FLAVOURS
                        Which W+jets HF to keep. Can be all, bb, cc, bbcc, c
                        or l. (default: all)
  -P PDFS, --pdf PDFS   Which PDFs to reweight to. (default: )
  -Q CHANNEL, --qcd CHANNEL
                        Apply QCD weights? (default: False)
  -N, --noMttSlices     If set, stop vetoing high mtt events in 410000 sample.
                        (default: False)
  -M CUT, --applyMET CUT
                        Extra MET cut to be applied. (default: 0)
  -S MH,MA,SBA,TANB,TYPE, --SCALAR MH,MA,SBA,TANB,TYPE
                        Parameters to use when reweighting LO ttbar+jets to a
                        scalar 2HDM setup with a configuration of
                        {mH,mA,sin(b-a), tan(b) and the model type}. (default:
                        )
  -E LAMBDA,CVV, --EFT LAMBDA,CVV
                        Parameters to use when reweighting LO ttbar to an EFT
                        setup with a lambda and cvv configuration. Set lambda
                        to a negative value to disable this. (default: )
  -K WIDTH, --KKgluon WIDTH
                        Parameters to use when reweighting KK gluon samples.
                        The parameter should be the destination width as an
                        integer, which is a percentage of the mass. (default:
                        )
  -D, --DM              Do Zprime to DM reweighting? (default: False)
  -p PDF, --pdfForWeight PDF
                        PDF to use to get alpha_S when doing either the EFT or
                        the scalar model reweighting. (default:
                        NNPDF30_nlo_as_0118)
  -F, --af2             Is this AF2? (default: False)
  -w, --noPRW           Don't do pile up reweighting. (default: False)
  -u FLOAT, --accept_prob FLOAT
                        Probability of accepting an event. Factor to use when
                        dropping events in data to reduce luminosity
                        available. (default: 1)
  -t TOP_TAGGER, --top-tagger TOP_TAGGER
                        "GLOBAL" Boosted top tagger which will applied to the
                        large-R jet for the hadronic-top reconstruction in the
                        boost selection. Simple logical operation are
                        supported. ONLY WORK IF YOU DON'T USE ANY TOP-TAGGER
                        IN THE _OUTPUT_ SELECTIONS. (default:
                        good_smooth_ts80)
```

Create your own scripts based on this! Some very nice examples can be found in `pyHistograms/`.

#### Quick Start
1. Please first follow the instruction [__HERE__](https://gitlab.cern.ch/atlas-phys/exot/hqt/R21-ttbar-1lep/HQTTtResonancesTools/wikis/home) of HQTTtResonancesTools and generate a TopNtuple `run/output.root`.
2. `cd $TestArea/../run/` and run TopNtupleAnalysis

     ```bash
     echo "$TestArea/../run/output.root" > tna-input.txt
     $SourceArea/TopNtupleAnalysis/pyHistograms/makeHistograms.py \
     -f tna-input.txt
     ```
   Change the flags according to [Usage](#usage) to adapt to your needs.
   
<details>
<summary><h3>AnalysisTop Rel.20.7</h3></summary>
It is recommended to use the Python code in <code>pyHistograms</code>, which will also link to the C++ code, but it should be easier to adapt to your needs.
To do that, please compile the code using RootCore, so that it can link against the library created by RootCore.
To run this code, one must also checkout the following packages and recompile the RootCore setup:
<pre><code class=bash>svn co svn+ssh://$CERN_USER@svn.cern.ch/reps/atlasoff/PhysicsAnalysis/TopPhys/TopPhysUtils/TopDataPreparation/trunk TopDataPreparation
svn co svn+ssh://$CERN_USER@svn.cern.ch/reps/atlasphys-hsg8/Physics/Higgs/HSG8/AnalysisCode/NNLOReweighter/tags/NNLOReweighter-00-00-03 NNLOReweighter</code></pre>

In that Python code, you can run it with: <code>cd pyHistograms</code>

<ol>
  <li style="font-weight: bold;">
     <p><span style="font-weight: bold;">the following make a list of all input MC files (adapt it to point to the input files list)</span></p>
     <pre><code class=bash>python makeInputsListLocal.py</code></pre>
  <\li>
  <li style="font-weight: bold;">
    <p><span style="font-weight: bold;">this generates the text files with the sum of weights using the input files above</span></p>
    <pre><code class=bash> python sumWeights.py</code></pre>
    <\li>
  <li style="font-weight: bold;">
    <p><span style="font-weight: bold;">this generates the histograms itself:</span></p>
    <pre><code class=bash>./makeHistograms.py - --files input.txt --output be,be.root\;bmu,bmu.root\;re,re.root\;rmu,rmu.root --analysis AnaTtresSL --systs nominal</code></pre>
</ol>

You can set <code>--systs</code> to all to run over all systematics (takes much longer), or give it a comma-separated list of systematics.
You can use the option -d to indicate you want to run over data.
The syntax of the --output flag is to provide a semi-colon-separated list of "XXX,YYY", where XXX indicates the channel to run (it will be read by the analysis in analysis.py,
specified in the <code>--analysis</code> flag) and YYY indicates the output ROOT file for that channel.
AnaTtresSL in analysis.py is set up to have the be, bmu, re, rmu channels as well as be2015, bmu2015, re2015, rmu2016, be2016, bmu2016, re2016, rmu2016,
be3,bmu3,be2,bmu2,be1,bmu1,be0,bmu0,re3,rmu3,re2,rmu2,re1,rmu1,re0,rmu0. But you can create
a new class in analysis.py of your choice and define different channels.

Check <code>runBatchLocal.py</code> to check how to submit it on a local cluster.
</details>

<details>
<summary><h3>Pre AnalysisTop Rel.20.7</h3></summary>
The framework works by reading the flat ntuples using the class MiniTree, as called
from <code>read.cxx</code> and then running an analysis class (that derives of Analysis) on each event and
producing histograms to be saved in the output(s).

To compile the code, do in this directory (only ROOT must be setup):
<pre><code class=bash>make</code></pre>
You can also compile the code using RootCore, by setting up RootCore (<code>setupATLAS</code> and then <code>rcSetup Top,2.4.29</code>) and doing:
<pre><code class=bash>rc find_packages
rc compile</code></pre>

To check your options on how to run it: <code>./read --help</code>

If you used RootCore, you must run it with: <code>$ROOTCOREBIN/bin/x86_64-slc6-gcc49-opt/read --help</code>

(this will be implied in what follows)


For example:
<pre><code class=bash>./read --files input1.root,input2.root --analysis AnaTtresSL --output resolved_e.root,resolved_mu.root,boosted_e.root,boosted_mu.root --data 0</pre></code>
The --analysis flag indicate which class that derives of analysis should be called. It is created in read.cxx.
To create your own Analysis class, just change <code>read.cxx</code> to check the value of <code>--analysis</code> and create an instance of your analysis class
in analogy with:
<pre><code class=cpp>  std::vector<Analysis *> vec_analysis; 
  if (analysis == "AnaTtresSL") {
    vec_analysis.push_back(new AnaTtresSL(outList[0], true,  false )); // resolved electron
    vec_analysis.push_back(new AnaTtresSL(outList[1], false, false )); // resolved muon
    vec_analysis.push_back(new AnaTtresSL(outList[2], true,  true  )); // boosted  electron
    vec_analysis.push_back(new AnaTtresSL(outList[3], false, true  )); // boosted  muon
  } </code></pre>

The list of output files is given as 4 files, since in this analysis 4 channels are expected. If your analysis only outputs one file, only the
first should be considered.

The list of inout files can be given as a comma-separated list, or it can be given as a newline-separated text file that ends in .txt and starts
with input, for example:
<pre><code class=bash>./read --files input.txt --analysis AnaTtresSL --output resolved_e.root,resolved_mu.root,boosted_e.root,boosted_mu.root --data 0</pre></code>

where input.txt has:
<pre><code>input1.root
input2.root</pre></code>

Take a look at the <code>Root/AnaTtresSL.cxx</code> and <code>TopNtupleAnalysis/AnaTtresSL.h</code> files for an analysis example.

If, however, the mini flat ntuple files contain a histogram with the sum of weights (which is the correct
way of doing this), one can just read the information from there.

You can also write a <code>sumOfWeights.txt</code> file containing, in each line the dataset ID and the sum of weights and use:
<pre><code class=bash>./read --files input.txt --analysis AnaTtresSL --output re.root,rmu.root,be.root,bmu.root --data 0 --sumWeights sumOfWeights.txt</pre></code>

This will speed it up.
</details>

Auxiliary scripts
-----------------
The input files for read.cxx can be produced by running top-xaod from the TopAnalysis package with the OutputMinixAOD flag set to False
in the configuration file.
The output is then downloaded with dq2-get and the script in `scripts/addFiles.py` can be used to add all output ROOT file in a single file per
sample type.
However, for large files, it is recommended to use `scripts/run.py` directly, so that the original files are read and processed
with no intermediate step.

To use `scripts/run.py`, edit the following lines so that ntuplesDir points to the directory where you downloaded the Grid
datasets, outputDir points to the directory where to save the output of TopNtupleAnalysis and names contains a list of
datasets defined according to the imports from `HQTTtResonancesTools/python`.

```python
import HQTTtResonancesTools.DC15MC13TeV_25ns_EXOT4_p2375
import HQTTtResonancesTools.DC15MC13TeV_EXOT4_p2352

ntuplesDir = '/afs/cern.ch/user/d/dferreir/work/eos/atlas/user/d/dferreir/topana/09092015'
outputDir = 'test25ns'
analysisType='AnaTtresSL'

#### each string defines a set of datasets in the Grid, which are written in the Python files above
names  = ['MC15_13TeV_25ns_FS_EXOT4_ttbarPowhegPythia', 'MC15_13TeV_25ns_FS_EXOT4_ttbarPowhegPythia_mttsliced']
```

Run it with: `python scripts/run.py`

(in the future an official 13 TeV configuration file might be helpful)

`svn co svn+ssh://$CERN_USER@svn.cern.ch/reps/atlasoff/PhysicsAnalysis/TopPhys/TopPhysUtils/TopDataPreparation/trunk TopDataPreparation`
There is no need to compile it, since the current Makefile includes it directly only for the C++ file needed.


Plotting and limit setting preparation code
-------------------------------------------

A C++ code has been written which can calculate all systematic uncertainties, plot them, smoothen them and also
output the smoothened results.

To compile it, go to the plotting directory and do make first:
```bash
cd plotting
make
```

You can then move to the directory in which your output files are and run the plotting code, however the following
conventions must be observed. The name of the ROOT files must follow the standard `[prefix]_[channel]_[sample].root`
and each ROOT file must contain the histogram to be plotted with the same binning. The systematic variations and sample names
can be configured in a configuration file described below.

The plotting code can be run, for example, as follows:
```bash
cd directoryWithOutput
</path/to/plotting/code/plot> -p prefix -c channel -h histogramName -l 3.209 --smoothen 1 -C configuration.txt
```

This will look for files called `prefix_channel_[sample].root` (where "[sample]" is specified in the configuration file) and it
expects the histogram "histogramName" to be in those files. The samples that do not have "Data" or "QCD" in the name will be scaled
by the argument of `-l` (the luminosity). You can set the "luminosity" to 0 if the input files are already normalised, but this is used to
show the luminosity in the plots (if a negative value is used, the luminosity is not used to normalise the MC samples, but it is shown in the plots in absolute value).
The `--smoothen` flag indicates whether smoothening should be enabled (it can be forcefully
disabled in the configuration file if it should not be applied to a specific systematic uncertainty).

An example of the configuration file can be seen in plotting/config.txt.

The lines beginning with "sample" indicate a sample to be considered when making the stack plot. Its format is the following:
```
sample      InternalName            fileSuffix                "Name to show in plot legend"                   "Name to show in LaTeX table output"             colorNumber
```

The internal name is only used internally as an identifier, while fileSuffix is the ending of the file name. In the example above,
the file used for this sample would be prefix_channel_fileSuffix.root. The color number indicates the color used when filling the histogram in the stack plot.
The names in columns 4 and 5 need to be in double quotes if they include spaces (otherwise the double quotes are optional).

The systematic uncertainties can be included in different ways. A flat systematic uncertainty to be applied in only
a subset of the samples can be added with lines beginning with "syst_flat"). For example:
```
syst_flat lumi             "luminosity"                     "ttbar,singletop,Zjets,VV"        0.05                                       -0.05
```

This adds an uncertainty called internally "lumi", but shown in the output LaTeX tables as "luminosity". This uncertainty will be a flat +/- 5%
uncertainy applied only in the samples with suffixes including either ttbar, singletop, Zjets or VV in their name.

An uncertainty that comes from the difference between the histograms (the histogram name is given by the -h parameter in the plot call above)
can be included as with a line beginning with "syst_model". For example:

```
syst_model ttgen           "ttbar gen."                     "ttbar"                           suffixA                suffixB          S
```

This line adds an uncertainty internally called "ttgen", but shown in the output LaTeX tables as "ttbar gen." (notice the double quotes due to the space).
It will be calculated as the bin-by-bin quantity taken from the histograms in `prefix_channel_suffixA.root` and `prefix_channel_suffixB.root`. The final letter "__S__" indicates
this systematic uncerrtainty should be smoothened, if the --smooth option in the command line has been activated. A letter "N" can be used instead if smoothing is not desired.
The uncertainty is calculated as $`(A-B)/(0.5*(A+B))`$, bin by bin.

Finally, if the systematic uncertainty variation histograms are available in the same original file (that is, prefix_channel_sampleName.root)
but just in a different histogram, one can use the "syst" line to include that systematic variation. For example, if the nominal result is
in a histogram called histogramName and the systematic variation up is in histogram histogramName_varUp and the down variation is
in histogram histogramName_varDw, you can use the following line to include this systematic variation:
```
syst      myvariation      "Name to show in LaTeX"          _varUp                            _varDw                 S                 sampleZ,sampleW
```

The column with "__S__" can also have "__N__" to avoid smoothing this systematic uncertainty. The last column has a comma-separated list of
samples on which this uncertainty should not be applied. It can be ignored if this is to be applied to all samples.


Finally, note that one other option in plot is `--saveTH1` channel. If this option is provided, a set of output files called `hist_[internalSampleName].root` are created.
These files will have the histogram and all its systematic variations after smoothing and including the uncertainties in syst_flat and syst_model.
This file can be used to be fed to the TRexFitter for limit setting.

Note as well, that running plot with the `--saveTH1 [channel]` multiple times will update the output hist_[sample].root files with the different channels.
So it is recommended to remove any `hist_*.root` files in the current directory when calling this. This is done in such a way, so that the different
signal regions can be added in the output files.


Limit setting
-------------

The limit setting can be done using __TRexFitter__. The input files used in the limit setting will be following the format dumped by the
--saveTH1 option mentioned in the previous section. The files are called hist_[sampleName].root and they have the nominal histogram in them with the name
"x[channel]", where [channel] is the option sent to the --saveTH1 option. The systematic variations are appended to the end of the
histogram name. For example, the nominal spectrum in the electron channel would be in the histogram "xe" and the ttbar generator uncetainty for this channel
would be in histogram "xettgenup" and "xettgendw".

These names are, of course configurable, but this is the format of the histograms dumped by the --saveTH1 option above, which also smoothens the
histograms correctly. The standard configuration below will be following these guidelines and it should be compatible with the configuration
in plotting/config_limit.txt.

One example of the standard way of generating the input files for the limit setting using the output of read and AnaTtresSL, would be:
```bash
rm -f hist*.root

for ch in boosted resolved ; do
  for lep in e mu ; do
    ../plotting/plot  -c $lep -p $ch -h mtt -l 3.209 --saveTH1 ${ch}${lep}  --smoothen 1 -C ../plotting/config_limit.txt
  done
done
```

The TRexFitter can be downloaded and compiled as:
```bash
cd limits/binned
svn co svn+ssh://$CERN_USER@svn.cern.ch/reps/atlasinst/Institutes/UdineICTP/TtHFitter/trunk  TRexFitter
cd TRexFitter
make
```

At this stage you can copy the `inputs.py`, `ttres_template.config` and `makeConfigs.py`, as well as the `hist_*.root` files generated previously with the spectra
in the __TRexFitter__ directory. The ttres_template.config has the configuration for the ttbar boosted channel limit setting, but with the signal line commented out.
As the limit setting has to be done separately for each of the signal mass points, the script makeConfigs.py can be used to loop over the signal points and do the
limit setting automatically.

Therefore, assuming the ttres_template.config sample names and the files (hist_XXX) are compatible with your output, you can simply do now:
```bash
python makeConfigs.py
```

This will add the signal configuration lines for each signal sample and produce copies of `ttres_template.config` for each sample. It will then do the
background only fit and the limit setting for each mass point.

Alternatively, you can uncomment the signal lines in ttres_template.config yourself (preferably use a different name for this file), and then call __TRexFitter__ for
the limit setting:
```bash
./myFit.exe h ttres_myConfig.config
./myFit.exe w ttres_myConfig.config
./myFit.exe l ttres_myConfig.config
```

If data is not available or it is blind, you can create the pseudo-data file with:
```bash
hadd -f hist_data.root hist_ttbar.root hist_singletop.root hist_Zjets.root hist_Wjets.root hist_VV.root
```

The output file showing the upper limit in mu will be in `JobTtres*/Limits/JobTtres*.root`.
You can produce correlation matrices and the nuisance parameter pulls using this:
```bash
./myFit.exe f ttres_myConfig.config
```

Notice that for the last command you still need to specify a signal sample, but if you change the FitType option from __SPLUSB__ to __BONLY__, only the background
fit is done.
The output nuisance parameter fit is done in `JobTtres*/NuisPar.png`. The correlation matrix is in `JobTtres*/CorrMatrix.png`.

Please look for more information on TRexFitter here:
https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/TtHFitter

The final mass limit plot can be produced using the massLimit.py script:
```bash
python massLimit.py
```
It generates the mass limit in `mass_limit.py`.


-------------------------------
For more information, contact:  
Danilo Enoque Ferreira de Lima  
dferreir@mail.cern.ch


