from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.SphereSegmentCalculator import SphereSegmentCalculator
from game.engine.GameData import GameData
from game.tools.CpuProfiler import cpuProfile


class BackgroundVisibilityUpdater:

    def __init__(
        self,
        gameData: GameData,
        sphereSegmentCalculator: SphereSegmentCalculator,
    ):
        self.sphereRadius = CommonConstants.maxLevelSize
        self.gameData = gameData
        self.gameData.backgroundVisibility.horizontalPointsCount = 7
        self.gameData.backgroundVisibility.verticalPointsCount = 5
        self.sphereSegmentCalculator = sphereSegmentCalculator

    def updateIfPlayerMovedOrTurned(self):
        if self.gameData.player.hasMoved or self.gameData.player.hasTurned or self.gameData.camera.hasVerticalViewRadiansChanged:
            self.update()

    # @cpuProfile
    def update(self):
        player = self.gameData.player
        camera = self.gameData.camera
        endPoint = player.lookDirection.copy()
        endPoint.mul(2 * self.sphereRadius)
        endPoint.add(camera.position)

        centerPoint = Geometry.getSphereIntersectPointOrNone(self.sphereRadius, camera.position, endPoint, 100.0)
        self.gameData.backgroundVisibility.vertices = self.sphereSegmentCalculator.getVertices(
            camera.position,
            centerPoint,
            player.rightNormal,
            camera.horizontalViewRadians + 0.1,
            camera.verticalViewRadians + 0.2,
            self.gameData.backgroundVisibility.horizontalPointsCount,
            self.gameData.backgroundVisibility.verticalPointsCount,
        )

        self.gameData.backgroundVisibility.texCoords = self.sphereSegmentCalculator.getTexCoords(
            player.yawRadians,
            player.pitchRadians,
            camera.horizontalViewRadians + 0.1,
            camera.verticalViewRadians + 0.2,
            self.gameData.backgroundVisibility.horizontalPointsCount,
            self.gameData.backgroundVisibility.verticalPointsCount,
        )
