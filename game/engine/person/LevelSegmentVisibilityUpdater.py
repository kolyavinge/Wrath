from game.anx.CommonConstants import CommonConstants
from game.engine.person.CameraScopeChecker import CameraScopeChecker


class LevelSegmentVisibilityUpdater:

    def __init__(
        self,
        cameraScopeChecker: CameraScopeChecker,
    ):
        self.cameraScopeChecker = cameraScopeChecker

    def update(self, gameState):
        gameState.visibleLevelSegments = set()
        self.checkedJoinLines = set()
        self.checkLevelSegment(gameState, gameState.player.visibilityLevelSegment)

    def checkLevelSegment(self, gameState, levelSegment):
        gameState.visibleLevelSegments.add(levelSegment)
        for joinLine in levelSegment.joinLines:
            if joinLine not in self.checkedJoinLines:
                self.checkedJoinLines.add(joinLine)
                if self.isJoinLineVisible(joinLine, gameState.camera):
                    joinedLevelSegment = joinLine.getJoinedLevelSegment(levelSegment)
                    self.checkLevelSegment(gameState, joinedLevelSegment)

    def isJoinLineVisible(self, joinLine, camera):
        for point in joinLine.points:
            if self.isPointVisible(point, camera):
                return True

        return False

    def isPointVisible(self, point, camera):
        direction = camera.position.getDirectionTo(point)
        if direction.getLength() > CommonConstants.maxDepth:
            return False

        pointInFront = camera.lookDirection.dotProduct(direction) > 0

        return pointInFront
