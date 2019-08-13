def fourSum(nums: list, target: int) -> list:

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
            return [[s]*4]

    hh = set()
    result = []

    for k in range(0, len(nums)-2):
        cs4 = s - nums[k]
        for i in range(k+1, len(nums)-1):
            h = set()
            cs3 = cs4 - nums[i]
            for j in range(i+1, len(nums)):
                if (cs3 - nums[j]) in h:
                    quad = [nums[k], nums[i], nums[j], cs3-nums[j]]
                    if frozenset(quad) not in hh:
                        result.append(quad)
                        hh.add(frozenset(quad))
                h.add(nums[j])
            h.add(nums[i])
        h.add(nums[k])

    print(result)
    return result


#fourSum([1, 0, -1, 0, -2, 2],0)
