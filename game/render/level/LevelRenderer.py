from OpenGL.GL import *

from game.engine.GameData import GameData
from game.render.level.LevelItemRenderer import LevelItemRenderer
from game.render.level.ShadowCasterRenderer import ShadowCasterRenderer
from game.render.person.EnemyRenderer import EnemyRenderer
from game.render.powerup.PowerupRenderer import PowerupRenderer
from game.render.weapon.BulletHoleRenderer import BulletHoleRenderer
from game.render.weapon.BulletRenderer import BulletRenderer


class LevelRenderer:

    def __init__(self, gameData, levelItemRenderer, bulletRenderer, bulletHoleRenderer, powerupRenderer, enemyRenderer, shadowCasterRenderer):
        self.gameData = gameData
        self.levelItemRenderer = levelItemRenderer
        self.bulletRenderer = bulletRenderer
        self.bulletHoleRenderer = bulletHoleRenderer
        self.powerupRenderer = powerupRenderer
        self.enemyRenderer = enemyRenderer
        self.shadowCasterRenderer = shadowCasterRenderer

    def renderLevelSegments(self, shader):
        for levelSegment in self.gameData.visibleLevelSegments:
            shader.setLight(levelSegment.lightsWithJoined, self.gameData.playerTorch)
            self.levelItemRenderer.render(shader, levelSegment)
            self.bulletRenderer.render(shader, levelSegment)
            self.bulletHoleRenderer.render(shader, levelSegment)
            self.powerupRenderer.render(shader, levelSegment)
            self.enemyRenderer.render(shader, levelSegment)

    def renderShadowCasters(self, shader):
        for levelSegment in self.gameData.visibleLevelSegments:
            shader.setLight(levelSegment.lights, self.gameData.playerTorch)
            self.shadowCasterRenderer.render(levelSegment)


def makeLevelRenderer(resolver):
    return LevelRenderer(
        resolver.resolve(GameData),
        resolver.resolve(LevelItemRenderer),
        resolver.resolve(BulletRenderer),
        resolver.resolve(BulletHoleRenderer),
        resolver.resolve(PowerupRenderer),
        resolver.resolve(EnemyRenderer),
        resolver.resolve(ShadowCasterRenderer),
    )
