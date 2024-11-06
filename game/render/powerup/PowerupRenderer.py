from OpenGL.GL import *

from game.gl.VBORenderer import VBORenderer
from game.model.powerup.WeaponPowerup import WeaponPowerup
from game.render.weapon.WeaponRenderCollection import WeaponRenderCollection


class PowerupRenderer:

    def __init__(self, weaponRenderCollection, vboRenderer):
        self.weaponRenderCollection = weaponRenderCollection
        self.vboRenderer = vboRenderer

    def render(self, shader, levelSegment):
        for powerup in levelSegment.powerups:
            shader.setModelMatrix(powerup.getModelMatrix())

            if isinstance(powerup, WeaponPowerup):
                model = self.weaponRenderCollection.getRenderModel3d(powerup.weaponType)
            else:
                model = self.powerupRenderCollection.getRenderModel3d(type(powerup))

            for mesh in model.meshes:
                shader.setMaterial(mesh.material)
                mesh.texture.bind(GL_TEXTURE0)
                self.vboRenderer.render(mesh.vbo)


def makePowerupRenderer(resolver):
    return PowerupRenderer(resolver.resolve(WeaponRenderCollection), resolver.resolve(VBORenderer))
