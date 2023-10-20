from .State import state as st

class Automata:
    def __init__(self):
        self.states: list[st.State] = []
        self.states.append(st.State(0, False))
        self.no_states: int = 1
