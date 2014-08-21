#!/usr/bin/python3

import sys
from utils import *


def get_rus_sentences_flom_files_list(files_list):
    for file in files_list:
        try:
            text = open(file).read()
            #text = preprocess(text)
            matches = re.finditer(r'[А-Я][А-Яа-я\s\n,!-]+\.', text)
            for m in matches:
                multiline = m.group(0)
                step1 = re.sub('-\n', '', multiline)
                step2 = re.sub('\n', ' ', step1)

                yield step2
        except:
            print(file, 'cannot be processed')


def enumerate_habra(input_path):
    files_list = enum_files(input_path)
    sentences = get_rus_sentences_flom_files_list(files_list)
    for i, sentence in enumerate(sentences):
        print(sentence)


if __name__ == '__main__':
    enumerate_habra(sys.argv[1])