#!/usr/bin/python

import networkx as nx
import matplotlib.pyplot as plt

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
    def __init__(self, data = 0, child = [], parent = [], level = 0):
        self.data = data
        self.child = child
        self.parent = parent
        self.level = level
    def __str__(self):
        return '%d' % self.data
    def find_node(root, data):
        items = [root]
        while len(items):
            pt = items.pop()
            if pt.data == data:
                return pt
            for x in pt.child:
                if not(x in items):
                    items.append(x)
        return None
    def print_node(root):
        items = [root]
        while len(items):
            pt = items.pop(0)
            print "pt:", pt, "child:",
            for x in pt.child:
                print x,
                if not(x in items):
                    items.append(x)
            print
        return 


def open_read_file():
    #file_name="D-small-practice.in"
    file_name="D-large-practice.in"
    #file_name="sample_input.txt"
    fin=open(file_name, 'r')
    return fin

def find_gthtn(node, parent, ttn):
    global gthtn
    global graph
    global num_P
    global i

    if 1 in ttn:
        l = ttn 
        l = list(set(l))
        if 0 in l:
            l.remove(0)
        assert(1 in l)
        if gthtn < len(l):
            gthtn = len(l)

    items = node.child[:]
    ln1 = []
    big = 0
    for x in items:
        t = ttn+graph[x.data]+graph[parent.data]
        if len(prev[x.data]) != 0:
            for y in prev[x.data]:
                t1 = t + graph[y]
                t2 = list(set(t1))
                ln1.append(len(t2))
                if big < len(t2):
                    big = len(t2)
        else:
            t1 = list(set(t))
            ln1.append(len(t1))
            if big < len(t1):
                big = len(t1)


    ii = 0
    items1 = []
    out_break = 0
    for x in items:
        if len(prev[x.data]) != 0:
            for y in prev[x.data]:
               if ln1[ii] == big:
                   items1.append(x)
                   #out_break = True
                   break
               ii += 1
            if out_break:
                break
        else:
            if ln1[ii] == big:
                items1.append(x)
                break
            ii += 1
    for pt in items1:
        find_gthtn(pt, node, list(set(ttn + graph[pt.data]))) 

def find_thtn(ptv):
    global graph, prev
    global gown, gthtn
    global i

    nodeg = []
    for x in range(400):
        nodeg.append(None)

    root = node(data = ptv, child = [], parent = [], level = 1)
    G = nx.Graph()
    items = [root]
    while len(items):
        pt = items.pop(0)

        for x in graph[pt.data]:
            if not ((pt.data, x) in G.edges()):
                G.add_edge(pt.data, x, color = 'blue')
        for z in prev[pt.data]:
            n = nodeg[z] #node.find_node(root, z)
            if (n == None):
                n = node(data = z, child = [], parent = [])
                nodeg[z] = n
                n.level = pt.level + 1
                items.append(n)
            G.add_edge(pt.data, n.data, color = 'red')
            pt.child.append(n)
            assert (n.level == (pt.level + 1))
            if (debug):
                print 'pt:' ,pt, 'ptprev:', prev[pt.data], 'n:', n, "nprev:", prev[n.data]
                #print 'pt:', pt, 'n:', n, 'prev:', prev[pt.data], 'parent:', 
                #for x in n.parent:
                #    print x, 
                #print 
    if (debug):
        color = nx.get_edge_attributes(G,'color')
        colors = []
        for x in color:
            colors.append(color[x])
        print colors
        nx.draw_networkx(G, pos=nx.shell_layout(G), edge_color=colors)
        plt.axis('on')
        plt.show()
    find_gthtn(root, root, graph[root.data])

def find_own(pt):
    global graph, prev
    global gown, gthtn
    global i

    own = 0
    while True:
        if (pt != 1) and (pt != 0):
            own += 1
        pt = prev[pt][-1]
        if pt == 1:
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

    attr[1][1] = 0

    for x in range(num_W):
        s = string[x].split(',')
        m = int(s[0])
        n = int(s[1])
        graph[m].append(n)
        graph[n].append(m)

    for x in range(num_P):
        graph[x].sort()
    
    lst = [1]
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
    find_own(0)
    find_thtn(0)
    if (debug):
        print gown,gthtn
    i += 1
    gthtn -= gown
    print 'Case #%d: %d %d' % (i, gown, gthtn)

