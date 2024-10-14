import os

import impasse
import numpy
from impasse.constants import TextureSemantic

from game.gl.Mesh import ChildMesh, Mesh
from game.gl.TextureLoader import TextureLoader


class MeshLoader:

    def __init__(self, textureLoader):
        self.textureLoader = textureLoader

    def load(self, objFilePath):
        resultMesh = Mesh()
        scene = impasse.load(objFilePath)
        directoryName = os.path.dirname(objFilePath)

        for mesh in scene.meshes:
            childMesh = ChildMesh()
            childMesh.vertices = numpy.array(mesh.vertices, dtype=numpy.float32)
            childMesh.normals = numpy.array(mesh.normals, dtype=numpy.float32)
            childMesh.texCoords = numpy.array(mesh.texture_coords[0], dtype=numpy.float32)
            childMesh.faces = numpy.array(mesh.faces, dtype=numpy.uint32)
            texFile = self.getDiffuseTextureFileName(mesh.material)
            childMesh.texture = self.textureLoader.load(f"{directoryName}\\{texFile}")
            resultMesh.addChild(childMesh)

        return resultMesh

    def getDiffuseTextureFileName(self, material):
        for key, value in material.items():
            name, kind = key
            if name == "$tex.file" and kind == TextureSemantic.DIFFUSE:
                return value

        raise Exception(f"No texture for mesh.")


def makeMeshLoader(resolver):
    return MeshLoader(resolver.resolve(TextureLoader))
