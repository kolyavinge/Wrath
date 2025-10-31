from OpenGL.GL import GL_SEPARATE_ATTRIBS, glTransformFeedbackVaryings

from game.gl.ShaderProgram import ShaderProgram
from game.lib.sys import convertListToLPLPChar


class LauncherBulletTraceShaderProgram(ShaderProgram):

    def __init__(self, shaders):
        super().__init__(shaders)

    def initBeforeLink(self):
        outputNames = ["Position", "Velocity", "Age"]
        glTransformFeedbackVaryings(self.id, len(outputNames), convertListToLPLPChar(outputNames), GL_SEPARATE_ATTRIBS)

    def setPassNumber(self, passNumber):
        self.setInt32("passNumber", passNumber)

    def setTracePosition(self, tracePosition):
        self.setVector3("tracePosition", tracePosition)

    def setBulletDirection(self, bulletDirection):
        self.setVector3("bulletDirection", bulletDirection)

    def setBulletDirectionTopNormal(self, bulletDirectionTopNormal):
        self.setVector3("bulletDirectionTopNormal", bulletDirectionTopNormal)

    def setBulletNozzleRadius(self, bulletNozzleRadius):
        self.setFloat32("bulletNozzleRadius", bulletNozzleRadius)

    def setIsBulletAlive(self, isBulletAlive):
        self.setBoolean("isBulletAlive", isBulletAlive)

    def setViewMatrix(self, viewMatrix):
        self.setTransformMatrix4("viewMatrix", viewMatrix)

    def setProjectionMatrix(self, projectionMatrix):
        self.setTransformMatrix4("projectionMatrix", projectionMatrix)

    def setParticleAppearanceDelay(self, particleAppearanceDelay):
        self.setFloat32("particleAppearanceDelay", particleAppearanceDelay)

    def setParticleLifeTime(self, particleLifeTime):
        self.setFloat32("particleLifeTime", particleLifeTime)

    def setParticleSize(self, particleSize):
        self.setFloat32("particleSize", particleSize)

    def setDeltaTime(self, deltaTime):
        self.setFloat32("deltaTime", deltaTime)
