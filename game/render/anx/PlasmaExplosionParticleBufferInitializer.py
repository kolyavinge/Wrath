from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Plane import Plane
from game.engine.GameState import GameState
from game.gl.FeedbackParticleBufferFactory import FeedbackParticleBufferFactory
from game.lib.Math import Math
from game.lib.Random import Random
from game.model.person.Person import Person


class PlasmaExplosionParticleBufferInitializer:

    def __init__(
        self,
        gameData: GameState,
        particleBufferFactory: FeedbackParticleBufferFactory,
    ):
        self.gameData = gameData
        self.particleBufferFactory = particleBufferFactory

    def makeEmpty(self, explosion):
        particlesCount = explosion.particlesInGroup * explosion.particleGroupsCount
        buffer = self.particleBufferFactory.make(particlesCount)

        return buffer

    def init(self, buffer, explosion):
        buffer.setPositionData(self.getPositionData(explosion))
        buffer.setVelocityData(self.getVelocityData(explosion))
        buffer.setAgeData(self.getAgeData(explosion))

    def getPositionData(self, explosion):
        positionData = []
        particlesCount = explosion.particlesInGroup * explosion.particleGroupsCount
        damagedObject = explosion.bullet.damagedObject
        if isinstance(damagedObject, Person):
            explosionPosition = self.gameData.camera.getCameraFacedNormal(explosion.position)
            explosionPosition.setLength(0.5)
            explosionPosition.add(explosion.position)
        else:
            explosionPosition = explosion.position
        for _ in range(0, particlesCount):
            positionData.append(explosionPosition)

        return positionData

    def getVelocityData(self, explosion):
        velocityDataForGroup = []
        damagedObject = explosion.bullet.damagedObject
        if isinstance(damagedObject, Person):
            planeNormal = self.gameData.camera.getCameraFacedNormal(explosion.position)
        else:
            planeNormal = damagedObject.frontNormal
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
