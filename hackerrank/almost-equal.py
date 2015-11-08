#!/usr/bin/python

debug = True
string = raw_input().split()
num_N = int(string[0])
num_K = int(string[1])

string = raw_input().split()
hts = []
for k in range(num_N):
    hts.append((k,int(string[k])))

hts.sort(key=lambda hts: hts[1])

if (debug):
    print hts

pos = [[] for x in range(num_N)]
if (debug):
    print pos

i = -1
while i <= 0:
    idx = hts[i][0]
    ht = hts[i][1]
    if ht > num_K:
        m = 0
        diff = ht - num_K
        while m < num_N:
            ht1 = hts[m][1]
            if ht1 >= diff:
                break
            m += 1
        if m < num_N:
            for n in range(m):
                pos[hts[n][0]].append(idx)
            if (debug):
                print pos
        i -= 1
    else:
        break


#num_Q = int(raw_input())
#for k in range(num_Q):
#    string = raw_input().split()
#    num_A = int(string[0])
#    num_B = int(string[1])
#    sets = []
#    start = num_A
#    while start <= num_B:
#        for m in range(len(pos[start])):
#            if pos[start][m][0] > num_B:
#                break
#            if pos[start][m][0] > start:
#                sets.append(pos[start][m])
#        start += 1
#    if (debug):
#        print sets
#    print len(sets)
#
