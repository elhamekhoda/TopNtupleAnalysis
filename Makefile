
ROOTCFLAGS    = $(shell root-config --cflags)

MYCF=""

ifneq ($(findstring m32,$(ROOTCFLAGS)),)
        MYCF= CXXFLAGS=-m32 CFLAGS=-m32
endif

ROOTLIB    = $(shell root-config --libs) -lMinuit

CXXFLAGS   = -g -I.
CXXFLAGS  += -Wno-long-long -fPIC
CXXFLAGS  += $(shell root-config --cflags)

LDFLAGS    =
LDFLAGS   += $(ROOTLIB) -lCintex

OBJS       = Root/Event.o Root/LargeJet.o Root/Muon.o Root/Electron.o Root/Jet.o Root/MObject.o
OBJS      += Root/ParseUtils.o
OBJS      += Root/MiniTree.o

OBJS_READ += $(OBJS)
OBJS_READ += Root/EventCount.o
OBJS_READ += Root/Analysis.o Root/AnaTtresSL.o Root/HistogramService.o
OBJS_READ += util/read.o

# can use RootCore, but keep like this to make it portable
#OBJS_READ += TopDataPreparation/Root/SampleXsection.o
OBJS_READ += ../TopDataPreparation/Root/SampleXsection.o
CXXFLAGS += -I../RootCoreBin/include

OBJS_READ += Root/TtresChi2.o Root/TtresdRmin.o Root/TtresNeutrinoBuilder.o

%.o: %.cxx
	g++ -c $(CXXFLAGS) -o $@ $<


all: read

read: $(OBJS_READ)
	g++ $(CXXFLAGS) -o read $(OBJS_READ) $(LDFLAGS)
clean:
	rm -rf *.o read Root/*.o util/*.o


