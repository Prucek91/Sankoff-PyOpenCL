float ro(float A, float B) { return 0.0; }

int calc_idx(int i, int j, int k, int l, int LA, int LB) {
  int ip = LA - i + 1;
  int jp = LA - j + 1;
  int kp = LB - k + 1;
  int lp = LB - l + 1;

  int idx = (((1 + LB) * LB) / 2);
  idx *= ((ip * (ip - 1)) / 2);
  idx += ip * ((kp * (kp - 1)) / 2);
  idx += (jp - 1) * kp;
  idx += lp - 1;
  return idx;
}

__kernel void adjust_score(__global short *D, __global short *values,
                           __global short *final_data, const int M, const int N,
                           const int external_i, const int external_k,
                           const int idx) {
  // algorytm 3 str. 8/14 z artykulu

  int i = external_i;
  int k = external_k;

  int l = get_global_id(0); // x
  int j = get_global_id(1); // y

  if (l + j == idx) {

    float y = 0;

    // petle
    float element = 0;
    float y2 = 0;
    float bijA = 0;
    float bklB = 0;
    float teta = 0;
    if (i > 0 && k > 0 && l > 0 && j > 0) {
      element = D[calc_idx(i, j, k, l, M, N)];
      element =
          (D[calc_idx(i, j, k, l, M, N)] + y > D[calc_idx(i, j, k, l, M, N)])
              ? D[calc_idx(i, j, k, l, M, N)] + y
              : D[calc_idx(i, j, k, l, M, N)];
      element = (D[calc_idx(i, j, k + 1, l, M, N)] + y >
                 D[calc_idx(i, j, k, l, M, N)])
                    ? D[calc_idx(i, j, k + 1, l, M, N)] + y
                    : D[calc_idx(i, j, k, l, M, N)];
      element = (D[calc_idx(i, j, k, l - 1, M, N)] + y >
                 D[calc_idx(i, j, k, l, M, N)])
                    ? D[calc_idx(i, j, k, l - 1, M, N)] + y
                    : D[calc_idx(i, j, k, l, M, N)];
      element = (D[calc_idx(i + 1, j, k + 1, l, M, N)] + ro(0, 0) >
                 D[calc_idx(i, j, k, l, M, N)])
                    ? D[calc_idx(i + 1, j, k + 1, l, M, N)] + ro(0, 0)
                    : D[calc_idx(i, j, k, l, M, N)];
      element = (D[calc_idx(i, j - 1, k, l - 1, M, N)] + ro(0, 0) >
                 D[calc_idx(i, j, k, l, M, N)])
                    ? D[calc_idx(i, j - 1, k, l - 1, M, N)] + ro(0, 0)
                    : D[calc_idx(i, j, k, l, M, N)];
      element = (D[calc_idx(i + 1, j - 1, k, l, M, N)] + bijA + y2 >
                 D[calc_idx(i, j, k, l, M, N)])
                    ? D[calc_idx(i + 1, j - 1, k, l, M, N)] + bijA + y2
                    : D[calc_idx(i, j, k, l, M, N)];
      element = (D[calc_idx(i, j, k + 1, l - 1, M, N)] + bklB + y2 >
                 D[calc_idx(i, j, k, l, M, N)])
                    ? D[calc_idx(i, j, k + 1, l - 1, M, N)] + bklB + y2
                    : D[calc_idx(i, j, k, l, M, N)];
      element =
          (D[calc_idx(i + 1, j - 1, k + 1, l - 1, M, N)] + bijA + teta >
           D[calc_idx(i, j, k, l, M, N)])
              ? D[calc_idx(i + 1, j - 1, k + 1, l - 1, M, N)] + bijA + teta
              : D[calc_idx(i, j, k, l, M, N)];
    }

    if (D[calc_idx(i + 1, j - 1, k + 1, l - 1, M, N)] >
        D[calc_idx(i, j, k, l, M, N)]) {
      element = D[calc_idx(i + 1, j - 1, k + 1, l - 1, M, N)];
    }
    final_data[j * M + l] = element;
  }
}