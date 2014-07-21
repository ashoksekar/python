#!/usr/bin/python

num_of_test = 0 # number of test case (N)
num_of_se = 0 # number of search engine (S)
num_of_query = 0 # number of Queries (Q)
debug = 0

def open_read_file():
    # file_name=raw_input()
    file_name="A-large-practice.in"
    #file_name="A-small-practice.in"
    fin=open(file_name, 'r')
    return fin
def parse_dict_list(se_dict, se_list, val):
    j = 0
    switch = 0
    big = 0
    while (1):
        for x in se_list:
            if (len(se_dict[x]) == 0):
                return switch
            pos = se_dict[x][j]
            if (pos >  big):
                big = pos
        switch += 1
        if debug:
            print se_list
            print se_dict
        for x in se_list:
            y = 0
            if (se_dict[x][-1] < big):
                return switch
            while y < len(se_dict[x]):
                pos = se_dict[x][y]
                if (pos >= big):
                    del se_dict[x][:y]
                    break
                y += 1
            
    return switch

fin = open_read_file()
num_of_test = int(fin.readline())
if debug:
    print 'num of test case: ', num_of_test
i = 0
while i < num_of_test:
    num_of_se = int(fin.readline())
    if debug:
        print 'num of search engine: ', num_of_se
    se_dict = dict()
    j = 0
    se_list = []
    while j < num_of_se:
        se_str = fin.readline()
        se_dict[se_str] = []
        se_list.append(se_str)
        j += 1
    if debug:
        print 'dict is now: ', se_dict
    num_of_query=int(fin.readline())
    j = 0
    while j < num_of_query:
        query_str = fin.readline()
        se_dict[query_str].append(j)
        j += 1
    val = num_of_query
    for j in se_list:
        length = len(se_dict[j])
        if (length < val):
            val = length
    if debug:
        print 'val: ', val
        print 'dict is now: ', se_dict
    switch = parse_dict_list(se_dict, se_list, val)
    print 'Case #%d: %d' % (i+1,switch)
    i += 1
fin.close()
