#!/usr/bin/python
import math

debug = False
sqlist = []
notsqlist = [2, 3, 7, 8]
digital_root_list = [0, 1, 4, 7]
for x in range(44722):
    sqlist.append(x*x)
numN = int(raw_input())
i = 0

def find_in_list(x):
    for y in sqlist:
        if x == y:
            return True
        elif y > x:
            return False
    return False

def digital_root(x):
    total = 0
    while(x):
        total += x%10
        x = x/10
    if (total/10):
        return digital_root(total)
    return total
while i < numN:
    string = raw_input().split()
    r2 = int(string[0])
    r = int(math.sqrt(r2))
    k = int(string[1])
    start = 0
    count = 0
    while (start <= r/2):
        y2 = r2 - start * start
        if (((y2%10) not in notsqlist) and
                (digital_root(y2) in digital_root_list) and 
                (y2 in sqlist[start:r])):
            if (y2 != r2):
                count += 2
            else:
                count += 1
        start += 1
        if (count * 4) > k:
            break
    count *= 4
    if (debug):
        print count, 
    if (count != k):
        print 'impossible'
    else:
        print 'possible'
    i += 1
