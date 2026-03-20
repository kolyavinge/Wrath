from game.lib.calc.TransformMatrix4 import TransformMatrix4
from game.render.level.ShadowCasterRenderCollection import *
from game.render.lib.vbo.VBORenderer import VBORenderer


class ShadowCasterRenderer:

    def __init__(
        self,
        renderCollection: ShadowCasterRenderCollection,
        vboRenderer: VBORenderer,
    ):
        self.renderCollection = renderCollection
        self.vboRenderer = vboRenderer

    def render(self, shader, levelSegment):
        shader.setModelMatrix(TransformMatrix4.identity)
        vbo = self.renderCollection.getShadowCastersVBO(levelSegment)
        if vbo is not None:
            self.vboRenderer.render(vbo)
