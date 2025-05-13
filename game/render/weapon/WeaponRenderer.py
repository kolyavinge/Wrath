from OpenGL.GL import *

from game.engine.GameData import GameData
from game.gl.model3d.Model3dRenderer import Model3dRenderer
from game.render.weapon.WeaponRenderCollection import WeaponRenderCollection


class WeaponRenderer:

    def __init__(
        self,
        gameData: GameData,
        renderCollection: WeaponRenderCollection,
        model3dRenderer: Model3dRenderer,
    ):
        self.gameData = gameData
        self.renderCollection = renderCollection
        self.model3dRenderer = model3dRenderer

    def renderAllWeapons(self, shader):
        for personItems in self.gameData.allPersonItems.values():
            self.renderWeapon(shader, personItems.rightHandWeapon)
            if personItems.leftHandWeapon is not None:
                self.renderWeapon(shader, personItems.leftHandWeapon)

    def renderEnemyWeapons(self, shader):
        for enemyItems in self.gameData.enemyItems.values():
            self.renderWeapon(shader, enemyItems.rightHandWeapon)
            if enemyItems.leftHandWeapon is not None:
                self.renderWeapon(shader, enemyItems.leftHandWeapon)

    def renderWeapon(self, shader, weapon):
        shader.setModelMatrix(weapon.getModelMatrix())
        model = self.renderCollection.getRenderModel3d(type(weapon))
        self.model3dRenderer.render(model, shader)
