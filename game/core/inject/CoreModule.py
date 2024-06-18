from game.core.Game import *


class CoreModule:

    def init(self, binder):
        binder.bindSingleton(Game, makeGame)
