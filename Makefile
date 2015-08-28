
ROOTCFLAGS    = $(shell root-config --cflags)

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
OBJS      += Root/MiniTree.o
OBJS      += Root/UserFunktions.o
OBJS      += Root/KinematicUtils.o

OBJS_READ += $(OBJS)
OBJS_READ += Root/EventCount.o
OBJS_READ += Root/Analysis.o Root/AnaTtresSL.o Root/AnaTuDoSL.o Root/AnaTuDoTtresResolved.o Root/AnaTuDoTtresBoosted.o Root/HistogramService.o Root/AnaTtresQCD.o
OBJS_READ += util/read.o

OBJS_READTUDO += $(OBJS)
OBJS_READTUDO += Root/EventCount.o
OBJS_READTUDO += Root/Analysis.o Root/AnaTtresSL.o Root/AnaTuDoSL.o Root/AnaTuDoTtresResolved.o Root/AnaTuDoTtresBoosted.o Root/HistogramService.o
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


%.o: %.cxx
	g++ -c $(CXXFLAGS) -o $@ $<


all: read readTuDo

read: $(OBJS_READ)
	g++ $(CXXFLAGS) -o read $(OBJS_READ) $(LDFLAGS)
	
readTuDo: $(OBJS_READTUDO)
	g++ $(CXXFLAGS) -o readTuDo $(OBJS_READTUDO) $(LDFLAGS)
	
clean:
	rm -rf *.o read readTuDo Root/*.o util/*.o


