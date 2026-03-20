from game.calc.Vector3 import Vector3


class SnapshotPersonDiffFields:

    centerPoint = 1 << 0
    yawRadians = 1 << 1
    pitchRadians = 1 << 2
    health = 1 << 3
    vest = 1 << 4
    jumpingValue = 1 << 5
    selectedWeaponNumber = 1 << 6

    @staticmethod
    def toBitMask(diff):
        bitMask = 0
        for fieldName in diff.__dict__.keys():
            if fieldName == "id":
                continue
            bitMask |= SnapshotPersonDiffFields.__dict__[fieldName]

        return bitMask


class SnapshotPersonDiff:

    @staticmethod
    def makeFull(id, centerPoint, yawRadians, pitchRadians, health, vest, jumpingValue, selectedWeaponNumber):
        diff = SnapshotPersonDiff()
        diff.id = id
        diff.centerPoint = centerPoint
        diff.yawRadians = yawRadians
        diff.pitchRadians = pitchRadians
        diff.health = health
        diff.vest = vest
        diff.jumpingValue = jumpingValue
        diff.selectedWeaponNumber = selectedWeaponNumber

        return diff

    def makeWithHealth(id, health):
        diff = SnapshotPersonDiff()
        diff.id = id
        diff.health = health

        return diff

    def __init__(self):
        self.id = 0
        # остальные поля добавляются динамически при создании

    def isEmpty(self):
        return len(self.__dict__) == 1  # id

    def __eq__(self, value):
        return (
            self.id == value.id
            and ((not hasattr(self, "centerPoint") and not hasattr(value, "centerPoint")) or self.centerPoint == value.centerPoint)
            and ((not hasattr(self, "yawRadians") and not hasattr(value, "yawRadians")) or self.yawRadians == value.yawRadians)
            and ((not hasattr(self, "pitchRadians") and not hasattr(value, "pitchRadians")) or self.pitchRadians == value.pitchRadians)
            and ((not hasattr(self, "health") and not hasattr(value, "health")) or self.health == value.health)
            and ((not hasattr(self, "vest") and not hasattr(value, "vest")) or self.vest == value.vest)
            and ((not hasattr(self, "jumpingValue") and not hasattr(value, "jumpingValue")) or self.jumpingValue == value.jumpingValue)
            and (
                (not hasattr(self, "selectedWeaponNumber") and not hasattr(value, "selectedWeaponNumber"))
                or self.selectedWeaponNumber == value.selectedWeaponNumber
            )
        )

    def __hash__(self):
        return hash(
            (
                self.id.__hash__(),
                self.centerPoint.__hash__(),
                self.yawRadians.__hash__(),
                self.pitchRadians.__hash__(),
                self.health.__hash__(),
                self.vest.__hash__(),
                self.jumpingValue.__hash__(),
                self.selectedWeaponNumber.__hash__(),
            )
        )

    def toBytes(self, writer):
        fieldsBitMask = SnapshotPersonDiffFields.toBitMask(self)
        writer.write("H", fieldsBitMask)

        writer.write("i", self.id)

        if hasattr(self, "centerPoint"):
            # centerPoint.z передаем как double 64bit, чтобы избежать 'проваливания' персонажа сквозь пол
            writer.write("ffd", self.centerPoint.x, self.centerPoint.y, self.centerPoint.z)

        if hasattr(self, "yawRadians"):
            writer.write("f", self.yawRadians)

        if hasattr(self, "pitchRadians"):
            writer.write("f", self.pitchRadians)

        if hasattr(self, "health"):
            writer.write("B", self.health)

        if hasattr(self, "vest"):
            writer.write("B", self.vest)

        if hasattr(self, "jumpingValue"):
            writer.write("f", self.jumpingValue)

        if hasattr(self, "selectedWeaponNumber"):
            writer.write("B", self.selectedWeaponNumber)

    @staticmethod
    def fromBytes(reader):
        fieldsBitMask = reader.read("H")

        diff = SnapshotPersonDiff()
        diff.id = reader.read("i")

        if fieldsBitMask & SnapshotPersonDiffFields.centerPoint > 0:
            diff.centerPoint = Vector3()
            diff.centerPoint.x, diff.centerPoint.y, diff.centerPoint.z = reader.read("ffd")

        if fieldsBitMask & SnapshotPersonDiffFields.yawRadians > 0:
            diff.yawRadians = reader.read("f")

        if fieldsBitMask & SnapshotPersonDiffFields.pitchRadians > 0:
            diff.pitchRadians = reader.read("f")

        if fieldsBitMask & SnapshotPersonDiffFields.health > 0:
            diff.health = reader.read("B")

        if fieldsBitMask & SnapshotPersonDiffFields.vest > 0:
            diff.vest = reader.read("B")

        if fieldsBitMask & SnapshotPersonDiffFields.jumpingValue > 0:
            diff.jumpingValue = reader.read("f")

        if fieldsBitMask & SnapshotPersonDiffFields.selectedWeaponNumber > 0:
            diff.selectedWeaponNumber = reader.read("B")

        return diff
