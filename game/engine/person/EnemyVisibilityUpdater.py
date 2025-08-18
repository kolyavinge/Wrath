from game.calc.Vector3 import Vector3
from game.engine.CameraScopeChecker import CameraScopeChecker
from game.engine.GameData import GameData


class EnemyVisibilityUpdater:

    def __init__(
        self,
        gameData: GameData,
        cameraScopeChecker: CameraScopeChecker,
    ):
        self.gameData = gameData
        self.cameraScopeChecker = cameraScopeChecker

    def updateEnemiesVisibility(self):
        for levelSegment in self.gameData.visibleLevelSegments:
            for enemy in levelSegment.enemies:
                enemy.isVisibleForPlayer = self.isEnemyVisible(enemy)

    def isEnemyVisible(self, enemy):
        def checkPoints(startPoint, endPoint):
            for point in Vector3.fromStartToEnd(startPoint, endPoint, 0.3):
                if self.cameraScopeChecker.isPointInCamera(point):
                    return True

            return False

        bottom = enemy.currentBorder.bottom
        top = enemy.currentBorder.top

        return (
            checkPoints(bottom.downLeft, top.downLeft)
            or checkPoints(bottom.downRight, top.downRight)
            or checkPoints(bottom.upLeft, top.upLeft)
            or checkPoints(bottom.upRight, top.upRight)
        )
