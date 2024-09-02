from game.gl.VBO import VBO


class VBOBuilder:

    def __init__(self):
        self.vertices = []
        self.normals = []
        self.texCoords = []

    def addVertex(self, vector):
        self.vertices.append(vector.x)
        self.vertices.append(vector.y)
        self.vertices.append(vector.z)

    def addNormal(self, vector):
        self.normals.append(vector.x)
        self.normals.append(vector.y)
        self.normals.append(vector.z)

    def addTexCoord(self, x, y):
        self.texCoords.append(x)
        self.texCoords.append(y)

    def build(self):

        return VBO(1)
