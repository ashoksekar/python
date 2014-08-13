#!/usr/bin/python

num_of_test = 0 # number of test case (N)
debug = 1
num_N = 0
num_L = 0
mat_o = []
mat_d = []
def open_read_file():
    # file_name=raw_input()
    #file_name="sample_input.txt"
    file_name="A-small-practice.in"
    #file_name="A-large-practice.in"
    fin=open(file_name, 'r')
    return fin


fin = open_read_file()
num_of_test = int(fin.readline())
i = 0
while i < num_of_test:
    string = fin.readline().split()
    num_N = int(string[0])
    num_L = int(string[1])
    mat_o = []
    mat_d = []
    string = fin.readline().split()
    for x in range(num_N):
        mat_o.append(int(string[x], 2))
    string = fin.readline().split()
    for x in range(num_N):
        mat_d.append(int(string[x], 2))
    mat_o.sort()
    mat_d.sort()
    print 'Case #%d: %d %d' % ((i+1), num_N, num_L)
    if (debug):
        print mat_o
        print mat_d
    i += 1

