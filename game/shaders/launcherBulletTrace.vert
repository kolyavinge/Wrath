#version 460 core

layout (location = 0) in vec3 in_Position;
layout (location = 1) in vec3 in_Velocity;
layout (location = 2) in float in_Age;
layout (location = 6) in vec4 in_Random;

// for feedback buffer
out vec3 UpdatedPosition;
out vec3 UpdatedVelocity;
out float UpdatedAge;

out vec4 ParticleColor;

uniform int passNumber;
uniform vec3 tracePosition;
uniform vec3 bulletDirection;
uniform vec3 bulletDirectionTopNormal;
uniform float bulletNozzleRadius;
uniform bool isBulletAlive;
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

// common.glsl
vec3 rotatePoint(vec3 point, vec3 pivotAxis, float radian);

vec3 getInitPosition()
{
    vec3 initPoint = in_Random.x * bulletNozzleRadius * bulletDirectionTopNormal;
    return tracePosition + rotatePoint(initPoint, bulletDirection, in_Random.z) - in_Random.y * bulletDirection;
}

void update()
{
    // particle is alive - move it, whether bullet is alive or not
    if (0 <= in_Age && in_Age < particleLifeTime)
    {
        UpdatedPosition = in_Position + in_Velocity;
        UpdatedVelocity = in_Velocity;
        UpdatedAge = in_Age + deltaTime;
    }
    // particle is not alive, check bullet is alive
    else if (isBulletAlive)
    {
        // particle spawn
        if (in_Age < 0 && (in_Age + deltaTime) >= 0)
        {
            UpdatedPosition = getInitPosition();
            UpdatedVelocity = -in_Random.w * bulletDirection;
            UpdatedAge = in_Age + deltaTime;
        }
        // particle dead - respawn
        else if (in_Age > particleLifeTime)
        {
            UpdatedPosition = getInitPosition();
            UpdatedVelocity = -in_Random.w * bulletDirection;
            UpdatedAge = in_Age - particleLifeTime;
        }
        // particle is coming
        else // in_Age < 0
        {
            UpdatedAge = in_Age + deltaTime;
        }
    }
}

void render()
{
    if (0 <= in_Age && in_Age < particleLifeTime)
    {
        ParticleColor = vec4(vec3(in_Random.w), clamp(1.0 - in_Age / particleLifeTime, 0.0, 1.0));
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
