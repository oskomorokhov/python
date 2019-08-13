class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        s = target

        if len(nums) < 4:
            return []
        elif len(nums) == 4:
            if sum(nums) == s:
                return [nums]
            else:
                return []
        elif len(nums) > 4:
            if set(nums) == {s}:
                return [[0, 0, 0, 0]]

        hh = set()
        result = []

        for k in range(0, len(nums)):
            h = set()
            cs4 = s - nums[k]
            print("cs4", cs4)
            for i in range(k+1, len(nums)-1):
                #h = set()
                cs3 = cs4 - nums[i]
                print("cs3", cs3)
                for j in range(i+1, len(nums)-2):
                    print(nums[k], nums[i], nums[j])
                    print(f"is there", cs4)
                    if (cs3 - nums[j]) in h:
                        triple = [nums[i], nums[j], cs3-nums[j]]
                        if frozenset(quad) not in hh:
                            result.append(quad)
                            hh.add(frozenset(quad))
                    h.add(nums[j])
                h.add(nums[i])
            h.add(nums[k])

        return result
