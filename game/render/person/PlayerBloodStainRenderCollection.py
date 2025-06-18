from game.render.person.PlayerBloodStainRenderMeshFactory import *


class PlayerBloodStainRenderCollection:

    def __init__(self, renderMeshFactory: PlayerBloodStainRenderMeshFactory):
        self.renderMeshFactory = renderMeshFactory

    def init(self):
        self.meshes = []
        self.meshes.append(self.renderMeshFactory.make())

    def getRenderMesh(self, bloodStainNumber):
        return self.meshes[bloodStainNumber]
