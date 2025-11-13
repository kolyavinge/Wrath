from game.gl.ShaderProgram import ShaderProgram


class PlasmaExplosionShaderProgram(ShaderProgram):

    def __init__(self, shaders):
        super().__init__(shaders)

    def initBeforeLink(self):
        self.setOutputNamesForTransformFeedback(["UpdatedPosition", "UpdatedVelocity", "UpdatedAge"])

    def setPassNumber(self, passNumber):
        self.setInt32("passNumber", passNumber)

    def setViewMatrix(self, viewMatrix):
        self.setTransformMatrix4("viewMatrix", viewMatrix)

    def setProjectionMatrix(self, projectionMatrix):
        self.setTransformMatrix4("projectionMatrix", projectionMatrix)

    def setParticleLifeTime(self, particleLifeTime):
        self.setFloat32("particleLifeTime", particleLifeTime)

    def setParticleSize(self, particleSize):
        self.setFloat32("particleSize", particleSize)

    def setDeltaTime(self, deltaTime):
        self.setFloat32("deltaTime", deltaTime)
