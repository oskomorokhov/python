#!/usr/bin/env checkio --domain=py run the-most-frequent

# https://py.checkio.org/mission/the-most-frequent/

# You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence.
#
# Input:a list of strings.
#
# Output:a string.
#
#
# END_DESC


def most_frequent(data):


<< << << < HEAD

return sorted(data, key=lambda x: data.count(x), reverse=True)[0]
== == == =
"""
        determines the most frequently occurring string in the sequence.
    """
# your code here
return None


def radix_lsd(list, base=10):

    #print("unsorted list is", list)

    num_passes = len(str(abs(max(list))))
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
            # print("num=",num,"lsd=",lsd)
            # put LSD of each number in corresponding bucket
            buckets[lsd].append(num)
        # go to flush foo with our buckets, we should get updatedlist in return
        return flush(buckets)

    for n in range(0, num_passes):

        # for num_passes times, do fill-flush cycle, replacing unordered list with flush yield
        #print("return of fill+flush is",fill(list,n,base))
        list = fill(list, n, base)

    #print("list is now",list)
    return list


>>>>>> > 98fa6ff036ccfeb62253c60979fda532adc48e6e

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

<< << << < HEAD


== == == =
assert radix_lsd([9, 1, 55, 23, 100, 7]) == [1, 7, 9, 23, 55, 100]
assert radix_lsd([170, 45, 75, 90, 2, 802, 2, 66]) == [
    1, 7, 9, 23, 55, 100]

'''
>>>>>>> 98fa6ff036ccfeb62253c60979fda532adc48e6e
    assert most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
<<<<<<< HEAD
    
=======
    '''
>>>>>> > 98fa6ff036ccfeb62253c60979fda532adc48e6e
print('Done')
