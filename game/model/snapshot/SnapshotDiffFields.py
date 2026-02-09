class SnapshotDiffFields:

    player = 1 << 0
    enemies = 1 << 1
    addedBullets = 1 << 2
    addedDebris = 1 << 3
    addedRays = 1 << 4
    removedRayIds = 1 << 5
    addedPowerups = 1 << 6
    removedPowerupIds = 1 << 7
    pickedupPowerupIds = 1 << 8
    addedPersonBulletCollisions = 1 << 9
    addedPersonRayCollisions = 1 << 10
    addedPersonFrags = 1 << 11
    addedPersonDeaths = 1 << 12

    @staticmethod
    def toBitMask(diff):
        bitMask = 0
        for fieldName in diff.__dict__.keys():
            bitMask |= SnapshotDiffFields.__dict__[fieldName]

        return bitMask
