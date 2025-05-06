from game.engine.ai.AttackStateHandler import AttackStateHandler
from game.engine.ai.HealthSearchStateHandler import HealthSearchStateHandler
from game.engine.ai.PatrollingStateHandler import PatrollingStateHandler
from game.engine.ai.WeaponSearchStateHandler import WeaponSearchStateHandler
from game.model.person.Enemy import EnemyState


class StateHandlerCollection:

    def __init__(self, patrollingState, attackState, healthSearchState, weaponSearchState):
        self.states = {}
        self.states[EnemyState.patrolling] = patrollingState
        self.states[EnemyState.attack] = attackState
        self.states[EnemyState.healthSearch] = healthSearchState
        self.states[EnemyState.weaponSearch] = weaponSearchState

    def getStateHandler(self, enemyState):
        return self.states[enemyState]


def makeStateHandlerCollection(resolver):
    return StateHandlerCollection(
        resolver.resolve(PatrollingStateHandler),
        resolver.resolve(AttackStateHandler),
        resolver.resolve(HealthSearchStateHandler),
        resolver.resolve(WeaponSearchStateHandler),
    )
