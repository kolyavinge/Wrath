from game.gl.VBOBuilder import VBOBuilder


class ExtVBOBuilder(VBOBuilder):

    def __init__(self, adjacencyFormatConverter):
        super().__init__(adjacencyFormatConverter)

    def addMesh(self, mesh):
        for vertex in mesh.vertices:
            self.addVertex(vertex.x, vertex.y, vertex.z)

        for normal in mesh.normals:
            self.addNormal(normal.x, normal.y, normal.z)

        for texCoord in mesh.texCoords:
            self.addTexCoord(texCoord.x, texCoord.y)

        for face in mesh.faces:
            self.addFace(face.i1, face.i2, face.i3)
