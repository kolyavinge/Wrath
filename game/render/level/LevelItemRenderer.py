from OpenGL.GL import *

from game.gl.VBORenderer import VBORenderer
from game.render.level.LevelRenderModel3dCollection import LevelRenderModel3dCollection


class LevelItemRenderer:

    def __init__(self, levelRenderModel3dCollection, vboRenderer):
        self.levelRenderModel3dCollection = levelRenderModel3dCollection
        self.vboRenderer = vboRenderer

    def init(self, allLevelSegments):
        self.levelRenderModel3dCollection.init(allLevelSegments)

    def render(self, shader, levelSegment):
        model3d = self.levelRenderModel3dCollection.getRenderModel3d(levelSegment)
        for mesh in model3d.meshes:
            shader.setMaterial(mesh.material)
            mesh.texture.bind(GL_TEXTURE0)
            self.vboRenderer.render(mesh.vbo)


def makeLevelItemRenderer(resolver):
    return LevelItemRenderer(resolver.resolve(LevelRenderModel3dCollection), resolver.resolve(VBORenderer))
