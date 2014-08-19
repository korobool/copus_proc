import pymorphy2
from utils import *


class CorpusProcessor():
    def __init__(self, punct=(), pos=None):
        self.punct = punct
        self.pos = pos
        self.morph = pymorphy2.MorphAnalyzer()
        self.pos_templates = {}

    def _pos_tag_rus(self, sentence):
        words = filter(lambda w: len(w) > 0, re.split('[\s\.\n]', replace_punctuation(sentence)))
        tags = []

        for w in words:
            parsed = self.morph.parse(w)

            if w in self.punct:
                tags.append(w)
            else:
                parsed_pos = str(parsed[0].tag.POS)
                if parsed_pos in self.pos:
                    tags.append(parsed_pos)
        return tuple(tags)



    def load_habra(self, input_path, max_length=100):
        files_list = enum_files(input_path)
        sentences = list(get_rus_sentences_flom_habra_files_list(files_list))
        for i, sentence in enumerate(sentences):
            if len(sentence) <= max_length:
                pos_tagged = self._pos_tag_rus(sentence)
                print(i, repr(pos_tagged), sentence)
                if pos_tagged in self.pos_templates:
                    self.pos_templates[pos_tagged].append(sentence)
                else:
                    self.pos_templates[pos_tagged] = [sentence]

    def load_pocket_lib(self, input_path):

        pass

    def load_opencorpora(self, input_path):
        pass

    def analyze(self, report_path='./'):
        os.system('mkdir -p {}'.format(report_path))
        with open(os.path.join(report_path, 'report.txt'), 'w') as outfile:
            for val in self.pos_templates:
                outfile.write(str(len(self.pos_templates[val])) + ' => ' + repr(val) + '\n')
                with open(os.path.join(report_path, repr(val)), 'a') as f:
                    f.write(repr(self.pos_templates[val]))
        os.system('sort -k1.1n report.txt | tac > 0a_ordered_templates.txt')




