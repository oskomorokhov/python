#!/usr/bin/env checkio --domain=py run simplify-unix-path

# https://py.checkio.org/mission/simplify-unix-path/

# You can think about it as simplifying of the first argument "cd" command (a standart bash command). Simplifying means making shorter.
#
# For instance if I docd a/../bit works the same ascd b. Which means "b" is simplifying of "a/../b". It is much easier to explain everything using examples.
#
# Input:String. Non-Empty valid unix path.
#
# Output:String. Unix path.
#
#
# END_DESC


def simplify_path(path):
    """
        simplifying a given path
    """
    # your code here
    return path


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # last slash is not important
    assert simplify_path('/a/') == '/a'

    # double slash can be united in one
    assert simplify_path('/a//b/c') == '/a/b/c'

    # double dot - go to previous folder
    assert simplify_path('dir/fol/../no') == 'dir/no'
    assert simplify_path('dir/fol/../../no') == 'no'

    # one dot means current dir
    assert simplify_path('/a/b/./ci') == '/a/b/ci'
    assert simplify_path('vi/..') == '.'
    assert simplify_path('./.') == '.'

    # you can't go deeper than root folder
    assert simplify_path('/for/../..') == '/'
    assert simplify_path('/for/../../no/..') == '/'

    # not all double-dots can be simplyfied in related path
    assert simplify_path('for/../..') == '..'
    assert simplify_path('../foo') == '../foo'

    print('Simply enough! Let\'s check it now!!')
