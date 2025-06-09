from game.calc.Vector3 import Vector3


class CommonConstants:

    gameTitle = b"Wrath"
    gameTitleU = "Wrath"
    screenAspect = 16.0 / 9.0
    minPerspectiveDepth = 0.05
    maxPerspectiveDepth = 1000.0
    maxDepth = 100.0
    maxLevelSize = 500.0
    maxEnemyAnimationDistance = 100.0
    axisOrigin = Vector3(0, 0, 0)
    xAxis = Vector3(1, 0, 0)
    yAxis = Vector3(0, 1, 0)
    zAxis = Vector3(0, 0, 1)
    up = Vector3(0, 0, 1)
    down = Vector3(0, 0, -1)
    mainTimerMsec = 20
    maxBulletHoles = 1000
