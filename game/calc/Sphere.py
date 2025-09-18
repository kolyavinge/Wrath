from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Point2 import Point2
from game.calc.SphereElementHorizontalIterator import SphereElementHorizontalIterator
from game.calc.SphereElementVerticalIterator import SphereElementVerticalIterator
from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.lib.Numeric import Numeric
from game.lib.Query import Query


class SpherePoint:

    def __init__(self, vertex, texCoord):
        self.vertex = vertex
        self.texCoord = texCoord
        self.joinedElements = []


# четырехугольные элементы из которых состоит сфера
class SphereElement:

    def __init__(self, downLeft, downRight, upLeft, upRight):
        self.downLeft = downLeft
        self.downRight = downRight
        self.upLeft = upLeft
        self.upRight = upRight
        self.points = [downLeft, downRight, upRight, upLeft]  # против часовой стрелки
        self.joinedElementLeft = None
        self.joinedElementRight = None
        self.joinedElementUp = None
        self.joinedElementDown = None

    def anyPointWithVertex(self, vertex):
        for point in self.points:
            if point.vertex == vertex:
                return True

        return False


class Sphere:

    def __init__(self, radius, levelsCount, levelPointsCount, defaultRotation=None):
        if Numeric.isOdd(levelPointsCount):
            raise Exception("levelPointsCount must be an even number.")

        self.radius = radius
        self.levelsCount = levelsCount
        self.levelPointsCount = levelPointsCount
        self.points = {}
        self.elements = {}
        self.makeEquatorPoints()
        self.makeLevelPoints()
        self.makeElements()
        self.pointsCount = len(Query(self.points.values()).flatten().result)
        self.elementsCount = len(Query(self.elements.values()).flatten().result)
        self.elementsList = []
        self.joinPointsAndElements()
        self.joinElements()
        self.checkElementsCorrection()
        self.rotateIfNeeded(defaultRotation)

    def makeEquatorPoints(self):
        # точки на экваторе (нулевой уровень)
        levelPoints = []
        self.points[0] = levelPoints
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
            self.points[levelNumber] = levelPoints
            self.points[-levelNumber] = levelPointsInv
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

    def makeElements(self):
        for levelNumber in range(-self.levelsCount, self.levelsCount):
            self.elements[levelNumber] = []
            for i in range(0, self.levelPointsCount):
                element = SphereElement(
                    downLeft=self.points[levelNumber][i + 1],
                    downRight=self.points[levelNumber][i],
                    upRight=self.points[levelNumber + 1][i],
                    upLeft=self.points[levelNumber + 1][i + 1],
                )
                self.elements[levelNumber].append(element)

    def joinPointsAndElements(self):
        self.elementsList = Query(self.elements.values()).flatten().result
        for point in Query(self.points.values()).flatten().result:
            for element in self.elementsList:
                if element.anyPointWithVertex(point.vertex):
                    point.joinedElements.append(element)

    def joinElements(self):
        for levelNumber in range(-self.levelsCount, self.levelsCount):
            iter = SphereElementHorizontalIterator(self, levelNumber)
            iter.move()
            first = iter.current
            right = iter.current
            while iter.move():
                left = iter.current
                right.joinedElementLeft = left
                left.joinedElementRight = right
                right = left
            last = iter.current
            first.joinedElementRight = last
            last.joinedElementLeft = first

        for levelPointIndex in range(0, int(self.levelPointsCount / 2)):
            iter = SphereElementVerticalIterator(self, levelPointIndex)
            iter.move()
            first = iter.current
            down = iter.current
            while iter.move():
                up = iter.current
                down.joinedElementUp = up
                up.joinedElementDown = down
                down = up
            last = iter.current
            first.joinedElementDown = last
            last.joinedElementUp = first

    def rotateIfNeeded(self, defaultRotation):
        if defaultRotation is None:
            return
        radians, axis = defaultRotation
        for point in Query(self.points.values()).flatten().result:
            point.vertex = Geometry.rotatePoint(point.vertex, axis, CommonConstants.axisOrigin, radians)

    def getAllSpherePoints(self):
        return Query(self.points.values()).flatten().result

    def checkElementsCorrection(self):
        for points in self.points.values():
            for point in points:
                assert len(point.joinedElements) == 4 or len(point.joinedElements) == self.levelPointsCount

        for elements in self.elements.values():
            for element in elements:
                assert element.joinedElementLeft is not None
                assert element.joinedElementRight is not None
                assert element.joinedElementUp is not None
                assert element.joinedElementDown is not None
