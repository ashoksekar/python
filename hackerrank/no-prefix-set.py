#!/usr/bin/python

debug = False
num_N = int(raw_input())

class node:
    ch = ''
    child = None
root = node()
root.child = []

def find_node(n, ch):
    for x in n.child:
        if x.ch == ch:
            return x
    return None
def enqueue_node(s):
    global root
    prev = root
    added = False
    for x in list(s):
        n = find_node(prev,x)
        if n == None:
            if ((prev != root) and (len(prev.child) == 0) 
                    and (added == False)) :
                if (debug):
                    print 1,s
                return s
            added = True
            n = node()
            n.ch = x
            n.child = []
            prev.child.append(n)
        prev = n
    if added == False:
        if (debug):
            print 2,s
        return s
    return None
        
for k in range(num_N):
    string = raw_input()
    s = enqueue_node(string)
    if s != None:
        print 'BAD SET'
        print s
        exit()
    else:
        if (debug):
            print s

print 'GOOD SET'




