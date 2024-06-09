from game.calc.Geometry import Geometry
from game.anx.Constants import Constants
from game.engine.bsp.BSPTreeTraversal import BSPTreeTraversal
from game.engine.GameData import GameData


class LevelSegmentVisibilityUpdater:

    def __init__(self, gameData, traversal):
        self.gameData = gameData
        self.traversal = traversal

    def update(self):
        self.gameData.visibleLevelSegments = [self.gameData.playerLevelSegment]
        self.checkDirection(self.gameData.camera.lookDirection)
        viewAngleRadiansHalf = self.gameData.camera.viewAngleRadians / 2.0
        leftLookDirection = Geometry.rotatePoint(self.gameData.camera.lookDirection, Constants.zAxis, Constants.axisOrigin, -viewAngleRadiansHalf)
        self.checkDirection(leftLookDirection)
        rightLookDirection = Geometry.rotatePoint(self.gameData.camera.lookDirection, Constants.zAxis, Constants.axisOrigin, viewAngleRadiansHalf)
        self.checkDirection(rightLookDirection)

    def checkDirection(self, direction):
        depthLength = 5.0
        stepLength = 0.5
        stepsCount = depthLength / stepLength
        checkPoint = direction.getCopy()
        checkPoint.setLength(depthLength)
        checkPoint.add(self.gameData.camera.position)
        stepDirection = direction.getCopy()
        stepDirection.setLength(stepLength)
        playerFloor = self.gameData.level.floors[self.gameData.player.floorIndex]
        segment = self.traversal.findLevelSegmentOrNone(playerFloor.bspTree, checkPoint)
        stepNumber = 1
        while segment != self.gameData.playerLevelSegment and stepNumber < stepsCount:
            self.addVisibleSegment(segment)
            checkPoint.sub(stepDirection)
            segment = self.traversal.findLevelSegmentOrNone(playerFloor.bspTree, checkPoint)
            stepNumber += 1

    def addVisibleSegment(self, segment):
        if segment is not None and segment != self.gameData.visibleLevelSegments[-1]:
            self.gameData.visibleLevelSegments.append(segment)


def makeLevelSegmentVisibilityUpdater(resolver):
    return LevelSegmentVisibilityUpdater(resolver.resolve(GameData), resolver.resolve(BSPTreeTraversal))
