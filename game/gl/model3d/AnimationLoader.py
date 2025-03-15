# https://learnopengl.com/Guest-Articles/2020/Skeletal-Animation

from game.calc.Quaternion import Quaternion
from game.calc.TransformMatrix4 import TransformMatrix4
from game.calc.TransformMatrix4Builder import TransformMatrix4Builder
from game.gl.model3d.Model3d import *
from game.lib.Tree import Tree


class AnimationLoader:

    def __init__(self):
        pass

    def loadAnimations(self, model3d, scene):
        model3d.hasAnimations = True
        model3d.animations = {}
        meshesByNodesDictionary = self.getMeshesByNodesDictionary(model3d, scene)
        for animation in scene.animations:
            modelAnimation = Animation(animation.name, animation.duration, animation.ticks_per_second)
            for channel in animation.channels:
                modelChannel = Channel()
                modelChannel.meshes = meshesByNodesDictionary[channel.node_name]
                modelChannel.translations = [Frame(frame.time, frame.value) for frame in channel.position_keys]
                modelChannel.rotations = [Frame(frame.time, frame.value) for frame in channel.rotation_keys]
                modelChannel.scales = [Frame(frame.time, frame.value) for frame in channel.scaling_keys]
                modelAnimation.channels.append(modelChannel)
            model3d.animations[modelAnimation.name] = modelAnimation

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


def makeAnimationLoader(resolver):
    return AnimationLoader()
