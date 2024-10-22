from game.gl.VBORenderer import VBORenderer
from game.render.weapon.BulletHoleRenderCollection import BulletHoleRenderCollection


class BulletHoleRenderer:

    def __init__(self, bulletHoleRenderCollection, vboRenderer):
        self.bulletHoleRenderCollection = bulletHoleRenderCollection
        self.vboRenderer = vboRenderer

    def init(self, allVisibilityLevelSegments):
        self.bulletHoleRenderCollection.init(allVisibilityLevelSegments)

    def render(self, shader, levelSegment):
        vbo = self.bulletHoleRenderCollection.getVBO(levelSegment)
        if vbo.elementsCount > 0:
            self.vboRenderer.render(vbo)


def makeBulletHoleRenderer(resolver):
    return BulletHoleRenderer(resolver.resolve(BulletHoleRenderCollection), resolver.resolve(VBORenderer))
