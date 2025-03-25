from OpenGL.GL import *

from game.gl.BufferIndices import BufferIndices
from game.gl.model3d.Model3d import Bone
from game.gl.vbo.VBO import VBO


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

            if model3d.animations is not None:
                vboIds = glGenBuffers(6)
            else:
                vboIds = glGenBuffers(4)

            glBindBuffer(GL_ARRAY_BUFFER, vboIds[BufferIndices.vertices])
            glBufferData(GL_ARRAY_BUFFER, mesh.vertices.nbytes, mesh.vertices, GL_STATIC_DRAW)
            glVertexAttribPointer(BufferIndices.vertices, 3, GL_FLOAT, GL_FALSE, 0, None)
            glEnableVertexAttribArray(BufferIndices.vertices)

            glBindBuffer(GL_ARRAY_BUFFER, vboIds[BufferIndices.normals])
            glBufferData(GL_ARRAY_BUFFER, mesh.normals.nbytes, mesh.normals, GL_STATIC_DRAW)
            glVertexAttribPointer(BufferIndices.normals, 3, GL_FLOAT, GL_FALSE, 0, None)
            glEnableVertexAttribArray(BufferIndices.normals)

            glBindBuffer(GL_ARRAY_BUFFER, vboIds[BufferIndices.texCoords])
            glBufferData(GL_ARRAY_BUFFER, mesh.texCoords.nbytes, mesh.texCoords, GL_STATIC_DRAW)
            glVertexAttribPointer(BufferIndices.texCoords, 3, GL_FLOAT, GL_FALSE, 0, None)
            glEnableVertexAttribArray(BufferIndices.texCoords)

            glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, vboIds[BufferIndices.faces])
            glBufferData(GL_ELEMENT_ARRAY_BUFFER, mesh.faces.nbytes, mesh.faces, GL_STATIC_DRAW)

            if model3d.animations is not None:
                glBindBuffer(GL_ARRAY_BUFFER, vboIds[BufferIndices.boneIds])
                glBufferData(GL_ARRAY_BUFFER, mesh.boneIds.nbytes, mesh.boneIds, GL_STATIC_DRAW)
                glVertexAttribPointer(BufferIndices.boneIds, Bone.maxBonesCountInfluence, GL_INT, GL_FALSE, 0, None)
                glEnableVertexAttribArray(BufferIndices.boneIds)

                glBindBuffer(GL_ARRAY_BUFFER, vboIds[BufferIndices.weights])
                glBufferData(GL_ARRAY_BUFFER, mesh.weights.nbytes, mesh.weights, GL_STATIC_DRAW)
                glVertexAttribPointer(BufferIndices.weights, Bone.maxBonesCountInfluence, GL_FLOAT, GL_FALSE, 0, None)
                glEnableVertexAttribArray(BufferIndices.weights)

            glBindBuffer(GL_ARRAY_BUFFER, 0)
            glBindVertexArray(0)

            format = GL_TRIANGLES if not withAdjacency else GL_TRIANGLES_ADJACENCY

            vbo = VBO(vaoId, vboIds, 3 * len(mesh.faces), format)
            result.append((mesh, vbo))

        return result
