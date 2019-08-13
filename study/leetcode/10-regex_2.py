from collections import defaultdict


def isMatch(s, p):
    transfer = defaultdict(set)
    print("transfer", transfer)
    curr_states = [0]
    print("curr_states,", curr_states)
    for i, c in enumerate(p):
        if c == '*':
            print("c is *, continue")
            continue
        new_state = curr_states[-1] + 1
        print("new state", new_state)
        print("---begin iterate over current_states---", curr_states)
        for state in curr_states:
            print(f"add {state} & token {c} to transfer")
            transfer[state, c].add(new_state)
            print("transfer", transfer)
        if i < len(p) - 1 and p[i + 1] == '*':  # if next c is *
            print("next token is *")
            print(f"transfer[{new_state},{c}] = {new_state}")
            transfer[new_state, c] = {new_state}
            print("transfer", transfer)
            print(f"append {new_state} to {curr_states}")
            curr_states.append(new_state)
            print("curr_states", curr_states)
        else:
            print(
                f"next token is not *, set curr_states {curr_states} to new_state [{new_state}]")
            curr_states = [new_state]
            print("curr_states", curr_states)

    success = curr_states  # final states
    print("success", success)
    curr_states = {0}
    print("curr_states")
    print("---begin iterate over s---", s)
    for c in s:
        next_states = set()
        print("next_states is empty set", next_states)
        print("---begin iterave over curr_states---", curr_states)
        for state in curr_states:
            print("state", state)
            next_states.update(transfer[state, c] | transfer[state, '.'])
            print(
                f"update {next_states} to {transfer[state,c]} | {transfer[state,'.']} ({transfer[state,c] | transfer[state,'.']})")
        curr_states = next_states
        print(f"set curr_states to {next_states}", curr_states)

    print("check if any state in curr_states is success",
          list(state in curr_states for state in success))
    # check any curr_states is success
    return any(state in curr_states for state in success)


assert(isMatch("aa", "a*")) == True

print("all done!")
