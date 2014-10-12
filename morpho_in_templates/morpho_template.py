import sys
import os
import re

folder = sys.argv[1]


def list_template_files(f):
    for file in os.listdir(f):
        if file.endswith(')'):
            yield file


def get_setnence_metainfo(sentence):
    words = filter(lambda w: len(w) > 0, re.split(' \\\n'))
    meta = []
    for word in words:
        yield get_word_metainfo(word)



def process_file(data):
    for sentence in data:
        metainfo = get_setnence_metainfo(sentence)
        yield metainfo

for filename in list_template_files(folder):
    with open(os.path.join(folder, filename)) as tplfile:
        metainfos = set(list(process_file(tplfile.read())))

