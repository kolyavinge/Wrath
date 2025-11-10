#version 460 core

layout (location = 0) in vec3 in_VertexPosition;
layout (location = 1) in vec3 in_VertexVelocity;
layout (location = 2) in float in_VertexAge;
layout (location = 6) in vec4 in_Random;

// for feedback buffer
out vec3 Position;
out vec3 Velocity;
out float Age;

// for fragment shader
out vec3 ParticleColor;
out float TransparentValue;

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

vec3 rotatePoint(vec3 point, vec3 pivotAxis, float radian)
{
    float sinValue = sin(radian);
    float cosValue = cos(radian);
    // Формула Родрига
    vec3 rotated = cosValue * point + dot(pivotAxis, point) * (1.0 - cosValue) * pivotAxis + sinValue * cross(pivotAxis, point);

    return rotated;
}

vec3 getInitPosition()
{
    vec3 initPoint = in_Random.x * bulletNozzleRadius * bulletDirectionTopNormal;
    return tracePosition + rotatePoint(initPoint, bulletDirection, in_Random.z) - in_Random.y * bulletDirection;
}

void update()
{
    // particle is alive - move it, whether bullet is alive or not
    if (0 <= in_VertexAge && in_VertexAge < particleLifeTime)
    {
        Position = in_VertexPosition + in_VertexVelocity;
        Velocity = in_VertexVelocity;
        Age = in_VertexAge + deltaTime;
    }
    // particle is not alive, check bullet is alive
    else if (isBulletAlive)
    {
        // particle spawn
        if (in_VertexAge < 0 && (in_VertexAge + deltaTime) >= 0)
        {
            Position = getInitPosition();
            Velocity = -in_Random.w * bulletDirection;
            Age = in_VertexAge + deltaTime;
        }
        // particle dead - respawn
        else if (in_VertexAge > particleLifeTime)
        {
            Position = getInitPosition();
            Velocity = -in_Random.w * bulletDirection;
            Age = in_VertexAge - particleLifeTime;
        }
        // particle is coming
        else // in_VertexAge < 0
        {
            Age = in_VertexAge + deltaTime;
        }
    }
}

void render()
{
    if (0 <= in_VertexAge && in_VertexAge < particleLifeTime)
    {
        ParticleColor = vec3(in_Random.w);
        TransparentValue = clamp(1.0 - in_VertexAge / particleLifeTime, 0.0, 1.0);
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
