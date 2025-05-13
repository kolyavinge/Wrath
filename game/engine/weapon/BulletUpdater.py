from game.engine.GameData import GameData


class BulletUpdater:

    def __init__(self, gameData: GameData):
        self.gameData = gameData

    def update(self):
        for bullet in self.gameData.bullets:
            bullet.update()


def makeBulletUpdater(resolver):
    return BulletUpdater(resolver.resolve(GameData))
