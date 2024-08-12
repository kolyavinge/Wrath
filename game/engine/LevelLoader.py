from game.levels.LevelAurora import LevelAurora


class LevelLoader:

    def load(self):
        level = LevelAurora()
        level.validate()

        return level


def makeLevelLoader(resolver):
    return LevelLoader()
