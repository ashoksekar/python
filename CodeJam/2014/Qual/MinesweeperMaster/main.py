#!/usr/bin/python
import sys

num_of_test = 0 # number of test case (N)
num_R = 0
num_C = 0
num_M = 0
debug = 1
debug_xy = 0
matrix = []
mines = 0
def open_read_file():
    # file_name=raw_input()
    #file_name="sample_input.txt"
    #file_name="C-large-practice.in"
    file_name="C-small-practice.in"
    fin=open(file_name, 'r')
    return fin
def construct_matrix():
    global num_R, num_C, num_M
    global matrix
    x = 0
    matrix = []
    while x < num_R:
        matrix.append([0] * num_C)
        x += 1
    return
def find_zero(r, c):
    global num_R, num_C, num_M
    global matrix
    zeroes = 0
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if ((i < 0) or (j < 0)):
                continue
            if ((i >= num_R) or (j >= num_C)):
                continue
            if (matrix[i][j] == 0):
                zeroes += 1
    return zeroes
def find_max_zeroes():
    global num_R, num_C, num_M
    global matrix
    maxzero = 0
    maxzero_loc = (-1,-1)

    for i in range(num_R):
        for j in range(num_C):
            if matrix[i][j] == 0:
                if maxzero < find_zero(i,j):
                    maxzero = find_zero(i,j)
                    maxzero_loc = (i,j)
    return maxzero_loc

def print_format_matrix():
    global num_R, num_C, num_M
    global matrix
    x = y = 0
    loc = find_max_zeroes()
    while x < num_R:
        y = 0
        while y < num_C:
            if ((x,y) == loc):
                print 'c',
                sys.stdout.softspace=0
            elif (matrix[x][y] < 0):
                print '*',
                sys.stdout.softspace=0
            else:
                print '.',
                sys.stdout.softspace=0
            y += 1
        print 
        x += 1
    return

def print_matrix():
    global num_R, num_C, num_M
    global matrix
    x = y = 0
    while x < num_R:
        print '|',
        y = 0
        while y < num_C:
            if (matrix[x][y] < 0):
                print '%d' % matrix[x][y],
            else:
                print '%2d' % matrix[x][y],
            y += 1
        print '|'
        x += 1
    return
def are_neighbors(p1, p2):
    global num_R, num_C, num_M
    r = p1[0]
    c = p1[1]
    lst = []
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if ((i < 0) or (j < 0)):
                 continue
            if ((i >= num_R) or (j >= num_C)):
                continue
            lst.append((i,j))
    """
    if (debug_xy):
        print p1, p2, lst
    """
    return (p2 in lst)

def check_neighbor(lst, r,c):
    global num_R, num_C, num_M
    global matrix, debug_xy
    zlst = []
    #corner = 1
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if ((i < 0) or (j < 0)):
                continue
            if ((i >= num_R) or (j >= num_C)):
                continue
            if ((i,j) == (r,c)):
                continue
            if ((i,j) in lst) == True:
                continue
            #corner = 0
            if (matrix[i][j] == 0):
                zlst.append((i,j))
    if (debug_xy):
        print lst
        print (r,c),zlst
    for i in range(len(zlst)):
        ret = False
        for j in range(len(zlst)):
            if (i == j):
                if (len(zlst) == 1):
                    ret = True
                continue
            if (are_neighbors(zlst[i], zlst[j]) == True):
                ret = True
                break
        if (ret == False):
            return False
    if (len(zlst) != 0):
    #if (len(zlst) != 0 or corner):
        return True

    return False
def fix_pos(r,c):
    global mines, num_R, num_C, num_M
    global matrix, debug_xy
    is_mine = 0
    if (matrix[r][c] == -1):
        return
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if ((i < 0) or (j < 0)):
                continue
            if ((i >= num_R) or (j >= num_C)):
                continue
            if ((i,j) == (r,c)):
                continue
            if (matrix[i][j] == -1):
                is_mine = 1
                break;
    if (is_mine):
        matrix[r][c] = 1
    else:
        matrix[r][c] = 0
    return
def fix_box(r,c):
    global mines, num_R, num_C, num_M
    global matrix, debug_xy
    matrix[r][c] = 1
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if ((i < 0) or (j < 0)):
                continue
            if ((i >= num_R) or (j >= num_C)):
                continue
            fix_pos(i,j)
    return
def add_mine(r,c):
    global mines, num_R, num_C, num_M
    global matrix, debug_xy
    lst = []
    rlst = []
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if ((i < 0) or (j < 0)):
                continue
            if ((i >= num_R) or (j >= num_C)):
                continue
            lst.append((i,j))
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if ((i < 0) or (j < 0)):
                continue
            if ((i >= num_R) or (j >= num_C)):
                continue
            if ((i,j) == (r,c)):
                matrix[r][c] = -1
                continue
            if (matrix[i][j] == 0):
                matrix[i][j] = 1

    mines += 1
    if ((-1,-1) == (r,c)):
        debug_xy = 1
    else:
        debug_xy = 0
    i = r-1
    while i < (r+2):
        j = c-1
        while j < (c+2):
            if ((i < 0) or (j < 0)):
                j += 1
                continue
            if ((i >= num_R) or (j >= num_C)):
                j += 1
                continue
            if (debug_xy):
                print 'check %d' % (matrix[i][j]),
                print (i,j)
            if ((i,j) == (r,c)):
                j += 1
                continue
            if (matrix[i][j] == -1):
                j += 1
                continue
            if (check_neighbor(lst,i,j) == False):
                if (mines == (num_M)):
                    mines -= 1
                    matrix[r][c] = 1
                    fix_box(r,c)
                    return False
                if ((matrix[i][j] != -1) and 
                        (add_mine(i,j) == False)):
                    matrix[r][c] = 1
                    mines -= 1
                    if (len(rlst) != 0):
                        for x in rlst:
                            matrix[x[0]][x[1]] = 1
                            mines -= 1
                    fix_box(r,c)
                    if (len(rlst) != 0):
                        for x in rlst:
                            fix_box(x[0],x[1])
                    return False
                else:
                    rlst.append((i,j))
                    #print 'recurse ', (i,j)
                    """
                    if (mines == num_M):
                       print (i,j),(r,c)
                       assert(0)
                    """
                    i = r-1
                    j = c-1
                    continue
            j += 1
        i += 1
    return True
def fill_mines():
    global num_R, num_C, num_M
    global matrix, mines, rlst
    i = 0
    j = 0
    # 0 - East
    # 1 - South
    # 2 - West
    # 3 - North
    direction = 0;
    loop = 0
    mines = 0
    if (num_M == (num_R * num_C - 1)):
        for i in range(num_R):
            for j in range(num_C):
                if ((i,j) == (0,0)):
                    continue
                matrix[i][j] = -1
        mines = num_M
        return True
    while True:
        rlst = []
        if (mines == num_M):
            return True
        if (matrix[i][j] != -1):
            if (add_mine(i,j) == True):
                if (mines == num_M):
                    return True
        if (direction == 0):
            if ((j+1) < (num_C-loop)):
                j += 1
            else:
                direction = 1
                if ((i+1) >= (num_R-loop)):
                    break
                i += 1
        elif (direction == 1):
            if ((i+1) < (num_R-loop)):
                i += 1
            else:
                direction = 2
                if ((j-1) < loop):
                    break
                j -= 1
        elif (direction == 2):
            if ((j-1) >= loop):
                j -= 1
            else:
                direction = 3
                if ((i-1) <= loop):
                    break
                i -= 1
        elif (direction == 3):
            if ((i-1) > loop):
                i -= 1
            else:
                direction = 0
                loop += 1
                if ((j+1) >= (num_C - loop)):
                    break
                j += 1
    return False

    
fin = open_read_file()
num_of_test = int(fin.readline())
if debug:
    print 'num of test case: ', num_of_test
i = 0
while i < num_of_test:
    string = fin.readline().split()
    num_R = int(string[0])
    num_C = int(string[1])
    num_M = int(string[2])
    construct_matrix()
    mines = 0
    if (num_M != 0):
        fill_mines()
    if (debug):
        print 'Case #%d %d %d %d %d' % ((i+1), num_R, num_C, num_M, mines)
    else:
        print 'Case #%d:' % (i+1)
    if (mines == num_M):
        print_format_matrix()
    else:
        print 'Impossible'
        if (debug):
            print_format_matrix()
    i += 1
