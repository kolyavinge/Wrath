from game.anx.CommonConstants import CommonConstants
from game.anx.PersonConstants import PersonConstants
from game.calc.TransformMatrix4Builder import TransformMatrix4Builder
from game.engine.GameState import GameState
from game.lib.Math import Math
from game.lib.Numeric import Numeric
from game.model.person.PersonStates import LifeCycle


class EnemyLifeBarUpdater:

    def __init__(self, gameState: GameState):
        self.gameState = gameState

    def update(self):
        self.decreaseFade()
        self.setVisibility()
        self.calcModelMatrix()

    def decreaseFade(self):
        for enemy, lifeBar in self.gameState.enemyLifeBars.items():
            lifeBar.fadeRemain.decrease()
            lifeBar.alpha = lifeBar.fadeRemain.value / lifeBar.fadeRemain.initValue
            lifeBar.isVisible = enemy.lifeCycle == LifeCycle.alive and Numeric.limitMin(lifeBar.alpha, 0.01, 0) > 0

    def setVisibility(self):
        for enemy in self.gameState.enemies:
            if (
                enemy.isVisibleForPlayer
                and enemy.lifeCycle == LifeCycle.alive
                and (
                    enemy in self.gameState.collisionData.personBullet
                    or enemy in self.gameState.collisionData.personRay
                    or enemy in self.gameState.collisionData.personExplosion
                )
            ):
                lifeBar = self.gameState.enemyLifeBars[enemy]
                lifeBar.fadeRemain.set(100)
                lifeBar.alpha = 1.0
                lifeBar.isVisible = True

    def calcModelMatrix(self):
        for enemy, lifeBar in self.gameState.enemyLifeBars.items():
            if lifeBar.isVisible:
                enemyPoint = enemy.currentCenterPoint
                angleToCamera = self.getAngleToCamera(enemyPoint)
                lifeBar.modelMatrix = (
                    TransformMatrix4Builder()
                    .translate(enemyPoint.x, enemyPoint.y, enemyPoint.z)
                    .rotate(angleToCamera, CommonConstants.zAxis)
                    .scale(enemy.health / PersonConstants.maxPersonHealth, 1, 1)
                ).resultMatrix

    def getAngleToCamera(self, enemyPoint):
        directionToCamera = enemyPoint.getDirectionTo(self.gameState.camera.position)
        directionToCamera.z = 0  # make 2d vector
        directionToCamera.normalize()
        dotProduct = directionToCamera.dotProduct(CommonConstants.yAxis)
        dotProduct = Numeric.limitBy(dotProduct, -1.0, 1.0)  # float issues
        angleToCamera = Math.arccos(dotProduct)
        orientDirection = CommonConstants.yAxis.copy()
        orientDirection.vectorProduct(directionToCamera)
        if orientDirection.z < 0:
            angleToCamera = -angleToCamera

        return angleToCamera
