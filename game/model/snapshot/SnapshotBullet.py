from game.calc.Vector3 import Vector3


class WeaponExtraBit:

    leftHandWeapon = 1 << 7


class SnapshotBullet:

    @staticmethod
    def make(id, personId, weaponNumber, position, direction):
        bullet = SnapshotBullet()
        bullet.id = id
        bullet.personId = personId
        bullet.weaponNumber = weaponNumber
        bullet.position = position
        bullet.direction = direction

        return bullet

    def __init__(self):
        self.id = 0
        self.personId = 0
        self.weaponNumber = 0
        self.position = Vector3()
        self.direction = Vector3()

    def __eq__(self, value):
        return (
            self.id == value.id
            and self.personId == value.personId
            and self.weaponNumber == value.weaponNumber
            and self.position == value.position
            and self.direction == value.direction
        )

    def __hash__(self):
        return hash(
            (
                self.id.__hash__(),
                self.personId.__hash__(),
                self.weaponNumber.__hash__(),
                self.position.__hash__(),
                self.direction.__hash__(),
            )
        )

    def toBytes(self, writer):
        writer.write(
            "iiBffffff",
            self.id,
            self.personId,
            self.weaponNumber,
            self.position.x,
            self.position.y,
            self.position.z,
            self.direction.x,
            self.direction.y,
            self.direction.z,
        )

    @staticmethod
    def fromBytes(reader):
        bullet = SnapshotBullet()
        (
            bullet.id,
            bullet.personId,
            bullet.weaponNumber,
            bullet.position.x,
            bullet.position.y,
            bullet.position.z,
            bullet.direction.x,
            bullet.direction.y,
            bullet.direction.z,
        ) = reader.read("iiBffffff")

        return bullet
