#!/usr/bin/python

num_of_test = 0 # number of test case (N)
num_B = 0
mat_n = []
mat_k = []
debug = 0

def open_read_file():
    # file_name=raw_input()
    #file_name="sample_input.txt"
    #file_name="D-small-practice.in"
    file_name="D-large-practice.in"
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
    mat_n.sort(reverse=True)
    mat_k.sort(reverse=True)
    res = num_B
    if (debug):
        print mat_n
        print mat_k
    for x in range(num_B):
        if (mat_n[x] < mat_k[x]):
            res -= 1
            tmp = mat_n[num_B-1]
            mat_n.insert(x, tmp)
            del mat_n[len(mat_n)-1]
    mat_n.sort()
    mat_k.sort()
    if (debug):
        print mat_n
        print mat_k
    x = 0
    y = 0
    while x < len(mat_n):
        while y < len(mat_k):
            if (mat_k[y] > mat_n[x]):
                del mat_k[y]
                break
            y += 1
        x += 1
    res1 = len(mat_k) 
    print 'Case #%d: %d %d' % ((i+1), res, res1)
    i += 1

