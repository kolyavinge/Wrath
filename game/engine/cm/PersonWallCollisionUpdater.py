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
        self.gameData.collisionData.personWalls[person] = []
        collidedWall = self.personWallCollisionDetector.getCollidedWallOrNone(person)
        while collidedWall is not None:
            self.processWall(person, collidedWall)
            self.gameData.collisionData.personWalls[person].append(collidedWall)
            collidedWall = self.personWallCollisionDetector.getCollidedWallOrNone(person)
            assert collidedWall not in self.gameData.collisionData.personWalls[person]

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
