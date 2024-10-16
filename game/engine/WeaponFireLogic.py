from game.engine.GameData import GameData


class WeaponFireLogic:

    def __init__(self, gameData):
        self.gameData = gameData

    def process(self):
        pass


def makeWeaponFireLogic(resolver):
    return WeaponFireLogic(resolver.resolve(GameData))
