// common shader functions

vec3 rotatePoint(vec3 point, vec3 pivotAxis, float radian)
{
    float sinValue = sin(radian);
    float cosValue = cos(radian);
    // Формула Родрига
    vec3 rotated = cosValue * point + dot(pivotAxis, point) * (1.0 - cosValue) * pivotAxis + sinValue * cross(pivotAxis, point);

    return rotated;
}
