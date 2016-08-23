#!/usr/bin/python -t

import traceback
import sys
from random import shuffle
from subprocess import call

#
#0  1  2  3  
#4  5  6  7  
#8  9  10 11 
#12 13 14 15 

debug=True
NUMROWS = NUMCOLS = 4
TOTALSQUARES = NUMROWS * NUMCOLS
matrix = [0 for x in range(TOTALSQUARES)] 
targetV = 1
for x in range(TOTALSQUARES):
    matrix[x] = x
shuffle(matrix)

def swap(x,y):
    global matrix, targetV
    assert (is_neighbor(x,y))
    t = matrix[x]
    matrix[x] = matrix[y]
    matrix[y] = t
    try:
        if (debug):
            #call(["clear"])
            print 'Unsolved: ', targetV, isSolved(targetV)
            printMatrix()
            dummy = raw_input()
            #exc_info = sys.exc_info()
            if (len(dummy) and int(dummy) == 1):
                raise TypeError("Manual")
    except Exception as ex:
        traceback.print_tb()
def isComplete():
    global matrix
    for x in range(TOTALSQUARES-1):
        if matrix[x] != (x+1):
            return False
    return True
def isSolved(val):
    global matrix
    if val < 1 or val >= TOTALSQUARES:
        return False
    if matrix[val-1] == val:
        return True
    return False

def returnUnsolved(target):
    global matrix
    for x in xrange(target-1,-1,-1):
        if matrix[x] != (x+1):
            return x+1
    return 0

def row(x):
    return x/NUMROWS
def col(x):
    return x % NUMCOLS

def is_neighbor(x,y):
    if row(y) == row(x) and y == x+1:
        return True
    elif row(y) == row(x) and y == x-1:
        return True
    elif col(y) == col(x) and y == x-NUMCOLS:
        return True
    elif col(y) == col(x) and y == x+NUMCOLS:
        return True
    return False

def build_graph():
    global graph
    for i in xrange(0,TOTALSQUARES):
        graph[i] = []
        for j in xrange(0, TOTALSQUARES):
            if is_neighbor(i,j):
                graph[i].append(j)
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

graph=dict()
build_graph()
paths = []
for i in xrange(0,TOTALSQUARES):
    paths.append([])
    for j in xrange(i,TOTALSQUARES):
        if i == j:
            continue
        p = find_all_paths(graph,i,j)
        p.sort(key = lambda x:len(x))
        paths[i].append(filter(lambda x: len(x) <= 4*NUMROWS, p))

def choose_path(src, dest, target):
    global matrix, paths
    zidx = matrix.index(src)
    idx = matrix.index(dest)
    if zidx < idx:
        x = zidx
        y = idx-(x+1)
    else:
        x = idx
        y = zidx-(x+1)
    chsn = 0
    while chsn < len(paths[x][y]):
        pos = True
        for i in paths[x][y][chsn]:
            if i == zidx:
                continue
            if ((matrix[i] and (matrix[i] == target)) or 
                    (matrix[i] and (matrix[i] <= target) and (matrix[i] == i+1)) or 
                    ((row(i) == row(target-1)) and matrix[i] == i+1)):
                pos = False
                break
        if pos:
            break
        chsn += 1
    if (chsn == len(paths[x][y])):
        chsn = 0
        while chsn < len(paths[x][y]):
            gotit = True
            if ((src == 0) and matrix[i] and (matrix[i] == target)):
                gotit = False
                chsn += 1
                continue
            if len(range(row(target-1)*NUMROWS, target-1)) == 0:
                gotit = False
                chsn += 1
                continue
            for i in xrange(row(target-1)*NUMROWS,target-1):
                if ((i not in paths[x][y][chsn]) or 
                        ((src == 0) and (matrix.index(target) in paths[x][y][chsn]))):
                    gotit = False
                    break
            if gotit:
                break
            chsn += 1
    if not (chsn < len(paths[x][y])):
        print 'src: ', src, 'dest: ', dest, 'target: ', target
        assert(0)
    if paths[x][y][chsn][0] != matrix.index(src):
        paths[x][y][chsn].reverse()
        
    return paths[x][y][chsn]
    #for rix in paths[x][y]:
    #    for rixi in rix:

def printMatrix():
    global matrix
    i = 0
    while i < TOTALSQUARES:
        if i % NUMROWS == 0:
            print ""
        print matrix[i],
        if (matrix[i] < 10):
            print "",
        i += 1
    print ""

def solve():
    global matrix
    global targetV
    if isComplete() == True:
        return
    target = 1
    while True:
        if isSolved(target) == True:
            targetV = returnUnsolved(target)
            if targetV == 0:
                target = target + 1
                continue
            else:
                target = targetV
        print 'Target changed to: ', target
        targetV = target
        while (isSolved(target) == False):
            p1 = choose_path(target, matrix[target-1], target)
            for x in p1:
                if x == matrix.index(target):
                    continue
                if matrix.index(0) != x:
                    for y in choose_path(0,matrix[x], target):
                        if y == matrix.index(0):
                            continue
                        swap(y,matrix.index(0))
                swap(matrix.index(0), matrix.index(target))



printMatrix()
solve()
            
