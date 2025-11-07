from OpenGL.GL import *

from game.gl.Shader import ShaderConstants


class FeedbackParticleRenderer:

    def update(self, particleBuffer, shader):
        shader.setPassNumber(ShaderConstants.updatePass)
        glEnable(GL_RASTERIZER_DISCARD)
        glBindTransformFeedback(GL_TRANSFORM_FEEDBACK, particleBuffer.destinationFeedbackId)
        glBeginTransformFeedback(GL_POINTS)
        glBindVertexArray(particleBuffer.sourceBufferId)
        glVertexAttribDivisor(0, 0)
        glVertexAttribDivisor(1, 0)
        glVertexAttribDivisor(2, 0)
        glDrawArrays(GL_POINTS, 0, particleBuffer.particlesCount)
        glBindVertexArray(0)
        glEndTransformFeedback()
        glDisable(GL_RASTERIZER_DISCARD)

    def render(self, particleBuffer, shader, elementsCount):
        shader.setPassNumber(ShaderConstants.renderPass)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_ALPHA_TEST)
        glEnable(GL_DEPTH_TEST)
        glBindVertexArray(particleBuffer.destinationBufferId)
        glVertexAttribDivisor(0, 1)
        glVertexAttribDivisor(1, 1)
        glVertexAttribDivisor(2, 1)
        glDrawArraysInstanced(GL_TRIANGLES, 0, elementsCount, particleBuffer.particlesCount)
        glBindVertexArray(0)
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_ALPHA_TEST)
        glDisable(GL_BLEND)
