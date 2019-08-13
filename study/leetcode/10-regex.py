import string


def solution(s: str, p: str) -> bool:
    # edge cases
    print("----------")
    print(s, "matches", p, "?")

    if not p:
        return not s
    elif p == ".*":
        return True
    elif p.startswith("*"):
        return False
    elif not s:
        return p.startswith(".*")

    l = len(p)

    match = True
    s_prev = ""
    p_prev = ""

    for i, c in enumerate(s):
        print("-----")
        if len(p) > i+1 and p[i+1] == '*':
            mode = "star"
            print("next is *, mode=star")
        elif p[i] == '*':
            print("we are at *, mode=star")
            continue
        else:
            mode = "explicit"
            print("next is not *, mode=explicit")

        print("char", s[i], "token", p[i])

    print("final result is", match)
    return match


#assert(solution("aa","a*")) == True
assert(solution("ab", "aa*b")) == True
#assert(solution("abb","a.*")) == True
#assert(solution("aBaCaDeF","a.aCa.*F")) == True

print("all done!")
