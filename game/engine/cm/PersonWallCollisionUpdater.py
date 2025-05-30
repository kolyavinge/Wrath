from game.calc.Geometry import Geometry
from game.calc.Vector3 import Vector3
from game.engine.cm.PersonWallCollisionDetector import PersonWallCollisionDetector
from game.engine.GameData import GameData
from game.lib.Math import Math
from game.model.Orientation import Orientation


class PersonWallCollisionUpdater:

    def __init__(
        self,
        gameData: GameData,
        personWallCollisionDetector: PersonWallCollisionDetector,
    ):
        self.gameData = gameData
        self.personWallCollisionDetector = personWallCollisionDetector

    def update(self):
        for person in self.gameData.allPerson:
            if person.hasMoved:
                self.updatePersonCollisions(person)

    def updatePersonCollisions(self, person):
        collidedWalls = self.personWallCollisionDetector.getCollidedWalls(person)
        if len(collidedWalls) == 0:
            return

        self.gameData.collisionData.personWalls[person] = collidedWalls

        self.processWall(person, collidedWalls[0])

        for i in range(1, len(collidedWalls)):
            wall = collidedWalls[i]
            if self.personWallCollisionDetector.hasCollision(person, wall):
                self.processWall(person, wall)

    def processWall(self, person, wall):
        x, y = self.getPointOnLimitLine(wall, person.nextCenterPoint)
        newNextPosition = Vector3(Math.round(x, 2), Math.round(y, 2), person.getZ())
        person.moveNextPositionTo(newNextPosition)

    def getPointOnLimitLine(self, wall, personNextCenterPoint):
        if wall.orientation == Orientation.horizontal:
            return (personNextCenterPoint.x, wall.limitLine.startPoint.y)
        elif wall.orientation == Orientation.vertical:
            return (wall.limitLine.startPoint.x, personNextCenterPoint.y)
        elif wall.orientation == Orientation.diagonal:
            personDirection = wall.limitLine.startPoint.getDirectionTo(personNextCenterPoint)
            projected = Geometry.getProjectedVector(personDirection, wall.limitLineDirection)
            projected.add(wall.limitLine.startPoint)

            return (projected.x, projected.y)
        else:
            raise Exception("Wrong wall orientation.")
