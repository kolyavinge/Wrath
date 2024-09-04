from game.render.level.LevelItemGroupBuilder import LevelItemGroupBuilder


class LevelItemGroupCollection:

    def __init__(self, levelItemGroupBuilder):
        self.levelItemGroupBuilder = levelItemGroupBuilder
        self.levelItemGroups = {}

    def init(self, allVisibilityLevelSegments):
        for item in self.levelItemGroups.values():
            item.release()

        self.levelItemGroups.clear()

        for levelSegment in allVisibilityLevelSegments:
            items = self.levelItemGroupBuilder.buildForLevelSegment(levelSegment)
            self.levelItemGroups[levelSegment] = items

    def getLevelItemGroups(self, levelSegment):
        return self.levelItemGroups[levelSegment]


def makeLevelItemGroupCollection(resolver):
    return LevelItemGroupCollection(resolver.resolve(LevelItemGroupBuilder))
