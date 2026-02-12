from game.core.Game import Game
from game.core.inject.AIModule import AIModule
from game.core.inject.CommonModule import CommonModule
from game.core.inject.CoreModule import CoreModule
from game.core.inject.EngineModule import EngineModule
from game.core.inject.LevelDebugModule import LevelDebugModule
from game.core.inject.NetworkModule import NetworkModule
from game.core.inject.RenderModule import RenderModule
from game.core.inject.UIModule import UIModule
from game.core.inject.VoxModule import VoxModule
from game.lib.DependencyContainer import DependencyContainer


class GameFactory:

    @staticmethod
    def makeGame(gameStartMode, levelDebugMode=False):
        container = DependencyContainer()
        container.initFromModule(AIModule())
        container.initFromModule(CommonModule())
        container.initFromModule(CoreModule())
        container.initFromModule(EngineModule())
        container.initFromModule(NetworkModule())
        container.initFromModule(RenderModule())
        container.initFromModule(UIModule())
        container.initFromModule(VoxModule())

        if levelDebugMode:
            container.initFromModule(LevelDebugModule())

        game = container.resolve(Game)
        game.init(gameStartMode)

        if not levelDebugMode:
            container.errorIfUnusedInstances()

        return game
