import string

from .State import state as st

class Automata:
    def __init__(self):
        self.states: list[st.State] = []
        self.states.append(st.State(0, False))
        self.no_states: int = 1

    def add_expression(self, regex: string, token: string):
        print(regex, token)

    def regex_splitter(self, regex: string) -> list[string]:
        expressions: list[string] = []

        meta_characters: dict[string, string] = {
            '(': '(', ')': ')', '[': '[', ']': ']', '{': '{', '}': '}',
            '*': '*', '+': '+', '?': '?', '|': '|', '.': '.', '\\': '\\',
            '^': '^', '$': '$'
        }

        for i in range(len(regex)):
            if regex[i] in
