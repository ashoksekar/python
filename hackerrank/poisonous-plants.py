#!/usr/bin/python
debug = False
#debug = False 
num_N = int(raw_input())
string = raw_input().split()
arr = []
stack = []
maxd = 0
for k in range(num_N):
    arr.append(int(string[k]))
cnt = 0
cntl = []
for k in range(num_N):
    if ((len(stack) == 0) or (arr[k] <= stack[-1])):
        stack.append(arr[k])
        maxd = max(maxd, cnt)
        cnt = 0
        cntl = []
    elif ((arr[k] > stack[-1]) and (arr[k] <= arr[k-1])):
        if (len(cntl) == 0) or (arr[k] <= cntl[-1]):
            cnt += 1
        else:
            maxd = max(maxd, cnt)
            cnt = 1
            cntl = []
        cntl.append(arr[k])
if (debug):
    print stack
maxd = max(maxd, cnt)
if maxd:
    maxd += 1

print maxd


