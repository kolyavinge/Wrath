class LevelValidator:

    def validate(self, level):
        level.validate()

        levelSegments = level.bspTree.getAllLevelSegments()
        for levelSegment in levelSegments:
            levelSegment.validate()


def makeLevelValidator(resolver):
    return LevelValidator()
