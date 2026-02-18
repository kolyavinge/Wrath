class SnapshotDiffFields:

    addedPersonIds = 1 << 0
    person = 1 << 1
    player = 1 << 2
    enemies = 1 << 3
    respawnedPerson = 1 << 4
    addedBullets = 1 << 5
    addedDebris = 1 << 6
    addedRays = 1 << 7
    removedRayIds = 1 << 8
    addedPowerups = 1 << 9
    removedPowerupIds = 1 << 10
    pickedupPowerupIds = 1 << 11
    addedPersonBulletCollisions = 1 << 12
    addedPersonRayCollisions = 1 << 13
    addedPersonFrags = 1 << 14
    addedPersonDeaths = 1 << 15

    @staticmethod
    def toBitMask(diff):
        bitMask = 0
        for fieldName in diff.__dict__.keys():
            bitMask |= SnapshotDiffFields.__dict__[fieldName]

        return bitMask
