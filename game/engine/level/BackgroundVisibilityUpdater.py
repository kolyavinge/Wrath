from game.calc.Vector3 import Vector3
from game.engine.CameraScopeChecker import CameraScopeChecker
from game.engine.GameData import GameData
from game.lib.Math import Math


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
        self.lastPitchRadians = 0
        self.lastYawRadians = 0
        self.personTurnRadiansDelta = 0.1

    def updateIfNeeded(self):
        if self.needUpdate():
            self.lastPitchRadians = self.gameData.player.pitchRadians
            self.lastYawRadians = self.gameData.player.yawRadians
            self.update()

    def needUpdate(self):
        if self.gameData.camera.hasVerticalViewRadiansChanged:
            return True
        return (
            Math.abs(self.gameData.player.pitchRadians - self.lastPitchRadians) > self.personTurnRadiansDelta
            or Math.abs(self.gameData.player.yawRadians - self.lastYawRadians) > self.personTurnRadiansDelta
        )

    def update(self):

        def checkVisiblePoint(point):
            for element in point.joinedElements:
                self.gameData.backgroundVisibility.visibleSphereElements.add(element)
                for joinedPoint in element.points:
                    if joinedPoint not in self.alreadyCheckedPoints:
                        self.alreadyCheckedPoints.add(joinedPoint)
                        if self.cameraScopeChecker.isPointInCamera(joinedPoint.vertex.x, joinedPoint.vertex.y, joinedPoint.vertex.z):
                            checkVisiblePoint(joinedPoint)
                        else:
                            for element in joinedPoint.joinedElements:
                                self.gameData.backgroundVisibility.visibleSphereElements.add(element)

        self.alreadyCheckedPoints.clear()
        point = self.getAnyVisiblePointOrNone()
        if point is not None:
            self.gameData.backgroundVisibility.visibleSphereElements = set()
            checkVisiblePoint(point)

    def getAnyVisiblePointOrNone(self):
        lookDirection = self.gameData.camera.lookDirection
        self.lookDirectionPoint.set(lookDirection.x, lookDirection.y, lookDirection.z)
        self.lookDirectionPoint.mul(self.gameData.backgroundVisibility.sphere.radius)
        self.lookDirectionPoint.add(self.gameData.camera.position)
        spherePoints = self.gameData.backgroundVisibility.sphereBSPTree.findNodeItemsByPoint(self.lookDirectionPoint)
        for point in spherePoints:
            if self.cameraScopeChecker.isPointInCamera(point.vertex.x, point.vertex.y, point.vertex.z):
                self.alreadyCheckedPoints.add(point)
                return point

        # если смотрим в снайперский прицел (узкое поле зрения), то на экран может не попасть ни одна точка сферы
        return None
