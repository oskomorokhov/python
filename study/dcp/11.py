"""
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""


def autocomplete_1(lst: list = [], query: str = "") -> list:
    # BF
    if not list:
        return None
    result = []
    for word in lst:
        if word.startswith(query):
            result.append(word)
    return result


def hash_the_list(lst: list = []) -> dict:
    # convert list to dict
    # d={'d':['dog','deer','deal'], 'do':['dog'], 'dog':['dog'], 'de':['deer','deal'], 'dee':['deer'], 'deer':['deer'], 'dea':['deal'], 'deal':['deal']}
    if not list:
        return None

    dct = {}
    i = 0
    j = len(lst)-1

    while i <= j:

        for il in range(len(lst[i])):

            if dct.get(lst[i][:il+1]):
                dct[lst[i][:il+1]].add(lst[i])
            else:
                dct[lst[i][:il+1]] = set()
                dct[lst[i][:il+1]].add(lst[i])

        if i == j:
            break

        for jl in range(len(lst[j])):

            if dct.get(lst[j][:jl+1]):
                dct[lst[j][:jl+1]].add(lst[j])
            else:
                dct[lst[j][:jl+1]] = set()
                dct[lst[j][:jl+1]].add(lst[j])

        i += 1
        j -= 1

    return dct


def autocomplete_2(dct: dict = {}, query: str = "") -> list:
    # lookup query in dict
    return dct[query]


if __name__ == "__main__":

    lst = ['dog', 'deer', 'deal']
    query = "de"

    assert autocomplete_1(lst, query) == ['deer', 'deal']

    dct = hash_the_list(lst)
    assert autocomplete_2(dct, query) == {'deer', 'deal'}

    print("all tests passed")
