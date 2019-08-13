def radix_lsd(list, base=10):
    import math
    #print("unsorted list is", list)

    num_passes = math.floor(math.log10(abs(max(list))))+1

    #print("number of passes through list, as number of digits for max num in list", num_passes)

    def flush(buckets):
        list = []
        # print(buckets)
        for bucket in buckets:
            for digit in bucket:
                list.append(digit)
        #print("Flushed bucket into list", list)
        return list

    def fill(list, n, base):
        # create bucket(list) for each digit in base
        buckets = [[] for d in range(base)]
        # travere unsorted array
        for num in list:
            # take num, divide by base to the power of n (current pass over list) and take remainder after dividing by base
            lsd = (num // base**n) % base
            # print("num=",num,"lsd=",lsd,"n=",n)
            # put LSD of each number in corresponding bucket
            buckets[lsd].append(num)
        # go to flush foo with our buckets, we should get updated list in return
        return flush(buckets)

    for n in range(0, num_passes):

        # for num_passes times, do fill-flush cycle, replacing unordered list with flush yield
        #print("return of fill+flush is",fill(list,n,base))
        list = fill(list, n, base)

    #print("list is now",list)
    return list


if __name__ == '__main__':
    # print(radix_lsd([934,56,2,13,89,446,0,124]))
    print(radix_lsd([0x1, 0xff, 0xaaa, 0x9000, 0xbbcc], 16))
