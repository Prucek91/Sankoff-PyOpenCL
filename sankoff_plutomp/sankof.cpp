// g++ sankof.cpp -pthread -O3 -fopenmp -o binarka
#include <omp.h>
#include <math.h>
#include <algorithm>
#include <chrono>
#include <iostream>
#include <fstream>
#include <vector>

//#define ceild(n,d)  ceil(((double)(n))/((double)(d)))
//#define floord(n,d) floor(((double)(n))/((double)(d)))
//#define max(x,y)    ((x) > (y)? (x) : (y))
//#define min(x,y)    ((x) < (y)? (x) : (y))

int ro(int a, int b)
{
  return 0;
}

int MAX(int a, int b)
{
  if (a > b)
    return a;
  else
    return b;
}

int MIN(int a, int b)
{
  if (a < b)
    return a;
  else
    return b;
}

std::string test(int F, int N)
{

  auto generowanie_danych_start = std::chrono::high_resolution_clock::now();

  int t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13;
  int lb, ub, lbp, ubp, lb2, ub2;
  register int lbv, ubv;
  int y = 0;
  int y2 = 0;
  int teta = 0;
  int bijA = 0;
  int bijB = 0;
  int bklB = 0;

  int size1 = F + 2;
  int size2 = N + 10;
  int size3 = N + 10;
  int size4 = N + 10;

  int ****D = new int ***[size1];

  for (int i = 0; i < size1; i++)
  {
    D[i] = new int **[size2];
    for (int j = 0; j < size2; j++)
    {
      D[i][j] = new int *[size3];
      for (int k = 0; k < size3; k++)
        D[i][j][k] = new int[size4];
    }
  }

  std::vector<int> A(10000);
  std::vector<int> B(10000);

  int LA = F;
  int LB = N;

  auto generowanie_danych_stop = std::chrono::high_resolution_clock::now();

  //  Start of CLooG code
  auto obliczenia_start = std::chrono::high_resolution_clock::now();

  if ((LA >= 1) && (LB >= 1))
  {
    if ((LA >= 2) && (LB >= 2))
    {
      for (t2 = -LA - LB; t2 <= -LA - LB + 1; t2++)
      {
        lbp = -LB;
        ubp = t2 + LA;

#pragma omp parallel for private(lbv, ubv, t5, t6, t7, t8, t9, t10, t11, t12, t13)
        for (t4 = lbp; t4 <= ubp; t4++)
        {
          for (t6 = -t2 + t4; t6 <= LA; t6++)
          {
            for (t8 = -t4; t8 <= LB; t8++)
            {
              if ((-t2 + t4) < 0 || t6 < 0 || -t4 < 0 || t8 < 0)
              {
                continue;
              }
              D[(-t2 + t4)][t6][-t4][t8] = D[(-t2 + t4) + 1][t6][-t4][t8] + y;
              ;
              D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t6 - 1][-t4][t8] + y, D[(-t2 + t4)][t6][-t4][t8]);
              ;
              D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t6][-t4 + 1][t8] + y, D[(-t2 + t4)][t6][-t4][t8]);
              ;
              D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t6][-t4][t8 - 1] + y, D[(-t2 + t4)][t6][-t4][t8]);
              ;
              D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4) + 1][t6][-t4 + 1][t8] + ro(A[(-t2 + t4)], B[-t4]), D[(-t2 + t4)][t6][-t4][t8]);
              ;
              D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t6 - 1][-t4][t8 - 1] + ro(A[t6], B[t8]), D[(-t2 + t4)][t6][-t4][t8]);
              ;
              D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4) + 1][t6 - 1][-t4][1] + bijA + y2, D[(-t2 + t4)][t6][-t4][t8]);
              ;
              D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t6][-t4 + 1][t8 - 1] + bklB + y2, D[(-t2 + t4)][t6][-t4][t8]);
              ;
              D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4) + 1][t6 - 1][-t4 + 1][t8 - 1] + bijA + bklB + teta, D[(-t2 + t4)][t6][-t4][t8]);
              ;
            }
          }
        }
      }
    }

    if ((LA >= 2) && (LB == 1))
    {
      for (t2 = -LA - 1; t2 <= -2; t2++)
      {
        for (t6 = -t2 - 1; t6 <= LA; t6++)
        {
          D[(-t2 - 1)][t6][1][1] = D[(-t2 - 1) + 1][t6][1][1] + y;
          ;
          D[(-t2 - 1)][t6][1][1] = MAX(D[(-t2 - 1)][t6 - 1][1][1] + y, D[(-t2 - 1)][t6][1][1]);
          ;
          D[(-t2 - 1)][t6][1][1] = MAX(D[(-t2 - 1)][t6][1 + 1][1] + y, D[(-t2 - 1)][t6][1][1]);
          ;
          D[(-t2 - 1)][t6][1][1] = MAX(D[(-t2 - 1)][t6][1][1 - 1] + y, D[(-t2 - 1)][t6][1][1]);
          ;
          D[(-t2 - 1)][t6][1][1] = MAX(D[(-t2 - 1) + 1][t6][1 + 1][1] + ro(A[(-t2 - 1)], B[1]), D[(-t2 - 1)][t6][1][1]);
          ;
          D[(-t2 - 1)][t6][1][1] = MAX(D[(-t2 - 1)][t6 - 1][1][1 - 1] + ro(A[t6], B[1]), D[(-t2 - 1)][t6][1][1]);
          ;
          D[(-t2 - 1)][t6][1][1] = MAX(D[(-t2 - 1) + 1][t6 - 1][1][1] + bijA + y2, D[(-t2 - 1)][t6][1][1]);
          ;
          D[(-t2 - 1)][t6][1][1] = MAX(D[(-t2 - 1)][t6][1 + 1][1 - 1] + bklB + y2, D[(-t2 - 1)][t6][1][1]);
          ;
          D[(-t2 - 1)][t6][1][1] = MAX(D[(-t2 - 1) + 1][t6 - 1][1 + 1][1 - 1] + bijA + bklB + teta, D[(-t2 - 1)][t6][1][1]);
          ;
        }
      }
    }
    if (LA == 1)
    {
      for (t2 = -LB - 1; t2 <= -2; t2++)
      {
        for (t8 = -t2 - 1; t8 <= LB; t8++)
        {
          D[1][1][(-t2 - 1)][t8] = D[1 + 1][1][(-t2 - 1)][t8] + y;
          ;
          D[1][1][(-t2 - 1)][t8] = MAX(D[1][1 - 1][(-t2 - 1)][t8] + y, D[1][1][(-t2 - 1)][t8]);
          ;
          D[1][1][(-t2 - 1)][t8] = MAX(D[1][1][(-t2 - 1) + 1][t8] + y, D[1][1][(-t2 - 1)][t8]);
          ;
          D[1][1][(-t2 - 1)][t8] = MAX(D[1][1][(-t2 - 1)][t8 - 1] + y, D[1][1][(-t2 - 1)][t8]);
          ;
          D[1][1][(-t2 - 1)][t8] = MAX(D[1 + 1][1][(-t2 - 1) + 1][t8] + ro(A[1], B[(-t2 - 1)]), D[1][1][(-t2 - 1)][t8]);
          ;
          D[1][1][(-t2 - 1)][t8] = MAX(D[1][1 - 1][(-t2 - 1)][t8 - 1] + ro(A[1], B[t8]), D[1][1][(-t2 - 1)][t8]);
          ;
          D[1][1][(-t2 - 1)][t8] = MAX(D[1 + 1][1 - 1][(-t2 - 1)][1] + bijA + y2, D[1][1][(-t2 - 1)][t8]);
          ;
          D[1][1][(-t2 - 1)][t8] = MAX(D[1][1][(-t2 - 1) + 1][t8 - 1] + bklB + y2, D[1][1][(-t2 - 1)][t8]);
          ;
          D[1][1][(-t2 - 1)][t8] = MAX(D[1 + 1][1 - 1][(-t2 - 1) + 1][t8 - 1] + bijA + bklB + teta, D[1][1][(-t2 - 1)][t8]);
          ;
        }
      }
    }
    for (t2 = -LA - LB + 2; t2 <= MIN(-LA - 1, -LB - 1); t2++)
    {
      for (t6 = -t2 - LB; t6 <= LA; t6++)
      {
        D[(-t2 - LB)][t6][LB][LB] = D[(-t2 - LB) + 1][t6][LB][LB] + y;
        ;
        D[(-t2 - LB)][t6][LB][LB] = MAX(D[(-t2 - LB)][t6 - 1][LB][LB] + y, D[(-t2 - LB)][t6][LB][LB]);
        ;
        D[(-t2 - LB)][t6][LB][LB] = MAX(D[(-t2 - LB)][t6][LB + 1][LB] + y, D[(-t2 - LB)][t6][LB][LB]);
        ;
        D[(-t2 - LB)][t6][LB][LB] = MAX(D[(-t2 - LB)][t6][LB][LB - 1] + y, D[(-t2 - LB)][t6][LB][LB]);
        ;
        D[(-t2 - LB)][t6][LB][LB] = MAX(D[(-t2 - LB) + 1][t6][LB + 1][LB] + ro(A[(-t2 - LB)], B[LB]), D[(-t2 - LB)][t6][LB][LB]);
        ;
        D[(-t2 - LB)][t6][LB][LB] = MAX(D[(-t2 - LB)][t6 - 1][LB][LB - 1] + ro(A[t6], B[LB]), D[(-t2 - LB)][t6][LB][LB]);
        ;
        D[(-t2 - LB)][t6][LB][LB] = MAX(D[(-t2 - LB) + 1][t6 - 1][LB][1] + bijA + y2, D[(-t2 - LB)][t6][LB][LB]);
        ;
        D[(-t2 - LB)][t6][LB][LB] = MAX(D[(-t2 - LB)][t6][LB + 1][LB - 1] + bklB + y2, D[(-t2 - LB)][t6][LB][LB]);
        ;
        D[(-t2 - LB)][t6][LB][LB] = MAX(D[(-t2 - LB) + 1][t6 - 1][LB + 1][LB - 1] + bijA + bklB + teta, D[(-t2 - LB)][t6][LB][LB]);
        ;
      }
      lbp = -LB + 1;
      ubp = t2 + LA - 1;
#pragma omp parallel for private(lbv, ubv, t5, t6, t7, t8, t9, t10, t11, t12, t13)
      for (t4 = lbp; t4 <= ubp; t4++)
      {
        for (t8 = -t4; t8 <= LB; t8++)
        {
          D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = D[(-t2 + t4) + 1][(-t2 + t4)][-t4][t8] + y;
          ;
          D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4)][(-t2 + t4) - 1][-t4][t8] + y, D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
          ;
          D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4)][(-t2 + t4)][-t4 + 1][t8] + y, D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
          ;
          D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4)][(-t2 + t4)][-t4][t8 - 1] + y, D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
          ;
          D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4) + 1][(-t2 + t4)][-t4 + 1][t8] + ro(A[(-t2 + t4)], B[-t4]), D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
          ;
          D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4)][(-t2 + t4) - 1][-t4][t8 - 1] + ro(A[(-t2 + t4)], B[t8]), D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
          ;
          D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4) + 1][(-t2 + t4) - 1][-t4][1] + bijA + y2, D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
          ;
          D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4)][(-t2 + t4)][-t4 + 1][t8 - 1] + bklB + y2, D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
          ;
          D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4) + 1][(-t2 + t4) - 1][-t4 + 1][t8 - 1] + bijA + bklB + teta, D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
          ;
        }
        for (t6 = -t2 + t4 + 1; t6 <= LA; t6++)
        {
          D[(-t2 + t4)][t6][-t4][-t4] = D[(-t2 + t4) + 1][t6][-t4][-t4] + y;
          ;
          D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4)][t6 - 1][-t4][-t4] + y, D[(-t2 + t4)][t6][-t4][-t4]);
          ;
          D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4)][t6][-t4 + 1][-t4] + y, D[(-t2 + t4)][t6][-t4][-t4]);
          ;
          D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4)][t6][-t4][-t4 - 1] + y, D[(-t2 + t4)][t6][-t4][-t4]);
          ;
          D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4) + 1][t6][-t4 + 1][-t4] + ro(A[(-t2 + t4)], B[-t4]), D[(-t2 + t4)][t6][-t4][-t4]);
          ;
          D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4)][t6 - 1][-t4][-t4 - 1] + ro(A[t6], B[-t4]), D[(-t2 + t4)][t6][-t4][-t4]);
          ;
          D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4) + 1][t6 - 1][-t4][1] + bijA + y2, D[(-t2 + t4)][t6][-t4][-t4]);
          ;
          D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4)][t6][-t4 + 1][-t4 - 1] + bklB + y2, D[(-t2 + t4)][t6][-t4][-t4]);
          ;
          D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4) + 1][t6 - 1][-t4 + 1][-t4 - 1] + bijA + bklB + teta, D[(-t2 + t4)][t6][-t4][-t4]);
          ;
          for (t8 = -t4 + 1; t8 <= LB; t8++)
          {
            D[(-t2 + t4)][t6][-t4][t8] = D[(-t2 + t4) + 1][t6][-t4][t8] + y;
            ;
            D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t6 - 1][-t4][t8] + y, D[(-t2 + t4)][t6][-t4][t8]);
            ;
            D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t6][-t4 + 1][t8] + y, D[(-t2 + t4)][t6][-t4][t8]);
            ;
            D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t6][-t4][t8 - 1] + y, D[(-t2 + t4)][t6][-t4][t8]);
            ;
            D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4) + 1][t6][-t4 + 1][t8] + ro(A[(-t2 + t4)], B[-t4]), D[(-t2 + t4)][t6][-t4][t8]);
            ;
            D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t6 - 1][-t4][t8 - 1] + ro(A[t6], B[t8]), D[(-t2 + t4)][t6][-t4][t8]);
            ;
            D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4) + 1][t6 - 1][-t4][1] + bijA + y2, D[(-t2 + t4)][t6][-t4][t8]);
            ;
            D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t6][-t4 + 1][t8 - 1] + bklB + y2, D[(-t2 + t4)][t6][-t4][t8]);
            ;
            D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4) + 1][t6 - 1][-t4 + 1][t8 - 1] + bijA + bklB + teta, D[(-t2 + t4)][t6][-t4][t8]);
            ;
            for (t10 = -t2 + t4 + 1; t10 <= t6; t10++)
            {
              for (t12 = -t4 + 1; t12 <= t8; t12++)
              {
                D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t10][-t4][t12] + D[t10 + 1][t6][t12 + 1][t8], D[(-t2 + t4)][t6][-t4][t8]);
                ;
              }
            }
          }
        }
      }
      for (t8 = -t2 - LA; t8 <= LB; t8++)
      {
        D[LA][LA][(-t2 - LA)][t8] = D[LA + 1][LA][(-t2 - LA)][t8] + y;
        ;
        D[LA][LA][(-t2 - LA)][t8] = MAX(D[LA][LA - 1][(-t2 - LA)][t8] + y, D[LA][LA][(-t2 - LA)][t8]);
        ;
        D[LA][LA][(-t2 - LA)][t8] = MAX(D[LA][LA][(-t2 - LA) + 1][t8] + y, D[LA][LA][(-t2 - LA)][t8]);
        ;
        D[LA][LA][(-t2 - LA)][t8] = MAX(D[LA][LA][(-t2 - LA)][t8 - 1] + y, D[LA][LA][(-t2 - LA)][t8]);
        ;
        D[LA][LA][(-t2 - LA)][t8] = MAX(D[LA + 1][LA][(-t2 - LA) + 1][t8] + ro(A[LA], B[(-t2 - LA)]), D[LA][LA][(-t2 - LA)][t8]);
        ;
        D[LA][LA][(-t2 - LA)][t8] = MAX(D[LA][LA - 1][(-t2 - LA)][t8 - 1] + ro(A[LA], B[t8]), D[LA][LA][(-t2 - LA)][t8]);
        ;
        D[LA][LA][(-t2 - LA)][t8] = MAX(D[LA + 1][LA - 1][(-t2 - LA)][1] + bijA + y2, D[LA][LA][(-t2 - LA)][t8]);
        ;
        D[LA][LA][(-t2 - LA)][t8] = MAX(D[LA][LA][(-t2 - LA) + 1][t8 - 1] + bklB + y2, D[LA][LA][(-t2 - LA)][t8]);
        ;
        D[LA][LA][(-t2 - LA)][t8] = MAX(D[LA + 1][LA - 1][(-t2 - LA) + 1][t8 - 1] + bijA + bklB + teta, D[LA][LA][(-t2 - LA)][t8]);
        ;
      }
    }
    if (LB >= 2)
    {
      for (t2 = -LA; t2 <= -LB - 1; t2++)
      {
        for (t6 = -t2 - LB; t6 <= LA; t6++)
        {
          D[(-t2 - LB)][t6][LB][LB] = D[(-t2 - LB) + 1][t6][LB][LB] + y;
          ;
          D[(-t2 - LB)][t6][LB][LB] = MAX(D[(-t2 - LB)][t6 - 1][LB][LB] + y, D[(-t2 - LB)][t6][LB][LB]);
          ;
          D[(-t2 - LB)][t6][LB][LB] = MAX(D[(-t2 - LB)][t6][LB + 1][LB] + y, D[(-t2 - LB)][t6][LB][LB]);
          ;
          D[(-t2 - LB)][t6][LB][LB] = MAX(D[(-t2 - LB)][t6][LB][LB - 1] + y, D[(-t2 - LB)][t6][LB][LB]);
          ;
          D[(-t2 - LB)][t6][LB][LB] = MAX(D[(-t2 - LB) + 1][t6][LB + 1][LB] + ro(A[(-t2 - LB)], B[LB]), D[(-t2 - LB)][t6][LB][LB]);
          ;
          D[(-t2 - LB)][t6][LB][LB] = MAX(D[(-t2 - LB)][t6 - 1][LB][LB - 1] + ro(A[t6], B[LB]), D[(-t2 - LB)][t6][LB][LB]);
          ;
          D[(-t2 - LB)][t6][LB][LB] = MAX(D[(-t2 - LB) + 1][t6 - 1][LB][1] + bijA + y2, D[(-t2 - LB)][t6][LB][LB]);
          ;
          D[(-t2 - LB)][t6][LB][LB] = MAX(D[(-t2 - LB)][t6][LB + 1][LB - 1] + bklB + y2, D[(-t2 - LB)][t6][LB][LB]);
          ;
          D[(-t2 - LB)][t6][LB][LB] = MAX(D[(-t2 - LB) + 1][t6 - 1][LB + 1][LB - 1] + bijA + bklB + teta, D[(-t2 - LB)][t6][LB][LB]);
          ;
        }
        lbp = -LB + 1;
        ubp = -1;
#pragma omp parallel for private(lbv, ubv, t5, t6, t7, t8, t9, t10, t11, t12, t13)
        for (t4 = lbp; t4 <= ubp; t4++)
        {
          for (t8 = -t4; t8 <= LB; t8++)
          {
            D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = D[(-t2 + t4) + 1][(-t2 + t4)][-t4][t8] + y;
            ;
            D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4)][(-t2 + t4) - 1][-t4][t8] + y, D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
            ;
            D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4)][(-t2 + t4)][-t4 + 1][t8] + y, D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
            ;
            D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4)][(-t2 + t4)][-t4][t8 - 1] + y, D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
            ;
            D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4) + 1][(-t2 + t4)][-t4 + 1][t8] + ro(A[(-t2 + t4)], B[-t4]), D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
            ;
            D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4)][(-t2 + t4) - 1][-t4][t8 - 1] + ro(A[(-t2 + t4)], B[t8]), D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
            ;
            D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4) + 1][(-t2 + t4) - 1][-t4][1] + bijA + y2, D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
            ;
            D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4)][(-t2 + t4)][-t4 + 1][t8 - 1] + bklB + y2, D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
            ;
            D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4) + 1][(-t2 + t4) - 1][-t4 + 1][t8 - 1] + bijA + bklB + teta, D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
            ;
          }
          for (t6 = -t2 + t4 + 1; t6 <= LA; t6++)
          {
            D[(-t2 + t4)][t6][-t4][-t4] = D[(-t2 + t4) + 1][t6][-t4][-t4] + y;
            ;
            D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4)][t6 - 1][-t4][-t4] + y, D[(-t2 + t4)][t6][-t4][-t4]);
            ;
            D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4)][t6][-t4 + 1][-t4] + y, D[(-t2 + t4)][t6][-t4][-t4]);
            ;
            D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4)][t6][-t4][-t4 - 1] + y, D[(-t2 + t4)][t6][-t4][-t4]);
            ;
            D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4) + 1][t6][-t4 + 1][-t4] + ro(A[(-t2 + t4)], B[-t4]), D[(-t2 + t4)][t6][-t4][-t4]);
            ;
            D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4)][t6 - 1][-t4][-t4 - 1] + ro(A[t6], B[-t4]), D[(-t2 + t4)][t6][-t4][-t4]);
            ;
            D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4) + 1][t6 - 1][-t4][1] + bijA + y2, D[(-t2 + t4)][t6][-t4][-t4]);
            ;
            D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4)][t6][-t4 + 1][-t4 - 1] + bklB + y2, D[(-t2 + t4)][t6][-t4][-t4]);
            ;
            D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4) + 1][t6 - 1][-t4 + 1][-t4 - 1] + bijA + bklB + teta, D[(-t2 + t4)][t6][-t4][-t4]);
            ;
            for (t8 = -t4 + 1; t8 <= LB; t8++)
            {
              D[(-t2 + t4)][t6][-t4][t8] = D[(-t2 + t4) + 1][t6][-t4][t8] + y;
              ;
              D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t6 - 1][-t4][t8] + y, D[(-t2 + t4)][t6][-t4][t8]);
              ;
              D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t6][-t4 + 1][t8] + y, D[(-t2 + t4)][t6][-t4][t8]);
              ;
              D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t6][-t4][t8 - 1] + y, D[(-t2 + t4)][t6][-t4][t8]);
              ;
              D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4) + 1][t6][-t4 + 1][t8] + ro(A[(-t2 + t4)], B[-t4]), D[(-t2 + t4)][t6][-t4][t8]);
              ;
              D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t6 - 1][-t4][t8 - 1] + ro(A[t6], B[t8]), D[(-t2 + t4)][t6][-t4][t8]);
              ;
              D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4) + 1][t6 - 1][-t4][1] + bijA + y2, D[(-t2 + t4)][t6][-t4][t8]);
              ;
              D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t6][-t4 + 1][t8 - 1] + bklB + y2, D[(-t2 + t4)][t6][-t4][t8]);
              ;
              D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4) + 1][t6 - 1][-t4 + 1][t8 - 1] + bijA + bklB + teta, D[(-t2 + t4)][t6][-t4][t8]);
              ;
              for (t10 = -t2 + t4 + 1; t10 <= t6; t10++)
              {
                for (t12 = -t4 + 1; t12 <= t8; t12++)
                {
                  D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t10][-t4][t12] + D[t10 + 1][t6][t12 + 1][t8], D[(-t2 + t4)][t6][-t4][t8]);
                  ;
                }
              }
            }
          }
        }
      }
    }
    if (LA >= 2)
    {
      for (t2 = -LB; t2 <= -LA - 1; t2++)
      {
        lbp = t2 + 1;
        ubp = t2 + LA - 1;
#pragma omp parallel for private(lbv, ubv, t5, t6, t7, t8, t9, t10, t11, t12, t13)
        for (t4 = lbp; t4 <= ubp; t4++)
        {
          for (t8 = -t4; t8 <= LB; t8++)
          {
            D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = D[(-t2 + t4) + 1][(-t2 + t4)][-t4][t8] + y;
            ;
            D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4)][(-t2 + t4) - 1][-t4][t8] + y, D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
            ;
            D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4)][(-t2 + t4)][-t4 + 1][t8] + y, D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
            ;
            D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4)][(-t2 + t4)][-t4][t8 - 1] + y, D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
            ;
            D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4) + 1][(-t2 + t4)][-t4 + 1][t8] + ro(A[(-t2 + t4)], B[-t4]), D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
            ;
            D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4)][(-t2 + t4) - 1][-t4][t8 - 1] + ro(A[(-t2 + t4)], B[t8]), D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
            ;
            D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4) + 1][(-t2 + t4) - 1][-t4][1] + bijA + y2, D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
            ;
            D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4)][(-t2 + t4)][-t4 + 1][t8 - 1] + bklB + y2, D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
            ;
            D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4) + 1][(-t2 + t4) - 1][-t4 + 1][t8 - 1] + bijA + bklB + teta, D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
            ;
          }
          for (t6 = -t2 + t4 + 1; t6 <= LA; t6++)
          {
            D[(-t2 + t4)][t6][-t4][-t4] = D[(-t2 + t4) + 1][t6][-t4][-t4] + y;
            ;
            D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4)][t6 - 1][-t4][-t4] + y, D[(-t2 + t4)][t6][-t4][-t4]);
            ;
            D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4)][t6][-t4 + 1][-t4] + y, D[(-t2 + t4)][t6][-t4][-t4]);
            ;
            D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4)][t6][-t4][-t4 - 1] + y, D[(-t2 + t4)][t6][-t4][-t4]);
            ;
            D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4) + 1][t6][-t4 + 1][-t4] + ro(A[(-t2 + t4)], B[-t4]), D[(-t2 + t4)][t6][-t4][-t4]);
            ;
            D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4)][t6 - 1][-t4][-t4 - 1] + ro(A[t6], B[-t4]), D[(-t2 + t4)][t6][-t4][-t4]);
            ;
            D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4) + 1][t6 - 1][-t4][1] + bijA + y2, D[(-t2 + t4)][t6][-t4][-t4]);
            ;
            D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4)][t6][-t4 + 1][-t4 - 1] + bklB + y2, D[(-t2 + t4)][t6][-t4][-t4]);
            ;
            D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4) + 1][t6 - 1][-t4 + 1][-t4 - 1] + bijA + bklB + teta, D[(-t2 + t4)][t6][-t4][-t4]);
            ;
            for (t8 = -t4 + 1; t8 <= LB; t8++)
            {
              D[(-t2 + t4)][t6][-t4][t8] = D[(-t2 + t4) + 1][t6][-t4][t8] + y;
              ;
              D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t6 - 1][-t4][t8] + y, D[(-t2 + t4)][t6][-t4][t8]);
              ;
              D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t6][-t4 + 1][t8] + y, D[(-t2 + t4)][t6][-t4][t8]);
              ;
              D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t6][-t4][t8 - 1] + y, D[(-t2 + t4)][t6][-t4][t8]);
              ;
              D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4) + 1][t6][-t4 + 1][t8] + ro(A[(-t2 + t4)], B[-t4]), D[(-t2 + t4)][t6][-t4][t8]);
              ;
              D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t6 - 1][-t4][t8 - 1] + ro(A[t6], B[t8]), D[(-t2 + t4)][t6][-t4][t8]);
              ;
              D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4) + 1][t6 - 1][-t4][1] + bijA + y2, D[(-t2 + t4)][t6][-t4][t8]);
              ;
              D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t6][-t4 + 1][t8 - 1] + bklB + y2, D[(-t2 + t4)][t6][-t4][t8]);
              ;
              D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4) + 1][t6 - 1][-t4 + 1][t8 - 1] + bijA + bklB + teta, D[(-t2 + t4)][t6][-t4][t8]);
              ;
              for (t10 = -t2 + t4 + 1; t10 <= t6; t10++)
              {
                for (t12 = -t4 + 1; t12 <= t8; t12++)
                {
                  D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t10][-t4][t12] + D[t10 + 1][t6][t12 + 1][t8], D[(-t2 + t4)][t6][-t4][t8]);
                  ;
                }
              }
            }
          }
        }
        for (t8 = -t2 - LA; t8 <= LB; t8++)
        {
          D[LA][LA][(-t2 - LA)][t8] = D[LA + 1][LA][(-t2 - LA)][t8] + y;
          ;
          D[LA][LA][(-t2 - LA)][t8] = MAX(D[LA][LA - 1][(-t2 - LA)][t8] + y, D[LA][LA][(-t2 - LA)][t8]);
          ;
          D[LA][LA][(-t2 - LA)][t8] = MAX(D[LA][LA][(-t2 - LA) + 1][t8] + y, D[LA][LA][(-t2 - LA)][t8]);
          ;
          D[LA][LA][(-t2 - LA)][t8] = MAX(D[LA][LA][(-t2 - LA)][t8 - 1] + y, D[LA][LA][(-t2 - LA)][t8]);
          ;
          D[LA][LA][(-t2 - LA)][t8] = MAX(D[LA + 1][LA][(-t2 - LA) + 1][t8] + ro(A[LA], B[(-t2 - LA)]), D[LA][LA][(-t2 - LA)][t8]);
          ;
          D[LA][LA][(-t2 - LA)][t8] = MAX(D[LA][LA - 1][(-t2 - LA)][t8 - 1] + ro(A[LA], B[t8]), D[LA][LA][(-t2 - LA)][t8]);
          ;
          D[LA][LA][(-t2 - LA)][t8] = MAX(D[LA + 1][LA - 1][(-t2 - LA)][1] + bijA + y2, D[LA][LA][(-t2 - LA)][t8]);
          ;
          D[LA][LA][(-t2 - LA)][t8] = MAX(D[LA][LA][(-t2 - LA) + 1][t8 - 1] + bklB + y2, D[LA][LA][(-t2 - LA)][t8]);
          ;
          D[LA][LA][(-t2 - LA)][t8] = MAX(D[LA + 1][LA - 1][(-t2 - LA) + 1][t8 - 1] + bijA + bklB + teta, D[LA][LA][(-t2 - LA)][t8]);
          ;
        }
      }
    }
    for (t2 = MAX(-LA, -LB); t2 <= -2; t2++)
    {
      lbp = t2 + 1;
      ubp = -1;
#pragma omp parallel for private(lbv, ubv, t5, t6, t7, t8, t9, t10, t11, t12, t13)
      for (t4 = lbp; t4 <= ubp; t4++)
      {
        for (t8 = -t4; t8 <= LB; t8++)
        {
          D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = D[(-t2 + t4) + 1][(-t2 + t4)][-t4][t8] + y;
          ;
          D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4)][(-t2 + t4) - 1][-t4][t8] + y, D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
          ;
          D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4)][(-t2 + t4)][-t4 + 1][t8] + y, D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
          ;
          D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4)][(-t2 + t4)][-t4][t8 - 1] + y, D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
          ;
          D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4) + 1][(-t2 + t4)][-t4 + 1][t8] + ro(A[(-t2 + t4)], B[-t4]), D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
          ;
          D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4)][(-t2 + t4) - 1][-t4][t8 - 1] + ro(A[(-t2 + t4)], B[t8]), D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
          ;
          D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4) + 1][(-t2 + t4) - 1][-t4][1] + bijA + y2, D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
          ;
          D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4)][(-t2 + t4)][-t4 + 1][t8 - 1] + bklB + y2, D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
          ;
          D[(-t2 + t4)][(-t2 + t4)][-t4][t8] = MAX(D[(-t2 + t4) + 1][(-t2 + t4) - 1][-t4 + 1][t8 - 1] + bijA + bklB + teta, D[(-t2 + t4)][(-t2 + t4)][-t4][t8]);
          ;
        }
        for (t6 = -t2 + t4 + 1; t6 <= LA; t6++)
        {
          D[(-t2 + t4)][t6][-t4][-t4] = D[(-t2 + t4) + 1][t6][-t4][-t4] + y;
          ;
          D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4)][t6 - 1][-t4][-t4] + y, D[(-t2 + t4)][t6][-t4][-t4]);
          ;
          D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4)][t6][-t4 + 1][-t4] + y, D[(-t2 + t4)][t6][-t4][-t4]);
          ;
          D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4)][t6][-t4][-t4 - 1] + y, D[(-t2 + t4)][t6][-t4][-t4]);
          ;
          D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4) + 1][t6][-t4 + 1][-t4] + ro(A[(-t2 + t4)], B[-t4]), D[(-t2 + t4)][t6][-t4][-t4]);
          ;
          D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4)][t6 - 1][-t4][-t4 - 1] + ro(A[t6], B[-t4]), D[(-t2 + t4)][t6][-t4][-t4]);
          ;
          D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4) + 1][t6 - 1][-t4][1] + bijA + y2, D[(-t2 + t4)][t6][-t4][-t4]);
          ;
          D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4)][t6][-t4 + 1][-t4 - 1] + bklB + y2, D[(-t2 + t4)][t6][-t4][-t4]);
          ;
          D[(-t2 + t4)][t6][-t4][-t4] = MAX(D[(-t2 + t4) + 1][t6 - 1][-t4 + 1][-t4 - 1] + bijA + bklB + teta, D[(-t2 + t4)][t6][-t4][-t4]);
          ;
          for (t8 = -t4 + 1; t8 <= LB; t8++)
          {
            D[(-t2 + t4)][t6][-t4][t8] = D[(-t2 + t4) + 1][t6][-t4][t8] + y;
            ;
            D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t6 - 1][-t4][t8] + y, D[(-t2 + t4)][t6][-t4][t8]);
            ;
            D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t6][-t4 + 1][t8] + y, D[(-t2 + t4)][t6][-t4][t8]);
            ;
            D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t6][-t4][t8 - 1] + y, D[(-t2 + t4)][t6][-t4][t8]);
            ;
            D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4) + 1][t6][-t4 + 1][t8] + ro(A[(-t2 + t4)], B[-t4]), D[(-t2 + t4)][t6][-t4][t8]);
            ;
            D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t6 - 1][-t4][t8 - 1] + ro(A[t6], B[t8]), D[(-t2 + t4)][t6][-t4][t8]);
            ;
            D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4) + 1][t6 - 1][-t4][1] + bijA + y2, D[(-t2 + t4)][t6][-t4][t8]);
            ;
            D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t6][-t4 + 1][t8 - 1] + bklB + y2, D[(-t2 + t4)][t6][-t4][t8]);
            ;
            D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4) + 1][t6 - 1][-t4 + 1][t8 - 1] + bijA + bklB + teta, D[(-t2 + t4)][t6][-t4][t8]);
            ;
            for (t10 = -t2 + t4 + 1; t10 <= t6; t10++)
            {
              for (t12 = -t4 + 1; t12 <= t8; t12++)
              {
                D[(-t2 + t4)][t6][-t4][t8] = MAX(D[(-t2 + t4)][t10][-t4][t12] + D[t10 + 1][t6][t12 + 1][t8], D[(-t2 + t4)][t6][-t4][t8]);
                ;
              }
            }
          }
        }
      }
    }
  }

  /* End of CLooG code */
  auto obliczenia_stop = std::chrono::high_resolution_clock::now();

  auto generowanie_danych = std::chrono::duration_cast<std::chrono::microseconds>(generowanie_danych_stop - generowanie_danych_start);
  auto czas_obliczen = std::chrono::duration_cast<std::chrono::microseconds>(obliczenia_stop - obliczenia_start);
  std::cout << F << "," << N << "," << (generowanie_danych.count()) << "," << czas_obliczen.count() << std::endl;

  std::string a = std::to_string(F) + "," +
                  std::to_string(N) + "," +
                  std::to_string(generowanie_danych.count()) +
                  "," +
                  std::to_string(czas_obliczen.count());

  return a;
}

int main(int ac, char **av)
{

  //int Fs[] = {2, 4, 6, 8, 10, 12};
  //int Ns[] = {24, 48, 72, 96, 120, 168, 216, 240};

  int F = atoi(av[1]);
  int N = atoi(av[2]);

  auto x = test(F, N);
  std::string filename("tmp.txt");
  std::ofstream file_out;

  file_out.open(filename, std::ios_base::app);
  file_out << x << std::endl;

  return 0;
}