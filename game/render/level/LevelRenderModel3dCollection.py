from game.render.level.LevelRenderModel3dBuilder import LevelRenderModel3dBuilder


class LevelRenderModel3dCollection:

    def __init__(self, levelRenderModel3dBuilder):
        self.levelRenderModel3dBuilder = levelRenderModel3dBuilder
        self.models3d = {}

    def init(self, allVisibilityLevelSegments):
        for model in self.models3d.values():
            model.release()

        self.models3d.clear()

        for levelSegment in allVisibilityLevelSegments:
            model3d = self.levelRenderModel3dBuilder.buildRenderModel3d(levelSegment)
            self.models3d[levelSegment] = model3d

    def getRenderModel3d(self, levelSegment):
        return self.models3d[levelSegment]


def makeLevelRenderModel3dCollection(resolver):
    return LevelRenderModel3dCollection(resolver.resolve(LevelRenderModel3dBuilder))
