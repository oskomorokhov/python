def lengthOfLongestSubstring_BF(s):
    # BF
    # O(n)
    if not s:
        return 0

    seen = set()
    subs = set()
    shift = 0

    while shift < len(s):

        for i in range(shift, len(s)):

            if s[i] in seen:
                seen.clear()
                subs.add(s[shift:i])
                break

            seen.add(s[i])

        else:
            subs.add(s[shift:])
            break

        shift += 1

    return len(max(subs, key=len)) if subs else len(s)


def lengthOfLongestSubstring_set(s):
    # O(2n)
    # set as sliding window
    # store the characters in current window [i, j)[i,j) (j = ij=i initially).
    # Then we slide the index j to the right. If it is not in the set, we slide j further.
    # Doing so until s[j] is already in the HashSet. At this point, we found the maximum size of substrings without duplicate characters start with index i.
    # Do this for all i
    seen = set()
    ans = 0
    i = j = 0
    while i < len(s) and j < len(s):

        if not s[j] in seen:
            seen.add(s[j])
            j += 1
            ans = max(ans, j - i)
        else:
            seen.remove(s[i])
            i += 1

    return ans


def lengthOfLongestSubstring(s):
    # O(n)
    # map char to its index in dict, skip all the elements in the range [i, j'][i,j] and let i to be j' + 1 if duplicate found in [i:j]
    seen = {}
    ans = 0
    i = j = 0
    while j < len(s):

        if s[j] in seen.keys():
            i = max(seen[s[j]], i)

        ans = max(ans, j - i + 1)
        seen[s[j]] = j+1

        j += 1

    return ans


if __name__ == "__main__":
    assert(lengthOfLongestSubstring("abcabcbb")) == 3
    assert(lengthOfLongestSubstring("bbbbb")) == 1
    assert(lengthOfLongestSubstring("pwwkew")) == 3
    assert(lengthOfLongestSubstring("aab")) == 2
    assert(lengthOfLongestSubstring("dvdf")) == 3
    print("all tests passed")
