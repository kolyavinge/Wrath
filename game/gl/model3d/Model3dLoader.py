import os

import impasse
import numpy
from impasse.constants import TextureSemantic

from game.gl.model3d.AnimationLoader import AnimationLoader
from game.gl.model3d.Model3d import Mesh, Model3d
from game.gl.TextureLoader import TextureLoader
from game.render.common.TextureCollection import TextureCollection


class Model3dLoader:

    def __init__(self, textureLoader, textureCollection, animationLoader):
        self.textureLoader = textureLoader
        self.textureCollection = textureCollection
        self.animationLoader = animationLoader

    def load(self, modelFilePath):
        aiScene = impasse.load(modelFilePath)
        directoryName = os.path.dirname(modelFilePath)
        model3d = Model3d()
        self.loadMeshes(model3d, aiScene, directoryName)
        if len(aiScene.animations) > 0:
            self.animationLoader.loadAnimations(model3d, aiScene)

        return model3d

    def loadMeshes(self, model3d, aiScene, directoryName):
        for aiMesh in aiScene.meshes:
            mesh = Mesh()
            mesh.name = aiMesh.name
            mesh.vertices = numpy.array(aiMesh.vertices, dtype=numpy.float32)
            mesh.normals = numpy.array(aiMesh.normals, dtype=numpy.float32)
            mesh.texCoords = numpy.array(aiMesh.texture_coords[0], dtype=numpy.float32)
            mesh.faces = numpy.array(aiMesh.faces, dtype=numpy.uint32)
            texFile = self.getDiffuseTextureFileNameOrNone(aiMesh.material)
            if texFile is not None:
                mesh.texture = self.textureLoader.load(f"{directoryName}\\{texFile}")
            else:
                mesh.texture = self.textureCollection.blank
            model3d.meshes.append(mesh)

    def getDiffuseTextureFileNameOrNone(self, material):
        for key, value in material.items():
            name, kind = key
            if name == "$tex.file" and kind == TextureSemantic.DIFFUSE:
                return value

        return None


def makeModel3dLoader(resolver):
    return Model3dLoader(resolver.resolve(TextureLoader), resolver.resolve(TextureCollection), resolver.resolve(AnimationLoader))
