from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.lib.Math import Math
from game.lib.Numeric import Numeric


class PersonTurnLogic:

    def orientToFrontNormal(self, person, frontNormal):
        dotProduct = person.frontNormal.dotProduct(frontNormal)
        dotProduct = Numeric.limitBy(dotProduct, -1.0, 1.0)
        radians = Math.arccos(dotProduct)
        if not Numeric.floatEquals(radians, 0.0):
            person.hasTurned = True
            vectorProduct = person.frontNormal.copy()
            vectorProduct.vectorProduct(frontNormal)
            if vectorProduct.z < 0.0:
                radians *= -1.0
            person.yawRadians = Geometry.normalizeRadians(person.yawRadians + radians)
            self.calculateDirectionVectors(person)

    def calculateDirectionVectors(self, person):
        person.frontNormal = Geometry.rotatePoint(CommonConstants.yAxis, CommonConstants.zAxis, CommonConstants.axisOrigin, person.yawRadians)
        person.rightNormal = Geometry.rotatePoint(person.frontNormal, CommonConstants.zAxis, CommonConstants.axisOrigin, -Math.piHalf)
        person.lookDirection = Geometry.rotatePoint(person.frontNormal, person.rightNormal, CommonConstants.axisOrigin, person.pitchRadians)
        person.lookDirectionNormal = Geometry.rotatePoint(person.lookDirection, person.rightNormal, CommonConstants.axisOrigin, Math.piHalf)


def makePersonTurnLogic(resolver):
    return PersonTurnLogic()
