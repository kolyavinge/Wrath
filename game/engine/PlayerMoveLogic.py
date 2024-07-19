from game.engine.GameData import GameData


class PlayerMoveLogic:

    def __init__(self, gameData):
        self.gameData = gameData

    def process(self):
        inputData = self.gameData.playerInputData

        if inputData.goForward:
            self.goForward()
        elif inputData.goBackward:
            self.goBackward()

        if inputData.stepLeft:
            self.stepLeft()
        elif inputData.stepRight:
            self.stepRight()

    def goForward(self):
        player = self.gameData.player
        player.hasMoved = True
        velocityDirection = player.frontNormal.copy()
        velocityDirection.setLength(player.getVelocity())
        player.moveNextPositionBy(velocityDirection)
        player.movingTime += player.movingTimeDelta

    def goBackward(self):
        player = self.gameData.player
        player.hasMoved = True
        delta = player.frontNormal.copy()
        delta.setLength(0.1)
        delta.mul(-1)
        player.moveNextPositionBy(delta)

    def stepLeft(self):
        player = self.gameData.player
        player.hasMoved = True
        delta = player.rightNormal.copy()
        delta.setLength(0.1)
        delta.mul(-1)
        player.moveNextPositionBy(delta)

    def stepRight(self):
        player = self.gameData.player
        player.hasMoved = True
        delta = player.rightNormal.copy()
        delta.setLength(0.1)
        player.moveNextPositionBy(delta)


def makePlayerMoveLogic(resolver):
    return PlayerMoveLogic(resolver.resolve(GameData))
