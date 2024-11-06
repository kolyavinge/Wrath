from OpenGL.GL import *

from game.calc.TransformMatrix4 import TransformMatrix4
from game.gl.VBORenderer import VBORenderer
from game.render.level.LevelItemRenderCollection import *


class LevelItemRenderer:

    def __init__(self, renderCollection, vboRenderer):
        self.renderCollection = renderCollection
        self.vboRenderer = vboRenderer

    def init(self, allLevelSegments):
        self.renderCollection.init(allLevelSegments)

    def render(self, shader, levelSegment):
        shader.setModelMatrix(TransformMatrix4())
        model3d = self.renderCollection.getRenderModel3d(levelSegment)
        for mesh in model3d.meshes:
            shader.setMaterial(mesh.material)
            mesh.texture.bind(GL_TEXTURE0)
            self.vboRenderer.render(mesh.vbo)


def makeLevelItemRenderer(resolver):
    return LevelItemRenderer(resolver.resolve(LevelItemRenderCollection), resolver.resolve(VBORenderer))
