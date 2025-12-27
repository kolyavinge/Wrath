from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Plane import Plane
from game.lib.Math import Math


class PlaneOrientationLogic:

    def getVerticesOrientedToCamera(self, startPosition, endPosition, mainAxis, cameraPosition, planeWidth=1.0):
        rotatedCameraPosition = Geometry.rotatePoint(cameraPosition, mainAxis, startPosition, Math.piHalf)
        plane = Plane.makeByThreePoints(rotatedCameraPosition, startPosition, endPosition)

        step = Geometry.rotatePoint(plane.getNormal(), mainAxis, CommonConstants.axisOrigin, Math.piHalf)
        step.setLength(planeWidth)

        nearLeft = startPosition.copy()
        nearRight = startPosition.copy()
        farRight = endPosition.copy()
        farLeft = endPosition.copy()

        nearLeft.add(step)
        nearRight.sub(step)
        farRight.sub(step)
        farLeft.add(step)

        # от точки nearLeft (ближняя левая) обходим остальные против часовой стрелки

        return [nearLeft, nearRight, farRight, farLeft]
