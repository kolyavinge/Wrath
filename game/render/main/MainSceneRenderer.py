from game.render.level.LevelSegmentRenderer import LevelSegmentRenderer
from game.render.main.ShadowedObjectRenderer import ShadowedObjectRenderer
from game.render.weapon.WeaponAltRenderer import WeaponAltRenderer
from game.render.weapon.WeaponRenderer import WeaponRenderer


class MainSceneRenderer:

    def __init__(
        self,
        shadowedObjectRenderer: ShadowedObjectRenderer,
        levelSegmentRenderer: LevelSegmentRenderer,
        weaponRenderer: WeaponRenderer,
        weaponAltRenderer: WeaponAltRenderer,
    ):
        self.shadowedObjectRenderer = shadowedObjectRenderer
        self.levelSegmentRenderer = levelSegmentRenderer
        self.weaponRenderer = weaponRenderer
        self.weaponAltRenderer = weaponAltRenderer

    def init(self, gameState):
        self.gameState = gameState

    def renderDefaultAimState(self):
        self.shadowedObjectRenderer.render(self.gameState.camera, self.defaultAimStateFunc, self.renderShadowCasters)

    def renderSniperAimState(self):
        self.shadowedObjectRenderer.render(self.gameState.camera, self.sniperAimStateFunc, self.renderShadowCasters)

    def defaultAimStateFunc(self, shader):
        self.levelSegmentRenderer.render(self.gameState, shader)
        self.weaponRenderer.renderPlayerWeapon(self.gameState.playerItems, shader)
        self.weaponRenderer.renderEnemyWeapons(self.gameState.enemyItems, shader)
        self.weaponAltRenderer.renderPlayerWeapon(self.gameState.playerItems, self.gameState.camera)

    def sniperAimStateFunc(self, shader):
        self.levelSegmentRenderer.render(self.gameState, shader)
        self.weaponRenderer.renderEnemyWeapons(self.gameState.enemyItems, shader)

    def renderShadowCasters(self, shader):
        self.levelSegmentRenderer.renderShadowCasters(self.gameState.playerItems, self.gameState.visibleLevelSegments, shader)
