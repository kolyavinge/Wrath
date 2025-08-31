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
        result = False

        current = person.currentFootRect
        next = person.nextFootRect

        dx = next.center.x - current.center.x
        dy = next.center.y - current.center.y

        if dy > 0:
            result = result or self.isCollidedWall(wall, current.upLeft, next.upLeft)
            result = result or self.isCollidedWall(wall, current.upRight, next.upRight)
            result = result or self.isCollidedWall(wall, current.middleTop, next.middleTop)

        if dy < 0:
            result = result or self.isCollidedWall(wall, current.downLeft, next.downLeft)
            result = result or self.isCollidedWall(wall, current.downRight, next.downRight)
            result = result or self.isCollidedWall(wall, current.middleBottom, next.middleBottom)

        if dx < 0:
            result = result or self.isCollidedWall(wall, current.downLeft, next.downLeft)
            result = result or self.isCollidedWall(wall, current.upLeft, next.upLeft)
            result = result or self.isCollidedWall(wall, current.middleLeft, next.middleLeft)

        if dx > 0:
            result = result or self.isCollidedWall(wall, current.downRight, next.downRight)
            result = result or self.isCollidedWall(wall, current.upRight, next.upRight)
            result = result or self.isCollidedWall(wall, current.middleRight, next.middleRight)

        return result

    def anyCollisions(self, startPoint, endPoint, startLevelSegment, endLevelSegment):

        def checkCollisionOrNone(walls, start, end):
            for wall in walls:
                if self.isCollidedWall(wall, start, end):
                    return True

            return None

        return (
            self.levelSegmentItemFinder.findItemOrNone(
                self.gameData.collisionTree,
                startLevelSegment,
                endLevelSegment,
                startPoint,
                endPoint,
                lambda segment, start, end: checkCollisionOrNone(segment.walls, start, end),
            )
            or False
        )

    def isCollidedWall(self, wall, startPoint, endPoint):
        return self.constructionCollisionDetector.isCollidedConstruction(wall, startPoint, endPoint, 0.01)
