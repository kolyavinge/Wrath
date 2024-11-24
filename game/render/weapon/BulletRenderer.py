from OpenGL.GL import *

from game.gl.VBORenderer import VBORenderer
from game.model.weapon.Launcher import LauncherBullet
from game.render.weapon.BulletRenderCollection import BulletRenderCollection


class BulletRenderer:

    def __init__(self, renderCollection, vboRenderer):
        self.renderCollection = renderCollection
        self.vboRenderer = vboRenderer
        self.bulletTypes = set()
        self.bulletTypes.add(LauncherBullet)

    def render(self, shader, levelSegment):
        for bullet in levelSegment.bullets:
            if type(bullet) in self.bulletTypes:
                shader.setModelMatrix(bullet.getModelMatrix())
                model = self.renderCollection.getRenderModel3d(type(bullet))
                for mesh in model.meshes:
                    shader.setMaterial(mesh.material)
                    mesh.texture.bind(GL_TEXTURE0)
                    self.vboRenderer.render(mesh.vbo)


def makeBulletRenderer(resolver):
    return BulletRenderer(resolver.resolve(BulletRenderCollection), resolver.resolve(VBORenderer))
