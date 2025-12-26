from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Plane import Plane
from game.lib.Math import Math


class PlaneOrientationLogic:

    def getVerticesOrientedToCamera(self, startPosition, endPosition, mainAxis, cameraPosition):
        rotatedCameraPosition = Geometry.rotatePoint(cameraPosition, mainAxis, startPosition, Math.piHalf)
        plane = Plane.makeByThreePoints(rotatedCameraPosition, startPosition, endPosition)

        step = Geometry.rotatePoint(plane.getNormal(), mainAxis, CommonConstants.axisOrigin, Math.piHalf)
        step.setLength(1)

        p1 = startPosition.copy()
        p2 = startPosition.copy()
        p3 = endPosition.copy()
        p4 = endPosition.copy()

        p1.add(step)
        p2.sub(step)
        p3.add(step)
        p4.sub(step)

        return [p1, p2, p3, p4]
