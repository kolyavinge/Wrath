class SnapshotDiffFields:

    addedPersonIds = 1 << 0
    person = 1 << 1
    player = 1 << 2
    enemies = 1 << 3
    respawnedPerson = 1 << 4
    addedBullets = 1 << 5
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
