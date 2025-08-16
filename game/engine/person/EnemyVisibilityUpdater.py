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
        border = enemy.currentBorder
        return (
            self.cameraScopeChecker.isPointInCamera(border.bottom.downLeft)
            or self.cameraScopeChecker.isPointInCamera(border.bottom.upRight)
            or self.cameraScopeChecker.isPointInCamera(border.top.downLeft)
            or self.cameraScopeChecker.isPointInCamera(border.top.upRight)
        )
