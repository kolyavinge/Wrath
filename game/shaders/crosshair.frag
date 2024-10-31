#version 460 core

out vec4 FragColor;

const vec3 crosshairColor = vec3(1.0, 0.5, 0.0);
const float smoothValue = 0.001;

uniform vec2 resolution;

bool between(float x, float left, float right)
{
    return left <= x && x <= right;
}

float getArcColor(vec2 uv, float dist, float radius, float thickness)
{
    float outRadius = radius + thickness;
    if (between(dot(uv, vec2(+1.0, 0.0)) / dist, 0.8, 1.0) ||
        between(dot(uv, vec2(-1.0, 0.0)) / dist, 0.8, 1.0))
    {
        return
            smoothstep(outRadius - smoothValue, outRadius, dist) -
            smoothstep(radius - smoothValue, radius, dist);
    }
    else
    {
        return 0.0;
    }
}

float getCenterPointColor(float dist)
{
    return smoothstep(0.001, 0.002, dist);
}

void main()
{
    vec2 uv = gl_FragCoord.xy / resolution;
    uv -= vec2(0.5);
    uv.x *= resolution.x / resolution.y;
    float dist = length(uv);
    float alpha =
        getArcColor(uv, dist, 0.02, 0.001) +
        getArcColor(uv, dist, 0.015, 0.0008) +
        getCenterPointColor(dist);
    FragColor = vec4(crosshairColor, 1.0 - alpha);
}
