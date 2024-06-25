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
        level = gameData.level
        player = gameData.player
        camera = gameData.camera

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
        level = self.game.levelManager.gameData.level
        glColor3f(0.5, 0.5, 0.5)
        for wall in level.walls:
            glBegin(GL_QUADS)
            glVertex3f(wall.startPoint.x, wall.startPoint.y, wall.startPoint.z)
            glVertex3f(wall.endPoint.x, wall.endPoint.y, wall.endPoint.z)
            glVertex3f(wall.endPoint.x, wall.endPoint.y, wall.endPoint.z + 1)
            glVertex3f(wall.startPoint.x, wall.startPoint.y, wall.startPoint.z + 1)
            glEnd()
        glDisable(GL_DEPTH_TEST)

        self.game.renderCurrentScreen()

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
