#!/usr/bin/python
import sys
num_of_test = 0 # number of test case (N)
debug = 0
num_N = 0
def open_read_file():
    # file_name=raw_input()
    #file_name="sample_input.txt"
    #file_name="B-small-practice.in"
    file_name="B-large-practice.in"
    fin=open(file_name, 'r')
    return fin
def prune_node(frm, to):
    global mat, pcount
    visit = 0
    tmp = []
    for x in mat[to]:
        if (x == frm):
            continue
        tmp.append(prune_node(to, x))
        visit += 1
    totsum = sum(tmp)+visit
    tmp.sort()
    if (visit > 2) or (visit == 1):
        if (visit == 1):
            pcount += tmp[0]+visit
            totsum -= tmp[0]+visit
        else:
            for x in range(len(tmp)-2):
                pcount += tmp[x]
                totsum -= tmp[x]
            pcount += visit-2
            totsum -= visit-2
        if (debug):
            print 'cut frm: ', frm, 'to: ', to, 'val: ', tmp[0]
    return totsum
    
sys.setrecursionlimit(10000)
fin = open_read_file()
num_of_test = int(fin.readline())
i = 0
while i < num_of_test:
    num_N = int(fin.readline())
    mat = []
    pcount = 0
    for x in range(num_N+1):
        mat.append([])
    for x in range(num_N-1):
        string = fin.readline().split() 
        string[0] = int(string[0])
        string[1] = int(string[1])
        mat[string[0]].append(string[1])
        mat[string[1]].append(string[0])
    small = num_N
    smalloc = -1
    for x in range(1,num_N+1):
        pcount = 0
        totsum = prune_node(-1, x)
        if (debug):
            print 'x: ', x,
            print 'Totsum: ', totsum,
            print 'pcount: ', pcount
        if (small > pcount):
            small = pcount
            smalloc = x
        
    if (debug):
        print 'Case #%d: %d %d %d' % ((i+1), num_N, small, smalloc)
        for x in range(1,num_N+1):
            print x, ':', mat[x]
    else:
        print 'Case #%d: %d' % ((i+1), small)
    i += 1
