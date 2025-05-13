from game.engine.cm.WallCollisionDetector import WallCollisionDetector


class PersonWallCollisionDetector:

    def __init__(self, wallCollisionDetector: WallCollisionDetector):
        self.wallCollisionDetector = wallCollisionDetector

    def getCollidedWalls(self, person):
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
        return self.wallCollisionDetector.lineIntersectsWall(personPointFrom, personPointTo, wall)
