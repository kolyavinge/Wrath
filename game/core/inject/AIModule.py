from game.engine.ai.common.BurstFireLogic import *
from game.engine.ai.common.EnemyCollisionDetector import *
from game.engine.ai.common.FireLogic import *
from game.engine.ai.common.MovingLogic import *
from game.engine.ai.common.ObstacleAvoidanceLogic import *
from game.engine.ai.common.PowerupFinder import *
from game.engine.ai.common.RouteCollisionDetector import *
from game.engine.ai.common.RouteFinder import *
from game.engine.ai.common.RouteOptimizer import *
from game.engine.ai.EnemyAIUpdater import *
from game.engine.ai.state.AttackStateHandler import *
from game.engine.ai.state.HealthSearchStateHandler import *
from game.engine.ai.state.IdleStateHandler import *
from game.engine.ai.state.PatrollingStateHandler import *
from game.engine.ai.state.StateHandlerCollection import *
from game.engine.ai.state.WeaponSearchStateHandler import *


class AIModule:

    def init(self, binder):
        binder.bindSingleton(BurstFireLogic)
        binder.bindSingleton(EnemyCollisionDetector)
        binder.bindSingleton(FireLogic)
        binder.bindSingleton(MovingLogic)
        binder.bindSingleton(ObstacleAvoidanceLogic)
        binder.bindSingleton(PowerupFinder)
        binder.bindSingleton(RouteCollisionDetector)
        binder.bindSingleton(RouteFinder)
        binder.bindSingleton(RouteOptimizer)
        binder.bindSingleton(AttackStateHandler)
        binder.bindSingleton(HealthSearchStateHandler)
        binder.bindSingleton(IdleStateHandler)
        binder.bindSingleton(PatrollingStateHandler)
        binder.bindSingleton(StateHandlerCollection)
        binder.bindSingleton(WeaponSearchStateHandler)
