#version 460 core

layout (triangles_adjacency) in;
layout (triangle_strip, max_vertices = 18) out;
in vec3 PositionView[];

uniform mat4 projectionMatrix;
const int maxLightsCount = 25;
uniform int lightsCount;
uniform vec3 lightPosition[maxLightsCount];

bool facesLight(vec3 light, vec3 a, vec3 b, vec3 c)
{
    vec3 n = cross(b - a, c - a);
    vec3 da = light - a;
    vec3 db = light - b;
    vec3 dc = light - c;

    return dot(n, da) > 0.0 || dot(n, db) > 0.0 || dot(n, dc) > 0.0; 
}

void emitEdgeQuad(vec3 light, vec3 a, vec3 b)
{
    gl_Position = projectionMatrix * vec4(a, 1.0);
    EmitVertex();

    gl_Position = projectionMatrix * vec4(a - light, 0.0);
    EmitVertex();

    gl_Position = projectionMatrix * vec4(b, 1.0);
    EmitVertex();

    gl_Position = projectionMatrix * vec4(b - light, 0.0);
    EmitVertex();

    EndPrimitive();
}

void main()
{
    // If the main triangle faces the light, check each adjacent triangle.
    // If an adjacent triangle does not face the light - output a sihlouette edge quad for the corresponding edge.
    for (int lightIndex = 0; lightIndex < lightsCount; lightIndex++)
    {
        if (facesLight(lightPosition[lightIndex], PositionView[0], PositionView[2], PositionView[4]))
        {
            if (!facesLight(lightPosition[lightIndex], PositionView[0], PositionView[1], PositionView[2]))
            {
                emitEdgeQuad(lightPosition[lightIndex], PositionView[0], PositionView[2]);
            }

            if (!facesLight(lightPosition[lightIndex], PositionView[2], PositionView[3], PositionView[4]))
            {
                emitEdgeQuad(lightPosition[lightIndex], PositionView[2], PositionView[4]);
            }

            if (!facesLight(lightPosition[lightIndex], PositionView[4], PositionView[5], PositionView[0]))
            {
                emitEdgeQuad(lightPosition[lightIndex], PositionView[4], PositionView[0]);
            }
        }
    }
}
