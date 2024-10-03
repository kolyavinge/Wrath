from OpenGL.GL import *

from game.engine.GameData import GameData
from game.gl.VBORenderer import VBORenderer
from game.render.level.LevelItemGroupCollection import LevelItemGroupCollection
from game.render.level.ShadowCastLevelItemCollection import *


class LevelRenderer:

    def __init__(self, gameData, levelItemGroupCollection, shadowCastLevelItemCollection, vboRenderer):
        self.gameData = gameData
        self.levelItemGroupCollection = levelItemGroupCollection
        self.shadowCastLevelItemCollection = shadowCastLevelItemCollection
        self.vboRenderer = vboRenderer

    def init(self):
        allLevelSegments = self.gameData.level.visibilityTree.getAllLevelSegments()
        self.levelItemGroupCollection.init(allLevelSegments)
        self.shadowCastLevelItemCollection.init(allLevelSegments)

    def renderLevelSegments(self, shader):
        torch = self.gameData.playerItems.torch
        player = self.gameData.player
        for levelSegment in self.gameData.visibleLevelSegments:
            shader.setLight(levelSegment.lightsWithJoined, player, torch)
            levelItemGroups = self.levelItemGroupCollection.getLevelItemGroups(levelSegment)
            for item in levelItemGroups:
                shader.setMaterial(item.material)
                item.texture.bind(GL_TEXTURE0)
                self.vboRenderer.render(item.vbo)
                # item.texture.unbind()

    def renderShadowCasters(self, shader):
        for levelSegment in self.gameData.visibleLevelSegments:
            shader.setLight(levelSegment.lights, self.gameData.player, self.gameData.playerItems.torch)
            vbo = self.shadowCastLevelItemCollection.getShadowCastersVBO(levelSegment)
            self.vboRenderer.render(vbo)


def makeLevelRenderer(resolver):
    return LevelRenderer(
        resolver.resolve(GameData),
        resolver.resolve(LevelItemGroupCollection),
        resolver.resolve(ShadowCastLevelItemCollection),
        resolver.resolve(VBORenderer),
    )
