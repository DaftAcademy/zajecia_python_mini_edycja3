def get_words_from_line(line):
    last = line.split('/')[-1]
    name = last.split('.')[0]
    words = set()
    begin = 0
    end = 0
    in_word = False
    for i in range(len(name)):
        if name[i].isalpha():
            if not in_word:
                in_word = True
                begin = i
        else:
            if in_word:
                in_word = False
                end = i
                words.add(name[begin:end])
    if in_word:
        words.add(name[begin:])
    return words


def get_words(file_name):
    words = set()
    with open(file_name, 'r') as f:
        for line in f:
            line_words = get_words_from_line(line)
            words |= line_words
    words = list(words)
    words.sort()
    return words

with open('wikipedia_slowa.txt', 'w') as f:
    words = get_words('html.lst')
    f.writelines((w+'\n' for w in words))
