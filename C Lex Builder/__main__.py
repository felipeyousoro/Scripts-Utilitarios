import sys
import os
import string

TRANSITION_TABLE: list[list] = [[-1 for _ in range(256)]]
STATE_TABLE: list[int] = [0]
TOKEN_TABLE: list[string] = [None]

if __name__ == '__main__':
    file = open(os.path.join(sys.path[0], "regex.clb"), "r")

    for line in file:
        regex = " ".join(line.split(" ")[:-1])
        token = line.split(" ")[-1].strip("\n").strip("\t")
        print(regex, token)
