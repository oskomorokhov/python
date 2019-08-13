#!/usr/bin/env checkio --domain=py run correct-sentence

# https://py.checkio.org/mission/correct-sentence/

# For the input of your function will be given one sentence. You have to return its fixed copy in a way so it’s always starts with a capital letter and ends with a dot.
#
# Pay attention to the fact that not all of the fixes is necessary. If a sentence already ends with a dot then adding another one will be a mistake.
#
# Input:A string.
#
# Output:A string.
#
# Precondition:No leading and trailing spaces, text contains only spaces, a-z A-Z , and .
#
#
# END_DESC


def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """

    return text[0].upper()+text[1:]+("" if text.endswith(".") else ".")


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    print("Coding complete? Click 'Check' to earn cool rewards!")
