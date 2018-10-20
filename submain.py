#!/usr/bin/python3
import re
from string import ascii_lowercase

if __name__ == '__main__':
    alpha_list = [0] * 26
    with open('patterns.txt') as fo:
        for index, line in enumerate(fo):
            line = re.sub(r"[^A-Za-z]+", '', line)
            for letin, letter in enumerate(ascii_lowercase):
                if line[0] == letter:
                    if len(line) > alpha_list[letin]:
                        alpha_list[letin] = len(line)
                    break
    print(alpha_list)
