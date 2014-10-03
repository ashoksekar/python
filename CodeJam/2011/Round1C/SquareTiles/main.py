#!/usr/bin/python
num_of_test = 0 # number of test case (N)
debug = 1
num_N = 0
num_R = 0
num_C = 0
def print_matrix():
    global num_R, num_C, num_M
    global mat
    x = y = 0
    while x < num_R:
        print '|',
        y = 0
        while y < num_C:
            if (mat[x][y] < 0):
                print '%d' % mat[x][y],
            else:
                print '%2d' % mat[x][y],
            y += 1
        print '|'
        x += 1
    return

def open_read_file():
    # file_name=raw_input()
    file_name="sample_input.txt"
    #file_name="A-small-practice.in"
    #file_name="A-large-practice.in"
    fin=open(file_name, 'r')
    return fin

fin = open_read_file()
num_of_test = int(fin.readline())
i = 0
while i < num_of_test:
    string = fin.readline().split()
    num_R = int(string[0])
    num_C = int(string[1])
    mat = []
    num_B = 0
    for k in range(num_R): 
        mat.append([])
        string = fin.readline()
        for m in range(num_C):
            if string[m] == '#':
                mat[k].append(1)
                num_B += 1
            else:
                mat[k].append(0)
    i += 1
    if (num_B % 4) != 0:
        print 'Case #%d:' % i
        print 'Impossible'
    else:
        print 'Case #%d:' % i
        if (debug):
            print_matrix()
