from game.gl.RenderModel3d import RenderMesh, RenderModel3d
from game.gl.VBOBuilderFactory import VBOBuilderFactory


class RenderModel3dLoader:

    def __init__(self, vboBuilderFactory):
        self.vboBuilderFactory = vboBuilderFactory

    def make(self, model3d, material):
        vboBuilder = self.vboBuilderFactory.makeModel3dVBOBuilder()
        vbos = vboBuilder.build(model3d)
        meshes = [RenderMesh(vbo, mesh.texture, material) for mesh, vbo in vbos]

        return RenderModel3d(meshes)


def makeRenderModel3dLoader(resolver):
    return RenderModel3dLoader(resolver.resolve(VBOBuilderFactory))
