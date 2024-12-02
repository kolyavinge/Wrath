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


class RayParams:

    def __init__(self):
        self.rayHeight = 0
        self.rayColor = ColorVector3()
        self.shineStrength = 0


class RayRenderer:

    def __init__(self, gameData, vboUpdaterFactory, shaderProgramCollection, vboRenderer):
        self.gameData = gameData
        self.vboUpdater = vboUpdaterFactory.makeVBOUpdater()
        self.shaderProgramCollection = shaderProgramCollection
        self.vboRenderer = vboRenderer
        self.vbo = self.vboUpdater.buildUnfilled(4, 2)

    def render(self, startPosition, endPosition, params):
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)

        mainAxis = startPosition.getDirectionTo(endPosition)
        mainAxis.normalize()
        plane = self.getPlane(startPosition, endPosition, mainAxis)
        vertices = self.getVertices(startPosition, endPosition, plane, mainAxis)
        self.updateVBO(vertices)
        shader = self.shaderProgramCollection.ray
        shader.use()
        shader.setModelMatrix(TransformMatrix4.identity)
        shader.setViewMatrix(self.gameData.camera.viewMatrix)
        shader.setProjectionMatrix(self.gameData.camera.projectionMatrix)
        shader.setOriginPosition(startPosition)
        shader.setMainAxis(mainAxis)
        shader.setRayHeight(params.rayHeight)
        shader.setRayColor(params.rayColor)
        shader.setShineStrength(params.shineStrength)
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

    def getVertices(self, startPosition, endPosition, plane, mainAxis):
        step = Geometry.rotatePoint(plane.getNormal(), mainAxis, CommonConstants.axisOrigin, Math.piHalf)
        step.setLength(1)

        p1 = startPosition.copy()
        p2 = startPosition.copy()
        p3 = endPosition.copy()
        p4 = endPosition.copy()

        p1.add(step)
        p2.sub(step)
        p3.add(step)
        p4.sub(step)

        return [p1, p2, p3, p4]

    def getPlane(self, startPosition, endPosition, mainAxis):
        rotatedCameraPosition = Geometry.rotatePoint(self.gameData.camera.position, mainAxis, CommonConstants.axisOrigin, Math.piHalf)
        plane = Plane.makeByThreePoints(rotatedCameraPosition, startPosition, endPosition)

        return plane


def makeRayRenderer(resolver):
    return RayRenderer(
        resolver.resolve(GameData), resolver.resolve(VBOUpdaterFactory), resolver.resolve(ShaderProgramCollection), resolver.resolve(VBORenderer)
    )