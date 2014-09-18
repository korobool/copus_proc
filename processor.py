import sys
import pymorphy2
from utils import *


class CorpusProcessor():
    def __init__(self, punct=(), pos=None, max_length=100):
        self.punct = punct
        self.pos = pos
        self.morph = pymorphy2.MorphAnalyzer()
        self.pos_templates = {}
        self.max_length = max_length

    def _megre_pos(self, parsed_pos):
        # http://opencorpora.org/dict.php?act=gram
        substitutons ={
            'ADJF': 'ADJC',  # ADJC - common class for ADJF and ADJS
            'ADJS': 'ADJC',
            'COMP': 'ADVB',
            # 'INFN': 'VREB',
            'PRTF': 'ADJC',
            'PRTS': 'ADJC',
            'GRND': 'VERB',
            'NUMR': 'NOUN',
            'NPRO': 'NOUN',
            'PRED': 'ADJC'
        }
        if parsed_pos in substitutons:
            return substitutons[parsed_pos]
        return parsed_pos

    def _pos_tag_rus(self, sentence):
        words = filter(lambda w: len(w) > 0, re.split('[\s\.\n]', replace_punctuation(sentence)))
        tags = []

        for w in words:
            parsed = self.morph.parse(w)

            if w in self.punct:
                tags.append(w)
            else:
                parsed_pos = str(parsed[0].tag.POS)
                parsed_pos = self._megre_pos(parsed_pos)
                if parsed_pos in self.pos:
                    tags.append(parsed_pos)
                else:
                    tags.append('XXXX')
        return tuple(tags)

    def _load_sentence(self, line):
        if len(line) <= self.max_length:
            pos_tagged = self._pos_tag_rus(line)
            if pos_tagged in self.pos_templates:
                self.pos_templates[pos_tagged].append(line)
            else:
                self.pos_templates[pos_tagged] = [line]

    def load_stdin(self):
        for line in sys.stdin:
            self._load_sentence(line)

    def analyze(self, report_path='./'):

        os.system('mkdir -p {}'.format(report_path))
        report = os.path.join(report_path, 'report.txt')

        pr = (lambda template: len(set(template)-set(self.punct)) > 4 and not 'XXXX' in set(template))

        with open(report, 'w') as outfile:
            for val in self.pos_templates:
                # print()
                if pr(val):
                    outfile.write(str(len(self.pos_templates[val])) + ' => ' + repr(val) + '\n')
                    try:
                        with open(os.path.join(report_path, str(val)), 'a') as f:
                            f.write(repr(self.pos_templates[val]))
                    except Exception as ex:
                        print('Cannot process file: {}'.format(ex))
        # sort -k1.1n report.txt | tac > 0a_ordered_templates.txt
        os.system('cd {} && sort -k1.1n report.txt | tac > 0a_ordered_templates.txt'.format(report_path))

