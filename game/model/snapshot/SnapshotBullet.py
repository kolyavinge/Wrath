from game.calc.Vector3 import Vector3
from game.model.weapon.WeaponCollection import WeaponCollection


class WeaponInfoExtraBit:

    leftHandWeapon = 1 << 7


class SnapshotBullet:

    @staticmethod
    def readWeaponInfo(weaponInfo):
        weaponNumber = weaponInfo & ~WeaponInfoExtraBit.leftHandWeapon
        isLeftHandWeapon = weaponInfo & WeaponInfoExtraBit.leftHandWeapon > 0

        return (weaponNumber, isLeftHandWeapon)

    @staticmethod
    def make(id, personId, weaponInfo, position, direction, randomSeed):
        bullet = SnapshotBullet()
        bullet.id = id
        bullet.personId = personId
        bullet.weaponInfo = weaponInfo
        bullet.position = position
        bullet.direction = direction
        bullet.randomSeed = randomSeed

        return bullet

    def __init__(self):
        self.id = 0
        self.personId = 0
        self.weaponInfo = 0
        self.position = Vector3()
        self.direction = Vector3()
        self.randomSeed = None

    def __eq__(self, value):
        return (
            self.id == value.id
            and self.personId == value.personId
            and self.weaponInfo == value.weaponInfo
            and self.position == value.position
            and self.direction == value.direction
            and self.randomSeed == value.randomSeed
        )

    def __hash__(self):
        return hash(
            (
                self.id.__hash__(),
                self.personId.__hash__(),
                self.weaponInfo.__hash__(),
                self.position.__hash__(),
                self.direction.__hash__(),
                self.randomSeed.__hash__(),
            )
        )

    def toBytes(self, writer):
        writer.write(
            "iiBffffff",
            self.id,
            self.personId,
            self.weaponInfo,
            self.position.x,
            self.position.y,
            self.position.z,
            self.direction.x,
            self.direction.y,
            self.direction.z,
        )

        if self.randomSeed is not None:
            writer.write("H", self.randomSeed)

    @staticmethod
    def fromBytes(reader):
        bullet = SnapshotBullet()
        (
            bullet.id,
            bullet.personId,
            bullet.weaponInfo,
            bullet.position.x,
            bullet.position.y,
            bullet.position.z,
            bullet.direction.x,
            bullet.direction.y,
            bullet.direction.z,
        ) = reader.read("iiBffffff")

        weaponNumber, _ = SnapshotBullet.readWeaponInfo(bullet.weaponInfo)
        if WeaponCollection.getWeaponTypeByNumber(weaponNumber).hasDebrisAfterExplosion:
            bullet.randomSeed = reader.read("H")

        return bullet
