from game.ui.GameScreen import *
from game.ui.ScreenManager import *


class UIModule:

    def init(self, binder):
        binder.bindSingleton(GameScreen, makeGameScreen)
        binder.bindSingleton(ScreenManager, makeScreenManager)
