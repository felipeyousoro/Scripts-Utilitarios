class State:
    POSSIBLE_TRANSITIONS: int = 256

    def __init__(self, name: int, is_final: bool = False):
        if name < 0:
            raise ValueError("State name must be a positive integer")

        self.name: int = name
        self.is_final: bool = is_final
        self.transitions: list[int] = [-1 for _ in range(State.POSSIBLE_TRANSITIONS)]
