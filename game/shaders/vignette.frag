#version 460 core

out vec4 FragColor;

uniform vec2 resolution;
uniform float radius;
uniform float alphaFactor;

const float maxRadius = 0.70710678; // 0.5 * √2

void main()
{
    vec2 uv = gl_FragCoord.xy / resolution;
    uv -= vec2(0.5);
    float dist = length(uv);
    if (dist < radius)
    {
        discard;
    }
    else
    {
        float alpha = alphaFactor * smoothstep(radius, maxRadius, dist);
        FragColor = vec4(0.0, 0.0, 0.0, alpha);
    }
}
