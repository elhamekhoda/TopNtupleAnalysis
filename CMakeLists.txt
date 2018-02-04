# CMakeLists.txt for event package. It creates a library with dictionary and a main program
cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
project(TopNtupleAnalysis)

# You need to tell CMake where to find the ROOT installation. This can be done in a number of ways:
#   - ROOT built with classic configure/make use the provided $ROOTSYS/etc/cmake/FindROOT.cmake
#   - ROOT built with CMake. Add in CMAKE_PREFIX_PATH the installation prefix for ROOT
list(APPEND CMAKE_PREFIX_PATH $ENV{ROOTSYS})

#---Locate the ROOT package and defines a number of variables (e.g. ROOT_INCLUDE_DIRS)
find_package(ROOT REQUIRED COMPONENTS Minuit TreePlayer)

#---Define useful ROOT functions and macros (e.g. ROOT_GENERATE_DICTIONARY)
include(${ROOT_USE_FILE})

# Find source files
file(GLOB SOURCES   ../TopDataPreparation/Root/SampleXsection.cxx
                    Root/AnaTtresMM.cxx
                    Root/AnaTtresQCD.cxx
                    Root/AnaTtresSB.cxx
                    Root/AnaTtresSL.cxx
                    Root/AnaTtresSLMtt.cxx
                    Root/AnaTtresWJ.cxx
                    Root/AnaTuDoSL.cxx
                    Root/AnaTuDoTtresBoosted.cxx
                    Root/AnaTuDoTtresResolved.cxx
                    Root/Analysis.cxx
                    Root/Electron.cxx
                    Root/Event.cxx
                    Root/EventCount.cxx
                    Root/HistogramService.cxx
                    Root/Jet.cxx
                    Root/KinematicUtils.cxx
                    Root/LargeJet.cxx
                    Root/MMUtils.cxx
                    Root/MObject.cxx
                    Root/MiniTree.cxx
                    Root/Muon.cxx
                    Root/ParseUtils.cxx
                    Root/TtresChi2.cxx
                    Root/TtresNeutrinoBuilder.cxx
                    Root/TtresdRmin.cxx
                    Root/UserFunktions.cxx
                    Root/WeakCorrScaleFactorParam.cxx
                    ## pyHistogram Only
                    # Root/EFTLib.cxx
                    Root/wrapper.cxx
                    Root/DMWeight.C)

include_directories(${CMAKE_CURRENT_SOURCE_DIR} ${ROOT_INCLUDE_DIRS} ../TopDataPreparation)
add_definitions(${ROOT_CXX_FLAGS})
ROOT_GENERATE_DICTIONARY(G__TopNtupleAnalysis TopNtupleAnalysis/wrapper.h LINKDEF LinkDef.h)

#---Create a shared library with geneated dictionary
add_library(TopNtupleAnalysis SHARED ${SOURCES} G__TopNtupleAnalysis.cxx)
set_target_properties(TopNtupleAnalysis PROPERTIES SUFFIX ".so")
target_link_libraries(TopNtupleAnalysis ${ROOT_LIBRARIES})

#---Create a main program using the library
add_executable(read util/read.cxx)
target_link_libraries(read TopNtupleAnalysis)
add_executable(readTuDo util/readTuDo.cxx)
target_link_libraries(readTuDo TopNtupleAnalysis)