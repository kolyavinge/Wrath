from OpenGL.GL import *

from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Plane import Plane
from game.calc.TransformMatrix4 import TransformMatrix4
from game.engine.GameData import GameData
from game.gl.BufferIndices import BufferIndices
from game.gl.ColorVector3 import ColorVector3
from game.gl.vbo.VBORenderer import VBORenderer
from game.gl.vbo.VBOUpdaterFactory import VBOUpdaterFactory
from game.lib.Math import Math
from game.render.common.ShaderProgramCollection import ShaderProgramCollection


class RayParams:

    def __init__(self):
        self.rayHeight = 0
        self.rayColor = ColorVector3()
        self.shineStrength = 0


class RayRenderer:

    def __init__(
        self,
        gameData: GameData,
        vboUpdaterFactory: VBOUpdaterFactory,
        shaderProgramCollection: ShaderProgramCollection,
        vboRenderer: VBORenderer,
    ):
        self.gameData = gameData
        self.vboUpdater = vboUpdaterFactory.makeVBOUpdater()
        self.shaderProgramCollection = shaderProgramCollection
        self.vboRenderer = vboRenderer
        self.vbo = self.makeVBO()

    def render(self, traces, params):
        self.vbo.reset()
        originPositions = []
        mainAxes = []
        rayLengths = []
        rayBrightnesses = []
        for trace in traces:
            rayDirection = trace.startPosition.getDirectionTo(trace.currentPosition)
            mainAxis = rayDirection.copy()
            mainAxis.normalize()
            plane = self.getPlane(trace.startPosition, trace.currentPosition, mainAxis)
            vertices = self.getVertices(trace.startPosition, trace.currentPosition, plane, mainAxis)
            self.addVerticesToVBO(vertices)
            originPositions.append(trace.startPosition)
            mainAxes.append(mainAxis)
            rayLengths.append(rayDirection.getLength())
            rayBrightnesses.append(trace.brightness)

        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_ALPHA_TEST)
        glEnable(GL_DEPTH_TEST)
        shader = self.shaderProgramCollection.ray
        shader.use()
        shader.setModelMatrix(TransformMatrix4.identity)
        shader.setViewMatrix(self.gameData.camera.viewMatrix)
        shader.setProjectionMatrix(self.gameData.camera.projectionMatrix)
        shader.setOriginPositions(originPositions)
        shader.setMainAxes(mainAxes)
        shader.setRayLengths(rayLengths)
        shader.setRayHeight(params.rayHeight)
        shader.setRayColor(params.rayColor)
        shader.setRayBrightnesses(rayBrightnesses)
        shader.setShineStrength(params.shineStrength)
        self.vboRenderer.render(self.vbo)
        shader.unuse()
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)

    def addVerticesToVBO(self, vertices):
        self.vboUpdater.beginUpdate(self.vbo)

        self.vboUpdater.addVertex(vertices[0])
        self.vboUpdater.addVertex(vertices[1])
        self.vboUpdater.addVertex(vertices[2])
        self.vboUpdater.addVertex(vertices[3])

        self.vboUpdater.addFace(0, 1, 2)
        self.vboUpdater.addFace(1, 3, 2)

        self.vboUpdater.endUpdate()

    def getVertices(self, startPosition, endPosition, plane, mainAxis):  # ф-я не относится к рендеру луча, убрать в другой класс, в BulletTrace
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

    def getPlane(self, startPosition, endPosition, mainAxis):  # ф-я не относится к рендеру луча
        rotatedCameraPosition = Geometry.rotatePoint(self.gameData.camera.position, mainAxis, startPosition, Math.piHalf)
        plane = Plane.makeByThreePoints(rotatedCameraPosition, startPosition, endPosition)

        return plane

    def makeVBO(self):
        maxTracesCount = 100
        vbo = self.vboUpdater.buildUnfilled(4 * maxTracesCount, 2 * maxTracesCount, [BufferIndices.vertices, BufferIndices.faces])

        return vbo
