from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Plane import Plane
from game.lib.Math import Math


class RayOrientationLogic:

    def getVerticesOrientedToCamera(self, rayStartPosition, rayEndPosition, rayMainAxis, cameraPosition):
        rotatedCameraPosition = Geometry.rotatePoint(cameraPosition, rayMainAxis, rayStartPosition, Math.piHalf)
        plane = Plane.makeByThreePoints(rotatedCameraPosition, rayStartPosition, rayEndPosition)

        step = Geometry.rotatePoint(plane.getNormal(), rayMainAxis, CommonConstants.axisOrigin, Math.piHalf)
        step.setLength(1)

        p1 = rayStartPosition.copy()
        p2 = rayStartPosition.copy()
        p3 = rayEndPosition.copy()
        p4 = rayEndPosition.copy()

        p1.add(step)
        p2.sub(step)
        p3.add(step)
        p4.sub(step)

        return [p1, p2, p3, p4]
