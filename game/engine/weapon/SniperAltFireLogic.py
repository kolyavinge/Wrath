from game.engine.person.AimStateSwitcher import AimStateSwitcher


class SniperAltFireLogic:

    def __init__(self, aimStateSwitcher: AimStateSwitcher):
        self.aimStateSwitcher = aimStateSwitcher

    def apply(self, person, weapon, inputData):
        if inputData.altFireClick:
            self.aimStateSwitcher.switchDefaultOrSniper()
