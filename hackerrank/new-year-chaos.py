#!/usr/bin/python
debug = False
numT = numN = j = count = 0
lst = [0]
bribe = [0]
numT = int(raw_input())
def swap(i):
    global lst, count, bribe
    if (i+1 >= len(lst)):
        return
    if (debug):
        print lst[i], lst[i+1]
    bribe[lst[i]] += 1
    t = lst[i+1]
    lst[i+1] = lst[i]
    lst[i] = t
    count += 1
while j < numT:
    numN = int(raw_input())
    string = raw_input().split()
    count = oldcount = 0
    invalid = False
    lst = [0]
    bribe = [0]
    for x in string:
        lst.append(int(x))
        bribe.append(0)
    k = len(lst) - 2
    while k >= 1:
        if (((lst[k]-k > 0) or (lst[k+1] < lst[k])) and (lst[k]-(k+1) < lst[k]-k)):
            if bribe[lst[k]] < 2:
                swap(k)
            else:
                invalid = True
                break
        k -= 1
        if k == 0:
            if oldcount == count:
                break
            oldcount = count
            k = len(lst) - 2
    if (debug):
        print lst
    if invalid:
        print 'Too chaotic'
    else:
        print count
    j += 1
