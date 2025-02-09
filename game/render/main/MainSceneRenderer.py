from OpenGL.GL import *

from game.render.level.LevelRenderer import LevelRenderer
from game.render.main.ShadowedObjectRenderer import ShadowedObjectRenderer
from game.render.weapon.PlayerWeaponRenderer import PlayerWeaponRenderer


class MainSceneRenderer:

    def __init__(self, shadowedObjectRenderer, levelRenderer, playerWeaponRenderer):
        self.shadowedObjectRenderer = shadowedObjectRenderer
        self.levelRenderer = levelRenderer
        self.playerWeaponRenderer = playerWeaponRenderer

    def renderDefaultAimState(self):
        self.shadowedObjectRenderer.render(self.defaultAimStateFunc, self.levelRenderer.renderShadowCasters)

    def renderSniperAimState(self):
        self.shadowedObjectRenderer.render(self.sniperAimStateFunc, self.levelRenderer.renderShadowCasters)

    def defaultAimStateFunc(self, shader):
        self.levelRenderer.renderLevelSegments(shader)
        self.playerWeaponRenderer.render(shader)

    def sniperAimStateFunc(self, shader):
        self.levelRenderer.renderLevelSegments(shader)


def makeMainSceneRenderer(resolver):
    return MainSceneRenderer(
        resolver.resolve(ShadowedObjectRenderer),
        resolver.resolve(LevelRenderer),
        resolver.resolve(PlayerWeaponRenderer),
    )
