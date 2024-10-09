from game.gl.Mesh import Mesh
from game.gl.Texture import Texture


class MeshLoader:

    def load(self, filePath):
        mesh = Mesh()
        mesh.mainTexture = Texture(1, 10, 10)

        return mesh


def makeMeshLoader(resolver):
    return MeshLoader()
