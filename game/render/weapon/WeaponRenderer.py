from OpenGL.GL import *

from game.engine.GameState import GameState
from game.gl.model3d.Model3dRenderer import Model3dRenderer
from game.model.person.PersonStates import LifeCycle
from game.render.weapon.WeaponRenderCollection import WeaponRenderCollection


class WeaponRenderer:

    def __init__(
        self,
        gameState: GameState,
        renderCollection: WeaponRenderCollection,
        model3dRenderer: Model3dRenderer,
    ):
        self.gameState = gameState
        self.renderCollection = renderCollection
        self.model3dRenderer = model3dRenderer

    def renderPlayerWeapon(self, shader):
        self.renderWeapon(shader, self.gameState.playerItems.rightHandWeapon)
        if self.gameState.playerItems.leftHandWeapon is not None:
            self.renderWeapon(shader, self.gameState.playerItems.leftHandWeapon)

    def renderEnemyWeapons(self, shader):
        for enemy, enemyItems in self.gameState.enemyItems.items():
            if enemy.isVisibleForPlayer:
                self.renderEnemyWeapon(enemy, enemyItems, shader)

    def renderEnemyWeapon(self, enemy, enemyItems, shader):
        if enemy.lifeCycle != LifeCycle.alive:
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            glEnable(GL_BLEND)
            glEnable(GL_ALPHA_TEST)
            shader.setAlphaFactor(enemy.getAlphaForLifeCycle())

        self.renderWeapon(shader, enemyItems.rightHandWeapon)
        if enemyItems.leftHandWeapon is not None:
            self.renderWeapon(shader, enemyItems.leftHandWeapon)

        if enemy.lifeCycle != LifeCycle.alive:
            glDisable(GL_ALPHA_TEST)
            glDisable(GL_BLEND)

    def renderWeapon(self, shader, weapon):
        shader.setModelMatrix(weapon.getModelMatrix())
        model = self.renderCollection.getRenderModel3d(type(weapon))
        self.model3dRenderer.render(model, shader)
