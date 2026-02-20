import sys

import OpenGL

OpenGL.ERROR_CHECKING = False
from OpenGL.GL import GL_NO_ERROR, glGetError, glViewport
from OpenGL.GLU import gluErrorString
from OpenGL.GLUT import *

from game.anx.CommonConstants import CommonConstants
from game.core.GameFactory import GameFactory
from game.core.GameStartMode import GameStartMode
from game.input.Keyboard import KeyboardButtons
from game.lib.EventManager import Events
from game.lib.Screen import Screen
from game.tools.CpuProfiler import CpuProfiler


class App:

    def __init__(self):
        self.isFullscreen = False
        self.windowWidth = 1000
        self.windowHeight = (int)(self.windowWidth / CommonConstants.screenAspect)

    def run(self):
        glutInit()
        glutInitWindowSize(self.windowWidth, self.windowHeight)
        x, y = Screen.getCenterWindowPosition(self.windowWidth, self.windowHeight)
        glutInitWindowPosition(x, y)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
        glutSetOption(GLUT_ACTION_ON_WINDOW_CLOSE, GLUT_ACTION_EXIT)
        glutCreateWindow(CommonConstants.gameTitle)
        glutDisplayFunc(self.render)
        glutReshapeFunc(self.resize)
        glutKeyboardUpFunc(self.keyup)
        glutSetCursor(GLUT_CURSOR_NONE)
        glutWMCloseFunc(self.closeWindow)
        gameStartMode = GameStartMode.clientMode if "clientMode" in sys.argv else GameStartMode.clientServerMode
        self.game = GameFactory.makeGame(gameStartMode)
        # self.game = GameFactory.makeGame(GameStartMode.clientServerMode, levelDebugMode=True)  # отладочный режим для рисования местности
        glutTimerFunc(CommonConstants.mainTimerMsec, self.mainTimerCallback, 0)
        glutMainLoop()

    def mainTimerCallback(self, value):
        self.game.updateCurrentScreen()
        self.game.voxCurrentScreen()
        glutPostRedisplay()
        glutTimerFunc(CommonConstants.mainTimerMsec, self.mainTimerCallback, 0)

    def render(self):
        self.game.renderCurrentScreen()
        glutSwapBuffers()
        error = glGetError()
        if error != GL_NO_ERROR:
            raise Exception(f"OpenGL error: {gluErrorString(error)}")

    def resize(self, width, height):
        glViewport(0, 0, width, height)
        self.game.eventManager.raiseEvent(Events.viewportSizeChanged, (width, height))

    def keyup(self, key, x, y):
        if key == KeyboardButtons.esc:
            glutLeaveMainLoop()
        elif key == KeyboardButtons.backspace:
            self.toggleFullscreen()

    def toggleFullscreen(self):
        self.isFullscreen = not self.isFullscreen
        if self.isFullscreen:
            glutFullScreen()
        else:
            glutReshapeWindow(self.windowWidth, self.windowHeight)
            x, y = Screen.getCenterWindowPosition(self.windowWidth, self.windowHeight)
            glutPositionWindow(x, y)

    def closeWindow(self):
        self.game.eventManager.raiseEvent(Events.appExited)
        self.game.finalize()


print("\r\nStart the app")

app = App()
app.run()

CpuProfiler.makeResultIfNeeded()
