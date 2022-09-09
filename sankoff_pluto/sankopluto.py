import numpy as np
import time
import pandas as pd


def MAX(a, b):
    if a > b:
        return a
    else:
        return b


def ro(a, b):
    return 0


def action(F, N, iter_=0):
    prepare_data_start_time = time.process_time()
    D = np.random.randint(low=1,  high=5,  size=(
        F+5, N+5, N+5, N+5)).astype(np.int8)
    A = D[0][0]
    B = D[0][0]
    t1 = 0
    t2 = 0
    t3 = 0
    t4 = 0
    t5 = 0
    t6 = 0
    t7 = 0
    t8 = 0
    t9 = 0
    t10 = 0
    t11 = 0
    t12 = 0
    t13 = 0
    lb = 0
    ub = 0
    lbp = 0
    ubp = 0
    lb2 = 0
    ub2 = 0
    y, y2 = 0, 0
    bijA, bklB,  teta = 0, 0, 0
    LA,  LB = F, N
    lbv,  ubv = 0, 0

    prepare_data_stop_time = time.process_time()

    seq_calc_start_time = time.process_time()

    # /*  Start  of  CLooG  code  */
    if ((LA >= 1) and (LB >= 1)):
        if ((LA >= 2) and (LB >= 2)):
            for t2 in range(-LA-LB,  -LA-LB+1,  1):
                lbp = -LB
                ubp = t2+LA
                for t4 in range(lbp,  ubp,  1):
                    for t6 in range(-t2+t4,  LA,  1):
                        for t8 in range(-t4,  LB,  1):
                            D[(-t2+t4)][t6][-t4][t8] = D[(-t2+t4)+1][t6][-t4][t8] + y
                            D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t6-1]
                                                           [-t4][t8] + y,  D[(-t2+t4)][t6][-t4][t8])
                            D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t6]
                                                           [-t4+1][t8] + y,  D[(-t2+t4)][t6][-t4][t8])
                            D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t6]
                                                           [-t4][t8-1] + y,  D[(-t2+t4)][t6][-t4][t8])
                            D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)+1][t6][-t4+1]
                                                           [t8] + ro(A[(-t2+t4)], B[-t4]),  D[(-t2+t4)][t6][-t4][t8])
                            D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t6-1][-t4]
                                                           [t8-1] + ro(A[t6], B[t8]),  D[(-t2+t4)][t6][-t4][t8])
                            D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)+1][t6-1]
                                                           [-t4][1] + bijA + y2,  D[(-t2+t4)][t6][-t4][t8])
                            D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t6][-t4+1]
                                                           [t8-1] + bklB + y2,  D[(-t2+t4)][t6][-t4][t8])
                            D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)+1][t6-1][-t4+1]
                                                           [t8-1] + bijA + bklB + teta,  D[(-t2+t4)][t6][-t4][t8])

        if ((LA >= 2) and (LB == 1)):
            for t2 in range(-LA-1,  -2,  1):
                for t6 in range(-t2-1,  LA,  1):
                    D[(-t2-1)][t6][1][1] = D[(-t2-1)+1][t6][1][1] + y
                    D[(-t2-1)][t6][1][1] = MAX(D[(-t2-1)]
                                               [t6-1][1][1] + y,  D[(-t2-1)][t6][1][1])
                    D[(-t2-1)][t6][1][1] = MAX(D[(-t2-1)][t6]
                                               [1 + 1][1] + y,  D[(-t2-1)][t6][1][1])
                    D[(-t2-1)][t6][1][1] = MAX(D[(-t2-1)][t6]
                                               [1][1 - 1] + y,  D[(-t2-1)][t6][1][1])
                    D[(-t2-1)][t6][1][1] = MAX(D[(-t2-1)+1][t6][1 + 1]
                                               [1] + ro(A[(-t2-1)], B[1]),  D[(-t2-1)][t6][1][1])
                    D[(-t2-1)][t6][1][1] = MAX(D[(-t2-1)][t6-1][1]
                                               [1 - 1] + ro(A[t6], B[1]),  D[(-t2-1)][t6][1][1])
                    D[(-t2-1)][t6][1][1] = MAX(D[(-t2-1)+1][t6-1]
                                               [1][1] + bijA + y2,  D[(-t2-1)][t6][1][1])
                    D[(-t2-1)][t6][1][1] = MAX(D[(-t2-1)][t6][1 + 1]
                                               [1 - 1] + bklB + y2,  D[(-t2-1)][t6][1][1])
                    D[(-t2-1)][t6][1][1] = MAX(D[(-t2-1)+1][t6-1][1 + 1]
                                               [1 - 1] + bijA + bklB + teta,  D[(-t2-1)][t6][1][1])

        if (LA == 1):
            for t2 in range(-LB-1,  -2,  1):
                for t8 in range(-t2 - 1,  LB,  1):
                    D[1][1][(-t2-1)][t8] = D[1 + 1][1][(-t2-1)][t8] + y
                    D[1][1][(-t2-1)][t8] = MAX(D[1][1 - 1][(-t2-1)]
                                               [t8] + y,  D[1][1][(-t2-1)][t8])
                    D[1][1][(-t2-1)][t8] = MAX(D[1][1][(-t2-1)+1]
                                               [t8] + y,  D[1][1][(-t2-1)][t8])
                    D[1][1][(-t2-1)][t8] = MAX(D[1][1][(-t2-1)]
                                               [t8-1] + y,  D[1][1][(-t2-1)][t8])
                    D[1][1][(-t2-1)][t8] = MAX(D[1 + 1][1][(-t2-1)+1]
                                               [t8] + ro(A[1], B[(-t2-1)]),  D[1][1][(-t2-1)][t8])
                    D[1][1][(-t2-1)][t8] = MAX(D[1][1 - 1][(-t2-1)]
                                               [t8-1] + ro(A[1], B[t8]),  D[1][1][(-t2-1)][t8])
                    D[1][1][(-t2-1)][t8] = MAX(D[1 + 1][1 - 1][(-t2-1)]
                                               [1] + bijA + y2,  D[1][1][(-t2-1)][t8])
                    D[1][1][(-t2-1)][t8] = MAX(D[1][1][(-t2-1)+1]
                                               [t8-1] + bklB + y2,  D[1][1][(-t2-1)][t8])
                    D[1][1][(-t2-1)][t8] = MAX(D[1 + 1][1 - 1][(-t2-1)+1]
                                               [t8-1] + bijA + bklB + teta,  D[1][1][(-t2-1)][t8])

        for t2 in range(-LA-LB+2,  min(-LA-1, -LB-1),  1):
            for t6 in range(-t2-LB,  LA,  1):
                D[(-t2-LB)][t6][LB][LB] = D[(-t2-LB)+1][t6][LB][LB] + y
                D[(-t2-LB)][t6][LB][LB] = MAX(D[(-t2-LB)][t6-1]
                                              [LB][LB] + y,  D[(-t2-LB)][t6][LB][LB])
                D[(-t2-LB)][t6][LB][LB] = MAX(D[(-t2-LB)][t6]
                                              [LB+1][LB] + y,  D[(-t2-LB)][t6][LB][LB])
                D[(-t2-LB)][t6][LB][LB] = MAX(D[(-t2-LB)][t6]
                                              [LB][LB-1] + y,  D[(-t2-LB)][t6][LB][LB])
                D[(-t2-LB)][t6][LB][LB] = MAX(D[(-t2-LB)+1][t6][LB+1]
                                              [LB] + ro(A[(-t2-LB)], B[LB]),  D[(-t2-LB)][t6][LB][LB])
                D[(-t2-LB)][t6][LB][LB] = MAX(D[(-t2-LB)][t6-1][LB]
                                              [LB-1] + ro(A[t6], B[LB]),  D[(-t2-LB)][t6][LB][LB])
                D[(-t2-LB)][t6][LB][LB] = MAX(D[(-t2-LB)+1][t6-1]
                                              [LB][1] + bijA + y2,  D[(-t2-LB)][t6][LB][LB])
                D[(-t2-LB)][t6][LB][LB] = MAX(D[(-t2-LB)][t6][LB+1]
                                              [LB-1] + bklB + y2,  D[(-t2-LB)][t6][LB][LB])
                D[(-t2-LB)][t6][LB][LB] = MAX(D[(-t2-LB)+1][t6-1][LB+1]
                                              [LB-1] + bijA + bklB + teta,  D[(-t2-LB)][t6][LB][LB])

            lbp = -LB+1
            ubp = t2+LA-1
            for t4 in range(lbp,  ubp,  1):
                for t8 in range(-t4,  LB,  1):
                    D[(-t2+t4)][(-t2+t4)][-t4][t8] = D[(-t2+t4) +
                                                       1][(-t2+t4)][-t4][t8] + y
                    D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)]
                                                         [(-t2+t4)-1][-t4][t8] + y,  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                    D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)][(-t2+t4)]
                                                         [-t4+1][t8] + y,  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                    D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)][(-t2+t4)]
                                                         [-t4][t8-1] + y,  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                    D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)+1][(-t2+t4)][-t4+1]
                                                         [t8] + ro(A[(-t2+t4)], B[-t4]),  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                    D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)][(-t2+t4)-1][-t4]
                                                         [t8-1] + ro(A[(-t2+t4)], B[t8]),  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                    D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)+1][(-t2+t4)-1]
                                                         [-t4][1] + bijA + y2,  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                    D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)][(-t2+t4)]
                                                         [-t4+1][t8-1] + bklB + y2,  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                    D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)+1][(-t2+t4)-1]
                                                         [-t4+1][t8-1] + bijA + bklB + teta,  D[(-t2+t4)][(-t2+t4)][-t4][t8])

                for t6 in range(-t2+t4+1,  LA,  1):
                    D[(-t2+t4)][t6][-t4][-t4] = D[(-t2+t4)+1][t6][-t4][-t4] + y
                    D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)][t6-1]
                                                    [-t4][-t4] + y,  D[(-t2+t4)][t6][-t4][-t4])
                    D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)][t6]
                                                    [-t4+1][-t4] + y,  D[(-t2+t4)][t6][-t4][-t4])
                    D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)][t6]
                                                    [-t4][-t4-1] + y,  D[(-t2+t4)][t6][-t4][-t4])
                    D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)+1][t6][-t4+1]
                                                    [-t4] + ro(A[(-t2+t4)], B[-t4]),  D[(-t2+t4)][t6][-t4][-t4])
                    D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)][t6-1][-t4]
                                                    [-t4-1] + ro(A[t6], B[-t4]),  D[(-t2+t4)][t6][-t4][-t4])
                    D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)+1][t6-1]
                                                    [-t4][1] + bijA + y2,  D[(-t2+t4)][t6][-t4][-t4])
                    D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)][t6][-t4+1]
                                                    [-t4-1] + bklB + y2,  D[(-t2+t4)][t6][-t4][-t4])
                    D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)+1][t6-1][-t4+1]
                                                    [-t4-1] + bijA + bklB + teta,  D[(-t2+t4)][t6][-t4][-t4])

                    for t8 in range(-t4+1,  LB,  1):
                        D[(-t2+t4)][t6][-t4][t8] = D[(-t2+t4)+1][t6][-t4][t8] + y
                        D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t6-1]
                                                       [-t4][t8] + y,  D[(-t2+t4)][t6][-t4][t8])
                        D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t6]
                                                       [-t4+1][t8] + y,  D[(-t2+t4)][t6][-t4][t8])
                        D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t6]
                                                       [-t4][t8-1] + y,  D[(-t2+t4)][t6][-t4][t8])
                        D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)+1][t6][-t4+1]
                                                       [t8] + ro(A[(-t2+t4)], B[-t4]),  D[(-t2+t4)][t6][-t4][t8])
                        D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t6-1][-t4]
                                                       [t8-1] + ro(A[t6], B[t8]),  D[(-t2+t4)][t6][-t4][t8])
                        D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)+1][t6-1]
                                                       [-t4][1] + bijA + y2,  D[(-t2+t4)][t6][-t4][t8])
                        D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t6][-t4+1]
                                                       [t8-1] + bklB + y2,  D[(-t2+t4)][t6][-t4][t8])
                        D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)+1][t6-1][-t4+1]
                                                       [t8-1] + bijA + bklB + teta,  D[(-t2+t4)][t6][-t4][t8])

                        for t10 in range(-t2+t4+1,  1):
                            for t12 in range(-t4+1,  t8,  1):
                                D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t10][-t4]
                                                               [t12] + D[t10+1][t6][t12+1][t8],  D[(-t2+t4)][t6][-t4][t8])

            for t8 in range(-t2-LA,  LB,  1):
                D[LA][LA][(-t2-LA)][t8] = D[LA+1][LA][(-t2-LA)][t8] + y
                D[LA][LA][(-t2-LA)][t8] = MAX(D[LA][LA-1][(-t2-LA)]
                                              [t8] + y,  D[LA][LA][(-t2-LA)][t8])
                D[LA][LA][(-t2-LA)][t8] = MAX(D[LA][LA][(-t2-LA)+1]
                                              [t8] + y,  D[LA][LA][(-t2-LA)][t8])
                D[LA][LA][(-t2-LA)][t8] = MAX(D[LA][LA][(-t2-LA)]
                                              [t8-1] + y,  D[LA][LA][(-t2-LA)][t8])
                D[LA][LA][(-t2-LA)][t8] = MAX(D[LA+1][LA][(-t2-LA)+1]
                                              [t8] + ro(A[LA], B[(-t2-LA)]),  D[LA][LA][(-t2-LA)][t8])
                D[LA][LA][(-t2-LA)][t8] = MAX(D[LA][LA-1][(-t2-LA)]
                                              [t8-1] + ro(A[LA], B[t8]),  D[LA][LA][(-t2-LA)][t8])
                D[LA][LA][(-t2-LA)][t8] = MAX(D[LA+1][LA-1][(-t2-LA)]
                                              [1] + bijA + y2,  D[LA][LA][(-t2-LA)][t8])
                D[LA][LA][(-t2-LA)][t8] = MAX(D[LA][LA][(-t2-LA)+1]
                                              [t8-1] + bklB + y2,  D[LA][LA][(-t2-LA)][t8])
                D[LA][LA][(-t2-LA)][t8] = MAX(D[LA+1][LA-1][(-t2-LA)+1]
                                              [t8-1] + bijA + bklB + teta,  D[LA][LA][(-t2-LA)][t8])

        if (LB >= 2):
            for t2 in range(-LA,  -LB-1,  1):
                for t6 in range(-t2-LB,  LA,  1):
                    D[(-t2-LB)][t6][LB][LB] = D[(-t2-LB)+1][t6][LB][LB] + y
                    D[(-t2-LB)][t6][LB][LB] = MAX(D[(-t2-LB)][t6-1]
                                                  [LB][LB] + y,  D[(-t2-LB)][t6][LB][LB])
                    D[(-t2-LB)][t6][LB][LB] = MAX(D[(-t2-LB)][t6]
                                                  [LB+1][LB] + y,  D[(-t2-LB)][t6][LB][LB])
                    D[(-t2-LB)][t6][LB][LB] = MAX(D[(-t2-LB)][t6]
                                                  [LB][LB-1] + y,  D[(-t2-LB)][t6][LB][LB])
                    D[(-t2-LB)][t6][LB][LB] = MAX(D[(-t2-LB)+1][t6][LB+1]
                                                  [LB] + ro(A[(-t2-LB)], B[LB]),  D[(-t2-LB)][t6][LB][LB])
                    D[(-t2-LB)][t6][LB][LB] = MAX(D[(-t2-LB)][t6-1][LB]
                                                  [LB-1] + ro(A[t6], B[LB]),  D[(-t2-LB)][t6][LB][LB])
                    D[(-t2-LB)][t6][LB][LB] = MAX(D[(-t2-LB)+1][t6-1]
                                                  [LB][1] + bijA + y2,  D[(-t2-LB)][t6][LB][LB])
                    D[(-t2-LB)][t6][LB][LB] = MAX(D[(-t2-LB)][t6][LB+1]
                                                  [LB-1] + bklB + y2,  D[(-t2-LB)][t6][LB][LB])
                    D[(-t2-LB)][t6][LB][LB] = MAX(D[(-t2-LB)+1][t6-1][LB+1]
                                                  [LB-1] + bijA + bklB + teta,  D[(-t2-LB)][t6][LB][LB])

                lbp = -LB+1
                ubp = -1
                for t4 in range(lbp,  ubp,  1):
                    for t8 in range(-t4,  LB,  1):
                        D[(-t2+t4)][(-t2+t4)][-t4][t8] = D[(-t2+t4) +
                                                           1][(-t2+t4)][-t4][t8] + y
                        D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)]
                                                             [(-t2+t4)-1][-t4][t8] + y,  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                        D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)][(-t2+t4)]
                                                             [-t4+1][t8] + y,  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                        D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)][(-t2+t4)]
                                                             [-t4][t8-1] + y,  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                        D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)+1][(-t2+t4)][-t4+1]
                                                             [t8] + ro(A[(-t2+t4)], B[-t4]),  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                        D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)][(-t2+t4)-1][-t4]
                                                             [t8-1] + ro(A[(-t2+t4)], B[t8]),  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                        D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)+1][(-t2+t4)-1]
                                                             [-t4][1] + bijA + y2,  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                        D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)][(-t2+t4)]
                                                             [-t4+1][t8-1] + bklB + y2,  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                        D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)+1][(-t2+t4)-1]
                                                             [-t4+1][t8-1] + bijA + bklB + teta,  D[(-t2+t4)][(-t2+t4)][-t4][t8])

                    for t6 in range(-t2+t4+1,  LA,  1):
                        D[(-t2+t4)][t6][-t4][-t4] = D[(-t2+t4)+1][t6][-t4][-t4] + y
                        D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)][t6-1]
                                                        [-t4][-t4] + y,  D[(-t2+t4)][t6][-t4][-t4])
                        D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)][t6]
                                                        [-t4+1][-t4] + y,  D[(-t2+t4)][t6][-t4][-t4])
                        D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)][t6]
                                                        [-t4][-t4-1] + y,  D[(-t2+t4)][t6][-t4][-t4])
                        D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)+1][t6][-t4+1]
                                                        [-t4] + ro(A[(-t2+t4)], B[-t4]),  D[(-t2+t4)][t6][-t4][-t4])
                        D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)][t6-1][-t4]
                                                        [-t4-1] + ro(A[t6], B[-t4]),  D[(-t2+t4)][t6][-t4][-t4])
                        D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)+1][t6-1]
                                                        [-t4][1] + bijA + y2,  D[(-t2+t4)][t6][-t4][-t4])
                        D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)][t6][-t4+1]
                                                        [-t4-1] + bklB + y2,  D[(-t2+t4)][t6][-t4][-t4])
                        D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)+1][t6-1][-t4+1]
                                                        [-t4-1] + bijA + bklB + teta,  D[(-t2+t4)][t6][-t4][-t4])
                        for t8 in range(-t4+1,  LB,  1):
                            D[(-t2+t4)][t6][-t4][t8] = D[(-t2+t4)+1][t6][-t4][t8] + y
                            D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t6-1]
                                                           [-t4][t8] + y,  D[(-t2+t4)][t6][-t4][t8])
                            D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t6]
                                                           [-t4+1][t8] + y,  D[(-t2+t4)][t6][-t4][t8])
                            D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t6]
                                                           [-t4][t8-1] + y,  D[(-t2+t4)][t6][-t4][t8])
                            D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)+1][t6][-t4+1]
                                                           [t8] + ro(A[(-t2+t4)], B[-t4]),  D[(-t2+t4)][t6][-t4][t8])
                            D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t6-1][-t4]
                                                           [t8-1] + ro(A[t6], B[t8]),  D[(-t2+t4)][t6][-t4][t8])
                            D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)+1][t6-1]
                                                           [-t4][1] + bijA + y2,  D[(-t2+t4)][t6][-t4][t8])
                            D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t6][-t4+1]
                                                           [t8-1] + bklB + y2,  D[(-t2+t4)][t6][-t4][t8])
                            D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)+1][t6-1][-t4+1]
                                                           [t8-1] + bijA + bklB + teta,  D[(-t2+t4)][t6][-t4][t8])
                            for t10 in range(-t2+t4+1,  t6,  1):
                                for t12 in range(-t4+1,  t8,  1):
                                    D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t10][-t4]
                                                                   [t12] + D[t10+1][t6][t12+1][t8],  D[(-t2+t4)][t6][-t4][t8])

        if (LA >= 2):
            for t2 in range(-LB,  -LA-1,  1):
                lbp = t2+1
                ubp = t2+LA-1
                for t4 in range(lbp,  ubp,  1):
                    for t8 in range(-t4,  LB,  1):
                        D[(-t2+t4)][(-t2+t4)][-t4][t8] = D[(-t2+t4) +
                                                           1][(-t2+t4)][-t4][t8] + y
                        D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)]
                                                             [(-t2+t4)-1][-t4][t8] + y,  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                        D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)][(-t2+t4)]
                                                             [-t4+1][t8] + y,  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                        D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)][(-t2+t4)]
                                                             [-t4][t8-1] + y,  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                        D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)+1][(-t2+t4)][-t4+1]
                                                             [t8] + ro(A[(-t2+t4)], B[-t4]),  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                        D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)][(-t2+t4)-1][-t4]
                                                             [t8-1] + ro(A[(-t2+t4)], B[t8]),  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                        D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)+1][(-t2+t4)-1]
                                                             [-t4][1] + bijA + y2,  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                        D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)][(-t2+t4)]
                                                             [-t4+1][t8-1] + bklB + y2,  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                        D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)+1][(-t2+t4)-1]
                                                             [-t4+1][t8-1] + bijA + bklB + teta,  D[(-t2+t4)][(-t2+t4)][-t4][t8])

                    for t6 in range(-t2+t4+1,  LA,  1):
                        D[(-t2+t4)][t6][-t4][-t4] = D[(-t2+t4)+1][t6][-t4][-t4] + y
                        D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)][t6-1]
                                                        [-t4][-t4] + y,  D[(-t2+t4)][t6][-t4][-t4])
                        D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)][t6]
                                                        [-t4+1][-t4] + y,  D[(-t2+t4)][t6][-t4][-t4])
                        D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)][t6]
                                                        [-t4][-t4-1] + y,  D[(-t2+t4)][t6][-t4][-t4])
                        D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)+1][t6][-t4+1]
                                                        [-t4] + ro(A[(-t2+t4)], B[-t4]),  D[(-t2+t4)][t6][-t4][-t4])
                        D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)][t6-1][-t4]
                                                        [-t4-1] + ro(A[t6], B[-t4]),  D[(-t2+t4)][t6][-t4][-t4])
                        D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)+1][t6-1]
                                                        [-t4][1] + bijA + y2,  D[(-t2+t4)][t6][-t4][-t4])
                        D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)][t6][-t4+1]
                                                        [-t4-1] + bklB + y2,  D[(-t2+t4)][t6][-t4][-t4])
                        D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)+1][t6-1][-t4+1]
                                                        [-t4-1] + bijA + bklB + teta,  D[(-t2+t4)][t6][-t4][-t4])
                        for t8 in range(-t4+1,  LB,  1):
                            D[(-t2+t4)][t6][-t4][t8] = D[(-t2+t4)+1][t6][-t4][t8] + y
                            D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t6-1]
                                                           [-t4][t8] + y,  D[(-t2+t4)][t6][-t4][t8])
                            D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t6]
                                                           [-t4+1][t8] + y,  D[(-t2+t4)][t6][-t4][t8])
                            D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t6]
                                                           [-t4][t8-1] + y,  D[(-t2+t4)][t6][-t4][t8])
                            D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)+1][t6][-t4+1]
                                                           [t8] + ro(A[(-t2+t4)], B[-t4]),  D[(-t2+t4)][t6][-t4][t8])
                            D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t6-1][-t4]
                                                           [t8-1] + ro(A[t6], B[t8]),  D[(-t2+t4)][t6][-t4][t8])
                            D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)+1][t6-1]
                                                           [-t4][1] + bijA + y2,  D[(-t2+t4)][t6][-t4][t8])
                            D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t6][-t4+1]
                                                           [t8-1] + bklB + y2,  D[(-t2+t4)][t6][-t4][t8])
                            D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)+1][t6-1][-t4+1]
                                                           [t8-1] + bijA + bklB + teta,  D[(-t2+t4)][t6][-t4][t8])
                            for t10 in range(-t2+t4+1,  t6,  1):
                                for t12 in range(-t4+1,  t8,  1):
                                    D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t10][-t4]
                                                                   [t12] + D[t10+1][t6][t12+1][t8],  D[(-t2+t4)][t6][-t4][t8])

                for t8 in range(-t2-LA,  LB,  1):
                    D[LA][LA][(-t2-LA)][t8] = D[LA+1][LA][(-t2-LA)][t8] + y
                    D[LA][LA][(-t2-LA)][t8] = MAX(D[LA][LA-1]
                                                  [(-t2-LA)][t8] + y,  D[LA][LA][(-t2-LA)][t8])
                    D[LA][LA][(-t2-LA)][t8] = MAX(D[LA][LA][(-t2-LA)+1]
                                                  [t8] + y,  D[LA][LA][(-t2-LA)][t8])
                    D[LA][LA][(-t2-LA)][t8] = MAX(D[LA][LA][(-t2-LA)]
                                                  [t8-1] + y,  D[LA][LA][(-t2-LA)][t8])
                    D[LA][LA][(-t2-LA)][t8] = MAX(D[LA+1][LA][(-t2-LA)+1]
                                                  [t8] + ro(A[LA], B[(-t2-LA)]),  D[LA][LA][(-t2-LA)][t8])
                    D[LA][LA][(-t2-LA)][t8] = MAX(D[LA][LA-1][(-t2-LA)]
                                                  [t8-1] + ro(A[LA], B[t8]),  D[LA][LA][(-t2-LA)][t8])
                    D[LA][LA][(-t2-LA)][t8] = MAX(D[LA+1][LA-1][(-t2-LA)]
                                                  [1] + bijA + y2,  D[LA][LA][(-t2-LA)][t8])
                    D[LA][LA][(-t2-LA)][t8] = MAX(D[LA][LA][(-t2-LA)+1]
                                                  [t8-1] + bklB + y2,  D[LA][LA][(-t2-LA)][t8])
                    D[LA][LA][(-t2-LA)][t8] = MAX(D[LA+1][LA-1][(-t2-LA)+1]
                                                  [t8-1] + bijA + bklB + teta,  D[LA][LA][(-t2-LA)][t8])

        for t2 in range(max(-LA, -LB),  -2,  1):
            lbp = t2+1
            ubp = -1

            for t4 in range(lbp,  ubp, 1):
                for t8 in range(-t4,  LB,  1):
                    D[(-t2+t4)][(-t2+t4)][-t4][t8] = D[(-t2+t4) +
                                                       1][(-t2+t4)][-t4][t8] + y
                    D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)]
                                                         [(-t2+t4)-1][-t4][t8] + y,  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                    D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)][(-t2+t4)]
                                                         [-t4+1][t8] + y,  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                    D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)][(-t2+t4)]
                                                         [-t4][t8-1] + y,  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                    D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)+1][(-t2+t4)][-t4+1]
                                                         [t8] + ro(A[(-t2+t4)], B[-t4]),  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                    D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)][(-t2+t4)-1][-t4]
                                                         [t8-1] + ro(A[(-t2+t4)], B[t8]),  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                    D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)+1][(-t2+t4)-1]
                                                         [-t4][1] + bijA + y2,  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                    D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)][(-t2+t4)]
                                                         [-t4+1][t8-1] + bklB + y2,  D[(-t2+t4)][(-t2+t4)][-t4][t8])
                    D[(-t2+t4)][(-t2+t4)][-t4][t8] = MAX(D[(-t2+t4)+1][(-t2+t4)-1]
                                                         [-t4+1][t8-1] + bijA + bklB + teta,  D[(-t2+t4)][(-t2+t4)][-t4][t8])

                for t6 in range(-t2+t4+1,  LA,  1):
                    D[(-t2+t4)][t6][-t4][-t4] = D[(-t2+t4)+1][t6][-t4][-t4] + y
                    D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)][t6-1]
                                                    [-t4][-t4] + y,  D[(-t2+t4)][t6][-t4][-t4])
                    D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)][t6]
                                                    [-t4+1][-t4] + y,  D[(-t2+t4)][t6][-t4][-t4])
                    D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)][t6]
                                                    [-t4][-t4-1] + y,  D[(-t2+t4)][t6][-t4][-t4])
                    D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)+1][t6][-t4+1]
                                                    [-t4] + ro(A[(-t2+t4)], B[-t4]),  D[(-t2+t4)][t6][-t4][-t4])
                    D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)][t6-1][-t4]
                                                    [-t4-1] + ro(A[t6], B[-t4]),  D[(-t2+t4)][t6][-t4][-t4])
                    D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)+1][t6-1]
                                                    [-t4][1] + bijA + y2,  D[(-t2+t4)][t6][-t4][-t4])
                    D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)][t6][-t4+1]
                                                    [-t4-1] + bklB + y2,  D[(-t2+t4)][t6][-t4][-t4])
                    D[(-t2+t4)][t6][-t4][-t4] = MAX(D[(-t2+t4)+1][t6-1][-t4+1]
                                                    [-t4-1] + bijA + bklB + teta,  D[(-t2+t4)][t6][-t4][-t4])
                    for t8 in range(-t4+1,  LB,  1):
                        D[(-t2+t4)][t6][-t4][t8] = D[(-t2+t4)+1][t6][-t4][t8] + y
                        D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t6-1]
                                                       [-t4][t8] + y,  D[(-t2+t4)][t6][-t4][t8])
                        D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t6]
                                                       [-t4+1][t8] + y,  D[(-t2+t4)][t6][-t4][t8])
                        D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t6]
                                                       [-t4][t8-1] + y,  D[(-t2+t4)][t6][-t4][t8])
                        D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)+1][t6][-t4+1]
                                                       [t8] + ro(A[(-t2+t4)], B[-t4]),  D[(-t2+t4)][t6][-t4][t8])
                        D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t6-1][-t4]
                                                       [t8-1] + ro(A[t6], B[t8]),  D[(-t2+t4)][t6][-t4][t8])
                        D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)+1][t6-1]
                                                       [-t4][1] + bijA + y2,  D[(-t2+t4)][t6][-t4][t8])
                        D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t6][-t4+1]
                                                       [t8-1] + bklB + y2,  D[(-t2+t4)][t6][-t4][t8])
                        D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)+1][t6-1][-t4+1]
                                                       [t8-1] + bijA + bklB + teta,  D[(-t2+t4)][t6][-t4][t8])
                        for t10 in range(-t2+t4+1,  t6,  1):
                            for t12 in range(-t4+1,  t8,  1):
                                D[(-t2+t4)][t6][-t4][t8] = MAX(D[(-t2+t4)][t10][-t4]
                                                               [t12] + D[t10+1][t6][t12+1][t8],  D[(-t2+t4)][t6][-t4][t8])

    seq_calc_stop_time = time.process_time()

    d = {
        'First dim': F,
        'Dimentions': N,
        'Prepare data': prepare_data_stop_time - prepare_data_start_time,
        'execution time': seq_calc_stop_time - seq_calc_start_time,
    }
    df = pd.DataFrame([d])
    print(df.to_string())
    df.to_csv('sankopluto.csv', mode='a', index=False, header=False)


if __name__ == '__main__':
    TYPE = 1
    if TYPE == 0:
        N = 200
        F = 2
        iters = 1
        for i in range(iters):
            action(F, N, info=i)
    if TYPE == 1:
        iters = 20
        Fs = [2, 4, 6, 8, 10, 12]
        Ns = [24, 48, 72, 96, 120, 168, 216, 240]
        for iFs in Fs:
            for jNs in Ns:
                for k_iter in range(iters):
                    action(iFs, jNs, k_iter)