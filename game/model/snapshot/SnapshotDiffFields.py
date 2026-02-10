class SnapshotDiffFields:

    player = 1 << 0
    players = 1 << 1
    enemies = 1 << 2
    addedBullets = 1 << 3
    addedDebris = 1 << 4
    addedRays = 1 << 5
    removedRayIds = 1 << 6
    addedPowerups = 1 << 7
    removedPowerupIds = 1 << 8
    pickedupPowerupIds = 1 << 9
    addedPersonBulletCollisions = 1 << 10
    addedPersonRayCollisions = 1 << 11
    addedPersonFrags = 1 << 12
    addedPersonDeaths = 1 << 13

    @staticmethod
    def toBitMask(diff):
        bitMask = 0
        for fieldName in diff.__dict__.keys():
            bitMask |= SnapshotDiffFields.__dict__[fieldName]

        return bitMask
