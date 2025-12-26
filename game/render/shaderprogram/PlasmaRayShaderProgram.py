from game.gl.ShaderProgram import ShaderProgram


class PlasmaRayShaderProgram(ShaderProgram):

    def __init__(self, shaders):
        super().__init__(shaders)

    def setModelMatrix(self, modelMatrix):
        self.setTransformMatrix4("modelMatrix", modelMatrix)

    def setViewMatrix(self, viewMatrix):
        self.setTransformMatrix4("viewMatrix", viewMatrix)

    def setProjectionMatrix(self, projectionMatrix):
        self.setTransformMatrix4("projectionMatrix", projectionMatrix)

    def setResolution(self, width, height):
        self.setVector2("resolution", width, height)

    def setStartPosition(self, startPosition):
        self.setVector3("startPosition", startPosition)

    def setInitTimeSec(self, initTimeSec):
        self.setFloat32("initTimeSec", initTimeSec)

    def setCurrentTimeSec(self, currentTimeSec):
        self.setFloat32("currentTimeSec", currentTimeSec)
