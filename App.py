import os
import sys

from OpenGL.GL import *
from OpenGL.GLUT import *

from game.anx.CommonConstants import CommonConstants
from game.anx.Events import Events
from game.core.GameFactory import GameFactory
from game.input.Keys import Keys
from game.lib.Environment import Environment
from game.lib.Screen import Screen
from game.tools.CpuProfiler import CpuProfiler


class App:

    def __init__(self):
        Environment.programRootPath = os.getcwd()
        self.isFullscreen = False
        self.windowWidth = 1200
        self.windowHeight = (int)(self.windowWidth / CommonConstants.screenAspect)

    def resize(self, width, height):
        glViewport(0, 0, width, height)
        self.game.eventManager.raiseEvent(Events.viewportSizeChanged, (width, height))

    def render(self):
        self.game.renderCurrentScreen()
        glutSwapBuffers()

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
        glutTimerFunc(CommonConstants.mainTimerMsec, self.timerCallback, 0)
        glutMainLoop()

    def timerCallback(self, value):
        self.game.updateCurrentScreen()
        self.game.voxCurrentScreen()
        glutPostRedisplay()
        glutTimerFunc(CommonConstants.mainTimerMsec, self.timerCallback, 0)

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
