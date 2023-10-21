import sys
import os

#from Automata import automata as atmt
from RegexParser import regex_parser as rp

if __name__ == '__main__':
    file = open(os.path.join(sys.path[0], "regex.clb"), "r")

    #automaton = atmt.Automata()

    lines_list = []
    for line in file:
        regex = " ".join(line.split(" ")[:-1])
        token = line.split(" ")[-1].strip("\n").strip("\t")
        lines_list.append([regex, token])

    regex_parser = rp.RegexParser()
    groups = []

    for line in lines_list:
        regex_parser.set_regex(line[0])
        groups.append(regex_parser.get_groups())

    for gp in groups:
        print(gp)
