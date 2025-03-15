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
        scene = impasse.load(modelFilePath)
        directoryName = os.path.dirname(modelFilePath)
        model3d = Model3d()
        self.loadMeshes(model3d, scene, directoryName)
        if len(scene.animations) > 0:
            self.animationLoader.loadAnimations(model3d, scene)

        return model3d

    def loadMeshes(self, model3d, scene, directoryName):
        for mesh in scene.meshes:
            modelMesh = Mesh()
            modelMesh.name = mesh.name
            modelMesh.vertices = numpy.array(mesh.vertices, dtype=numpy.float32)
            modelMesh.normals = numpy.array(mesh.normals, dtype=numpy.float32)
            modelMesh.texCoords = numpy.array(mesh.texture_coords[0], dtype=numpy.float32)
            modelMesh.faces = numpy.array(mesh.faces, dtype=numpy.uint32)
            texFile = self.getDiffuseTextureFileNameOrNone(mesh.material)
            if texFile is not None:
                modelMesh.texture = self.textureLoader.load(f"{directoryName}\\{texFile}")
            else:
                modelMesh.texture = self.textureCollection.blank
            model3d.meshes.append(modelMesh)

    def getDiffuseTextureFileNameOrNone(self, material):
        for key, value in material.items():
            name, kind = key
            if name == "$tex.file" and kind == TextureSemantic.DIFFUSE:
                return value

        return None


def makeModel3dLoader(resolver):
    return Model3dLoader(resolver.resolve(TextureLoader), resolver.resolve(TextureCollection), resolver.resolve(AnimationLoader))
