from game.anx.PersonConstants import PersonConstants
from game.calc.Box3d import Box3d
from game.calc.Vector3 import Vector3
from game.engine.CameraScopeChecker import CameraScopeChecker
from game.engine.GameData import GameData
from game.model.person.PersonStates import LifeCycle


class EnemyVisibilityUpdater:

    def __init__(
        self,
        gameData: GameData,
        cameraScopeChecker: CameraScopeChecker,
    ):
        self.gameData = gameData
        self.cameraScopeChecker = cameraScopeChecker
        self.calculateVisibilityPoints()

    def updateEnemiesVisibility(self):
        for levelSegment in self.gameData.visibleLevelSegments:
            for enemy in levelSegment.enemies:
                enemy.isVisibleForPlayer = enemy.lifeCycle != LifeCycle.respawnDelay and self.inCamera(enemy)

    def inCamera(self, enemy):
        shift = enemy.currentCenterPoint
        for initPoint in self.initVisibilityPoints:
            if self.cameraScopeChecker.isPointInCamera(initPoint.x + shift.x, initPoint.y + shift.y, initPoint.z + shift.z):
                return True

        return False

    def calculateVisibilityPoints(self):
        box = Box3d(PersonConstants.xyLength, PersonConstants.xyLength, PersonConstants.zLength)
        box.calculatePointsByCenter(Vector3(0, 0, 0))
        self.initVisibilityPoints = []
        self.initVisibilityPoints.extend(Vector3.fromStartToEnd(box.bottom.downLeft, box.top.downLeft, 0.3))
        self.initVisibilityPoints.extend(Vector3.fromStartToEnd(box.bottom.downRight, box.top.downRight, 0.3))
        self.initVisibilityPoints.extend(Vector3.fromStartToEnd(box.bottom.upLeft, box.top.upLeft, 0.3))
        self.initVisibilityPoints.extend(Vector3.fromStartToEnd(box.bottom.upRight, box.top.upRight, 0.3))
