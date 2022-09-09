import os
import subprocess

filename = 'binarka'

Fs = [2,4,6,8,10,12]
Ns = [24, 48,72, 96, 120, 168, 216, 240]

for k in range(1):
    for j in Ns:
        for i in Fs:
            arg1 = str(i)
            arg2 = str(j)
            proc = subprocess.Popen(["./binarka", arg1, arg2])
            proc.wait()