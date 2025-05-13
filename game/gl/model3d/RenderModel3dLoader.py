from game.gl.model3d.RenderModel3d import RenderMesh, RenderModel3d
from game.gl.vbo.VBOBuilderFactory import VBOBuilderFactory


class RenderModel3dLoader:

    def __init__(self, vboBuilderFactory: VBOBuilderFactory):
        self.vboBuilderFactory = vboBuilderFactory

    def make(self, model3d, material):
        vboBuilder = self.vboBuilderFactory.makeModel3dVBOBuilder()
        vbos = vboBuilder.build(model3d)
        meshes = [RenderMesh(vbo, mesh.texture, material) for mesh, vbo in vbos]

        return RenderModel3d(meshes, model3d.animations)
