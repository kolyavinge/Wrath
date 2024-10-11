from game.gl.VBOBuilder import VBOBuilder


class ExtVBOBuilder(VBOBuilder):

    def __init__(self, adjacencyFormatConverter):
        super().__init__(adjacencyFormatConverter)

    def addMesh(self, mesh):
        for vertex in mesh.vertices:
            self.addVertex(vertex)

        for normal in mesh.normals:
            self.addNormal(normal)

        for texCoord in mesh.texCoords:
            self.addTexCoord(texCoord.x, texCoord.y)

        for face in mesh.faces:
            self.addFace(face.i1, face.i2, face.i3)
