from game.gl.ShaderProgram import ShaderProgram


class FireExplosionShaderProgram(ShaderProgram):

    def __init__(self, shaders):
        super().__init__(shaders)

    def setViewMatrix(self, viewMatrix):
        self.uniformSetter.setTransformMatrix4("viewMatrix", viewMatrix)

    def setProjectionMatrix(self, projectionMatrix):
        self.uniformSetter.setTransformMatrix4("projectionMatrix", projectionMatrix)

    def setInitTimeSec(self, initTimeSec):
        self.uniformSetter.setFloat32("initTimeSec", initTimeSec)

    def setCurrentTimeSec(self, currentTimeSec):
        self.uniformSetter.setFloat32("currentTimeSec", currentTimeSec)
