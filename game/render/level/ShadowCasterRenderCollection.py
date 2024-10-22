from game.render.level.ShadowCasterBuilder import ShadowCasterBuilder


class ShadowCasterRenderCollection:

    def __init__(self, shadowCasterBuilder):
        self.shadowCasterBuilder = shadowCasterBuilder
        self.shadowCastersVbos = {}

    def init(self, allVisibilityLevelSegments):
        for vbo in self.shadowCastersVbos:
            vbo.release()

        self.shadowCastersVbos.clear()

        for levelSegment in allVisibilityLevelSegments:
            vbo = self.shadowCasterBuilder.buildForLevelSegment(levelSegment)
            self.shadowCastersVbos[levelSegment] = vbo

    def getShadowCastersVBO(self, levelSegment):
        return self.shadowCastersVbos[levelSegment]


def makeShadowCasterRenderCollection(resolver):
    return ShadowCasterRenderCollection(resolver.resolve(ShadowCasterBuilder))
