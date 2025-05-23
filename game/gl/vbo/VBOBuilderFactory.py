from game.gl.AdjacencyFormatConverter import AdjacencyFormatConverter
from game.gl.model3d.Model3dVBOBuilder import Model3dVBOBuilder
from game.gl.vbo.VBOBuilder import VBOBuilder


class VBOBuilderFactory:

    def __init__(self, adjacencyFormatConverter: AdjacencyFormatConverter):
        self.adjacencyFormatConverter = adjacencyFormatConverter

    def makeVBOBuilder(self):
        return VBOBuilder(self.adjacencyFormatConverter)

    def makeModel3dVBOBuilder(self):
        return Model3dVBOBuilder(self.adjacencyFormatConverter)
