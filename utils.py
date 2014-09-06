import os
import re
import yaml


def replace_punctuation(sentence):
    line = sentence
    replacements = {',': ' , ',
                    '!': ' ! ',
                    '\)': ' ) ',
                    '\(': ' ( ',
                    '\[': ' [ ',
                    '\]': ' ] ',
                    ':': ' : ',
                    '--': ' - '
                    # r'[\s]+': ' ',
                    # r'[\t]+': ' ',

    }
    for replacement in replacements:
        line = re.sub(replacement, replacements[replacement], line)
    return line


def preprocess(text):
    # FIXME: Select more appropriate substitutions (probably EMPTY ?)
    substitutions = {
        '\s[м|М][\.]*[ж|Ж][\.]*\s': ' туалет ',
        '\sт[\.]*п[\.]*\s': '',  # ' тому подобное ',
        '\sт[\.]*д[\.]*\s': '',  # ' так далее ',
        '\sт[\.]*е[\.]*\s': '',  # ' то есть ',
        '\sт[\.]*к[\.]*\s': '',  # ' так как ',
        '\sч[\.]*т[\.]*д[\.]*\s': '',  # что и требовалось доказать ',
        '-\n': ' ',
        '\n': ' ',
        '\r': '',
        r'\\': '',
        r'[\s]+': ' ',
        r'[\t]+': ' ',

    }
    txt = text.lower()
    for subst in substitutions:
        txt = re.sub(subst, substitutions[subst], txt)

    return txt


def enum_files(input_path):
    for dirname, dirnames, filenames in os.walk(input_path):
        for filename in filenames:
            yield os.path.join(dirname, filename)


