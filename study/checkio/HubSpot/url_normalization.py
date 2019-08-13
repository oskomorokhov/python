#!/usr/bin/env checkio --domain=py run url-normalization

# https://py.checkio.org/mission/url-normalization/

# URL normalization is the process by which URLs are modified and standardized in a    consistent manner. The goal of the normalization process is to transform a URL into a normalized or canonical URL so    it is possible to determine if two syntactically different URLs may be equivalent.
#
# For our normalization we will use normalizations that preserve semantics.    You should normalize a given url using the next rules (only these rules. They are slightly different from RFC).
#
# Normalization Rules:1. Converting the scheme and host to lower case.HTTP://www.Example.com/ → http://www.example.com/2. Capitalizing letters in escape sequences.        All letters within a percent-encoding triplet (e.g., "%3B") are case-insensitive, and should be capitalized.http://www.example.com/a%c2%b1b → http://www.example.com/a%C2%B1b3. Decoding percent-encoded octets of unreserved characters. For consistency, percent-encoded octets in the        ranges        ofALPHA (%41–%5A and %61–%7A), DIGIT (%30–%39), hyphen (%2D), period (%2E), underscore (%5F), or tilde        (%7E)should not be created by Uniform Resource Identifiers (URI) producers and, when found in a URI, should be decoded to their corresponding        unreserved characters by URI normalizers.http://www.example.com/%7Eusername/ → http://www.example.com/~username/4. Removing the default port. The default port (port 80 for the “http” scheme) should be removed from a URL.http://www.example.com:80/bar.html → http://www.example.com/bar.html5. Removing dot-segments. The segments “..” and “.” can be removed from a URL according to the algorithm        described in RFC 3986 (or a similar algorithm). ".." is a parent directory, "." is the same directory.http://www.example.com/a/b/../c/./d.html → http://www.example.com/a/c/d.htmlAdditional links:If you are interested to know more about URL normalization    (This is not necessarily for this task), then you can find more information here:Wikipedia,RFC3986
#
#
# Input:URL, an unicode string.
#
# Output:Normalized URL, a string.
#
# Precondition:All input urls are valid.
#
#
#
# END_DESC

import re


def checkio(url):

    url = url.lower()

    url = p_encoded(url)

    url = re.sub(':80(?=\/|$)', '', url)

    url = re.sub('\/\.(\/\.)*\/', '/', url)

    url = re.sub('\/[a-zA-Z0-9]+(\/\.\.(\/\.\.)*)', '', url)

    return url


def p_encoded(url):

    if '%' in url:

        url = re.sub('\%[a-zA-Z0-9]{2}',
                     lambda match: match.group(0).upper(), url)

        matches = re.findall('\%[a-zA-Z0-9]{2}', url)

        for c in matches:

            if any(int(c[1:], 16) in x for x in [range(int('41', 16), int('5A', 16)+1), range(int('61', 16), int('7A', 16)+1), range(int('30', 16), int('39', 16)+1), [int('2D', 16), int('2E', 16), int('5F', 16), int('7E', 16)]]):

                url = re.sub(c, lambda match: bytearray.fromhex(
                    match.group(0)[1:]).decode().lower(), url)

    return url


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    '''assert checkio("Http://Www.Checkio.org") == \
        "http://www.checkio.org", "1st rule"
    assert checkio("http://www.checkio.org/%cc%b1bac") == \
        "http://www.checkio.org/%CC%B1bac", "2nd rule"
    assert checkio("http://www.checkio.org/task%5F%31") == \
        "http://www.checkio.org/task_1", "3rd rule"
    assert checkio("http://www.checkio.org:80/home/") == \
        "http://www.checkio.org/home/", "4th rule"
    assert checkio("http://www.checkio.org:8080/home/") == \
        "http://www.checkio.org:8080/home/", "4th rule again"'''
    assert checkio("http://www.checkio.org/task/./1/../2/././name") == \
        "http://www.checkio.org/task/2/name", "5th rule"
    print('First set of tests done')
