from game.core.Game import *
from game.core.GameInitializer import *
from game.core.ScreenManager import *


class CoreModule:

    def init(self, binder):
        binder.bindSingleton(Game, makeGame)
        binder.bindSingleton(GameInitializer, makeGameInitializer)
        binder.bindSingleton(ScreenManager, makeScreenManager)
