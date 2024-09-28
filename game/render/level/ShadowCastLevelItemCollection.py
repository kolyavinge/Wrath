from game.render.level.ShadowCastLevelItemBuilder import ShadowCastLevelItemBuilder


class ShadowCastLevelItemCollection:

    def __init__(self, shadowCastLevelItemBuilder):
        self.shadowCastLevelItemBuilder = shadowCastLevelItemBuilder
        self.shadowCastersVbos = {}

    def init(self, allVisibilityLevelSegments):
        for vbo in self.shadowCastersVbos:
            vbo.release()

        self.shadowCastersVbos.clear()

        for levelSegment in allVisibilityLevelSegments:
            vbo = self.shadowCastLevelItemBuilder.buildForLevelSegment(levelSegment)
            self.shadowCastersVbos[levelSegment] = vbo

    def getShadowCastersVBO(self, levelSegment):
        return self.shadowCastersVbos[levelSegment]


def makeShadowCastLevelItemCollection(resolver):
    return ShadowCastLevelItemCollection(resolver.resolve(ShadowCastLevelItemBuilder))
