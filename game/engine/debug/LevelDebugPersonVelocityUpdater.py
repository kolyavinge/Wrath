from game.engine.GameState import GameState


class LevelDebugPersonVelocityUpdater:

    def __init__(self, gameData: GameState):
        self.gameData = gameData

    def update(self):
        for person, inputData in self.gameData.allPersonInputData.items():
            self.updateForPerson(person, inputData)

    def updateForPerson(self, person, inputData):
        person.prevVelocityValue = person.velocityValue

        person.velocityValue = 0
        person.velocityVector.set(0, 0, 0)

        if inputData.goForward:
            person.velocityVector.add(person.lookDirection)
        elif inputData.goBackward:
            person.velocityVector.sub(person.lookDirection)

        if inputData.stepLeft:
            person.velocityVector.sub(person.rightNormal)
        elif inputData.stepRight:
            person.velocityVector.add(person.rightNormal)

        if not person.velocityVector.isZero():
            person.velocityValue = 0.25 * (2.0 if inputData.jump else 1.0)
            person.velocityVector.setLength(person.velocityValue)
