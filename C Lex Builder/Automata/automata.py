import str

from .State import state as st

class Automata:
    def __init__(self):
        self.states: list[st.State] = []
        self.states.append(st.State(0, False))
        self.no_states: int = 1

    def add_expression(self, regex: str, token: str):
        print(regex, token)

    def regex_splitter(self, regex: str) -> list[str]:
        for i in range(len(regex)):
            print('oi')
