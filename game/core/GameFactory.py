from game.lib.DependencyContainer import DependencyContainer
from game.core.inject.CoreModule import CoreModule
from game.core.inject.EngineModule import EngineModule
from game.core.inject.UIModule import UIModule
from game.core.Game import Game


class GameFactory:

    def makeGame(self):
        container = DependencyContainer()
        container.initFromModule(CoreModule())
        container.initFromModule(EngineModule())
        container.initFromModule(UIModule())

        game = container.resolve(Game)

        container.errorIfUnusedInstances()

        return game
