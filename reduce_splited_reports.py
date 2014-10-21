from pprint import pprint
import sys
from os.path import exists
import re
import statistics


def get_data_from_report(file_name, norm=True):
    data = []
    with open(file_name, 'r') as file:
        for line in file.readlines():
            items = re.split(' => ', line.strip())
            if len(items) == 2:
                data.append([items[1], int(items[0])])
    if norm:
        vals = [val[1] for val in data]

        stddev = statistics.stdev(vals)
        for item in data:
            item[1] = item[1] / stddev
    return data

filelist = map(lambda f: f.strip(), open(sys.argv[1], 'r').readlines())

common_dict = {}

for file in filelist:
    if exists(file):
        for i in get_data_from_report(file, norm=False):
            if i[0] in common_dict:
                common_dict[i[0]] += i[1]
            else:
                common_dict[i[0]] = i[1]

#pprint(common_dict)

common_data = sorted(common_dict.items(), key=lambda item: item[1], reverse=True)

for line in common_data:
    print('{0}\t{1}'.format(line[0], line[1]))



