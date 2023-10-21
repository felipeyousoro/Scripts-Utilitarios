def get_transitions_from_brackets(brackets: str) -> list[str]:
    transitions: list[str] = []

    # if brackets[1] == '^':
    #     for i in range(ord(brackets[2]), ord(brackets[4]) + 1):
    #         transitions.append(chr(i))

    for i in range(0, len(brackets)):
        char = brackets[i]
        if char == '^':
            continue
        if char != '\\':
            # If there is a '-' after the current char, then it is a range
            if i + 1 < len(brackets) and brackets[i + 1] == '-':
                for j in range(ord(char), ord(brackets[i + 2]) + 1):
                    transitions.append(chr(j))
            else:
                transitions.append(char)
        else:
            # Is \t
            if (brackets[i + 1]) == 't':
                transitions.append('\t')
            # Is \n
            elif (brackets[i + 1]) == 'n':
                transitions.append('\n')
            # Is \r
            elif (brackets[i + 1]) == 'r':
                transitions.append('\r')
            # Is \'
            elif (brackets[i + 1]) == '\'':
                transitions.append('\'')
            # Is \"
            elif (brackets[i + 1]) == '\"':
                transitions.append('\"')
            # Is \\
            elif (brackets[i + 1]) == '\\':
                transitions.append('\\')
            # Is [
            elif (brackets[i + 1]) == '[':
                transitions.append('[')
            # Is ]
            elif (brackets[i + 1]) == ']':
                transitions.append(']')
            # Is (
            elif (brackets[i + 1]) == '(':
                transitions.append('(')
            # Is )
            elif (brackets[i + 1]) == ')':
                transitions.append(')')
            # Is ^
            elif (brackets[i + 1]) == '^':
                transitions.append('^')
            # Is $
            elif (brackets[i + 1]) == '$':
                transitions.append('$')
            # Is ?
            elif (brackets[i + 1]) == '?':
                transitions.append('?')
            # Is *
            elif (brackets[i + 1]) == '*':
                transitions.append('*')
            # Is +
            elif (brackets[i + 1]) == '+':
                transitions.append('+')
            # Is .
            elif (brackets[i + 1]) == '.':
                transitions.append('.')
            # Is |
            elif (brackets[i + 1]) == '|':
                transitions.append('|')
            # Is {
            elif (brackets[i + 1]) == '{':
                transitions.append('{')
            # Is }
            elif (brackets[i + 1]) == '}':
                transitions.append('}')

    if brackets[0] == '^':
        transitions = [chr(i) for i in range(256) if chr(i) not in transitions]

    return transitions