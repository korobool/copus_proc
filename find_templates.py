#!/usr/bin/python3

import os
import sys
import processor

if __name__ == '__main__':
    output_folder = sys.argv[1]

    os.system('mkdir -p ' + output_folder)

    ALLOWED_PUNCTUATION = (',', ';', '!', '"', ':', '-', '--')

    ALLOWED_POS = (
        'PREP', 'ADVB', 'PRCL', 'ADJC', 'INFN', 'NPRO',
        'PRED', 'INTJ', 'NUMR', 'COMP', 'CONJ', 'VERB',
        'NOUN', 'ADJF', 'ADJS', 'PRTF', 'PRTS', 'GRND'
    )  # http://opencorpora.org/dict.php?act=gram

    proc = processor.CorpusProcessor(punct=ALLOWED_PUNCTUATION, pos=ALLOWED_POS)

    proc.load_stdin()

    proc.analyze(output_folder)