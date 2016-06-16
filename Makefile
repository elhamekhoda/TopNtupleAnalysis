
ROOTCFLAGS    = $(shell root-config --cflags)

SUFFIXES += .d

MYCF=""

ifneq ($(findstring m32,$(ROOTCFLAGS)),)
        MYCF= CXXFLAGS=-m32 CFLAGS=-m32
endif

ROOTLIB    = $(shell root-config --glibs) -lMinuit -lTreePlayer

CXXFLAGS   = -g -I.
CXXFLAGS  += -Wno-long-long -fPIC
CXXFLAGS  += $(shell root-config --cflags)

LDFLAGS    =
LDFLAGS   += $(ROOTLIB)

OBJS       = Root/Event.o Root/LargeJet.o Root/Muon.o Root/Electron.o Root/Jet.o Root/MObject.o
OBJS      += Root/ParseUtils.o
OBJS      += Root/MMUtils.o
OBJS      += Root/MiniTree.o
OBJS      += Root/UserFunktions.o
OBJS      += Root/KinematicUtils.o

OBJS_READ += $(OBJS)
OBJS_READ += Root/EventCount.o
OBJS_READ += Root/Analysis.o Root/AnaTtresSL.o Root/AnaTtresSLMtt.o Root/AnaTuDoSL.o Root/AnaTuDoTtresResolved.o Root/AnaTuDoTtresBoosted.o Root/HistogramService.o Root/AnaTtresQCD.o Root/AnaTtresMM.o
OBJS_READ += Root/WeakCorrScaleFactorParam.o
OBJS_READ += Root/TopEFTWeight.o
OBJS_READ += util/read.o

OBJS_READTUDO += $(OBJS)
OBJS_READTUDO += Root/EventCount.o
OBJS_READTUDO += Root/Analysis.o Root/AnaTtresSL.o Root/AnaTuDoSL.o Root/AnaTuDoTtresResolved.o Root/AnaTuDoTtresBoosted.o Root/HistogramService.o
OBJS_READTUDO += Root/WeakCorrScaleFactorParam.o
OBJS_READTUDO += util/readTuDo.o

# can use RootCore, but keep like this to make it portable
#OBJS_READ += TopDataPreparation/Root/SampleXsection.o
OBJS_READ += ../TopDataPreparation/Root/SampleXsection.o
# CXXFLAGS += -I../RootCoreBin/include
CXXFLAGS += -I../TopDataPreparation

#  to include the HistoList tool
# CXXFLAGS += -I../TuDoBase
# LDFLAGS += -L../TuDoBase/lib/ -lTuDoBase

OBJS_READ += Root/TtresChi2.o Root/TtresdRmin.o Root/TtresNeutrinoBuilder.o
OBJS_READTUDO += Root/TtresChi2.o Root/TtresdRmin.o Root/TtresNeutrinoBuilder.o

all: read readTuDo

#We don't need to clean up when we're making these targets
NODEPS:=clean
#Find all the C++ files in the src/ directory
SOURCES:=$(shell find Root/ util/ -name "*.cxx")
#These are the dependency files, which make will clean up after it creates them
DEPFILES:=$(patsubst %.cxx,%.d,$(SOURCES))
#Don't create dependencies when we're cleaning, for instance
ifeq (0, $(words $(findstring $(MAKECMDGOALS), $(NODEPS))))
    #Chances are, these files don't exist.  GMake will create them and
    #clean up automatically afterwards
    -include $(DEPFILES)
endif


%.o: %.cxx %.d
	g++ -c $(CXXFLAGS) -o $@ $<

%.d: %.cxx
	g++ $(CXXFLAGS) -MM -MT '$(patsubst %.cxx,%.o,$<)' $< -MF $@


read: $(OBJS_READ)
	g++ $(CXXFLAGS) -o read $(OBJS_READ) $(LDFLAGS)

read2: $(OBJS_READ)
	g++ $(CXXFLAGS) -o read2 $(OBJS_READ) $(LDFLAGS)
	
readTuDo: $(OBJS_READTUDO)
	g++ $(CXXFLAGS) -o readTuDo $(OBJS_READTUDO) $(LDFLAGS)
	
clean:
	rm -rf *.o read readTuDo Root/*.o util/*.o


