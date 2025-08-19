from game.anx.CommonConstants import CommonConstants
from game.engine.GameData import GameData
from game.gl.model3d.AnimationPlayer import AnimationPlayer
from game.gl.model3d.Model3dRenderer import Model3dRenderer
from game.model.person.AimState import SniperAimState
from game.render.person.EnemyAnimationCollection import EnemyAnimationCollection
from game.render.person.EnemyRenderCollection import EnemyRenderCollection


class EnemyRenderer:

    def __init__(
        self,
        gameData: GameData,
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
        enemyDirectionLength = self.gameData.camera.position.getLengthTo(enemy.middleCenterPoint)
        if enemyDirectionLength < CommonConstants.maxEnemyAnimationDistance or type(self.gameData.aimState) == SniperAimState:
            animation = self.enemyAnimationCollection.getPlayableAnimationOrNone(enemy)
            if animation is not None:
                self.animationPlayer.update(animation)
                shader.hasAnimation(True)
                shader.setBoneTransformMatrices(animation.boneTransformMatrices)
        self.model3dRenderer.render(self.renderCollection.enemyModel, shader)
        shader.hasAnimation(False)

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
        self.model3dRenderer.renderForShadow(self.renderCollection.enemyModel)
