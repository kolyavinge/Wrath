from game.anx.CommonConstants import CommonConstants
from game.anx.PersonConstants import PersonConstants
from game.calc.Geometry import Geometry
from game.engine.GameData import GameData
from game.lib.Math import Math


class PersonTurnLogic:

    def __init__(self, gameData):
        self.gameData = gameData

    def process(self):
        for person, inputData in self.gameData.allPersonInputData.items():
            self.processForPerson(person, inputData)

    def processForPerson(self, person, inputData):
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
        person.hasTurned = True
        person.yawRadians = Geometry.normalizeRadians(person.yawRadians + radians)
        self.calculateDirectionVectors(person)

    def turnRight(self, person, radians):
        assert radians > 0
        person.hasTurned = True
        person.yawRadians = Geometry.normalizeRadians(person.yawRadians - radians)
        self.calculateDirectionVectors(person)

    def lookUp(self, person, radians):
        assert radians > 0
        person.hasTurned = True
        person.pitchRadians = Geometry.normalizeRadians(person.pitchRadians + radians)
        if person.pitchRadians >= PersonConstants.maxPitchRadians:
            person.pitchRadians = PersonConstants.maxPitchRadians
        self.calculateDirectionVectors(person)

    def lookDown(self, person, radians):
        assert radians > 0
        person.hasTurned = True
        person.pitchRadians = Geometry.normalizeRadians(person.pitchRadians - radians)
        if person.pitchRadians <= -PersonConstants.maxPitchRadians:
            person.pitchRadians = -PersonConstants.maxPitchRadians
        self.calculateDirectionVectors(person)

    def orientByFrontNormal(self, person, frontNormal):
        radians = Math.arccos(person.frontNormal.dotProduct(frontNormal))
        vectorProduct = person.frontNormal.copy()
        vectorProduct.vectorProduct(frontNormal)
        if vectorProduct.z < 0:
            radians *= -1
        person.yawRadians = radians
        self.calculateDirectionVectors(person)

    def calculateDirectionVectors(self, person):
        person.frontNormal = Geometry.rotatePoint(CommonConstants.yAxis, CommonConstants.zAxis, CommonConstants.axisOrigin, person.yawRadians)
        person.rightNormal = Geometry.rotatePoint(person.frontNormal, CommonConstants.zAxis, CommonConstants.axisOrigin, -Math.piHalf)
        person.lookDirection = Geometry.rotatePoint(person.frontNormal, person.rightNormal, CommonConstants.axisOrigin, person.pitchRadians)
        person.lookDirectionNormal = Geometry.rotatePoint(person.lookDirection, person.rightNormal, CommonConstants.axisOrigin, Math.piHalf)


def makePersonTurnLogic(resolver):
    return PersonTurnLogic(resolver.resolve(GameData))
