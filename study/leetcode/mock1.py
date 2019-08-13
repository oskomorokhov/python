"""
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. 
Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.
"""

def findPairs_BF(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    # BF O(n^2)
    """
    unique_pairs=set()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            e1,e2=nums[i],nums[j]
            print(f"e1:{nums[i]},e2:{nums[j]}")
            if abs(e1-e2) == k:
                print("abs diff is k, add pair to set")
                if (e1,e2) not in unique_pairs and (e2,e1) not in unique_pairs:
                    unique_pairs.add((e1,e2))
    return len(unique_pairs)

def findPairs_2(nums,k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    # O(n) + lookups
    """
    print("-----foo start-----")

    if k < 0: return 0

    i=0
    j=len(nums)-1
    complements=set()
    unique_pairs=set()
    while i <= j:
        if i<j:
            e1,e2=nums[i],nums[j]
            print(f"e1:{e1},e2:{e2},k:{k}")
            if abs(e1-e2) == k:
                print(f"abs(e1-e2) == k -> add to pair")
                unique_pairs.add(frozenset((e1,e2)))
            if e1+k in complements:
                print(f"e1+k={e1+k} in comps, add ({e1},{e1+k}) as unique pair")
                unique_pairs.add(frozenset((e1,e1+k)))
            if e1-k in complements and e1-k != e1+k:
                print(f"e1-k={e1-k} in comps, add ({e1},{e1-k}) as unique pair")
                unique_pairs.add(frozenset((e1,e1-k)))
            print(f"add e1 {e1} to comps")
            complements.add(e1)
            if e2+k in complements:
                print(f"e2+k={e2+k} in comps, add ({e2},{e2+k}) as unique pair")
                unique_pairs.add(frozenset((e2,e2+k)))
            if e2-k in complements and e2-k != e2+k:
                print(f"e2-k={e2-k} in comps, add ({e2},{e2-k}) as unique pair")
                unique_pairs.add(frozenset((e2,e2-k)))
            print(f"add e2 {e2} to comps")
            complements.add(e2)
                
        elif i == j:
            e1 = nums[i]
            print(f"e1:{e1},k:{k}")
            if e1+k in complements:
                    print(f"e1+k={e1+k} in comps, add ({e1},{e1+k}) as unique pair")
                    unique_pairs.add(frozenset((e1,e1+k)))
            if e1-k in complements:
                print(f"e1-k={e1-k} in comps, add ({e1},{e1-k}) as unique pair")
                unique_pairs.add(frozenset((e1,e1-k)))

        print(f"uq: {unique_pairs}")

        i+=1
        j-=1

    return len(unique_pairs)


def findPairs(nums, k):
    print("---foo start---")
    if k < 0 or not nums: 
        return 0
    
    i=0
    j=len(nums)-1
    
    hashed_nums=set(nums)
    complements=set()
    unique_pairs=set()
    
    while i <= j:
        
        print(nums[i],nums[j])

        if abs(nums[i]-nums[j]) == k and i != j:
            print("i&j=pair, +pair")
            unique_pairs.add(frozenset((nums[i],nums[j])))

        if nums[i]+k in complements:
            print(f"{nums[i]}+{k}={nums[i]+k} in comps, +pair")
            unique_pairs.add(frozenset((nums[i],nums[i]+k)))
        
        if nums[i]-k in complements:
            print(f"{nums[i]}-{k}={nums[i]-k} in comps, +pair")
            unique_pairs.add(frozenset((nums[i],nums[i]-k)))

        complements.add(nums[i])

        if nums[j]+k in complements and i != j:
            print(f"{nums[j]}+{k}={nums[j]+k} in comps, +pair")
            unique_pairs.add(frozenset((nums[j],nums[j]+k)))
        
        if nums[j]-k in complements and i != j:
            print(f"{nums[j]}-{k}={nums[j]-k} in comps, +pair")
            unique_pairs.add(frozenset((nums[j],nums[j]-k)))

        complements.add(nums[j])
        
        i+=1
        j-=1

    print("up", unique_pairs)
    return len(unique_pairs)


if __name__ == "__main__":
    lst=[1, 2, 3, 4, 5]
    k=0
    assert(findPairs(lst,k)) == 0
    lst=[1, 3, 1, 5, 4]
    k=0
    assert(findPairs(lst,k)) == 1
    lst=[1, 2, 3, 4, 5]
    k=1
    assert(findPairs(lst,k)) == 4
    lst=[3, 1, 4, 1, 5]
    k=2
    assert(findPairs(lst,k)) == 2
    lst=[1, 2, 3, 4, 5]
    k=-1
    assert(findPairs(lst,k)) == 0
    lst=[1, 2, 3, 4, 5]
    k=2
    assert(findPairs(lst,k)) == 3
    lst=[1,1,1,2,1]
    k=1
    assert(findPairs(lst,k)) == 1
    lst=[397,313,220,34,286,227,257,515,322,127,188,57,159,306,89,284,466,396,412,31,458,177,403,157,470,44,156,326,213,239,455,156,498,409,292,155,333,451,92,379,172,252,309,232,304,53,237,372,126,137,342,318,519,370,366,367,518,479,19,52,39,100,38,486,77,64,392,38,87,2,76,291,370,341,305,409,352,342,417,454,92,493,28,143,32,133,73,97,205,448,358,448,353,196,222,185,350,145,156,113,246,349,181,307,346,262,214,504,106,78,63,494,521,130,425,408,30,107,72,69,40,392,351,246,74,314,37,310,456,128,87,380,355,466,380,493,456,278,4,314,213,326,191,102,409,304,152,378,105,333,207,98,478,45,15,131,81,217,310,330,262,31,147,338,23,253,254,187,193,225,469,368,287,353,247,204,88,199,364,175,186,300,434,395,183,99,242,380,242,504,29,398,425,477,301,412,152,165,325,97,78,232,154,480,137,393,117,360,370,122,340,175,89,483,24,379,517,224,109,170,425,85,268,411,227,182,25,323,300,447,120,497,215,194,100,52,480,43,246,280,221,504,327,61,464,177,394,131,6,408,82,226,50,523,192,448,332,137,462,128,222,268,153,442,135,120,413,309,94,434,374,487,416,30,232,103,79,325,350,370,103,408,522,371,333,182,318,43,230,429,156,63,499,240,513,334,317,421,152,111,314,446,423,387,496,123,435,512,234,68,154,357,177,439,412,171,362,188,483,374,366,426,81,162,52,327,229,378,409,490,8,381,445,480,150,82,346,508,310,476,60,438,280,274,128,322,144,204,367,269,156,169,158,140,283,298,228,498,201,16,60,232,140,150,4,265,173,236,429,358,300,337,17,220,470,200,233,99,320,457,371,376,198,113,474,150,116,502,241,45,221,13,108,358,191,46,214,465,117,190,36,55,506,513,335,475,180,459,21,346,493,29,73,355,496,436,263,352,301,413,137,336,200,330,283,27,343,307,363,417,505,351,54,101,21,32,171,381,172,397,320,183,118,231,486,240,486,354,218,487,160,360,66,521,295,23,303,176,143,281,19,41,151,394,138,521,388,17,28,145,415,145,77,428,372,500,319,364,327,199,281,284,451,12,106,448,459,250,55,256,273,387,179,45,394,172,342,290,228,387,80,492,446,516,303,68,145,418,26,1,137,480,281,336,155,247,250,477,518,173,480,187,425,434,497,212,280,460,307,45,211,452,476,94,257,214,147,408,525,181,161,454,359,342,88,453,292,465,511,329,150,453,272,512,97,36,33,25,469,246,220,165,248,258,508,341,362,218,484,144,435,68,244,300,293,398,347,486,92,100,24,267,351,498,137,289,241,19,175,217,46,36,269,479,348,372,507,78,315,97,370,40,192,76,130,70,503,255,516,314,289,415,213,28,53,212,187,421,118,16,291,329,166,247,23,389,317,424,354,80,508,296,1,471,308,184,353,481,426,275,187,412,204,472,130,324,5,192,469,509,470,53,396,466,448,495,41,298,348,468,426,341,223,328,45,95,459,494,471,313,455,425,314,368,32,0,81,230,341,7,403,495,22,398,389,212,15,505,309,343,4,310,5,329,218,433,206,501,485,131,346,193,64,483,215,179,217,250,138,35,42,6,306,464,248,253,489,24,3,351,517,192,151,353,180,406,365,273,254,450,485,220,436,350,175,170,122,269,18,448,446,266,194,337,141,136,249,112,302,383,323,408,264,192,320,273,428,32,250,444,318,514,449,411,352,20,143,424,222,463,246,117,27,87,327,175,119,245,87,257,155,183,254,380,305,464,305,390,415,260,408,506,497,131,26,331,394,80,499,47,17,276,229,393,384,520,450,390,44,80,206,191,402,461,465,161,65,268,369,213,159,64,207,120,245,178,395,63,109,29,69,392,168,59,103,438,157,155,266,189,284,258,190,505,391,301,189,139,87,144,39,417,504,333,8,45,278,31,219,101,397,68,483,462,486,77,38,355,392,266,206,369,233,230,9,507,99,161,416,281,310,76,307,479,324,358,56,410,203,188,242,337,326,78,125,27,194,96,24,169,404,53,250,178,29,375,13,441,414,207,505,499,132,476,98,490,429,68,8,110,7,375,440,95,1,105,309,226,445,28,502,290,453,99,445,12,481,292,285,150,74,500,192,178,255,327,187,484,447,267,349,119,520,32,361,277,297,350,74,37,364,325,163,255,24,229,331,258,74,343,196,196,103,141,39,487,373,236,230,72,461,233,200,353,279,204,12,16,343,273,234,469,151,1,211,54,404,354,52,273]
    k=-157
    assert(findPairs(lst,k)) == 0
    print("all tests passed")





"""
lst=[3, 1, 4, 1, 5]
k=2
--------------
e1=3
e2=5

abs(3-5)=2
+pair

3 comps: 
3-2=1
    is 1 in comps?
    no -> add 1 to comps
3+2=5 
    is 5 in comps?
    no -> add 5 to comps

5 comps:
5-2=3
    is 3 in comps? 
    no -> add 3 to comps
5+2=7
    is 7 in comps?
    no -> add 7 to comps

comps: 1,3,5,7
--------------
e1=1
e2=1

abs(1-1)=0
no pair

1 comps:
1+2=3
    is 3 in comps? 
    yes -> add fset(1,3) to result
1-2=-1
    is -1 in comps?
    no -> add -1 to comps

1 comps:
skip

"""