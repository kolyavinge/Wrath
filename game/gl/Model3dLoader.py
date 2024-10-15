import os

import impasse
import numpy
from impasse.constants import TextureSemantic

from game.gl.Model3d import Mesh, Model3d
from game.gl.TextureLoader import TextureLoader


class Model3dLoader:

    def __init__(self, textureLoader):
        self.textureLoader = textureLoader

    def load(self, objFilePath):
        model3d = Model3d()
        directoryName = os.path.dirname(objFilePath)
        scene = impasse.load(objFilePath)

        for mesh in scene.meshes:
            modelMesh = Mesh()
            modelMesh.vertices = numpy.array(mesh.vertices, dtype=numpy.float32)
            modelMesh.normals = numpy.array(mesh.normals, dtype=numpy.float32)
            modelMesh.texCoords = numpy.array(mesh.texture_coords[0], dtype=numpy.float32)
            modelMesh.faces = numpy.array(mesh.faces, dtype=numpy.uint32)
            texFile = self.getDiffuseTextureFileName(mesh.material)
            modelMesh.texture = self.textureLoader.load(f"{directoryName}\\{texFile}")
            model3d.addMesh(modelMesh)

        return model3d

    def getDiffuseTextureFileName(self, material):
        for key, value in material.items():
            name, kind = key
            if name == "$tex.file" and kind == TextureSemantic.DIFFUSE:
                return value

        raise Exception(f"No texture for mesh.")


def makeModel3dLoader(resolver):
    return Model3dLoader(resolver.resolve(TextureLoader))
