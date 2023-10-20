import sys
import os

from Automata import automata as atmt

if __name__ == '__main__':
    file = open(os.path.join(sys.path[0], "regex.clb"), "r")

    automaton = atmt.Automata()

    for line in file:
        regex = " ".join(line.split(" ")[:-1])
        token = line.split(" ")[-1].strip("\n").strip("\t")
        automaton.add_expression(regex, token)



    print('oi')