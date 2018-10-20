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

all_match_subwords = list() # a list of all given words matching subwords
for wo in user_word_list:
    """
    our matching subwords dataset needs to be a list of lists, because the
    position within the words is important
    e.g. banana, lillies
    """
    match_subwords = [None] * len(wo)
    end_a = wo[-1]
    for wo_i, wo_a in wo:
        max_rem_l = len(wo) - i + 1
        """
            Prefixes
        """
        if wo_i == 0:
            if max_rem_l >= len(prefixes["."+wo_i]): # do them all
                for sw_size, sw_val in enumerate(prefixes["."+wo_a]):
                    for pre_sw_sized in prefixes["."+wo_a][sw_size]:
                        if wo[:sw_size+1] == re.sub(r"[^a-zA-Z]+", '', pre_sw_sized):
                            match_subwords[wo_i].append(wo[:sw_size+1]
            else:
                for sw_size, sw_val in enumerate(prefixes["."+wo_a]):
                    if max_rem_l < sw_size+1: # sw_size is 0-based
                        pass  # ignore cases where we have less letters than sw's need
                    else:
                        for pre_sw_sized in prefixes["."+wo_a][sw_size]:
                            if wo[:sw_size+1] == re.sub(r"[^a-zA-Z]+", '', pre_sw_sized):
                                match_subwords[wo_i].append(wo[:sw_size+1]
        """
            Subwords
        """
        if max_rem_l >= len(subwords[wo_i]): # do them all
            for sw_size, sw_val in enumerate(subwords[wo_a]):
                for pre_sw_sized in subwords[wo_a][sw_size]:
                    if wo[wo_i:] == re.sub(r"[^a-zA-Z]+", '', pre_sw_sized):
                        match_subwords[wo_i].append(wo[:sw_size+1]
        else:
            for sw_size, sw_val in enumerate(subwords[wo_a]):
                if max_rem_l < sw_size+1: # sw_size is 0-based
                    pass  # ignore cases where we have less letters than sw's need
                else:
                    for pre_sw_sized in subwords[wo_a][sw_size]:
                        if wo[wo_i:] == re.sub(r"[^a-zA-Z]+", '', pre_sw_sized):
                            match_subwords[wo_i].append(wo[:sw_size+1]
        """
            Suffixes
        """
        if max_rem_l <= len(suffixes[end_a+"."]):
            for sw_size, sw_val in enumerate(suffixes[end_a+"."]):
                if max_rem_l < sw_size+1: # sw_size is 0-based
                    pass  # ignore cases where we have less letters than sw's need
                else:
                    for pre_sw_sized in suffixes[end_a+"."][sw_size]:
                        if wo[wo_i:] == re.sub(r"[^a-zA-Z]+", '', pre_sw_sized):
                            # need to clean up match_subwords
                            match_subwords[wo_i].append(wo[:sw_size+1]

    all_match_subwords.extend(match_subwords)
    print(match_subwords)

"""
Selection of the actual hyphenated combos from the match_word list.
"""
final_words = list()
for wo_index, wo in enumerate(user_word_list):
    hyphen_scores = [0] * len(wo)
    # for m_sws in all_match_subwords[wo_index]:  #iterate matching swords for one word
    for m_sws in all_match_subwords[wo_index]:
        for mw_chr in m_sws:  # iterate characters of one subword
            if mw_chr.isnumeric():
                if int(mw_chr) > hyphen_scores[0000]:
                    hyphen_scores[0000] = int(mw_chr)
            elif mw_chr.isalpha():
                pass

    final_words.append(".......")

with open("output.txt", "w+") as answers:
    for i in final_words:
        answers.write(final_words[i])
