from OpenGL.GL import *

from game.anx.CommonConstants import CommonConstants
from game.engine.GameState import GameState
from game.gl.model3d.AnimationPlayer import AnimationPlayer
from game.gl.model3d.Model3dRenderer import Model3dRenderer
from game.model.person.AimState import SniperAimState
from game.model.person.PersonStates import LifeCycle
from game.render.person.EnemyAnimationCollection import EnemyAnimationCollection
from game.render.person.EnemyRenderCollection import EnemyRenderCollection


class EnemyRenderer:

    def __init__(
        self,
        gameData: GameState,
        renderCollection: EnemyRenderCollection,
        model3dRenderer: Model3dRenderer,
        enemyAnimationCollection: EnemyAnimationCollection,
        animationPlayer: AnimationPlayer,
    ):
        self.gameData = gameData
        self.renderCollection = renderCollection
        self.model3dRenderer = model3dRenderer
        self.enemyAnimationCollection = enemyAnimationCollection
        self.animationPlayer = animationPlayer

    def render(self, shader, levelSegment):
        for enemy in levelSegment.enemies:
            if enemy.isVisibleForPlayer:
                self.renderEnemy(enemy, shader)

    def renderEnemy(self, enemy, shader):
        shader.setModelMatrix(enemy.getModelMatrix())

        if self.animationNeedApply(enemy):
            animation = self.enemyAnimationCollection.getPlayableAnimationOrNone(enemy)
            if animation is not None and self.animationNeedUpdate(enemy):
                self.animationPlayer.update(animation)
            shader.hasAnimation(True)
            shader.setBoneTransformMatrices(animation.boneTransformMatrices)

        if enemy.lifeCycle != LifeCycle.alive:
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            glEnable(GL_BLEND)
            glEnable(GL_ALPHA_TEST)
            shader.setAlphaFactor(enemy.getAlphaForLifeCycle())

        self.model3dRenderer.render(self.renderCollection.enemyModel, shader)

        shader.hasAnimation(False)
        if enemy.lifeCycle != LifeCycle.alive:
            glDisable(GL_ALPHA_TEST)
            glDisable(GL_BLEND)

    def renderForShadow(self, shader, levelSegment):
        shader.hasAnimation(True)
        for enemy in levelSegment.enemies:
            if enemy.isVisibleForPlayer:
                self.renderEnemyForShadow(enemy, shader)
        shader.hasAnimation(False)

    def renderEnemyForShadow(self, enemy, shader):
        shader.setModelMatrix(enemy.getModelMatrix())
        animation = self.enemyAnimationCollection.getPlayableAnimationOrNone(enemy)
        shader.setBoneTransformMatrices(animation.boneTransformMatrices)
        self.model3dRenderer.renderForShadow(self.renderCollection.enemyModelForShadow)

    def animationNeedApply(self, enemy):
        if type(self.gameData.aimState) == SniperAimState:
            return True

        enemyDirectionLength = self.gameData.camera.position.getLengthTo(enemy.middleCenterPoint)
        if enemyDirectionLength < CommonConstants.maxEnemyAnimationDistance:
            return True

        return False

    def animationNeedUpdate(self, enemy):
        return enemy.lifeCycle == LifeCycle.alive
