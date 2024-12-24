from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.SphereSegment import SphereSegment
from game.engine.GameData import GameData


class BackgroundVisibilityDetector:

    def __init__(self, gameData):
        self.sphereRadius = CommonConstants.maxLevelSize
        self.gameData = gameData
        self.gameData.backgroundVisibility.horizontalPointsCount = 15
        self.gameData.backgroundVisibility.verticalPointsCount = 15

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
        segment = SphereSegment(
            camera.position,
            centerPoint,
            player.rightNormal,
            camera.viewAngleRadians * CommonConstants.screenAspect - 0.2,
            camera.viewAngleRadians - 0.1,
            self.gameData.backgroundVisibility.horizontalPointsCount,
            self.gameData.backgroundVisibility.verticalPointsCount,
        )
        self.gameData.backgroundVisibility.visiblePoints = segment.points


def makeBackgroundVisibilityDetector(resolver):
    return BackgroundVisibilityDetector(resolver.resolve(GameData))
