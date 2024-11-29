from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Plane import Plane
from game.calc.TransformMatrix4 import TransformMatrix4
from game.engine.GameData import GameData
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

    def renderTrace(self, trace):
        plane = self.getPlane(trace)
        vertices = self.getVertices(trace, plane)
        self.updateVBO(vertices)
        shader = self.shaderProgramCollection.mesh
        shader.use()
        shader.setModelMatrix(TransformMatrix4.identity)
        shader.setViewMatrix(self.gameData.camera.viewMatrix)
        shader.setProjectionMatrix(self.gameData.camera.projectionMatrix)
        shader.setAlpha(1)
        self.vboRenderer.render(self.vbo)
        shader.unuse()

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

    def getVertices(self, trace, plane):
        axis = trace.startPosition.getDirectionTo(trace.currentPosition)
        axis.normalize()
        normal = plane.getNormal()
        step = Geometry.rotatePoint(normal, axis, CommonConstants.axisOrigin, Math.piHalf)
        step.setLength(0.05)

        p1 = trace.startPosition.copy()
        p2 = trace.startPosition.copy()
        p3 = trace.currentPosition.copy()
        p4 = trace.currentPosition.copy()

        p1.add(step)
        p2.sub(step)
        p3.add(step)
        p4.sub(step)

        return [p1, p2, p3, p4]

    def getPlane(self, trace):
        axis = trace.startPosition.getDirectionTo(trace.currentPosition)
        axis.normalize()
        rotatedCameraPosition = Geometry.rotatePoint(self.gameData.camera.position, axis, CommonConstants.axisOrigin, Math.piHalf)
        plane = Plane.makeByThreePoints(rotatedCameraPosition, trace.startPosition, trace.currentPosition)

        return plane


def makeRailgunBulletTraceRenderer(resolver):
    return RailgunBulletTraceRenderer(
        resolver.resolve(GameData), resolver.resolve(VBOUpdaterFactory), resolver.resolve(ShaderProgramCollection), resolver.resolve(VBORenderer)
    )
