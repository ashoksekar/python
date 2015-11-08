#!/usr/bin/python -t

from random import shuffle

MAXSQUARES = 4
TOTALSQUARES = MAXSQUARES * MAXSQUARES
matrix = [0 for x in range(TOTALSQUARES)] 
for x in range(TOTALSQUARES):
    matrix[x] = x
shuffle(matrix)

def swap(x,y):
    global matrix
    t = matrix[x]
    matrix[x] = matrix[y]
    matrix[y] = t
def isComplete:
    global matrix
    for x in range(TOTALSQUARES-1):
        if matrix[x] != (x+1):
            return false
    return true
    
def returnUnsolved:
    global matrix
    for x in range(TOTALSQUARES-1):
        if matrix[x] != (x+1):
            return x+1
    assert(1)
def walkThruNeighbor(pos, func):
    if ((pos-1) >=0 and 
            ((pos-1) % MAXSQUARES) < (pos % MAXSQUARES)):
        func(pos-1)
    elif ((pos-MAXSQUARES) >= 0):
        func(pos-MAXSQUARES)
    elif ((pos+1) < TOTALSQUARES and 
            ((pos+1) % MAXSQUARES) > (pos % MAXSQUARES)):
        func(pos+1)
    elif ((pos+MAXSQUARES) < TOTALSQUARES):
        func(pos+MAXSQUARES)

def moveZeroNearTarget(target):
    global matrix

def printMatrix:
    global matrix
    i = 0
    while i < TOTALSQUARES:
        if i % MAXSQUARES == 0:
            print ""
        print matrix[i],
        i += 1


def solve:
    printMatrix()
    if isComplete() == True:
        return


print matrix

