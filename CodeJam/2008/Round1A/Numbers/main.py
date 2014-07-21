#!/usr/bin/python

import math

num_of_test = 0 # number of test case (N)
debug = 0

def open_read_file():
    # file_name=raw_input()
    #file_name="sample_input.txt"
    #file_name="C-large-practice.in"
    file_name="C-small-practice.in"
    fin=open(file_name, 'r')
    return fin

def custom_power(x, y):
    i = 0
    result = 1
    while i < y:
        result = float(result) * float(x)
        result = float(result) % 1000.0
        i += 1
    return result

fin = open_read_file()
num_of_test = int(fin.readline())
if debug:
    print 'num of test case: ', num_of_test

i = 0
while i < num_of_test:
    num_n = int(fin.readline())
    result = custom_power(3+math.sqrt(5), num_n)
    if (debug):
        print result
    print 'Case #%d: %03d' % (i+1, int(result))
    i += 1

