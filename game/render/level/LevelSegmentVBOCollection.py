from game.render.level.LevelSegmentVBOBuilder import LevelSegmentVBOBuilder


class LevelSegmentVBOCollection:

    def __init__(self, levelSegmentVBOBuilder):
        self.levelSegmentVBOBuilder = levelSegmentVBOBuilder
        self.levelSegmentVBO = {}

    def init(self, allVisibilityLevelSegments):
        for vbo in self.levelSegmentVBO.values():
            vbo.release()

        self.levelSegmentVBO.clear()

        for levelSegment in allVisibilityLevelSegments:
            vbo = self.levelSegmentVBOBuilder.build(levelSegment)
            self.levelSegmentVBO[levelSegment] = vbo

    def getLevelSegmentVBO(self, levelSegment):
        return self.levelSegmentVBO[levelSegment]


def makeLevelSegmentVBOCollection(resolver):
    return LevelSegmentVBOCollection(resolver.resolve(LevelSegmentVBOBuilder))
