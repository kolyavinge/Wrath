from game.core.Game import Game
from game.core.inject.CoreModule import CoreModule
from game.core.inject.EngineModule import EngineModule
from game.core.inject.LibModule import LibModule
from game.core.inject.RenderModule import RenderModule
from game.core.inject.UIModule import UIModule
from game.lib.DependencyContainer import DependencyContainer


class GameFactory:

    @staticmethod
    def makeGame():
        container = DependencyContainer()
        container.initFromModule(LibModule())
        container.initFromModule(CoreModule())
        container.initFromModule(EngineModule())
        container.initFromModule(UIModule())
        container.initFromModule(RenderModule())

        game = container.resolve(Game)

        container.errorIfUnusedInstances()

        return game
