from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Point2 import Point2
from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.lib.Query import Query


class SpherePoint:

    def __init__(self, vertex, texCoord):
        self.vertex = vertex
        self.texCoord = texCoord
        self.joinedElements = []


# четырехугольник (элементы из которых состоит сфера)
class SphereElement:

    def __init__(self, points):
        self.points = points

    def anyPointWithVertex(self, vertex):
        for point in self.points:
            if point.vertex == vertex:
                return True

        return False


class Sphere:

    def __init__(self, radius, levelsCount, levelPointsCount, defaultRotation=None):
        self.radius = radius
        self.radiusHalf = radius / 2
        self.levelsCount = levelsCount
        self.levelPointsCount = levelPointsCount
        self.levels = {}
        self.makeEquatorPoints()
        self.makeLevelPoints()
        self.joinPointsAndElements()
        self.checkElementsCorrection()
        self.rotateIfNeeded(defaultRotation)

    def makeEquatorPoints(self):
        # точки на экваторе (нулевой уровень)
        levelPoints = []
        self.levels[0] = levelPoints
        z = 0.0
        radianStep = Math.piDouble / self.levelPointsCount
        textureXStep = 1.0 / self.levelPointsCount
        for levelPointNumber in range(0, self.levelPointsCount):
            radians = levelPointNumber * radianStep
            x = self.radius * Math.cos(radians)
            y = self.radius * Math.sin(radians)
            tx = 1.0 - levelPointNumber * textureXStep
            levelPoints.append(SpherePoint(Vector3(x, y, z), Point2(tx, 0.5)))
        # доп точка соединяющая начало и конец одного уровня сферы
        # нужна для более удобного наложения текстуры
        levelPoints.append(SpherePoint(Vector3(self.radius, 0.0, z), Point2(0.0, 0.5)))

    def makeLevelPoints(self):
        # точки на уровнях выше и ниже экватора
        radianStep = Math.piDouble / self.levelPointsCount
        textureXStep = 1.0 / self.levelPointsCount
        for levelNumber in range(1, self.levelsCount + 1):
            levelPoints = []
            levelPointsInv = []
            self.levels[levelNumber] = levelPoints
            self.levels[-levelNumber] = levelPointsInv
            z = levelNumber * (self.radius / self.levelsCount)
            ty = levelNumber * (0.5 / self.levelsCount)
            levelRadius = Math.sqrt(self.radius * self.radius - z * z)
            for levelPointNumber in range(0, self.levelPointsCount):
                radians = levelPointNumber * radianStep
                x = levelRadius * Math.cos(radians)
                y = levelRadius * Math.sin(radians)
                tx = 1.0 - levelPointNumber * textureXStep
                levelPoints.append(SpherePoint(Vector3(x, y, z), Point2(tx, 0.5 + ty)))
                levelPointsInv.append(SpherePoint(Vector3(x, y, -z), Point2(tx, 0.5 - ty)))
            # доп точки
            levelPoints.append(SpherePoint(Vector3(levelRadius, 0.0, z), Point2(0.0, 0.5 + ty)))
            levelPointsInv.append(SpherePoint(Vector3(levelRadius, 0.0, -z), Point2(0.0, 0.5 - ty)))

    def joinPointsAndElements(self):
        self.elements = list(self.makeElements())
        for point in Query(self.levels.values()).flatten().result:
            for element in self.elements:
                if element.anyPointWithVertex(point.vertex):
                    point.joinedElements.append(element)

    def makeElements(self):
        for levelNumber in range(-self.levelsCount, self.levelsCount):
            for i in range(0, self.levelPointsCount):
                yield SphereElement(
                    [
                        self.levels[levelNumber][i + 1],
                        self.levels[levelNumber][i],
                        self.levels[levelNumber + 1][i],
                        self.levels[levelNumber + 1][i + 1],
                    ]
                )

    def rotateIfNeeded(self, defaultRotation):
        if defaultRotation is None:
            return
        radians, axis = defaultRotation
        for point in Query(self.levels.values()).flatten().result:
            point.vertex = Geometry.rotatePoint(point.vertex, axis, CommonConstants.axisOrigin, radians)

    def getAllSpherePoints(self):
        return Query(self.levels.values()).flatten().result

    def checkElementsCorrection(self):
        for points in self.levels.values():
            for point in points:
                assert len(point.joinedElements) == 4 or len(point.joinedElements) == self.levelPointsCount
