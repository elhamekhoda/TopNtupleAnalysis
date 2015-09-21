
vpath %.cxx src
vpath %.h src

CXXFLAGS = -g $(shell root-config --cflags)
LDFLAGS  = $(shell root-config --libs) -lRooFit -lRooFitCore -lRooStats
LD       = g++
CC       = g++

SRC      = Fit.cxx eventdict.cxx ParseUtils.cxx Models.cxx FitUtils.cxx
OBJDIR   = obj
OBJS     = $(patsubst %.cxx,$(OBJDIR)/%.o,$(SRC))
DEPS     = Models.h FitUtils.h
PROGRAM  = Fit

SRC_FITSIGNAL      = FitSignal.cxx BaseSignalModel.cxx SignalModel.cxx eventdict.cxx ParseUtils.cxx Models.cxx FitUtils.cxx
OBJS_FITSIGNAL     = $(patsubst %.cxx,$(OBJDIR)/%.o,$(SRC_FITSIGNAL))

SRC_MAKEWORKSPACE  = MakeWorkspace.cxx BaseSignalModel.cxx SignalModel.cxx BkgModel.cxx eventdict.cxx ParseUtils.cxx Models.cxx FitUtils.cxx
OBJS_MAKEWORKSPACE = $(patsubst %.cxx,$(OBJDIR)/%.o,$(SRC_MAKEWORKSPACE))

SRC_SETLIMIT       = SetLimit.cxx BaseSignalModel.cxx SignalModel.cxx BkgModel.cxx eventdict.cxx ParseUtils.cxx Models.cxx FitUtils.cxx
OBJS_SETLIMIT      = $(patsubst %.cxx,$(OBJDIR)/%.o,$(SRC_SETLIMIT))

SRC_FITCOMBINED    = FitCombined.cxx BaseSignalModel.cxx SignalModel.cxx BkgModel.cxx eventdict.cxx ParseUtils.cxx Models.cxx FitUtils.cxx
OBJS_FITCOMBINED   = $(patsubst %.cxx,$(OBJDIR)/%.o,$(SRC_FITCOMBINED))

SRC_FITBKG         = FitBkg.cxx BaseSignalModel.cxx SignalModel.cxx BkgModel.cxx eventdict.cxx ParseUtils.cxx Models.cxx FitUtils.cxx
OBJS_FITBKG        = $(patsubst %.cxx,$(OBJDIR)/%.o,$(SRC_FITBKG))


all: $(PROGRAM) FitSignal MakeWorkspace SetLimit FitCombined FitBkg

$(OBJS): | obj

$(OBJDIR):
	@mkdir -p $@

$(OBJDIR)/%.o: %.cxx $(DEPS)
	$(CC) $(CXXFLAGS) -c -o $@ $<

$(PROGRAM): $(OBJS)
	$(LD) -o $(PROGRAM) $^ $(LDFLAGS)

FitSignal: $(OBJS_FITSIGNAL)
	$(LD) -o FitSignal $^ $(LDFLAGS)

MakeWorkspace: $(OBJS_MAKEWORKSPACE)
	$(LD) -o MakeWorkspace $^ $(LDFLAGS)

SetLimit: $(OBJS_SETLIMIT)
	$(LD) -o SetLimit $^ $(LDFLAGS)

FitCombined: $(OBJS_FITCOMBINED)
	$(LD) -o FitCombined $^ $(LDFLAGS)

FitBkg: $(OBJS_FITBKG)
	$(LD) -o FitBkg $^ $(LDFLAGS)

clean:
	rm -f *.o $(PROGRAM) FitSignal MakeWorkspace SetLimit FitBkg $(OBJDIR)/eventdict.cxx

$(OBJDIR)/eventdict.cxx: Models.h
	@echo "Generating dictionary ..."
	rootcint -f $(OBJDIR)/eventdict.cxx -c -p src/Models.h src/LinkDef.h
$(OBJDIR)/eventdict.o: $(OBJDIR)/eventdict.cxx
	$(CC) $(CXXFLAGS) -I. -c -o $(OBJDIR)/eventdict.o $(OBJDIR)/eventdict.cxx



