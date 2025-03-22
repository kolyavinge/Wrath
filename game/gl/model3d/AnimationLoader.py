# https://learnopengl.com/Guest-Articles/2020/Skeletal-Animation

import numpy

from game.calc.Quaternion import Quaternion
from game.calc.TransformMatrix4 import TransformMatrix4
from game.gl.model3d.Model3d import Animation, Bone, FrameTransformation, Node
from game.lib.Tree import Tree


class AnimationLoader:

    def __init__(self):
        pass

    def loadAnimations(self, model3d, aiScene):
        model3d.hasAnimations = True
        model3d.animations = {}
        bonesDictionary = self.getBonesDictionary(aiScene)
        self.setWeightsToMeshes(model3d, aiScene, bonesDictionary)
        rootNode = self.getRootNode(aiScene, bonesDictionary)
        self.readAnimations(model3d, aiScene, rootNode, bonesDictionary)

        return model3d

    def getBonesDictionary(self, aiScene):
        bones = {}
        boneId = 0
        for aiMesh in aiScene.meshes:
            for aiBone in aiMesh.bones:
                if aiBone.name not in bones:
                    bones[aiBone.name] = Bone(boneId, aiBone.name, TransformMatrix4.fromRowMajorFormat(aiBone.offsetmatrix))
                    boneId += 1

        return bones

    def setWeightsToMeshes(self, model3d, aiScene, bonesDictionary):
        for aiMesh in aiScene.meshes:
            mesh = model3d.meshes[aiMesh.id]
            bonesCount = Bone.maxBoneCountInfluence * len(mesh.vertices)
            mesh.boneIds = numpy.empty(bonesCount, dtype=numpy.int32)
            mesh.weights = numpy.empty(bonesCount, dtype=numpy.float32)
            mesh.boneIds.fill(-1)
            mesh.weights.fill(0.0)
            vertexWeightsCount = [0] * len(mesh.vertices)
            for aiBone in aiMesh.bones:
                bone = bonesDictionary[aiBone.name]
                for aiWeight in aiBone.weights:
                    weightIndex = Bone.maxBoneCountInfluence * aiWeight.vertexid + vertexWeightsCount[aiWeight.vertexid]
                    mesh.boneIds[weightIndex] = bone.id
                    mesh.weights[weightIndex] = aiWeight.weight
                    vertexWeightsCount[aiWeight.vertexid] += 1

    def getRootNode(self, aiScene, bonesDictionary):

        def readRec(aiNode, node):
            node.name = aiNode.name
            node.transformMatrix = TransformMatrix4.fromRowMajorFormat(aiNode.transformation)
            if node.name in bonesDictionary:
                node.bone = bonesDictionary[node.name]

            for aiChild in aiNode.children:
                child = Node()
                child.parent = node
                node.children.append(child)
                readRec(aiChild, child)

        rootNode = Node()
        readRec(aiScene.rootnode, rootNode)

        return rootNode

    def readAnimations(self, model3d, aiScene, rootNode, bonesDictionary):
        for aiAnimation in aiScene.animations:
            animation = Animation(aiAnimation.name, aiAnimation.duration, aiAnimation.tickspersecond, rootNode)
            for aiChannel in aiAnimation.channels:
                nodeName = aiChannel.nodename.data.decode("utf-8")
                if nodeName in bonesDictionary:
                    bone = bonesDictionary[nodeName]
                    bone.translations = list(self.getTranslations(aiChannel))
                    bone.rotations = list(self.getRotations(aiChannel))
                    bone.scales = list(self.getScales(aiChannel))
                else:
                    pass
            model3d.animations[animation.name] = animation

    def getTranslations(self, aiChannel):
        for aiFrame in aiChannel.positionkeys:
            transformMatrix = TransformMatrix4()
            transformMatrix.translate(aiFrame.mValue.x, aiFrame.mValue.y, aiFrame.mValue.z)
            yield FrameTransformation(aiFrame.time, transformMatrix)

    def getRotations(self, aiChannel):
        for aiFrame in aiChannel.rotationkeys:
            quat = Quaternion()
            quat.setComponents(aiFrame.mValue.w, aiFrame.mValue.x, aiFrame.mValue.y, aiFrame.mValue.z)
            if quat.w > 1.0:  # shitty data
                quat.w = 1.0
            elif quat.w < -1.0:
                quat.w = -1.0
            radians, pivot = quat.getAngleAndPivot()
            transformMatrix = TransformMatrix4()
            transformMatrix.rotate(radians, pivot)
            yield FrameTransformation(aiFrame.time, transformMatrix)

    def getScales(self, aiChannel):
        for aiFrame in aiChannel.scalingkeys:
            transformMatrix = TransformMatrix4()
            transformMatrix.scale(aiFrame.mValue.x, aiFrame.mValue.y, aiFrame.mValue.z)
            yield FrameTransformation(aiFrame.time, transformMatrix)


def makeAnimationLoader(resolver):
    return AnimationLoader()
