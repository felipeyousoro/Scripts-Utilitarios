import sys
import os

#from Automata import automata as atmt
from RegexParser import regex_lexer as rl

if __name__ == '__main__':
    file = open(os.path.join(sys.path[0], "regex.clb"), "r")

    #automaton = atmt.Automata()

    lexer_list = []
    for line in file:
        regex = " ".join(line.split(" ")[:-1])
        token = line.split(" ")[-1].strip("\n").strip("\t")
        lexer = rl.RegexLexer(regex)
        lexer_list.append(lexer)

    sncd_lexer = lexer_list[1]
    print(sncd_lexer.regex)
    tokens = sncd_lexer.get_tokens()
    for tk in tokens:
        print(tk[1])
