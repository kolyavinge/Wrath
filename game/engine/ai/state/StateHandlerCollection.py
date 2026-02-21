from game.engine.ai.state.AttackStateHandler import AttackStateHandler
from game.engine.ai.state.HealthSearchStateHandler import HealthSearchStateHandler
from game.engine.ai.state.IdleStateHandler import IdleStateHandler
from game.engine.ai.state.PatrollingStateHandler import PatrollingStateHandler
from game.engine.ai.state.WeaponSearchStateHandler import WeaponSearchStateHandler
from game.model.ai.AIData import BotState


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
        self.states[BotState.idle] = idleState
        self.states[BotState.patrolling] = patrollingState
        self.states[BotState.attack] = attackState
        self.states[BotState.healthSearch] = healthSearchState
        self.states[BotState.weaponSearch] = weaponSearchState

    def getStateHandler(self, botState):
        return self.states[botState]
