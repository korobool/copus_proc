#!/usr/bin/python3

import os
import sys
import processor

if __name__ == '__main__':
    output_folder = sys.argv[1]

    os.system('mkdir -p ' + output_folder)

    ALLOWED_PUNCTUATION = (',', ';', '!', '"', ':', '-', '--')

    ALLOWED_POS = ('NOUN', 'VERB', 'ADJF', 'ADVB', 'CONJ',
                   'ADJS', 'COMP', 'INFN', 'PRTF', 'PRTS',
                   'GRND', 'NUMR', 'ADVB', 'NPRO', 'PRED',
                   'PREP', 'CONJ', 'PRCL', 'INTJ', 'ADJF',
                   'ADJC', 'ADJS', 'ADJC', 'COMP', 'ADVB',
                   'INFN', 'VREB', 'PRTF', 'ADJC', 'PRTS',
                   'ADJC', 'GRND', 'VERB', 'NUMR', 'NOUN',
                   'NPRO', 'NOUN', 'PRED', 'ADJC'
    )  # http://opencorpora.org/dict.php?act=gram

    proc = processor.CorpusProcessor(punct=ALLOWED_PUNCTUATION, pos=ALLOWED_POS)

    proc.load_stdin()

    proc.analyze(output_folder)