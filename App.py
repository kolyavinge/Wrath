import os
import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from game.anx.CommonConstants import CommonConstants
from game.core.GameFactory import GameFactory
from game.lib.Environment import Environment
from game.lib.Screen import Screen


class App:

    def __init__(self):
        Environment.programRootPath = os.path.dirname(__file__)

    def resize(self, width, height):
        glViewport(0, 0, width, height)

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.game.renderCurrentScreen()
        glutSwapBuffers()

    def run(self):
        glutInit(sys.argv)
        windowWidth = 1200
        windowHeight = (int)(windowWidth / CommonConstants.screenAspect)
        glutInitWindowSize(windowWidth, windowHeight)
        screenWidth, screenHeight = Screen.getWidthAndHeight()
        glutInitWindowPosition(int((screenWidth - windowWidth) / 2), int((screenHeight - windowHeight) / 2))
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
        glutCreateWindow(CommonConstants.gameTitle)
        glutDisplayFunc(self.render)
        glutReshapeFunc(self.resize)
        glutKeyboardUpFunc(self.keyup)
        glutSetCursor(GLUT_CURSOR_NONE)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        gameFactory = GameFactory()
        self.game = gameFactory.makeGame()
        glutTimerFunc(CommonConstants.mainTimerMsec, self.timerCallback, 0)
        glutMainLoop()

    def timerCallback(self, value):
        self.game.updateCurrentScreen()
        glutPostRedisplay()
        glutTimerFunc(CommonConstants.mainTimerMsec, self.timerCallback, 0)

    def keyup(self, key, a, b):
        if key == b"\x1b":  # Esc
            Environment.shutdown()


app = App()
app.run()
