import numpy
import pyassimp
from pyassimp import postprocess

from game.gl.model3d.AnimationLoader import AnimationLoader
from game.gl.model3d.Model3d import Mesh, Model3d
from game.gl.TextureLoader import TextureLoader
from game.lib.FileSystem import FileSystem
from game.lib.Query import Query
from game.lib.Stopwatch import Stopwatch
from game.render.common.TextureCollection import TextureCollection


class Model3dLoader:

    def __init__(
        self,
        textureLoader: TextureLoader,
        textureCollection: TextureCollection,
        animationLoader: AnimationLoader,
        fileSystem: FileSystem,
    ):
        self.textureLoader = textureLoader
        self.textureCollection = textureCollection
        self.animationLoader = animationLoader
        self.fileSystem = fileSystem

    def load(self, modelFilePath):
        directoryName = self.fileSystem.getDirectoryName(modelFilePath)
        loadSw = Stopwatch()
        loadSw.start()
        with pyassimp.load(modelFilePath, processing=postprocess.aiProcess_Triangulate | postprocess.aiProcess_LimitBoneWeights) as aiScene:
            loadSw.stop()
            procSw = Stopwatch()
            procSw.start()
            model3d = Model3d()
            textures = self.getTextures(directoryName)
            self.loadMeshes(model3d, aiScene, textures, directoryName)
            if len(aiScene.animations) > 0:
                self.animationLoader.loadAnimations(model3d, aiScene)
            procSw.stop()

        print(f"Load model {modelFilePath} {loadSw.elapsed:.8f} (process {procSw.elapsed:.8f}).")

        return model3d

    def getTextures(self, directoryName):
        textures = {}
        imageFiles = self.fileSystem.findFilesByExtension(directoryName, ".jpg")
        for imageFile in imageFiles:
            textures[imageFile] = self.textureLoader.load(imageFile)

        return textures

    def loadMeshes(self, model3d, aiScene, textures, directoryName):
        meshId = 0
        for aiMesh in aiScene.meshes:
            mesh = Mesh()
            aiMesh.id = meshId
            mesh.id = meshId
            mesh.vertices = numpy.array(aiMesh.vertices, dtype=numpy.float32).flatten()
            mesh.normals = numpy.array(aiMesh.normals, dtype=numpy.float32).flatten()
            mesh.texCoords = numpy.array(aiMesh.texturecoords[0], dtype=numpy.float32).flatten()
            mesh.faces = numpy.array(aiMesh.faces, dtype=numpy.uint32).flatten()
            mesh.texture = self.getDiffuseTexture(aiMesh.material, textures, directoryName)
            model3d.meshes.append(mesh)
            meshId += 1

    def getDiffuseTexture(self, material, textures, directoryName):
        if len(textures) == 1:
            return Query(textures.values()).first()

        for key, value in material.properties.items():
            if key == "name":
                fileName = f"{directoryName}\\{value}_BaseColor.jpg"
                if fileName in textures:
                    return textures[fileName]

            if key == "file":
                fileName = f"{directoryName}\\{value}"
                return textures[fileName]

        return self.textureCollection.blank
