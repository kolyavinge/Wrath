from OpenGL.GL import *

from game.gl.VBORenderer import VBORenderer
from game.model.powerup.WeaponPowerup import WeaponPowerup
from game.render.powerup.PowerupRenderCollection import PowerupRenderCollection
from game.render.weapon.WeaponRenderCollection import WeaponRenderCollection


class PowerupRenderer:

    def __init__(self, powerupRenderCollection, weaponRenderCollection, vboRenderer):
        self.powerupRenderCollection = powerupRenderCollection
        self.weaponRenderCollection = weaponRenderCollection
        self.vboRenderer = vboRenderer

    def render(self, shader, levelSegment):
        for powerup in levelSegment.powerups:
            shader.setModelMatrix(powerup.getModelMatrix())
            model = self.getModel(powerup)
            for mesh in model.meshes:
                shader.setMaterial(mesh.material)
                mesh.texture.bind(GL_TEXTURE0)
                self.vboRenderer.render(mesh.vbo)

    def getModel(self, powerup):
        if isinstance(powerup, WeaponPowerup):
            return self.weaponRenderCollection.getRenderModel3d(powerup.weaponType)
        else:
            return self.powerupRenderCollection.getRenderModel3d(type(powerup))


def makePowerupRenderer(resolver):
    return PowerupRenderer(resolver.resolve(PowerupRenderCollection), resolver.resolve(WeaponRenderCollection), resolver.resolve(VBORenderer))
