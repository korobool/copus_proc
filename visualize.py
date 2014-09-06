from pprint import pprint
import statistics
import sys
import re


# def trend_from_file(file_name, norm=True):
#     items = []
#     with open(file_name, 'r') as file:
#         for line in file.readlines():
#             items = re.split(' => ', line.strip())
#             items.append((items[1], int(items[0])))
#     if norm:
#         vals = [val[1] for val in items]
#
#         stddev = statistics.stdev(vals)
#         for item in items:
#             item[1] = item[1] / stddev
#     return items  # tuple


# load
file_names = sys.argv[1:]
data = {}

for name in file_names:
    data[name] = trend_from_file(name)

pprint(data)

# def get_common_keys(*args):
#     common = set(args[0])
#     for lst in args[1:]:
#         common = common & set(lst)
#     for item in args[0]:
#         if item in common:
#             yield item

# common_keys = get_common_keys(*data.values())

# print(len(common_keys), len(list(data.values())[0]))
# for key in common_keys:
#     print(list(data.values())[0][key])