from OpenGL.GL import *

from game.gl.VBO import VBO


class Model3dVBOBuilder:

    def __init__(self, adjacencyFormatConverter):
        self.adjacencyFormatConverter = adjacencyFormatConverter

    def build(self, model3d, withAdjacency=False):
        result = []

        vaoIdList = glGenVertexArrays(len(model3d.meshes))
        if len(model3d.meshes) == 1:
            vaoIdList = [vaoIdList]

        for index, mesh in enumerate(model3d.meshes):
            vaoId = vaoIdList[index]
            glBindVertexArray(vaoId)

            if withAdjacency:
                mesh.faces = self.adjacencyFormatConverter.getFacesWithAdjacency(mesh.faces)

            vboIds = glGenBuffers(4)

            glBindBuffer(GL_ARRAY_BUFFER, vboIds[0])
            glBufferData(GL_ARRAY_BUFFER, mesh.vertices.nbytes, mesh.vertices, GL_STATIC_DRAW)
            glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

            glBindBuffer(GL_ARRAY_BUFFER, vboIds[1])
            glBufferData(GL_ARRAY_BUFFER, mesh.normals.nbytes, mesh.normals, GL_STATIC_DRAW)
            glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

            glBindBuffer(GL_ARRAY_BUFFER, vboIds[2])
            glBufferData(GL_ARRAY_BUFFER, mesh.texCoords.nbytes, mesh.texCoords, GL_STATIC_DRAW)
            glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 0, None)

            glEnableVertexAttribArray(0)
            glEnableVertexAttribArray(1)
            glEnableVertexAttribArray(2)

            glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, vboIds[3])
            glBufferData(GL_ELEMENT_ARRAY_BUFFER, mesh.faces.nbytes, mesh.faces, GL_STATIC_DRAW)

            glBindBuffer(GL_ARRAY_BUFFER, 0)
            glBindVertexArray(0)

            format = GL_TRIANGLES if not withAdjacency else GL_TRIANGLES_ADJACENCY

            vbo = VBO(vaoId, vboIds, 3 * len(mesh.faces), format)
            result.append((mesh, vbo))

        return result
