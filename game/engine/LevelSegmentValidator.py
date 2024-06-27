class LevelSegmentValidator:

    def validate(self, level):
        levelSegments = level.bspTree.getAllLevelSegments()
        for levelSegment in levelSegments:
            levelSegment.validate()


def makeLevelSegmentValidator(resolver):
    return LevelSegmentValidator()
