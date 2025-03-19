# https://learnopengl.com/Guest-Articles/2020/Skeletal-Animation

import numpy

from game.calc.Quaternion import Quaternion
from game.calc.TransformMatrix4 import TransformMatrix4
from game.calc.TransformMatrix4Builder import TransformMatrix4Builder
from game.gl.model3d.Model3d import *
from game.lib.Tree import Tree


class AnimationLoader:

    def __init__(self):
        pass

    def loadAnimations(self, model3d, aiScene):
        model3d.hasAnimations = True
        model3d.animations = {}
        bones = self.getBonesDictionary(aiScene)
        self.setWeightsToMeshes(aiScene, model3d, bones)
        for aiAnimation in aiScene.animations:
            animation = Animation(aiAnimation.name, aiAnimation.duration, aiAnimation.tickspersecond)
            for aiChannel in aiAnimation.channels:
                channel = Channel()
                # channel.meshes = meshesByNodesDictionary[aiChannel.node_name]
                channel.translations = [Frame(aiFrame.time, aiFrame.value) for aiFrame in aiChannel.positionkeys]
                channel.rotations = [Frame(aiFrame.time, aiFrame.value) for aiFrame in aiChannel.rotationkeys]
                channel.scales = [Frame(aiFrame.time, aiFrame.value) for aiFrame in aiChannel.scalingkeys]
                # animation.channels.append(channel)
            model3d.animations[animation.name] = animation

        return model3d

    def setWeightsToMeshes(self, aiScene, model3d, bones):
        meshDictionary = dict([(mesh.name, mesh) for mesh in model3d.meshes])
        for aiMesh in aiScene.meshes:
            mesh = meshDictionary[aiMesh.name]
            mesh.boneIds = numpy.empty(4 * len(mesh.vertices), dtype=numpy.int32)
            mesh.weights = numpy.empty(4 * len(mesh.vertices), dtype=numpy.float32)
            mesh.boneIds.fill(-1)
            mesh.weights.fill(0.0)
            for aiBone in aiMesh.bones:
                bone = bones[aiBone.name]

    def getBonesDictionary(self, aiScene):
        bones = {}
        boneId = 0
        for aiMesh in aiScene.meshes:
            for aiBone in aiMesh.bones:
                if aiBone.name not in bones:
                    bones[aiBone.name] = Bone(boneId, aiBone.name, TransformMatrix4.fromRowMajorFormat(aiBone.offsetmatrix))
                    boneId += 1

        return bones

    def getMeshesByNodesDictionary(self, model3d, aiScene):
        modelMeshDictionary = dict([(mesh.name, mesh) for mesh in model3d.meshes])
        aiNodesDictionary = self.getAiNodesDictionary(aiScene.root_node)
        meshesByNodesDictionary = {}
        for nodeName, meshNames in aiNodesDictionary.items():
            nodeMeshes = [modelMeshDictionary[meshName] for meshName in meshNames]
            meshesByNodesDictionary[nodeName] = nodeMeshes

        return meshesByNodesDictionary

    def getAiNodesDictionary(self, rootNode):
        aiNodes = Tree.flattenToList(rootNode, lambda parent: parent.children)
        nodesDictionary = dict([(aiNode.name, set()) for aiNode in aiNodes])
        for aiNode in aiNodes:
            for aiMesh in aiNode.meshes:
                nodesDictionary[aiNode.name].add(aiMesh.name)
                for aiBone in aiMesh.bones:
                    nodesDictionary[aiBone.name].add(aiMesh.name)

        return nodesDictionary


def makeAnimationLoader(resolver):
    return AnimationLoader()
