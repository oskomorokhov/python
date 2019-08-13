# longest palindromic substring in string


def lps(s: str) -> str:

    table = [[False for i in range(len(s))] for j in range(len(s))]

    lps = s[0]
    lps_len = 1

    # all 1-chr strings are palindroms
    for i in range(len(s)):
        table[i][i] = True

    # process all substrings with length of 2
    found = False
    for i in range(len(s)-1):
        j = i+1
        if s[i] == s[j]:
            table[i][j] = True
            if not found:
                lps = s[i:j+1]
                lps_len = len(lps)
                found = True

    # check all substrings with length > 2
    for k in range(2, len(s)):
        for i in range(0, len(s)-k):
            j = i + k
            if s[i] == s[j] and table[i+1][j-1] is True:
                table[i][j] = True
                if len(s[i:j+1]) > len(lps):
                    lps = s[i:j+1]
                    lps_len = len(lps)

    return lps


def lps_hash(s: str) -> str:

    # edge cases
    if not s:
        return ""
    if len(s) == 1 or s == reversed(s):
        return s

    # all 1-chr strings are palindroms
    table = {f'{i}:{j}': False if i != j else True for i in range(
        len(s)) for j in range(i, len(s))}

    lps = s[0]
    lps_len = 1

    # process all substrings with length of 2
    found = False
    for i in range(len(s)-1):
        j = i+1
        if s[i] == s[j]:
            table[f'{i}:{j}'] = True
            if not found:
                lps = s[i:j+1]
                lps_len = len(lps)
                found = True

    # check all substrings with length > 2
    for k in range(2, len(s)):
        for i in range(0, len(s)-k):
            j = i + k
            if s[i] == s[j] and table[f'{i+1}:{j-1}'] is True:
                table[f'{i}:{j}'] = True
                if len(s[i:j+1]) > len(lps):
                    lps = s[i:j+1]
                    lps_len = len(lps)
    return lps


if __name__ == "__main__":
    # s="abccbd"
    # s="civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    print(lps_hash(s))
