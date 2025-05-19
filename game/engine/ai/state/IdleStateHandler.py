from game.calc.Vector3 import Vector3
from game.engine.ai.common.FireLogic import FireLogic
from game.engine.ai.common.MovingLogic import MovingLogic
from game.engine.GameData import GameData
from game.engine.person.PersonTurnLogic import PersonTurnLogic
from game.lib.Random import Random
from game.model.ai.AIData import EnemyState


class IdleStateHandler:

    def __init__(
        self,
        gameData: GameData,
        movingLogic: MovingLogic,
        fireLogic: FireLogic,
        personTurnLogic: PersonTurnLogic,
    ):
        self.gameData = gameData
        self.movingLogic = movingLogic
        self.fireLogic = fireLogic
        self.personTurnLogic = personTurnLogic
        self.rand = Random()

    def init(self, enemy):
        enemy.aiData.idleTimeLimit = self.rand.getInt(100, 400)
        enemy.aiData.idleTurnTimeLimit = self.rand.getInt(50, 200)

    def process(self, enemy, inputData):
        aiData = enemy.aiData
        if aiData.idleTurnTimeLimit > 0:
            aiData.idleTurnTimeLimit -= 1
            if aiData.idleTurnTimeLimit == 0:
                newFrontNormal = Vector3.getRandomNormalVector()
                self.personTurnLogic.orientToFrontNormal(enemy, newFrontNormal)

    def getNewStateOrNone(self, enemy):
        if enemy.aiData.stateTime > enemy.aiData.idleTimeLimit:
            return EnemyState.patrolling

        if self.fireLogic.targetExists(enemy):
            return EnemyState.attack

        return None
