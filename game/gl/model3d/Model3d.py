class Frame:

    def __init__(self, time, value):
        self.time = time
        self.value = value
        self.nextFrame = None
        self.leftChild = None
        self.rightChild = None


class Channel:

    def __init__(self):
        self.node = None
        self.translationRootFrame = []
        self.rotationRootFrame = []
        self.scaleRootFrame = []


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
        if self.animations is not None:
            raise Exception("Model cannot be scaled if it has any animations.")

        for mesh in self.meshes:
            mesh.vertices *= scale
