class Solution:
    @staticmethod
    def product(*args, repeat=1):
        # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
        # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
        pools = [tuple(pool) for pool in args] * repeat
        result = [[]]
        for pool in pools:
            result = [x+[y] for x in result for y in pool]
        for prod in result:
            yield ''.join(prod)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []

        d = {'1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
             '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': ''}

        n = [d[digit] for digit in digits]

        return list(Solution.product(*n))


if __name__ == "__main__":
    input = "23"
    test1 = Solution()
    assert(test1.letterCombinations(input)) == [
        "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    print("all tests passed")
