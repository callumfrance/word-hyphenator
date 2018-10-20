#!/usr/bin/python3
import re

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

prefixes = {
    '.a' : [], '.b' : [], '.c' : [], '.d' : [], '.e' : [], '.f' : [], '.g' : [],
    '.h' : [], '.i' : [], '.j' : [], '.k' : [], '.l' : [], '.m' : [], '.n' : [],
    '.o' : [], '.p' : [], '.q' : [], '.r' : [], '.s' : [], '.t' : [], '.u' : [],
    '.v' : [], '.w' : [], '.x' : [], '.y' : [], '.z' : [],
}
word_bites = {
    'a' : [], 'b' : [], 'c' : [], 'd' : [], 'e' : [], 'f' : [], 'g' : [],
    'h' : [], 'i' : [], 'j' : [], 'k' : [], 'l' : [], 'm' : [], 'n' : [],
    'o' : [], 'p' : [], 'q' : [], 'r' : [], 's' : [], 't' : [], 'u' : [],
    'v' : [], 'w' : [], 'x' : [], 'y' : [], 'z' : [],
}
suffixes = {
    'a.' : [], 'b.' : [], 'c.' : [], 'd.' : [], 'e.' : [], 'f.' : [], 'g.' : [],
    'h.' : [], 'i.' : [], 'j.' : [], 'k.' : [], 'l.' : [], 'm.' : [], 'n.' : [],
    'o.' : [], 'p.' : [], 'q.' : [], 'r.' : [], 's.' : [], 't.' : [], 'u.' : [],
    'v.' : [], 'w.' : [], 'x.' : [], 'y.' : [], 'z.' : [],
}
with open('patterns.txt') as fo:
    for line in fo:
        line = line.rstrip()
        if line.endswith('.'):
            re.sub(r"[^a-zA-Z]+", '', line)
        elif line.startswith('.'):
            pass
        else:
            pass
