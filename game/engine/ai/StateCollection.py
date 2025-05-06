from game.engine.ai.AttackState import AttackState
from game.engine.ai.HealthSearchState import HealthSearchState
from game.engine.ai.PatrollingState import PatrollingState
from game.engine.ai.WeaponSearchState import WeaponSearchState
from game.model.person.Enemy import EnemyState


class StateCollection:

    def __init__(self, patrollingState, attackState, healthSearchState, weaponSearchState):
        self.states = {}
        self.states[EnemyState.patrolling] = patrollingState
        self.states[EnemyState.attack] = attackState
        self.states[EnemyState.healthSearch] = healthSearchState
        self.states[EnemyState.weaponSearch] = weaponSearchState

    def getState(self, enemyState):
        return self.states[enemyState]


def makeStateCollection(resolver):
    return StateCollection(
        resolver.resolve(PatrollingState), resolver.resolve(AttackState), resolver.resolve(HealthSearchState), resolver.resolve(WeaponSearchState)
    )
