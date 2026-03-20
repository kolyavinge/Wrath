from game.render.gl.ShaderProgram import ShaderProgram


class ShineCircleShaderProgram(ShaderProgram):

    def __init__(self, shaders):
        super().__init__(shaders)

    def setModelMatrix(self, modelMatrix):
        self.uniformSetter.setTransformMatrix4("modelMatrix", modelMatrix)

    def setViewMatrix(self, viewMatrix):
        self.uniformSetter.setTransformMatrix4("viewMatrix", viewMatrix)

    def setProjectionMatrix(self, projectionMatrix):
        self.uniformSetter.setTransformMatrix4("projectionMatrix", projectionMatrix)

    def setRadius(self, radius):
        self.uniformSetter.setFloat32("radius", radius)

    def setShineColor(self, colorVector):
        self.uniformSetter.setVector3("shineColor", colorVector)

    def setShineStrength(self, value):
        self.uniformSetter.setFloat32("shineStrength", value)

    def setScreenAspect(self, screenAspect):
        self.uniformSetter.setFloat32("screenAspect", screenAspect)
