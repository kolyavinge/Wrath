from game.engine.ai.state.AttackStateHandler import AttackStateHandler
from game.engine.ai.state.HealthSearchStateHandler import HealthSearchStateHandler
from game.engine.ai.state.IdleStateHandler import IdleStateHandler
from game.engine.ai.state.PatrollingStateHandler import PatrollingStateHandler
from game.engine.ai.state.WeaponSearchStateHandler import WeaponSearchStateHandler
from game.model.ai.AIData import EnemyState


class StateHandlerCollection:

    def __init__(
        self,
        idleState: IdleStateHandler,
        patrollingState: PatrollingStateHandler,
        attackState: AttackStateHandler,
        healthSearchState: HealthSearchStateHandler,
        weaponSearchState: WeaponSearchStateHandler,
    ):
        self.states = {}
        self.states[EnemyState.idle] = idleState
        self.states[EnemyState.patrolling] = patrollingState
        self.states[EnemyState.attack] = attackState
        self.states[EnemyState.healthSearch] = healthSearchState
        self.states[EnemyState.weaponSearch] = weaponSearchState

    def getStateHandler(self, enemyState):
        return self.states[enemyState]
