#!/usr/bin/python
debug = False
numT = numN = numB = numK = 0
numT = int(raw_input())
j = 0
def calc_sum(n):
    return (n * (n+1))/2 
while j < numT:
    string = raw_input().split()
    numN = int(string[0])
    numK = int(string[1])
    numB = int(string[2])
    sum = calc_sum(numB)
    if ((numN > (calc_sum(numK)-calc_sum(numK-numB))) or
            (numN < sum)):
        print -1
        j += 1
        continue
    else:
        lst = set(range(1,numB+1))
        tmp = numB
        if numK > numN:
            top = numN
        else:
            top = numK
        while sum < numN:
            lst.remove(tmp)
            lst.add(top)
            sum += (top - tmp)
            top -= 1
            tmp -= 1
            if (debug):
                print lst
        if (sum != numN):
            lst.remove(top+1)
            sum -= (top+1)
            lst.add(numN - sum)
            sum = numN
    print(" ".join(repr(e) for e in lst))
    j += 1
