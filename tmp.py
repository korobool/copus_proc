import sys
from utils import enum_files

for file in enum_files(sys.argv[1]):
    print(file)