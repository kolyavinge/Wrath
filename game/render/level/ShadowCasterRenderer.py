from OpenGL.GL import *

from game.gl.VBORenderer import VBORenderer
from game.render.level.ShadowCasterRenderCollection import *


class ShadowCasterRenderer:

    def __init__(self, renderCollection, vboRenderer):
        self.renderCollection = renderCollection
        self.vboRenderer = vboRenderer

    def render(self, levelSegment):
        vbo = self.renderCollection.getShadowCastersVBO(levelSegment)
        self.vboRenderer.render(vbo)


def makeShadowCasterRenderer(resolver):
    return ShadowCasterRenderer(
        resolver.resolve(ShadowCasterRenderCollection),
        resolver.resolve(VBORenderer),
    )
