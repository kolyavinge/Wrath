class Frame:

    def __init__(self, time, value):
        self.time = time
        self.value = value


class Channel:

    def __init__(self):
        self.meshes = []
        self.translations = []
        self.rotations = []
        self.scales = []


class Animation:

    def __init__(self, name, duration, ticksPerSecond):
        self.name = name
        self.duration = duration
        self.ticksPerSecond = ticksPerSecond
        self.channels = []


class Mesh:

    def __init__(self):
        self.name = ""
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
            for animation in self.animations:
                for channel in animation.channels:
                    for frame in channel.translations:
                        frame.value = frame.value * scale  # output array is readonly
