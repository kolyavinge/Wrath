from game.levels.AuroraLevel import AuroraLevel
from game.levels.TestLevel import TestLevel
from game.levels.TowersLevel import TowersLevel


class LevelLoader:

    def load(self):
        level = TowersLevel()
        level.validate()

        return level


def makeLevelLoader(resolver):
    return LevelLoader()
