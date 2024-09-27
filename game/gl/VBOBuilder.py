import numpy
from OpenGL.GL import *

from game.gl.VBO import VBO


class VBOBuilder:

    def __init__(self, adjacencyFormatConverter):
        self.vertices = []
        self.vertexCount = 0
        self.normals = []
        self.texCoords = []
        self.faces = []
        self.adjacencyFormatConverter = adjacencyFormatConverter

    def getVertexCount(self):
        return self.vertexCount

    def addVertex(self, vector):
        self.vertices.append(vector.x)
        self.vertices.append(vector.y)
        self.vertices.append(vector.z)
        self.vertexCount += 1

    def addNormal(self, vector):
        self.normals.append(vector.x)
        self.normals.append(vector.y)
        self.normals.append(vector.z)

    def addTexCoord(self, x, y):
        self.texCoords.append(x)
        self.texCoords.append(y)

    def addFace(self, i1, i2, i3):
        self.faces.append(i1)
        self.faces.append(i2)
        self.faces.append(i3)

    def validate(self):
        # if len(self.vertices) == 0: TODO
        # raise Exception("Vertices cannot be empty.")
        if len(self.vertices) != len(self.normals):
            raise Exception("Vertices and normals must be the same length.")
        # if len(self.faces) == 0:
        # raise Exception("Faces cannot be empty.")

    def build(self, withAdjacency=False):
        self.validate()

        # https://www.patternsgameprog.com/opengl-2d-facade-3-vertex-array-objects
        vaoId = glGenVertexArrays(1)
        glBindVertexArray(vaoId)

        if withAdjacency:
            self.faces = self.adjacencyFormatConverter.getFacesWithAdjacency(self.faces)

        vertices = numpy.array(self.vertices, dtype=numpy.float32)
        normals = numpy.array(self.normals, dtype=numpy.float32)
        texCoords = numpy.array(self.texCoords, dtype=numpy.float32)
        faces = numpy.array(self.faces, dtype=numpy.uint32)

        vboIds = glGenBuffers(4)

        glBindBuffer(GL_ARRAY_BUFFER, vboIds[0])
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

        glBindBuffer(GL_ARRAY_BUFFER, vboIds[1])
        glBufferData(GL_ARRAY_BUFFER, normals.nbytes, normals, GL_STATIC_DRAW)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

        glBindBuffer(GL_ARRAY_BUFFER, vboIds[2])
        glBufferData(GL_ARRAY_BUFFER, texCoords.nbytes, texCoords, GL_STATIC_DRAW)
        glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 0, None)

        glEnableVertexAttribArray(0)
        glEnableVertexAttribArray(1)
        glEnableVertexAttribArray(2)

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, vboIds[3])
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, faces.nbytes, faces, GL_STATIC_DRAW)

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

        format = GL_TRIANGLES if not withAdjacency else GL_TRIANGLES_ADJACENCY
        return VBO(vaoId, vboIds, len(faces), format)
