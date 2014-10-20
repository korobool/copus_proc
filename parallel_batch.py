import subprocess
import sys
import time
import multiprocessing as mp

import os


def process_file(path):
    print("PID: {}, file: {}".format(os.getpid(), path))

    filename = path.split('/')
    filename = filename[len(filename)-1]
    print(subprocess.Popen('python3 find_templates.py ./report/{0} < {1}'.format(filename, path),
                           shell=True).communicate())
    time.sleep(1)
 
if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        file_list = f.read().splitlines()
   
    cores = os.popen('grep "cpu cores" /proc/cpuinfo | head -n1 | awk \'{print $4;}\'').read().rstrip()
    with mp.Pool(processes=int(cores)) as pool:
        pool.map(process_file, file_list)