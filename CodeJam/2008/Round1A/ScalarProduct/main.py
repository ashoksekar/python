#!/usr/bin/python

num_of_test = 0 # number of test case (N)
num_n = 0 # number of search engine (S)
debug = 0

def mul(x,y):
    return x*y
def add(x,y):
    return x+y

def open_read_file():
    # file_name=raw_input()
    #file_name="sample_input.txt"
    file_name="A-large-practice.in"
    #file_name="A-small-practice.in"
    fin=open(file_name, 'r')
    return fin

fin = open_read_file()
num_of_test = int(fin.readline())
if debug:
    print 'num of test case: ', num_of_test
i = 0
while i < num_of_test:
    num_n = int(fin.readline())
    lists = []
    j = 0
    while j < 2:
        reverse = False
        lists.append(fin.readline().split())
        lists[j] = map(int, lists[j])
        if j:
            reverse = True
        lists[j].sort(reverse=reverse)
        j += 1
    if (debug):
        print lists
    total = reduce(add, map(mul, lists[0], lists[1]))
    print 'Case #%d: %d' % (i+1, total)
    i += 1
