from game.engine.CameraUpdater import CameraUpdater
from game.engine.GameData import GameData
from game.engine.level.BackgroundVisibilityUpdater import BackgroundVisibilityUpdater
from game.engine.person.PersonPositionUpdater import PersonPositionUpdater
from game.engine.person.PersonTurnUpdater import PersonTurnUpdater
from game.engine.person.PersonUpdater import PersonUpdater
from game.engine.person.PersonVelocityUpdater import PersonVelocityUpdater


class LevelDebugGameUpdater:

    gameData: GameData
    personTurnUpdater: PersonTurnUpdater
    personVelocityUpdater: PersonVelocityUpdater
    backgroundVisibilityUpdater: BackgroundVisibilityUpdater
    personPositionUpdater: PersonPositionUpdater
    personUpdater: PersonUpdater
    cameraUpdater: CameraUpdater

    def update(self):
        self.personTurnUpdater.update()
        self.personVelocityUpdater.update()
        self.personPositionUpdater.moveNextPosition()
        self.personPositionUpdater.commitNextPosition()
        self.cameraUpdater.update()
        self.backgroundVisibilityUpdater.updateIfNeeded()
        self.personPositionUpdater.resetMovedAndTurned()
