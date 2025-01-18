from game.calc.Geometry import Geometry
from game.engine.GameData import GameData
from game.lib.Numeric import Numeric
from game.model.Orientation import Orientation


class PersonWallCollisionDetector:

    def __init__(self, gameData):
        self.gameData = gameData

    def getCollidedWalls(self, person):
        if not person.hasMoved:
            return []

        collidedWalls = []

        for levelSegment in person.collisionLevelSegments:
            for wall in levelSegment.horizontalVerticalWalls:
                if self.hasCollision(person, wall):
                    if wall not in collidedWalls:
                        collidedWalls.append(wall)

        for levelSegment in person.collisionLevelSegments:
            for wall in levelSegment.diagonalWalls:
                if self.hasCollision(person, wall):
                    if wall not in collidedWalls:
                        collidedWalls.append(wall)

        return collidedWalls

    def hasCollision(self, person, wall):
        currentBorder = person.currentBorder.bottom
        nextBorder = person.nextBorder.bottom
        # check corners
        result = self.personLineIntersectsWall(currentBorder.downLeft, nextBorder.downLeft, wall)
        result = result or self.personLineIntersectsWall(currentBorder.downRight, nextBorder.downRight, wall)
        result = result or self.personLineIntersectsWall(currentBorder.upLeft, nextBorder.upLeft, wall)
        result = result or self.personLineIntersectsWall(currentBorder.upRight, nextBorder.upRight, wall)
        # check middle
        result = result or self.personLineIntersectsWall(currentBorder.middleLeft, nextBorder.middleLeft, wall)
        result = result or self.personLineIntersectsWall(currentBorder.middleRight, nextBorder.middleRight, wall)
        result = result or self.personLineIntersectsWall(currentBorder.middleTop, nextBorder.middleTop, wall)
        result = result or self.personLineIntersectsWall(currentBorder.middleBottom, nextBorder.middleBottom, wall)

        return result

    def personLineIntersectsWall(self, personPointFrom, personPointTo, wall):
        if self.isPersonPointBehindWall(personPointTo, wall):
            intersectPoint = self.getWallIntersectPointOrNone(personPointFrom, personPointTo, wall)
            if intersectPoint is not None:
                if self.personLineContainsPoint(personPointFrom, personPointTo, intersectPoint) and self.wallContainsPoint(wall, intersectPoint):
                    return True

        return False

    def isPersonPointBehindWall(self, personPoint, wall):
        behindDirection = wall.startPoint.getDirectionTo(personPoint)
        dotProduct = behindDirection.dotProduct(wall.frontNormal)

        return dotProduct < 0

    def getWallIntersectPointOrNone(self, personPointFrom, personPointTo, wall):
        return Geometry.getLinesIntersectPointOrNone(
            wall.startPoint.x,
            wall.startPoint.y,
            wall.endPoint.x,
            wall.endPoint.y,
            personPointFrom.x,
            personPointFrom.y,
            personPointTo.x,
            personPointTo.y,
        )

    def personLineContainsPoint(self, personPointFrom, personPointTo, point):
        x, y = point
        return Geometry.lineContainsPoint(personPointFrom.x, personPointFrom.y, personPointTo.x, personPointTo.y, x, y)

    def wallContainsPoint(self, wall, point):
        x, y = point
        if wall.orientation == Orientation.horizontal:
            return Numeric.between(x, wall.startPoint.x, wall.endPoint.x) or Numeric.between(x, wall.endPoint.x, wall.startPoint.x)
        elif wall.orientation == Orientation.vertical:
            return Numeric.between(y, wall.startPoint.y, wall.endPoint.y) or Numeric.between(y, wall.endPoint.y, wall.startPoint.y)
        elif wall.orientation == Orientation.diagonal:
            return Geometry.lineContainsPoint(wall.startPoint.x, wall.startPoint.y, wall.endPoint.x, wall.endPoint.y, x, y)
        else:
            raise Exception("Wrong wall orientation.")


def makePersonWallCollisionDetector(resolver):
    return PersonWallCollisionDetector(resolver.resolve(GameData))
