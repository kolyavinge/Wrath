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

