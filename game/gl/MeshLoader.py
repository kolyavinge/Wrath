import impasse
import numpy

from game.gl.Mesh import ChildMesh, Mesh
from game.gl.Texture import Texture


class MeshLoader:

    def load(self, objFilePath):
        resultMesh = Mesh()
        scene = impasse.load(objFilePath)
        for mesh in scene.meshes:
            childMesh = ChildMesh()
            childMesh.vertices = numpy.array(mesh.vertices, dtype=numpy.float32)
            childMesh.normals = numpy.array(mesh.normals, dtype=numpy.float32)
            childMesh.texCoords = numpy.array(mesh.texture_coords[0], dtype=numpy.float32)
            childMesh.faces = numpy.array(mesh.faces, dtype=numpy.uint32)
            childMesh.mainTexture = None
            resultMesh.addChild(childMesh)

        return resultMesh


def makeMeshLoader(resolver):
    return MeshLoader()
