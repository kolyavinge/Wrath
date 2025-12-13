from game.anx.CommonConstants import CommonConstants
from game.anx.PersonConstants import PersonConstants
from game.calc.RectPlane import RectPlane
from game.calc.Vector3 import Vector3
from game.engine.cm.PlaneCollisionDetector import PlaneCollisionDetector
from game.engine.cm.SphereCollisionDetector import SphereCollisionDetector
from game.model.person.PersonStates import LifeCycle


class PersonCollisionTarget:

    body = 1
    head = 2


class PersonCollisionDetector:

    def __init__(
        self,
        planeCollisionDetector: PlaneCollisionDetector,
        sphereCollisionDetector: SphereCollisionDetector,
    ):
        self.planeCollisionDetector = planeCollisionDetector
        self.sphereCollisionDetector = sphereCollisionDetector
        self.xNormal = Vector3(1, 0, 0)
        self.yNormal = Vector3(0, 1, 0)

    def getCollisionLengthOrNone(self, person1, person2):
        if person1.lifeCycle == LifeCycle.alive and person2.lifeCycle == LifeCycle.alive:
            return self.getCollisionLengthBetweenPointsOrNone(person1.nextCenterPoint, person2.nextCenterPoint)
        else:
            return None

    def getCollisionLengthBetweenPointsOrNone(self, point1, point2):
        # пересечение окружностей
        collisionLength = PersonConstants.xyLength - point1.getLengthTo(point2)
        return collisionLength if collisionLength > 0 else None

    def getNearestCollisionResultOrNone(self, excludedPerson, allPerson, startPoint, endPoint):
        result = None
        nearestLength = CommonConstants.maxLevelSize
        for person in allPerson:
            collisionResult = self.getCollisionResultForPersonOrNone(excludedPerson, person, startPoint, endPoint)
            if collisionResult is None:
                continue
            collisionPoint, target = collisionResult
            length = startPoint.getLengthTo(collisionPoint)
            if length < nearestLength:
                result = (collisionPoint, person, target)
                nearestLength = length

        return result

    def getAllCollisionResultOrNone(self, excludedPerson, allPerson, startPoint, endPoint):
        result = []
        for person in allPerson:
            collisionResult = self.getCollisionResultForPersonOrNone(excludedPerson, person, startPoint, endPoint)
            if collisionResult is not None:
                collisionPoint, target = collisionResult
                result.append((collisionPoint, person, target))

        return result if len(result) > 0 else None

    def getCollisionResultForPersonOrNone(self, excludedPerson, person, startPoint, endPoint):
        if person == excludedPerson:
            return None
        if person.lifeCycle != LifeCycle.alive:
            return None

        # check body (two cross planes)
        border = person.nextBodyBorder
        plane = RectPlane(self.xNormal, border.bottom.middleBottom, border.bottom.middleTop, border.top.middleBottom, border.top.middleTop)
        collisionPoint = self.planeCollisionDetector.getRectPlaneCollisionPointOrNone(startPoint, endPoint, plane, 0.1)
        target = PersonCollisionTarget.body
        if collisionPoint is None:
            plane = RectPlane(self.yNormal, border.bottom.middleRight, border.bottom.middleLeft, border.top.middleRight, border.top.middleLeft)
            collisionPoint = self.planeCollisionDetector.getRectPlaneCollisionPointOrNone(startPoint, endPoint, plane, 0.1)

        # check head (sphere)
        if collisionPoint is None:
            collisionPoint = self.sphereCollisionDetector.getCollisionPointOrNone(
                startPoint, endPoint, person.headCenterPoint, PersonConstants.headSize, 0.1
            )
            target = PersonCollisionTarget.head

        if collisionPoint is not None:
            return (collisionPoint, target)

        return None
