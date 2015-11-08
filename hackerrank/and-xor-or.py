#!/usr/bin/python
debug = False
num_N = int(raw_input())
string = raw_input().split()
arr = []
for k in range(num_N):
    arr.append(int(string[k]))

pri = [[-1,-1,num_N,num_N] for x in range(num_N)]
def calc_xor(pos, before):
    global arr, num_N, pri
    val = arr[pos]
    opos = pos
    if (before):
        pos -= 1
        while((pos >= 0) and (arr[pos] >= val)):
            if (pri[pos][0] < val):
                pri[opos][0] = pri[pos][0]
                pri[opos][2] = pri[pos][2]
                if (pri[pos][0] < 0):
                    return 0
                return val ^ pri[pos][0]
            else:
                pos = pri[pos][2]
                continue
            pos -= 1
        if (pos >= 0):
            pri[opos][0] = arr[pos]
            pri[opos][2] = pos
            return val ^ arr[pos]
        else:
            return 0
    else:
        pos += 1
        while((pos < num_N) and (arr[pos] >= val)):
            if (pri[pos][1] < val):
                pri[opos][1] = pri[pos][1]
                pri[opos][3] = pri[pos][3]
                if (pri[pos][1] < 0):
                    return 0
                return val ^ pri[pos][1]
            else:
                pos = pri[pos][3]
                continue
            pos += 1
        if (pos < num_N):
            pri[opos][1] = arr[pos]
            pri[opos][3] = pos
            return val ^ arr[pos]
        else:
            return 0

val1 = []
val2 = []
for k in range(num_N):
    val = calc_xor(k, True)
    val1.append(val)
k = num_N-1
while k >= 0:
    val = calc_xor(k, False)
    val2.append(val)
    k -= 1

valm1 = max(val1)
valm2 = max(val2)
print max(valm1,valm2)

