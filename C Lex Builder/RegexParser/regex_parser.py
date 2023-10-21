import time

from . import regex_lexer as rl
class RegexParser:
    def __init__(self, regex: str = ''):
        self.current_index: int = 0
        self.regex_lexer: rl.RegexLexer = rl.RegexLexer(regex)
        self.tokens: list[str] = []

    def __del__(self):
        pass

    def set_regex(self, regex: str) -> None:
        self.regex_lexer.set_regex(regex)

    def get_next_group(self) -> str:
        group: str = ''

        # Char
        if self.tokens[self.current_index][0] == 1:
            group += self.tokens[self.current_index][1]
            self.current_index += 1

            group += self.eat_post_token()

        # Backslash
        elif self.tokens[self.current_index][0] == 3:
            group += self.tokens[self.current_index][1]
            self.current_index += 1

            group += self.eat_post_token()

        # # Caret
        # elif self.tokens[self.current_index][0] == 5:
        #     group += self.tokens[self.current_index][1]
        #     self.current_index += 1

        # Left square brack
        elif self.tokens[self.current_index][0] == 7:
            group += self.tokens[self.current_index][1]
            self.current_index += 1
            while self.tokens[self.current_index][0] != 8:
                group += self.tokens[self.current_index][1]
                self.current_index += 1

            group += self.tokens[self.current_index][1]
            self.current_index += 1

            group += self.eat_post_token()

        # Left parenthesis
        elif self.tokens[self.current_index][0] == 9:
            group += self.tokens[self.current_index][1]
            self.current_index += 1
            while self.tokens[self.current_index][0] != 10:
                group += self.get_next_group()

            group += self.tokens[self.current_index][1]
            self.current_index += 1

            group += self.eat_post_token()

        # Dot
        elif self.tokens[self.current_index][0] == 14:
            group += self.tokens[self.current_index][1]
            self.current_index += 1

            group += self.eat_post_token()

        # # Left curly brack
        # elif self.tokens[self.current_index][0] == 19:

        return group

    def eat_post_token(self) -> str:
        post: str = ''

        if self.current_index >= len(self.tokens):
            return post

        # Star
        if self.tokens[self.current_index][0] == 13:
            post += self.tokens[self.current_index][1]
            self.current_index += 1

        # Plus
        elif self.tokens[self.current_index][0] == 12:
            post += self.tokens[self.current_index][1]
            self.current_index += 1

        # Question
        elif self.tokens[self.current_index][0] == 11:
            post += self.tokens[self.current_index][1]
            self.current_index += 1

        return post

    def get_groups(self) -> list[str]:
        self.current_index = 0
        self.tokens = self.regex_lexer.get_tokens()

        groups: list[str] = []
        while self.current_index < len(self.tokens):
            groups.append(self.get_next_group())

        return groups

