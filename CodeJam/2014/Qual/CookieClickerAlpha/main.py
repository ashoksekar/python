#!/usr/bin/python

num_of_test = 0 # number of test case (N)
num_C = 0.0 
num_F = 0.0
num_X = 0.0
cps = 2.0
tot_time = 0.0
debug = 0

def open_read_file():
    # file_name=raw_input()
    #file_name="sample_input.txt"
    file_name="B-large-practice.in"
    #file_name="B-small-practice.in"
    fin=open(file_name, 'r')
    return fin
def buy_farm():
    global num_C, num_F, num_X, cps
    global tot_time
    tot_time += (num_C / cps)
    cps += num_F
    return

fin = open_read_file()
num_of_test = int(fin.readline())
if debug:
    print 'num of test case: ', num_of_test
i = 0
while i < num_of_test:
    string = fin.readline().split()
    num_C = float(string[0])
    num_F = float(string[1])
    num_X = float(string[2])
    cps = 2.0
    tot_time = 0.0
    if (debug):
        print num_C, num_F, num_X
    while True:
        if (((num_X)/(cps+num_F)) < ((num_X-num_C)/cps)):
            if (debug):
                print (num_X/(cps+num_F)), ((num_X-num_C)/cps)
            buy_farm()
        else:
            tot_time += (num_X/cps)
            break
    i += 1
    print 'Case #%d: %.06f' % (i, tot_time)

