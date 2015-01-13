#!/usr/bin/python
num_of_test = 0 # number of test case (N)
debug = 0
num_P = 0
num_W = 0
gown = 0
gthtn = 0
th = []

class node(object):
    """ data = n
        child = child nodes """
    def __init__(self, data = 0, child = [], parent = []):
        self.data = data
        self.child = child
        self.parent = parent
    def __str__(self):
        return '%d' % self.data
    def find_node(root, data):
        items = [root]
        while len(items):
            pt = items.pop()
            if pt.data == data:
                return pt
            items = items + pt.child
        return None

def open_read_file():
    file_name="D-small-practice.in"
    #file_name="D-large-practice.in"
    #file_name="sample_input.txt"
    fin=open(file_name, 'r')
    return fin

def find_gthtn(node, parent):
    global gthtn
    global graph
    global num_P

    if node.data == 0:
        l = []
        tmp = parent + [node]
        for z in tmp:
            assert (z.data < num_P)
            if z.data != 1:
                l = l + graph[z.data]
        l = list(set(l))
        if 0 in l:
            l.remove(0)
        assert(1 in l)
        if gthtn < len(l):
            if (debug):
                for x in parent+[node]:
                    print x,
                print 
                print l
            gthtn = len(l)

    items = node.child[:]
    while len(items):
        pt = items.pop()
        find_gthtn(pt, parent + [node]) 

def find_thtn(ptv):
    global graph, prev
    global gown, gthtn
    global i

    root = node(data = ptv, child = [], parent = [])
    items = [root]
    while len(items):
        pt = items.pop(0)

        for z in prev[pt.data]:
            n = node.find_node(root, z)
            if (n == None):
                n = node(data = z, child = [], parent = [])
            #n.parent = pt.parent + [pt]
            items.append(n)
            pt.child.append(n)
            if (debug):
                print 'pt:' ,pt, 'ptprev:', prev[pt.data], 'n:', n, "nprev:", prev[n.data]
                #print 'pt:', pt, 'n:', n, 'prev:', prev[pt.data], 'parent:', 
                #for x in n.parent:
                #    print x, 
                #print 
    find_gthtn(root, [])

def find_own(pt):
    global graph, prev
    global gown, gthtn
    global i

    own = 0
    while True:
        if (pt != 1) and (pt != 0):
            own += 1
        pt = prev[pt][-1]
        if pt == 0:
            break
    gown = own

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
    gown = 0
    gthtn = 0
    string = fin.readline().split()
    #if i == 5:
    #    debug = 1
    #else:
    #    debug = 0
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

    for x in range(num_P):
        graph[x].sort()
    
    lst = [0]
    while len(lst) > 0:
        m = lst.pop(0)
        if attr[m][0] != 0:
            continue
        for x in range(len(graph[m])):
            dest = graph[m][x]
            if (attr[dest][0] == 0):
                lst.append(dest)
                if ((attr[m][1]+1) < attr[dest][1]):
                    attr[dest][1] = attr[m][1]+1
                    prev[dest] = [m]
                elif ((attr[m][1]+1) == attr[dest][1]):
                    if not (m in prev[dest]):
                        prev[dest].append(m)
                else:
                    continue
        attr[m][0] = 1
    find_own(1)
    find_thtn(1)
    if (debug):
        print gown,gthtn
    i += 1
    gthtn -= gown
    print 'Case #%d: %d %d' % (i, gown, gthtn)

