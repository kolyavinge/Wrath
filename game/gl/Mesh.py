class Face:

    def __init__(self, i1, i2, i3):
        self.i1 = i1
        self.i2 = i2
        self.i3 = i3


class Mesh:

    def __init__(self):
        self.vertices = []
        self.normals = []
        self.texCoords = []
        self.faces = []
        self.mainTexture = None

    def addVertex(self, vector):
        self.vertices.append(vector)

    def addNormal(self, vector):
        self.normals.append(vector)

    def addTexCoord(self, point):
        self.texCoords.append(point)

    def addFace(self, face):
        self.faces.append(face)
