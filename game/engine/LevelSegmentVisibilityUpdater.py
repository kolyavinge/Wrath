from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData
from game.lib.Math import Math


class LevelSegmentVisibilityUpdater:

    def __init__(self, gameData, traversal):
        self.gameData = gameData
        self.traversal = traversal
        self.maxCosLookDirection = Math.cos(self.gameData.camera.viewAngleRadians)

    def update(self):
        player = self.gameData.player
        if player.hasMoved or player.hasTurned:
            self.gameData.visibleLevelSegments = set()
            checkedJoinLines = set()
            self.cameraLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.level.visibilityTree, self.gameData.camera.position)
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
        for point in joinLine.points:
            if self.isPointVisible(point):
                return True

        return False

    def isPointVisible(self, point):
        startPoint = self.gameData.camera.position
        endPoint = point
        direction = endPoint.getDirectionTo(startPoint)

        direction2d = direction.copy()
        direction2d.z = 0
        direction2d.normalize()

        look2d = self.gameData.camera.lookDirection.copy()
        look2d.z = 0
        look2d.normalize()

        dotProduct = look2d.dotProduct(direction2d)
        if dotProduct < self.maxCosLookDirection:
            return False

        while direction.getLength() > 1:
            direction.div(2)
            middlePoint = startPoint.copy()
            middlePoint.add(direction)
            middleLevelSegment = self.traversal.findLevelSegmentOrNone(self.gameData.level.visibilityTree, middlePoint)
            if middleLevelSegment is None:
                return False
            elif self.cameraLevelSegment == middleLevelSegment:
                startPoint = middlePoint
            else:
                endPoint = middlePoint

        return True


def makeLevelSegmentVisibilityUpdater(resolver):
    return LevelSegmentVisibilityUpdater(resolver.resolve(GameData), resolver.resolve(BSPTreeTraversal))
