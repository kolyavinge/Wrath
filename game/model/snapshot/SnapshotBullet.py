from game.calc.Vector3 import Vector3


class SnapshotBullet:

    def __init__(self):
        self.id = 0
        self.personId = 0
        self.weaponNumber = 0
        self.position = Vector3()
        self.direction = Vector3()
