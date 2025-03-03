from game.gl.model3d.RenderModel3dLoader import RenderModel3dLoader
from game.model.Material import Material
from game.model.powerup.LargeHealthPowerup import LargeHealthPowerup
from game.model.powerup.SmallHealthPowerup import SmallHealthPowerup
from game.model.powerup.VestPowerup import VestPowerup
from game.render.powerup.PowerupModel3dFactory import PowerupModel3dFactory


class PowerupRenderCollection:

    def __init__(self, powerupModel3dFactory, renderModel3dLoader):
        self.powerupModel3dFactory = powerupModel3dFactory
        self.renderModel3dLoader = renderModel3dLoader
        self.models = {}

    def init(self):
        for vbo in self.models:
            vbo.release()

        self.models = {}
        self.makeSmallHealth()
        self.makeLargeHealth()
        self.makeVest()

    def makeSmallHealth(self):
        model = self.powerupModel3dFactory.makeSmallHealth()
        self.models[SmallHealthPowerup] = self.renderModel3dLoader.make(model, Material.powerup)

    def makeLargeHealth(self):
        model = self.powerupModel3dFactory.makeLargeHealth()
        self.models[LargeHealthPowerup] = self.renderModel3dLoader.make(model, Material.powerup)

    def makeVest(self):
        model = self.powerupModel3dFactory.makeVest()
        self.models[VestPowerup] = self.renderModel3dLoader.make(model, Material.powerup)

    def getRenderModel3d(self, powerupType):
        return self.models[powerupType]


def makePowerupRenderCollection(resolver):
    return PowerupRenderCollection(resolver.resolve(PowerupModel3dFactory), resolver.resolve(RenderModel3dLoader))
