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

    def updateIfPlayerMovedOrTurned(self):
        if self.gameData.player.hasMoved or self.gameData.player.hasTurned or self.gameData.camera.hasVerticalViewRadiansChanged:
            self.update()

    # @cpuProfile
    def update(self):
        player = self.gameData.player
        camera = self.gameData.camera
        endPoint = player.lookDirection.copy()
        endPoint.add(camera.position)
        self.gameData.backgroundVisibility.visibleSphereElements = self.getVisibleElements()

    def getVisibleElements(self):
        alreadyCheckedPoints = set()
        visibleElements = set()

        def check(point):
            alreadyCheckedPoints.add(point)
            for element in point.joinedElements:
                visibleElements.add(element)
                for joinedPoint in element.points:
                    if joinedPoint not in alreadyCheckedPoints and self.cameraScopeChecker.isPointInCamera(
                        joinedPoint.vertex.x,
                        joinedPoint.vertex.y,
                        joinedPoint.vertex.z,
                        scale=1.5,
                    ):
                        check(joinedPoint)

        check(self.getAnyVisiblePoint())
        # print(len(visibleElements))

        return visibleElements

    def getAnyVisiblePoint(self):
        sphere = self.gameData.backgroundVisibility.sphere
        for points in sphere.levels.values():
            for point in points:
                if self.cameraScopeChecker.isPointInCamera(point.vertex.x, point.vertex.y, point.vertex.z):
                    return point

        assert False
