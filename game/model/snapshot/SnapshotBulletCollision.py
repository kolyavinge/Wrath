from game.calc.Vector3 import Vector3


class SnapshotBulletCollision:

    def __init__(self, damagedPersonId=0, bulletId=0, collisionPoint=Vector3()):
        self.damagedPersonId = damagedPersonId
        self.bulletId = bulletId
        self.collisionPoint = collisionPoint

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
