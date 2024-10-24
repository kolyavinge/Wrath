from game.calc.Geometry import Geometry
from game.calc.Plane import Plane
from game.calc.PlaneUtils import PlaneUtils
from game.lib.Math import Math
from game.model.weapon.BulletHole import BulletHole


class BulletHoleFactory:

    def make(self, collisionPoint, frontNormal, levelSegment, bulletHoleInfo):
        bulletHole = BulletHole(bulletHoleInfo)
        plane = Plane(frontNormal, collisionPoint)
        point1 = collisionPoint.getDirectionTo(PlaneUtils.getRandomPointOnPlane(plane))
        point1.setLength(bulletHole.halfSize)
        point1.add(collisionPoint)
        bulletHole.frontNormal = frontNormal
        bulletHole.point1 = point1
        bulletHole.point2 = Geometry.rotatePoint(point1, frontNormal, collisionPoint, Math.piHalf)
        bulletHole.point3 = Geometry.rotatePoint(point1, frontNormal, collisionPoint, Math.pi)
        bulletHole.point4 = Geometry.rotatePoint(point1, frontNormal, collisionPoint, Math.threePiHalf)
        bulletHole.levelSegment = levelSegment

        return bulletHole


def makeBulletHoleFactory(resolver):
    return BulletHoleFactory()
