def check_balance(text):
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}
    count = 0

    for i, char in enumerate(text):
        # Opening bracket
        if char in "([{":
            stack.push((char, i))

        # Closing bracket
        elif char in ")]}":
            if len(stack) == 0:
                return f"Match error at position {i}"

            top_char, top_pos = stack.pop()

            if top_char != pairs[char]:
                return f"Match error at position {i}"

            count += 1

    # If unmatched opening brackets remain
    if len(stack) != 0:
        _, pos = stack.pop()
        return f'Match error at position {pos}'

    return f'Ok - {count}'
