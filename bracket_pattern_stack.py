def check_brackets(brackets):
    stack = []
    bracket_map = {
        "[": "]",
        "{": "}",
        "(": ")",
    }

    for bracket in brackets:
        if bracket in bracket_map.keys():
            stack.append(bracket)
        elif bracket in bracket_map.values() and bracket_map[stack[-1]] == bracket:
            stack.pop()

    if len(stack) == 0:
        return "Valid"
    return "Invalid"


def tower_of_hanoi(no_of_disks):
    def move(no_of_disks, _from, to, aux):
        if no_of_disks == 0:
            return
        move(no_of_disks - 1, _from, aux, to)
        print("Move disk", no_of_disks, "from rod", _from, "to rod", to)
        move(no_of_disks - 1, aux, to, _from)

    move(no_of_disks, "A", "C", "B")


print(check_brackets("[[{}]()]"))
tower_of_hanoi(3)
