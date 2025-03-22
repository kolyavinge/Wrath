class FrameTransformation:

    def __init__(self, time, transformMatrix):
        self.time = time
        self.transformMatrix = transformMatrix


class Bone:

    maxBoneCountInfluence = 4

    def __init__(self, id, name, offsetMatrix):
        self.id = id
        self.name = name
        self.offsetMatrix = offsetMatrix
        self.translations = []
        self.rotations = []
        self.scales = []


class Node:

    def __init__(self):
        self.name = ""
        self.parent = None
        self.children = []
        self.transformMatrix = None
        self.bone = None


class Animation:

    def __init__(self, name, duration, ticksPerSecond, rootNode):
        self.name = name
        self.duration = duration
        self.ticksPerSecond = ticksPerSecond
        self.rootNode = rootNode


class Mesh:

    def __init__(self):
        self.id = 0
        self.vertices = []
        self.normals = []
        self.texCoords = []
        self.faces = []
        self.texture = None


class Model3d:

    def __init__(self):
        self.meshes = []
        self.hasAnimations = False

    def setScale(self, scale):
        for mesh in self.meshes:
            mesh.vertices *= scale

        if self.hasAnimations:
            return  # TODO
            for animation in self.animations.values():
                for channel in animation.channels:
                    for frame in channel.translations:
                        frame.value = frame.value * scale  # output array is readonly
