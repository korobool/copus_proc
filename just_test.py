import utils

files = utils.enum_files('/home/oleksandr/corpuses/habrahubs')

for item in utils.get_rus_sentences_flom_habra_files_list(files):
    print(item)