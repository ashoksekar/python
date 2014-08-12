#!/usr/bin/python

num_of_test = 0 # number of test case (N)
ans1 = 0
ans2 = 0
mat1 = []
mat2 = []
debug = 0

def open_read_file():
    # file_name=raw_input()
    #file_name="sample_input.txt"
    file_name="A-small-practice.in"
    fin=open(file_name, 'r')
    return fin


fin = open_read_file()
i = 0
num_of_test = int(fin.readline())
while i < num_of_test:
    ans1 = int(fin.readline()) - 1
    j = 0
    mat1 = []
    while j < 4:
        string=fin.readline().split()
        x = 0
        while x < len(string):
            string[x] = int(string[x])
            x += 1
        mat1.append(string)
        j += 1
    ans2 = int(fin.readline()) - 1
    j = 0
    mat2 = []
    while j < 4:
        string=fin.readline().split()
        x = 0
        while x < len(string):
            string[x] = int(string[x])
            x += 1
        mat2.append(string)
        j += 1
    matches = 0
    loc = -1
    j = 0
    while j < 4:
        if (debug):
            print mat1[ans1][j], mat2[ans2]
        if mat1[ans1][j] in mat2[ans2]:
            matches += 1
            loc = mat1[ans1][j] 
        j += 1

    if (debug):
        print ans1, ans2, matches
    if (matches > 1):
        print 'Case #%d: Bad magician!' % (i+1)
    elif (matches == 0):
        print 'Case #%d: Volunteer cheated!' % (i+1)
    else:
        print 'Case #%d: %d' % ((i+1), loc) 
    i += 1
