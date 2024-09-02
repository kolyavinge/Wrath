from game.engine.GameData import GameData
from game.gl.VBORenderer import VBORenderer
from game.render.level.LevelSegmentVBOCollection import LevelSegmentVBOCollection


class LevelRenderer:

    def __init__(self, gameData, levelSegmentVBOCollection, vboRenderer):
        self.gameData = gameData
        self.levelSegmentVBOCollection = levelSegmentVBOCollection
        self.vboRenderer = vboRenderer

    def init(self):
        self.levelSegmentVBOCollection.init(self.gameData.level.visibilityTree.getAllLevelSegments())

    def render(self):
        for levelSegment in self.gameData.visibleLevelSegments:
            vbo = self.levelSegmentVBOCollection.getLevelSegmentVBO(levelSegment)
            self.vboRenderer.render(vbo)


def makeLevelRenderer(resolver):
    return LevelRenderer(resolver.resolve(GameData), resolver.resolve(LevelSegmentVBOCollection), resolver.resolve(VBORenderer))
