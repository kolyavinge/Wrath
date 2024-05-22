from game.core.Game import Game, makeGame


class CoreModule:

    def init(self, binder):
        binder.bindSingleton(Game, makeGame)
