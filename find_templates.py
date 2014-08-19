import os
import sys
import processor

if __name__ == '__main__':

    corpuse_folder = sys.argv[1]
    output_folder = sys.argv[2]

    print(corpuse_folder, output_folder)

    if not os.path.exists(corpuse_folder):
        print('Input data strictly required.')
        exit(1)

    os.system('mkdir -p ' + output_folder)

    ALLOWED_PUNCTUATION = (',', ';', '!', '"', ':')
    # ALLOWED_POS = ('NOUN', 'VERB', 'ADJF', 'INFN', 'PRTF', 'ADVB', 'CONJ')
    ALLOWED_POS = ('NOUN', 'VERB', 'ADJF', 'ADVB', 'CONJ')

    processor = processor.CorpusProcessor(punct=ALLOWED_PUNCTUATION, pos=ALLOWED_POS)

    processor.load_habra(corpuse_folder)

    processor.analyze(output_folder)