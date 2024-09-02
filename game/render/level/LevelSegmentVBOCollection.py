from game.render.level.LevelSegmentVBOBuilder import LevelSegmentVBOBuilder


class LevelSegmentVBOCollection:

    def __init__(self, levelSegmentVBOBuilder):
        self.levelSegmentVBOBuilder = levelSegmentVBOBuilder

    def init(self, visibilityTreeLevelSegments):
        self.levelSegmentDictionary = {}
        # release current vbo-s
        for levelSegment in visibilityTreeLevelSegments:
            vbo = self.levelSegmentVBOBuilder.build(levelSegment)
            self.levelSegmentDictionary[levelSegment] = vbo

    def getLevelSegmentVBO(self, levelSegment):
        return self.levelSegmentDictionary[levelSegment]


def makeLevelSegmentVBOCollection(resolver):
    return LevelSegmentVBOCollection(resolver.resolve(LevelSegmentVBOBuilder))
