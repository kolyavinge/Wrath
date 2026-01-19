from game.calc.Vector3 import Vector3
from game.engine.person.CameraScopeChecker import CameraScopeChecker
from game.lib.Math import Math


class BackgroundVisibilityUpdater:

    def __init__(
        self,
        cameraScopeChecker: CameraScopeChecker,
    ):
        self.cameraScopeChecker = cameraScopeChecker
        self.lookDirectionPoint = Vector3()
        self.alreadyCheckedPoints = set()
        self.lastPitchRadians = 0
        self.lastYawRadians = 0
        self.personTurnRadiansDelta = 0.1

    def updateIfNeeded(self, gameState):
        if self.needUpdate(gameState):
            self.lastPitchRadians = gameState.player.pitchRadians
            self.lastYawRadians = gameState.player.yawRadians
            self.update(gameState)

    def needUpdate(self, gameState):
        if gameState.camera.hasVerticalViewRadiansChanged:
            return True
        return (
            Math.abs(gameState.player.pitchRadians - self.lastPitchRadians) > self.personTurnRadiansDelta
            or Math.abs(gameState.player.yawRadians - self.lastYawRadians) > self.personTurnRadiansDelta
        )

    def update(self, gameState):
        backgroundVisibility = gameState.backgroundVisibility

        def checkVisiblePoint(point):
            for element in point.joinedElements:
                backgroundVisibility.visibleSphereElements.add(element)
                for joinedPoint in element.points:
                    if joinedPoint not in self.alreadyCheckedPoints:
                        self.alreadyCheckedPoints.add(joinedPoint)
                        if self.cameraScopeChecker.isPointInCamera(
                            gameState.camera,
                            joinedPoint.vertex.x,
                            joinedPoint.vertex.y,
                            joinedPoint.vertex.z,
                        ):
                            checkVisiblePoint(joinedPoint)
                        else:
                            for element in joinedPoint.joinedElements:
                                backgroundVisibility.visibleSphereElements.add(element)

        self.alreadyCheckedPoints.clear()
        point = self.getAnyVisiblePointOrNone(gameState)
        if point is not None:
            backgroundVisibility.visibleSphereElements = set()
            checkVisiblePoint(point)
        else:
            backgroundVisibility.visibleSphereElements = set(backgroundVisibility.sphere.elementsList)

    def getAnyVisiblePointOrNone(self, gameState):
        self.lookDirectionPoint.copyFrom(gameState.camera.lookDirection)
        self.lookDirectionPoint.mul(gameState.backgroundVisibility.sphere.radius)
        self.lookDirectionPoint.add(gameState.camera.position)
        spherePoints = gameState.backgroundVisibility.sphereBSPTree.findNodeItemsByPoint(self.lookDirectionPoint)
        for point in spherePoints:
            if self.cameraScopeChecker.isPointInCamera(gameState.camera, point.vertex.x, point.vertex.y, point.vertex.z):
                self.alreadyCheckedPoints.add(point)
                return point

        # если смотрим в снайперский прицел (узкое поле зрения), то на экран может не попасть ни одна точка сферы
        return None
