from OpenGL.GL import *

from game.gl.VBORenderer import VBORenderer
from game.render.level.ShadowCasterCollection import *


class ShadowCasterRenderer:

    def __init__(self, shadowCasterCollection, vboRenderer):
        self.shadowCasterCollection = shadowCasterCollection
        self.vboRenderer = vboRenderer

    def init(self, allLevelSegments):
        self.shadowCasterCollection.init(allLevelSegments)

    def render(self, levelSegment):
        vbo = self.shadowCasterCollection.getShadowCastersVBO(levelSegment)
        self.vboRenderer.render(vbo)


def makeShadowCasterRenderer(resolver):
    return ShadowCasterRenderer(
        resolver.resolve(ShadowCasterCollection),
        resolver.resolve(VBORenderer),
    )
