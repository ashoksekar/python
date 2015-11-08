#!/usr/bin/python

debug = False
num_T = int(raw_input())
output = []

for k in range(num_T):
    string = raw_input().split()
    num_A = int(string[0])
    num_B = int(string[1])
    bin_mat = []
    
    for i in range(32):
        bin_mat.append(1 << i)
    
    if (debug):
        print bin_mat
    
    lst = []
    for i in range(len(bin_mat)):
        if bin_mat[i] > num_A and bin_mat[i] <= num_B:
            lst.append(bin_mat[i])
    
    if (debug):
        print lst
    if len(lst) >= 1:
        output.append(0)
    else:
        diff = num_B - num_A
        closer = 0
        for i in range(len(bin_mat)):
            if (diff and diff < bin_mat[i]):
                closer = bin_mat[i-1]
                break
        if closer:
            num_A = num_A & ~(2*closer-1)
        output.append(num_A)

for x in output:
    print x


