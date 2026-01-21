from game.model.weapon.Railgun import Railgun
from game.render.weapon.anx.RailgunChargingRenderer import RailgunChargingRenderer


class WeaponAltRenderer:

    def __init__(
        self,
        railgunChargingRenderer: RailgunChargingRenderer,
    ):
        self.renderers = {}
        self.renderers[Railgun] = railgunChargingRenderer

    def renderPlayerWeapon(self, playerItems, camera):
        weaponType = playerItems.getCurrentWeaponType()
        if weaponType in self.renderers:
            self.renderers[weaponType].renderPlayerWeapon(playerItems.currentWeapon, camera)
