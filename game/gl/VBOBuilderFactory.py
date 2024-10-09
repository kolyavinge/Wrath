from game.gl.AdjancencyFormatConverter import AdjacencyFormatConverter
from game.gl.ExtVBOBuilder import ExtVBOBuilder
from game.gl.VBOBuilder import VBOBuilder


class VBOBuilderFactory:

    def __init__(self, adjacencyFormatConverter):
        self.adjacencyFormatConverter = adjacencyFormatConverter

    def makeVBOBuilder(self):
        return VBOBuilder(self.adjacencyFormatConverter)

    def makeExtVBOBuilder(self):
        return ExtVBOBuilder(self.adjacencyFormatConverter)


def makeVBOBuilderFactory(resolver):
    return VBOBuilderFactory(resolver.resolve(AdjacencyFormatConverter))
