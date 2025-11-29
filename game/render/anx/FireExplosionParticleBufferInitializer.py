from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Vector3 import Vector3
from game.calc.Vector4 import Vector4
from game.engine.GameData import GameData
from game.gl.ParticleBuffer import ExtraParticleDataBuffers
from game.gl.ParticleBufferFactory import ParticleBufferFactory
from game.lib.Math import Math
from game.lib.Random import Random


class FireExplosionParticleBufferInitializer:

    def __init__(
        self,
        gameData: GameData,
        particleBufferFactory: ParticleBufferFactory,
    ):
        self.gameData = gameData
        self.particleBufferFactory = particleBufferFactory
        self.fireParticlesCount = 8
        self.flashParticlesCount = 1
        self.smokeParticlesCount = 32
        self.sparkParticlesCount = 16

    def makeEmpty(self, explosion):
        particlesCount = self.fireParticlesCount + self.flashParticlesCount + self.smokeParticlesCount + self.sparkParticlesCount
        buffer = self.particleBufferFactory.make(
            particlesCount,
            [ExtraParticleDataBuffers.lifeTimeBuffer, ExtraParticleDataBuffers.texCoordBuffer],
        )

        return buffer

    def init(self, buffer, explosion):
        buffer.setPositionData(self.getPositionData(explosion))
        buffer.setVelocityData(self.getVelocityData())
        buffer.setAgeData(self.getAgeData())
        buffer.setLifeTimeData(self.getLifeTimeData())
        buffer.setTexCoordData(self.getTexCoordData())

    def getPositionData(self, explosion):
        stepToCamera = self.gameData.camera.getCameraFacedNormal(explosion.position)
        stepToCamera.mul(0.5)
        initPosition = explosion.position.copy()
        initPosition.add(stepToCamera)

        positionData = []

        # fire
        jitter = Vector3(Random.getFloat(-1.0, 1.0), Random.getFloat(-1.0, 1.0), 0.0)
        jitter.setLength(0.5)
        fireInitPosition = initPosition.copy()
        fireInitPosition.z += 0.5
        for i in range(0, self.fireParticlesCount):
            point = Geometry.rotatePoint(jitter, CommonConstants.zAxis, CommonConstants.axisOrigin, i * Math.piHalf)
            point.add(fireInitPosition)
            point.z += Random.getFloat(-0.2, 0.2)
            positionData.append(point)

        # flash
        positionData.append(initPosition)

        # smoke
        for _ in range(0, self.smokeParticlesCount):
            positionData.append(explosion.position)

        # spark
        for _ in range(0, self.sparkParticlesCount):
            p = explosion.position.copy()
            p.x += Random.getFloat(-0.2, 0.2)
            p.y += Random.getFloat(-0.2, 0.2)
            p.z += Random.getFloat(-0.2, 0.2)
            positionData.append(p)

        return positionData

    def getVelocityData(self):
        velocityData = []

        # fire
        for _ in range(0, self.fireParticlesCount):
            x = Random.getFloat(-0.1, 0.1)
            y = Random.getFloat(-0.1, 0.1)
            z = Random.getFloat(0.1, 0.5)
            velocityData.append(Vector3(x, y, z))

        # flash
        velocityData.append(Vector3())

        # smoke
        p = Vector3(Random.getFloat(-1.0, 1.0), Random.getFloat(-1.0, 1.0), 0.0)
        p.setLength(2.0)
        radianStep = Math.piDouble / self.smokeParticlesCount
        for i in range(0, self.smokeParticlesCount):
            velocityData.append(Geometry.rotatePoint(p, CommonConstants.zAxis, CommonConstants.axisOrigin, i * radianStep))

        # spark
        for _ in range(0, self.sparkParticlesCount):
            v = Vector3.getRandomNormalVector()
            v.setLength(3.0)
            velocityData.append(v)

        return velocityData

    def getAgeData(self):
        ageData = []

        # fire
        for _ in range(0, self.fireParticlesCount):
            ageData.append(-Random.getFloat(0.0, 0.1))

        # flash
        ageData.append(0)

        # smoke
        for _ in range(0, self.smokeParticlesCount):
            ageData.append(0)

        # spark
        for _ in range(0, self.sparkParticlesCount):
            ageData.append(0)

        return ageData

    def getLifeTimeData(self):
        lifeTimeData = []

        # fire
        for _ in range(0, self.fireParticlesCount):
            lifeTimeData.append(Random.getFloat(2.5, 4.0))

        # flash
        lifeTimeData.append(0.2)

        # smoke
        for _ in range(0, self.smokeParticlesCount):
            lifeTimeData.append(1.0)

        # spark
        for _ in range(0, self.sparkParticlesCount):
            lifeTimeData.append(0.5)

        return lifeTimeData

    def getTexCoordData(self):
        texCoordData = []

        # fire
        for _ in range(0, self.fireParticlesCount):
            texCoordData.append(Vector4(0, 0, 0.5, 0.5))

        # flash
        texCoordData.append(Vector4(0.5, 0.0, 0.5, 0.5))

        # smoke
        for _ in range(0, self.smokeParticlesCount):
            texCoordData.append(Vector4(0.0, 0.5, 0.5, 0.5))

        # spark
        for _ in range(0, self.sparkParticlesCount):
            texCoordData.append(Vector4(0.5, 0.5, 0.5, 0.5))

        return texCoordData
