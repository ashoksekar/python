#!/usr/bin/python
num_of_test = 0 # number of test case (N)
debug = 1
num_P = 0
num_W = 0

def open_read_file():
    file_name="sample_input.txt"
    fin=open(file_name, 'r')
    return fin

fin = open_read_file()
num_of_test = int(fin.readline())
i = 0
while i < num_of_test:
    string = fin.readline().split()
    num_P = int(string[0])
    num_W = int(string[1])
    graph = dict()
    attr = []
    prev = []
    string = fin.readline().split()
    for x in range(num_P):
        graph[x] = []
        attr.append([0,0xffffffff])
        prev.append([])

    attr[0][1] = 0

    for x in range(num_W):
        s = string[x].split(',')
        m = int(s[0])
        n = int(s[1])
        graph[m].append(n)
        graph[n].append(m)
    
    lst = [0]
    while len(lst) > 0:
        m = lst.pop(0)
        for x in range(len(graph[m])):
            dest = graph[m][x]
            if attr[dest][0] == 0:
                lst.append(dest)
                if ((attr[m][1]+1) < attr[dest][1]):
                    attr[dest][1] = attr[m][1]+1
                    prev[dest] = [m]
                elif ((attr[m][1]+1) == attr[dest][1]):
                    if not (m in prev[dest]):
                        prev[dest].append(m)
        attr[m][0] = 1
    if (debug):
        print graph
        print attr
        print prev
    i += 1
    print 'Case #%d:' % i

