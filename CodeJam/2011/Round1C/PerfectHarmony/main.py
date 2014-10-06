#!/usr/bin/python

num_of_test = 0 # number of test case (N)
debug = 0
num_N = 0
num_L = 0
num_H = 0

def open_read_file():
    # file_name=raw_input()
    #file_name="sample_input.txt"
    #file_name="C-small-practice.in"
    file_name="C-large-practice.in"
    fin=open(file_name, 'r')
    return fin
def find_hfreq():
    global num_N, num_L, num_H
    global freq
    i = num_L
    while i <= num_H:
        ans = i
        for k in freq:
            if (k > i):
                ans = 0
                break
            elif ((k < i) and (i % k)):
                ans = 0
                break
        if (ans):
            return ans
        i += 1
    return 0

fin = open_read_file()
num_of_test = int(fin.readline())
i = 0
while i < num_of_test:
    string = fin.readline().split()
    num_N = int(string[0])
    num_L = int(string[1])
    num_H = int(string[2])
    freq = []
    string = fin.readline().split()
    for k in range(num_N):
        freq.append(int(string[k]))
    freq.sort()
    val = find_hfreq()
    i += 1
    if val:
        print 'Case #%d: %d' % (i, val)
    else:
        print 'Case #%d: NO' % i

