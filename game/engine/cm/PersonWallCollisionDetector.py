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

    def getCollidedWallOrNone(self, person):
        for levelSegment in person.collisionLevelSegments:
            collidedWall = self.getCollidedWallForPerson(person, levelSegment.horizontalVerticalWalls)
            if collidedWall is not None:
                return collidedWall

        for levelSegment in person.collisionLevelSegments:
            collidedWall = self.getCollidedWallForPerson(person, levelSegment.diagonalWalls)
            if collidedWall is not None:
                return collidedWall

        return None

    def getCollidedWallForPerson(self, person, walls):
        currentBorder = person.currentBorder.bottom
        nextBorder = person.nextBorder.bottom
        # check corners
        result = self.getCollidedWallInLine(walls, currentBorder.downLeft, nextBorder.downLeft)
        result = result or self.getCollidedWallInLine(walls, currentBorder.downRight, nextBorder.downRight)
        result = result or self.getCollidedWallInLine(walls, currentBorder.upLeft, nextBorder.upLeft)
        result = result or self.getCollidedWallInLine(walls, currentBorder.upRight, nextBorder.upRight)
        # check middle
        result = result or self.getCollidedWallInLine(walls, currentBorder.middleLeft, nextBorder.middleLeft)
        result = result or self.getCollidedWallInLine(walls, currentBorder.middleRight, nextBorder.middleRight)
        result = result or self.getCollidedWallInLine(walls, currentBorder.middleTop, nextBorder.middleTop)
        result = result or self.getCollidedWallInLine(walls, currentBorder.middleBottom, nextBorder.middleBottom)

        return result

    def getCollidedWallInLine(self, walls, linePointFrom, linePointTo):
        linePointFrom = linePointFrom.copy()
        linePointTo = linePointTo.copy()

        linePointFrom.z += 0.2
        linePointTo.z += 0.2

        return self.constructionCollisionDetector.getCollidedConstructionOrNone(walls, linePointFrom, linePointTo)

    def anyCollisions(self, linePointFrom, linePointTo, fromLevelSegment, toLevelSegment):

        def checkCollisionOrNone(walls, linePointFrom, linePointTo):
            if self.getCollidedWallInLine(walls, linePointFrom, linePointTo) is not None:
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

        linePointFrom.z += 0.2
        linePointTo.z += 0.2

        return self.constructionCollisionDetector.isCollidedConstruction(wall, linePointFrom, linePointTo)
