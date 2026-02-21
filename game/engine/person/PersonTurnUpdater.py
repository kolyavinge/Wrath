from game.anx.PersonConstants import PersonConstants
from game.calc.Geometry import Geometry
from game.engine.person.PersonTurnLogic import PersonTurnLogic


class PersonTurnUpdater:

    def __init__(
        self,
        personTurnLogic: PersonTurnLogic,
    ):
        self.personTurnLogic = personTurnLogic

    def updateForPlayer(self, gameState):
        self.updateForPerson(gameState.player, gameState.playerInputData)

    def updateForBots(self, gameState):
        for bot, inputData in gameState.botInputData.items():
            self.updateForPerson(bot, inputData)

    def updateForPerson(self, person, inputData):
        if inputData.turnLeftRadians > 0:
            self.turnLeft(person, inputData.turnLeftRadians)
        elif inputData.turnRightRadians > 0:
            self.turnRight(person, inputData.turnRightRadians)

        if inputData.lookUpRadians > 0:
            self.lookUp(person, inputData.lookUpRadians)
        elif inputData.lookDownRadians > 0:
            self.lookDown(person, inputData.lookDownRadians)

    def turnLeft(self, person, radians):
        assert radians > 0
        person.yawRadians = Geometry.normalizeRadians(person.yawRadians + radians)
        self.personTurnLogic.calculateDirectionVectors(person)

    def turnRight(self, person, radians):
        assert radians > 0
        person.yawRadians = Geometry.normalizeRadians(person.yawRadians - radians)
        self.personTurnLogic.calculateDirectionVectors(person)

    def lookUp(self, person, radians):
        assert radians > 0
        person.pitchRadians = Geometry.normalizeRadians(person.pitchRadians + radians)
        if person.pitchRadians >= PersonConstants.maxPitchRadians:
            person.pitchRadians = PersonConstants.maxPitchRadians
        self.personTurnLogic.calculateDirectionVectors(person)

    def lookDown(self, person, radians):
        assert radians > 0
        person.pitchRadians = Geometry.normalizeRadians(person.pitchRadians - radians)
        if person.pitchRadians <= -PersonConstants.maxPitchRadians:
            person.pitchRadians = -PersonConstants.maxPitchRadians
        self.personTurnLogic.calculateDirectionVectors(person)
