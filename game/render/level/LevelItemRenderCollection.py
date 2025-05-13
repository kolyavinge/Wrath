from game.render.level.LevelItemRenderModel3dBuilder import *


class LevelItemRenderCollection:

    def __init__(self, levelItemRenderModel3dBuilder: LevelItemRenderModel3dBuilder):
        self.levelItemRenderModel3dBuilder = levelItemRenderModel3dBuilder
        self.models3d = {}

    def init(self, allVisibilityLevelSegments):
        for model in self.models3d.values():
            model.release()

        self.models3d.clear()

        for levelSegment in allVisibilityLevelSegments:
            model3d = self.levelItemRenderModel3dBuilder.buildRenderModel3d(levelSegment)
            self.models3d[levelSegment] = model3d

    def getRenderModel3d(self, levelSegment):
        return self.models3d[levelSegment]


def makeLevelItemRenderCollection(resolver):
    return LevelItemRenderCollection(resolver.resolve(LevelItemRenderModel3dBuilder))
