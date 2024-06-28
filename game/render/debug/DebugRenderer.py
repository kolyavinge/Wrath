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
        # self.renderFloorGrid()
        self.renderWalls()
        self.renderWallCrossLines()
        self.renderFloors()
        self.renderLevelSegmentFloors()
        self.renderLevelSegmentWalls()
        self.renderPlayerBorder()
        # self.renderAxis()

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
            glVertex3f(x, 1000, 0)
            glEnd()
            x += 1

        y = 0
        while y < 1000:
            glBegin(GL_LINES)
            glVertex3f(0, y, 0)
            glVertex3f(1000, y, 0)
            glEnd()
            y += 1
        glDisable(GL_DEPTH_TEST)

    def renderWalls(self):
        glEnable(GL_DEPTH_TEST)
        glColor3f(0.4, 0.4, 0.4)
        for levelSegment in self.gameData.visibleLevelSegments:
            for wall in levelSegment.walls:
                startPointUp = wall.startPoint.getCopy()
                endPointUp = wall.endPoint.getCopy()
                startPointUp.z += wall.height
                endPointUp.z += wall.height
                self.renderGridQuad(wall.startPoint, wall.endPoint, startPointUp, endPointUp)
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

    def renderFloors(self):
        glEnable(GL_DEPTH_TEST)
        for levelSegment in self.gameData.visibleLevelSegments:
            for floor in levelSegment.floors:
                self.renderGridQuad(floor.downLeft, floor.downRight, floor.upLeft, floor.upRight)
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

    def renderLevelSegmentWalls(self):
        player = self.gameData.player
        glEnable(GL_BLEND)
        glColor4f(1, 0, 0, 0.2)
        for levelSegment in player.levelSegments:
            for wall in levelSegment.walls:
                glBegin(GL_QUADS)
                glVertex3f(wall.startPoint.x, wall.startPoint.y, wall.startPoint.z)
                glVertex3f(wall.endPoint.x, wall.endPoint.y, wall.endPoint.z)
                glVertex3f(wall.endPoint.x, wall.endPoint.y, wall.endPoint.z + wall.height)
                glVertex3f(wall.startPoint.x, wall.startPoint.y, wall.startPoint.z + wall.height)
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

    def renderGridQuad(self, downLeft, downRight, upLeft, upRight):
        glColor3f(0.4, 0.4, 0.4)
        glBegin(GL_QUADS)
        glVertex3f(downLeft.x, downLeft.y, downLeft.z)
        glVertex3f(downRight.x, downRight.y, downRight.z)
        glVertex3f(upRight.x, upRight.y, upRight.z)
        glVertex3f(upLeft.x, upLeft.y, upLeft.z)
        glEnd()

        glColor3f(0.1, 0.1, 0.1)

        downDirection = downRight.getCopy()
        downDirection.sub(downLeft)
        upDirection = upRight.getCopy()
        upDirection.sub(upLeft)
        x = 1
        width = min(downDirection.getLength(), upDirection.getLength())
        downDirection.setLength(1)
        upDirection.setLength(1)
        while x < width:
            left = downLeft.getCopy()
            left.add(downDirection)
            right = upLeft.getCopy()
            right.add(upDirection)
            glBegin(GL_LINES)
            glVertex3f(left.x, left.y, left.z)
            glVertex3f(right.x, right.y, right.z)
            glEnd()
            downDirection.setLength(downDirection.getLength() + 1)
            upDirection.setLength(upDirection.getLength() + 1)
            x += 1

        leftDirection = upLeft.getCopy()
        leftDirection.sub(downLeft)
        rightDirection = upRight.getCopy()
        rightDirection.sub(downRight)
        y = 1
        height = min(leftDirection.getLength(), rightDirection.getLength())
        leftDirection.setLength(1)
        rightDirection.setLength(1)
        while y < height:
            left = downLeft.getCopy()
            left.add(leftDirection)
            right = downRight.getCopy()
            right.add(rightDirection)
            glBegin(GL_LINES)
            glVertex3f(left.x, left.y, left.z)
            glVertex3f(right.x, right.y, right.z)
            glEnd()
            leftDirection.setLength(leftDirection.getLength() + 1)
            rightDirection.setLength(rightDirection.getLength() + 1)
            y += 1


def makeDebugRenderer(resolver):
    return DebugRenderer(resolver.resolve(GameData))
