from game.model.snapshot.SnapshotBullet import SnapshotBullet
from game.model.snapshot.SnapshotBulletCollision import SnapshotBulletCollision
from game.model.snapshot.SnapshotDebris import SnapshotDebris
from game.model.snapshot.SnapshotDiffFields import SnapshotDiffFields
from game.model.snapshot.SnapshotFragStatistic import SnapshotFragStatistic
from game.model.snapshot.SnapshotPerson import SnapshotPerson
from game.model.snapshot.SnapshotPowerup import SnapshotPowerup
from game.model.snapshot.SnapshotRay import SnapshotRay
from game.model.snapshot.SnapshotRayCollision import SnapshotRayCollision


class SnapshotDiff:

    # пустой обьект. поля добавляются динамически при создании

    def isEmpty(self):
        return len(self.__dict__) == 0

    def toBytes(self, writer):
        fieldsBitMask = SnapshotDiffFields.toBitMask(self)
        writer.write("h", fieldsBitMask)

        if hasattr(self, "player"):
            self.player.toBytes(writer)

        if hasattr(self, "enemies"):
            writer.write("b", len(self.enemies))
            for enemy in self.enemies:
                enemy.toBytes(writer)

        if hasattr(self, "addedBullets"):
            writer.write("b", len(self.addedBullets))
            for addedBullet in self.addedBullets:
                addedBullet.toBytes(writer)

        if hasattr(self, "addedDebris"):
            writer.write("b", len(self.addedDebris))
            for addedPiece in self.addedDebris:
                addedPiece.toBytes(writer)

        if hasattr(self, "addedRays"):
            writer.write("b", len(self.addedRays))
            for addedRay in self.addedRays:
                addedRay.toBytes(writer)

        if hasattr(self, "removedRayIds"):
            writer.write("b", len(self.removedRayIds))
            for removedRayId in self.removedRayIds:
                writer.write("i", removedRayId)

        if hasattr(self, "addedPowerups"):
            writer.write("b", len(self.addedPowerups))
            for addedPowerup in self.addedPowerups:
                addedPowerup.toBytes(writer)

        if hasattr(self, "removedPowerupIds"):
            writer.write("b", len(self.removedPowerupIds))
            for removedPowerupId in self.removedPowerupIds:
                writer.write("i", removedPowerupId)

        if hasattr(self, "pickedupPowerupIds"):
            writer.write("b", len(self.pickedupPowerupIds))
            for pickedupPowerupId in self.pickedupPowerupIds:
                writer.write("i", pickedupPowerupId)

        if hasattr(self, "addedPersonBulletCollisions"):
            writer.write("b", len(self.addedPersonBulletCollisions))
            for collision in self.addedPersonBulletCollisions:
                collision.toBytes(writer)

        if hasattr(self, "addedPersonRayCollisions"):
            writer.write("b", len(self.addedPersonRayCollisions))
            for collision in self.addedPersonRayCollisions:
                collision.toBytes(writer)

        if hasattr(self, "addedPersonFrags"):
            writer.write("b", len(self.addedPersonFrags))
            for frag in self.addedPersonFrags:
                frag.toBytes(writer)

        if hasattr(self, "addedPersonDeaths"):
            writer.write("b", len(self.addedPersonDeaths))
            for death in self.addedPersonDeaths:
                death.toBytes(writer)

    @staticmethod
    def fromBytes(reader):
        diff = SnapshotDiff()
        fieldsBitMask = reader.read("h")

        if fieldsBitMask & SnapshotDiffFields.player > 0:
            diff.player = SnapshotPerson.fromBytes(reader)

        if fieldsBitMask & SnapshotDiffFields.enemies > 0:
            count = reader.read("b")
            diff.enemies = [SnapshotPerson.fromBytes(reader) for _ in range(0, count)]

        if fieldsBitMask & SnapshotDiffFields.addedBullets > 0:
            count = reader.read("b")
            diff.addedBullets = [SnapshotBullet.fromBytes(reader) for _ in range(0, count)]

        if fieldsBitMask & SnapshotDiffFields.addedDebris > 0:
            count = reader.read("b")
            diff.addedDebris = [SnapshotDebris.fromBytes(reader) for _ in range(0, count)]

        if fieldsBitMask & SnapshotDiffFields.addedRays > 0:
            count = reader.read("b")
            diff.addedRays = [SnapshotRay.fromBytes(reader) for _ in range(0, count)]

        if fieldsBitMask & SnapshotDiffFields.removedRayIds > 0:
            count = reader.read("b")
            diff.removedRayIds = [reader.read("i") for _ in range(0, count)]

        if fieldsBitMask & SnapshotDiffFields.addedPowerups > 0:
            count = reader.read("b")
            diff.addedPowerups = [SnapshotPowerup.fromBytes(reader) for _ in range(0, count)]

        if fieldsBitMask & SnapshotDiffFields.removedPowerupIds > 0:
            count = reader.read("b")
            diff.removedPowerupIds = [reader.read("i") for _ in range(0, count)]

        if fieldsBitMask & SnapshotDiffFields.pickedupPowerupIds > 0:
            count = reader.read("b")
            diff.pickedupPowerupIds = [reader.read("i") for _ in range(0, count)]

        if fieldsBitMask & SnapshotDiffFields.addedPersonBulletCollisions > 0:
            count = reader.read("b")
            diff.addedPersonBulletCollisions = [SnapshotBulletCollision.fromBytes(reader) for _ in range(0, count)]

        if fieldsBitMask & SnapshotDiffFields.addedPersonRayCollisions > 0:
            count = reader.read("b")
            diff.addedPersonRayCollisions = [SnapshotRayCollision.fromBytes(reader) for _ in range(0, count)]

        if fieldsBitMask & SnapshotDiffFields.addedPersonFrags > 0:
            count = reader.read("b")
            diff.addedPersonFrags = [SnapshotFragStatistic.fromBytes(reader) for _ in range(0, count)]

        if fieldsBitMask & SnapshotDiffFields.addedPersonDeaths > 0:
            count = reader.read("b")
            diff.addedPersonDeaths = [SnapshotFragStatistic.fromBytes(reader) for _ in range(0, count)]

        return diff
