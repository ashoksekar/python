#!/usr/bin/python
debug = False
string = raw_input().split()
N = int(string[0])
M = int(string[1])
l = []
def row(pos):
    global M
    return pos / M
def col(pos):
    global M
    return pos % M
def printset(s):
    global l, M
    for x in range(N*M):
        if (x % M == 0):
            print ''
        if x in s:
            print 1,
        else:
            print 0,
    print ''
    return

def find_cross(pos, len, sett):
    global l, M
    tset = []
    t = pos
    if t/M != (pos+len-1)/M:
        return
    while t < pos+len:
        if not l[t]:
            return
        tset.append(t)
        t += 1
    t = pos+len/2
    t -= (len/2) * M
    if t < 0:
        return
    max = t + M * (len-1)
    if (max >= (N * M)):
        return
    while t <= max:
        if not l[t]:
            return
        tset.append(t)
        t += M
    sett[:] = tset[:]
    return


for x in range(N):
    string = raw_input()
    for x in string:
        if x == 'G':
            l.append(1)
        else:
            l.append(0)
if (debug):
    print l
if min(N,M) % 2 == 0:
    maxcross = min(N,M)-1
else:
    maxcross = min(N,M)
crosslist = []
for cross in range(maxcross/2+1):
    for x in range(N*M):
        s = []
        find_cross(x, cross*2+1, s)
        if len(s):
            crosslist.append(set(s))
            if (debug):
                printset(s)
if (debug):
    print crosslist
big = 0
i = 0
while i < len(crosslist)-1:
    j = i+1
    while j < len(crosslist):
        if (crosslist[i].isdisjoint(crosslist[j])):
            length = len(crosslist[i]) * len(crosslist[j])
            if (big < length):
                big = length
        j += 1
    i += 1
print big
    






    
