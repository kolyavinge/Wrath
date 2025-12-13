from game.engine.person.AimStateSwitcher import AimStateSwitcher
from game.model.person.PersonInputData import FireState


class SniperAltFireLogic:

    def __init__(self, aimStateSwitcher: AimStateSwitcher):
        self.aimStateSwitcher = aimStateSwitcher

    def apply(self, person, weapon, inputData):
        if inputData.altFireState == FireState.activated:
            self.aimStateSwitcher.switchDefaultOrSniper()
