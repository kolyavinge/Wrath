from game.anx.PersonConstants import PersonConstants
from game.engine.cm.ConstructionCollisionDetector import ConstructionCollisionDetector
from game.engine.GameData import GameData
from game.engine.level.LevelSegmentItemFinder import LevelSegmentItemFinder


class PersonWallCollisionDetector:

    def __init__(
        self,
        gameData: GameData,
        constructionCollisionDetector: ConstructionCollisionDetector,
        levelSegmentItemFinder: LevelSegmentItemFinder,
    ):
        self.gameData = gameData
        self.constructionCollisionDetector = constructionCollisionDetector
        self.levelSegmentItemFinder = levelSegmentItemFinder

    def getCollidedWalls(self, person):
        collidedWalls = []

        for levelSegment in person.collisionLevelSegments:
            for wall in levelSegment.horizontalVerticalWalls:
                if self.hasWallCollision(person, wall):
                    if wall not in collidedWalls:
                        collidedWalls.append(wall)

        for levelSegment in person.collisionLevelSegments:
            for wall in levelSegment.diagonalWalls:
                if self.hasWallCollision(person, wall):
                    if wall not in collidedWalls:
                        collidedWalls.append(wall)

        return collidedWalls

    def hasWallCollision(self, person, wall):
        currentBorder = person.currentBorder.bottom
        nextBorder = person.nextBorder.bottom
        # check corners
        result = self.isCollidedWall(wall, currentBorder.downLeft, nextBorder.downLeft)
        result = result or self.isCollidedWall(wall, currentBorder.downRight, nextBorder.downRight)
        result = result or self.isCollidedWall(wall, currentBorder.upLeft, nextBorder.upLeft)
        result = result or self.isCollidedWall(wall, currentBorder.upRight, nextBorder.upRight)
        # check middle
        result = result or self.isCollidedWall(wall, currentBorder.middleLeft, nextBorder.middleLeft)
        result = result or self.isCollidedWall(wall, currentBorder.middleRight, nextBorder.middleRight)
        result = result or self.isCollidedWall(wall, currentBorder.middleTop, nextBorder.middleTop)
        result = result or self.isCollidedWall(wall, currentBorder.middleBottom, nextBorder.middleBottom)

        return result

    def anyCollisions(self, linePointFrom, linePointTo, fromLevelSegment, toLevelSegment):

        def checkCollisionOrNone(walls, linePointFrom, linePointTo):
            for wall in walls:
                if self.isCollidedWall(wall, linePointFrom, linePointTo):
                    return True

            return None

        return (
            self.levelSegmentItemFinder.findItemOrNone(
                self.gameData.collisionTree,
                fromLevelSegment,
                toLevelSegment,
                linePointFrom,
                linePointTo,
                lambda segment, start, end: checkCollisionOrNone(segment.walls, start, end),
            )
            or False
        )

    def isCollidedWall(self, wall, linePointFrom, linePointTo):
        linePointFrom = linePointFrom.copy()
        linePointTo = linePointTo.copy()

        linePointFrom.z += PersonConstants.zFootLength
        linePointTo.z += PersonConstants.zFootLength

        return self.constructionCollisionDetector.isCollidedConstruction(wall, linePointFrom, linePointTo)
