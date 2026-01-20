from game.engine.GameState import GameState
from game.engine.level.BackgroundVisibilityUpdater import BackgroundVisibilityUpdater
from game.engine.person.CameraUpdater import CameraUpdater
from game.engine.person.PersonPositionUpdater import PersonPositionUpdater
from game.engine.person.PersonTurnUpdater import PersonTurnUpdater
from game.engine.person.PersonUpdater import PersonUpdater
from game.engine.person.PersonVelocityUpdater import PersonVelocityUpdater


class LevelDebugGameUpdater:

    gameState: GameState
    backgroundVisibilityUpdater: BackgroundVisibilityUpdater
    cameraUpdater: CameraUpdater
    personPositionUpdater: PersonPositionUpdater
    personTurnUpdater: PersonTurnUpdater
    personUpdater: PersonUpdater
    personVelocityUpdater: PersonVelocityUpdater

    def update(self):
        self.personTurnUpdater.updateForPlayer(self.gameState)
        self.personVelocityUpdater.updateForPlayer(self.gameState)
        self.personPositionUpdater.movePlayerNextPosition(self.gameState)
        self.personPositionUpdater.commitPlayerNextPosition(self.gameState)
        self.cameraUpdater.update(self.gameState)
        self.backgroundVisibilityUpdater.updateIfNeeded(self.gameState)
        self.personPositionUpdater.resetMovedAndTurned(self.gameState)
