from game.anx.CommonConstants import CommonConstants
from game.engine.CameraScopeChecker import CameraScopeChecker
from game.engine.GameState import GameState


class LevelSegmentVisibilityUpdater:

    def __init__(
        self,
        gameData: GameState,
        cameraScopeChecker: CameraScopeChecker,
    ):
        self.gameData = gameData
        self.cameraScopeChecker = cameraScopeChecker

    def updateIfPlayerMovedOrTurned(self):
        player = self.gameData.player
        if player.hasMoved or player.hasTurned:
            self.update()

    def update(self):
        self.gameData.visibleLevelSegments = set()
        self.checkedJoinLines = set()
        self.checkLevelSegment(self.gameData.player.visibilityLevelSegment)

    def checkLevelSegment(self, levelSegment):
        self.gameData.visibleLevelSegments.add(levelSegment)
        for joinLine in levelSegment.joinLines:
            if joinLine not in self.checkedJoinLines:
                self.checkedJoinLines.add(joinLine)
                if self.isJoinLineVisible(joinLine):
                    joinedLevelSegment = joinLine.getJoinedLevelSegment(levelSegment)
                    self.checkLevelSegment(joinedLevelSegment)

    def isJoinLineVisible(self, joinLine):
        for point in joinLine.points:
            if self.isPointVisible(point):
                return True

        return False

    def isPointVisible(self, point):
        direction = self.gameData.camera.position.getDirectionTo(point)
        if direction.getLength() > CommonConstants.maxDepth:
            return False

        pointInFront = self.gameData.camera.lookDirection.dotProduct(direction) > 0

        return pointInFront
