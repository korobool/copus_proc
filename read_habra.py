#!/usr/bin/python3

import sys
from utils import *


def get_rus_sentences_flom_habra_files_list(files_list):
    for file in files_list:
        try:
            text = yaml.load(open(file).read())['text']
            #text = preprocess(text)
            matches = re.finditer(r'[А-Я][А-Яа-я\s\n,-]+[\.|!|?]', text)
            for m in matches:
                multiline = m.group(0)
                line = re.sub('-\n', '', multiline)
                line = re.sub('\n', ' ', line)
                line = re.sub('[-]+', '-', line)
                line = re.sub('[\s]+', ' ', line)
                line = re.sub('[\t]+', ' ', line)
                line = re.sub('[,] -', ', ', line)
                line = re.sub('[:] -', ': ', line)
                yield line
        except:
            pass  # print(file, 'cannot be processed')


def enumerate_habra(input_path):
    files_list = enum_files(input_path)
    sentences = get_rus_sentences_flom_habra_files_list(files_list)
    for i, sentence in enumerate(sentences):
        print(sentence)


if __name__ == '__main__':
    enumerate_habra(sys.argv[1])