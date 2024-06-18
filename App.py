import os
import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from game.anx.Constants import Constants
from game.core.GameFactory import GameFactory
from game.lib.Environment import Environment
from game.lib.Screen import Screen


class App:

    def __init__(self):
        Environment.programRootPath = os.path.dirname(__file__)

    def resize(self, width, height):
        glViewport(0, 0, width, height)

    def render(self):
        gameData = self.game.levelManager.gameData
        level = self.game.levelManager.gameData.level
        player = self.game.levelManager.gameData.player
        camera = self.game.levelManager.gameData.camera

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
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

        glColor3f(0.5, 0.5, 0.5)
        for wall in level.floors[0].walls:
            glBegin(GL_QUADS)
            glVertex3f(wall.startPoint.x, wall.startPoint.y, wall.startPoint.z)
            glVertex3f(wall.endPoint.x, wall.endPoint.y, wall.endPoint.z)
            glVertex3f(wall.endPoint.x, wall.endPoint.y, wall.endPoint.z + 1)
            glVertex3f(wall.startPoint.x, wall.startPoint.y, wall.startPoint.z + 1)
            glEnd()

        glDisable(GL_DEPTH_TEST)

        glEnable(GL_BLEND)
        glColor4f(1, 0, 0, 0.2)

        for levelSegment in player.levelSegments:
            glBegin(GL_QUADS)
            glVertex3f(levelSegment.minX, levelSegment.minY, 0)
            glVertex3f(levelSegment.maxX, levelSegment.minY, 0)
            glVertex3f(levelSegment.maxX, levelSegment.maxY, 0)
            glVertex3f(levelSegment.minX, levelSegment.maxY, 0)
            glEnd()

        for levelSegment in player.levelSegments:
            for wall in levelSegment.walls:
                glBegin(GL_QUADS)
                glVertex3f(wall.startPoint.x, wall.startPoint.y, wall.startPoint.z)
                glVertex3f(wall.endPoint.x, wall.endPoint.y, wall.endPoint.z)
                glVertex3f(wall.endPoint.x, wall.endPoint.y, wall.endPoint.z + 1)
                glVertex3f(wall.startPoint.x, wall.startPoint.y, wall.startPoint.z + 1)
                glEnd()
        glDisable(GL_BLEND)

        glColor3f(1, 1, 0)
        for levelSegment in player.levelSegments:
            for wall in levelSegment.walls:
                glBegin(GL_LINES)
                glVertex3f(wall.crossLine.startPoint.x, wall.crossLine.startPoint.y, wall.startPoint.z)
                glVertex3f(wall.crossLine.endPoint.x, wall.crossLine.endPoint.y, wall.endPoint.z)
                glEnd()

        glEnable(GL_BLEND)
        glColor4f(0, 1, 0, 0.2)
        border = player.currentBorder.bottom
        glBegin(GL_QUADS)
        glVertex3f(border.downLeft.x, border.downLeft.y, border.downLeft.z)
        glVertex3f(border.downRight.x, border.downRight.y, border.downRight.z)
        glVertex3f(border.upRight.x, border.upRight.y, border.upRight.z)
        glVertex3f(border.upLeft.x, border.upLeft.y, border.upLeft.z)
        glEnd()
        glDisable(GL_BLEND)

        glColor3f(0, 1, 0)
        glBegin(GL_LINES)
        v = player.currentCenterPoint.getCopy()
        v.add(player.frontNormal)
        glVertex3f(player.currentCenterPoint.x, player.currentCenterPoint.y, player.currentCenterPoint.z)
        glVertex3f(v.x, v.y, v.z)
        glEnd()

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

        glutSwapBuffers()

    def run(self):
        glutInit(sys.argv)
        windowWidth = 1200
        windowHeight = (int)(windowWidth / Constants.screenAspect)
        glutInitWindowSize(windowWidth, windowHeight)
        screenWidth, screenHeight = Screen.getWidthAndHeight()
        glutInitWindowPosition(int((screenWidth - windowWidth) / 2), int((screenHeight - windowHeight) / 2))
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
        glutCreateWindow(Constants.gameTitle)
        glutDisplayFunc(self.render)
        glutReshapeFunc(self.resize)
        glutKeyboardUpFunc(self.keyup)
        glutSetCursor(GLUT_CURSOR_NONE)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        gameFactory = GameFactory()
        self.game = gameFactory.makeGame()
        glutTimerFunc(Constants.mainTimerMsec, self.timerCallback, 0)
        glutMainLoop()

    def timerCallback(self, value):
        self.game.updateCurrentScreen()
        glutPostRedisplay()
        glutTimerFunc(Constants.mainTimerMsec, self.timerCallback, 0)

    def keyup(self, key, a, b):
        if key == b"\x1b":  # Esc
            Environment.shutdown()


app = App()
app.run()
