#include "pch.h"
#include <limits.h>
#include "api.h"

// adjResult must be passed already created with double capacity of faces
void convertFacesToAdjacencyFormat(int facesCount, unsigned int* faces, unsigned int* adjResult) {
    int adjCount = 2 * facesCount;

    // Copy and make room for adjacency info
    for (int i = 0; i < facesCount; i += 3) {
        adjResult[i * 2 + 0] = faces[i];
        adjResult[i * 2 + 1] = UINT_MAX;
        adjResult[i * 2 + 2] = faces[i + 1];
        adjResult[i * 2 + 3] = UINT_MAX;
        adjResult[i * 2 + 4] = faces[i + 2];
        adjResult[i * 2 + 5] = UINT_MAX;
    }

    // Find matching edges
    for (int i = 0; i < adjCount; i += 6) {
        // A triangle
        unsigned int a1 = adjResult[i];
        unsigned int b1 = adjResult[i + 2];
        unsigned int c1 = adjResult[i + 4];

        // Scan subsequent triangles
        for (int j = i + 6; j < adjCount; j += 6) {
            unsigned int a2 = adjResult[j];
            unsigned int b2 = adjResult[j + 2];
            unsigned int c2 = adjResult[j + 4];

            // Edge 1 == Edge 1
            if ((a1 == a2 && b1 == b2) || (a1 == b2 && b1 == a2)) {
                adjResult[i + 1] = c2;
                adjResult[j + 1] = c1;
            }
            // Edge 1 == Edge 2
            if ((a1 == b2 && b1 == c2) || (a1 == c2 && b1 == b2)) {
                adjResult[i + 1] = a2;
                adjResult[j + 3] = c1;
            }
            // Edge 1 == Edge 3
            if ((a1 == c2 && b1 == a2) || (a1 == a2 && b1 == c2)) {
                adjResult[i + 1] = b2;
                adjResult[j + 5] = c1;
            }
            // Edge 2 == Edge 1
            if ((b1 == a2 && c1 == b2) || (b1 == b2 && c1 == a2)) {
                adjResult[i + 3] = c2;
                adjResult[j + 1] = a1;
            }
            // Edge 2 == Edge 2
            if ((b1 == b2 && c1 == c2) || (b1 == c2 && c1 == b2)) {
                adjResult[i + 3] = a2;
                adjResult[j + 3] = a1;
            }
            // Edge 2 == Edge 3
            if ((b1 == c2 && c1 == a2) || (b1 == a2 && c1 == c2)) {
                adjResult[i + 3] = b2;
                adjResult[j + 5] = a1;
            }
            // Edge 3 == Edge 1
            if ((c1 == a2 && a1 == b2) || (c1 == b2 && a1 == a2)) {
                adjResult[i + 5] = c2;
                adjResult[j + 1] = b1;
            }
            // Edge 3 == Edge 2
            if ((c1 == b2 && a1 == c2) || (c1 == c2 && a1 == b2)) {
                adjResult[i + 5] = a2;
                adjResult[j + 3] = b1;
            }
            // Edge 3 == Edge 3
            if ((c1 == c2 && a1 == a2) || (c1 == a2 && a1 == c2)) {
                adjResult[i + 5] = b2;
                adjResult[j + 5] = b1;
            }
        }
    }

    // Look for any outside edges
    for (int i = 0; i < adjCount; i += 6) {
        if (adjResult[i + 1] == UINT_MAX) adjResult[i + 1] = adjResult[i + 4];
        if (adjResult[i + 3] == UINT_MAX) adjResult[i + 3] = adjResult[i];
        if (adjResult[i + 5] == UINT_MAX) adjResult[i + 5] = adjResult[i + 2];
    }
}
