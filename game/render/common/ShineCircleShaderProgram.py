from game.gl.ShaderProgram import ShaderProgram


class ShineCircleShaderProgram(ShaderProgram):

    def __init__(self, shaders):
        super().__init__(shaders)

    def setModelMatrix(self, modelMatrix):
        self.setTransformMatrix4("modelMatrix", modelMatrix)

    def setViewMatrix(self, viewMatrix):
        self.setTransformMatrix4("viewMatrix", viewMatrix)

    def setProjectionMatrix(self, projectionMatrix):
        self.setTransformMatrix4("projectionMatrix", projectionMatrix)

    def setRadius(self, radius):
        self.setFloat32("radius", radius)

    def setShineColor(self, colorVector):
        self.setVector3("shineColor", colorVector)

    def setShineStrength(self, value):
        self.setFloat32("shineStrength", value)

    def setScreenAspect(self, screenAspect):
        self.setFloat32("screenAspect", screenAspect)
