from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from game.anx.CommonConstants import CommonConstants
from game.engine.GameData import GameData


class DebugRenderer:

    def __init__(self, gameData):
        self.gameData = gameData

    def render(self):
        self.initCamera()
        # self.renderFloorGrid()
        self.renderVisibleWalls()
        self.renderVisibleFloors()
        self.renderVisibleCeilings()
        # self.renderVisibleSegmentJoinLines()
        # self.renderPlayerSegmentWalls()
        # self.renderPlayerSegmentWallLimitLines()
        # self.renderPlayerSegmentFloors()
        # self.renderPlayerSegmentCeilings()
        # self.renderPlayerBorder()
        # self.renderAxis()

    def initCamera(self):
        camera = self.gameData.camera
        glLoadIdentity()
        glMatrixMode(GL_PROJECTION)
        gluPerspective(camera.viewAngleDegrees, CommonConstants.screenAspect, CommonConstants.minDepth, CommonConstants.maxDepth)
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

    def renderVisibleWalls(self):
        glEnable(GL_BLEND)
        glEnable(GL_DEPTH_TEST)
        for levelSegment in self.gameData.visibleLevelSegments:
            for wall in levelSegment.walls:
                startPointUp = wall.startPoint.copy()
                endPointUp = wall.endPoint.copy()
                startPointUp.z += wall.height
                endPointUp.z += wall.height
                glColor3f(0.5, 0.5, 0.5)
                # glColor4f(1, 1, 1, 0.3)
                self.renderGridQuad(wall.startPoint, wall.endPoint, startPointUp, endPointUp)
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_BLEND)

    def renderVisibleFloors(self):
        glEnable(GL_BLEND)
        glEnable(GL_DEPTH_TEST)
        for levelSegment in self.gameData.visibleLevelSegments:
            for floor in levelSegment.floors:
                glColor3f(0.4, 0.4, 0.4)
                # glColor4f(1, 1, 1, 0.1)
                self.renderGridQuad(floor.downLeft, floor.downRight, floor.upLeft, floor.upRight)
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_BLEND)

    def renderVisibleCeilings(self):
        glEnable(GL_DEPTH_TEST)
        for levelSegment in self.gameData.visibleLevelSegments:
            for ceiling in levelSegment.ceilings:
                glColor3f(0.4, 0.4, 0.4)
                self.renderGridQuad(ceiling.downLeft, ceiling.downRight, ceiling.upLeft, ceiling.upRight)
        glDisable(GL_DEPTH_TEST)

    def renderVisibleSegmentJoinLines(self):
        glEnable(GL_DEPTH_TEST)
        glColor3f(1, 0, 1)
        for levelSegment in self.gameData.visibleLevelSegments:
            for joinLine in levelSegment.joinLines:
                glBegin(GL_LINES)
                glVertex3f(joinLine.startPoint.x, joinLine.startPoint.y, joinLine.startPoint.z + 0.01)
                glVertex3f(joinLine.endPoint.x, joinLine.endPoint.y, joinLine.endPoint.z + 0.01)
                glEnd()
        glDisable(GL_DEPTH_TEST)

    def renderPlayerSegmentWalls(self):
        glEnable(GL_BLEND)
        glColor4f(1, 0, 0, 0.2)
        for levelSegment in self.gameData.player.collisionLevelSegments:
            for wall in levelSegment.walls:
                glBegin(GL_QUADS)
                glVertex3f(wall.startPoint.x, wall.startPoint.y, wall.startPoint.z)
                glVertex3f(wall.endPoint.x, wall.endPoint.y, wall.endPoint.z)
                glVertex3f(wall.endPoint.x, wall.endPoint.y, wall.endPoint.z + wall.height)
                glVertex3f(wall.startPoint.x, wall.startPoint.y, wall.startPoint.z + wall.height)
                glEnd()
        glDisable(GL_BLEND)

    def renderPlayerSegmentWallLimitLines(self):
        glEnable(GL_DEPTH_TEST)
        glColor3f(1, 1, 0)
        for levelSegment in self.gameData.player.collisionLevelSegments:
            for wall in levelSegment.walls:
                glBegin(GL_LINES)
                glVertex3f(wall.limitLine.startPoint.x, wall.limitLine.startPoint.y, wall.startPoint.z)
                glVertex3f(wall.limitLine.endPoint.x, wall.limitLine.endPoint.y, wall.endPoint.z)
                glEnd()
        glDisable(GL_DEPTH_TEST)

    def renderPlayerSegmentFloors(self):
        glEnable(GL_BLEND)
        glEnable(GL_DEPTH_TEST)
        glColor4f(1, 0, 0, 0.2)
        for levelSegment in self.gameData.player.collisionLevelSegments:
            for floor in levelSegment.floors:
                glBegin(GL_QUADS)
                glVertex3f(floor.downLeft.x, floor.downLeft.y, floor.downLeft.z + 0.01)
                glVertex3f(floor.downRight.x, floor.downRight.y, floor.downRight.z + 0.01)
                glVertex3f(floor.upRight.x, floor.upRight.y, floor.upRight.z + 0.01)
                glVertex3f(floor.upLeft.x, floor.upLeft.y, floor.upLeft.z + 0.01)
                glEnd()
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_BLEND)

    def renderPlayerSegmentCeilings(self):
        glEnable(GL_BLEND)
        glEnable(GL_DEPTH_TEST)
        glColor4f(1, 0, 0, 0.2)
        for levelSegment in self.gameData.player.collisionLevelSegments:
            for ceiling in levelSegment.ceilings:
                glBegin(GL_QUADS)
                glVertex3f(ceiling.downLeft.x, ceiling.downLeft.y, ceiling.downLeft.z - 0.01)
                glVertex3f(ceiling.downRight.x, ceiling.downRight.y, ceiling.downRight.z - 0.01)
                glVertex3f(ceiling.upRight.x, ceiling.upRight.y, ceiling.upRight.z - 0.01)
                glVertex3f(ceiling.upLeft.x, ceiling.upLeft.y, ceiling.upLeft.z - 0.01)
                glEnd()
        glDisable(GL_DEPTH_TEST)
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
        glBegin(GL_QUADS)
        glVertex3f(downLeft.x, downLeft.y, downLeft.z)
        glVertex3f(downRight.x, downRight.y, downRight.z)
        glVertex3f(upRight.x, upRight.y, upRight.z)
        glVertex3f(upLeft.x, upLeft.y, upLeft.z)
        glEnd()

        glColor3f(0.1, 0.1, 0.1)

        glBegin(GL_LINES)
        glVertex3f(downLeft.x, downLeft.y, downLeft.z)
        glVertex3f(upLeft.x, upLeft.y, upLeft.z)
        glEnd()

        glBegin(GL_LINES)
        glVertex3f(downRight.x, downRight.y, downRight.z)
        glVertex3f(upRight.x, upRight.y, upRight.z)
        glEnd()

        glBegin(GL_LINES)
        glVertex3f(downLeft.x, downLeft.y, downLeft.z)
        glVertex3f(downRight.x, downRight.y, downRight.z)
        glEnd()

        glBegin(GL_LINES)
        glVertex3f(upLeft.x, upLeft.y, upLeft.z)
        glVertex3f(upRight.x, upRight.y, upRight.z)
        glEnd()

        glBegin(GL_LINES)
        glVertex3f(downLeft.x, downLeft.y, downLeft.z)
        glVertex3f(upRight.x, upRight.y, upRight.z)
        glEnd()

        glBegin(GL_LINES)
        glVertex3f(downRight.x, downRight.y, downRight.z)
        glVertex3f(upLeft.x, upLeft.y, upLeft.z)
        glEnd()


def makeDebugRenderer(resolver):
    return DebugRenderer(resolver.resolve(GameData))
