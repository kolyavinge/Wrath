from OpenGL.GL import *

from game.engine.GameData import GameData
from game.gl.VBORenderer import VBORenderer
from game.render.level.LevelRenderModel3dCollection import LevelRenderModel3dCollection
from game.render.level.ShadowCastLevelItemCollection import *


class LevelRenderer:

    def __init__(self, gameData, levelRenderModel3dCollection, shadowCastLevelItemCollection, vboRenderer):
        self.gameData = gameData
        self.levelRenderModel3dCollection = levelRenderModel3dCollection
        self.shadowCastLevelItemCollection = shadowCastLevelItemCollection
        self.vboRenderer = vboRenderer

    def init(self):
        allLevelSegments = self.gameData.level.visibilityTree.getAllLevelSegments()
        self.levelRenderModel3dCollection.init(allLevelSegments)
        self.shadowCastLevelItemCollection.init(allLevelSegments)

    def renderLevelSegments(self, shader):
        torch = self.gameData.playerItems.torch
        player = self.gameData.player
        for levelSegment in self.gameData.visibleLevelSegments:
            shader.setLight(levelSegment.lightsWithJoined, player, torch)
            model3d = self.levelRenderModel3dCollection.getRenderModel3d(levelSegment)
            for mesh in model3d.meshes:
                shader.setMaterial(mesh.material)
                mesh.texture.bind(GL_TEXTURE0)
                self.vboRenderer.render(mesh.vbo)

    def renderShadowCasters(self, shader):
        for levelSegment in self.gameData.visibleLevelSegments:
            shader.setLight(levelSegment.lights, self.gameData.player, self.gameData.playerItems.torch)
            vbo = self.shadowCastLevelItemCollection.getShadowCastersVBO(levelSegment)
            self.vboRenderer.render(vbo)


def makeLevelRenderer(resolver):
    return LevelRenderer(
        resolver.resolve(GameData),
        resolver.resolve(LevelRenderModel3dCollection),
        resolver.resolve(ShadowCastLevelItemCollection),
        resolver.resolve(VBORenderer),
    )
