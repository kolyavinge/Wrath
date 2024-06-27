from game.anx.Constants import Constants
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
            self.gameData.visibleLevelSegments = player.levelSegments.copy()
            camera = self.gameData.camera
            straightLookDirection = camera.lookDirection.getCopy()
            straightLookDirection.z = 0
            straightLookDirection.setLength(20)
            leftLookDirection = Geometry.rotatePoint(straightLookDirection, Constants.zAxis, Constants.axisOrigin, -(camera.viewAngleRadiansHalf + 2))
            rightLookDirection = Geometry.rotatePoint(straightLookDirection, Constants.zAxis, Constants.axisOrigin, (camera.viewAngleRadiansHalf + 2))
            leftLookDirectionQ = Geometry.rotatePoint(straightLookDirection, Constants.zAxis, Constants.axisOrigin, -camera.viewAngleRadiansQuarter)
            rightLookDirectionQ = Geometry.rotatePoint(straightLookDirection, Constants.zAxis, Constants.axisOrigin, camera.viewAngleRadiansQuarter)
            self.checkDirection(straightLookDirection)
            self.checkDirection(leftLookDirection)
            self.checkDirection(rightLookDirection)
            self.checkDirection(leftLookDirectionQ)
            self.checkDirection(rightLookDirectionQ)

    def checkDirection(self, direction):
        camera = self.gameData.camera
        startPoint = camera.position
        endPoint = startPoint.getCopy()
        endPoint.add(direction)
        levelSegments = self.segmentItemFinder.getItemLevelSegments(self.gameData.level.bspTree, startPoint, endPoint)
        for levelSegment in levelSegments:
            self.gameData.visibleLevelSegments.append(levelSegment)


def makeLevelSegmentVisibilityUpdater(resolver):
    return LevelSegmentVisibilityUpdater(resolver.resolve(GameData), resolver.resolve(LevelSegmentItemFinder))
