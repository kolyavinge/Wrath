from game.calc.Vector3 import Vector3


class CommonConstants:

    gameTitle = b"Wrath"
    gameTitleU = "Wrath"
    screenAspect = 16 / 9
    minDepth = 0.1
    maxDepth = 1000
    maxLevelSize = 10000
    maxViewDepth = 50
    axisOrigin = Vector3(0, 0, 0)
    xAxis = Vector3(1, 0, 0)
    yAxis = Vector3(0, 1, 0)
    zAxis = Vector3(0, 0, 1)
    up = Vector3(0, 0, 1)
    down = Vector3(0, 0, -1)
    mainTimerMsec = 20
