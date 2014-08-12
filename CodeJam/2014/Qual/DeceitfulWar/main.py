#!/usr/bin/python

num_of_test = 0 # number of test case (N)
num_B = 0
mat_n = []
mat_k = []
debug = 1

def open_read_file():
    # file_name=raw_input()
    #file_name="sample_input.txt"
    file_name="D-small-practice.in"
    fin=open(file_name, 'r')
    return fin


fin = open_read_file()
num_of_test = int(fin.readline())
i = 0
while i < num_of_test:
    mat_n = []
    mat_k = []
    num_B = int(fin.readline())
    string = fin.readline().split()
    for x in range(num_B):
        mat_n.append(float(string[x]))
    string = fin.readline().split()
    for x in range(num_B):
        mat_k.append(float(string[x]))
    mat_n.sort()
    mat_k.sort(reverse=True)
    res = 0
    if (debug):
        print mat_n
        print mat_k
    for x in range(num_B):
        if ((mat_n[x] > mat_k[num_B-1])):
            res = num_B-x
            if (debug):
                print 'Found a  value: ', x
            break
    mat_k.sort()
    res1 = 0
    if (debug):
        print mat_n
        print mat_k
    x = 0
    y = 0
    while x < num_B:
        while y < num_B:
            if (mat_n[x] < mat_k[y]):
                y += 1
                break
            y += 1
        if y == num_B:
            if mat_n[x] < mat_k[num_B-1]:
                x += 1
            res1 = num_B - x
            break
        x += 1
    print 'Case #%d: %d %d' % ((i+1), res, res1)
    i += 1

