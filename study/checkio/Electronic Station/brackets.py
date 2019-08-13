#!/usr/bin/env checkio --domain=py run brackets

# https://py.checkio.org/mission/brackets/

# “Great!” Exclaimed Sofia. “Now we have the password.”
#
# “To what exactly?” Quipped Nikola.
#
# “Untold treasures, vast riches beyond belief! Gold! Silver! Silicon! Hydraulic Fluid! Anything your heart        desires!”
#
# “And you’re going to do what with a password to absolutely nothing?” Nikola smirked.
#
# “Oh... Right...”
#
# Stephen spoke up. “Well, this door back here has a keypad. Only thing is the brackets look pretty busted up. We        could try fixing it and then punching in the password?”
#
# “YES! That!” Sofia exclaimed.
#
# You are given an expression with numbers, brackets and operators.    For this task only the brackets matter. Brackets come in three flavors: "{}" "()" or "[]".    Brackets are used to determine scope or to restrict some expression.     If a bracket is open, then it must be closed with a closing bracket of the same type.     The scope of a bracket must not intersected by another bracket.     In this task you should make a decision, whether to correct an expression or not based on the brackets.     Do not worry about operators and operands.
#
# Input:An expression with different of types brackets as a string (unicode).
#
# Output:A verdict on the correctness of the expression in boolean (True or False).
#
# Precondition:
# There are only brackets ("{}" "()" or "[]"), digits or operators ("+" "-" "*" "/").
# 0 < len(expression) < 103
#
#
# END_DESC


def checkio(str):

    brackets = "()[]{}"

    d = {x: brackets[brackets.index(x)+1] for x in brackets[::2]}

    print("brackets dict (open:close)", d)

    str = list(str)

    for i in str[:]:

        if i not in brackets:
            str.remove(i)

    print("Removed all non-bracket chars from str, it's now", str)

    if len(str) % 2 != 0:
        print("Odd amount of brackets, return False")
        return False
    else:
        middle_index = len(str)//2
        # print(middle_index)

        half1 = str[:middle_index]
        half2 = str[middle_index:]
        print(half1, half2)

        if half2 == [d.get(x) for x in half1][::-1]:
            print("Open == Close, return True")
            return True

        else:
            print("halves do not match, return False")
            return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    #assert checkio("((5+3)*2+1)") == True, "Simple"
    #assert checkio(")(5+3(*2+1)") == False, "Wrong Direction"
    #assert checkio("{[(3+1)+2]+}") == True, "Different types"
    #assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    #assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    #assert checkio("2+3") == True, "No brackets, no problem"
    #assert checkio("({[3]})-[4/(3*{1001-1000}*3)/4]") == True
    #assert checkio("{") == False
    #assert checkio("]") == False
    #assert checkio("([{([{(({{{([{[[[{[([((([(({[[[[(([{([[{[[{{({[([([[{((([{{{[{[[([(({((({[((({(([({{{[([({([[{({{[[{[[([[{([{[([([([(([(([({((({(((((({[({([[{[{[([({[[({[[([[[[{{(([{{[{[{{[{[{{[[((((([{[[{({([[[[[({((({{[[{[[[[[({(([[{[{[[{{[{[{([([{{{{{{{((([[{{((({[[[[[([(((({{({{[([[[(({{{([[{{{([[{([({[({[({(([[([{[[[(([[{[{{{{({[[[{[{{([{({[({{({([((([(([{({(({[[([([([{{[([{[[{([({[{({[[(([((({(([[({{({[{({{{[{({{({[({{{{(([{(([(({({[{{[({[({([[[[(([[{(([{[{({(((([[[(([([{[{{(((([[{({{([[{(((((({[[{{(({([[]])}))}}]]}))))))}]])}})}]]))))}}]}])]))]]]))))})}]}]))}]]))]]]])})]})]}}]})}))]))}]))}}}})]})}})}]}}})}]})}})]]))})))]))]]})}]})])}]]}])]}}])])])]]}))})}]))])))])})}})]})}])}}]}]]]})}}}}]}]]))]]]}])]]))})]})]})])}]])}}}]])}}}))]]])]}})}}))))])]]]]]})))}}]])))}}}}}}}])])}]}]}}]]}]}]]))})]]]]]}]]}})))})]]]]])})}]]}])))))]]}}]}]}}]}]}}]))}}]]]])]]})]]})])]}]}]])})]}))))))})))})]))]))])])])]}])}]])]]}]]}})}]])})])]}}})]))})))]})))}))])]]}]}}}])))}]])])]})}}]]}]])}]))]]]]}))])))])]}]]]}])}}}))}])}])") == True
    print("Done! Press check")

    '''
    (({[(((1)-2)+3)-3]/3}-3)
    (({[((ZZZ-2)+3)-3]/3}-3)
    (({[(ZZZZZZZ+3)-3]/3}-3)
    (({[ZZZZZZZZZZZ-3]/3}-3)
    (({ZZZZZZZZZZZZZZZ/3}-3)
    ((ZZZZZZZZZZZZZZZZZZZ-3)
    (ZZZZZZZZZZZZZZZZZZZZZZZ
    
    ( is redundant! return False
    '''
