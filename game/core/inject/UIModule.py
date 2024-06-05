from game.ui.GameScreen import GameScreen, makeGameScreen
from game.ui.ScreenManager import ScreenManager, makeScreenManager


class UIModule:

    def init(self, binder):
        binder.bindSingleton(GameScreen, makeGameScreen)
        binder.bindSingleton(ScreenManager, makeScreenManager)
