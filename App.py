import os
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from game.lib.Environment import Environment
from game.core.GameFactory import GameFactory


class App:

    def __init__(self):
        Environment.programRootPath = os.path.dirname(__file__)

    def resize(self, width, height):
        glViewport(0, 0, width, height)

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        glMatrixMode(GL_PROJECTION)
        gluOrtho2D(0.0, 100.0, 0.0, 100.0)
        glColor3f(1, 0, 0)
        glBegin(GL_QUADS)
        glVertex3f(0, 0, 0)
        glVertex3f(50, 0, 0)
        glVertex3f(50, 50, 0)
        glVertex3f(0, 50, 0)
        glEnd()
        glutSwapBuffers()

    def run(self):
        glutInit(sys.argv)
        glutInitWindowSize(300, 300)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
        glutCreateWindow(b"Wrath")
        glutInitWindowPosition(50, 50)
        glutDisplayFunc(self.render)
        glutReshapeFunc(self.resize)
        gameFactory = GameFactory()
        self.game = gameFactory.makeGame()
        glutMainLoop()


app = App()
app.run()
