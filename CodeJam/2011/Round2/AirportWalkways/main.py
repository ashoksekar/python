#!/usr/bin/python
num_of_test = 0 # number of test case (N)
debug = 0
num_X = 0
num_S = 0
num_R = 0
num_t = 0
num_N = 0
num_Bi = 0
num_Ei = 0
num_Wi = 0

def open_read_file():
    #file_name="sample_input.txt"
    #file_name="A-small-practice.in"
    file_name="A-large-practice.in"
    fin=open(file_name, 'r')
    return fin

fin = open_read_file()
num_of_test = int(fin.readline())
i = 0
while i < num_of_test:
    string = fin.readline().split()
    num_X = float(string[0])
    num_S = float(string[1])
    num_R = float(string[2])
    num_t = float(string[3])
    num_N = int(string[4])
    tot_m = 0
    time = 0.0000000
    tm = 0.0000000
    D = []
    for x in range(num_N):
    	string = fin.readline().split()
        num_Bi = (float(string[0]))
    	num_Ei = (float(string[1]))
    	num_Wi = (float(string[2]))
        dist = (num_Ei - num_Bi)
        D.append([dist, num_Wi])
        tot_m += dist
    if (debug):
        print 'X: %f S: %f R: %f t: %f N: %f tot: %f' % (num_X, num_S, num_R,
                num_t, num_N, tot_m)

    D.sort(key=lambda D: D[1], reverse=False)
    tm = (num_X-tot_m)/num_R
    if (num_t - tm) > 0:
        num_t -= tm
        time += tm
    else:
        tm = ((num_X-tot_m) - num_R*num_t)/num_S
        time += num_t
        time += tm
        num_t = 0

    if (debug):
        print 'tot: %f dist: %f time: %f num_t: %f' % (num_X, tot_m, time, num_t)
        print D
    num_X = tot_m 
    for x in range(num_N):
        dist = D[x][0]
        tm = (dist) / (D[x][1]+num_R)
        if (num_t - tm) > 0:
            num_t -= tm
            time += tm
        else:
            tm = (dist - (D[x][1]+num_R)*num_t) / (D[x][1]+num_S)
            time += num_t
            time += tm
            num_t = 0

    i += 1
    print 'Case #%d:' % i,
    print '%.20f' % time

