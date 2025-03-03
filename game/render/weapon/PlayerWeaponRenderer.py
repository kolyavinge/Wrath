from OpenGL.GL import *

from game.engine.GameData import GameData
from game.gl.model3d.Model3dRenderer import Model3dRenderer
from game.render.weapon.WeaponRenderCollection import WeaponRenderCollection


class PlayerWeaponRenderer:

    def __init__(self, gameData, renderCollection, model3dRenderer):
        self.gameData = gameData
        self.renderCollection = renderCollection
        self.model3dRenderer = model3dRenderer

    def render(self, shader):
        playerItems = self.gameData.playerItems
        self.renderWeapon(shader, playerItems.rightHandWeapon)
        if playerItems.leftHandWeapon is not None:
            self.renderWeapon(shader, playerItems.leftHandWeapon)

    def renderWeapon(self, shader, weapon):
        shader.setModelMatrix(weapon.getModelMatrix())
        model = self.renderCollection.getRenderModel3d(type(weapon))
        self.model3dRenderer.render(model, shader)


def makePlayerWeaponRenderer(resolver):
    return PlayerWeaponRenderer(resolver.resolve(GameData), resolver.resolve(WeaponRenderCollection), resolver.resolve(Model3dRenderer))
