from game.calc.Vector3 import Vector3


class SnapshotRayCollision:

    @staticmethod
    def make(damagedPersonId, rayId, collisionPoint):
        collision = SnapshotRayCollision()
        collision.damagedPersonId = damagedPersonId
        collision.rayId = rayId
        collision.collisionPoint = collisionPoint

        return collision

    def __init__(self):
        self.damagedPersonId = 0
        self.rayId = 0
        self.collisionPoint = Vector3()

    def __eq__(self, value):
        return self.damagedPersonId == value.damagedPersonId and self.rayId == value.rayId and self.collisionPoint == value.collisionPoint

    def __hash__(self):
        return hash((self.damagedPersonId.__hash__(), self.rayId.__hash__(), self.collisionPoint.__hash__()))

    def toBytes(self, writer):
        writer.write("iifff", self.damagedPersonId, self.rayId, self.collisionPoint.x, self.collisionPoint.y, self.collisionPoint.z)

    @staticmethod
    def fromBytes(reader):
        collision = SnapshotRayCollision()
        collision.damagedPersonId, collision.rayId, collision.collisionPoint.x, collision.collisionPoint.y, collision.collisionPoint.z = reader.read(
            "iifff"
        )

        return collision
