#!/usr/bin/python
num_of_test = 0 # number of test case (N)
debug = 0
num_N = 0
mote = 0
def open_read_file():
    # file_name=raw_input()
    #file_name="sample_input.txt"
    file_name="A-small-practice.in"
    #file_name="A-large-practice.in"
    fin=open(file_name, 'r')
    return fin
def find_greater(pos, val):
    global mat
    ret = 0
    for x in range(pos, len(mat)):
        if mat[x] >= val:
            ret += 1
    return ret

def do_osmos():
    global mat, ops, mote
    if (len(mat) == 0):
        return
    if (debug):
        print mat
        print mote, mat[0], ops
    if ((mote-1) and (mote <= mat[0])):
        val = mote
        tmp = 0
        while (val <= mat[0]):
            val += (val-1)
            tmp += 1
        if (find_greater(0, mat[0]) > tmp):
            mote = val
            assert (mote > mat[0])
            if (mote > mat[0]):
                ops += tmp
    if (mote > mat[0]):
        mote += mat[0]
    else:
        ops += 1

    del mat[0]
    do_osmos()
    return

fin = open_read_file()
num_of_test = int(fin.readline())
i = 0
while i < num_of_test:
    string = fin.readline().split()
    mote = int(string[0])
    num_N = int(string[1])
    string = fin.readline().split()
    mat = []
    for x in range(num_N):
        mat.append(int(string[x]))
    ops = 0
    mat.sort()
    length = len(mat)
    do_osmos()
    if (ops > length):
        ops = length
    print 'Case #%d: %d' % ((i+1), ops)
    i += 1
