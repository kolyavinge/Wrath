class LevelSegmentLightAnalyzer:

    def analyzeLights(self, bspTree):
        allLevelSegments = bspTree.getAllLevelSegments()

        result = {}
        for levelSegment in allLevelSegments:
            result[levelSegment] = []

        for levelSegment in allLevelSegments:
            for joinLine in levelSegment.joinLines:
                joinedLevelSegment = joinLine.getJoinedLevelSegment(levelSegment)
                result[joinedLevelSegment].extend(levelSegment.lights)

        for levelSegment in result.keys():
            levelSegment.lights.extend(result[levelSegment])


def makeLevelSegmentLightAnalyzer(resolver):
    return LevelSegmentLightAnalyzer()
