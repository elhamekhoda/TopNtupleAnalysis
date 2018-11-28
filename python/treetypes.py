"""
Wrappers for basic types that are compatible with ROOT TTrees

Copyright (c) 2012-2017, The rootpy developers
All rights reserved.
"""
import re
import sys
import array
from ROOT import vector, AddressOf
if sys.version_info[0] >= 3:
    long = int

registered = {}

# ROOT type codes:
root_type_codes = [
"O", #       a boolean (Bool_t) (see note 1)
"B", #       an 8 bit signed integer (Char_t)
"b", #       an 8 bit unsigned integer (UChar_t)
"S", #       a 16 bit signed integer (Short_t)
"s", #       a 16 bit unsigned integer (UShort_t)
"I", #       a 32 bit signed integer (Int_t)
"i", #       a 32 bit unsigned integer (UInt_t)
"L", #       a 64 bit signed integer (Long64_t)
"l", #       a 64 bit unsigned integer (ULong64_t)
"F", #       a 32 bit floating point (Float_t)
"D"  #       a 64 bit floating point (Double_t)\
]

# ROOT type names:
root_type_names = [
"Bool_t",
"Char_t",
"UChar_t",
"Short_t",
"UShort_t",
"Int_t",
"UInt_t",
"Long64_t",
"ULong64_t",
"Float_t",
"Double_t",
]

# Python array:
python_codes = [
"B", #       unsigned char   int                 1 (used as boolean)
"b", #       signed char     int                 1
"B", #       unsigned char   int                 1
"h", #       signed short    int                 2
"H", #       unsigned short  int                 2
"i", #       signed int      int                 2
"I", #       unsigned int    long                2
"l", #       signed long     int                 4
"L", #       unsigned long   long                4
"f", #       float           float               4
"d"  #       double          float               8\
]

# ctypes:
cpp_codes = [
"unsigned",
"signed",
"unsigned",
"signed",
"unsigned",
"signed",
"unsigned",
"signed",
"unsigned",
"float",
"double"
]

# Python NumPy array:
numpy_codes = [
"b", #       Boolean
"i1", #      Char
"u1", #      Unsigned Char
"i2", #      Short Integer
"u2", #      Unsigned Short integer
"i4", #      Integer
"u4", #      Unsigned integer
"i8", #      Long Integer
"u8", #      Unsigned Long integer
"f4", #      Floating point
"f8"  #      Double Floating point\
]


def convert(origin, target, type):
    """
    convert type from origin to target
    origin/target must be ROOTCODE, ROOTNAME, ARRAY, or NUMPY
    """
    _origin = origin.upper()
    if _origin == 'ROOTCODE':
        _origin = root_type_codes
    elif _origin == 'ROOTNAME':
        _origin = root_type_names
    elif _origin == 'ARRAY':
        _origin = python_codes
    elif _origin == 'NUMPY':
        _origin = numpy_codes
    elif _origin == "CPP":
        _origin = cpp_codes
    else:
        raise ValueError("{0} is not a valid type".format(origin))

    _target = target.upper()
    if _target == 'ROOTCODE':
        _target = root_type_codes
    elif _target == 'ROOTNAME':
        _target = root_type_names
    elif _target == 'ARRAY':
        _target = python_codes
    elif _target == 'NUMPY':
        _target = numpy_codes
    elif _target == "CPP":
        _target = cpp_codes
    else:
        raise ValueError("{0} is not a valid type".format(target))

    if type not in _origin:
        raise ValueError("{0} is not a valid {1} type".format(type, origin))

    return _target[_origin.index(type)]

prog_isvector = re.compile(r'vector<(.*)>')
def convert_branchtype(branch, set_address = True, register = True):
    if branch in registered:
        ptr = registered[branch]
    else:
        print 'New Branch! >>>>>>', branch
        branch_type = branch.GetListOfLeaves().At(0).GetTypeName()
        isvector = prog_isvector.match(branch_type)
        if not isvector:
            ptr = array.array(convert('ROOTNAME', 'ARRAY', branch_type), [0])
            branch.SetAddress(ptr)
        else:
            ptr = vector(isvector.group(1))()
            branch.SetAddress(AddressOf(ptr))
        if register:
            registered[branch] = ptr
    return ptr
