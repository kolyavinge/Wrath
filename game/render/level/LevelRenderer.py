from OpenGL.GL import *

from game.engine.GameData import GameData
from game.gl.VBORenderer import VBORenderer
from game.render.level.LevelItemRenderer import LevelItemRenderer
from game.render.level.ShadowCastLevelItemCollection import *


class LevelRenderer:

    def __init__(self, gameData, levelItemRenderer, shadowCastLevelItemCollection, vboRenderer):
        self.gameData = gameData
        self.levelItemRenderer = levelItemRenderer
        self.shadowCastLevelItemCollection = shadowCastLevelItemCollection
        self.vboRenderer = vboRenderer

    def init(self):
        allLevelSegments = self.gameData.level.visibilityTree.getAllLevelSegments()
        self.levelItemRenderer.init(allLevelSegments)
        self.shadowCastLevelItemCollection.init(allLevelSegments)

    def renderLevelSegments(self, shader):
        for levelSegment in self.gameData.visibleLevelSegments:
            shader.setLight(levelSegment.lightsWithJoined, self.gameData.playerItems.torch)
            self.levelItemRenderer.render(shader, levelSegment)

    def renderShadowCasters(self, shader):
        for levelSegment in self.gameData.visibleLevelSegments:
            shader.setLight(levelSegment.lights, self.gameData.playerItems.torch)
            vbo = self.shadowCastLevelItemCollection.getShadowCastersVBO(levelSegment)
            self.vboRenderer.render(vbo)


def makeLevelRenderer(resolver):
    return LevelRenderer(
        resolver.resolve(GameData),
        resolver.resolve(LevelItemRenderer),
        resolver.resolve(ShadowCastLevelItemCollection),
        resolver.resolve(VBORenderer),
    )
