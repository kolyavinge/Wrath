from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.SphereSegmentCalculator import SphereSegmentCalculator
from game.engine.GameData import GameData


class BackgroundVisibilityDetector:

    def __init__(self, gameData, sphereSegmentCalculator):
        self.sphereRadius = CommonConstants.maxLevelSize
        self.gameData = gameData
        self.gameData.backgroundVisibility.horizontalPointsCount = 5
        self.gameData.backgroundVisibility.verticalPointsCount = 5
        self.sphereSegmentCalculator = sphereSegmentCalculator

    def updateIfPlayerMovedOrTurned(self):
        if self.gameData.player.hasMoved or self.gameData.player.hasTurned:
            self.update()

    def update(self):
        player = self.gameData.player
        camera = self.gameData.camera
        endPoint = player.lookDirection.copy()
        endPoint.setLength(2 * self.sphereRadius)
        endPoint.add(camera.position)

        centerPoint = Geometry.getSphereIntersectPointOrNone(self.sphereRadius, camera.position, endPoint)
        self.gameData.backgroundVisibility.vertices = self.sphereSegmentCalculator.getVertices(
            camera.position,
            centerPoint,
            player.rightNormal,
            camera.horizontalViewRadians,
            camera.verticalViewRadians,
            self.gameData.backgroundVisibility.horizontalPointsCount,
            self.gameData.backgroundVisibility.verticalPointsCount,
        )

        self.gameData.backgroundVisibility.texCoords = self.sphereSegmentCalculator.getTexCoords(
            player.yawRadians,
            player.pitchRadians,
            camera.horizontalViewRadians,
            camera.verticalViewRadians,
            self.gameData.backgroundVisibility.horizontalPointsCount,
            self.gameData.backgroundVisibility.verticalPointsCount,
        )


def makeBackgroundVisibilityDetector(resolver):
    return BackgroundVisibilityDetector(resolver.resolve(GameData), resolver.resolve(SphereSegmentCalculator))
