from game.engine.GameData import GameData
from game.engine.LevelSegmentItemFinder import LevelSegmentItemFinder


class LevelSegmentVisibilityUpdater:

    def __init__(self, gameData, segmentItemFinder):
        self.gameData = gameData
        self.segmentItemFinder = segmentItemFinder

    def update(self):
        player = self.gameData.player
        if player.hasMoved or player.hasTurned:
            self.gameData.visibleLevelSegments = set()
            camera = self.gameData.camera
            for levelSegment in player.levelSegments:
                for joinLine in levelSegment.joinLines:
                    point = joinLine.middlePoint.getCopy()
                    point.sub(camera.position)
                    point.mul(2)
                    self.checkDirection(point)

    def checkDirection(self, direction):
        startPoint = self.gameData.camera.position
        endPoint = startPoint.getCopy()
        endPoint.add(direction)
        levelSegments = self.segmentItemFinder.getItemLevelSegments(self.gameData.level.visibilityTree, startPoint, endPoint)
        for levelSegment in levelSegments:
            self.gameData.visibleLevelSegments.add(levelSegment)


def makeLevelSegmentVisibilityUpdater(resolver):
    return LevelSegmentVisibilityUpdater(resolver.resolve(GameData), resolver.resolve(LevelSegmentItemFinder))
