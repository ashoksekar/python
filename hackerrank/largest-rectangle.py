#!/usr/bin/python

debug = False
num_N = int(raw_input())
string = raw_input().split()
val = []
lst = []
for k in range(num_N):
    ht = int(string[k])
    if (len(lst)):
        lht = lst[-1]
        cnt = k
        while ht < lht[0]:
            val.append(lht[0] * (k-lht[1]))
            cnt = lht[1]
            del lst[-1]
            if len (lst):
                lht = lst[-1]
            else:
                break
        k = cnt
    lst.append((ht,k))

while len(lst):
    lht = lst[-1]
    val.append(lht[0] * (num_N - lht[1]))
    del lst[-1]

if (debug):
    print val

print max(val)    

if (debug):
    print val

