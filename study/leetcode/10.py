def cache(f):
    seen = {}

    def wrapper(s: str, p: str):
        key = (s, p)
        if key in seen:
            return seen[key]
        seen[key] = f(s, p)
        return seen[key]
    return wrapper


@cache
def isMatch(s: str, p: str) -> bool:

    if not p:
        return not s

    first_match = bool(s) and p[0] in {s[0], '.'}

    if len(p) > 1 and p[1] == "*":
        return isMatch(s, p[2:]) or (first_match and isMatch(s[1:], p))
    else:
        return first_match and isMatch(s[1:], p[1:])


if __name__ == "__main__":
    assert(isMatch("aa", "a")) == False
    assert(isMatch("aa", "a*")) == True
    assert(isMatch("ab", ".*")) == True
    assert(isMatch("aab", "c*a*b")) == True
    assert(isMatch("mississippi", "mis*is*p*.")) == False
    assert(isMatch("a", "a*a")) == True
    assert(isMatch("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "a*")) == True

    print("all done!")
