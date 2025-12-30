from game.engine.person.AimStateSwitcher import AimStateSwitcher
from game.model.weapon.Weapon import FireState


class SniperAltFireLogic:

    def __init__(self, aimStateSwitcher: AimStateSwitcher):
        self.aimStateSwitcher = aimStateSwitcher

    def apply(self, person, personItems, weapon):
        if weapon.altFireState == FireState.activated:
            self.aimStateSwitcher.switchDefaultOrSniper()
