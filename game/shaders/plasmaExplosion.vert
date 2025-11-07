#version 460 core

layout (location = 0) in vec3 in_VertexPosition;
layout (location = 1) in vec3 in_VertexVelocity;
layout (location = 2) in float in_VertexAge;

// for feedback buffer
out vec3 Position;
out vec3 Velocity;
out float Age;

// for fragment shader
out vec3 ParticleColor;
out float TransparentValue;

uniform int passNumber;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;
uniform float particleLifeTime;
uniform float particleSize;
uniform float deltaTime;

const float cos45 = 0.70710678118;
// circle
const vec3 offsets[] = vec3[]
(
    vec3(0.0, 0.0, 0.0), vec3(   0.0,    1.0, 0.0), vec3(-cos45,  cos45, 0.0),
    vec3(0.0, 0.0, 0.0), vec3(-cos45,  cos45, 0.0), vec3(  -1.0,    0.0, 0.0),
    vec3(0.0, 0.0, 0.0), vec3(  -1.0,    0.0, 0.0), vec3(-cos45, -cos45, 0.0),
    vec3(0.0, 0.0, 0.0), vec3(-cos45, -cos45, 0.0), vec3(   0.0,   -1.0, 0.0),
    vec3(0.0, 0.0, 0.0), vec3(   0.0,   -1.0, 0.0), vec3( cos45, -cos45, 0.0),
    vec3(0.0, 0.0, 0.0), vec3( cos45, -cos45, 0.0), vec3(   1.0,    0.0, 0.0),
    vec3(0.0, 0.0, 0.0), vec3(   1.0,    0.0, 0.0), vec3( cos45,  cos45, 0.0),
    vec3(0.0, 0.0, 0.0), vec3( cos45,  cos45, 0.0), vec3(   0.0,    1.0, 0.0)
);

void update()
{
    Position = in_VertexPosition;
    Velocity = in_VertexVelocity;
    Age = in_VertexAge + deltaTime;
    if (0 <= in_VertexAge && in_VertexAge < particleLifeTime)
    {
        Position += in_VertexVelocity;
    }
}

void render()
{
    if (0 <= in_VertexAge && in_VertexAge < particleLifeTime)
    {
        float da = clamp(in_VertexAge / particleLifeTime, 0.0, 1.0);
        ParticleColor = mix(vec3(0.03, 0.19, 0.46), vec3(0.33, 0.93, 0.96), da);
        TransparentValue = 1.0 - da;
        vec3 viewPosition = (viewMatrix * vec4(in_VertexPosition, 1.0)).xyz + offsets[gl_VertexID] * particleSize;
        gl_Position = projectionMatrix * vec4(viewPosition, 1.0);
    }
    else
    {
        TransparentValue = 0.0;
        gl_Position = vec4(0.0);
    }
}

void main()
{
    if (passNumber == 1)
    {
        update();
    }
    else
    {
        render();
    }
}
