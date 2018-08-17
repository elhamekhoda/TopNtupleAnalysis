FROM gitlab-registry.cern.ch/atlas-phys/exot/hqt/r21-ttbar-1lep/hqtttresonancestools
ARG CI_JOB_TOKEN
ADD . /Ttres/source/TopNtupleAnalysis
WORKDIR /Ttres/run
RUN source /home/atlas/release_setup.sh && \
    source /Ttres/build/*/setup.sh && \
    cd /Ttres/source && \
    git clone https://gitlab-ci-token:${CI_JOB_TOKEN}@gitlab.cern.ch/MultiBJets/NNLOReweighter.git && \
    cd /Ttres/build && \
    cmake /Ttres/source && \
    make -j4