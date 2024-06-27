from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from game.anx.Constants import Constants
from game.engine.GameData import GameData


class DebugRenderer:

    def __init__(self, gameData):
        self.gameData = gameData

    def render(self):
        self.initCamera()
        self.renderFloorGrid()
        self.renderLevelSegmentFloors()
        self.renderWalls()
        self.renderWallCrossLines()
        self.renderLevelSegmentWalls()
        self.renderPlayerBorder()
        self.renderAxis()

    def initCamera(self):
        camera = self.gameData.camera
        glLoadIdentity()
        glMatrixMode(GL_PROJECTION)
        gluPerspective(camera.viewAngleDegrees, Constants.screenAspect, Constants.minDepth, Constants.maxDepth)
        gluLookAt(
            camera.position.x,
            camera.position.y,
            camera.position.z,
            camera.position.x + camera.lookDirection.x,
            camera.position.y + camera.lookDirection.y,
            camera.position.z + camera.lookDirection.z,
            0,
            0,
            1,
        )

    def renderFloorGrid(self):
        glEnable(GL_DEPTH_TEST)
        glColor3f(0.25, 0.25, 0.25)
        x = 0
        while x < 1000:
            glBegin(GL_LINES)
            glVertex3f(x, 0, 0)
            glVertex3f(x, 100, 0)
            glEnd()
            x += 1

        y = 0
        while y < 1000:
            glBegin(GL_LINES)
            glVertex3f(0, y, 0)
            glVertex3f(100, y, 0)
            glEnd()
            y += 1
        glDisable(GL_DEPTH_TEST)

    def renderLevelSegmentFloors(self):
        player = self.gameData.player
        glEnable(GL_BLEND)
        glColor4f(1, 0, 0, 0.2)
        for levelSegment in player.levelSegments:
            glBegin(GL_QUADS)
            glVertex3f(levelSegment.minX, levelSegment.minY, levelSegment.minZ)
            glVertex3f(levelSegment.maxX, levelSegment.minY, levelSegment.minZ)
            glVertex3f(levelSegment.maxX, levelSegment.maxY, levelSegment.minZ)
            glVertex3f(levelSegment.minX, levelSegment.maxY, levelSegment.minZ)
            glEnd()
        glDisable(GL_BLEND)

    def renderWalls(self):
        glEnable(GL_DEPTH_TEST)
        glColor3f(0.5, 0.5, 0.5)
        for wall in self.gameData.level.walls:
            glBegin(GL_QUADS)
            glVertex3f(wall.startPoint.x, wall.startPoint.y, wall.startPoint.z)
            glVertex3f(wall.endPoint.x, wall.endPoint.y, wall.endPoint.z)
            glVertex3f(wall.endPoint.x, wall.endPoint.y, wall.endPoint.z + 1)
            glVertex3f(wall.startPoint.x, wall.startPoint.y, wall.startPoint.z + 1)
            glEnd()
        glDisable(GL_DEPTH_TEST)

    def renderWallCrossLines(self):
        player = self.gameData.player
        glEnable(GL_DEPTH_TEST)
        glColor3f(1, 1, 0)
        for levelSegment in player.levelSegments:
            for wall in levelSegment.walls:
                glBegin(GL_LINES)
                glVertex3f(wall.crossLine.startPoint.x, wall.crossLine.startPoint.y, wall.startPoint.z)
                glVertex3f(wall.crossLine.endPoint.x, wall.crossLine.endPoint.y, wall.endPoint.z)
                glEnd()
        glDisable(GL_DEPTH_TEST)

    def renderLevelSegmentWalls(self):
        player = self.gameData.player
        glEnable(GL_BLEND)
        glColor4f(1, 0, 0, 0.2)
        for levelSegment in player.levelSegments:
            for wall in levelSegment.walls:
                glBegin(GL_QUADS)
                glVertex3f(wall.startPoint.x, wall.startPoint.y, wall.startPoint.z)
                glVertex3f(wall.endPoint.x, wall.endPoint.y, wall.endPoint.z)
                glVertex3f(wall.endPoint.x, wall.endPoint.y, wall.endPoint.z + 1)
                glVertex3f(wall.startPoint.x, wall.startPoint.y, wall.startPoint.z + 1)
                glEnd()
        glDisable(GL_BLEND)

    def renderPlayerBorder(self):
        border = self.gameData.player.currentBorder.bottom
        glEnable(GL_BLEND)
        glColor4f(0, 1, 0, 0.2)
        glBegin(GL_QUADS)
        glVertex3f(border.downLeft.x, border.downLeft.y, border.downLeft.z)
        glVertex3f(border.downRight.x, border.downRight.y, border.downRight.z)
        glVertex3f(border.upRight.x, border.upRight.y, border.upRight.z)
        glVertex3f(border.upLeft.x, border.upLeft.y, border.upLeft.z)
        glEnd()
        glDisable(GL_BLEND)

    def renderAxis(self):
        glColor3f(1, 0, 0)
        glBegin(GL_LINES)
        glVertex3f(0, 0, 0)
        glVertex3f(100, 0, 0)
        glEnd()

        glColor3f(0, 1, 0)
        glBegin(GL_LINES)
        glVertex3f(0, 0, 0)
        glVertex3f(0, 100, 0)
        glEnd()

        glColor3f(0, 0, 1)
        glBegin(GL_LINES)
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, 100)
        glEnd()


def makeDebugRenderer(resolver):
    return DebugRenderer(resolver.resolve(GameData))
