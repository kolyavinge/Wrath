# https://learnopengl.com/Guest-Articles/2020/Skeletal-Animation

import numpy

from game.calc.Quaternion import Quaternion
from game.calc.TransformMatrix4 import TransformMatrix4
from game.gl.model3d.Model3d import Animation, Bone, Channel, Frame, Node
from game.lib.Numeric import Numeric
from game.lib.Tree import Tree


class AnimationLoader:

    def loadAnimations(self, model3d, aiScene):
        model3d.animations = {}
        bonesDictionary = self.getBonesDictionary(aiScene)
        if len(bonesDictionary) > Bone.maxBonesCount:
            raise Exception("Model has too many bones.")
        self.setWeightsToMeshes(model3d, aiScene, bonesDictionary)
        rootNode = self.getRootNode(aiScene, bonesDictionary)
        self.readAnimations(model3d, aiScene, rootNode, len(bonesDictionary))

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
            bonesCount = Bone.maxBonesCountInfluence * len(mesh.vertices)
            mesh.boneIds = numpy.empty(bonesCount, dtype=numpy.int32)
            mesh.weights = numpy.empty(bonesCount, dtype=numpy.float32)
            mesh.boneIds.fill(-1)
            mesh.weights.fill(0.0)
            vertexWeightsCount = [0] * len(mesh.vertices)
            for aiBone in aiMesh.bones:
                bone = bonesDictionary[aiBone.name]
                for aiWeight in aiBone.weights:
                    weightIndex = Bone.maxBonesCountInfluence * aiWeight.vertexid + vertexWeightsCount[aiWeight.vertexid]
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

    def readAnimations(self, model3d, aiScene, rootNode, allBonesCount):
        nodesDictionary = dict([(node.name, node) for node in Tree.flattenToList(rootNode, lambda n: n.children)])
        for aiAnimation in aiScene.animations:
            animation = Animation(aiAnimation.name, aiAnimation.duration, aiAnimation.tickspersecond, rootNode, allBonesCount)
            for aiChannel in aiAnimation.channels:
                nodeName = aiChannel.nodename.data.decode("utf-8")
                channel = Channel()
                channel.node = nodesDictionary[nodeName]
                channel.translationFrames = list(self.getTranslationFrames(aiChannel))
                channel.rotationFrames = list(self.getRotationFrames(aiChannel))
                channel.scaleFrames = list(self.getScaleFrames(aiChannel))
                animation.channels[nodeName] = channel
            model3d.animations[animation.name] = animation

    def getTranslationFrames(self, aiChannel):
        for aiFrame in aiChannel.positionkeys:
            transformMatrix = TransformMatrix4()
            transformMatrix.translate(aiFrame.mValue.x, aiFrame.mValue.y, aiFrame.mValue.z)
            yield Frame(aiFrame.time, transformMatrix)

    def getRotationFrames(self, aiChannel):
        for aiFrame in aiChannel.rotationkeys:
            quat = Quaternion()
            quat.setComponents(aiFrame.mValue.w, aiFrame.mValue.x, aiFrame.mValue.y, aiFrame.mValue.z)
            quat.w = Numeric.limitBy(quat.w, -1.0, 1.0)  # shitty data
            radians, axis = quat.getAngleAndAxis()
            transformMatrix = TransformMatrix4()
            transformMatrix.rotate(radians, axis)
            yield Frame(aiFrame.time, transformMatrix)

    def getScaleFrames(self, aiChannel):
        for aiFrame in aiChannel.scalingkeys:
            transformMatrix = TransformMatrix4()
            transformMatrix.scale(aiFrame.mValue.x, aiFrame.mValue.y, aiFrame.mValue.z)
            yield Frame(aiFrame.time, transformMatrix)


def makeAnimationLoader(resolver):
    return AnimationLoader()
