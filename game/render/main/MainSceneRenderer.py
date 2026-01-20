from game.engine.GameState import GameState
from game.render.level.LevelSegmentRenderer import LevelSegmentRenderer
from game.render.main.ShadowedObjectRenderer import ShadowedObjectRenderer
from game.render.weapon.WeaponAltRenderer import WeaponAltRenderer
from game.render.weapon.WeaponRenderer import WeaponRenderer


class MainSceneRenderer:

    def __init__(
        self,
        gameState: GameState,
        shadowedObjectRenderer: ShadowedObjectRenderer,
        levelSegmentRenderer: LevelSegmentRenderer,
        weaponRenderer: WeaponRenderer,
        weaponAltRenderer: WeaponAltRenderer,
    ):
        self.gameState = gameState
        self.shadowedObjectRenderer = shadowedObjectRenderer
        self.levelSegmentRenderer = levelSegmentRenderer
        self.weaponRenderer = weaponRenderer
        self.weaponAltRenderer = weaponAltRenderer

    def renderDefaultAimState(self):
        self.shadowedObjectRenderer.render(self.defaultAimStateFunc, self.levelSegmentRenderer.renderShadowCasters)

    def renderSniperAimState(self):
        self.shadowedObjectRenderer.render(self.sniperAimStateFunc, self.levelSegmentRenderer.renderShadowCasters)

    def defaultAimStateFunc(self, shader):
        self.levelSegmentRenderer.render(shader)
        self.weaponRenderer.renderPlayerWeapon(self.gameState.playerItems, shader)
        self.weaponRenderer.renderEnemyWeapons(self.gameState.enemyItems, shader)
        self.weaponAltRenderer.renderPlayerWeapon()

    def sniperAimStateFunc(self, shader):
        self.levelSegmentRenderer.render(shader)
        self.weaponRenderer.renderEnemyWeapons(shader)
