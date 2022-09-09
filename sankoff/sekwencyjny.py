import numpy as np
import time
import pandas as pd


def MAX(a, b):
    return max(a, b)


def ro(a, b):
    return 0


def tau(Ai, Aj, Bk, Bl):
    return 0


def action(F, N, info=0):
    prepare_data_start_time = time.process_time()
    D = np.random.randint(low=1, high=5, size=(
        F+5, N+5, N+5, N+5)).astype(np.int8)
    D1 = np.zeros_like(D)
    LA, LB = F, N
    y, y2 = 0, 0
    bijA = 0
    bijB = 0
    bklB = 0
    teta = 0
    A = np.arange(N)
    B = np.arange(N)

    prepare_data_stop_time = time.process_time()

    seq_calc_start_time = time.process_time()

    for i in range(LA+1, -1, -1):
        for k in range(LB, -1, -1):
            for j in range(i, LA, 1):
                for l in range(k, LB, 1):
                    d = D[i+1][j][k][l] + y
                    d = MAX(d, D[i][j-1][k][l]+y)
                    d = MAX(d, D[i][j][k+1][l]+y)
                    d = MAX(d, D[i][j][k][l-1]+y)
                    d = MAX(d, D[i+1][j][k+1][l] + ro(A[i], B[k]))
                    d = MAX(d, D[i][j-1][k][l-1] + ro(A[j], B[l]))
                    d = MAX(d, D[i+1][j-1][k][l] + bijA + np.dot(y, 2))
                    d = MAX(d, D[i][j][k+1][l-1] + bklB + np.dot(y, 2))
                    d = MAX(d, D[i+1][j-1][k+1][l-1]+bijA +
                            bklB + tau(A[i], A[j], B[k], B[l]))
                    for m in range(i+1, j, 1):
                        for n in range(k+1, l, 1):
                            d = MAX(d, D[i][m][k][n] + D[m+1][j][n+1][l])
                    D[i][j][k][l] = d

    seq_calc_stop_time = time.process_time()

    d = {
        'First dim': F,
        'Dimentions': N,
        'Prepare data': prepare_data_stop_time - prepare_data_start_time,
        'execution time': seq_calc_stop_time - seq_calc_start_time,
    }
    df = pd.DataFrame([d])
    print(df.to_string())
    df.to_csv('seq.csv', mode='a', index=False, header=False)


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
