#version 460 core

out vec4 FragColor;

in vec3 Position;

uniform vec3 origin;
uniform vec3 mainAxis;
uniform float rayLength;
uniform float rayHeight;
uniform vec3 rayColor;
uniform float rayBrightness;
uniform float shineStrength;

void main()
{
    vec3 positionDirection = Position - origin;
    float projectedLength = dot(mainAxis, positionDirection);
    vec3 projectedPosition = projectedLength * mainAxis + origin;
    vec3 heightDirection = Position - projectedPosition;
    float height = length(heightDirection) - rayHeight;
    vec4 color = vec4(step(0.0, -height));
    float shine = shineStrength / height;
    shine = clamp(shine, 0.0, 1.0);
    color += shine;
    color *= vec4(rayColor, 1.0);
    color.w *= smoothstep((1.0 - rayBrightness) * rayLength, (1.0 - rayBrightness + 0.1) * rayLength, projectedLength);
    FragColor = color;
}
