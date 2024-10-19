from game.calc.Geometry import Geometry
from game.calc.Plane import Plane
from game.calc.PlaneUtils import PlaneUtils
from game.lib.Math import Math
from game.model.level.BulletHole import BulletHole


class BulletHoleFactory:

    def make(self, collisionPoint, frontNormal):
        plane = Plane(frontNormal, collisionPoint)
        point1 = collisionPoint.getDirectionTo(PlaneUtils.getRandomPointOnPlane(plane))
        point1.setLength(BulletHole.halfSize)
        point1.add(collisionPoint)
        bulletHole = BulletHole()
        bulletHole.point1 = point1
        bulletHole.point2 = Geometry.rotatePoint(point1, frontNormal, collisionPoint, Math.piHalf)
        bulletHole.point3 = Geometry.rotatePoint(point1, frontNormal, collisionPoint, Math.pi)
        bulletHole.point4 = Geometry.rotatePoint(point1, frontNormal, collisionPoint, Math.threePiHalf)

        return bulletHole


def makeBulletHoleFactory(resolver):
    return BulletHoleFactory()
