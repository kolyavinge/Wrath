from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.engine.GameData import GameData
from game.engine.LevelSegmentItemFinder import LevelSegmentItemFinder


class LevelSegmentVisibilityUpdater:

    def __init__(self, gameData, segmentItemFinder):
        self.gameData = gameData
        self.segmentItemFinder = segmentItemFinder

    def update(self):
        player = self.gameData.player
        if player.hasMoved or player.hasTurned:
            self.gameData.visibleLevelSegments = []
            camera = self.gameData.camera
            straightLookDirection = camera.lookDirection.getCopy()
            straightLookDirection.z = 0
            straightLookDirection.setLength(camera.viewDepth)
            self.checkDirection(straightLookDirection)
            radiansStep = camera.viewAngleRadians / 2
            radians = radiansStep
            while radians <= camera.viewAngleRadians:
                self.checkDirection(Geometry.rotatePoint(straightLookDirection, CommonConstants.zAxis, CommonConstants.axisOrigin, -radians))
                self.checkDirection(Geometry.rotatePoint(straightLookDirection, CommonConstants.zAxis, CommonConstants.axisOrigin, radians))
                self.checkDirection(Geometry.rotatePoint(straightLookDirection, CommonConstants.xAxis, CommonConstants.axisOrigin, -radians))
                self.checkDirection(Geometry.rotatePoint(straightLookDirection, CommonConstants.xAxis, CommonConstants.axisOrigin, radians))
                radians += radiansStep

    def checkDirection(self, direction):
        startPoint = self.gameData.camera.position
        endPoint = startPoint.getCopy()
        endPoint.add(direction)
        levelSegments = self.segmentItemFinder.getItemLevelSegments(self.gameData.level.visibilityTree, startPoint, endPoint)
        for levelSegment in levelSegments:
            if levelSegment not in self.gameData.visibleLevelSegments:
                self.gameData.visibleLevelSegments.append(levelSegment)


def makeLevelSegmentVisibilityUpdater(resolver):
    return LevelSegmentVisibilityUpdater(resolver.resolve(GameData), resolver.resolve(LevelSegmentItemFinder))
