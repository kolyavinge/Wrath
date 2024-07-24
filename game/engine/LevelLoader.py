from game.levels.Level1 import Level1
from game.levels.LevelAurora import LevelAurora
from game.levels.LevelLoop import LevelLoop


class LevelLoader:

    def loadFromFile(self):
        level = LevelAurora()
        level.validate()

        return level


def makeLevelLoader(resolver):
    return LevelLoader()
