#!/usr/bin/python
debug = False
numN = int(raw_input())
string = raw_input().split()
a1 = a2 = 0
old = -1
d = [-1]
def swap(a1,a2):
    global d
    t = d[a1]
    d[a1] = d[a2]
    d[a2] = t
def find_peak(x):
    global d
    if (d[x-1] < d[x] and
            d[x+1] < d[x]):
        return True
    if (d[x-1] > d[x] and
            d[x+1] > d[x]):
        return True
    return False
for x in range(len(string)):
    d.append(int(string[x]))
d.append(1000001)

j = 1
while j <= numN:
    if find_peak(j):
        if not a1:
            a1 = j
        else:
            a2 = j
    j += 1

j = a1+1
swap(a1,a2)
isSwap = True
noSol = False
while j < a2:
    if d[j] < old: 
        isSwap = False
    elif (isSwap == False and d[j] > old):
        noSol = True
    old = d[j]
    j += 1
if d[a2+1] < d[a2] or d[a1-1] > d[a1]:
    noSol=True
    isSwap=False
if isSwap:
    print 'yes'
    print 'swap', a1, a2
elif not noSol:
    print 'yes'
    print 'reverse', a1, a2
else:
    print 'no'


