class LevelValidator:

    def validate(self, level):
        level.validate()

        levelSegments = level.collisionTree.getAllLevelSegments()
        # for levelSegment in levelSegments:
        #    levelSegment.validate()


def makeLevelValidator(resolver):
    return LevelValidator()
