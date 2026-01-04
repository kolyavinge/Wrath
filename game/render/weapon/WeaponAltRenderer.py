from game.engine.GameState import GameState
from game.model.weapon.Railgun import Railgun
from game.render.weapon.anx.RailgunChargingRenderer import RailgunChargingRenderer


class WeaponAltRenderer:

    def __init__(
        self,
        gameData: GameState,
        railgunChargingRenderer: RailgunChargingRenderer,
    ):
        self.gameData = gameData
        self.renderers = {}
        self.renderers[Railgun] = railgunChargingRenderer

    def renderPlayerWeapon(self):
        weaponType = self.gameData.playerItems.getCurrentWeaponType()
        if weaponType in self.renderers:
            self.renderers[weaponType].renderPlayerWeapon(self.gameData.playerItems.currentWeapon)
