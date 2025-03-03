class Mesh:

    def __init__(self):
        self.vertices = []
        self.normals = []
        self.texCoords = []
        self.faces = []
        self.texture = None


class Model3d:

    def __init__(self):
        self.meshes = []

    def addMesh(self, mesh):
        self.meshes.append(mesh)

    def setScale(self, scale):
        for mesh in self.meshes:
            mesh.vertices *= scale
