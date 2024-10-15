from game.gl.AdjancencyFormatConverter import AdjacencyFormatConverter
from game.gl.Model3dVBOBuilder import Model3dVBOBuilder
from game.gl.VBOBuilder import VBOBuilder


class VBOBuilderFactory:

    def __init__(self, adjacencyFormatConverter):
        self.adjacencyFormatConverter = adjacencyFormatConverter

    def makeVBOBuilder(self):
        return VBOBuilder(self.adjacencyFormatConverter)

    def makeModel3dVBOBuilder(self):
        return Model3dVBOBuilder(self.adjacencyFormatConverter)


def makeVBOBuilderFactory(resolver):
    return VBOBuilderFactory(resolver.resolve(AdjacencyFormatConverter))
