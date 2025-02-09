from OpenGL.GL import *

from game.render.level.LevelSegmentRenderer import LevelSegmentRenderer
from game.render.main.ShadowedObjectRenderer import ShadowedObjectRenderer
from game.render.weapon.PlayerWeaponRenderer import PlayerWeaponRenderer


class MainSceneRenderer:

    def __init__(self, shadowedObjectRenderer, levelSegmentRenderer, playerWeaponRenderer):
        self.shadowedObjectRenderer = shadowedObjectRenderer
        self.levelSegmentRenderer = levelSegmentRenderer
        self.playerWeaponRenderer = playerWeaponRenderer

    def renderDefaultAimState(self):
        self.shadowedObjectRenderer.render(self.defaultAimStateFunc, self.levelSegmentRenderer.renderShadowCasters)

    def renderSniperAimState(self):
        self.shadowedObjectRenderer.render(self.sniperAimStateFunc, self.levelSegmentRenderer.renderShadowCasters)

    def defaultAimStateFunc(self, shader):
        self.levelSegmentRenderer.render(shader)
        self.playerWeaponRenderer.render(shader)

    def sniperAimStateFunc(self, shader):
        self.levelSegmentRenderer.render(shader)


def makeMainSceneRenderer(resolver):
    return MainSceneRenderer(
        resolver.resolve(ShadowedObjectRenderer),
        resolver.resolve(LevelSegmentRenderer),
        resolver.resolve(PlayerWeaponRenderer),
    )
