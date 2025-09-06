from game.anx.CommonConstants import CommonConstants
from game.engine.GameData import GameData
from game.lib.Math import Math
from game.lib.Numeric import Numeric


class EnemyLifeBarUpdater:

    def __init__(self, gameData: GameData):
        self.gameData = gameData

    def update(self):
        self.decreaseFade()
        self.setVisibility()
        self.calcModelMatrix()

    def decreaseFade(self):
        for lifeBar in self.gameData.enemyLifeBars.values():
            lifeBar.fadeRemain.decrease()
            lifeBar.alpha = lifeBar.fadeRemain.value / lifeBar.fadeRemain.initValue
            lifeBar.isVisible = Numeric.limitMin(lifeBar.alpha, 0.01, 0) > 0

    def setVisibility(self):
        for enemy in self.gameData.enemies:
            if enemy.isVisibleForPlayer and enemy in self.gameData.collisionData.personBullet:
                lifeBar = self.gameData.enemyLifeBars[enemy]
                lifeBar.fadeRemain.set(50)
                lifeBar.alpha = 1.0
                lifeBar.isVisible = True

    def calcModelMatrix(self):
        for enemy, lifeBar in self.gameData.enemyLifeBars.items():
            if lifeBar.isVisible:
                enemyPoint = enemy.currentCenterPoint
                angleToCamera = self.getAngleToCamera(enemyPoint)
                lifeBar.modelMatrix.translateAndRotate(enemyPoint.x, enemyPoint.y, enemyPoint.z, angleToCamera, CommonConstants.zAxis)

    def getAngleToCamera(self, enemyPoint):
        directionToCamera = enemyPoint.getDirectionTo(self.gameData.camera.position)
        directionToCamera.z = 0  # make 2d vector
        directionToCamera.normalize()
        dotProduct = directionToCamera.dotProduct(CommonConstants.yAxis)
        dotProduct = Numeric.limitBy(dotProduct, -1.0, 1.0)
        angleToCamera = Math.arccos(dotProduct)

        return angleToCamera
