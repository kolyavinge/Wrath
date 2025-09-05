import sys

import OpenGL

OpenGL.ERROR_CHECKING = False
from OpenGL.GL import GL_NO_ERROR, glGetError, glViewport
from OpenGL.GLU import gluErrorString
from OpenGL.GLUT import *

from game.anx.CommonConstants import CommonConstants
from game.anx.Events import Events
from game.core.GameFactory import GameFactory
from game.input.Keys import Keys
from game.lib.Screen import Screen
from game.tools.CpuProfiler import CpuProfiler


class App:

    def __init__(self):
        self.isFullscreen = False
        self.windowWidth = 1400
        self.windowHeight = (int)(self.windowWidth / CommonConstants.screenAspect)

    def resize(self, width, height):
        glViewport(0, 0, width, height)
        self.game.eventManager.raiseEvent(Events.viewportSizeChanged, (width, height))

    def render(self):
        self.game.renderCurrentScreen()
        glutSwapBuffers()
        error = glGetError()
        if error != GL_NO_ERROR:
            raise Exception(f"OpenGL error: {gluErrorString(error)}")

    def run(self):
        glutInit(sys.argv)
        glutInitWindowSize(self.windowWidth, self.windowHeight)
        x, y = self.getCenterWindowPosition()
        glutInitWindowPosition(x, y)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
        glutSetOption(GLUT_ACTION_ON_WINDOW_CLOSE, GLUT_ACTION_CONTINUE_EXECUTION)
        glutCreateWindow(CommonConstants.gameTitle)
        glutDisplayFunc(self.render)
        glutReshapeFunc(self.resize)
        glutKeyboardUpFunc(self.keyup)
        glutSetCursor(GLUT_CURSOR_NONE)
        self.game = GameFactory.makeGame()
        # self.game = GameFactory.makeGame(levelDebugMode=True)  # отладочный режим для рисования местности
        glutTimerFunc(CommonConstants.mainTimerMsec, self.timerCallback, 0)
        glutTimerFunc(CommonConstants.renderTimerMsec, self.renderCallback, 0)
        glutMainLoop()

    def timerCallback(self, value):
        self.game.updateCurrentScreen()
        self.game.voxCurrentScreen()
        glutTimerFunc(CommonConstants.mainTimerMsec, self.timerCallback, 0)

    def renderCallback(self, value):
        glutPostRedisplay()
        glutTimerFunc(CommonConstants.renderTimerMsec, self.renderCallback, 0)

    def keyup(self, key, a, b):
        if key == Keys.esc:
            glutLeaveMainLoop()
        elif key == Keys.backspace:
            self.toggleFullscreen()

    def toggleFullscreen(self):
        self.isFullscreen = not self.isFullscreen
        if self.isFullscreen:
            glutFullScreen()
        else:
            glutReshapeWindow(self.windowWidth, self.windowHeight)
            x, y = self.getCenterWindowPosition()
            glutPositionWindow(x, y)

    def getCenterWindowPosition(self):
        screenWidth, screenHeight = Screen.getWidthAndHeight()
        x = int((screenWidth - self.windowWidth) / 2)
        y = int((screenHeight - self.windowHeight) / 2)

        return (x, y)


print("\r\nProgram start")
# CpuProfiler.init()
app = App()
app.run()
# CpuProfiler.makeResult()
