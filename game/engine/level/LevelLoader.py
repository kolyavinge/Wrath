from game.levels.NebulaLevel import NebulaLevel


class LevelLoader:

    def load(self):
        level = NebulaLevel()
        level.validate()

        return level
