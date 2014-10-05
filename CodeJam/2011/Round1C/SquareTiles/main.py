#!/usr/bin/python
import sys
import copy

num_of_test = 0 # number of test case (N)
debug = 0
num_N = 0
num_R = 0
num_C = 0
def print_matrix(mat):
    global num_R, num_C
    x = y = 0
    while x < num_R:
        print '|',
        y = 0
        while y < num_C:
            print mat[x][y],
            y += 1
        print '|'
        x += 1
    return
def print_matrix_format(mat):
    global num_R, num_C
    x = y = 0
    while x < num_R:
        y = 0
        while y < num_C:
            print mat[x][y],
            sys.stdout.softspace=0
            y += 1
        print 
        x += 1
    return

def replace_tile1(nmat, nlist):
    loc = 0
    while loc < len(nlist):
        (x,y) = nlist[loc]

        if ((nmat[x][y] == '#') and 
                ((x+1,y) in nlist) and
                ((x+1,y+1) in nlist) and
                ((x,y+1) in nlist)):
            if ((nmat[x+1][y] != '#') or
                    (nmat[x+1][y+1] != '#') or
                    (nmat[x][y+1] != '#')):
                break
            nmat[x][y] = '/'
            nmat[x][y+1] = '\\'
            nmat[x+1][y+1] = '/'
            nmat[x+1][y] = '\\'
            """
            if (debug):
                print nlist[loc]
                print_matrix(nmat)
            """
        loc +=1
    return
def replace_tiles():
    global num_R, num_C
    global mat
    lst = build_list(mat)
    if (len(lst) == 0):
        return mat
    nmat = copy.deepcopy(mat)
    replace_tile1(nmat, lst)
    if (count_blue(nmat) == 0):
        return nmat
    return None

def build_list(mat):
    global num_R, num_C
    list = []
    for x in range(num_R):
        for y in range(num_C):
            if mat[x][y] == '#':
                list.append((x,y))
    if (debug):
        print list
    return list

def count_blue(mat):
    global num_R, num_C
    num_B = 0
    for x in range(num_R):
        for y in range(num_C):
            if mat[x][y] == '#':
                num_B += 1
    return num_B

def open_read_file():
    # file_name=raw_input()
    #file_name="sample_input.txt"
    #file_name="A-small-practice.in"
    file_name="A-large-practice.in"
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
            mat[k].append(string[m])
    i += 1
    if (debug):
        print_matrix(mat)
    mat = replace_tiles()
    if mat == None:
        print 'Case #%d:' % i
        print 'Impossible'
    else:
        print 'Case #%d:' % i
        if (debug):
            print_matrix(mat)
        else:
            print_matrix_format(mat)
