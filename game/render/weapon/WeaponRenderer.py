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

    def renderPlayerWeapons(self, shader):
        self.renderWeapon(shader, self.gameData.playerItems.rightHandWeapon)
        if self.gameData.playerItems.leftHandWeapon is not None:
            self.renderWeapon(shader, self.gameData.playerItems.leftHandWeapon)

    def renderEnemyWeapons(self, shader):
        for enemy, enemyItems in self.gameData.enemyItems.items():
            if enemy.isVisibleForPlayer:
                self.renderWeapon(shader, enemyItems.rightHandWeapon)
                if enemyItems.leftHandWeapon is not None:
                    self.renderWeapon(shader, enemyItems.leftHandWeapon)

    def renderWeapon(self, shader, weapon):
        shader.setModelMatrix(weapon.getModelMatrix())
        model = self.renderCollection.getRenderModel3d(type(weapon))
        self.model3dRenderer.render(model, shader)
