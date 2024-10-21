from OpenGL.GL import *

from game.gl.VBORenderer import VBORenderer
from game.render.level.LevelItemRenderModel3dCollection import *


class LevelItemRenderer:

    def __init__(self, levelItemRenderModel3dCollection, vboRenderer):
        self.levelItemRenderModel3dCollection = levelItemRenderModel3dCollection
        self.vboRenderer = vboRenderer

    def init(self, allLevelSegments):
        self.levelItemRenderModel3dCollection.init(allLevelSegments)

    def render(self, shader, levelSegment):
        model3d = self.levelItemRenderModel3dCollection.getRenderModel3d(levelSegment)
        for mesh in model3d.meshes:
            shader.setMaterial(mesh.material)
            mesh.texture.bind(GL_TEXTURE0)
            self.vboRenderer.render(mesh.vbo)


def makeLevelItemRenderer(resolver):
    return LevelItemRenderer(resolver.resolve(LevelItemRenderModel3dCollection), resolver.resolve(VBORenderer))
