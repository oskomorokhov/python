class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:

        target = sum(A+B)//2
        SB = sum(B)
        B = set(B)

        for a in itertools.combinations(A, len(A)-1):
            complement = target - sum(a)
            if complement in B:
                return [target-(SB-complement), complement]
