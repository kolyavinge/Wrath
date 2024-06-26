class LevelSegmentValidator:

    def validate(self, level):
        levelSegments = level.bspTree.getAllLevelSegments()
        return
        for levelSegment in levelSegments:
            assert levelSegment.floor is not None


def makeLevelSegmentValidator(resolver):
    return LevelSegmentValidator()
