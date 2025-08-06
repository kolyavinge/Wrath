# считает пары значений (косинус, синус) для алгоритма размытия тени в шейдере mainSceneCompose.frag

import math

resolutionX = 1920
resolutionY = 1080

radius = 4.0
radiusX = radius / resolutionX
radiusY = radius / resolutionY

step = 2.0 * math.pi / 32.0

offsets = []
offsetsX = []
offsetsY = []

radians = 0
while radians <= 2.0 * math.pi:
    x = radiusX * math.cos(radians)
    y = radiusY * math.sin(radians)
    offsetsX.append(x)
    offsetsY.append(y)
    offsets.append((x, y))
    radians += step

for offset in offsets:
    x, y = offset
    print(f"vec2({x}, {y}),")
