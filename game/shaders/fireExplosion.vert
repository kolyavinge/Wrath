#version 460 core

layout (location = 0) in vec3 in_InitPosition;
layout (location = 1) in vec3 in_InitVelocity;
layout (location = 2) in float in_InitAge;
layout (location = 3) in float in_LifeTime;
layout (location = 5) in vec4 in_TexCoord;

out vec4 ParticleColor;
out vec2 TexCoord;

uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;
uniform float initTimeSec;
uniform float currentTimeSec;

#define UNKNOWN 0
#define FIRE 1
#define FLASH 2
#define SPARK 3
#define TRAIT 4

const vec3 vertices[] = vec3[]
(
    vec3(-0.5, -0.5, 0.0), vec3(0.5, -0.5, 0.0), vec3( 0.5, 0.5, 0.0),
    vec3(-0.5, -0.5, 0.0), vec3(0.5,  0.5, 0.0), vec3(-0.5, 0.5, 0.0)
);

bool inRange(int value, int left, int right)
{
    return left <= value && value < right;
}

bool inRange(float value, float left, float right)
{
    return left <= value && value < right;
}

int getParticleType()
{
    if (inRange(gl_InstanceID, 0, 4)) return FIRE;
    if (inRange(gl_InstanceID, 4, 8)) return FLASH;
    if (inRange(gl_InstanceID, 8, 18)) return SPARK;
    if (inRange(gl_InstanceID, 18, 24)) return TRAIT;

    return UNKNOWN;
}

float getParticleAge()
{
    return in_InitAge + (currentTimeSec - initTimeSec);
}

vec3 getFireVelocity(float age)
{
    return in_InitVelocity * age;
}

float getFireSize(float age)
{
    return clamp(age / 0.1, 0.0, 1.0);
}

vec2 getParticleTexCoord()
{
    if (gl_VertexID == 0 || gl_VertexID == 3) return vec2(in_TexCoord.x, in_TexCoord.y);
    if (gl_VertexID == 1) return vec2(in_TexCoord.x + in_TexCoord.z, in_TexCoord.y);
    if (gl_VertexID == 2 || gl_VertexID == 4) return vec2(in_TexCoord.x + in_TexCoord.z, in_TexCoord.y + in_TexCoord.w);
    if (gl_VertexID == 5) return vec2(in_TexCoord.x, in_TexCoord.y + in_TexCoord.w);
}

void main()
{
    float age = getParticleAge();
    if (age >= 0)
    {
        vec3 velocity = vec3(0.0);
        float size = 0.0;
        int particleType = getParticleType();
        if (particleType == FIRE)
        {
            velocity = getFireVelocity(age);
            size = getFireSize(age);
        }
        else if (particleType == FLASH)
        {
        }
        else if (particleType == SPARK)
        {
        }
        else if (particleType == TRAIT)
        {
        }
        vec3 position = in_InitPosition + velocity;
        ParticleColor = vec4(vec3(1.0), clamp(1.0 - age / in_LifeTime, 0.0, 1.0));
        TexCoord = getParticleTexCoord();
        vec3 viewPosition = (viewMatrix * vec4(position, 1.0)).xyz + vertices[gl_VertexID] * size;
        gl_Position = projectionMatrix * vec4(viewPosition, 1.0);
    }
    else
    {
        ParticleColor = vec4(0.0);
        gl_Position = vec4(0.0);
    }
}
