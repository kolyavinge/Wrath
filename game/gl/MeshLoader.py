from game.gl.Mesh import Mesh


class MeshLoader:

    def load(self, filePath):

        return Mesh()


def makeMeshLoader(resolver):
    return MeshLoader()
