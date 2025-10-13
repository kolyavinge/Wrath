class PersonZState:

    onFloor = 1
    jumping = 2
    falling = 3
    landing = 4


class LifeCycle:

    alive = 0
    dead = 1
    respawnDelay = 2
    respawn = 3


class WeaponSelectState:

    startSelection = 0
    putWeaponDown = 1
    startRaising = 2
    raiseWeaponUp = 3
