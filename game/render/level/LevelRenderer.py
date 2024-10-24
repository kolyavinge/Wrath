from OpenGL.GL import *

from game.engine.GameData import GameData
from game.render.level.LevelItemRenderer import LevelItemRenderer
from game.render.level.ShadowCasterRenderer import ShadowCasterRenderer
from game.render.weapon.BulletHoleRenderer import BulletHoleRenderer


class LevelRenderer:

    def __init__(self, gameData, levelItemRenderer, bulletHoleRenderer, shadowCasterRenderer):
        self.gameData = gameData
        self.levelItemRenderer = levelItemRenderer
        self.bulletHoleRenderer = bulletHoleRenderer
        self.shadowCasterRenderer = shadowCasterRenderer

    def init(self):
        allLevelSegments = self.gameData.level.visibilityTree.getAllLevelSegments()
        self.levelItemRenderer.init(allLevelSegments)
        self.bulletHoleRenderer.init(allLevelSegments)
        self.shadowCasterRenderer.init(allLevelSegments)

    def renderLevelSegments(self, shader):
        for levelSegment in self.gameData.visibleLevelSegments:
            shader.setLight(levelSegment.lightsWithJoined, self.gameData.playerItems.torch)
            self.levelItemRenderer.render(shader, levelSegment)
            self.bulletHoleRenderer.render(shader, levelSegment)

    def renderShadowCasters(self, shader):
        for levelSegment in self.gameData.visibleLevelSegments:
            shader.setLight(levelSegment.lights, self.gameData.playerItems.torch)
            self.shadowCasterRenderer.render(levelSegment)


def makeLevelRenderer(resolver):
    return LevelRenderer(
        resolver.resolve(GameData),
        resolver.resolve(LevelItemRenderer),
        resolver.resolve(BulletHoleRenderer),
        resolver.resolve(ShadowCasterRenderer),
    )
