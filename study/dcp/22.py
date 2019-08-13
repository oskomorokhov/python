"""
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""


def original_sentence(words: set = set(), sentence: str = "") -> list:

    result = []
    start = 0
    pivot = 1

    while pivot <= len(sentence):
        if sentence[start:pivot] in words:
            result.append(sentence[start:pivot])
            start = pivot
        pivot += 1

    return result


if __name__ == "__main__":
    words = {'quick', 'brown', 'the', 'fox'}
    sentence = "thequickbrownfox"
    assert(original_sentence(words, sentence)) == [
        'the', 'quick', 'brown', 'fox']
    words = {'bed', 'bath', 'bedbath', 'and', 'beyond'}
    sentence = "bedbathandbeyond"
    assert(original_sentence(words, sentence) == ['bed', 'bath', 'and', 'beyond'] or original_sentence(
        words, sentence) == ['bedbath', 'and', 'beyond'])
    print("all tests complete")
