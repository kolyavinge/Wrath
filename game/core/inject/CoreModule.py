from game.core.ClientPersonInitializer import *
from game.core.Game import *
from game.core.GameInitializer import *
from game.core.ScreenManager import *


class CoreModule:

    def init(self, binder):
        binder.bindSingleton(ClientPersonInitializer)
        binder.bindSingleton(Game)
        binder.bindSingleton(GameInitializer)
        binder.bindSingleton(ScreenManager)
