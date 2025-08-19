import numpy

from game.external.gameexlib import gameexlib


class AdjacencyFormatConverter:

    def __init__(self):
        self.maxUint32 = numpy.iinfo(numpy.uint32).max

    def getFacesWithAdjacency(self, faces):
        faces = numpy.array(faces, dtype=numpy.uint32)
        maxUint32 = numpy.iinfo(numpy.uint32).max
        result = numpy.full(2 * len(faces), maxUint32, dtype=numpy.uint32)

        gameexlib.convertFacesToAdjacencyFormat(len(faces), faces, result)

        return result
