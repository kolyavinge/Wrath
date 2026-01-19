from game.anx.CommonConstants import CommonConstants
from game.anx.PersonConstants import PersonConstants
from game.calc.TransformMatrix4Builder import TransformMatrix4Builder
from game.lib.Math import Math
from game.lib.Numeric import Numeric
from game.model.person.PersonStates import LifeCycle


class EnemyLifeBarUpdater:

    def update(self, gameState):
        self.decreaseFade(gameState)
        self.setVisibility(gameState)
        self.calcModelMatrix(gameState)

    def decreaseFade(self, gameState):
        for enemy, lifeBar in gameState.enemyLifeBars.items():
            lifeBar.fadeRemain.decrease()
            lifeBar.alpha = lifeBar.fadeRemain.value / lifeBar.fadeRemain.initValue
            lifeBar.isVisible = enemy.lifeCycle == LifeCycle.alive and Numeric.limitMin(lifeBar.alpha, 0.01, 0) > 0

    def setVisibility(self, gameState):
        for enemy in gameState.enemies:
            if (
                enemy.isVisibleForPlayer
                and enemy.lifeCycle == LifeCycle.alive
                and (
                    enemy in gameState.collisionData.personBullet
                    or enemy in gameState.collisionData.personRay
                    or enemy in gameState.collisionData.personExplosion
                )
            ):
                lifeBar = gameState.enemyLifeBars[enemy]
                lifeBar.fadeRemain.set(100)
                lifeBar.alpha = 1.0
                lifeBar.isVisible = True

    def calcModelMatrix(self, gameState):
        cameraPosition = gameState.camera.position
        for enemy, lifeBar in gameState.enemyLifeBars.items():
            if lifeBar.isVisible:
                enemyPoint = enemy.currentCenterPoint
                angleToCamera = self.getAngleToCamera(enemyPoint, cameraPosition)
                lifeBar.modelMatrix = (
                    TransformMatrix4Builder()
                    .translate(enemyPoint.x, enemyPoint.y, enemyPoint.z)
                    .rotate(angleToCamera, CommonConstants.zAxis)
                    .scale(enemy.health / PersonConstants.maxPersonHealth, 1, 1)
                ).resultMatrix

    def getAngleToCamera(self, enemyPoint, cameraPosition):
        directionToCamera = enemyPoint.getDirectionTo(cameraPosition)
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
