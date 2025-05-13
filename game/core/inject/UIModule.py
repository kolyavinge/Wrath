from game.ui.GameScreen import *


class UIModule:

    def init(self, binder):
        binder.bindSingleton(GameScreen)
