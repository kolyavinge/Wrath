from OpenGL.GL import *


class ParticleRenderer:

    def render(self, particleBuffer, elementsCount):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_ALPHA_TEST)
        glEnable(GL_DEPTH_TEST)
        glBindVertexArray(particleBuffer.vaid)
        particleBuffer.setVertexAttribDivisor(1)
        glDrawArraysInstanced(GL_TRIANGLES, 0, elementsCount, particleBuffer.particlesCount)
        glBindVertexArray(0)
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)
