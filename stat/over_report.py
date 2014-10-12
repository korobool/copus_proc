from pprint import pprint
import statistics
import sys


def parse_line(line):
    spliter = line.index(' => ')
    occur = int(line[:spliter].strip())
    template = line[spliter + 4:].strip()
    return template, occur


c1 = {}
c2 = {}
c3 = {}

with open('/home/oleksandr/tmp/h4pos_1000000/0a_ordered_templates.txt') as f:
    for line in f.readlines():
        item = parse_line(line)
        c1[item[0]] = item[1]

with open('/home/oleksandr/tmp/h4pos_habra666344/0a_ordered_templates.txt') as f:
    for line in f.readlines():
        item = parse_line(line)
        c2[item[0]] = item[1]

with open('/home/oleksandr/tmp/l4pos_report_tail1000000/0a_ordered_templates.txt') as f:
    for line in f.readlines():
        item = parse_line(line)
        c3[item[0]] = item[1]

# with open('/home/oleksandr/tmp/report1000000/0a_ordered_templates.txt') as f:
#     for line in f.readlines():
#         item = parse_line(line)
#         c1[item[0]] = item[1]
#
# with open('/home/oleksandr/tmp/habra666344/0a_ordered_templates.txt') as f:
#     for line in f.readlines():
#         item = parse_line(line)
#         c2[item[0]] = item[1]
#
# with open('/home/oleksandr/tmp/report_tail1000000/0a_ordered_templates.txt') as f:
#     for line in f.readlines():
#         item = parse_line(line)
#         c3[item[0]] = item[1]


norm1 = statistics.stdev(c1.values())
norm2 = statistics.stdev(c2.values())
norm3 = statistics.stdev(c3.values())

set_c1 = set(c1.keys())
set_c2 = set(c2.keys())
set_c3 = set(c3.keys())

intersect = set_c1 & set_c2 & set_c3

table = {}

for item in intersect:
    table[item] = [c1[item] / norm1, c2[item] / norm2, c3[item] / norm3]

# pprint(table)

items = []

for k, v in table.items():
    # print(k, v)
    items.append((k, v))

items.sort(key=lambda entry: entry[1][0] + entry[1][1]  # reverse=True)
                             + entry[1][2], reverse=True)


def report():
    for i in items:
        yield ((i[1][0] + i[1][1] + i[1][2]) / 3, i[1][0], i[1][1], i[1][2])

if len(sys.argv) > 0:
    with open(sys.argv[1], 'w') as report:
        for i in items:
            report.write('{0},{1},{2},{3}'.format(repr(i[0]), i[1][0], i[1][1], i[1][2]) + '\n')

from plot_report import plot_rep

plot_rep(list(report()))

# pprint(list(report()))