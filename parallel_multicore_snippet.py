import os, sys, time
import multiprocessing as mp

def process_file(file):
    print("PID: {}, file: {}".format(os.getpid(), file))
    time.sleep(5)

if __name__ == '__main__':
    with open('mylist') as f:
        file_list = f.read().splitlines()
    
    cores_per_node = os.popen('grep "cpu cores" /proc/cpuinfo | head -n1 | awk \'{print $4;}\'').read().rstrip()
    nodes = os.popen('grep "physical id" /proc/cpuinfo | awk \'{print $4;}\' | sort | tail -1').read().rstrip()
    cores = int(cores_per_node)*(int(nodes) + 1)
    with mp.Pool(processes=cores) as pool:
        pool.map(process_file, file_list)
