from game.calc.Matrix3 import Matrix3
from game.calc.Vector3 import Vector3
from game.lib.Math import Math

# https://registry.khronos.org/OpenGL-Refpages/gl2.1/xhtml/glTranslate.xml
# https://registry.khronos.org/OpenGL-Refpages/gl2.1/xhtml/glRotate.xml
# https://registry.khronos.org/OpenGL-Refpages/gl2.1/xhtml/glScale.xml
# https://learnopengl.com/Getting-started/Transformations
# https://registry.khronos.org/OpenGL-Refpages/gl2.1/xhtml/gluLookAt.xml
# https://graphicscompendium.com/opengl/18-lookat-matrix
# https://registry.khronos.org/OpenGL-Refpages/gl2.1/xhtml/glOrtho.xml
# https://registry.khronos.org/OpenGL-Refpages/gl2.1/xhtml/gluPerspective.xml


class TransformMatrix4:

    def setIdentity(self):
        self.items = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]

    def setZero(self):
        self.items = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def get(self, row, col):
        return self.items[4 * col + row]

    def mul(self, m):
        self.items = [
            # col 1
            self.items[0] * m.items[0] + self.items[4] * m.items[1] + self.items[8] * m.items[2] + self.items[12] * m.items[3],
            self.items[1] * m.items[0] + self.items[5] * m.items[1] + self.items[9] * m.items[2] + self.items[13] * m.items[3],
            self.items[2] * m.items[0] + self.items[6] * m.items[1] + self.items[10] * m.items[2] + self.items[14] * m.items[3],
            self.items[3] * m.items[0] + self.items[7] * m.items[1] + self.items[11] * m.items[2] + self.items[15] * m.items[3],
            # col 2
            self.items[0] * m.items[4] + self.items[4] * m.items[5] + self.items[8] * m.items[6] + self.items[12] * m.items[7],
            self.items[1] * m.items[4] + self.items[5] * m.items[5] + self.items[9] * m.items[6] + self.items[13] * m.items[7],
            self.items[2] * m.items[4] + self.items[6] * m.items[5] + self.items[10] * m.items[6] + self.items[14] * m.items[7],
            self.items[3] * m.items[4] + self.items[7] * m.items[5] + self.items[11] * m.items[6] + self.items[15] * m.items[7],
            # col 3
            self.items[0] * m.items[8] + self.items[4] * m.items[9] + self.items[8] * m.items[10] + self.items[12] * m.items[11],
            self.items[1] * m.items[8] + self.items[5] * m.items[9] + self.items[9] * m.items[10] + self.items[13] * m.items[11],
            self.items[2] * m.items[8] + self.items[6] * m.items[9] + self.items[10] * m.items[10] + self.items[14] * m.items[11],
            self.items[3] * m.items[8] + self.items[7] * m.items[9] + self.items[11] * m.items[10] + self.items[15] * m.items[11],
            # col 4
            self.items[0] * m.items[12] + self.items[4] * m.items[13] + self.items[8] * m.items[14] + self.items[12] * m.items[15],
            self.items[1] * m.items[12] + self.items[5] * m.items[13] + self.items[9] * m.items[14] + self.items[13] * m.items[15],
            self.items[2] * m.items[12] + self.items[6] * m.items[13] + self.items[10] * m.items[14] + self.items[14] * m.items[15],
            self.items[3] * m.items[12] + self.items[7] * m.items[13] + self.items[11] * m.items[14] + self.items[15] * m.items[15],
        ]

    def mulVector3(self, v):
        # четвертый компонент вектора равен 1
        x = self.items[0] * v.x + self.items[4] * v.y + self.items[8] * v.z + self.items[12]
        y = self.items[1] * v.x + self.items[5] * v.y + self.items[9] * v.z + self.items[13]
        z = self.items[2] * v.x + self.items[6] * v.y + self.items[10] * v.z + self.items[14]

        return Vector3(x, y, z)

    def translate(self, x, y, z):
        self.items = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, x, y, z, 1]

    def rotate(self, radians, axis):
        sin = Math.sin(radians)
        cos = Math.cos(radians)
        oneMinusCos = 1 - cos
        self.items = [
            # col 1
            cos + axis.x * axis.x * oneMinusCos,
            axis.y * axis.x * oneMinusCos + axis.z * sin,
            axis.z * axis.x * oneMinusCos - axis.y * sin,
            0,
            # col 2
            axis.x * axis.y * oneMinusCos - axis.z * sin,
            cos + axis.y * axis.y * oneMinusCos,
            axis.z * axis.y * oneMinusCos + axis.x * sin,
            0,
            # col 3
            axis.x * axis.z * oneMinusCos + axis.y * sin,
            axis.y * axis.z * oneMinusCos - axis.x * sin,
            cos + axis.z * axis.z * oneMinusCos,
            0,
            # col 4
            0,
            0,
            0,
            1,
        ]

    def translateAndRotate(self, x, y, z, radians, axis):
        sin = Math.sin(radians)
        cos = Math.cos(radians)
        oneMinusCos = 1 - cos
        self.items = [
            # col 1
            cos + axis.x * axis.x * oneMinusCos,
            axis.y * axis.x * oneMinusCos + axis.z * sin,
            axis.z * axis.x * oneMinusCos - axis.y * sin,
            0,
            # col 2
            axis.x * axis.y * oneMinusCos - axis.z * sin,
            cos + axis.y * axis.y * oneMinusCos,
            axis.z * axis.y * oneMinusCos + axis.x * sin,
            0,
            # col 3
            axis.x * axis.z * oneMinusCos + axis.y * sin,
            axis.y * axis.z * oneMinusCos - axis.x * sin,
            cos + axis.z * axis.z * oneMinusCos,
            0,
            # col 4
            x,
            y,
            z,
            1,
        ]

    def scale(self, x, y, z):
        self.items = [x, 0, 0, 0, 0, y, 0, 0, 0, 0, z, 0, 0, 0, 0, 1]

    def lookAt(self, eyePosition, lookDirection, upDirection):
        s = lookDirection.copy()
        s.vectorProduct(upDirection)
        s.normalize()
        u = s.copy()
        u.vectorProduct(lookDirection)
        self.items = [
            # col 1
            s.x,
            u.x,
            -lookDirection.x,
            0,
            # col 2
            s.y,
            u.y,
            -lookDirection.y,
            0,
            # col 3
            s.z,
            u.z,
            -lookDirection.z,
            0,
            # col 4
            -eyePosition.dotProduct(s),
            -eyePosition.dotProduct(u),
            eyePosition.dotProduct(lookDirection),
            1,
        ]

    def ortho(self, left, right, bottom, top, zNear, zFar):
        self.items = [
            # col 1
            2 / (right - left),
            0,
            0,
            0,
            # col 2
            0,
            2 / (top - bottom),
            0,
            0,
            # col 3
            0,
            0,
            -2 / (zFar - zNear),
            0,
            # col 4
            -(right + left) / (right - left),
            -(top + bottom) / (top - bottom),
            -(zFar + zNear) / (zFar - zNear),
            1,
        ]

    def perspective(self, viewAngleRadians, screenAspect, zNear, zFar):
        f = Math.cotan(viewAngleRadians / 2)
        self.items = [
            # col 1
            f / screenAspect,
            0,
            0,
            0,
            # col 2
            0,
            f,
            0,
            0,
            # col 3
            0,
            0,
            (zFar + zNear) / (zNear - zFar),
            -1,
            # col 4
            0,
            0,
            (2 * zFar * zNear) / (zNear - zFar),
            0,
        ]

    def inverse(self):
        m = self.items
        inv = [
            m[5] * m[10] * m[15] - m[5] * m[11] * m[14] - m[9] * m[6] * m[15] + m[9] * m[7] * m[14] + m[13] * m[6] * m[11] - m[13] * m[7] * m[10],
            -m[1] * m[10] * m[15] + m[1] * m[11] * m[14] + m[9] * m[2] * m[15] - m[9] * m[3] * m[14] - m[13] * m[2] * m[11] + m[13] * m[3] * m[10],
            m[1] * m[6] * m[15] - m[1] * m[7] * m[14] - m[5] * m[2] * m[15] + m[5] * m[3] * m[14] + m[13] * m[2] * m[7] - m[13] * m[3] * m[6],
            -m[1] * m[6] * m[11] + m[1] * m[7] * m[10] + m[5] * m[2] * m[11] - m[5] * m[3] * m[10] - m[9] * m[2] * m[7] + m[9] * m[3] * m[6],
            -m[4] * m[10] * m[15] + m[4] * m[11] * m[14] + m[8] * m[6] * m[15] - m[8] * m[7] * m[14] - m[12] * m[6] * m[11] + m[12] * m[7] * m[10],
            m[0] * m[10] * m[15] - m[0] * m[11] * m[14] - m[8] * m[2] * m[15] + m[8] * m[3] * m[14] + m[12] * m[2] * m[11] - m[12] * m[3] * m[10],
            -m[0] * m[6] * m[15] + m[0] * m[7] * m[14] + m[4] * m[2] * m[15] - m[4] * m[3] * m[14] - m[12] * m[2] * m[7] + m[12] * m[3] * m[6],
            m[0] * m[6] * m[11] - m[0] * m[7] * m[10] - m[4] * m[2] * m[11] + m[4] * m[3] * m[10] + m[8] * m[2] * m[7] - m[8] * m[3] * m[6],
            m[4] * m[9] * m[15] - m[4] * m[11] * m[13] - m[8] * m[5] * m[15] + m[8] * m[7] * m[13] + m[12] * m[5] * m[11] - m[12] * m[7] * m[9],
            -m[0] * m[9] * m[15] + m[0] * m[11] * m[13] + m[8] * m[1] * m[15] - m[8] * m[3] * m[13] - m[12] * m[1] * m[11] + m[12] * m[3] * m[9],
            m[0] * m[5] * m[15] - m[0] * m[7] * m[13] - m[4] * m[1] * m[15] + m[4] * m[3] * m[13] + m[12] * m[1] * m[7] - m[12] * m[3] * m[5],
            -m[0] * m[5] * m[11] + m[0] * m[7] * m[9] + m[4] * m[1] * m[11] - m[4] * m[3] * m[9] - m[8] * m[1] * m[7] + m[8] * m[3] * m[5],
            -m[4] * m[9] * m[14] + m[4] * m[10] * m[13] + m[8] * m[5] * m[14] - m[8] * m[6] * m[13] - m[12] * m[5] * m[10] + m[12] * m[6] * m[9],
            m[0] * m[9] * m[14] - m[0] * m[10] * m[13] - m[8] * m[1] * m[14] + m[8] * m[2] * m[13] + m[12] * m[1] * m[10] - m[12] * m[2] * m[9],
            -m[0] * m[5] * m[14] + m[0] * m[6] * m[13] + m[4] * m[1] * m[14] - m[4] * m[2] * m[13] - m[12] * m[1] * m[6] + m[12] * m[2] * m[5],
            m[0] * m[5] * m[10] - m[0] * m[6] * m[9] - m[4] * m[1] * m[10] + m[4] * m[2] * m[9] + m[8] * m[1] * m[6] - m[8] * m[2] * m[5],
        ]

        det = m[0] * inv[0] + m[1] * inv[4] + m[2] * inv[8] + m[3] * inv[12]
        if det == 0:
            raise Exception("The matrix cannot be inverted.")
        det = 1.0 / det

        i = 0
        while i < 16:
            inv[i] *= det
            i += 1

        self.items = inv

    def copy(self):
        result = TransformMatrix4()
        result.items = self.items.copy()

        return result

    def toMatrix3(self):
        return Matrix3(
            [
                # col1
                self.items[0],
                self.items[1],
                self.items[2],
                # col2
                self.items[4],
                self.items[5],
                self.items[6],
                # col3
                self.items[8],
                self.items[9],
                self.items[10],
            ]
        )

    def __str__(self):
        result = ""
        row = 0
        while row < 4:
            col = 0
            while col < 4:
                value = self.get(row, col)
                result += f"{value:f}" + "\t"
                col += 1
            row += 1
            result += "\r\n"

        return result.strip()

    def fromRowMajorFormat(aiMatrix):
        result = TransformMatrix4()
        result.items = [
            # col 1
            aiMatrix[0][0],
            aiMatrix[1][0],
            aiMatrix[2][0],
            aiMatrix[3][0],
            # col 2
            aiMatrix[0][1],
            aiMatrix[1][1],
            aiMatrix[2][1],
            aiMatrix[3][1],
            # col 3
            aiMatrix[0][2],
            aiMatrix[1][2],
            aiMatrix[2][2],
            aiMatrix[3][2],
            # col 4
            aiMatrix[0][3],
            aiMatrix[1][3],
            aiMatrix[2][3],
            aiMatrix[3][3],
        ]

        return result


TransformMatrix4.identity = TransformMatrix4()
TransformMatrix4.identity.setIdentity()
