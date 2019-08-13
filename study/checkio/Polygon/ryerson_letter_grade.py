#!/usr/bin/env checkio --domain=py run ryerson-letter-grade

# https://py.checkio.org/mission/ryerson-letter-grade/

# Given the percentage grade for the course, calculate and return the letter grade that would appear in the Ryerson grades transcript, as defined on the pageRyerson Grade Scales. The letter grade should be returned as a string that consists of the uppercase letter followed by the possible modifier  "+"  or  "-" .
#
# Input:Int. Percentage grade.
#
# Output:Str.  The letter grade.
#
# Precondition:argument can be from 0 to 150
#
# The mission was taken from Python CCPS 109 Fall 2018. It is taught for Ryerson Chang School of Continuing Education byIlkka Kokkarinen
#
#
# END_DESC

# feel free to change table structure in any way

TABLE = '''
A 85-89%
A- 80-84%
B+ 77-79%
B 73-76%
B- 70-72%
C+ 67-69%
C 63-66%
C- 60-62%
D+ 57-59%
D 53-56%
D- 50-52%
'''


def ryerson_letter_grade(pct: int) -> str:
    # your code here
    return "A"


if __name__ == '__main__':
    print("Example:")
    print(ryerson_letter_grade(45))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert ryerson_letter_grade(45) == "F"
    assert ryerson_letter_grade(62) == "C-"
    print("Coding complete? Click 'Check' to earn cool rewards!")
