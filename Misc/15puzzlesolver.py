#!/usr/bin/python -t

import traceback
import sys
from random import shuffle
from subprocess import call

#
#11 1  15 8  
#10 4  5  0  
#14 3  6  13 
#7  2  9  12 

debug=True
MAXSQUARES = 4
TOTALSQUARES = MAXSQUARES * MAXSQUARES
matrix = [0 for x in range(TOTALSQUARES)] 
targetV = 1
for x in range(TOTALSQUARES):
    matrix[x] = x
shuffle(matrix)

def swap(x,y):
    global matrix,  targetV
    if (((not checkZeroNeighbor(matrix[x])) and (not
        checkZeroNeighbor(matrix[y])))):
        return

    t = matrix[x]
    matrix[x] = matrix[y]
    matrix[y] = t
    try:
        if (debug):
            call(["clear"])
            print 'Unsolved: ', targetV
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
    return true
    
def returnUnsolved(target):
    global matrix
    for x in xrange(target-1,-1,-1):
        if matrix[x] != (x+1):
            return x+1
    return 0
def isSolvedAt(x):
    global matrix
    if x < 0 and val >= TOTALSQUARES:
        return False
    if matrix[x] == x+1:
        return True
    return False
def isSolved(val):
    global matrix
    if val < 1 and val >= TOTALSQUARES:
        return False
    if matrix[val-1] == val:
        return True
    return False

def checkZeroNeighbor(target):
    global matrix
    pos = matrix.index(target)
    if (row(pos-1) == row(pos) and
            matrix[pos-1] == 0):
        return True
    elif ((pos-MAXSQUARES) >= 0 and
            matrix[pos-MAXSQUARES] == 0):
        return True
    elif (row(pos+1) == row(pos) and 
            matrix[pos+1] == 0):
        return True
    elif ((pos+MAXSQUARES) < TOTALSQUARES and
            matrix[pos+MAXSQUARES] == 0):
        return True
    return False
def row(x):
    return x/MAXSQUARES
def col(x):
    return x % MAXSQUARES


def in_middleH(x,y,t):
    if (row(x) != row(y)):
        return False
    if (col(t) >= col(x) and col(t) <= col(y)):
        return True
    if (col(t) >= col(y) and col(t) <= col(x)):
        return True

def in_middleV(x,y,t):
    if (col(x) != col(y)):
        return False
    if (row(t) >= row(x) and row(t) <= row(y)):
        return True
    if (row(t) >= row(y) and row(t) <= row(x)):
        return True
    return False
def distance(x,y):
    global matrix
    return abs(row(x)-row(y))+abs(col(x)-col(y))
def isSolvedRoute(x,y):
    global matrix
    while row(x) != row(y):
        if (row(x) < row(y)):
            x += MAXSQUARES
        elif (row(x) < row(y)):
            x -= MAXSQUARES
        if isSolvedAt(x):
            return True
    while col(x) != col(y):
        if (col(x) < col(y)):
            x += 1
        elif (col(x) < col(y)):
            x -= 1
        if isSolvedAt(x):
            return True
    return False

def moveZeroNearTargetV(target):
    global matrix
    ret = False
    t = matrix.index(target)
    z = matrix.index(0)
    at = target-1
    if (row(t) > (row(at))):
        tg = t - MAXSQUARES
    elif (row(t) < (row(at))):
        tg = t + MAXSQUARES
    else:
        tg = t
        if (row(z) == row(t)):
            return moveZeroNearTargetH(target)
    if (isSolvedRoute(z,tg)):
        return moveZeroNearTargetH(target)
    if in_middleV(z,tg,t):
        if col(z+1) and (distance(target-1,z+1) <= distance(target-1,z-1)):
            swap(z,z+1)
        else:
            swap(z,z-1)
        return moveZeroNearTargetV(target)
    if (row(z) > row(tg)):
        while row(z) != row(tg):
            swap(z, z-MAXSQUARES)
            z = matrix.index(0)
        ret = True
    elif (row(z) < row(tg)):
        while row(z) != row(tg):
            swap(z, z+MAXSQUARES)
            z = matrix.index(0)
        ret = True
    else:
        ret = False

    while col(z) != col(tg):
        if (col(z) > col(tg)):
            swap(z,z-1)
        else:
            swap(z,z+1)
        z = matrix.index(0)
    return True

def rotate(z):
    global matrix
    while col(z):
        swap(z,z-1)
        z = matrix.index(0)
    assert(row(z))
    swap(z,z-MAXSQUARES)
    return

def moveZeroNearTargetH(target):
    global matrix
    t = matrix.index(target)
    z = matrix.index(0)
    at = target-1

    if (col(t) > (col(at))):
        tg = t - 1
    elif (col(t) < (col(at))):
        tg = t + 1
    else:
        tg = t
    if in_middleH(z,tg,t):
        if ((z+MAXSQUARES) < TOTALSQUARES): 
            swap(z,z+MAXSQUARES)
        elif (z-MAXSQUARES) >= 0: 
            swap(z,z-MAXSQUARES)
        else:
            assert(1)
        return moveZeroNearTargetH(target)

    if tg != t:
        if (col(z) > col(tg)):
            while col(z) != col(tg):
                swap(z,z-1)
                z = matrix.index(0)
        elif (col(z) < col(tg)):
            while col(z) != col(tg):
                swap(z,z+1)
                z = matrix.index(0)
    while row(z) != row(tg):
        if (row(z) > row(tg)):
            swap(z,z-MAXSQUARES)
        else:
            swap(z,z+MAXSQUARES)
        z = matrix.index(0)
    return True


def printMatrix():
    global matrix
    i = 0
    while i < TOTALSQUARES:
        if i % MAXSQUARES == 0:
            print ""
        print matrix[i],
        if (matrix[i] < 10):
            print "",
        i += 1
    print ""


def solve():
    global matrix, targetV
    if isComplete() == True:
        return
    target = 1
    while True:
        if isSolved(target):
            targetV = returnUnsolved(target)
            if targetV == 0:
                target = target + 1
                continue
            else:
                target = targetV
        targetV = target
        ret = moveZeroNearTargetV(target)
        if (distance(matrix.index(0), target-1) < 
                distance(matrix.index(target), target-1)):
            swap(matrix.index(0), matrix.index(target))




printMatrix()
solve()

