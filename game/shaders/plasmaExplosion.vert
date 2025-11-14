#version 460 core

layout (location = 0) in vec3 in_Position;
layout (location = 1) in vec3 in_Velocity;
layout (location = 2) in float in_Age;

// for feedback buffer
out vec3 UpdatedPosition;
out vec3 UpdatedVelocity;
out float UpdatedAge;

out vec4 ParticleColor;

uniform int passNumber;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;
uniform float particleLifeTime;
uniform float particleSize;
uniform float deltaTime;

const float cos45 = 0.70710678118;
// circle
const vec3 vertices[] = vec3[]
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
    UpdatedPosition = in_Position;
    UpdatedVelocity = in_Velocity;
    UpdatedAge = in_Age + deltaTime;
    if (0 <= in_Age && in_Age < particleLifeTime)
    {
        UpdatedPosition += in_Velocity;
    }
}

void render()
{
    if (0 <= in_Age && in_Age < particleLifeTime)
    {
        float ageFraction = clamp(in_Age / particleLifeTime, 0.0, 1.0);
        vec3 gradientColor = mix(vec3(0.03, 0.19, 0.46), vec3(0.33, 0.93, 0.96), ageFraction);
        ParticleColor = vec4(gradientColor, 1.0 - ageFraction);
        vec3 viewPosition = (viewMatrix * vec4(in_Position, 1.0)).xyz + vertices[gl_VertexID] * particleSize;
        gl_Position = projectionMatrix * vec4(viewPosition, 1.0);
    }
    else
    {
        ParticleColor = vec4(0.0);
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
