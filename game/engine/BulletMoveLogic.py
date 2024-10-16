from game.engine.GameData import GameData


class BulletMoveLogic:

    def __init__(self, gameData):
        self.gameData = gameData

    def process(self):
        pass


def makeBulletMoveLogic(resolver):
    return BulletMoveLogic(resolver.resolve(GameData))
