import numpy as np
import pyopencl as cl
import pyopencl
import time
import order as o
import pandas as pd


def MAX(a, b):
    return max(a, b)


def ro(a, b):
    return 0


def action(F, N, info=0):

    prepare_data_start_time = time.process_time()
    D = np.random.randint(low=1, high=5, size=(F, N, N, N)).astype(np.int8)
    matrix = np.random.rand(N, N).astype('float32')

    # prepare memory for final answer from OpenCL
    D1 = np.zeros_like(D)
    final = np.zeros_like(matrix)

    prepare_data_stop_time = time.process_time()

    # opencl
    #print('load program from cl source file')
    f = open('adjust_score.cl', 'r', encoding='utf-8')
    kernels = ''.join(f.readlines())
    f.close()

    #print('create context')
    #ctx = cl.create_some_context()
    create_ctx_start_time = time.process_time()

    platform = pyopencl.get_platforms()[0]
    devices = platform.get_devices()
    ctx = pyopencl.Context(devices)

    create_ctx_stop_time = time.process_time()

    #print('create command queue')
    ctx_queue_start_time = time.process_time()

    queue = cl.CommandQueue(
        ctx, properties=cl.command_queue_properties.PROFILING_ENABLE)

    ctx_queue_stop_time = time.process_time()

    #print('prepare device memory for input / output')

    upload_data_start_time1 = time.process_time()

    dev_D_matrix = cl.Buffer(ctx, cl.mem_flags.READ_ONLY |
                             cl.mem_flags.COPY_HOST_PTR, hostbuf=D)
    dev_matrix = cl.Buffer(ctx, cl.mem_flags.READ_ONLY |
                           cl.mem_flags.COPY_HOST_PTR, hostbuf=matrix)
    dev_final = cl.Buffer(ctx, cl.mem_flags.WRITE_ONLY, final.nbytes)

    upload_data_stop_time1 = time.process_time()

    #print('compile kernel code')
    compile_kernel_start_time = time.process_time()
    prg = cl.Program(ctx, kernels).build()
    compile_kernel_stop_time = time.process_time()

    # ## calculations

    res = o.order(input=np.arange(
        D.shape[0] * D.shape[1]), vmax=D.shape[0], hmax=D.shape[1])
    indices_order = [np.where(res == i) for i in range(N**2)]
    indices_order = indices_order[:D.shape[0]*D.shape[1]]

    upload_data_time = 0
    opencl_execution_time = 0
    download_data_time = 0

    for i in indices_order:
        idx_i, idx_k = i[0][0], i[1][0]
        matrix = D[idx_i][idx_k]
        final = np.zeros_like(matrix)
        upload_time = time.process_time()

        dev_matrix = cl.Buffer(ctx, cl.mem_flags.READ_ONLY |
                               cl.mem_flags.COPY_HOST_PTR, hostbuf=matrix)
        dev_final = cl.Buffer(ctx, cl.mem_flags.WRITE_ONLY, final.nbytes)

        upload_data_time += time.process_time() - upload_time

        opencl_start = time.process_time()
        for j in range(N-1):
            evt = prg.adjust_score(queue, (N, N), (1, 1),
                                   dev_D_matrix,
                                   dev_matrix, dev_final,
                                   np.int32(N), np.int32(N),
                                   np.int32(idx_i), np.int32(idx_k),
                                   np.int32(j))
            evt.wait()
        opencl_execution_time += time.process_time() - opencl_start

        download_time = time.process_time()

        cl.enqueue_copy(queue, final, dev_final).wait()

        download_data_time += time.process_time() - download_time

        D1[idx_i][idx_k] = final

    d = {
        'Device name': devices[0],
        'First dim': F,
        'Dimentions': N,
        'prepare data': prepare_data_stop_time - prepare_data_start_time,
        'create ctx': create_ctx_stop_time - create_ctx_start_time,
        'create command queue': ctx_queue_stop_time - ctx_queue_start_time,
        'first data upload': upload_data_stop_time1 - upload_data_start_time1,
        'kernel compile': compile_kernel_stop_time - compile_kernel_start_time,
        'upload data time': upload_data_time,
        'download data time': download_data_time,
        'opencl execution time': opencl_execution_time,
    }

    #df = pd.DataFrame([d])
    # print(pd.Series(d).to_string())

    df = pd.DataFrame([d])

    def f(x):
        res = x
        try:
            res = np.round_(x, decimals=5)
        except:
            pass
        return res
    df = df.applymap(f)
    df.to_csv('ocl.csv', mode='a', index=False, header=False)
    print(df[['First dim', 'Dimentions', 'opencl execution time']].to_string())


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