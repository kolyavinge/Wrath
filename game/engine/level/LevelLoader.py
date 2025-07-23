from game.levels.NebulaLevel import NebulaLevel
from game.levels.TowersLevel import TowersLevel


class LevelLoader:

    def load(self):
        level = NebulaLevel()
        level.validate()

        return level
