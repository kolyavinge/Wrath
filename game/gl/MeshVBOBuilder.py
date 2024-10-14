from OpenGL.GL import *

from game.gl.VBO import VBO


class MeshVBOBuilder:

    def __init__(self, adjacencyFormatConverter):
        self.adjacencyFormatConverter = adjacencyFormatConverter

    def build(self, mesh, withAdjacency=False):
        result = []

        vaoIdList = glGenVertexArrays(len(mesh.children))

        for index, childMesh in enumerate(mesh.children):
            vaoId = vaoIdList[index]
            glBindVertexArray(vaoId)

            if withAdjacency:
                childMesh.faces = self.adjacencyFormatConverter.getFacesWithAdjacency(childMesh.faces)

            vboIds = glGenBuffers(4)

            glBindBuffer(GL_ARRAY_BUFFER, vboIds[0])
            glBufferData(GL_ARRAY_BUFFER, childMesh.vertices.nbytes, childMesh.vertices, GL_STATIC_DRAW)
            glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

            glBindBuffer(GL_ARRAY_BUFFER, vboIds[1])
            glBufferData(GL_ARRAY_BUFFER, childMesh.normals.nbytes, childMesh.normals, GL_STATIC_DRAW)
            glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

            glBindBuffer(GL_ARRAY_BUFFER, vboIds[2])
            glBufferData(GL_ARRAY_BUFFER, childMesh.texCoords.nbytes, childMesh.texCoords, GL_STATIC_DRAW)
            glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 0, None)

            glEnableVertexAttribArray(0)
            glEnableVertexAttribArray(1)
            glEnableVertexAttribArray(2)

            glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, vboIds[3])
            glBufferData(GL_ELEMENT_ARRAY_BUFFER, childMesh.faces.nbytes, childMesh.faces, GL_STATIC_DRAW)

            glBindBuffer(GL_ARRAY_BUFFER, 0)
            glBindVertexArray(0)

            format = GL_TRIANGLES if not withAdjacency else GL_TRIANGLES_ADJACENCY

            vbo = VBO(vaoId, vboIds, 3 * len(childMesh.faces), format)
            result.append((childMesh, vbo))

        return result
