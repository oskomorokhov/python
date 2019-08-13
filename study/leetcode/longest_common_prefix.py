class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs or "" in strs:
            return ""

        if len(strs) == 1 or len(set(strs)) == 1:
            return strs[0]

        loop = True

        prefixes = []

        pivot = 1

        while loop is True and pivot <= len(strs[0]):
            prefix = strs[0][:pivot]
            for word in strs[1:]:
                if not word.startswith(prefix):
                    loop = False
                    break
            else:
                prefixes.append(prefix)
            pivot += 1

        return max(prefixes, key=len) if prefixes else ""


if __name__ == "__main__":
    strs = ["a", "ac"]
    test1 = Solution()
    assert(test1.longestCommonPrefix(strs)) == "a"
    print("all tests passed")
