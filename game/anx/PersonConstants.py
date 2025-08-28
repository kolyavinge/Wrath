from game.lib.Math import Math


class PersonConstants:

    xyLength = 0.7
    xyLengthHalf = xyLength / 2.0
    zLength = 1.8
    zLengthHalf = zLength / 2
    zLength34 = (3.0 / 4.0) * zLength
    headSize = 0.24
    headSizeHalf = headSize / 2.0
    zChestLength = zLength - headSize
    zFootLength = 0.2
    eyeLength = 1.6
    aimLength = 20.0
    maxPersonHealth = 100
    maxPitchRadians = Math.piHalf - 0.1
    maxVest = 100
    stepTimeLimit = 15
    selectWeaponDelay = 40
    selectWeaponDelayHalf = int(selectWeaponDelay / 2)
