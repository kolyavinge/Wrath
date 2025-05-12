from game.lib.Dictionary import Dictionary


class LevelSegmentLightAnalyzer:

    def analyzeLights(self, level, bspTree):
        # чтобы свет из одного сегмента действовал и на соседние
        groupedLights = Dictionary.groupby(level.lights, lambda x: x.joinGroup)
        allLevelSegments = bspTree.getAllLevelSegments()
        for levelSegment in allLevelSegments:
            levelSegment.lightsWithJoined = levelSegment.lights.copy()
            joinGroups = set([light.joinGroup for light in levelSegment.lights if light.joinGroup is not None])
            for joinGroup in joinGroups:
                for joinedLight in groupedLights[joinGroup]:
                    if joinedLight not in levelSegment.lightsWithJoined:
                        levelSegment.lightsWithJoined.append(joinedLight)


def makeLevelSegmentLightAnalyzer(resolver):
    return LevelSegmentLightAnalyzer()
