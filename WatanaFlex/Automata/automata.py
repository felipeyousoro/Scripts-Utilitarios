import time

from .State import state as st
from . import build_transitions as btrn
from . import build_tables as btbl

class Automata:
    def __init__(self):
        self.states: list[st.State] = []
        self.states.append(st.State(0, False))
        self.no_states: int = 1
        self.deterministic: bool = True

    def add_state(self, is_final: bool = False, token: str = None) -> st.State:
        self.states.append(st.State(self.no_states, is_final, token))
        self.no_states += 1

        return self.states[-1]

    def get_automata(self) -> tuple[list[list[int]], list[bool], list[str], list[str]]:
        if not self.deterministic:
            raise Exception("Automata is not deterministic")
        tokens, state_tokens = btbl.build_tokens_table(self.states)
        return btbl.build_transition_table(self.states), btbl.build_final_states_table(self.states), tokens, state_tokens

    def add_expression(self, regex_groups: list, token: str) -> None:
        current_state: int = self.states[0].name

        for group in regex_groups:
            new_state: st.State = self.add_state()
            transitions: list[str] = []

            # Parenthesis case, will be handled later
            if group[2] == True:
                break

            if group[0][0] == '[':
                transitions = btrn.get_transitions_from_brackets(group[0][1:-1])
            else:
                transitions.append(group[0])

            self.states[current_state].add_transitions(transitions, new_state)
            current_state = new_state.name

        self.states[-1].is_final = True
        self.states[-1].token = token

        self.check_automata_deterministic()

    def check_automata_deterministic(self):
        print('Checking automata determinism')
        for state in self.states:
            if not state.deterministic:
                print(f'\tState {state.name} is not deterministic, interrupting')
                self.deterministic = False
                return
            print(f'\tState {state.name} is deterministic')

        self.deterministic = True
