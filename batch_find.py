import subprocess
import sys

import sys
import os


def launch_worker(path):
    filename = path.split('/')
    filename = filename[len(filename)-1]

    # os.system('mkdir {}'.format(filename))
    subprocess.Popen('python3 {0} {1} < {2}'.format('find_templates.py', filename, path), shell=True)


for line in sys.stdin:
    launch_worker(line)