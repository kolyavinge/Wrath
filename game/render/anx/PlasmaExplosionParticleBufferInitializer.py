from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Plane import Plane
from game.engine.GameData import GameData
from game.gl.FeedbackParticleBuffer import FeedbackParticleBuffer
from game.lib.Math import Math
from game.lib.Random import Random


class PlasmaExplosionParticleBufferInitializer:

    def __init__(self, gameData: GameData):
        self.gameData = gameData

    def makeEmpty(self, explosion):
        particlesCount = explosion.particlesInGroup * explosion.particleGroupsCount
        buffer = FeedbackParticleBuffer(particlesCount)

        return buffer

    def init(self, buffer, explosion):
        buffer.setPositionData(self.getPositionData(explosion))
        buffer.setVelocityData(self.getVelocityData(explosion))
        buffer.setAgeData(self.getAgeData(explosion))

    def getPositionData(self, explosion):
        positionData = []
        particlesCount = explosion.particlesInGroup * explosion.particleGroupsCount
        for _ in range(0, particlesCount):
            positionData.append(explosion.position)

        return positionData

    def getVelocityData(self, explosion):
        velocityDataForGroup = []
        planeNormal = explosion.bullet.damagedObject.frontNormal
        plane = Plane(planeNormal, explosion.position)
        initPoint = plane.getAnyVector()
        for _ in range(0, explosion.particlesInGroup):
            radians = Random.getFloat(0.0, Math.piDouble)
            point = Geometry.rotatePoint(initPoint, planeNormal, CommonConstants.axisOrigin, radians)
            point.setLength(Random.getFloat(0.8, 1.2) * explosion.velocityValue)
            velocityDataForGroup.append(point)

        velocityData = []
        for _ in range(0, explosion.particleGroupsCount):
            velocityData.extend(velocityDataForGroup)

        return velocityData

    def getAgeData(self, explosion):
        ageData = []
        for groupNumber in range(0, explosion.particleGroupsCount):
            appearanceDelayMsec = groupNumber * explosion.particleAppearanceDelayMsec
            ageData.extend([-appearanceDelayMsec] * explosion.particlesInGroup)

        return ageData
