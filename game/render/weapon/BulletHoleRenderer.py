from OpenGL.GL import *

from game.gl.VBORenderer import VBORenderer
from game.render.weapon.BulletHoleRenderCollection import BulletHoleRenderCollection


class BulletHoleRenderer:

    def __init__(self, bulletHoleRenderCollection, vboRenderer):
        self.bulletHoleRenderCollection = bulletHoleRenderCollection
        self.vboRenderer = vboRenderer

    def init(self, allVisibilityLevelSegments):
        self.bulletHoleRenderCollection.init(allVisibilityLevelSegments)

    def render(self, shader, levelSegment):
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)

        meshes = self.bulletHoleRenderCollection.getRenderMeshes(levelSegment)
        for mesh in meshes:
            shader.setMaterial(mesh.material)
            mesh.texture.bind(GL_TEXTURE0)
            self.vboRenderer.render(mesh.vbo)

        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)


def makeBulletHoleRenderer(resolver):
    return BulletHoleRenderer(resolver.resolve(BulletHoleRenderCollection), resolver.resolve(VBORenderer))