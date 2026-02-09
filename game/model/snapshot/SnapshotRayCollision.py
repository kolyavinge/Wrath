from game.calc.Vector3 import Vector3


class SnapshotRayCollision:

    def __init__(self, damagedPersonId=0, rayId=0, collisionPoint=Vector3()):
        self.damagedPersonId = damagedPersonId
        self.rayId = rayId
        self.collisionPoint = collisionPoint

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
