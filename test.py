import pymorphy2


# Strips the newline character
def to_nominative(word):
    try:
        pL = morph.parse(word)
        p = pL[0]
        inflect = p.inflect({'nomn'})
        if ('Geox' in p.tag):
            return inflect.word + "(" + p.tag.POS + ")"
        return ""
    except Exception:
        return word


morph = pymorphy2.MorphAnalyzer()

file1 = open('./data/input.txt', 'r', encoding="utf-8")
Lines = file1.readlines()

count = 0
for line in Lines:
    line = line.replace('"', '')
    # line = line.replace('«', '')
    # line = line.replace('»', '')
    words = line.split()
    new_line = ''

    for word in words:
        tmp_str = to_nominative(word)
        if (len(tmp_str) != 0):
            new_line = new_line + " " + tmp_str

    print(line)
    print(new_line)
