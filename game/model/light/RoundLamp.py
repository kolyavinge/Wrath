from game.calc.Geometry import Geometry
from game.calc.Plane import Plane
from game.calc.PlaneUtils import PlaneUtils
from game.lib.Math import Math
from game.model.light.Lamp import Lamp


class RoundLamp(Lamp):

    def __init__(self):
        super().__init__()
        self.radius = 0
        self.height = 0

    def getPoints(self):
        plane = Plane(self.frontNormal, self.position)
        basePoint = PlaneUtils.getRandomPointOnPlane(plane)
        basePoint.sub(self.position)
        basePoint.setLength(self.radius)
        basePoint.add(self.position)
        pointsCount = 16
        radians = Math.piDouble / pointsCount
        heightDirection = self.frontNormal.copy()
        heightDirection.setLength(self.height)

        resultBasePoints = []
        resultFrontPoints = []
        resultNormals = []
        for _ in range(0, pointsCount):
            basePoint = Geometry.rotatePoint(basePoint, self.frontNormal, self.position, radians)
            resultBasePoints.append(basePoint)
            frontPoint = basePoint.copy()
            frontPoint.add(heightDirection)
            resultFrontPoints.append(frontPoint)
            normal = self.position.getDirectionTo(basePoint)
            normal.normalize()
            resultNormals.append(normal)

        resultBasePoints.append(resultBasePoints[0])
        resultFrontPoints.append(resultFrontPoints[0])
        resultNormals.append(resultNormals[0])

        return (resultBasePoints, resultFrontPoints, resultNormals)
