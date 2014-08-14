#!/usr/bin/python

num_of_test = 0 # number of test case (N)
debug = 0
num_N = 0
num_L = 0
mat_o = []
mat_d = []
def open_read_file():
    # file_name=raw_input()
    #file_name="sample_input.txt"
    #file_name="A-small-practice.in"
    file_name="A-large-practice.in"
    fin=open(file_name, 'r')
    return fin
def find_bits(num):
    c = 0
    while num:
        num &= (num-1)
        c += 1
    return c
def check_possibility(val):
    global mat_d, mat_o
    global xorg, small

    possible = False
    for x in mat_d:
        xor = val ^ x
        if (small > find_bits(xor)):
            possible=True
            for y in mat_o:
                if not((y ^ xor) in mat_d):
                    possible=False
                    break
            if (possible == True):
                small = find_bits(xor)
                xorg = xor


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
    if (debug):
        print mat_o
        print mat_d
    possible = False
    small = num_L+1
    xorg = 0
    check_possibility(mat_o[0])
    if small != (num_L+1):
        if (debug):
            print 'Case #%d: %d %d %d %d' % ((i+1), num_N, num_L, small, xorg)
        else:
            print 'Case #%d: %d' % ((i+1), small)
    else:
        print 'Case #%d: NOT POSSIBLE' % ((i+1))
    i += 1

