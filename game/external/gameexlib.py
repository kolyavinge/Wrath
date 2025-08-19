import ctypes
import glob

import numpy

from game.lib.Environment import Environment

libfile = glob.glob(f"{Environment.programRootPath}\game\external\gameexlib.dll")[0]
gameexlib = ctypes.CDLL(libfile)
gameexlib.convertFacesToAdjacencyFormat.restype = ctypes.c_void_p
gameexlib.convertFacesToAdjacencyFormat.argtypes = [
    ctypes.c_int,
    numpy.ctypeslib.ndpointer(dtype=numpy.uint32),
    numpy.ctypeslib.ndpointer(dtype=numpy.uint32),
]
