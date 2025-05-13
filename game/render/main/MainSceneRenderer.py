from OpenGL.GL import *

from game.render.level.LevelSegmentRenderer import LevelSegmentRenderer
from game.render.main.ShadowedObjectRenderer import ShadowedObjectRenderer
from game.render.weapon.WeaponRenderer import WeaponRenderer


class MainSceneRenderer:

    def __init__(
        self,
        shadowedObjectRenderer: ShadowedObjectRenderer,
        levelSegmentRenderer: LevelSegmentRenderer,
        weaponRenderer: WeaponRenderer,
    ):
        self.shadowedObjectRenderer = shadowedObjectRenderer
        self.levelSegmentRenderer = levelSegmentRenderer
        self.weaponRenderer = weaponRenderer

    def renderDefaultAimState(self):
        self.shadowedObjectRenderer.render(self.defaultAimStateFunc, self.levelSegmentRenderer.renderShadowCasters)

    def renderSniperAimState(self):
        self.shadowedObjectRenderer.render(self.sniperAimStateFunc, self.levelSegmentRenderer.renderShadowCasters)

    def defaultAimStateFunc(self, shader):
        self.levelSegmentRenderer.render(shader)
        self.weaponRenderer.renderAllWeapons(shader)

    def sniperAimStateFunc(self, shader):
        self.levelSegmentRenderer.render(shader)
        self.weaponRenderer.renderEnemyWeapons(shader)
