class SnapshotDiffFields:

    person = 1 << 0
    player = 1 << 1
    enemies = 1 << 2
    respawnedPerson = 1 << 3
    addedBullets = 1 << 4
    addedDebris = 1 << 5
    addedRays = 1 << 6
    removedRayIds = 1 << 7
    addedPowerups = 1 << 8
    removedPowerupIds = 1 << 9
    pickedupPowerupIds = 1 << 10
    addedPersonBulletCollisions = 1 << 11
    addedPersonRayCollisions = 1 << 12
    addedPersonFrags = 1 << 13
    addedPersonDeaths = 1 << 14

    @staticmethod
    def toBitMask(diff):
        bitMask = 0
        for fieldName in diff.__dict__.keys():
            bitMask |= SnapshotDiffFields.__dict__[fieldName]

        return bitMask
