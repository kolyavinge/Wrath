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

const float pi = 3.1415926535;

#define UNKNOWN 0
#define FIRE 1
#define FLASH 2
#define SMOKE 3
#define SPARK 4

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
    if (inRange(gl_InstanceID, 0, 8)) return FIRE;
    if (inRange(gl_InstanceID, 8, 9)) return FLASH;
    if (inRange(gl_InstanceID, 9, 41)) return SMOKE;
    if (inRange(gl_InstanceID, 49, 57)) return SPARK;

    return UNKNOWN;
}

float getParticleAge()
{
    return in_InitAge + (currentTimeSec - initTimeSec);
}

float getParticleAgePercent(float age)
{
    return age / in_LifeTime;
}

// fire

vec3 getFireDistance(float age)
{
    return in_InitVelocity * age;
}

float getFireSize(float age)
{
    return 1.5 * clamp(age / 0.1, 0.0, 1.0);
}

vec4 getFireColor(float age)
{
    float colorFactor = 1.0 - clamp(2.0 * getParticleAgePercent(age), 0.2, 1.0);
    float alphaFactor = 1.0 - getParticleAgePercent(age);

    return vec4(vec3(colorFactor), alphaFactor);
}

// flash

vec3 getFlashDistance(float age)
{
    return in_InitVelocity * age;
}

float getFlashSize(float age)
{
    return 2.0 * sin(pi * (age / (in_LifeTime / 2.0)));
}

vec4 getFlashColor(float age)
{
    float colorFactor = 1.0;
    float alphaFactor = sin(pi * (age / (in_LifeTime / 2.0)));

    return vec4(vec3(colorFactor), alphaFactor);
}

// smoke

vec3 getSmokeDistance(float age)
{
    float accel = 2.0 * getParticleAgePercent(age);
    return in_InitVelocity * age * accel;
}

float getSmokeSize(float age)
{
    return getParticleAgePercent(age);
}

vec4 getSmokeColor(float age)
{
    float alphaFactor = 0.5 * (1.0 - getParticleAgePercent(age));

    return vec4(vec3(1.0), alphaFactor);
}

// spark

vec3 getSparkDistance(float age)
{
    float accel = 2.0 * getParticleAgePercent(age);
    return in_InitVelocity * age * accel;
}

float getSparkSize(float age)
{
    return 0.25;
}

vec4 getSparkColor(float age)
{
    float alphaFactor = 1.0 - getParticleAgePercent(age);

    return vec4(vec3(2.0), alphaFactor);
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
    if (0 <= age && age < in_LifeTime)
    {
        vec3 dist = vec3(0.0);
        float size = 0.0;
        vec4 color = vec4(0.0);
        int particleType = getParticleType();
        if (particleType == FIRE)
        {
            dist = getFireDistance(age);
            size = getFireSize(age);
            color = getFireColor(age);
        }
        else if (particleType == FLASH)
        {
            dist = getFlashDistance(age);
            size = getFlashSize(age);
            color = getFlashColor(age);
        }
        else if (particleType == SMOKE)
        {
            dist = getSmokeDistance(age);
            size = getSmokeSize(age);
            color = getSmokeColor(age);
        }
        else if (particleType == SPARK)
        {
            dist = getSparkDistance(age);
            size = getSparkSize(age);
            color = getSparkColor(age);
        }
        vec3 position = in_InitPosition + dist;
        ParticleColor = color;
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
