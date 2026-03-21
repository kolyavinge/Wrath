from game.render.lib.ShaderProgram import ShaderProgram


class ParticleBulletTraceShaderProgram(ShaderProgram):

    def __init__(self, shaders):
        super().__init__(shaders)

    def initBeforeLink(self):
        self.setOutputNamesForTransformFeedback(["UpdatedPosition", "UpdatedVelocity", "UpdatedAge"])

    def setPassNumber(self, passNumber):
        self.uniformSetter.setInt32("passNumber", passNumber)

    def setTracePosition(self, tracePosition):
        self.uniformSetter.setVector3("tracePosition", tracePosition)

    def setBulletDirection(self, bulletDirection):
        self.uniformSetter.setVector3("bulletDirection", bulletDirection)

    def setBulletDirectionTopNormal(self, bulletDirectionTopNormal):
        self.uniformSetter.setVector3("bulletDirectionTopNormal", bulletDirectionTopNormal)

    def setBulletNozzleRadius(self, bulletNozzleRadius):
        self.uniformSetter.setFloat32("bulletNozzleRadius", bulletNozzleRadius)

    def setIsBulletAlive(self, isBulletAlive):
        self.uniformSetter.setBoolean("isBulletAlive", isBulletAlive)

    def setViewMatrix(self, viewMatrix):
        self.uniformSetter.setTransformMatrix4("viewMatrix", viewMatrix)

    def setProjectionMatrix(self, projectionMatrix):
        self.uniformSetter.setTransformMatrix4("projectionMatrix", projectionMatrix)

    def setParticleLifeTime(self, particleLifeTime):
        self.uniformSetter.setFloat32("particleLifeTime", particleLifeTime)

    def setParticleSize(self, particleSize):
        self.uniformSetter.setFloat32("particleSize", particleSize)

    def setDeltaTime(self, deltaTime):
        self.uniformSetter.setFloat32("deltaTime", deltaTime)
