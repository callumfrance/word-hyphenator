#!/usr/bin/python3
import re
from string import ascii_lowercase

"""
First, finds the maximum size of a 'subword' for each letter of the alphabet
"""
al = [0] * 26
with open('patterns.txt') as fo:
    for index, line in enumerate(fo):
        line = re.sub(r"[^A-Za-z]+", '', line)
        for letin, letter in enumerate(ascii_lowercase):
            if line[0] == letter:
                if len(line) > al[letin]:
                    al[letin] = len(line)
                break
print(al)

al_l = [None] * 26
for i, letter in enumerate(al):
    al_l[i] = [None] * al[i]
    for i2, x in enumerate(al_l[i]):
        al_l[i][i2] = list()
print(al_l)

"""
Creates a dictionary of lists of lists for each letter of the alphabet, where
each nested nested list represents the length of a subword, and each nested
list represents words that begin/end with the corresponding letter.
"""
prefixes = {
        '.a' : al_l[0], '.b' : al_l[1], '.c' : al_l[2],
        '.d' : al_l[3], '.e' : al_l[4], '.f' : al_l[5],
        '.g' : al_l[6], '.h' : al_l[7], '.i' : al_l[8],
        '.j' : al_l[9], '.k' : al_l[10], '.l' : al_l[11],
        '.m' : al_l[12], '.n' : al_l[13], '.o' : al_l[14],
        '.p' : al_l[15], '.q' : al_l[16], '.r' : al_l[17],
        '.s' : al_l[18], '.t' : al_l[19], '.u' : al_l[20],
        '.v' : al_l[21], '.w' : al_l[22], '.x' : al_l[23],
        '.y' : al_l[24], '.z' : al_l[25],
}
subwords = {
        'a' : al_l[0], 'b' : al_l[1], 'c' : al_l[2],
        'd' : al_l[3], 'e' : al_l[4], 'f' : al_l[5],
        'g' : al_l[6], 'h' : al_l[7], 'i' : al_l[8],
        'j' : al_l[9], 'k' : al_l[10], 'l' : al_l[11],
        'm' : al_l[12], 'n' : al_l[13], 'o' : al_l[14],
        'p' : al_l[15], 'q' : al_l[16], 'r' : al_l[17],
        's' : al_l[18], 't' : al_l[19], 'u' : al_l[20],
        'v' : al_l[21], 'w' : al_l[22], 'x' : al_l[23],
        'y' : al_l[24], 'z' : al_l[25],
}
suffixes = {
        'a.' : al_l[0], 'b.' : al_l[1], 'c.' : al_l[2],
        'd.' : al_l[3], 'e.' : al_l[4], 'f.' : al_l[5],
        'g.' : al_l[6], 'h.' : al_l[7], 'i.' : al_l[8],
        'j.' : al_l[9], 'k.' : al_l[10], 'l.' : al_l[11],
        'm.' : al_l[12], 'n.' : al_l[13], 'o.' : al_l[14],
        'p.' : al_l[15], 'q.' : al_l[16], 'r.' : al_l[17],
        's.' : al_l[18], 't.' : al_l[19], 'u.' : al_l[20],
        'v.' : al_l[21], 'w.' : al_l[22], 'x.' : al_l[23],
        'y.' : al_l[24], 'z.' : al_l[25],
}
"""
Goes through the patterns file and places the subwords into their appropriate
slot in prefixes, suffixes, or subwords
"""
with open('patterns.txt') as fo:
    for line in fo:
        line = line.rstrip()
        if line.endswith('.'):
            size = len(re.sub(r"[^a-zA-Z]+", '', line))
            suffixes[line[-2:]][size-1].append(line)
        elif line.startswith('.'):
            size = len(re.sub(r"[^a-zA-Z]+", '', line))
            prefixes[line[:2]][size-1].append(line)
        else:
            true_subword = re.sub(r"[^a-zA-Z]+", '', line)
            size = len(true_subword)
            subwords[true_subword[:1]][size-1].append(line)

"""
Now reading in the words that need to be hyphenated
"""
user_word_list = list()
with open('words_to_hyphenate.txt') as fi:
    for line in fo:
        user_word_list.append(line.rstrip())


for wo in user_word_list:
    """
    our matching subwords dataset needs to be a list of lists, because the
    position within the words is important
    e.g. banana, lillies
    """
    match_subwords = list()
    end_a = wo[-1]
    for wo_i, wo_a in wo:
        max_rem_l = len(wo) - i + 1
        if wo_i == 0:
            if max_rem_l >= len(prefixes[wo_i]): # do them all
                pass
            else:
                pass
        # look at subwords here that dont violate length
        # look at suffixes that dont violate length left here
        for suf in suffixes[end_a][max_rem_l]:
            if
