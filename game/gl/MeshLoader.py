import impasse
from impasse.constants import ProcessingStep

from game.calc.Point2 import Point2
from game.calc.Vector3 import Vector3
from game.gl.Mesh import Face, Mesh
from game.gl.Texture import Texture


class MeshLoader:

    def load(self, objFilePath):
        resultMesh = Mesh()

        totalVerticesCount = 0
        scene = impasse.load(objFilePath, processing=ProcessingStep.Triangulate)

        for mesh in scene.meshes:
            for vertex in mesh.vertices:
                resultMesh.addVertex(Vector3(vertex[0], vertex[1], vertex[2]))

            for normal in mesh.normals:
                resultMesh.addNormal(Vector3(normal[0], normal[1], normal[2]))

            for tc in mesh.texture_coords[0]:
                resultMesh.addTexCoord(Point2(tc[0], tc[1]))

            for face in mesh.faces:
                if len(face) == 3:
                    resultMesh.addFace(Face(totalVerticesCount + face[0], totalVerticesCount + face[1], totalVerticesCount + face[2]))

            totalVerticesCount = len(resultMesh.vertices)

        resultMesh.mainTexture = Texture(1, 10, 10)

        return resultMesh


def makeMeshLoader(resolver):
    return MeshLoader()
