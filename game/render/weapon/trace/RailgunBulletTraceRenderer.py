from OpenGL.GL import *

from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Plane import Plane
from game.calc.TransformMatrix4 import TransformMatrix4
from game.engine.GameData import GameData
from game.gl.ColorVector3 import ColorVector3
from game.gl.VBORenderer import VBORenderer
from game.gl.VBOUpdaterFactory import VBOUpdaterFactory
from game.lib.Math import Math
from game.render.common.ShaderProgramCollection import ShaderProgramCollection


class RailgunBulletTraceRenderer:

    def __init__(self, gameData, vboUpdaterFactory, shaderProgramCollection, vboRenderer):
        self.gameData = gameData
        self.vboUpdater = vboUpdaterFactory.makeVBOUpdater()
        self.shaderProgramCollection = shaderProgramCollection
        self.vboRenderer = vboRenderer
        self.vbo = self.vboUpdater.buildUnfilled(4, 2)
        self.rayColor = ColorVector3(3, 252, 115)
        self.rayColor.normalize()

    def renderTrace(self, trace):
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)

        traceAxis = trace.startPosition.getDirectionTo(trace.currentPosition)
        traceAxis.normalize()
        rayHeight = 0.001
        plane = self.getPlane(trace, traceAxis)
        vertices = self.getVertices(trace, plane, traceAxis, rayHeight)
        self.updateVBO(vertices)
        shader = self.shaderProgramCollection.ray
        shader.use()
        shader.setModelMatrix(TransformMatrix4.identity)
        shader.setViewMatrix(self.gameData.camera.viewMatrix)
        shader.setProjectionMatrix(self.gameData.camera.projectionMatrix)
        shader.setOriginPosition(trace.startPosition)
        shader.setMainAxis(traceAxis)
        shader.setRayHeight(rayHeight)
        shader.setRayColor(self.rayColor)
        shader.setShineStrength(0.002)
        self.vboRenderer.render(self.vbo)
        shader.unuse()

        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)

    def updateVBO(self, vertices):
        self.vbo.refill()
        self.vboUpdater.beginUpdate(self.vbo)
        self.vboUpdater.addVertex(vertices[0])
        self.vboUpdater.addVertex(vertices[1])
        self.vboUpdater.addVertex(vertices[2])
        self.vboUpdater.addVertex(vertices[3])
        self.vboUpdater.addNormal(CommonConstants.axisOrigin)
        self.vboUpdater.addNormal(CommonConstants.axisOrigin)
        self.vboUpdater.addNormal(CommonConstants.axisOrigin)
        self.vboUpdater.addNormal(CommonConstants.axisOrigin)
        self.vboUpdater.addTexCoord(0, 0)
        self.vboUpdater.addTexCoord(0, 0)
        self.vboUpdater.addTexCoord(0, 0)
        self.vboUpdater.addTexCoord(0, 0)
        self.vboUpdater.addFace(0, 1, 2)
        self.vboUpdater.addFace(1, 3, 2)
        self.vboUpdater.endUpdate()

    def getVertices(self, trace, plane, traceAxis, rayHeight):
        step = Geometry.rotatePoint(plane.getNormal(), traceAxis, CommonConstants.axisOrigin, Math.piHalf)
        step.setLength(1)

        p1 = trace.startPosition.copy()
        p2 = trace.startPosition.copy()
        p3 = trace.currentPosition.copy()
        p4 = trace.currentPosition.copy()

        p1.add(step)
        p2.sub(step)
        p3.add(step)
        p4.sub(step)

        return [p1, p2, p3, p4]

    def getPlane(self, trace, traceAxis):
        rotatedCameraPosition = Geometry.rotatePoint(self.gameData.camera.position, traceAxis, CommonConstants.axisOrigin, Math.piHalf)
        plane = Plane.makeByThreePoints(rotatedCameraPosition, trace.startPosition, trace.currentPosition)

        return plane


def makeRailgunBulletTraceRenderer(resolver):
    return RailgunBulletTraceRenderer(
        resolver.resolve(GameData), resolver.resolve(VBOUpdaterFactory), resolver.resolve(ShaderProgramCollection), resolver.resolve(VBORenderer)
    )
