from game.engine.person.PersonTurnLogic import PersonTurnLogic


class GameStateSynchronizer:

    def __init__(
        self,
        personTurnLogic: PersonTurnLogic,
    ):
        self.personTurnLogic = personTurnLogic

    def applySnapshotDiff(self, gameState, diff):
        if hasattr(diff, "player"):
            person = gameState.allPersonById[diff.player.id]
            person.moveNextPositionTo(diff.player.centerPoint)
            self.personTurnLogic.setYawPitchRadians(person, diff.player.yawRadians, diff.player.pitchRadians)
            person.commitNextPosition()
