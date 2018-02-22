# CMakeLists.txt for event package. It creates a library with dictionary and a main program
cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
# Find source files
file(GLOB SOURCES        ### Core ###
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
                         ### pyHistogram Only ###
                         ## Wrapper ##
                         Root/DMWeight.cxx
                         Root/wrapper.cxx
                         )

file(GLOB EFTLIB_SOURCES Root/EFTLib.cxx
                         Root/HelAmps_TopEffTh.cxx
                         Root/Parameters_TopEffTh.cxx
                         Root/Parameters_sm.cxx
                         Root/read_slha.cxx
                         Root/HelAmps_TopEffTh.cxx
                         Root/HelAmps_sm.cxx)
list(APPEND SOURCES ${EFTLIB_SOURCES})

add_definitions(-D ROOT_DIR="\\"${CMAKE_CURRENT_SOURCE_DIR}/\\"")

add_definitions(-Wno-ignored-qualifiers)
add_definitions(-Wno-unused-parameter)
add_definitions(-Wno-unused-variable)
add_definitions(-Wno-unused-but-set-variable)
#---Locate the ROOT package and defines a number of variables (e.g. ROOT_INCLUDE_DIRS)
if("$ENV{AtlasProject}" STREQUAL AnalysisTop)
    atlas_subdir( TopNtupleAnalysis )
    find_package(ROOT REQUIRED Minuit TreePlayer Physics Matrix LHAPDF)
    
    # Declare the package's dependencies:
    atlas_depends_on_subdirs(PUBLIC  TopDataPreparation
    	                             NNLOReweighter
    	                     PRIVATE Tools/PathResolver)
    # add_definitions(-D NNLOReweighter_NNLOReweighter_h)
    # Generate a CINT dictionary source file:
    atlas_add_root_dictionary( TopNtupleAnalysis _cintDictSource
                               ROOT_HEADERS TopNtupleAnalysis/wrapper.h Root/LinkDef.h
                               EXTERNAL_PACKAGES ROOT )

    # Build a library that other components can link against:
    atlas_add_library( TopNtupleAnalysis ${SOURCES} ${_cintDictSource} 
                       PUBLIC_HEADERS TopNtupleAnalysis
                       LINK_LIBRARIES NNLOReweighter ${ROOT_LIBRARIES}
                       PRIVATE_LINK_LIBRARIES PathResolver
                       INCLUDE_DIRS ${ROOT_INCLUDE_DIRS})

else()
    project(TopNtupleAnalysis)
    # You need to tell CMake where to find the ROOT installation. This can be done in a number of ways:
    #   - ROOT built with classic configure/make use the provided $ROOTSYS/etc/cmake/FindROOT.cmake
    #   - ROOT built with CMake. Add in CMAKE_PREFIX_PATH the installation prefix for ROOT
    list(APPEND CMAKE_PREFIX_PATH $ENV{ROOTSYS})
    # You need to download `TopDataPreparation` first
    list(APPEND SOURCES ${CMAKE_CURRENT_SOURCE_DIR}/../TopDataPreparation/Root/SampleXsection.cxx)
    find_package(ROOT REQUIRED Minuit TreePlayer Physics Matrix
                      OPTIONAL_COMPONENTS LHAPDF)
    if(NOT ROOT_LHAPDF_FOUND)
        add_definitions(-D NOEFT)
        message(AUTHOR_WARNING "LHAPDF is not found. EFTLib is not going to be built.")
    endif()
    #---Define useful ROOT functions and macros (e.g. ROOT_GENERATE_DICTIONARY)
    include(${ROOT_USE_FILE})

    include_directories(${CMAKE_CURRENT_SOURCE_DIR} ${ROOT_INCLUDE_DIRS} ${CMAKE_CURRENT_SOURCE_DIR}/../TopDataPreparation)
    add_definitions(${ROOT_CXX_FLAGS})
    ROOT_GENERATE_DICTIONARY(TopNtupleAnalysisCintDict TopNtupleAnalysis/wrapper.h LINKDEF Root/LinkDef.h MODULE TopNtupleAnalysis)

    #---Create a shared library with geneated dictionary
    add_library(TopNtupleAnalysis SHARED ${SOURCES} TopNtupleAnalysisCintDict)
    # set_target_properties(TopNtupleAnalysis PROPERTIES SUFFIX ".so")
    target_link_libraries(TopNtupleAnalysis ${ROOT_LIBRARIES})

    #---Create a main program using the library
    add_executable(read util/read.cxx)
    target_link_libraries(read TopNtupleAnalysis)
    add_executable(readTuDo util/readTuDo.cxx)
    target_link_libraries(readTuDo TopNtupleAnalysis)
    file(INSTALL pyHistograms DESTINATION . PATTERN '*')
    file(INSTALL share DESTINATION . PATTERN '*')
    file(INSTALL scripts DESTINATION . PATTERN '*.data')
endif()