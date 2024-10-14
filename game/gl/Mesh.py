class ChildMesh:

    def __init__(self):
        self.vertices = []
        self.normals = []
        self.texCoords = []
        self.faces = []
        self.mainTexture = None


class Mesh:

    def __init__(self):
        self.children = []

    def addChild(self, childMesh):
        self.children.append(childMesh)

    def setScale(self, scale):
        for child in self.children:
            child.vertices *= scale
