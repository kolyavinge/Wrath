#version 460 core

layout (triangles_adjacency) in;
layout (triangle_strip, max_vertices = 28) out;

const float epsilon = 0.1;

in vec3 PositionView[];

uniform mat4 projectionMatrix;
const int maxLightsCount = 25;
uniform int lightsCount;
uniform vec3 lightPositionsView[maxLightsCount];

bool facesLight(vec3 lightPositionView, vec3 a, vec3 b, vec3 c)
{
    vec3 n = cross(b - a, c - a);
    vec3 da = lightPositionView - a;
    vec3 db = lightPositionView - b;
    vec3 dc = lightPositionView - c;

    return dot(n, da) > 0.0 || dot(n, db) > 0.0 || dot(n, dc) > 0.0;
}

void emitEdgeQuad(vec3 lightPositionView, vec3 a, vec3 b)
{
    vec3 lightDirection = normalize(a - lightPositionView);
    vec3 deviation = lightDirection * epsilon;
    gl_Position = projectionMatrix * vec4(a + deviation, 1.0);
    EmitVertex();

    gl_Position = projectionMatrix * vec4(lightDirection, 0.0);
    EmitVertex();

    lightDirection = normalize(b - lightPositionView);
    deviation = lightDirection * epsilon;
    gl_Position = projectionMatrix * vec4(b + deviation, 1.0);
    EmitVertex();

    gl_Position = projectionMatrix * vec4(lightDirection, 0.0);
    EmitVertex();
    EndPrimitive();
}

void processLight(int lightIndex)
{
    vec3 lightPositionView = lightPositionsView[lightIndex];

    if (facesLight(lightPositionView, PositionView[0], PositionView[2], PositionView[4]))
    {
        if (!facesLight(lightPositionView, PositionView[0], PositionView[1], PositionView[2]))
        {
            emitEdgeQuad(lightPositionView, PositionView[0], PositionView[2]);
        }

        if (!facesLight(lightPositionView, PositionView[2], PositionView[3], PositionView[4]))
        {
            emitEdgeQuad(lightPositionView, PositionView[2], PositionView[4]);
        }

        if (!facesLight(lightPositionView, PositionView[4], PositionView[5], PositionView[0]))
        {
            emitEdgeQuad(lightPositionView, PositionView[4], PositionView[0]);
        }

        // front cap
        vec3 lightDirection = normalize(PositionView[0] - lightPositionView);
        vec3 deviation = lightDirection * epsilon;
        gl_Position = projectionMatrix * vec4(PositionView[0] + deviation, 1.0);
        EmitVertex();

        lightDirection = normalize(PositionView[2] - lightPositionView);
        deviation = lightDirection * epsilon;
        gl_Position = projectionMatrix * vec4(PositionView[2] + deviation, 1.0);
        EmitVertex();

        lightDirection = normalize(PositionView[4] - lightPositionView);
        deviation = lightDirection * epsilon;
        gl_Position = projectionMatrix * vec4(PositionView[4] + deviation, 1.0);
        EmitVertex();
        EndPrimitive();

        // back cap
        lightDirection = normalize(PositionView[0] - lightPositionView);
        gl_Position = projectionMatrix * vec4(lightDirection, 0.0);
        EmitVertex();

        lightDirection = normalize(PositionView[4] - lightPositionView);
        gl_Position = projectionMatrix * vec4(lightDirection, 0.0);
        EmitVertex();

        lightDirection = normalize(PositionView[2] - lightPositionView);
        gl_Position = projectionMatrix * vec4(lightDirection, 0.0);
        EmitVertex();
        EndPrimitive();
    }
}

void main()
{
    for (int lightIndex = 0; lightIndex < lightsCount; lightIndex++)
    {
        processLight(lightIndex);
    }
}
