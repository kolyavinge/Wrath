from game.calc.Vector3 import Vector3
from game.engine.CameraScopeChecker import CameraScopeChecker
from game.engine.GameData import GameData
from game.tools.CpuProfiler import cpuProfile


class BackgroundVisibilityUpdater:

    def __init__(
        self,
        gameData: GameData,
        cameraScopeChecker: CameraScopeChecker,
    ):
        self.gameData = gameData
        self.cameraScopeChecker = cameraScopeChecker
        self.lookDirectionPoint = Vector3()
        self.alreadyCheckedPoints = set()

    def updateIfPlayerMovedOrTurned(self):
        if self.gameData.player.hasMoved or self.gameData.player.hasTurned or self.gameData.camera.hasVerticalViewRadiansChanged:
            self.update()
        else:
            self.gameData.backgroundVisibility.isUpdated = False

    # @cpuProfile
    def update(self):

        def checkVisiblePoint(point):
            self.alreadyCheckedPoints.add(point)
            for element in point.joinedElements:
                self.gameData.backgroundVisibility.visibleSphereElements.add(element)
                for joinedPoint in element.points:
                    if joinedPoint not in self.alreadyCheckedPoints and self.cameraScopeChecker.isPointInCamera(
                        joinedPoint.vertex.x,
                        joinedPoint.vertex.y,
                        joinedPoint.vertex.z,
                        scale=1.5,
                    ):
                        checkVisiblePoint(joinedPoint)

        self.alreadyCheckedPoints.clear()
        point = self.getAnyVisiblePointOrNone()
        if point is not None:
            self.gameData.backgroundVisibility.visibleSphereElements.clear()
            checkVisiblePoint(point)
            self.gameData.backgroundVisibility.isUpdated = True
        else:
            self.gameData.backgroundVisibility.isUpdated = False

    def getAnyVisiblePointOrNone(self):
        lookDirection = self.gameData.camera.lookDirection
        self.lookDirectionPoint.set(lookDirection.x, lookDirection.y, lookDirection.z)
        self.lookDirectionPoint.mul(self.gameData.backgroundVisibility.sphere.radius)
        self.lookDirectionPoint.add(self.gameData.camera.position)
        spherePoints = self.gameData.backgroundVisibility.sphereBSPTree.findNodeItemsByPoint(self.lookDirectionPoint)
        for point in spherePoints:
            if self.cameraScopeChecker.isPointInCamera(point.vertex.x, point.vertex.y, point.vertex.z):
                return point
            else:
                self.alreadyCheckedPoints.add(point)

        # если смотрим в снайперский прицел (узкое поле зрения), то на экран может не попасть ни одна точка сферы
        return None
