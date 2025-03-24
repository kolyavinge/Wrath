class Frame:

    def __init__(self, time, transformMatrix):
        self.time = time
        self.transformMatrix = transformMatrix


class Channel:

    def __init__(self):
        self.node = None
        self.translationFrames = []
        self.rotationFrames = []
        self.scaleFrames = []


class Bone:

    # такие же константы есть в шейдерах
    maxBonesCountInfluence = 4
    maxBonesCount = 100

    def __init__(self, id, name, offsetMatrix):
        self.id = id
        self.name = name
        self.offsetMatrix = offsetMatrix


class Node:

    def __init__(self):
        self.name = ""
        self.parent = None
        self.children = []
        self.transformMatrix = None
        self.bone = None


class Animation:

    def __init__(self, name, duration, ticksPerSecond, rootNode, allBonesCount):
        self.name = name
        self.duration = duration
        self.ticksPerSecond = ticksPerSecond
        self.rootNode = rootNode
        self.channels = {}
        self.allBonesCount = allBonesCount


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
        self.animations = None

    def setScale(self, scale):
        for mesh in self.meshes:
            mesh.vertices *= scale

        if self.animations is not None:
            return  # TODO
            for animation in self.animations.values():
                for channel in animation.channels:
                    for frame in channel.translations:
                        frame.value = frame.value * scale  # output array is readonly
