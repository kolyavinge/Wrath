from game.engine.GameState import GameState
from game.model.weapon.Railgun import Railgun
from game.render.weapon.anx.RailgunChargingRenderer import RailgunChargingRenderer


class WeaponAltRenderer:

    def __init__(
        self,
        gameState: GameState,
        railgunChargingRenderer: RailgunChargingRenderer,
    ):
        self.gameState = gameState
        self.renderers = {}
        self.renderers[Railgun] = railgunChargingRenderer

    def renderPlayerWeapon(self):
        weaponType = self.gameState.playerItems.getCurrentWeaponType()
        if weaponType in self.renderers:
            self.renderers[weaponType].renderPlayerWeapon(self.gameState.playerItems.currentWeapon, self.gameState.camera)
