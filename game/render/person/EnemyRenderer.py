from game.anx.CommonConstants import CommonConstants
from game.engine.CameraScopeChecker import CameraScopeChecker
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
        cameraScopeChecker: CameraScopeChecker,
    ):
        self.gameData = gameData
        self.renderCollection = renderCollection
        self.model3dRenderer = model3dRenderer
        self.enemyAnimationCollection = enemyAnimationCollection
        self.animationPlayer = animationPlayer
        self.cameraScopeChecker = cameraScopeChecker

    def render(self, shader, levelSegment):
        for enemy in levelSegment.enemies:
            self.renderEnemy(enemy, shader)

    def renderEnemy(self, enemy, shader):
        if not self.isEnemyVisible(enemy):
            return
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

    def isEnemyVisible(self, enemy):
        border = enemy.currentBorder
        return (
            self.cameraScopeChecker.isPointInCamera(border.bottom.downLeft)
            or self.cameraScopeChecker.isPointInCamera(border.bottom.upRight)
            or self.cameraScopeChecker.isPointInCamera(border.top.downLeft)
            or self.cameraScopeChecker.isPointInCamera(border.top.upRight)
        )
