from OpenGL.GL import *

from game.anx.CommonConstants import CommonConstants
from game.calc.PlaneOrientationLogic import PlaneOrientationLogic
from game.calc.TransformMatrix4 import TransformMatrix4
from game.engine.GameData import GameData
from game.gl.BufferIndices import BufferIndices
from game.gl.ColorVector3 import ColorVector3
from game.gl.vbo.VBORenderer import VBORenderer
from game.gl.vbo.VBOUpdaterFactory import VBOUpdaterFactory
from game.render.common.ShaderProgramCollection import ShaderProgramCollection


class RayParams:

    def __init__(self):
        self.rayHeight = 0
        self.rayColor = ColorVector3()
        self.shineStrength = 0


class PlaneRayRenderer:

    def __init__(
        self,
        gameData: GameData,
        planeOrientationLogic: PlaneOrientationLogic,
        vboUpdaterFactory: VBOUpdaterFactory,
        shaderProgramCollection: ShaderProgramCollection,
        vboRenderer: VBORenderer,
    ):
        self.gameData = gameData
        self.planeOrientationLogic = planeOrientationLogic
        self.vboUpdater = vboUpdaterFactory.makeVBOUpdater()
        self.shaderProgramCollection = shaderProgramCollection
        self.vboRenderer = vboRenderer
        self.vbo = self.vboUpdater.buildUnfilled(
            4 * CommonConstants.maxRaysCount, 2 * CommonConstants.maxRaysCount, [BufferIndices.vertices, BufferIndices.faces]
        )

    def render(self, rays, params):
        self.vbo.reset()
        originPositions = []
        mainAxes = []
        rayLengths = []
        rayBrightnesses = []
        for ray in rays:
            rayDirection = ray.startPosition.getDirectionTo(ray.currentPosition)
            mainAxis = rayDirection.copy()
            mainAxis.normalize()
            vertices = self.planeOrientationLogic.getVerticesOrientedToCamera(
                ray.startPosition,
                ray.currentPosition,
                mainAxis,
                self.gameData.camera.position,
            )
            self.addVerticesToVBO(vertices)
            originPositions.append(ray.startPosition)
            mainAxes.append(mainAxis)
            rayLengths.append(rayDirection.getLength())
            rayBrightnesses.append(ray.brightness)

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
        self.vboUpdater.addFace(0, 2, 3)

        self.vboUpdater.endUpdate()
