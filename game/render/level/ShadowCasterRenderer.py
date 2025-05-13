from OpenGL.GL import *

from game.gl.vbo.VBORenderer import VBORenderer
from game.render.level.ShadowCasterRenderCollection import *


class ShadowCasterRenderer:

    def __init__(
        self,
        renderCollection: ShadowCasterRenderCollection,
        vboRenderer: VBORenderer,
    ):
        self.renderCollection = renderCollection
        self.vboRenderer = vboRenderer

    def render(self, levelSegment):
        vbo = self.renderCollection.getShadowCastersVBO(levelSegment)
        if vbo is not None:
            self.vboRenderer.render(vbo)


def makeShadowCasterRenderer(resolver):
    return ShadowCasterRenderer(
        resolver.resolve(ShadowCasterRenderCollection),
        resolver.resolve(VBORenderer),
    )
