from game.model.weapon.Launcher import Launcher
from game.model.weapon.Pistol import Pistol
from game.model.weapon.Plasma import Plasma
from game.model.weapon.Railgun import Railgun
from game.model.weapon.Rifle import Rifle
from game.model.weapon.Sniper import Sniper


class AllWeaponTypes:

    @staticmethod
    def getList():
        return [Pistol, Rifle, Plasma, Launcher, Railgun, Sniper]
