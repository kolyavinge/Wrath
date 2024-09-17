from game.anx.CommonConstants import CommonConstants
from game.engine.GameData import GameData
from game.lib.Math import Math


class LevelSegmentVisibilityUpdater:

    def __init__(self, gameData):
        self.gameData = gameData
        self.maxCosLookDirection = Math.cos(self.gameData.camera.viewAngleRadians)

    def updateIfPlayerMovedOrTurned(self):
        player = self.gameData.player
        if player.hasMoved or player.hasTurned:
            self.update()
            # print(len(self.gameData.visibleLevelSegments))

    def update(self):
        self.gameData.visibleLevelSegments = set()
        self.checkedJoinLines = set()
        for levelSegment in self.gameData.player.visibilityLevelSegments:
            self.checkLevelSegment(levelSegment)

    def checkLevelSegment(self, levelSegment):
        self.gameData.visibleLevelSegments.add(levelSegment)
        for joinLine in levelSegment.joinLines:
            if joinLine not in self.checkedJoinLines:
                self.checkedJoinLines.add(joinLine)
                if self.isJoinLineVisible(joinLine):
                    joinedLevelSegment = joinLine.backLevelSegment if joinLine.frontLevelSegment == levelSegment else joinLine.frontLevelSegment
                    self.checkLevelSegment(joinedLevelSegment)

    def isJoinLineVisible(self, joinLine):
        for point in joinLine.points:
            if self.isPointVisible(point):
                return True

        return False

    def isPointVisible(self, point):
        startPoint = self.gameData.camera.position
        endPoint = point
        direction = startPoint.getDirectionTo(endPoint)
        directionLength = direction.getLength()
        if directionLength > CommonConstants.maxViewDepth:
            return False
        if directionLength < 1:
            return True

        direction2d = direction.copy()
        direction2d.z = 0
        direction2d.normalize()

        look2d = self.gameData.camera.lookDirection.copy()
        look2d.z = 0
        look2d.normalize()

        dotProduct = look2d.dotProduct(direction2d)
        return dotProduct > self.maxCosLookDirection


def makeLevelSegmentVisibilityUpdater(resolver):
    return LevelSegmentVisibilityUpdater(resolver.resolve(GameData))
