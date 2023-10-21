class State:

    def __init__(self, name: int, is_final: bool = False, token: str = None):
        if name < 0:
            raise ValueError("State name must be a positive integer")

        self.name: int = name
        self.is_final: bool = is_final
        self.token: str = token
        self.transitions: list[str, State] = []
        self.deterministic: bool = True

    def add_transitions(self, transitions: list[str], to):
        for t in transitions:
            for transition in self.transitions:
                if t == transition[0]:
                    if transition[1] != to:
                        self.deterministic = False

            self.transitions.append([t, to])