import os

import impasse
import numpy
from impasse.constants import TextureSemantic

from game.gl.model3d.Model3d import *
from game.gl.TextureLoader import TextureLoader
from game.lib.Tree import Tree


class Model3dLoader:

    def __init__(self, textureLoader):
        self.textureLoader = textureLoader

    def load(self, modelFilePath):
        scene = impasse.load(modelFilePath)
        directoryName = os.path.dirname(modelFilePath)
        model3d = Model3d()
        self.loadMeshes(model3d, scene, directoryName)
        if len(scene.animations) > 0:
            meshesByNodesDictionary = self.getMeshesByNodesDictionary(model3d, scene)
            self.loadAnimations(model3d, scene, meshesByNodesDictionary)

        return model3d

    def loadMeshes(self, model3d, scene, directoryName):
        for mesh in scene.meshes:
            modelMesh = Mesh()
            modelMesh.name = mesh.name
            modelMesh.vertices = numpy.array(mesh.vertices, dtype=numpy.float32)
            modelMesh.normals = numpy.array(mesh.normals, dtype=numpy.float32)
            modelMesh.texCoords = numpy.array(mesh.texture_coords[0], dtype=numpy.float32)
            modelMesh.faces = numpy.array(mesh.faces, dtype=numpy.uint32)
            texFile = self.getDiffuseTextureFileName(mesh.material)
            modelMesh.texture = self.textureLoader.load(f"{directoryName}\\{texFile}")
            model3d.meshes.append(modelMesh)

    def loadAnimations(self, model3d, scene, meshesByNodesDictionary):
        model3d.hasAnimations = True
        model3d.animations = []
        for animation in scene.animations:
            modelAnimation = Animation(animation.name, animation.duration, animation.ticks_per_second)
            for channel in animation.channels:
                modelChannel = Channel()
                modelChannel.meshes = meshesByNodesDictionary[channel.node_name]
                modelChannel.translations = [Frame(frame.time, frame.value) for frame in channel.position_keys]
                modelChannel.rotations = [Frame(frame.time, frame.value) for frame in channel.rotation_keys]
                modelChannel.scales = [Frame(frame.time, frame.value) for frame in channel.scaling_keys]
                modelAnimation.channels.append(modelChannel)
            model3d.animations.append(modelAnimation)

        return model3d

    def getMeshesByNodesDictionary(self, model3d, scene):
        modelMeshDictionary = dict([(mesh.name, mesh) for mesh in model3d.meshes])
        nodesDictionary = self.getNodesDictionary(scene.root_node)
        meshesByNodesDictionary = {}
        for nodeName, meshNames in nodesDictionary.items():
            nodeMeshes = [modelMeshDictionary[meshName] for meshName in meshNames]
            meshesByNodesDictionary[nodeName] = nodeMeshes

        return meshesByNodesDictionary

    def getNodesDictionary(self, rootNode):
        nodes = Tree.flattenToList(rootNode, lambda parent: parent.children)
        nodesDictionary = dict([(node.name, set()) for node in nodes])
        for node in nodes:
            for mesh in node.meshes:
                nodesDictionary[node.name].add(mesh.name)
                for bone in mesh.bones:
                    nodesDictionary[bone.name].add(mesh.name)

        return nodesDictionary

    def getDiffuseTextureFileName(self, material):
        for key, value in material.items():
            name, kind = key
            if name == "$tex.file" and kind == TextureSemantic.DIFFUSE:
                return value

        raise Exception(f"No texture found for mesh.")


def makeModel3dLoader(resolver):
    return Model3dLoader(resolver.resolve(TextureLoader))
