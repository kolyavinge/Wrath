#pragma once

#define MYDLL_EXPORTS

#ifdef MYDLL_EXPORTS
#define MYDLL_API __declspec(dllexport)
#else
#define MYDLL_API __declspec(dllimport)
#endif

extern "C" MYDLL_API
void convertFacesToAdjacencyFormat(int facesCount, unsigned int* faces, unsigned int* adjResult);
