#!/usr/bin/python

debug = True 
num_N = int(raw_input())
output = []
lst = []
start_lst = []

for k in range(num_N):
    string = raw_input().split()
    num_P = int(string[0])
    num_D = int(string[1])
    lst.append((k,num_P,num_D))    
    if (num_P >= num_D):
        start_lst.append((k,num_P,num_D))

start_lst.sort(key=lambda index: index[0])

idx = -1

for i in range(len(start_lst)):
    lp = start_lst[i][0]
    petrol = start_lst[i][1]
    while True:
        petrol -= lst[lp][2]
        lp += 1
        lp = lp % num_N
        if lp == start_lst[i][0]:
            idx = lp
            break
        petrol += lst[lp][1]
        if petrol < lst[lp][2]:
            break
    if idx != -1:
        break


if (debug):
    print lst
    print start_lst

print idx

    


