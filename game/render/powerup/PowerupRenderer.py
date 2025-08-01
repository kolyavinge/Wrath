from game.gl.model3d.Model3dRenderer import Model3dRenderer
from game.model.powerup.WeaponPowerup import WeaponPowerup
from game.render.powerup.PowerupRenderCollection import PowerupRenderCollection
from game.render.weapon.WeaponRenderCollection import WeaponRenderCollection


class PowerupRenderer:

    def __init__(
        self,
        powerupRenderCollection: PowerupRenderCollection,
        weaponRenderCollection: WeaponRenderCollection,
        model3dRenderer: Model3dRenderer,
    ):
        self.powerupRenderCollection = powerupRenderCollection
        self.weaponRenderCollection = weaponRenderCollection
        self.model3dRenderer = model3dRenderer

    def render(self, shader, levelSegment):
        for powerup in levelSegment.powerups:
            shader.setModelMatrix(powerup.getModelMatrix())
            model = self.getModel(powerup)
            self.model3dRenderer.render(model, shader)

    def getModel(self, powerup):
        if type(powerup) == WeaponPowerup:
            return self.weaponRenderCollection.getRenderModel3d(powerup.weaponType)
        else:
            return self.powerupRenderCollection.getRenderModel3d(type(powerup))
