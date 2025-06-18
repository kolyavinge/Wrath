from game.anx.CommonConstants import CommonConstants
from game.anx.PersonConstants import PersonConstants
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
            self.renderEnemy(enemy, shader)

    def renderEnemy(self, enemy, shader):
        enemyDirection = self.gameData.camera.position.getDirectionTo(enemy.middleCenterPoint)
        enemyDirectionLength = enemyDirection.getLength()
        if not self.isEnemyVisible(enemyDirection, enemyDirectionLength):
            return
        shader.setModelMatrix(enemy.getModelMatrix())
        if enemyDirectionLength < CommonConstants.maxEnemyAnimationDistance or type(self.gameData.aimState) == SniperAimState:
            animation = self.enemyAnimationCollection.getPlayableAnimationOrNone(enemy)
            if animation is not None:
                self.animationPlayer.update(animation)
                shader.hasAnimation(True)
                shader.setBoneTransformMatrices(animation.boneTransformMatrices)
        self.model3dRenderer.render(self.renderCollection.enemyModel, shader)
        shader.hasAnimation(False)

    def isEnemyVisible(self, enemyDirection, enemyDirectionLength):
        dotProduct = self.gameData.camera.lookDirection.dotProduct(enemyDirection)
        if dotProduct < 0:
            return False

        if enemyDirectionLength < PersonConstants.zLength:
            return True

        dotProduct /= enemyDirectionLength
        isVisible = self.gameData.camera.horizontalViewRadiansHalfCos < dotProduct

        return isVisible
