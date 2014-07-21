#!/usr/bin/python
import string

num_of_test = 0 # number of test case (N)
num_tt = 0 # Turn around time (T)
num_NA = 0 # number of trips from A to B (NA)
num_NB = 0 # number of trips from B to A (NB)
debug = 0

def open_read_file():
    # file_name=raw_input()
    file_name="B-large-practice.in"
    #file_name="B-small-practice.in"
    #file_name="sample_input.txt"
    fin=open(file_name, 'r')
    return fin


nb_list = []
na_list = []
depart=0
arrival=1

def sort_key_func(lst):
    global depart
    return lst[depart]

def prune_dup(val, is_na):
    global nb_list, na_list
    global num_tt
    global depart, arrival

    x = 0
    if is_na:
        while x < len(na_list):
            if na_list[x][depart] >= (val+num_tt):
                val = na_list[x][arrival]
                del na_list[x]
                prune_dup(val, 0)
                return 1
            x += 1
    else:
        while x < len(nb_list):
            if nb_list[x][depart] >= (val+num_tt):
                val = nb_list[x][arrival]
                del nb_list[x]
                prune_dup(val, 1)
                return 1
            x += 1
    return 0

fin = open_read_file()
num_of_test = int(fin.readline())
if debug:
    print 'num of test case: ', num_of_test
i = 0
while i < num_of_test:
    num_tt = int(fin.readline())
    if debug:
        print 'Turn around time: ', num_tt
    string = fin.readline()
    list = string.split()
    num_NA=int(list[0])
    num_NB=int(list[1])
    if debug:
        print "NA: ", num_NA, " NB: ", num_NB
    na = 0
    na_list = []
    while na < num_NA:
        string = fin.readline()
        list=string.split()
        minutes=list[0].split(':')
        mins_dep = int(minutes[0])*60+int(minutes[1])
        minutes=list[1].split(':')
        mins_arr = int(minutes[0])*60+int(minutes[1])
        na_list.append([mins_dep, mins_arr])
        na += 1
    nb = 0
    nb_list = []
    while nb < num_NB:
        string = fin.readline()
        list=string.split()
        minutes=list[0].split(':')
        mins_dep = int(minutes[0])*60+int(minutes[1])
        minutes=list[1].split(':')
        mins_arr = int(minutes[0])*60+int(minutes[1])
        nb_list.append([mins_dep, mins_arr])
        nb += 1
    na_list.sort(key=sort_key_func)
    nb_list.sort(key=sort_key_func)
    if (debug):
        print na_list
        print nb_list
    y = 0
    while y < len(na_list):
        prune_dup(na_list[y][arrival], 0)
        y += 1
    y = 0
    while y < len(nb_list):
        val = nb_list[y][arrival]
        x = 0
        while x < len(na_list):
            if na_list[x][depart] >= (val+num_tt):
                del na_list[x]
                break
            x += 1
        y += 1

    print 'Case #%d: %d %d' % (i+1,len(na_list),len(nb_list))
    i += 1
fin.close()
