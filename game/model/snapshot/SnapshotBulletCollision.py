from game.calc.Vector3 import Vector3


class SnapshotBulletCollision:

    @staticmethod
    def make(damagedPersonId, bulletId, collisionPoint):
        collision = SnapshotBulletCollision()
        collision.damagedPersonId = damagedPersonId
        collision.bulletId = bulletId
        collision.collisionPoint = collisionPoint

        return collision

    def __init__(self):
        self.damagedPersonId = 0
        self.bulletId = 0
        self.collisionPoint = Vector3()

    def __eq__(self, value):
        return self.damagedPersonId == value.damagedPersonId and self.bulletId == value.bulletId and self.collisionPoint == value.collisionPoint

    def __hash__(self):
        return hash((self.damagedPersonId.__hash__(), self.bulletId.__hash__(), self.collisionPoint.__hash__()))

    def toBytes(self, writer):
        writer.write("iifff", self.damagedPersonId, self.bulletId, self.collisionPoint.x, self.collisionPoint.y, self.collisionPoint.z)

    @staticmethod
    def fromBytes(reader):
        collision = SnapshotBulletCollision()
        collision.damagedPersonId, collision.bulletId, collision.collisionPoint.x, collision.collisionPoint.y, collision.collisionPoint.z = (
            reader.read("iifff")
        )

        return collision
