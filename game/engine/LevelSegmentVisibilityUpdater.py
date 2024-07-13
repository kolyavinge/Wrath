from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData
from game.lib.Math import Math


class LevelSegmentVisibilityUpdater:

    def __init__(self, gameData, traversal):
        self.gameData = gameData
        self.traversal = traversal
        self.maxCosLookDirection = Math.cos(2 * self.gameData.camera.viewAngleRadians)

    def update(self):
        player = self.gameData.player
        if player.hasMoved or player.hasTurned:
            self.gameData.visibleLevelSegments = set()
            checkedJoinLines = set()
            for levelSegment in player.visibilityLevelSegments:
                self.checkLevelSegment(levelSegment, checkedJoinLines)

    def checkLevelSegment(self, levelSegment, checkedJoinLines):
        self.gameData.visibleLevelSegments.add(levelSegment)
        for joinLine in levelSegment.joinLines:
            if joinLine not in checkedJoinLines:
                checkedJoinLines.add(joinLine)
                if self.isJoinLineVisible(joinLine):
                    joinedLevelSegment = joinLine.backLevelSegment if joinLine.frontLevelSegment == levelSegment else joinLine.frontLevelSegment
                    self.checkLevelSegment(joinedLevelSegment, checkedJoinLines)

    def isJoinLineVisible(self, joinLine):
        return self.isPointVisible(joinLine.middlePoint) or self.isPointVisible(joinLine.startPoint) or self.isPointVisible(joinLine.endPoint)

    def isPointVisible(self, endPoint):
        stepDirection = endPoint.getCopy()
        stepDirection.sub(self.gameData.camera.position)
        dotProduct = self.gameData.camera.lookDirection.dotProduct(stepDirection) / stepDirection.getLength()
        if dotProduct < self.maxCosLookDirection:
            return False
        stepLength = 0.5
        stepsCount = stepDirection.getLength() / stepLength
        stepDirection.setLength(stepLength)
        stepNumber = 0
        point = self.gameData.camera.position.getCopy()
        while stepNumber < stepsCount:
            levelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.level.visibilityTree, point)
            if levelSegment is None:
                return False
            point.add(stepDirection)
            stepNumber += 1

        return True


def makeLevelSegmentVisibilityUpdater(resolver):
    return LevelSegmentVisibilityUpdater(resolver.resolve(GameData), resolver.resolve(BSPTreeTraversal))
