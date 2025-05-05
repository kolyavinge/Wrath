from game.engine.ai.AttackState import AttackState
from game.engine.ai.HealthSearchState import HealthSearchState
from game.engine.ai.PatrollingState import PatrollingState
from game.engine.ai.WeaponSearchState import WeaponSearchState
from game.engine.GameData import GameData
from game.model.person.Enemy import EnemyState


class EnemyAILogic:

    def __init__(self, gameData, patrollingState, attackState, healthSearchState, weaponSearchState):
        self.gameData = gameData
        self.states = {}
        self.states[EnemyState.patrolling] = patrollingState
        self.states[EnemyState.attack] = attackState
        self.states[EnemyState.healthSearch] = healthSearchState
        self.states[EnemyState.weaponSearch] = weaponSearchState

    def apply(self):
        for enemy in self.gameData.enemies:
            inputData = self.gameData.enemyInputData[enemy]
            inputData.clear()
            aiData = enemy.aiData
            state = self.states[aiData.state]
            state.process(enemy, inputData)
            newState = state.getNewStateOrNone(enemy)
            if newState is not None:
                aiData.state = newState


def makeEnemyAILogic(resolver):
    return EnemyAILogic(
        resolver.resolve(GameData),
        resolver.resolve(PatrollingState),
        resolver.resolve(AttackState),
        resolver.resolve(HealthSearchState),
        resolver.resolve(WeaponSearchState),
    )
