import os
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from game.lib.Environment import Environment
from game.lib.Screen import Screen
from game.anx.Constants import Constants
from game.core.GameFactory import GameFactory


class App:

    def __init__(self):
        Environment.programRootPath = os.path.dirname(__file__)

    def resize(self, width, height):
        glViewport(0, 0, width, height)

    def render(self):
        player = self.game.levelManager.gameData.player
        camera = self.game.levelManager.gameData.camera

        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        glMatrixMode(GL_PROJECTION)
        gluPerspective(60, 16 / 9, 0.1, 1000)
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
