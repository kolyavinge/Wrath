from game.calc.Vector3 import Vector3
from game.engine.CameraScopeChecker import CameraScopeChecker
from game.engine.GameState import GameState
from game.lib.Math import Math


class BackgroundVisibilityUpdater:

    def __init__(
        self,
        gameState: GameState,
        cameraScopeChecker: CameraScopeChecker,
    ):
        self.gameState = gameState
        self.cameraScopeChecker = cameraScopeChecker
        self.lookDirectionPoint = Vector3()
        self.alreadyCheckedPoints = set()
        self.lastPitchRadians = 0
        self.lastYawRadians = 0
        self.personTurnRadiansDelta = 0.1

    def updateIfNeeded(self):
        if self.needUpdate():
            self.lastPitchRadians = self.gameState.player.pitchRadians
            self.lastYawRadians = self.gameState.player.yawRadians
            self.update()

    def needUpdate(self):
        if self.gameState.camera.hasVerticalViewRadiansChanged:
            return True
        return (
            Math.abs(self.gameState.player.pitchRadians - self.lastPitchRadians) > self.personTurnRadiansDelta
            or Math.abs(self.gameState.player.yawRadians - self.lastYawRadians) > self.personTurnRadiansDelta
        )

    def update(self):

        def checkVisiblePoint(point):
            for element in point.joinedElements:
                self.gameState.backgroundVisibility.visibleSphereElements.add(element)
                for joinedPoint in element.points:
                    if joinedPoint not in self.alreadyCheckedPoints:
                        self.alreadyCheckedPoints.add(joinedPoint)
                        if self.cameraScopeChecker.isPointInCamera(joinedPoint.vertex.x, joinedPoint.vertex.y, joinedPoint.vertex.z):
                            checkVisiblePoint(joinedPoint)
                        else:
                            for element in joinedPoint.joinedElements:
                                self.gameState.backgroundVisibility.visibleSphereElements.add(element)

        self.alreadyCheckedPoints.clear()
        point = self.getAnyVisiblePointOrNone()
        if point is not None:
            self.gameState.backgroundVisibility.visibleSphereElements = set()
            checkVisiblePoint(point)
        else:
            self.gameState.backgroundVisibility.visibleSphereElements = set(self.gameState.backgroundVisibility.sphere.elementsList)

    def getAnyVisiblePointOrNone(self):
        self.lookDirectionPoint.copyFrom(self.gameState.camera.lookDirection)
        self.lookDirectionPoint.mul(self.gameState.backgroundVisibility.sphere.radius)
        self.lookDirectionPoint.add(self.gameState.camera.position)
        spherePoints = self.gameState.backgroundVisibility.sphereBSPTree.findNodeItemsByPoint(self.lookDirectionPoint)
        for point in spherePoints:
            if self.cameraScopeChecker.isPointInCamera(point.vertex.x, point.vertex.y, point.vertex.z):
                self.alreadyCheckedPoints.add(point)
                return point

        # если смотрим в снайперский прицел (узкое поле зрения), то на экран может не попасть ни одна точка сферы
        return None
